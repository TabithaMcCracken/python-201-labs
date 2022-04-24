# Use a quotes API, e.g. http://quotes.stormconsultancy.co.uk/random.json
# to fetch a random quote. Then use string manipulation to convert it to
# Doge speech (https://blogs.unimelb.edu.au/sciencecommunication/2016/10/22/how-to-speak-doge/)
# Create a tiny webpage that displays a doge image together
# with the altered quote. You can get an image URL from another API:
# http://shibe.online/api/shibes
# Write the code logic to make the API calls and assign the output to
# `doged_quote` and `doge_image_url` respectively.
# Then write the `html` string to a `.html` file and look at it in your browser.

import requests
from pathlib import Path

# Get quote
# Quotes from API http://quotes.stormconsultancy.co.uk/random.json
quote_url = "http://quotes.stormconsultancy.co.uk/random.json"
quote = requests.get(quote_url).json()["quote"]
print(f"Here is the quote: {quote}\n")

# Convert the quote to doge
# Conversion API https://api.funtranslations.com/translate/doge.json
doge_url = f"https://api.funtranslations.com/translate/doge.json?text={quote}"
doge_quote = requests.get(doge_url).json()["contents"]["translated"]
print(f"Here is quote converted to doge: \n {doge_quote}")

# Get dog image
# image from API http://shibe.online/api/shibes
img_url = "http://shibe.online/api/shibes?count=1"
doge_img = requests.get(img_url).json()[0]
print(f"Here is the link to the image: {doge_img} \n")


# create html structure
html = f"<p>Here is the original quote: {quote}</p><img src='{doge_img}'><p>Here is the doge translation: {doge_quote}</p>"
print(html)

# # create a new file
f = Path().home().joinpath("Documents").joinpath("codingnomads").joinpath("python-201-copy").joinpath("projects").joinpath("dogetranslator.html")
# write to the file
f.write_text(html)
