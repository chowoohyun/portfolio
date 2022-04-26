# from pytchat import LiveChat
# import pafy
# import pandas as pd

# pafy.set_api_key('AIzaSyAB840zsA2T64CfXuzwiwiLb8LliwUKnYw')

# #https://www.youtube.com/watch?v=JWreew4k_Ok

# video_id = 'z5A7FrFqDWM'

# v = pafy.new(video_id)
# title = v.title
# author = v.author
# published = v.published

# print(title)
# print(author)
# print(published)

import pytchat

chat = pytchat.create(video_id="JWreew4k_Ok")
while chat.is_alive():
    for c in chat.get().sync_items():
        print(f"{c.datetime} [{c.author.name}]- {c.message}")