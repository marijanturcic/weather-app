from pyowm import OWM
import pyowm
import os

OWM_API_KEY = (os.environ['OWM_API_KEY'])
OWM_CITY = (os.environ['OWM_CITY'])

owm = OWM(OWM_API_KEY)
mngr = owm.weather_manager()

observation = mngr.weather_at_place(OWM_CITY)
weather = observation.weather

print('city="{}",'.format(OWM_CITY), end=" ")
print('description="{}",'.format(weather.detailed_status), end=" ")
print('temp="{}",'.format(weather.temperature('celsius')['temp']), end=" ")
print('humidity="{}"'.format(weather.humidity))