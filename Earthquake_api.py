import requests
import pandas as pd
from datetime import datetime, timedelta
import os

# url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02"

def process_earthquake_data():
    today_date = datetime.now()
    # date 15 days ago
    date_15_days_ago = today_date - timedelta(days=15)

    start_time = date_15_days_ago.strftime("%Y-%m-%d")
    end_time = today_date.strftime("%Y-%m-%d")

    # api endpoint
    url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start_time}&endtime={end_time}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        features =  data['features']

        earthquake_data = []

        date = today_date.strftime("%Y-%m-%d")

        filename =f"C:/Users/BP/Downloads/python code converter/earthquake_data_{date}.csv"

        for feature in features:
            properties = feature['properties']
            geomentry = feature['geometry']
            earthquake = {
                'place': properties['place'],
                'magnitude': properties['mag'],
                # convert time in readable format
                'time': datetime.fromtimestamp(properties['time']/1000).strftime('%Y-%m-%d %H:%M:%S'),
                'latitude': geomentry['coordinates'][1],
                'longitude': geomentry['coordinates'][0],
                'depth': geomentry['coordinates'][2],
                'filename': filename
            }

            earthquake_data.append(earthquake)
        df = pd.DataFrame(earthquake_data)
        # df['time'] = pd.to_datetime(df['time'], unit='ms')
        # df['date'] = df['time'].dt.date
        # df['time'] = df['time'].dt.time
        # df['depth'] = df['depth'].astype(float)
        # df['magnitude'] = df['magnitude'].astype(float)
        # df['latitude'] = df['latitude'].astype(float)
        # df['longitude'] = df['longitude'].astype(float)
        # df['place'] = df['place'].astype(str)
        # df['filename'] = df['filename'].astype(str)
        # df['date'] = df['date'].astype(str)
        # df['time'] = df['time'].astype(str)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

    else:
        print("Error: ", response.status_code)

process_earthquake_data()

