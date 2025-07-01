import discord
import aiohttp
from discord.ext import commands
import random
from discord.ext.commands import BucketType, cooldown
from datetime import timedelta, datetime, timezone
from discord.ext import commands, tasks
import asyncio
import time
from collections import defaultdict
from bs4 import BeautifulSoup
import requests
from typing import Optional
from discord import Embed







intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


GIPHY_API_KEY = "e31EGu7hRU5pLGN4U6RfoQBD6aLs8vd5"
WEATHER_API_KEY = "51cf7e3589079f50ac2da3ce8b23ad42"

ARME_DESCRIPTIONS = {
    "eggk-47": "The EggK-47 is a classic full-auto rifle with a moderate rate of fire. Good for medium-range combat.",
    "scrambler": "The Scrambler is a close-range shotgun. Deadly up close, ineffective at long range.",
    "free ranger": "The Free Ranger is a semi-automatic precision weapon. Great for mid-range sniping.",
    "rpegg": "The RPG-like RPEGG fires explosive shells. Powerful but with limited ammo.",
    "whipper": "A lightweight automatic weapon with high fire rate. Ideal for hit-and-run.",
    "crackshot": "A bolt-action sniper rifle. One shot, one kill — if you aim right.",
    "tri-hard": "A triple-barrel shotgun. Insane burst damage up close."
}

async def get_gif_url(query):
    url = f"https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={query}&limit=10&rating=g"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            results = data.get("data", [])
            if not results:
                return None
            return random.choice(results)["images"]["original"]["url"]

@bot.event
async def on_ready():
    print(f"✅ Bot connecté en tant que {bot.user}")

# GIF commands
async def gif_command(ctx, query, mention=True):
    gif_url = await get_gif_url(query)
    if gif_url:
        await ctx.send(f"{ctx.author.mention if mention else ''} {gif_url}")
    else:
        await ctx.send("❌ No GIF found.")

@bot.command()
async def hello(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "hello")
    await ctx.send("👋")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} says hello to {membre.mention} ")

@bot.command()
async def bye(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "bye")
    await ctx.send("👋")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} says bye to {membre.mention} ")

@bot.command()
async def yes(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "yes")
    await ctx.send("👍")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} says yes to {membre.mention} ")

@bot.command()
async def no(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "no")
    await ctx.send("👎")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} says no to {membre.mention} ")

@bot.command()
async def fuck(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "fuck")
    await ctx.send("🍆")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} fucks {membre.mention} ")

@bot.command()
async def suck(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "suck")
    await ctx.send("👅")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} sucks {membre.mention} ")

@bot.command()
async def lick(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "lick")
    await ctx.send("👅")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} licks {membre.mention} ")

@bot.command()
async def kiss(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "kiss")
    await ctx.send("💋")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} kisses {membre.mention} ")

@bot.command()
async def hug(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "hug")
    await ctx.send("🤗")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} gives a hug to {membre.mention} ")

@bot.command()
async def egg(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "egg")
    await ctx.send("🥚")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} crushes an egg on the head of {membre.mention} ")

@bot.command()
async def poop(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "poop")
    await ctx.send("💩")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} poops on {membre.mention} ")

@bot.command()
async def duck(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "duck")
    await ctx.send("🦆")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} sends a duck to {membre.mention} ")

@bot.command()
async def farfadet(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "leprechaun")
    await ctx.send("🍀")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} is more mischievous than {membre.mention} ")


@bot.command()
async def troll(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "troll face")
    await ctx.send("🤡")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} is troller than {membre.mention} ")


@bot.command()
async def chill_guy(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "chill guy")
    await ctx.send("😎")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} is more chill than {membre.mention} ")


@bot.command()
async def jawline(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "jawline")
    await ctx.send("👄")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} has a biggest jawline than {membre.mention} ")


@bot.command()
async def hypopoténuse(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "hypopoténuse")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} is more stupid than {membre.mention} ")


@bot.command()
async def mbappe(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "mbappe")
    await ctx.send("🏆")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} is more black than {membre.mention} ")



@bot.command()
async def dancingchicken(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "dancing chicken")
    await ctx.send("🍗")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} is better to eat than {membre.mention} ")


@bot.command()
async def hungry(ctx, membre: Optional[discord.Member] = None): 
    await gif_command(ctx, "hungry")
    await ctx.send("🍔")
    if membre is not None:
        await ctx.send(f"{ctx.author.mention} is better for eat than {membre.mention} ")




@bot.command()
async def randomgif(ctx, membre: Optional[discord.Member] = None): 
    queries = [
        "hello", "bye", "yes", "no", "fuck", "suck", "lick", "kiss", "hug",
        "egg", "poop", "duck", "leprechaun", "troll face", "chill guy",
        "hypopoténuse", "mbappe", "dancing chicken", "luck", "bad luck", "lunctime", "tired", "edit", "jawline", "mbappe",
        "hungry"
    ]
    query = random.choice(queries)
    await gif_command(ctx, query)
    await ctx.send("🎲 Random GIF power activated!")
    if membre:
        await ctx.send(f"{ctx.author.mention} randomly targeted {membre.mention} 🎯")





@bot.command()
async def nerd(ctx):
    nerd_facts = [
        "Did you know an egg’s yolk color depends on the hen’s diet?",
        "Ostrich eggs are the largest eggs in the world.",
        "Some reptiles can lay eggs without mating.",
        "A chicken egg takes 21 days to hatch.",
        "The color of the eggshell does not affect the egg’s nutritional value or taste.",
        "The egg yolk contains all the fat and cholesterol of the egg, while the egg white is mostly protein and water.",
        "Eggs are one of the few natural foods that contain vitamin D.",
        "The chalazae are the two ropey strands in an egg that hold the yolk in the center.",
        "The thickness of the eggshell can vary depending on the hen's diet and age.",
        "Double-yolk eggs occur when a hen releases two yolks into the same shell.",
        "The world’s largest chicken egg on record weighed over 454 grams (1 pound).",
        "Eggs have been used for thousands of years in art, like in Fabergé eggs, which are jeweled masterpieces.",
        "An egg's air cell gets larger as it ages because moisture and carbon dioxide escape through the shell.",
        "In cooking, the pH of egg whites changes as they age, which affects how they whip up in recipes.",
        "The yolk color depends largely on the hen's diet, especially pigments called xanthophylls.",
        "Eggs are used in biochemistry research, especially the protein ovalbumin found in egg whites.",
        "The average hen lays about 250-300 eggs per year.",
        "Some reptiles and birds lay eggs with leathery shells instead of hard ones.",
        "The egg shell is mostly made of calcium carbonate, the same material as limestone and chalk.",
        "Fertilized eggs have a small white spot on the yolk called the blastoderm, which develops into an embryo.",




    ]
    await ctx.send(random.choice(nerd_facts))

# Arme command
@bot.command()
async def arme(ctx, *, name: str):
    name = name.lower().strip()
    if name in ARME_DESCRIPTIONS:
        await ctx.send(f"🛠️ **{name.title()}**: {ARME_DESCRIPTIONS[name]}")
    else:
        await ctx.send("❌ Unknown weapon. Try `!arme eggk-47`, `!arme scrambler`, etc.")

# Timeout command
@bot.command()
@commands.cooldown(1, 600, commands.BucketType.user)  # 1 utilisation / 600 secondes (10 minutes)
async def shutup(ctx, member: discord.Member):
    try:
        until = discord.utils.utcnow() + timedelta(minutes=1)
        await member.timeout(until, reason="Command !shutup use.")
        await ctx.send(f"🔇 {member.mention} was silenced during 1 minute. Congratulation {ctx.author.mention} !")
    except discord.Forbidden:
        await ctx.send("❌ I can't silence this person.Too powerful for me.")
    except commands.CommandOnCooldown as e:
        await ctx.send(f"⏳ You must wait {int(e.retry_after)} more seconds before reusing this command.")
    except Exception as e:
        await ctx.send(f"❌ Erreur : {e}")
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"⏳ Shut-up! {ctx.author.mention}, You must wait {int(error.retry_after)} more seconds before reusing this command.")
    else:
        raise error  # Pour les autres erreurs, on garde l'erreur normale






# Weather command
@bot.command()
async def weather(ctx, *, city: str):
    city = city.strip('"')  # enlève les guillemets si présents
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=fr"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                await ctx.send("❌ Ville non trouvée ou erreur API.")
                return
            data = await resp.json()

            name = data.get("name")
            sys = data.get("sys", {})
            main = data.get("main", {})
            weather = data.get("weather", [{}])[0]
            wind = data.get("wind", {})

            country = sys.get("country", "N/A")
            temp = main.get("temp", "N/A")
            feels_like = main.get("feels_like", "N/A")
            humidity = main.get("humidity", "N/A")
            weather_desc = weather.get("description", "N/A").capitalize()
            wind_speed = wind.get("speed", "N/A")

            message = (
                f"🌍 **Weather at {name}, {country}** :\n"
                f"🌡️ Température : {temp}°C (ressenti {feels_like}°C)\n"
                f"☁️ Conditions : {weather_desc}\n"
                f"💧 Humidité : {humidity}%\n"
                f"💨 Vent : {wind_speed} m/s"
            )
            await ctx.send(message)





@bot.command()
async def insult(ctx, member: discord.Member):
    insults = [
        "You're as sharp as a marble!",
        "If you were any slower, you'd be moving backwards!",
        "You're the human version of a typo.",
        "Your brain is like the Bermuda Triangle—ideas go in and never come out.",
        "You're like a cloud. When you disappear, it's a beautiful day.",
        "You're the reason God created the middle finger.",
        "You're so ugly, when your mom dropped you off at school, she got a fine for littering.",
        "You're so stupid, you couldn't pour water out of a boot if the instructions were on the heel.",
        "You're the human equivalent of a participation trophy.",
        "You're so old, your birth certificate is in Roman numerals.",
        "You're so old, you fart dust.",
        "You’re as bright as a black hole.",
        "You bring everyone so much joy… when you leave the room.",
        "You have something on your chin… no, the third one down.",
        "You’re proof that even evolution takes a break sometimes.",
        "Your secrets are safe with me — I never even listen when you tell me them.",
        "You’re like a cloud. When you disappear, it’s a beautiful day.",
        "You have something on your chin… no, the third one down.",
        "You’re like a software update — whenever you come around, I feel a little slower.",
        "You’re as useless as the “g” in “lasagna.”",
        "If I had a dollar for every smart thing you said, I’d be broke.",
        "You have the perfect face for radio.",
        "You’re like a puzzle with half the pieces missing.",
        "You’re the human version of a participation trophy.",
        "You have something on your chin… no, wait, it’s just your personality.",
        "You bring everyone so much joy… when you leave the room.",
        "Your brain’s so small, it can fit in a thimble.",
        "You have the charm of a wet sock.",
        "You’re like a candy bar: half sweet, half nuts.",
        "You’re as sharp as a marble.",
        "You’re the reason they put directions on shampoo bottles.",
        "You have the perfect face for a Halloween mask.",
        "You’re as useful as a screen door on a submarine.",
        "You have a face only a mother could love — and even she’s suspicious.",
        "You’re about as helpful as a chocolate teapot.",
        "You’re the human version of a typo.",
        "You’re like a cloud — fluffy but mostly full of hot air.",
        "You’re as interesting as watching paint dry — on a rainy day.",
        "Your brain is like the Bermuda Triangle — things go in and never come out.",
        "You’re the reason we have warning labels on everything.",
        "You have a heart of gold… that’s been covered in chocolate.",
        "You’re like a broken pencil — pointless. "
    ]
    insult_msg = random.choice(insults)
    await ctx.send(f"{member.mention}, {insult_msg}")




# Stockage simple en mémoire (pas persistant)
user_auras = defaultdict(int)

AURA_MESSAGES = {
    500: "\U0001F31F {user} is now radiating positivity! (+500 aura)",
    1000: "\u2728 {user} has become a beacon of divine light! (+1000 aura)",
    1500: "\U0001F308 {user} has transcended human limits. Bow before their glory!",
    -500: "\U0001F480 {user}'s vibe is dangerously toxic. Keep your distance.",
    -1000: "\u2620\ufe0f {user} is an aura black hole. Happiness dies near them.",
    -1500: "\U0001F47F {user} is now officially banned from the aura plane."
}

@bot.command()
@commands.cooldown(1, 180, commands.BucketType.user)  # 1 utilisation / 3 minutes / utilisateur
async def aura(ctx, member: commands.MemberConverter, amount: int):
    if amount < -100 or amount > 100:
        await ctx.send("❌ You can only give or take between -100 and +100 aura points.")
        return

    # Mise à jour du score d'aura
    user_auras[member.id] += amount
    total = user_auras[member.id]

    # Message principal
    await ctx.send(f"{ctx.author.mention} changed {member.mention}'s aura by {amount}. Current aura: **{total}**")

    # Message spécial à certains paliers
    if total in AURA_MESSAGES:
        await ctx.send(AURA_MESSAGES[total].format(user=member.mention))
# Cringe detector
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()

    cringe_keywords = ["cringe", "sigma", "based", "rizz", "l ratio", "touch grass"]
    if any(word in content for word in cringe_keywords):
        await message.channel.send(f"🤡 Cringe detected from {message.author.mention}. Please seek help.")
        await message.add_reaction("😬")

    await bot.process_commands(message)



# Réponses automatiques
context_responses = {
    "what": "the dog doin'?",
    "why": "Because I said so.",
    "ok": "boomer.",
    "no": "more like ratio.",
    "lol": "calm down funny guy",
    "bruh": "moment.",
    "who asked": "me. I asked.",
    "i’m hungry": "Hi hungry, I’m bot.",
    "i'm hungry": "Hi hungry, I’m bot.",
    "help": "I'm not legally responsible for anything.",
    "i’m tired": "Then go take a nap, warrior.",
    "i'm tired": "Then go take a nap, warrior.",
    "i’m bored": "Be more interesting.",
    "i'm bored": "Be more interesting.",
    "i have a question": "Too late. The council has spoken.",
    "sus": "I saw you vent.",
    "cringe": "Detected: maximum cringe levels. Self-destruct in 3... 2...",
    "egg": "🥚 Detected. Initiating breakfast protocol.",
    "ratio": "Ratio failed. Bot wins.",
    "you’re dumb": "Yeah? And you're unemployed.",
    "you're dumb": "Yeah? And you're unemployed.",
    "you suck": "Your mom didn’t think so.",
    "shut up": "Make me.",
    "i'm leaving": "Door's that way →",
    "this bot is useless": "Like your KD.",
    "life is hard": "So is this chair.",
    "what is love": "Baby don’t hurt me.",
    "am i real?": "In the eyes of the government, yes.",
    "brainrot": "Tralalero Tralala",
    "wdym": "I mean you suck at shell shocker noob",
    "yes": "no",
    "thxs": "You're welcome, noob."
}

# Événement de message
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    # Cherche une réponse exacte
    if content in context_responses:
        await message.channel.send(context_responses[content])

    # Réactions bonus
    if content == "lol":
        await message.add_reaction("💀")
    elif content == "lmao":
        await message.add_reaction("😭")
    elif content == "ok":
        await message.add_reaction("👍")
    elif content == "bruh":
        await message.add_reaction("🧠")
    elif content == "why":
        await message.add_reaction("❓")
    elif content == "what":
        await message.add_reaction("🐶")
    elif content == "brainrot":
        await message.add_reaction("🦈")
    elif content == "wdym":
        await message.add_reaction("🤔")
    elif content == "yes":
        await message.add_reaction("👍")
    elif content == "no":
        await message.add_reaction("👎")
    elif content == "thxs":
        await message.add_reaction("🤭")

    await bot.process_commands(message)


async def send_numbers(channel):
    for i in range(101):
        await channel.send(str(i))
        await asyncio.sleep(0.5)

sending_task = None  # Variable globale pour la tâche en co

@bot.command()
async def start(ctx):
    global sending_task
    if sending_task is not None and not sending_task.done():
        await ctx.send("I'm already sending the numbers!")
        return
    sending_task = bot.loop.create_task(send_numbers(ctx.channel))
    await ctx.send("I start sending the numbers!")

@bot.command()
async def stop(ctx):
    global sending_task
    if sending_task is None or sending_task.done():
        await ctx.send("I'm not sending numbers.")
        return
    sending_task.cancel()
    await ctx.send("I stop sending the numbers!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, asyncio.CancelledError):
        pass  # Just ignore task cancellation errors




# Dictionnaire des pseudos Shell Shocker associés aux noms Discord affichés
shell_names = {
    "𝔉𝔞𝔯𝔣𝔞𝔡𝔢𝔱 {ℭℭℑ}": "Farfadet {CCI}",
    "Dinoscape {CCI}": "Melee god",
    "CAT": "CAT {CCI}",
    "꧁༺ 𝓕𝓡_𝓞𝓝𝓔{𝓒𝓒𝓘} ༻꧂": "FR_ONE {CCI}",
    "7katter": "i misclicked",
    "Dude {CCI}": "Dude {CCI}",
    "Whoops": "Whoops {CCI}",
    "‶Ꝓιko ³⁶ ヾ‣ {CCI}": "Piko {CCI} (i have to find the spécial police he uses!)",
    "Velox_off": "Le Cixtoyen",
    "Elias": "Cobra 20 {CCI}"
}

@bot.command()
async def name(ctx, member: discord.Member):
    display_name = member.display_name
    pseudo = shell_names.get(display_name)

    if pseudo:
        await ctx.send(f"🎯 Pseudo Shell Shockers of {member.mention} : **{pseudo}**")
    else:
        await ctx.send(f"❓ Pseudo Shell Shockers of {member.mention} unknown.")




SUS_MESSAGES = [
    "Hmmm... {user} seems a bit *sus* 👀",
    "Emergency meeting! 🚨 {user} was acting weird near Electrical.",
    "{user} vented. I saw it. Trust me, bro.",
    "{user} was not the impostor... or were they?",
    "Red is always sus, but today it's {user} 🔴",
    "100% sus detected on {user} 🧠💥",
]

@bot.command()
async def sus(ctx, member: discord.Member = None):
    if member is None:
        member = random.choice(ctx.guild.members)

    message = random.choice(SUS_MESSAGES).format(user=member.mention)
    await ctx.send(message)


#Roland Garros


def get_results():
    url = "https://www.francebleu.fr/sports/tous-les-sports/roland-garros-le-programme-et-les-resultats-de-la-troisieme-journee-3121400"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Exemple : rechercher les balises contenant les résultats
    result_sections = soup.find_all("div", class_="some-class")  # Remplace "some-class" par la classe appropriée
    results = []

    for section in result_sections:
        match_info = section.get_text(strip=True)
        results.append(match_info)

    return results





@bot.command()
async def RG(ctx):
    try:
        results = get_results()
        if not results:
            await ctx.send("Aucun résultat disponible.")
            return
        msg = "**🎾 Résultats Roland-Garros :**\n" + "\n".join(f"• {r}" for r in results)
        await ctx.send(msg)
    except Exception as e:
        await ctx.send(f"Erreur : {e}")





@bot.command()
async def edit(ctx):
    await ctx.send("https://www.youtube.com/shorts/iZYb_jnX9Y4?feature=share")


@bot.command()
async def lunchtime(ctx):
    await ctx.send("https://cdn-www.konbini.com/files/2022/02/hall-11.jpeg")


@bot.command()
async def tired(ctx):
    await ctx.send("https://www.brawlstars-france.fr/wp-content/uploads/2019/10/brawl-stars-emeri-facebook.png")











@bot.command()
async def randomhyper(ctx):
    hypercharges_text = """

Brawler: Bibi
Hypercharge: Bat Barrage
Description: Bibi's next 3 swings shoot a wave of gum behind enemies, dealing 400 damage.
Image: https://cdn.brawlify.com/hypercharges/Bibi_Hypercharge.png

---

Brawler: Brock
Hypercharge: Rocket Assault
Description: Brock’s rockets leave a burning area on the ground for 1.5 seconds, dealing 400 damage per second.
Image: https://cdn.brawlify.com/hypercharges/Brock_Hypercharge.png

---

Brawler: Carl
Hypercharge: Molten Mines
Description: Carl’s pickaxe leaves 3 mines behind him that explode after 1.5 seconds, dealing 700 damage.
Image: https://cdn.brawlify.com/hypercharges/Carl_Hypercharge.png

---

Brawler: Edgar
Hypercharge: Life Leech
Description: Edgar’s punches heal him for 100% of the damage dealt for 5 seconds.
Image: https://cdn.brawlify.com/hypercharges/Edgar_Hypercharge.png

---

Brawler: El Primo
Hypercharge: Meteor Slam
Description: El Primo's Super summons a meteor from the sky that lands after 1.5 seconds, dealing 1500 damage in a large area.
Image: https://cdn.brawlify.com/hypercharges/El_Primo_Hypercharge.png

---

Brawler: Fang
Hypercharge: Kick of Fury
Description: Fang's Super kick is 50% faster and stuns enemies for 0.5 seconds.
Image: https://cdn.brawlify.com/hypercharges/Fang_Hypercharge.png

---

Brawler: Frank
Hypercharge: Heavy Slam
Description: Frank’s Super causes an earthquake on impact, dealing 1200 damage and stunning enemies for 1.2 seconds.
Image: https://cdn.brawlify.com/hypercharges/Frank_Hypercharge.png

---

Brawler: Gale
Hypercharge: Snowblower
Description: Gale’s Super slows enemies by 40% for 2 seconds.
Image: https://cdn.brawlify.com/hypercharges/Gale_Hypercharge.png

---

Brawler: Gene
Hypercharge: Magic Hands
Description: Gene’s Super pulls enemies 0.5 seconds longer.
Image: https://cdn.brawlify.com/hypercharges/Gene_Hypercharge.png

---

Brawler: Griff
Hypercharge: Repulsive Force
Description: Griff’s Super pushes enemies 30% farther.
Image: https://cdn.brawlify.com/hypercharges/Griff_Hypercharge.png

---

Brawler: Gus
Hypercharge: Knockdown
Description: Gus's Super knocks back enemies 15% farther.
Image: https://cdn.brawlify.com/hypercharges/Gus_Hypercharge.png

---

Brawler: Jacky
Hypercharge: Hard Hat
Description: Jacky’s shield reduces damage taken by 10%.
Image: https://cdn.brawlify.com/hypercharges/Jacky_Hypercharge.png

---

Brawler: Janet
Hypercharge: Rejuvenation
Description: Janet’s attacks heal her for 60 health.
Image: https://cdn.brawlify.com/hypercharges/Janet_Hypercharge.png

---

Brawler: Jessie
Hypercharge: Shocky Shock
Description: Jessie’s turret attack stuns enemies for 0.3 seconds.
Image: https://cdn.brawlify.com/hypercharges/Jessie_Hypercharge.png

---

Brawler: Max
Hypercharge: Maximum Speed
Description: Max’s reload speed is increased by 15%.
Image: https://cdn.brawlify.com/hypercharges/Max_Hypercharge.png

---

Brawler: Mortis
Hypercharge: Life Blood
Description: Mortis heals 200 health every time he hits an enemy with his shovel.
Image: https://cdn.brawlify.com/hypercharges/Mortis_Hypercharge.png

---

Brawler: Mr. P
Hypercharge: Quick Repair
Description: Mr. P’s turrets repair themselves 35% faster.
Image: https://cdn.brawlify.com/hypercharges/Mr_P_Hypercharge.png

---

Brawler: Pam
Hypercharge: Nurse’s Touch
Description: Pam’s healing turret heals 50% more health.
Image: https://cdn.brawlify.com/hypercharges/Pam_Hypercharge.png

---

Brawler: Penny
Hypercharge: Cannonball Barrage
Description: Penny’s cannonball drops 2 additional projectiles.
Image: https://cdn.brawlify.com/hypercharges/Penny_Hypercharge.png

---

Brawler: Piper
Hypercharge: High Noon
Description: Piper’s attacks deal 300 extra damage when fully charged.
Image: https://cdn.brawlify.com/hypercharges/Piper_Hypercharge.png

---

Brawler: Poco
Hypercharge: Healing Note
Description: Poco’s healing note heals an additional 150 health.
Image: https://cdn.brawlify.com/hypercharges/Poco_Hypercharge.png

---

Brawler: Ruffs
Hypercharge: Wave Runner
Description: Ruffs’ Super movement speed is increased by 25%.
Image: https://cdn.brawlify.com/hypercharges/Ruffs_Hypercharge.png

---

Brawler: Sandy
Hypercharge: Sandstorm
Description: Sandy’s Super invisibility lasts 0.5 seconds longer.
Image: https://cdn.brawlify.com/hypercharges/Sandy_Hypercharge.png

---

Brawler: Shelly
Hypercharge: Quick Draw
Description: Shelly’s reload speed is increased by 10%.
Image: https://cdn.brawlify.com/hypercharges/Shelly_Hypercharge.png

---

Brawler: Spike
Hypercharge: Needle Grenade
Description: Spike’s attacks cause 20% more area damage.
Image: https://cdn.brawlify.com/hypercharges/Spike_Hypercharge.png

---

Brawler: Stu
Hypercharge: Rocket Buddy
Description: Stu’s Super cooldown is reduced by 15%.
Image: https://cdn.brawlify.com/hypercharges/Stu_Hypercharge.png

---

Brawler: Surge
Hypercharge: Power Surge
Description: Surge’s next attack deals 200 extra damage.
Image: https://cdn.brawlify.com/hypercharges/Surge_Hypercharge.png

---

Brawler: Tara
Hypercharge: Dark Shadow
Description: Tara’s Super pulls enemies 0.3 seconds longer.
Image: https://cdn.brawlify.com/hypercharges/Tara_Hypercharge.png

---

Brawler: Tick
Hypercharge: Faster Explosions
Description: Tick’s mines explode 30% faster.
Image: https://cdn.brawlify.com/hypercharges/Tick_Hypercharge.png

---

Brawler: Bea
Hypercharge: Honeycomb Barrage
Description: Bea’s next 3 shots shoot a swarm of bees dealing 500 damage.
Image: https://cdn.brawlify.com/hypercharges/Bea_Hypercharge.png

---

Brawler: Nani
Hypercharge: Snipe Sight
Description: Nani’s Super deals 200 extra damage.
Image: https://cdn.brawlify.com/hypercharges/Nani_Hypercharge.png

---

Brawler: Colette
Hypercharge: Biting Price
    Description: Colette’s attacks deal 30% more damage to targets above 50% health.
    Image: https://cdn.brawlify.com/hypercharges/Colette_Hypercharge.png

    ---

    Brawler: Cordélia
    Hypercharge: Lightning Strike
    Description: Cordélia’s next attack stuns the enemy for 0.5 seconds.
    Image: https://cdn.brawlify.com/hypercharges/Cordelia_Hypercharge.png

    ---

    Brawler: Darryl
    Hypercharge: Rapid Reload
    Description: Darryl reloads 15% faster.
    Image: https://cdn.brawlify.com/hypercharges/Darryl_Hypercharge.png

    ---

    Brawler: Clancy
    Hypercharge: Hard Punch
    Description: Clancy’s punches knock back enemies 20% farther.
    Image: https://cdn.brawlify.com/hypercharges/Clancy_Hypercharge.png

    ---

    Brawler: Buzz
    Hypercharge: Shockwave
    Description: Buzz’s Super deals 300 extra damage and pushes enemies farther.
    Image: https://cdn.brawlify.com/hypercharges/Buzz_Hypercharge.png

    ---

    Brawler: Bull
    Hypercharge: Heavy Bull
    Description: Bull’s attacks knock back enemies 30% farther.
    Image: https://cdn.brawlify.com/hypercharges/Bull_Hypercharge.png

    ---

    Brawler: Bo
    Hypercharge: Eagle Eye
    Description: Bo’s attacks deal 20% more damage and reveal enemies in a larger area.
    Image: https://cdn.brawlify.com/hypercharges/Bo_Hypercharge.png

    ---

    Brawler: Berry
    Hypercharge: Explosive Trap
    Description: Berry’s traps explode dealing 400 extra damage.
    Image: https://cdn.brawlify.com/hypercharges/Berry_Hypercharge.png

    ---

    Brawler: Belle
    Hypercharge: Sniper Shot
    Description: Belle’s attacks deal 250 extra damage when fully charged.
    Image: https://cdn.brawlify.com/hypercharges/Belle_Hypercharge.png

    ---

    Brawler: Barley
    Hypercharge: Flaming Bottle
    Description: Barley’s attacks leave a burning area dealing 350 damage per second.
    Image: https://cdn.brawlify.com/hypercharges/Barley_Hypercharge.png

    ---

    Brawler: Ash
    Hypercharge: Quick Slash
    Description: Ash’s attacks recharge 10% faster.
    Image: https://cdn.brawlify.com/hypercharges/Ash_Hypercharge.png

    ---

    Brawler: Angelo
    Hypercharge: Shadow Step
    Description: Angelo’s Super cooldown is reduced by 20%.
    Image: https://cdn.brawlify.com/hypercharges/Angelo_Hypercharge.png

    ---

    Brawler: 8-Bit
    Hypercharge: Boosted Damage
    Description: 8-Bit’s attacks deal 15% more damage.
    Image: https://cdn.brawlify.com/hypercharges/8-Bit_Hypercharge.png

    ---

    Brawler: Emz
    Hypercharge: Viral Shield
    Description: Emz gains 15% damage reduction for 3 seconds after using her Super.
    Image: https://cdn.brawlify.com/hypercharges/Emz_Hypercharge.png

    ---

    Brawler: Gray
    Hypercharge: Smoke Bomb
    Description: Gray’s Super lasts 1 second longer and grants invisibility.
    Image: https://cdn.brawlify.com/hypercharges/Gray_Hypercharge.png

    ---

    Brawler: Grom
    Hypercharge: Earthquake
    Description: Grom’s attacks deal 300 extra damage and knockback.
    Image: https://cdn.brawlify.com/hypercharges/Grom_Hypercharge.png

    ---

    Brawler: Hank
    Hypercharge: Fast Recovery
    Description: Hank heals 150 health per hit.
    Image: https://cdn.brawlify.com/hypercharges/Hank_Hypercharge.png

    ---

    Brawler: Kenji
    Hypercharge: Ninja Reflexes
    Description: Kenji’s movement speed increases by 20% after attacking.
    Image: https://cdn.brawlify.com/hypercharges/Kenji_Hypercharge.png

    ---

    Brawler: Leon
    Hypercharge: Smoke Cloud
    Description: Leon’s invisibility duration is increased by 1 second.
    Image: https://cdn.brawlify.com/hypercharges/Leon_Hypercharge.png

    ---

    Brawler: Lola
    Hypercharge: Glamorous Shield
    Description: Lola’s shield absorbs 15% more damage.
    Image: https://cdn.brawlify.com/hypercharges/Lola_Hypercharge.png

    ---

    Brawler: Lou
    Hypercharge: Ice Barrier
    Description: Lou gains 10% damage reduction for 3 seconds after Super.
    Image: https://cdn.brawlify.com/hypercharges/Lou_Hypercharge.png

    ---

    Brawler: Maisie
    Hypercharge: Medic Boost
    Description: Maisie’s healing turret heals 30% faster.
    Image: https://cdn.brawlify.com/hypercharges/Maisie_Hypercharge.png

    ---

    Brawler: Mandy
    Hypercharge: Sticky Trap
    Description: Mandy’s traps slow enemies 40% for 2 seconds.
    Image: https://cdn.brawlify.com/hypercharges/Mandy_Hypercharge.png

    ---

    Brawler: Meg
    Hypercharge: Power Overload
    Description: Meg’s attacks deal 20% more damage.
    Image: https://cdn.brawlify.com/hypercharges/Meg_Hypercharge.png

    ---

    Brawler: Nita
    Hypercharge: Bear Roar
    Description: Nita’s bear’s attacks stun enemies for 0.5 seconds.
    Image: https://cdn.brawlify.com/hypercharges/Nita_Hypercharge.png

    ---

    Brawler: Otis
    Hypercharge: Sonic Boom
    Description: Otis’s Super deals 400 extra damage.
    Image: https://cdn.brawlify.com/hypercharges/Otis_Hypercharge.png

    ---

    Brawler: Pearl
    Hypercharge: Ocean Wave
    Description: Pearl’s Super knocks back enemies 30% farther.
    Image: https://cdn.brawlify.com/hypercharges/Pearl_Hypercharge.png

    ---

    Brawler: Rico
    Hypercharge: Ricochet Shot
    Description: Rico’s shots bounce 2 extra times.
    Image: https://cdn.brawlify.com/hypercharges/Rico_Hypercharge.png

    ---

    Brawler: Rosa
    Hypercharge: Thorny Shield
    Description: Rosa’s shield damages enemies on contact.
    Image: https://cdn.brawlify.com/hypercharges/Rosa_Hypercharge.png

    ---

    Brawler: Sam
    Hypercharge: Quick Fix
    Description: Sam’s attacks heal 50 health.
    Image: https://cdn.brawlify.com/hypercharges/Sam_Hypercharge.png

    ---

    Brawler: Sprout
    Hypercharge: Seed Bomber
    Description: Sprout’s attacks explode dealing 200 extra damage.
    Image: https://cdn.brawlify.com/hypercharges/Sprout_Hypercharge.png

    ---

    Brawler: Squeak
    Hypercharge: Sticky Explosion
    Description: Squeak’s attacks slow enemies 50% for 3 seconds.
    Image: https://cdn.brawlify.com/hypercharges/Squeak_Hypercharge.png

    ---

    Brawler: Willow
    Hypercharge: Fiery Rage
    Description: Willow’s attacks set enemies on fire for 2 seconds.
    Image: https://cdn.brawlify.com/hypercharges/Willow_Hypercharge.png

    ---

    Brawler: Amber
    Hypercharge: Firestorm
    Description: Amber’s attacks leave a trail of fire dealing 400 damage per second.
    Image: https://cdn.brawlify.com/hypercharges/Amber_Hypercharge.png

    ---

    Brawler: Buster
    Hypercharge: Heavy Punch
    Description: Buster’s attacks knock enemies back 40%.
    Image: https://cdn.brawlify.com/hypercharges/Buster_Hypercharge.png

    ---

    Brawler: Charlie
    Hypercharge: Lightning Strike
    Description: Charlie’s Super deals 350 extra damage and stuns enemies for 1 second.
    Image: https://cdn.brawlify.com/hypercharges/Charlie_Hypercharge.png

    ---

    Brawler: Chester
    Hypercharge: Deadly Aim
    Description: Chester’s attacks deal 25% more damage.
    Image: https://cdn.brawlify.com/hypercharges/Chester_Hypercharge.png

    ---

    Brawler: Eve
    Hypercharge: Energy Shield
    Description: Eve gains 20% damage reduction for 3 seconds after Super.
    Image: https://cdn.brawlify.com/hypercharges/Eve_Hypercharge.png

    ---

    Brawler: Lily
    Hypercharge: Healing Aura
    Description: Lily heals allies around her for 100 health per second.
    Image: https://cdn.brawlify.com/hypercharges/Lily_Hypercharge.png

    ---

    Brawler: Melodie
    Hypercharge: Sonic Boom
    Description: Melodie’s attacks deal 300 extra damage.
    Image: https://cdn.brawlify.com/hypercharges/Melodie_Hypercharge.png

    ---

    Brawler: Mico
    Hypercharge: Quick Reflexes
    Description: Mico’s reload speed is increased by 20%.
    Image: https://cdn.brawlify.com/hypercharges/Mico_Hypercharge.png

    ---

    Brawler: Kaze
    Hypercharge: Shadow Step
    Description: Kaze’s Super duration is increased by 1 second.
    Image: https://cdn.brawlify.com/hypercharges/Kaze_Hypercharge.png

    """






    hyper_list = hypercharges_text.strip().split('---')
    random_hyper = random.choice(hyper_list).strip()

    # Extraire les infos
    lines = random_hyper.split('\n')
    brawler = lines[0].split(": ")[1]
    name = lines[1].split(": ")[1]
    description = lines[2].split(": ")[1]
    image_url = lines[3].split(": ")[1]

    embed = discord.Embed(title=f"{brawler} – {name}", description=description, color=0xffc800)
    embed.set_thumbnail(url=image_url)

    await ctx.send(embed=embed)






@bot.command()
async def rich(ctx):
    embed = discord.Embed(color=discord.Color.gold())
    embed.set_image(url=random.choice([
        "https://media.discordapp.net/attachments/1159148341746204764/1376613834185511044/telechargement.jpeg-16.jpg?ex=6835f70a&is=6834a58a&hm=276a304d12670a92f19ca732cb77fb01b14fad15d12927a6bbc838e64b995a33&=&format=webp",
        "https://media.discordapp.net/attachments/1159148341746204764/1376613722830934046/telechargement.jpeg-17.jpg?ex=6835f6ef&is=6834a56f&hm=3bf3524b574c06e491c1760e29664b01af2bc530336cff959caff8e38f178b2d&=&format=webp", "https://media.discordapp.net/attachments/1159148341746204764/1376950943655923832/image.png?ex=68392b3f&is=6837d9bf&hm=7a0c1baa622e4527a5a3f63357d6021221908342bd4fcf9bbd1615a90a822a57&=&format=webp&quality=lossless", "https://media.discordapp.net/attachments/1159148341746204764/1376951490194706583/image.png?ex=68392bc1&is=6837da41&hm=9e2ff9b3c804297b99948956dc68e16cad989ffeeb8222cc0ba1afd83a73afb8&=&format=webp&quality=lossless", "https://media.discordapp.net/attachments/1159148341746204764/1376951576110956696/image.png?ex=68392bd6&is=6837da56&hm=747e0adfab8ff6e626e8057ac4f387f5face25654ea1f2e26fdefa45e130217d&=&format=webp&quality=lossless", "https://media.discordapp.net/attachments/1159148341746204764/1376945719696691281/Z.png?ex=68392661&is=6837d4e1&hm=0e34b5e8db2dd7a9bf65c36e5ad445a0b3e5d03549de1851eb4a0e43a1efefbd&=&format=webp&quality=lossless", "https://media.discordapp.net/attachments/1159148341746204764/1376945576494759936/Z.png?ex=6839263f&is=6837d4bf&hm=558a68d43888af87a253e877ffeabc2965fdd26d07bf9d2a18ff8b60454cb492&=&format=webp&quality=lossless", "https://media.discordapp.net/attachments/1159148341746204764/1376945529740857384/ggnKPgKwjgvQAAAABJRU5ErkJggg.png?ex=68392634&is=6837d4b4&hm=f97377661b5e67e3873e87b9ba9c05e4651960911d89fbcd04b5098479d2b0c1&=&format=webp&quality=lossless", "https://media.discordapp.net/attachments/1159148341746204764/1376945404201144351/XTShHAAAAABJRU5ErkJggg.png?ex=68392616&is=6837d496&hm=cf2395c368ec338954d8775369a6a367bf1ecabf0e8af55289d9650250fa2de4&=&format=webp&quality=lossless"
    ]))
    await ctx.send(embed=embed)





@bot.command()
async def luck(ctx):
    embed = discord.Embed(color=discord.Color.green())
    embed.set_image(url=random.choice([
        "https://tiermaker.com/images/template_images/2022/15463705/all-crackshot-skins-15463705/m2dznewyears-1jpg.png" ,
        "https://media.discordapp.net/attachments/1159148341746204764/1376613433310576710/telechargement.jpeg-15.jpg?ex=6835f6aa&is=6834a52a&hm=29348a8bf32069ac4a06f45b8389cc0214897463eafb239112547fe7192d7459&=&format=webp" ,
        "https://media.discordapp.net/attachments/1159148341746204764/1376613503007199252/telechargement.jpeg-18.jpg?ex=6835f6bb&is=6834a53b&hm=d4eaaee932bf87f96ffdb3677fe02ef19fcc723027ad004e3ca20526386e4b85&=&format=webp",
        "https://media.discordapp.net/attachments/1159148341746204764/1376614957159809064/Z.png?ex=6835f816&is=6834a696&hm=654ddb513ce8bf564c74d2679b7998f5a9933d7b9e085e163e033b944e5d3bbf&=&format=webp&quality=lossless", "https://media.discordapp.net/attachments/1159148341746204764/1376947204891344896/Z.png?ex=683927c4&is=6837d644&hm=e8b806a83aa1a9e23aad54723615ff2ce5f97ade264a91ece8037578e1057814&=&format=webp&quality=lossless", "https://media.discordapp.net/attachments/1159148341746204764/1376947091892605009/Z.png?ex=683927a9&is=6837d629&hm=c88379aeb1bafdc3631cf0e00d686df0ea3f8e91a74027ad12d73cee9caa52eb&=&format=webp&quality=lossless", "https://media.discordapp.net/attachments/1159148341746204764/1376946968114499784/9k.png?ex=6839278b&is=6837d60b&hm=8b180010297ddcc78efe1504f1ce3ee4769896e268fd0551cce6061de11a033a&=&format=webp&quality=lossless", "https://media.discordapp.net/attachments/1159148341746204764/1376946277467553962/Z.png?ex=683926e6&is=6837d566&hm=b3f3ff0e738c999aa43f096df2d3e38f180d08ce9910d0ca4b8160778265408a&=&format=webp&quality=lossless", "https://media.discordapp.net/attachments/1159148341746204764/1376946204654567435/9k.png?ex=683926d5&is=6837d555&hm=27d732fd3564086c5ca6c4dee6bf36c19bbee06d4c7af90ccc66bea2bbedee40&=&format=webp&quality=lossless", "https://media.discordapp.net/attachments/1159148341746204764/1376946044759314494/images.png?ex=683926af&is=6837d52f&hm=97e84ce8f02b79a63debd40c0020e493fc1b441dcd62a1feccbfa6fd466a5e0a&=&format=webp&quality=lossless", "https://media.discordapp.net/attachments/1159148341746204764/1376946016170803380/images.png?ex=683926a8&is=6837d528&hm=05ef09abe095d485348fd86c893be3196e5514aa5f7ea06aa95c823bb9c93339&=&format=webp&quality=lossless", "https://media.discordapp.net/attachments/1159148341746204764/1376945985929871441/images.png?ex=683926a1&is=6837d521&hm=19c0297d13199279cdef746f502a77a9cb27e15240a6a86986a1519770b91084&=&format=webp&quality=lossless", "https://media.discordapp.net/attachments/1159148341746204764/1376945921140719696/Z.png?ex=68392692&is=6837d512&hm=9ad80a2aafad96a59a59f4a3e090c2fcf825ad9e8a2f2e6333d629908a2b6b2a&=&format=webp&quality=lossless"
    ]))
    await ctx.send(embed=embed)



@bot.command()
async def badluck(ctx):
    embed = discord.Embed(color=discord.Color.red())
    embed.set_image(url=random.choice([
        "https://static.wikia.nocookie.net/shellshockers/images/b/b6/Screenshot_2023-09-03_at_5.16.43_pm.png/revision/latest/scale-to-width-down/248?cb=20230903071725", "https://media.discordapp.net/attachments/1159148341746204764/1376616938758869143/image.png?ex=6835f9ee&is=6834a86e&hm=7b43cbd4f017a3b60f58351df90d236309b631e69201836cf738f2cdfa388176&=&format=webp&quality=lossless", "https://www.immac-pau.com/images/sections/Sport/AS_ATHLE/WhatsApp_Image_2023-10-11_%C3%A0_18.19.02_09edfd43.jpg"
    ]))
    await ctx.send(embed=embed)


@bot.command()
async def challenge(ctx):
    embed = discord.Embed(color=discord.Color.dark_blue())
    embed.set_image(url=random.choice([
        "https://media.discordapp.net/attachments/1159148341746204764/1376949589571014846/2Q.png?ex=683929fc&is=6837d87c&hm=0796f3289cd8bdae06ff62a9dc0828a17ab47c3b75ac24b8ec783f693a834cc5&=&format=webp&quality=lossless", "https://media.discordapp.net/attachments/1159148341746204764/1376949877875146986/image.png?ex=68392a41&is=6837d8c1&hm=e1c3d8731d72e88b34ec3b404f2101d76769ec07ee24430d79edfa60ffc67b55&=&format=webp&quality=lossless"
    ]))
    await ctx.send(embed=embed)



@bot.command()
@commands.has_permissions(administrator=True)
async def testjoin(ctx):
    bot.dispatch("member_join", ctx.author)



class WeaponSelect(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(discord.ui.Select(
            placeholder="Choisis ton arme préférée 🔫",
            options=[
                discord.SelectOption(label="EggK-47", description="Classique mais efficace"),
                discord.SelectOption(label="Scrambler", description="À bout portant"),
                discord.SelectOption(label="Free Ranger", description="Tireur d’élite"),
                discord.SelectOption(label="RPEGG", description="BOOM !"),
                discord.SelectOption(label="Whipper", description="Un peu tout faire"),
                discord.SelectOption(label="Tri-Hard Cluck", description="Pour les pros")
            ],
            custom_id="weapon_select"
        ))

    @discord.ui.select(custom_id="weapon_select")
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(
            f"Tu as choisi : **{select.values[0]}** ! Bonne chance soldat 🥚", ephemeral=True
        )

@bot.event
async def on_member_join(member):
    # Chercher un salon nommé "welcome"
    channel = discord.utils.get(member.guild.text_channels, name="welcome👋")
    if channel:
        view = WeaponSelect()
        await channel.send(
            f"Bienvenue {member.mention} ! Choisis ton arme préférée de **Shell Shockers** pour rejoindre la bataille :",
            view=view
        )
    else:
        print("Salon #welcome👋 non trouvé.")











@bot.command()
async def ai(ctx, *, question):
    try:
        await ctx.send("🤖 Je réfléchis...")
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "tinyllama",
                "prompt": question,
                "stream": False
            },
            timeout=20
        )
        data = response.json()
        answer = data.get("response", "🤷‍♂️ Pas de réponse reçue.")
        await ctx.send(answer[:2000])  # Discord limite les messages à 2000 chars
    except Exception as e:
        await ctx.send(f"❌ Erreur : {e}")
        print(f"Erreur : {e}")




# Start the bot
import os
bot.run(os.getenv("TOKEN"))