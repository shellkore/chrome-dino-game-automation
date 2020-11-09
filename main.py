import pyautogui
from PIL import Image
import pyscreenshot as ImageGrab
import time
import numpy as np

def collisionCheck(data):
	#for dragon
	for i in range(340,400):
		for j in range(370,400):
			if data[i,j]<100:
				pyautogui.press('down')
				return
	# cactus
	for i in range(340,520):
		for j in range(410,450):
			if data[i,j]<100:
				pyautogui.press('up')
				return	

	return

def rectangleDraw():
	time.sleep(3)
	# for dragon
	for i in range(340,400):
		for j in range(370,400):
			data[i,j] = 100
	#for cactus
	im = ImageGrab.grab().convert('L')
	data = im.load()
	for i in range(340,520):
		for j in range(410,450):
			data[i,j] = 0


	im.show()

def play():
	time.sleep(4)
	print("pressing up key.......")
	pyautogui.press('up')
	time.sleep(2)
	while True:
		im = ImageGrab.grab().convert('L')
		data = im.load()
		collisionCheck(data)

if __name__ == '__main__':
	play()	
	# rectangleDraw()
	