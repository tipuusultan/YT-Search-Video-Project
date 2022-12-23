from django.shortcuts import render
from youtubesearchpython import *
from pytube import YouTube

# Create your views here.
def home(request):
    return render(request, 'home.html')


def SearchResult(request):  
    
    keyword = request.GET.get('keyword')
    search = VideosSearch(keyword)
    SearchData = search.result()['result']
    search.next()
    SearchData2 = search.result()['result']
    if request.POST:    
        print("request is post")

        search.next()
        SearchData3 = search.result()['result']

        search.next()
        SearchData4 = search.result()['result']

        i = request.session.get('page')
        pp = i + 1
        request.session['page'] = pp
        context = {
        'data':SearchData3,
        'data2':SearchData4,
        'keyword':keyword ,
        'page':pp
        }
        return render(request ,'partials/SearchResults2.html', context)

    keyword = request.GET['keyword']
    search = VideosSearch(keyword)
    SearchData = search.result()['result']
    i=1
    request.session['page'] = i
    context = {
        'data':SearchData,
        'data2':SearchData2,
        'keyword':keyword ,
        'page':i
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