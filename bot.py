import discord
from discord.ext import commands
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or('mod!'))


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("DONT SAY BAD WORDS"))
    print("Ready")


@bot.event
async def on_message(message):
    bad_words = ["fuck", "arschloch", "https://discord.gg", "http://disord.gg", "discord.gg", "fick", "arsch",
                 "Arschgesicht", "arschgesicht", "Arschloch", "Asshole", "asshole", "Fotze", "fotze", "Miststück",
                 "miststück", "Bitch", "bitch", "Schlampe", "schlampe", "Sheisse", "sheisse", "Shit", "shit", "Fick",
                 "huren", "Verpiss", "verpiss", "masturbiert", "Idiot", "idiot", "depp", "Depp", "Dumm", "dumm", "jude",
                 "Bastard", "bastard", "Wichser", "wichser", "wixxer", "Wixxer", "Hurensohn" "Wixer", "Pisser",
                 "Arschgesicht", "huso", "hure", "Hure", "verreck" "Verreck", "fehlgeburt", "Fehlgeburt", "ficken",
                 "adhs", "ADHS", "Btch", "faggot", "fck", "f4ck", "nigga", "Nutted", "flaschengeburt", "penis", "pusse",
                 "pusse", "pussy", "pussys", "nigger", "kacke", "fuucker"]
    for word in bad_words:
        if message.content.count(word) > 0:
            await message.channel.purge(limit=1)
            await message.channel.send(f"Please dont say that! {message.author.mention} YOU HAVE BEEN WARNED !warn {message.author.mention}")


bot.run('NzAyNjU4Mzg0MDQ1OTMyNjM0.XqDQLA.2vqLMpsxTBjYH-EWTPBL9ac9_A0')
