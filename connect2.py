import discord
from discord.ext import commands
from bot_logic import gen_pass

with open("token.txt", "r") as f: # Membaca token dari file token.txt
    token = f.read() # Menyimpan token ke dalam variabel token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def mem(ctx):
    nama_images = random.choice(os.listdir('images'))
    with open(f'images/{nama_images}', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def passwd(ctx):
    await ctx.send(gen_pass(5))

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run(token)
