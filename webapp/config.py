from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))

WEATHER_DEFAULT_CITY = 'Moscow, Russia'
WEATHER_API_KEY = '254b288df093406092c141709221809'
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
SECRET_KEY = "jsdhdkgrfsahcjkh34843hwedjljg459"
REMEMBER_COOKIE_DURATION = timedelta(days=5)
