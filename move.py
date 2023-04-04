import threading
from time import sleep
import pyautogui
import random
import math


class Move:
	def __init__(self):
		#Lock the thread
		self.lock = threading.Lock()
		#Center of the screen
        #TODO change this to be dynamic
		self.screen_center = [512, 284]
		print("Thread started MOVE")


		
	def nearest_object(self):
		dictionary = {}
		for i in range(len(self.centers)):
			object_location = self.centers[i]
			#Calculate distance between an object and the character
			distance = math.dist(object_location, self.screen_center)
			#Add result to dictionary
			dictionary[i] = distance 

		#print(dictionary)
		sort_dictionary = sorted(dictionary, key=dictionary.get, reverse=False)
		closest_object = self.centers[sort_dictionary[0]]
		return closest_object

	#Move player to mine rock
	def go_to(self):
		b = 0
        #TODO change this to be dynamic this is not fucking random
		rand_pos = [[660, 500], [424, 226]]

		if len(self.centers)>0:
			
			#Find the closest object to the player
			closest_object = self.nearest_object()
			
			#Display moving position
			print(f"Moving to: {closest_object[0]}, {closest_object[1]}")

			#Action 1 (Move mouse)
			pyautogui.moveTo(closest_object[0],closest_object[1],duration=0.1)
			print("click")
			#Action 2 (Movement click)
			pyautogui.click(button="left")
			sleep(0.1)

		else:
			print("No results")
			#Choose "random" position to move
			b = random.randint(0,1)
			
			#Display moving position
			print(f"Stuck, moving to: {rand_pos[b][0]}, {rand_pos[b][1]}")
			
			#Action 1 (Move mouse)
			pyautogui.moveTo(rand_pos[b][0],rand_pos[b][1],duration=0.1)
			print("click")

			
			#Action 2 (Movement click)
			pyautogui.click(button="left")
			sleep(0.1)
			
			#Reset var
			b = 0

    #Thread Functions
	def start(self):
		print("Thread started")
		self.stopped = False
		self.state = 0
		self.t = threading.Thread(target=self.run)
		self.t.start()
    
	def update(self, centers, bot_status):
		print(f"Updating with centers: {centers} and bot_status: {bot_status}")
		if bot_status==True:
			self.state = 1
		elif bot_status==False:
			self.state = 0
		self.centers = centers


	def stop(self):
		self.stopped = True
		print("Terminating...")


	def run(self):
		while not self.stopped:
			if self.state == 0:
				sleep(0.1)

			elif self.state == 1:
				self.lock.acquire()
				self.go_to()
				self.lock.release()
