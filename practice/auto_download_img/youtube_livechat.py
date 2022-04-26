from pytchat import LiveChat
import pafy
import pandas as pd

pafy.set_api_key('AIzaSyAB840zsA2T64CfXuzwiwiLb8LliwUKnYw')

#https://www.youtube.com/watch?v=JWreew4k_Ok

video_id = 'z5A7FrFqDWM'

v = pafy.new(video_id)
title = v.title
author = v.author
published = v.published

print(title)
print(author)
print(published)

