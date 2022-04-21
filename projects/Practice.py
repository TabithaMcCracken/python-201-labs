import requests

player_name = input("What is your name?")
print(player_name)

name_len = len(player_name)

URL = f"https://uzby.com/api.php?min={name_len}&max={name_len}"

response = requests.get(URL)
new_name = response.text

print(f"Your new name is: {new_name}")