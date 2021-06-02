import discord
from discord.ext import commands
from discord.ext.commands import Bot
import sys
from io import StringIO 
import requests, urllib, json, random
from pretty_help import *
import traceback
from joke_generator import generate

import xkcd_wrapper
menu = DefaultMenu()


bot = Bot(command_prefix='k!', help_command=PrettyHelp(menu=menu, index_title="sam's kitten :D", no_category="Unclassified"))


TOKEN = "ODQzNjUyMTYyNzk4MDkyMzA5.YKG-TQ.afG5SryYFmGeGRVYMn29s7b4AQE"

client = discord.Client()

class utilities(commands.Cog, name="Utilities", description="utilities :D"):
    def __init__(self, bot):
        self.bot = bot
        
        

    @commands.command(name = "define", help="define something")
    async def define(self,ctx, *, query):
        try:
            url = f"http://api.urbandictionary.com/v0/define?term={query}"
            response = urllib.request.urlopen(url)
            data = json.loads(response.read())
            definition = data['list'][0]['definition']
            await ctx.send(f"**{query}: `" + definition + "`**")
        except:
            await ctx.send("**Couldn't Find A Definition For: `" + query + "`!**")


    @commands.command(name="py", help="executes python script")
    async def python(self, ctx, *, arg):
        try:
            with Capturing() as output:
                exec(arg.replace('"', "'"))
            if "\n".join(output) == "":
                output = ["None"]
            await ctx.send("Code:\n```\n{0}\n```\nOutput:\n```\n{1}\n```".format(arg, "\n".join(output)))
        except Exception as e:
            error = traceback.format_exc().split("\n")
            del error[1]
            
            await ctx.send("```\n{}\n```".format("\n".join(error)))
    
    @commands.command(name="version", help="this bot's version")    
    async def version(self, ctx):
        await ctx.send(f"Version: v{version}")


    @commands.command(name = "lyrics", help="lyrics! \nUsage: k!lyrics (artist) (title)")
    async def lyric(self,ctx, artist, title):
        r = requests.get('https://api.lyrics.ovh/v1/{}/{}'.format(artist, title))
        if r.status_code == 200:
            l_response = json.loads(r.content)
            try:
                lyric = l_response["lyrics"]
                await ctx.send(f'**`Here are the lyrics:`**\n```{lyric}```')
            except:
                await ctx.send(f'**`Lyrics not found!`**')
import json
@bot.event
async def on_ready():
    import datetime
    guildlen = len(bot.guilds)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="sam :D | {0} servers! | k!help".format(str(guildlen))))
    print("[LOG] <READY>")
    
    
    index = 1
    for server in bot.guilds:
        print("{0}: {1}".format(index, server.name))
        print(server.id, server.owner_id)
        index += 1

class entertainment(commands.Cog, name="Fun stuff", description="really fun stuff."):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="cf", help="cat facts!")
    async def cf(self, ctx):
        data = requests.get("https://catfact.ninja/fact").json()
        await ctx.send(data["fact"])
    @commands.command(name="ff", help="gives a random fun fact")
    async def f(self,ctx):
        import randfacts
        x = randfacts.getFact()
        await ctx.send("Fun Fact:\n{}".format(x))

    @commands.command(name="meow", help="gives a random cat image/gif")
    async def meow(self,ctx):
        response = requests.get('https://aws.random.cat/meow')
        data = response.json()
        await ctx.send(data["file"])
    @commands.command(name="joke", help="you want a joke don't you.")
    async def joke(self, ctx):
        await ctx.send(generate())
        
    @commands.command(name="cartoon", help="an xkcd cartoon generator")
    async def cartoon(self, ctx):
        client = xkcd_wrapper.Client()
        random_comic = client.get_random()
        await ctx.send(random_comic.image_url)

from waifu import WaifuClient

client = WaifuClient()


class waifu_(commands.Cog, name="Waifu", description="don't you love waifus."):
    def __init__(self, bot):
        self.bot = bot
        self.img = ["kitsune"]


    @commands.command(name="waifu", help="generates waifu")
    async def waifu(self, ctx):
        if random.randint(1, 2) == 1:
            data = requests.get(f"https://api.nekos.dev/api/v3/images/sfw/img/{random.choice(self.img)}").json()
            await ctx.send(data["data"]["response"]["url"])
        else:
            sfw_waifu = client.sfw(category='waifu')
            await ctx.send(sfw_waifu)
            
    @commands.command(name="w", hidden=True)
    async def w(self, ctx):
        if random.randint(1, 2) == 1:
            data = requests.get(f"https://api.nekos.dev/api/v3/images/sfw/img/{random.choice(self.img)}").json()
            await ctx.send(data["data"]["response"]["url"])
        else:
            sfw_waifu = client.sfw(category='waifu')
            await ctx.send(sfw_waifu)

    @commands.command(name="smug", help="smug")
    async def smug(self, ctx):
        data = requests.get("https://api.nekos.dev/api/v3/images/sfw/gif/smug").json()
        await ctx.send(data["data"]["response"]["url"])
    @commands.command(name="baka", help="baka")
    async def baka(self, ctx):
        data = requests.get("https://api.nekos.dev/api/v3/images/sfw/gif/baka").json()
        await ctx.send(data["data"]["response"]["url"])
        
    @commands.command(name="tickle", help="tickle")
    async def tickle(self, ctx):
        data = requests.get("https://api.nekos.dev/api/v3/images/sfw/gif/tickle").json()
        await ctx.send(data["data"]["response"]["url"])
    
    @commands.command(name="poke", help="poke")
    async def poke(self, ctx):
        data = requests.get("https://api.nekos.dev/api/v3/images/sfw/gif/poke").json()
        await ctx.send(data["data"]["response"]["url"])
        
    @commands.command(name="kiss", help="kiss")
    async def kiss(self, ctx):
        data = requests.get("https://api.nekos.dev/api/v3/images/sfw/gif/kiss").json()
        await ctx.send(data["data"]["response"]["url"])
    
    @commands.command(name="slap", help="slap")
    async def slap(self, ctx):
        data = requests.get("https://api.nekos.dev/api/v3/images/sfw/gif/slap").json()
        await ctx.send(data["data"]["response"]["url"])
    
    @commands.command(name="cuddle", help="cuddle")
    async def cuddle(self, ctx):
        data = requests.get("https://api.nekos.dev/api/v3/images/sfw/gif/cuddle").json()
        await ctx.send(data["data"]["response"]["url"])
    @commands.command(name="hug", help="hug")
    async def hug(self, ctx):
        data = requests.get("https://api.nekos.dev/api/v3/images/sfw/gif/hug").json()
        await ctx.send(data["data"]["response"]["url"])
    @commands.command(name="pat", help="pat")
    async def pat(self, ctx):
        data = requests.get("https://api.nekos.dev/api/v3/images/sfw/gif/pat").json()
        await ctx.send(data["data"]["response"]["url"])
    @commands.command(name="feed", help="feed")
    async def feed(self, ctx):
        data = requests.get("https://api.nekos.dev/api/v3/images/sfw/gif/feed").json()
        await ctx.send(data["data"]["response"]["url"])

    

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout
"""
class economy(commands.Cog, name="economy", description="MONEy"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="profile", help="")
"""
version = "3.31x-Waifu"





print(bot)
print("[LOG] Version: {}".format(version))
bot.add_cog(utilities(bot))
bot.add_cog(entertainment(bot))
bot.add_cog(waifu_(bot))
#bot.add_cog(economy(bot))

bot.run(TOKEN)
