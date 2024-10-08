import requests
import json

import serpapi
import os
import json

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('SERPAPI_KEY')
client = serpapi.Client(api_key=api_key)

result = client.search(

    engine='google_flights', 
    departure_id='YYZ',
    arrival_id='YSJ',
    type=2, # 2 is one way, 1 is round trip
    outbound_date='2024-10-21',
    currency='CAD',
    hl='en',
)

best_flight = json.dumps(result["best_flights"][0], indent=2)
# flight_price = best_flight["price"]
best_flight = result["best_flights"][0].flights
#flight_airline = best_flight['flights']

print(best_flight)



