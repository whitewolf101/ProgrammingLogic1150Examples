import requests

kitten_picture_urls = [
    'https://placekitten.com/600/400',
    'https://placekitten.com/600/401',
    'https://placekitten.com/200/300',
    'https://placekitten.com/600/700'
    ]

for index, url in enumerate(kitten_picture_urls):
    response = requests.get(url)

    filename = f'kitten_{index}.jpg'  # generate unique filename
    with open(filename, 'wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)

