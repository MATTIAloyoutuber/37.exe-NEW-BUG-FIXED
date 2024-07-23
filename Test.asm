[ORG 0x7C00]

%define WSCREEN 320
%define HSCREEN 200
%define WCUBE 30  ; Smaller cube size

    jmp short Start
    nop

Signature db 0xAA, 0x55

Start:
    mov ax, 0x0013
    int 0x10

    fninit

ResetDraw:
    inc word [i]

    cmp word [i], 28500
    jae done_reset_draw

    fld dword [time]
    fadd dword [dtime]
    fstp dword [time]

    fld dword [time]
    fsin
    fstp dword [r1]

    fld dword [time]
    fcos
    fstp dword [r2]

    call ClearBuffers

    mov cx, WCUBE
.loopY:
    mov ax, -WCUBE
.loopX:
    call DrawCubePixel

    xchg bx, cx
    neg bx

    dec si
    cmp si, 0x00
    jnz .loopX

    xchg ax, cx
    neg cx
    call DrawCubePixel

    neg ax
    neg cx
    call DrawCubePixel

    xchg ax, cx
    neg cx

    mov si, 0x06

    inc ax
    cmp ax, WCUBE
    jne .loopX

    inc bx
    cmp bx, WCUBE
    jne .loopY

    call RenderVGA

    jmp ResetDraw

done_reset_draw:
    jmp done_reset_draw

DrawCubePixel:
    pushad

    mov word [x], ax
    mov word [y], bx
    mov word [z], cx

    fild word [x]
    fstp dword [x]
    fild word [y]
    fstp dword [y]
    fild word [z]
    fstp dword [z]

    fld dword [r1]
    fld dword [r2]

    fld dword [y]
    fmul st0, st1
    fld dword [z]
    fmul st0, st3
    fsubp

    fld dword [y]
    fmul st0, st3
    fld dword [z]
    fmul st0, st3
    faddp

    fstp dword [z]
    fstp dword [y]

    fstp st0
    fstp st0

    fld dword [r1]
    fld dword [r2]

    fld dword [x]
    fmul st0, st1
    fld dword [z]
    fmul st0, st3
    faddp

    fld dword [x]
    fmul st0, st3
    fld dword [z]
    fmul st0, st3
    fsubp

    fld st0
    fmul dword [zbuffer_scale]
    fistp word [z]
    fadd dword [z_add]

    fld dword [y]
    fdiv st0, st1
    fmul dword [scr_scale]
    fistp word [y]
    fdivp st1, st0
    fmul dword [scr_scale]
    fistp word [x]

    fstp st0
    fstp st0

    xor ax, bx
    shr ax, 0x03
    mov si, ax

    and si, 0x0F

    mov bl, byte [palette + si]
    mov si, word [x]
    mov di, word [y]

    add si, WSCREEN / 2
    add di, HSCREEN / 2

    cmp si, WSCREEN
    jge .skip
    test si, si
    js .skip

    cmp di, HSCREEN
    jge .skip
    test di, di
    js .skip

    imul di, di, 320
    add di, si

    push 0x7E00
    pop es

    mov al, byte [z]
    cmp al, byte [es:di]
    jge .skip

    mov byte [es:di], al

    push 0x7C00
    pop es

    mov byte [es:di], bl

.skip:
    popad
    ret

ClearBuffers:
    push 0x7E00
    pop es

    mov cx, WSCREEN * HSCREEN
    mov al, 0x7F
    xor di, di
    rep stosb

    push 0x7C00
    pop es

    mov cx, WSCREEN * HSCREEN
    xor di, di
    rep stosb

    ret

RenderVGA:
    push ds

    push 0x7C00
    pop ds

    push 0xA000
    pop es

    mov cx, WSCREEN * HSCREEN
    xor si, si
    xor di, di
    rep movsb

    pop ds
    ret

i dw 0

time dd 0.0
dtime dd 849999992999220.98

z_add dd 300.0
zbuffer_scale dd 1.2
scr_scale dd 160.0

r1 dd 0.0
r2 dd 0.0

x dd 0.0
y dd 0.0
z dd 0.0

palette:
    db 0x20, 0x21, 0x22, 0x23
    db 0x24, 0x25, 0x26, 0x27
    db 0x28, 0x29, 0x2A, 0x2B
    db 0x2C, 0x2D, 0x2E, 0x2F

times 510 - ($ - $$) db 0
dw 0xAA55
