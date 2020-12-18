import discord
import random
import time
from discord import Spotify
from discord.ext import commands

Bot = commands.Bot(command_prefix = '}')

#Events
@Bot.event
async def on_ready():
	print("Da Bot is ready. Piemol?")

@Bot.event
async def on_member_join(member):
		print (f'{member} has joined the server!')

@Bot.event
async def on_member_remove(member):
	print(f'{member} has left the server.')

@Bot.event
async def on_message(message, amount=1):

    if 'Jappie' in message.content:
        await message.channel.purge(limit=amount)

    if 'jappie' in message.content:
        await message.channel.purge(limit=amount)

    if 'jaapie' in message.content:
        await message.channel.purge(limit=amount)

    if 'Jaapie' in message.content:
        await message.channel.purge(limit=amount)

    if 'Japie' in message.content:
        await message.channel.purge(limit=amount)

    if 'japie' in message.content:
        await message.channel.purge(limit=amount)

    if 'Jasper' in message.content:
        await message.channel.purge(limit=amount)

    if 'jasper' in message.content:
        await message.channel.purge(limit=amount)



    if 'Jappie.' in message.content:
        await message.channel.purge(limit=amount)

    if 'jappie.' in message.content:
        await message.channel.purge(limit=amount)

    if 'jaapie.' in message.content:
        await message.channel.purge(limit=amount)

    if 'Jaapie.' in message.content:
        await message.channel.purge(limit=amount)

    if 'Japie.' in message.content:
        await message.channel.purge(limit=amount)

    if 'japie.' in message.content:
        await message.channel.purge(limit=amount)

    if 'Jasper.' in message.content:
        await message.channel.purge(limit=amount)

    if 'jasper.' in message.content:
        await message.channel.purge(limit=amount)


#Commands
@Bot.command()
async def Ping(ctx):
	await ctx.send(f'Pong!\n> {round(Bot.latency * 1000)}ms')

@Bot.command(aliases = ['8ball', 'test'])
async def _8ball(ctx, *, question ):
	responses = ['Sowieso, kennie anders!',
	 			 'Het is besloten dat dit correct is',
				 'Without a doubt',
				 'Ja! - Absoluut.',
				 'Ga er maar van uit.',
				 'Zoals ik het zie, ja.',
				 'Waarschijnlijk welm ja.',
				 'Het ziet er goed uit.',
				 'Yep.',
				 'De tekens van het universum zeggen ja.',
				 'Antwoord is onzeker. Probeer het opnieuw.',
				 'Probeer het later nog eens.',
				 'Dit is niet het goede moment, vraag het nog een keer.',
				 'Ik kan nu niks zeggen.',
				 'Concentrate and ask again.',
				 "Ga er maar niet van uit.",
				 'Mijn antwoord is nee.',
				 'Het ziet er niet goed uit. YIKES!',
				 'NEEEEE!!!! ABSOLUUT NIET!!!!!!!']
	await ctx.send(f'**Question**: {question}\n**Answer**: {random.choice(responses)}')

@Bot.command()
async def Clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount)

@Bot.command()
async def Clearall(ctx, amount=999):
	await ctx.channel.purge(limit=amount)

@Bot.command()
async def Test(ctx):
	await ctx.send(f'Test 123 123')

@Bot.command()
async def spotify(ctx, user: discord.Member=None):
    user = user or ctx.author
    for activity in user.activities:
        if isinstance(activity, Spotify):
            await ctx.send(f"{user} is listening to {activity.title} by {activity.artist}")

Bot.run('Nzg5NDU1Njg2MzI0NzE1NTQx.X9yT5g.xrlLyuhTkvhGj33NWbYp-1MOIFc')
