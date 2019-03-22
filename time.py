import random, time, math
def slot():
	return random.randint(0,9)
def generate_slots():
	return [slot(), slot(), slot(), slot()]
def show_slots():
	print(slots[0], slots[1], slots[2], slots[3], end='\r')
slots = []
won = False
current_time = 0
while not won:
	slots = generate_slots()
	won = slots[0] == slots[1] and slots[0] == slots[2] and slots[0] == slots[3]
	show_slots()
	time.sleep(0.1)
	current_time += 0.1
time.sleep(0.1)
for x in range(3):
	print('       ', end='\r')
	time.sleep(0.3)
	show_slots()
	time.sleep(0.3)
print('\nYou won in ' + str(round(current_time, 1)) + ' seconds')