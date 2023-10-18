import youtube_dl

class DownloadManager(object):
	def __init__(self, folder='./media'):
		self.opts = {
 			'format': 'bestaudio/best',
			'outtmpl': folder + '/%(id)s.%(ext)s',
			'download_archive': 'dl_archive',
			'writeinfojson': True,
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
        			'preferredcodec': 'opus',
				'preferredquality': '192'
			}]
		}

	def download(self, url):
		with youtube_dl.YoutubeDL(self.opts) as ydl:
			ret = ydl.download([ url ])
		print(ret)
