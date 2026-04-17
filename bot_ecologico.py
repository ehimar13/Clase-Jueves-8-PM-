import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot ecológico conectado como {bot.user}')

# Diccionario de residuos
residuos = {
    "plastico": "♻️ Reciclable",
    "papel": "♻️ Reciclable",
    "carton": "♻️ Reciclable",
    "vidrio": "♻️ Reciclable",
    "lata": "♻️ Reciclable",
    "banana": "🌱 Orgánico",
    "manzana": "🌱 Orgánico",
    "restos de comida": "🌱 Orgánico",
    "pañal": "🗑️ Basura",
    "colilla": "🗑️ Basura",
    "papel higienico": "🗑️ Basura"
}

@bot.command()
async def residuo(ctx, *, nombre):
    nombre = nombre.lower()

    if nombre in residuos:
        await ctx.send(f"🔍 **{nombre}** → {residuos[nombre]}")
    else:
        await ctx.send(
            f"🤔 No sé qué hacer con **{nombre}**.\n"
            "Pregunta a un experto o revisa normas locales."
        )




@bot.command()
async def consejo(ctx):
    

























@bot.command()
async def recomendacion(ctx):
    #escribe tu codigo aqui
    consejo1 = "apaga las luces al salir"

    await ctx.send()








@bot.command()
async def recomendacion(ctx):
    lista = [
        "usa botellas reutilizables",
        "separa la basura en reciclable y organica",
        "no dejes luces prendidas sin necesidad",
        "ahorra agua cuando te bañes",
        "usa bolsas reutilizables",
        "camina o usa bici si puedes",
        "no tires basura en la calle",
        "recicla papel y carton"
    ]


    await ctx.send(degradarse[random.choice(degradarse.keys())])




bot.run("MTQ4NjkwNDMzNjQ0NDQyODM0OA.G1aa7J.hNLVktfgfu9fruT-h12STHX5RRocM01o2u6GrM")
