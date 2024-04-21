import discord
import random
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic2 import gen_advice
from bot_logic3 import gen_smile

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await ctx.send('Всем привет! Меня зовут {bot.user}. Для более подробной информации напишите "!помощь"')

@bot.command()
async def помощь(ctx):
    await ctx.send("В список моих команд входят: приветствие (!привет), прощание (!пока), генерация пароля (!пароль), совет (!совет), калькулятор (!калькулятор), мемы (!мем), мем с животными (мем_животные) и варианты поделок из бутылок (эко_бутылки).")

@bot.command()
async def привет(ctx):
    await ctx.send("Приветствую!")

@bot.command()
async def пока(ctx):
    await ctx.send("До свидания!")

@bot.command()
async def пароль(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def совет(ctx):
    await ctx.send(gen_advice())

@bot.command()
async def калькулятор(ctx, first: int, action, second: int):
    if action == "+":
        await ctx.send(first + second)
    elif action == "-":
        await ctx.send(first - second)
    elif action == "*":
        await ctx.send(first * second)
    elif action == "/":
        await ctx.send(first / second)
    else:
        await ctx.send("Не допустимая операция")

@bot.command()
async def мем_животные(ctx):
    name = ['mem1.jpg', 'mem2.jpg', 'mem3.jpg', 'mem4.jpg', 'mem5.jpg', 'mem6.jpg', 'mem7.jpg', 'mem8.jpg']
    img_name = random.choice(name)
    with open(f'image/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def мем(ctx):
    name = ['mem1.jpg', 'mem2.jpg', 'mem3.jpg', 'mem4.png', 'mem5.jpg', 'mem6.jpg', 'mem7.jpg', 'mem8.jpg']
    img_name = random.choice(name)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def эко_бутылки(ctx):
    name = ['eco1.jpeg', 'eco2.png', 'eco3.jpeg', 'eco4.jpg', 'eco5.jpeg', 'eco6.jpg', 'eco7.jpg', 'eco8.jpg']
    img_name = random.choice(name)
    with open(f'images_eco/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
    await ctx.send('Не выбрасывайте пластиковые бутылки! Лучше сделайте такую красивую и полезную вещь!😊')

bot.run("")
