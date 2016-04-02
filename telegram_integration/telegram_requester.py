import requests
import json

from urllib.request import urlopen
from telegram_integration.telegram_photo import TelegramPhoto


class TelegramRequester:

    URL = "http://vespa.habitissimo.party/api"
    SOURCE = "telegram"

    @classmethod
    def send_request(cls, bot, key):
        payload = {}
        if 'type' not in key:
            return False

        # there are type and photo/s
        payload['type'] = key['type']
        # try get location
        if 'location' in key:
            payload['lat'] = key['location'][0]
            payload['lng'] = key['location'][1]

        # do post
        payload['source'] = cls.SOURCE
        payload['free_text'] = "Free Text"
        response = requests.post(cls.URL + "/sightings/", data=payload)

        # check response status
        if response.status_code == 201 and 'photos' in key:
            # get response
            sighting = json.loads(response.text)
            sighting_id = sighting['id']

            # send images
            for photo in key['photos']:
                photo_url = TelegramPhoto.get_file(bot=bot, file_id=photo).file_path
                open_photo = urlopen(photo_url)
                photo_bytes = open_photo.read()
                requests.post(cls.URL + "/sightings/" + str(sighting_id) + "/photos/", files={'file': photo_bytes})
