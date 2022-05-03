# from pytchat import LiveChat
# import pafy
# import pandas as pd

# pafy.set_api_key('AIzaSyAB840zsA2T64CfXuzwiwiLb8LliwUKnYw')

# #https://www.youtube.com/watch?v=JWreew4k_Ok

# video_id = 'JWreew4k_Ok'

# v = pafy.new(video_id)
# title = v.title
# author = v.author
# published = v.published

# print(title)
# print(author)
# print(published)

##2022-04-27 유투브 실시간 스트리밍 사이트 댓글 크롤링
#공식 문서 에서 발췌
import pytchat
import pandas as pd


empty_frame = pd.DataFrame(columns=['댓글 작성자', '댓글 내용', '댓글 작성 시간'])
empty_frame.to_csv('./youtube.csv')
chat = pytchat.create(video_id="MVCKrm-eoRg")


while chat.is_alive():
    try:
        data = chat.get()
        items = data.items
        for c in chat.get().sync_items():
            print(f"{c.datetime} [{c.author.name}]- {c.message}")
            data.tick()
            data2 = {'댓글 작성자' : [c.author.name], '댓글 내용' : [c.datetime], '댓글 작성 시간' : [c.message]}
            result = pd.DataFrame(data2)
            result.to_csv('youtube.csv', mode='a', header=False)
    except KeyboardInterrupt:
        chat.terminate()
        break


# empty_frame = pd.DataFrame(columns=['댓글 작성자', '댓글 내용', '댓글 작성 시간'])
# empty_frame.to_csv('./youtube.csv')

# chat = LiveChat(video_id = video_id, topchat_only = 'FALSE')

# while chat.is_alive():
#     try:
#         data = chat.get()
#         items = data.items
#         for c in items:
#             print(f"{c.datetime} [{c.author.name}]- {c.message}")
#             data.tick()
#             data2 = {'댓글 작성자' : [c.author.name], '댓글 내용' : [c.datetime], '댓글 작성 시간' : [c.message]}
#             result = pd.DataFrame(data2)
#             result.to_csv('youtube.csv', mode='a', header=False)
#     except KeyboardInterrupt:
#         chat.terminate()
#         break