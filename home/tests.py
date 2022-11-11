from django.test import TestCase

# Create your tests here.
from youtubesearchpython import *

channel_id = "UCUE5IBoxWDeSFmBKAlKgfpQ"
playlist = Playlist(playlist_from_channel_id(channel_id))

print(f'Videos Retrieved: {playlist.videos}')

while playlist.hasMoreVideos:
    print('Getting more videos...')
    playlist.getNextVideos()
    print(f'Videos Retrieved: {playlist.videos}')
    print(playlist.videos)

print('Found all the videos.')

# from youtubesearchpython import *

# # You can either pass an ID or a URL
# video_id = "hf3OJ32hw14"
# comments = Comments(video_id)

# print(f'Comments Retrieved: {len(comments.comments["result"])}')

# while comments.hasMoreComments:
#     print('Getting more comments...')
#     comments.getNextComments()
#     print(f'Comments Retrieved: {len(comments.comments["result"])}')

# print('Found all the comments.')