import sys

import discord
from discord.ext import commands

from download_manager import DownloadManager

def disco_ball():
	dlman = DownloadManager()

	intents = discord.Intents.default()
	intents.message_content = True
	intents.presences = True
	intents.members = True
	intents.voice_states = True
	bot = commands.Bot(command_prefix='~', intents=intents)

	@bot.command()
	async def ping(ctx):
		await ctx.send('pong')

	#video = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
	#video = 'https://www.youtube.com/watch?v=izGwDsrQ1eQ'

	@bot.command()
	async def play(ctx):
		args = ctx.message.content if ctx.message is not None else ''
		args = args.split()
		args = args[1:]
		user_voice = ctx.author.voice
		voice_channel = user_voice.channel if user_voice is not None else None
		if voice_channel is None: return
		voice = await user_voice.channel.connect()
		for video_url in args:
			try:
				metadata = dlman.download(video_url)
				if metadata is None:
					# video failed to download
					raise Exception("failed to download", video_url)
				#print(metadata)
				#voice = await user_voice.channel.connect()
		
				video_source = await discord.FFmpegOpusAudio.from_probe(metadata['filename'])
				await voice.play(video_source)
			except Exception as e:
				print(repr(e), file=sys.stderr)
		#await voice.disconnect()

	@bot.event
	async def on_presence_update(before, after):
		# TODO: add condition to only run for specific user
		#print(after.name, after.nick, repr(after.activities))
		games = tuple(filter(lambda a: type(a) is discord.Activity and a.type == discord.ActivityType.playing, after.activities))
		#print(after.name, after.nick, tuple(map(lambda g: g.name, games)))

	return bot

