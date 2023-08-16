import requests
import json


def tiktokdow(link):
    url = "https://aiov-download-youtube-videos.p.rapidapi.com/GetVideoDetails"

    querystring = {"URL": link}

    headers = {
        "X-RapidAPI-Key": "7452d0fd62msh95c522a9192162dp1c311bjsn64b7eb00230d",
        "X-RapidAPI-Host": "aiov-download-youtube-videos.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    natija = json.loads(response.text)

    if 'error' in natija:
        return 'bed'
    else:
        for i in natija['formats']:
            if i['format_note'] == "Playback video":
                return i['url']
                

