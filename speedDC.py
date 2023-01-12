import discord
from speedtest import Speedtest
from server import keep_alive

intents = discord.Intents.all()
client = discord.Client(intents=intents,heartbeat_interval=30)

async def speed_test():
    speedtester = Speedtest()
    speedtester.get_best_server()
    download_speed = speedtester.download() / 1_000_000
    upload_speed = speedtester.upload() / 1_000_000
    return download_speed, upload_speed

@client.event
async def on_ready():
    activity = discord.Activity(name='Htamin srr ny tl', type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):
    if message.content[0] == "!":
        if message.content[1:] == "speed":
            await message.channel.send("Checking connection...")
            download_speed, upload_speed = await speed_test()
            embed = discord.Embed(title="Internet Speed Test", description=f'Your current download speed is {download_speed:.2f} Mbps, upload speed is {upload_speed:.2f} Mbps.', color=0x00ff00)
            await message.channel.send(embed=embed)

keep_alive()
client.run('MTA2MzAyMzk5ODc4ODcwNjMzNQ.GHYxWc.KB-6oPU6gu5zRkiNFZiV2x4zM8jf9nKp7fS5jk')
