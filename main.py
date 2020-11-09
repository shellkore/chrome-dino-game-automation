import pyautogui
from PIL import Image
import pyscreenshot as ImageGrab
import time
import numpy as np

def isCactus(data):
	for i in range(420,580):
		for j in range(430,450):
			if data[i,j]<100:
				return True
	return False

def isBird(data):
	for i in range(310,380):
		for j in range(380,410):
			if data[i,j]<100:
				return True
	return False

def collisionCheck(data):
	# cactus
	for i in range(420,580):
		for j in range(430,450):
			if data[i,j]<100:
				return ('up')

	#bird
	for i in range(360,400):
		for j in range(380,410):
			if data[i,j]<100:
				return('down')

	return False

def rectangleDraw():
	time.sleep(3)
	im = ImageGrab.grab().convert('L')
	data = im.load()
	for i in range(310,380):
		for j in range(380,410):
			data[i,j] = 0
	im.show()

def play():
	print("pressing up key.......")
	pyautogui.press('up')
	time.sleep(3)
	while True:
		im = ImageGrab.grab().convert('L')
		data = im.load()
		keyToPress = (collisionCheck(data))
		if keyToPress != False:
			pyautogui.press(keyToPress)
		# if isCactus(data):
		# 	pyautogui.press('up')
		# if isBird(data):
		# 	pyautogui.press('down')

if __name__ == '__main__':
	play()	
	# rectangleDraw()
	