import requests

url = "notyetmade"

print("PNP web server status")
try:
    response = requests.get(url)
    if response.status_code == 200:
        print("is up and running")
    else:
        print(f"error, returned status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"{url} is down or somehow failed to respond: {e}")
print("end of PNP web status check.")