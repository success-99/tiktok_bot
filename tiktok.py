# link = 'https://www.tiktok.com/@uzbek__777/video/7065192361701199105'
def tiktokdow(link):
    import requests
    import json
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "639d77ff43msh31402ee7dc2d76cp188caejsndaca568262c4",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    f = response.text
    natija = json.loads(f)
    if 'error' in natija:
        return 'bed'
    else:
        # return natija['vidio'][0]
        # return {'vidio': natija['video'][0]}
        return natija['video'][0]
# print(tiktokdow())