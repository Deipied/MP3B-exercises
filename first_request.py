<<<<<<< HEAD
def dont_give_me_five(start,end):
    new_list = list(range(start,end+1))
    for num in new_list:
        if str(num).find('5') != -1:
            new_list.remove(num)
    return new_list

print(dont_give_me_five(50,81))
=======
import requests
# url = "http://www.google.com"
# response = requests.get(url)

# print(f"your request to {url} came back w/ status code {response.status_code}")

url = "https://icanhazdadjoke.com"

response = requests.get(url, headers = {"Accept":"application/json"})

data = response.json()

print(data["joke"])
>>>>>>> b12fb4405bd72fe605d30503631c8844451ace0c
