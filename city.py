__author__ = 'amka'
__created__ = '16.12.12'


class City(object):
    """
    Describe City object according to real city
    """
    def __init__(self, areaName=None, country=None, region=None,
                 weatherUrl=None, latitude=None, longitude=None, population=None):

        self.areaName = areaName
        self.country = country
        self.region = region
        self.weatherUrl = weatherUrl
        self.latitude = latitude
        self.longitude = longitude
        self.population = population

    def __repr__(self):
        return "<City({0}, {1}, {2})>".format(self.areaName, self.country, self.region)
