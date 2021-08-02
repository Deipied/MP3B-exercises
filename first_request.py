import requests
# url = "http://www.google.com"
# response = requests.get(url)

# print(f"your request to {url} came back w/ status code {response.status_code}")

url = "https://icanhazdadjoke.com"

response = requests.get(url, headers = {"Accept":"application/json"})

data = response.json()

print(data["joke"])