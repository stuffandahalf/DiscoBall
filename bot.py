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
	video = 'https://www.youtube.com/watch?v=izGwDsrQ1eQ'

	@bot.command()
	async def play(ctx):
		print(repr(ctx.author.voice))
		user_voice = ctx.author.voice
		if user_voice is None or user_voice.channel is None: return
		#voice_channel = user_voice.channel
		#voice = await user_voice.channel.connect()
		dlman.download(video)

	@bot.event
	async def on_presence_update(before, after):
		# TODO: add condition to only run for specific user
		#print(after.name, after.nick, repr(after.activities))
		games = tuple(filter(lambda a: type(a) is discord.Activity and a.type == discord.ActivityType.playing, after.activities))
		#print(after.name, after.nick, tuple(map(lambda g: g.name, games)))

	return bot

