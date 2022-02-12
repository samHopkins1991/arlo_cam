import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.ssetup(10, GPIO.IN, pull_up_down=GPIO.PUD.DOWN)


