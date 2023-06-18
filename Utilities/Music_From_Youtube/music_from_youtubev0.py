from pytube import YouTube 
import time

def Download(link,format='audio'):
    while True:
        try:
            ti = time.time()
            youtubeObj = YouTube(link)
            if format == 'video':
                youtubeObj = youtubeObj.streams.filter(progressive=True).get_highest_resolution()
            elif format == 'audio' :
                youtubeObj = youtubeObj.streams.filter(abr='160kbps', progressive=False).first()
            else:
                print('format not valid , try again 🥲')
                return
            try:
                youtubeObj.download()
                print('Time taken: {:.0f} sec'.format(time.time() - ti))
                print("Successfully downloaded")
                break
            except: 
                print('an error has been occurred while downloading your youtube {er}')
        except: 
            print('erro: {e}')


list_of_links = '''https://www.youtube.com/url1
https://www.youtube.com/url2
https://www.youtube.com/url3'''

for link in list_of_links.split('\n'):
    print('\n',link)
    Download(link, format='audio')
