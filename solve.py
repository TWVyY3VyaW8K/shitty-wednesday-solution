#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui
import time
import os
import subprocess

pyautogui.FAILSAFE = False

IMAGES_BASE_DIR = 'script_gfx'

IMAGES = {
		"M": ["down_0_test.png", 'down'],
		"F": ["up_0_test.png", 'up']
		}

TARGET = 'mydude.exe'

JUMP_THRESHOLD = 645 #px

def imageFullPath(filename):
	return os.path.join(IMAGES_BASE_DIR, filename)

def printBlockPosition(filename, name, screen_region):
	block_pos = pyautogui.locateCenterOnScreen(imageFullPath(filename), region = screen_region)#, confidence = 0.9)
	if not block_pos:
		return False
	print("%s block position: x = %i, y = %i" % (name, block_pos.x, block_pos.y))
	return block_pos.x, block_pos.y

def jump(control):
	key = 'down' if control == 'down' else 'up'
	pyautogui.keyDown(key)
	time.sleep(0.5)
	pyautogui.keyUp(key)
	print('KEY %s' % key)

subprocess.Popen(TARGET)
time.sleep(2)

while True:
	interested_region = pyautogui.locateOnScreen(imageFullPath('interested_region_1.png'), confidence = 0.7)
	if interested_region:
		break
	else:
		time.sleep(1)

start_button = pyautogui.locateCenterOnScreen(imageFullPath('start_button.png'))
pyautogui.moveTo(start_button)
pyautogui.click()
pyautogui.moveTo(0, 0)

while True:
	for key, value in IMAGES.items():
		block_pos = printBlockPosition(value[0], key, interested_region)
		if not block_pos:
			continue
		while True:
			if block_pos[0] < JUMP_THRESHOLD:
				jump(value[1])
				break
			block_pos = printBlockPosition(value[0], key, interested_region)
			if not block_pos:
				break
	#time.sleep(0.3)
