import yt_dlp
import time

def download(link, format='audio'):
    while True:
        try:
            ti = time.time()
            ydl_opts = {}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(link, download=False)
                formats = info['formats']
                if format == 'video':
                    best_format = next((f for f in formats if f.get('vcodec') == 'avc1'), None)
                elif format == 'audio':
                    best_format = next((f for f in formats if f.get('acodec') == 'mp4a.40.2'), None)
                else:
                    print('Format not valid, try again 🥲')
                    return

                if best_format is None:
                    print('No suitable format found for the specified format')
                    return

                ydl_opts['format'] = best_format['format_id']
                ydl.download([link])

            print('Time taken: {:.0f} sec'.format(time.time() - ti))
            print("Successfully downloaded")
            break
        except Exception as e:
            print(f'An error occurred while downloading your YouTube video: {e}')
            break

list_of_links = '''link_1
link_2'''

for link in list_of_links.split('\n'):
    print('\n', link)
    download(link, format='audio')
