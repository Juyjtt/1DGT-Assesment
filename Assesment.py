# Define the safe speed and the finish word
SAFE_SPEED = 10
END_WORD = 'OVER'

# Ask the user for the input
speed = float(input('Input descent speed in m/s: '))

# Getting user's speed, make sure it isn't empty
while speed == '':
    print('DId you type anything?')
    speed = float(input('Input descent speed in m/s: '))
while not speed.lstrip('-').isnumeric():
    print('That is not a number, please try again')
    speed = float(input('Input descent speed in m/s: '))
speed = int(speed)
while True:
    try:
        speed = float(input('Input descent speed in m/s: '))
        if speed != END_WORD:
            break
        except ValueError:
            print('Invalid speed')
            
       

  


        