import json

import youtube_dl

class DownloadManager(object):
	def __init__(self, folder='./media'):
		self.out_folder = folder
		self.opts = {
 			'format': 'bestaudio/best',
			'outtmpl': folder + '/%(id)s.%(ext)s',
			'download_archive': 'dl_archive.txt',
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
		if ret:
			return None

		opts = { kv[0]: kv[1] for kv in map(lambda kv: kv.split('='), url.split('?')[1].split('&')) }
		vid = opts.get('v', None)
		if vid is None:
			return None
		
		with open('%s/%s.info.json' % (self.out_folder, vid), 'r') as mdjs:
			metadata = json.load(mdjs)
		metadata['filename'] = '%s/%s.opus' % (self.out_folder, vid)
		return metadata
