# Importing libraries
import SDL_Pi_HDC1080
import sys

# Setting main path to HDC1080
sys.path.append('./SDL_Pi_HDC1080_Python3')
hdc1080 = SDL_Pi_HDC1080.SDL_Pi_HDC1080()

def HDCtemp(roundto):
	temperature = round(hdc1080.readTemperature(), roundto)
	return temperature

<<<<<<< HEAD
"""
# Setting counter in 0 value
HH = 0
MM = 0
SS = 0
"""
def initHDC():
	# Main loop
	while True:
	"""
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		if SS == 60:
			MM += 1
			SS = 0
		elif MM == 60:
			SS = 0
			HH += 1
			MM = 0
	"""
		# Getting temperature and humidity from methods
		temperature = round(hdc1080.readTemperature(), 1)
		humidity = round(hdc1080.readHumidity(), 1)
	"""
		with open('HDC-1080.csv', 'a+', newline='') as file:
			writer = csv.writer(file)
			writer.writerow([current_time, hdc1080.readTemperature(), hdc1080.readHumidity()])
	"""
		# Printing without color
		outTemp = (f'Temperature = {temperature} C°')
		outHum = (f'Humidity = {humidity} %')
		return outTemp, outHum

		# Upping the counter
		# SS += 1
		time.sleep(1)

		return temperature, humidity
=======
def HDChum(roundto):
	humidity = round(hdc1080.readHumidity(), roundto)
	return humidity
>>>>>>> 3065fde40c47b1c5c8e1a3728286a0aad92293b6
