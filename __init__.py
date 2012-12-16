#-*- coding: utf-8 -*-
__author__ = 'amka'
__created__ = '16.12.12'
__version__ = '0.1'
__description__ = u'Library to WorldWeatherOnline free API.'


from datetime import datetime
from urllib import urlencode
from urllib2 import urlopen, URLError, HTTPError, Request
import xml.etree.ElementTree as ET

from city import City
from condition import Condition
from weather import Weather


class WWOClient(object):

    base_url = 'http://free.worldweatheronline.com/feed/'
    format = 'xml'

    def __init__(self, key):
        self.key = key

    def __request(self, path, params):
        """
        Send request to worldweatheronline server and return response
        """
        params['key'] = self.key
        params = urlencode(params)
        url = '{0}{1}.ashx?{2}'.format(self.base_url, path, params)
        response = urlopen(url)
        return response.read()

    def search_location(self, location):
        """
        Try to find locations by given city name. Return list of :class:`City` objects
        """
        path = 'search'

        response = self.__request(path, {
            'query':location,
            'format':self.format,
        })

        tree = ET.fromstring(response)

        if tree.tag == 'data':
            raise Exception(tree.find('error').find('msg').text)

        cities = list()
        for result in tree:
            city = City(result.get)
            for child in result.getchildren():
                city.__setattr__(child.tag, child.text)
            cities.append(city)

        return cities

    def weather(self, location, num_of_days=2, date='today'):
        """
        Try to get forecast for given location.
        Location pass one of the following:

            City and Town name

            Acceptable formats are:
                City Name
                City Name, State (US only)
                City Name, State, Country
                City Name, Country
            e.g.: q=New+York or q=New+york,ny or q=London,united+kingdom

            IP address
            e.g.: q=101.25.32.325

            UK or Canada Postal Code or US Zipcode
            e.g.: q=SW1 or q=90201

            Latitude,Longitude (in decimal degree)
            e.g.: q=48.834,2.394

        Return current condition as :class:`Weather` and forecast as list of :class:`Weather`
        """
        path = 'weather'

        if isinstance(location, City):
            location = '{0},{1},{2}'.format(location.areaName, location.region, location.country)

        response = self.__request(path, {
            'q':location,
            'num_of_days':num_of_days,
            'format':self.format,
            'date':date,
            })

        tree = ET.fromstring(response)

        if tree.find('error'):
            raise Exception(tree.find('error').find('msg').text)

        condition = Condition()
        for node in tree.find('current_condition').getchildren():
            if node.tag == 'observation_time':
                utcnow = datetime.utcnow()
                source = '{0}-{1}-{2} '.format(
                    utcnow.year,
                    utcnow.month,
                    utcnow.day
                ) + node.text
                date = datetime.strptime(source,'%Y-%m-%d %I:%M %p')
                condition.__setattr__(node.tag, date)
                continue
            condition.__setattr__(node.tag, node.text)

        forecast = list()
        for node in tree.findall('weather'):
            weather = Weather()
            for child in node.getchildren():
                if child.tag == 'date':
                    date = datetime.strptime(child.text,'%Y-%m-%d')
                    weather.__setattr__(child.tag, date)
                    continue
                weather.__setattr__(child.tag, child.text)
            forecast.append(weather)

        return condition, forecast

    def timezone(self, location):
        """
        Try to get localtime and utc offset for given location.
        Location pass one of the following:

            City and Town name

            Acceptable formats are:
                City Name
                City Name, State (US only)
                City Name, State, Country
                City Name, Country
            e.g.: q=New+York or q=New+york,ny or q=London,united+kingdom

            IP address
            e.g.: q=101.25.32.325

            UK or Canada Postal Code or US Zipcode
            e.g.: q=SW1 or q=90201

            Latitude,Longitude (in decimal degree)
            e.g.: q=48.834,2.394

        Return localtime and utc offset
        :rtype : datetime, str
        """
        path = 'tz'

        if isinstance(location, City):
            location = '{0},{1},{2}'.format(location.areaName, location.region, location.country)

        response = self.__request(path, {
            'q':location,
            'format':self.format,
            })

        tree = ET.fromstring(response)

        timezone = tree.find('time_zone')
        if timezone is not None:
            localtime_s = timezone.find('localtime').text
            localtime = datetime.strptime(localtime_s, '%Y-%m-%d %H:%M')
            utcoffset = timezone.find('utcOffset').text

            return localtime, utcoffset
        else:
            return None, None


if __name__ == '__main__':

    KEY = ''

    wwo = WWOClient(KEY)
    try:
        cities = wwo.search_location('moscow')
        for city in cities:
            print ("{0:20}{1:20}{2:40}{3:>8} {4:8}".format(
                city.areaName,
                city.region,
                city.country,
                city.latitude,
                city.longitude)
            )

        print ('\nWeather for {0}, {1}'.format(cities[0].areaName, cities[0].country))
        current, forecast = wwo.weather(cities[0])
        localtime, offset = wwo.timezone(cities[0])
        print ('Current condition on {0} UTC:\n{1:>10} ˚C\n{2:>10} mbar\n{3:>10} %'.format(
            current.observation_time,
            current.temp_C,
            current.pressure,
            current.humidity,
            )
        )

    except Exception as e:
        print e
