# usr/bin/python3
# author: Shiqin Zhang
# Date: 2022/4/11 15:09
import os
import win32gui  # pywin32-221.win-amd64-py3.7.exe
import win32con
from ctypes import *
import win32clipboard as w
import time
from PIL import Image  # pip install pillow
from PIL import ImageGrab
import numpy as np
import cv2
import pyautogui
import time
import random


def doubleclick(self, x, y):
    pyautogui.moveTo(x, y, 0.5, pyautogui.easeInQuad)
    pyautogui.PAUSE = 0.5
    pyautogui.doubleClick(button='left')


pyautogui.doubleClick(1633, 43)  # 打开窗口
time.sleep(20)
beg = time.time()
debug = False
# img = ImageGrab.grab(bbox=(250, 161, 1141, 610))
img = ImageGrab.grab()
end = time.time()
img.save('success.jpg')
time.sleep(5)
pyautogui.doubleClick(1856, 869)  # 打开窗口
time.sleep(5)


# 发送图片
def setImage(imgpath):
    im = Image.open(imgpath)
    im.save('1.bmp')
    aString = windll.user32.LoadImageW(0, r"1.bmp", win32con.IMAGE_BITMAP, 0, 0, win32con.LR_LOADFROMFILE)

    print(aString)
    if aString != 0:  ## 由于图片编码问题  图片载入失败的话  aString 就等于0
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_BITMAP, aString)
        w.CloseClipboard()

    # 指定窗口（QQ昵称备注）


def sendByUser(uname):
    hwnd = win32gui.FindWindow('TXGuiFoundation', uname)
    # hwnd = win32gui.FindWindow('ChatWnd', uname)
    win32gui.SendMessage(hwnd, 258, 22, 2080193)
    win32gui.SendMessage(hwnd, 770, 0, 0)
    win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


setImage('success.jpg')
sendByUser('名字')
