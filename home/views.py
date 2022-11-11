from django.shortcuts import render
from youtubesearchpython import *
from pytube import YouTube

# Create your views here.
def home(request):
    return render(request, 'home.html')

def SearchResult(request):
    keyword = request.GET['keyword']
    search = VideosSearch(keyword)
    SearchData = search.result()['result']
    context = {
        'data':SearchData,
        'keyword':keyword
        }
    return render(request, 'SearchResults.html',context)

def SingleVieo(request):
    VideoId = request.GET['v']
    data = YouTube(f'https://youtu.be/{VideoId}')
    # # You can either pass an ID or a URL
    try:
        comments = Comments(VideoId)
        TotalComments = len(comments.comments["result"])
        while comments.hasMoreComments:
            print('Getting more comments...')
            comments.getNextComments()
            TotalComments = len(comments.comments["result"])
    except:
        TotalComments = 'Comments are turned off'
    context = {
        'data':data,
        'VideoId':VideoId,
        'TotalComments':TotalComments
        }
    return render(request, 'SingleVideo.html',context)