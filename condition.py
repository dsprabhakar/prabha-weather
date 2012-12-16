__author__ = 'amka'
__created__ = '16.12.12'


class Condition(object):
    """
    Store forecast weather data for one day.
    """

    def __init__(self, observation_time=None, temp_C=None, temp_F=None,
                 weatherCode=None, weatherIconUrl=None, weatherDesc=None,
                 windspeedMiles=None, windspeedKmph=None, winddirDegree=None, winddir16Point=None,
                 precipMM=None, humidity=None, visibility=None, pressure=None, cloudcover=None):
        self.observation_time = observation_time
        self.temp_C = temp_C
        self.temp_F = temp_F
        self.weatherCode = weatherCode
        self.weatherIconUrl = weatherIconUrl
        self.weatherDesc = weatherDesc
        self.windspeedMiles = windspeedMiles
        self.windspeedKmph = windspeedKmph
        self.winddirDegree = winddirDegree
        self.winddir16Point = winddir16Point
        self.precipMM = precipMM
        self.humidity = humidity
        self.visibility = visibility
        self.pressure = pressure
        self.cloudcover = cloudcover

    def __repr__(self):
        return "<Condition({0}, {1})>".format(self.observation_time, self.temp_C)