# WWOLib

Python library for www.worldweatheronline.com free API


## Usage

1. 1st of all import library

    `import wwolib`
    
2. Create client with your wwo free API key
   
   `client = WWOClient(YOUR_WWO_KEY)`
   
3. Get cities list

   `cities = client.search_location('london')`
   
4. Get current weather condition and forecast.
   
   Location pass one of the following:
   
   * **City** object
   
   * **City and Town name**. Acceptable formats are:
   
     * City Name
     * City Name, State (US only)
     * City Name, State, Country
     * City Name, Country
        
     e.g.: q=New+York or q=New+york,ny or q=London,united+kingdom

   * **IP address** e.g.: q=101.25.32.325

   * **UK or Canada Postal Code or US Zipcode** e.g.: q=SW1 or q=90201

   * **Latitude,Longitude (in decimal degree)** e.g.: q=48.834,2.394

   
   `current, forecast = client.weather(cities[0])`
   
   By default return forecast for 2 days but can be provided with num_of_days param:
   
   `current, forecast = client.weather(cities[0], num_of_days=4)`
   
    Also you can provide date of current condition by param `date` with values:
    
    * today
    * tomorrow
    * date in YYYY-MM-DD format, e.g.: 2012-12-31
  
   `current, forecast = client.weather(cities[0], num_of_days=4, date='today')`
   
   

5. Get local time for locations and UTC offset. `location` like in weather request.

    `localtime, offset = client.timezone(location)`