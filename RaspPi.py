import portableGpio
import RPi.GPIO as gpio

class GPIO:
    def __init__(self):
        pass

    def init(self):
        gpio.setmode(gpio.BCM)

    def create_pin(self, pin, direction):
        libDir = None
        if direction == portableGpio.IN:
            libDir = gpio.IN
        elif direction == portableGpio.OUT:
            libDir = gpio.OUT

        gpio.setup(pin, libDir)
        return GpioPin(pin)

class GpioPin:
    def __init__(self, pin):
        self.pin = pin

    def set(self, value):
        gpio.output(self.pin, value)

    def get(self):
        return gpio.input(self.pin)
