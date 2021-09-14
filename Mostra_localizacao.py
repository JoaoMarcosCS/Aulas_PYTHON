from geopy.geocoders import Nominatim
import time
from pprint import pprint

from geopy.location import Location

app = Nominatim(user_agent="tutorial")

def get_location_by_address(address):
    time.sleep(1)
    try:
        return app.geocode(address).raw
    except:
        return get_location_by_address(address)
    
address="Rua leopoldo macedo, Aparecida"
location=get_location_by_address(address)
reverse_location=app.reverse("28.5792615, 77.2440325")

pprint(location)
latitude=location["lat"]
longitude=location['lon']
print(f"{latitude},{longitude}")
print("Endereço: "+reverse_location.address)
