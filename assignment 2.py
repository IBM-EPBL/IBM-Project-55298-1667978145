import random
from time import sleep

# returns temperature in celcius (assumed)
class TemperatureSensor:
    def readTemp():
        return random.random() * 80

# returns humidity as relative humidity percentage (assumed)
class HumiditySensor:
    def readHumidity():
        return random.random() * 100

class Alarm:
    def __init__(self, temperatureThreshold, humidityThreshold):
        self.temperatureSensor = TemperatureSensor()
        self.humiditySensor = HumiditySensor()


        self.thresholds = {
            'temp' : temperatureThreshold,
            'humidity' : humidityThreshold
        }
    
    def monitor(self):
        while True:
            temp = TemperatureSensor.readTemp()
            humidity = HumiditySensor.readHumidity()

            print(f'Temperature : {temp:.2f} degree celcius\tHumidty : {humidity:.2f}%')

            if(temp > self.thresholds['temp']):
                print("-----------------------------------------")
                print("|        ALARM : HIGH TEMPERATURE       |")
                print("-----------------------------------------\n")

            if(humidity > self.thresholds['humidity']):
                print("-----------------------------------------")
                print("|        ALARM : HIGH HUMIDITY          |")
                print("-----------------------------------------\n")

            sleep(1)


if __name__ == "__main__":
    alarm = Alarm(70, 80)
    alarm.monitor()
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Stat