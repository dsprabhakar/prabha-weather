__author__ = 'amka'
__created__ = '16.12.12'


class Weather(object):
    """
    Store forecast weather data for one day.
    """

    def __init__(self, date=None, tempMaxC=None, tempMinC=None, tempMaxF=None, tempMinF=None,
                 windspeedMiles=None, windspeedKmph=None, winddirDegree=None, winddir16Point=None,
                 weatherIconUrl=None, weatherDesc=None, precipMM=None):
        self.date = date
        self.tempMaxC = tempMaxC
        self.tempMaxF = tempMaxF
        self.tempMinC = tempMinC
        self.tempMinF = tempMinF
        self.windspeedMiles = windspeedMiles
        self.windspeedKmph = windspeedKmph
        self.winddirection = winddirDegree
        self.winddir16Point = winddir16Point
        self.winddirDegree = winddirDegree
        self.weatherIconUrl = weatherIconUrl
        self.weatherDesc = weatherDesc
        self.precipMM = precipMM

    def __repr__(self):
        return "<Weather({0}, {1}, {2})>".format(self.date, self.tempMinC, self.tempMaxC)