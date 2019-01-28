class Temperature:
    def __init__(self,temp):
        self.temp = temp

    def convertFahrenheit(self):
        return 9/5*self.temp + 32

    def convertCelsius(self):
        return 5/9*(self.temp-32)
        

todayCel=Temperature(100)
todayFah=Temperature(250)
print("Today's temperature(in Fahrenheit) is ",round(todayCel.convertFahrenheit(),2))
print("Today's temperature(in Celsius) is ",round(todayFah.convertCelsius(),2))
