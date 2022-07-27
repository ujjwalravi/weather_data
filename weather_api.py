import requests

def get_weather_data(city="Bengaluru", api_key="bbcdbab400484c019e182748221707"):
	r = requests.get(f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no')
	if r.status_code != 200:
		return False, r.status_code, r.json()
	return True, r.status_code, r.json()

status, status_code, data =  get_weather_data()
print(status, status_code, data)