import requests

kitten_picture_url = 'https://placekitten.com/600/400'

response = requests.get(kitten_picture_url)

with open('kitten.jpg', 'wb') as file:
    for chunk in response.iter_content():
        file.write(chunk)

