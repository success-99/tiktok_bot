# # link = "https://youtu.be/Xu7f0CxHOt4"
# def youtubemp4(link1):
#     import requests
#     import json
#
#     url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"
#
#     querystring = {"id": link1}
#
#     headers = {
#         "X-RapidAPI-Key": "639d77ff43msh31402ee7dc2d76cp188caejsndaca568262c4",
#         "X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
#     }
#
#     response = requests.request("GET", url, headers=headers, params=querystring)
#
#     f = response.text
#     natija1 = json.loads(f)
#     if 'error' in natija1:
#         return 'bed'
#     else:
#         # return natija['vidio'][0]
#         # return {'vidio': natija['video'][0]}
#         return natija1["formats"][2]['url']
#
# # if message.text.startswith('https://youtube.be/') or message.text.startswith(
# #         'https://www.youtube.com/') or message.text.startswith('https://youtu.be/'):
# #     link1 = message.text
# #     data2 = youtubedow(link1)
# #     if data2 == "bed":
# #         await message.answer("Hechnarsa topilmadi 😔")
# #     else:
# #         await message.answer_video(data2)
#
#
#
# import json
#
# import requests
#
# #
# # def youtubedow(link):
# #     url = "https://aiov-download-youtube-videos.p.rapidapi.com/GetVideoDetails"
# #
# #     querystring = {"URL": link}
# #
# #     headers = {
# #         "X-RapidAPI-Key": "7452d0fd62msh95c522a9192162dp1c311bjsn64b7eb00230d",
# #         "X-RapidAPI-Host": "aiov-download-youtube-videos.p.rapidapi.com"
# #     }
# #
# #     response = requests.request("GET", url, headers=headers, params=querystring)
# #     natija = json.loads(response.text)
# #     if 'error' in natija:
# #         return 'bed'
# #     else:
# #         for i in natija['formats']:
# #             if i['format_note'] == '720p' and i['audio_channels'] == 2 and i['asr'] == 44100:
# #                 return i['url']
# #             elif i['format_note'] == '480p' and i['audio_channels'] == 2 and i['asr'] == 44100:
# #                 return i['url']
# #             elif i['format_note'] == '360p' and i['audio_channels'] == 2 and i['asr'] == 44100:
# #                 return i['url']
# #             elif i['format_note'] == '240p' and i['audio_channels'] == 2 and i['asr'] == 44100:
# #                 return i['url']
# #             elif i['format_note'] == '144p' and i['audio_channels'] == 2 and i['asr'] == 44100:
# #                 return i['url']
# #
#
# #         for i in natija5['formats']:
# #             if i['quality'] == 1:
# #                 return i['url']

# #
# # print(facebook("https://www.facebook.com/100006462294384/videos/583175966256115/"))

#
# import openai
# import os
# from playsound import playsound
#
# # OpenAI API Key
# openai.api_key = ""
#
#
# # Text-to-speech function
# def text_to_speech(text):
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=f"Convert the following text to speech:\n\n{text}\n\n",
#         temperature=0.8,
#         max_tokens=100,
#         n=1,
#         stop=None,
#     )
#
#     audio_url = response.choices[0].audio
#     os.system(f"curl -o audio.mp3 {audio_url}")
#     playsound("audio.mp3")
#     os.remove("audio.mp3")
#
#
# # Example usage
#     text = "Assalomu alaykum. Bu Python boti orqali matnni tovushga aylantirish imkoniyatini taqdim etadi."
#     hh=text_to_speech(text)
#     return hh