import discord
from discord.ext import commands
from googletrans import Translator

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)
translator = Translator()

@bot.command()
async def traduzir(ctx, lang, *, mensagem):
    try:
        traducao = await translator.translate(mensagem, dest=lang)
        await ctx.send(f'Tradução: {traducao.text}')
    except ValueError:
        await ctx.send('Idioma inválido!')

bot.run('INSIRA O TOKEN DO SEU BOT')
