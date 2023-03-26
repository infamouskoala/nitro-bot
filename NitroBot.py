import discord 
from discord.ext import commands
import random
import string

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Sponsored by KoalaGen || .help", url="https://twitch.tv/infamouskoala"))
    print(f'Logged in as {bot.user} ({bot.user.id})')

@bot.command()
async def nitro(ctx):
    # I used the if/else statements because I wanted to make the bot only be used by me for testing purposes 
    # Feel free to comment out or remove if/elif bits.
    if ctx.message.author.id == 938763585256034315: 
        code  = str(''.join(random.choices(string.ascii_uppercase +
                            string.digits + string.ascii_lowercase, length=random.randint(14,25))))
        message = f"""DISCORD NITRO?!?!?!?!
        https://discord.gift/{code}
        
        Coded with love by : https://github.com/infamous-koala
        """
        author = ctx.author
        message1 = ctx.message
        await message1.add_reaction("✅")
        await author.send(message)
    else:
        await message1.add_reaction("🤔")
        await author.send("Did you really try to get free nitro? Imagine bruh :skull:")

bot.run(input("Enter bot token: "))