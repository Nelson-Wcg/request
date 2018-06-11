# encoding: utf-8

import time
import os


class Wechat():

    def __init__(self):
        # 关闭微信
        os.system("adb shell am force-stop com.tencent.mm")
        time.sleep(1)
        # 启动微信
        os.system("adb shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI")
        time.sleep(3)

    def request_message(self, message):
        os.system("adb shell input tap 540 260")
        time.sleep(1)
        os.system("adb shell input tap 360 1840")
        time.sleep(1)
        os.system("adb shell input text " + message)
        time.sleep(1)
        os.system("adb shell input tap 1016 1010")
        time.sleep(1)
        os.system("adb shell input tap 760 830")
        time.sleep(1)
        os.system("adb shell input tap 77 140")