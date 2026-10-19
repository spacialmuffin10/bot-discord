import os
import discord
from discord.ext import tasks, commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@tasks.loop(minutes=1.0)
async def trimite_mesaj_automat():
    # MODIFICĂ AICI: Pune ID-ul real al canalului tău de Discord în loc de numerele de mai jos!
    # Trebuie să fie DOAR CIFRE, fără ghilimele.
    CANAL_ID = 1549771237905932380
    
    canal = bot.get_channel(CANAL_ID)
    if canal:
        await canal.send("⏳ Mesaj automat trimis din cloud la fiecare minut!")
        print("Mesaj trimis pe Discord.")
    else:
        print("Canalul nu a fost găsit. Verifică ID-ul introdus.")

@bot.event
async def on_ready():
    print(f"Botul {bot.user.name} este online!")
    if not trimite_mesaj_automat.is_running():
        trimite_mesaj_automat.start()

# Serverul va lua în siguranță token-ul tău din setările Render
TOKEN_BOT = os.environ.get("DISCORD_TOKEN")
bot.run(TOKEN_BOT)
