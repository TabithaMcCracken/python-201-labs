# Add an API call to your CLI game that assigns a name to your player.

import requests

name_len = 0
while not (name_len >=2 and name_len <=40):
    player_name = str(input("Please enter your name: \n"))
    name_len = len(player_name)

URL = f"https://uzby.com/api.php?min={name_len}&max={name_len}"

response = requests.get(URL)
new_name = response.text

print(f"Welcome, {new_name}! In this game, your new name will be: {new_name}")
print(" Enjoy the game, we hope you make it out alive! \n")
