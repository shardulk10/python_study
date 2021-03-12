# https://towardsdatascience.com/geocode-with-python-161ec1e62b89
# https://stackoverflow.com/questions/36064495/importerror-no-module-named-geopy-ipython-notebook
# https://stackoverflow.com/questions/45362210/own-nominatim-server-not-working-with-geopy
# https://medium.com/analytics-vidhya/how-to-generate-lat-and-long-coordinates-of-city-without-using-apis-25ebabcaf1d5

from geopy import Nominatim

locator = Nominatim(user_agent="myGeocoder")
location = locator.geocode("Chembur")

print(location)
print("Latitude = {}, Longitude = {}",str(location.latitude), str(location.longitude))