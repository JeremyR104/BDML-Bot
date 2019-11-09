import discord
import time
import asyncio
import random
id = 602567351770021938
nwordcount = 0
messages = joined = 0
messagetotal = 0
client = discord.Client()
jxhero1 = "Not Chosen"
jxhero2 = "Not Chosen"
jxhero3 = "Not Chosen"
jxhero4 = "Not Chosen"
jxhero5 = "Not Chosen"
jxhero6 = "Not Chosen"
jxhero7 = "Not Chosen"
jxhero8 = "Not Chosen"
jxhero9 = "Not Chosen"
jxhero10 = "Not Chosen"
jahero1 = "Not Chosen"
jahero2 = "Not Chosen"
jahero3 = "Not Chosen"
jahero4 = "Not Chosen"
jahero5 = "Not Chosen"
jahero6 = "Not Chosen"
jahero7 = "Not Chosen"
jahero8 = "Not Chosen"
jahero9 = "Not Chosen"
jahero10 = "Not Chosen"
jehero1 = "Not Chosen"
jehero2 = "Not Chosen"
jehero3 = "Not Chosen"
jehero4 = "Not Chosen"
jehero5 = "Not Chosen"
jehero6 = "Not Chosen"
jehero7 = "Not Chosen"
jehero8 = "Not Chosen"
jehero9 = "Not Chosen"
jehero10 = "Not Chosen"
mahero1 = "Not Chosen"
mahero2 = "Not Chosen"
mahero3 = "Not Chosen"
mahero4 = "Not Chosen"
mahero5 = "Not Chosen"
mahero6 = "Not Chosen"
mahero7 = "Not Chosen"
mahero8 = "Not Chosen"
mahero9 = "Not Chosen"
mahero10 = "Not Chosen"
dihero1 = "Not Chosen"
dihero2 = "Not Chosen"
dihero3 = "Not Chosen"
dihero4 = "Not Chosen"
dihero5 = "Not Chosen"
dihero6 = "Not Chosen"
dihero7 = "Not Chosen"
dihero8 = "Not Chosen"
dihero9 = "Not Chosen"
dihero10 = "Not Chosen"
bdaybonus = 0
bdaytotal = 0
bdaychance = 0
nwordcount = 0
nwmoyaichance = 0
nwmoyaibonus = 0
nwmoyaitotal = 0
nwpasschance = 0
nwpassbonus = 0
nwpasstotal = 0
nwbraydenchance = 0
nwbraydenbonus = 0
nwbraydentotal = 0
nwsoulesschance = 0
nwsoulessbonus = 0
nwsoulesstotal = 0
nwmonkeychance = 0
nwmonkeybonus = 0
nwmonkeytotal = 0
nwanshchance = 0
nwanshbonus = 0
nwanshtotal = 0

async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("statistics.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages},\n")

                messages = 0
                joined = 0

                await asyncio.sleep(600)
        except Exception as e:
            print(e)
            await asyncio.sleep(600)


@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count(":moyai:") > 0:
            last = before.nick
            if last:
                await after.edit(nick="last")
            else:
                await after.edit(nick="May Gan: The Mayest of Gan")


@client.event
async def on_message(message):
    global messages
    messages += 1
    id = client.get_guild(602567351770021938)
    clean_channels = ("minecraft")
    screenshot_flex = ("screenshot-flex")
    stupid_chat  = ("stupid-chat")
    invalid_users = ("megabot#4826")
    Jackson_Hlist = ("SpikedJackson#4383")
    Dillon_Hlist = ("Dillon#7149")
    Jeremy_Hlist = ("WarDemonTimmy#2112")
    Matthew_Hlist = ("Mattoo#6800")
    Jack_Hlist = ("Mr Smigly#5832")
    Monica_Hlist = ("Monica.s.k#0514")
    Bad_heros = ("Fanny", "fanny", "Esmerelda", "esmerelda", "Diggie", "diggie", "Khufra", "khufra", "Lylia", "lylia", "X Borg", "x borg")

    for word in Bad_heros:
        if message.content.count(word) > 0:
            print("A cursed name was uttered")
            await message.channel.purge(limit=1)
            await message.channel.send("Never speak of that cursed name in this sacred server")
            time.sleep(2)
            await message.channel.purge(limit=1)
    if str(message.channel) not in clean_channels and str(message.author) not in invalid_users:
        if message.content == "!users":
            await message.channel.send(f"""# of Members {id.member_count}""")
        if message.content == "!stats":
            await message.channel.send(f"""# of Members {id.member_count}""")
            global nwordcount
            await message.channel.send(f"""# of N-words {nwordcount}""")
        if message.content.find("!pass") != -1:
            await message.channel.send("You have used the pass, all past usages of the N-word are forgiven")
            nwordcount
            nwordcount = 0
        if message.content.find("headass") != -1:
            await message.channel.send(":moyai:")
        if message.content.find("bot broke") != -1:
            await message.channel.send(":moyai:")
        if message.content == "!help":
            embed = discord.Embed(title="Help with megabot", description="here are the commands you can do so far")
            embed.add_field(name="hello", value="Greets the user")
            embed.add_field(name="!gay", value="For when you spot Jackson")
            embed.add_field(name="!users", value="Count of total users on server")
            embed.add_field(name="!stats", value="Shows some cool stats of the server")
            embed.add_field(name="!ml help", value="A hep menu for Jeremy's cluttered ML secretary bot thing")
            await message.channel.send(content=None, embed=embed)
        if message.content == "!ml help":
            mlhembed = discord.Embed(title="Help with ML commands",
                                     description="here are the commands you can do so far")
            mlhembed.add_field(name="!ml <name> hero# add <hero name>",
                               value="Adds the named hero to the named person's 10 man roster. Eg.: !ml Jackson add Akai")
            mlhembed.add_field(name="!ml hlist <name>", value="Shows roster of named person")
            await message.channel.send(content=None, embed=mlhembed)
        if message.content == "!ml tanks":
            tanklistembed = discord.Embed(title="All tanks rated", description="This is based off of stats given by Halpie (Angela the ml bot)")
            tanklistembed.add_field(name="Akai", value="A: 55, O: 65, D: 90" )
            tanklistembed.add_field(name="Balmond", value="A: 40, O: 68, D: 80")
            tanklistembed.add_field(name="Bixi", value="A:N/A, O: N/A, D: N/A")
            tanklistembed.add_field(name="Franco", value="A: 50, O: 60, D: 80")
            tanklistembed.add_field(name="Esmerelda", value="A: 65, O: 65, D: 76")
            tanklistembed.add_field(name="Gatotkaca", value="A: 70, O: 49, D: 92")
            tanklistembed.add_field(name="Grock", value="A: 60, O: 54, D: 81")
            tanklistembed.add_field(name="Hilda", value="A: 52, O: 58, D: 85")
            tanklistembed.add_field(name="Hylos", value="A:62, O: 34, D: 90")
            tanklistembed.add_field(name="Johnson", value="A: 60, O: 39, D: 92")
            tanklistembed.add_field(name="Khufra", value="A: 72, O: 66, D: 78")
            tanklistembed.add_field(name="Lolita", value="A: 75, O: 52, D:83 ")
            tanklistembed.add_field(name="Masha", value="A: N/A, O: N/A, D: N/A")
            tanklistembed.add_field(name="Minotaur", value="A: 53, O: 64, D: 90")
            tanklistembed.add_field(name="Tigreal", value="A: 62, O: 34, D: 90")
            tanklistembed.add_field(name="Uranus", value="A: 82, O: 34, D: 85")
            await message.channel.send(content=None, embed=tanklistembed)
        if message.content.find("!birthdayboy") != -1:
            await message.channel.send(" :confetti_ball: :tada: :tada: ***Happy Birthday Matthew!*** :tada: :tada: :confetti_ball: ")
            birthdayprotocol = True
    if str(message.channel) not in clean_channels and str(message.author) in Monica_Hlist:
        if message.content.find("hello") != -1:
            await message.channel.send("Hey Monica, how are you?")
        if message.content.find("!gay") != -1:
            await message.channel.send("Oh god! Oh fuck! You're lesbian? I guess it make sense considering Matthew :matthewAY: :peach:")
        if message.content.find("!nigga") != -1:
            await message.channel.send("You've changed :eyes:")
        if message.content.find("nigga") != -1:
            global nwanshchance
            global nwanshbonus
            global nwanshtotal
            nwanshchance = random.randrange(0,20,1)
            nwanshtotal = nwanshchance+nwanshbonus
            if nwanshtotal > 15:
                await message.channel.send("Yeah im lightskin but im still a dark nigga")
                nwanshtotal = 0
                nwanshchance = 0
                nwanshbonus = 0
            else:
                nwanshbonus += 1
                nwanshtotal = 0
                nwanshchance = 0
            nwordcount
            nwordcount += 1
        if message.content.find("Nigga") != -1:
            nwanshchance = random.randrange(0,20,1)
            nwanshtotal = nwanshchance+nwanshbonus
            if nwanshtotal > 15:
                await message.channel.send("I'm so proud")
                nwanshtotal = 0
                nwanshchance = 0
                nwanshbonus = 0
            else:
                nwanshbonus += 1
                nwanshtotal = 0
                nwanshchance = 0
            nwordcount
            nwordcount += 1
        if message.content.find("NIGGA") != -1:
            nwanshchance = random.randrange(0,20,1)
            nwanshtotal = nwanshchance+nwanshbonus
            if nwanshtotal > 15:
                await message.channel.send("What would Ansh think if he saw you like this?")
                nwanshtotal = 0
                nwanshchance = 0
                nwanshbonus = 0
            else:
                nwanshbonus += 1
                nwanshtotal = 0
                nwanshchance = 0
            nwordcount
            nwordcount += 2
        if message.content.find("nigger") != -1:
            nwanshchance = random.randrange(0,20,1)
            nwanshtotal = nwanshchance+nwanshbonus
            if nwanshtotal > 15:
                await message.channel.send("I thought you said you'd never say it?")
                nwanshtotal = 0
                nwanshchance = 0
                nwanshbonus = 0
            else:
                nwanshbonus += 2
                nwanshtotal = 0
                nwanshchance = 0
            nwordcount
            nwordcount += 2
        if message.content.find("Nigger") != -1:
            nwanshchance = random.randrange(0,20,1)
            nwanshtotal = nwanshchance+nwanshbonus
            if nwanshtotal > 15:
                await message.channel.send(":ansh: :ansh: :ansh: ")
                nwanshtotal = 0
                nwanshchance = 0
                nwanshbonus = 0
            else:
                nwanshbonus += 2
                nwanshtotal = 0
                nwanshchance = 0
            nwordcount
            nwordcount += 2
        if message.content.find("NIGGER") != -1:
            nwanshchance = random.randrange(0,20,1)
            nwanshtotal = nwanshchance+nwanshbonus
            if nwanshtotal > 15:
                await message.channel.send(":ansh_hyper: :ansh_hyper: :ansh_hyper: ")
                nwanshtotal = 0
                nwanshchance = 0
                nwanshbonus = 0
            else:
                nwanshbonus += 2
                nwanshtotal = 0
                nwanshchance = 0
            nwordcount
            nwordcount += 3
    if str(message.channel) not in clean_channels and str(message.author) in Jackson_Hlist:
        if message.content.find("hello") != -1:
            await message.channel.send("Hey Jackson, how are you?")
        if message.content.find("!gay") != -1:
            await message.channel.send("So you finally admit it?")
        if message.content.find("!nigga") != -1:
            await message.channel.send("You got a pass for that?")
        if message.content.find("nigga") != -1:
            global nwpasschance
            global nwpassbonus
            global nwpasstotal
            nwpasschance = random.randrange(0,20,1)
            nwpasstotal = nwpasschance+nwpassbonus
            if nwpasstotal > 15:
                await message.channel.send("You got a pass for that?")
                nwpasstotal = 0
                nwpasschance = 0
                nwpassbonus = 0
            else:
                nwpassbonus += 1
                nwpasstotal = 0
                nwpasschance = 0
            nwordcount
            nwordcount += 1
        if message.content.find("Nigga") != -1:
            nwpasschance = random.randrange(0,20,1)
            nwpasstotal = nwpasschance+nwpassbonus
            if nwpasstotal > 15:
                await message.channel.send("Excuse me?")
                nwpasstotal = 0
                nwpasschance = 0
                nwpassbonus = 0
            else:
                nwpassbonus += 1
                nwpasstotal = 0
                nwpasschance = 0
            nwordcount
            nwordcount += 1
        if message.content.find("NIGGA") != -1:
            nwpasschance = random.randrange(0,20,1)
            nwpasstotal = nwpasschance+nwpassbonus
            if nwpasstotal > 15:
                await message.channel.send("Woah there buckaroo, you got a license for that?")
                nwpasstotal = 0
                nwpasschance = 0
                nwpassbonus = 0
            else:
                nwpassbonus += 1
                nwpasstotal = 0
                nwpasschance = 0
            nwordcount
            nwordcount += 2
        if message.content.find("nigger") != -1:
            nwpasschance = random.randrange(0,20,1)
            nwpasstotal = nwpasschance+nwpassbonus
            if nwpasstotal > 15:
                await message.channel.send("Huzzah, a man of culture.")
                nwpasstotal = 0
                nwpasschance = 0
                nwpassbonus = 0
            else:
                nwpassbonus += 2
                nwpasstotal = 0
                nwpasschance = 0
            nwordcount
            nwordcount += 2
        if message.content.find("Nigger") != -1:
            nwpasschance = random.randrange(0,20,1)
            nwpasstotal = nwpasschance+nwpassbonus
            if nwpasstotal > 15:
                await message.channel.send("Why yes, that is the profession term for them.")
                nwpasstotal = 0
                nwpasschance = 0
                nwpassbonus = 0
            else:
                nwpassbonus += 2
                nwpasstotal = 0
                nwpasschance = 0
            nwordcount
            nwordcount += 2
        if message.content.find("NIGGER") != -1:
            nwpasschance = random.randrange(0,20,1)
            nwpasstotal = nwpasschance+nwpassbonus
            if nwpasstotal > 15:
                await message.channel.send("(647) 528-3412")
                nwpasstotal = 0
                nwpasschance = 0
                nwpassbonus = 0
            else:
                nwpassbonus += 2
                nwpasstotal = 0
                nwpasschance = 0
            nwordcount
            nwordcount += 3
        if message.content == "!ml hero1 add Akai":
            global jxhero1
            jxhero1 = "Akai"
            await message.channel.send("Jackson's hero #1 is now Akai! :panda_face: ")
        if message.content == "!ml hero1 add Balmond":
            jxhero1 = "Balmond"
            await message.channel.send("Jackson's hero #1 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero1 add Belerick":
            jxhero1 = "Belerick"
            await message.channel.send("Jackson's hero #1 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero1 add Franco":
            jxhero1 = "Franco"
            await message.channel.send("Jackson's hero #1 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero1 add Esmerelda":
            jxhero1 = "Esmerelda"
            await message.channel.send("Jackson's hero #1 is now Esmerelda! :shield: ")
        if message.content == "!ml hero1 add Gatotkaca":
            jxhero1 = "Gatotkaca"
            await message.channel.send("Jackson's hero #1 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero1 add Grock":
            jxhero1 = "Grock"
            await message.channel.send("Jackson's hero #1 is now Grock! :european_castle: ")
        if message.content == "!ml hero1 add Hilda":
            jxhero1 = "Hilda"
            await message.channel.send("Jackson's hero #1 is now Hilda! :runner: ")
        if message.content == "!ml hero1 add Hylos":
            jxhero1 = "Hylos"
            await message.channel.send("Jackson's hero #1 is now Hylos! :unicorn: ")
        if message.content == "!ml hero1 add Johnson":
            jxhero1 = "Johnson"
            await message.channel.send("Jackson's hero #1 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero1 add Khufra":
            jxhero1 = "Khufra"
            await message.channel.send("Jackson's hero #1 is now Khufra! :clown: ")
        if message.content == "!ml hero1 add Lolita":
            jxhero1 = "Lolita"
            await message.channel.send("Jackson's hero #1 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jxhero1 = "Masha"
            await message.channel.send("Jackson's hero #1 is now Masha! :bear: ")
        if message.content == "!ml hero1 add Minotaur":
            jxhero1 = "Minotaur"
            await message.channel.send("Jackson's hero #1 is now Minotaur! :cow: ")
        if message.content == "!ml hero1 add Tigreal":
            jxhero1 = "Tigreal"
            await message.channel.send("Jackson's hero #1 is now Tigreal! :moyai: ")
        if message.content == "!ml hero1 add Uranus":
            jxhero1 = "Uranus"
            await message.channel.send("Jackson's hero #1 is now Uranus! :peach: ")
        if message.content == "!ml hero1 add X.Borg":
            jxhero1 = "X.Borg"
            await message.channel.send("Jackson's hero #1 is now X.Borg! :fire: ")
        if message.content == "!ml hero1 add Aldous":
            jxhero1 = "Aldous"
            await message.channel.send("Jackson's hero #1 is now Aldous! :fist: ")
        if message.content == "!ml hero1 add Alpha":
            jxhero1 = "Alpha"
            await message.channel.send("Jackson's hero #1 is now Alpha! :airplane: ")
        if message.content == "!ml hero1 add Alucard":
            jxhero1 = "Alucard"
            await message.channel.send("Jackson's hero #1 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero1 add Argus":
            jxhero1 = "Argus"
            await message.channel.send("Jackson's hero #1 is now Argus! :angel: ")
        if message.content == "!ml hero1 add Badang":
            jxhero1 = "Badang"
            await message.channel.send("Jackson's hero #1 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero1 add Bane":
            jxhero1 = "Bane"
            await message.channel.send("Jackson's hero #1 is now Bane! :octopus: ")
        if message.content == "!ml hero1 add Chou":
            jxhero1 = "Chou"
            await message.channel.send("Jackson's hero #1 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero1 add Dyrroth":
            jxhero1 = "Dyrroth"
            await message.channel.send("Jackson's hero #1 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero1 add Freya":
            jxhero1 = "Freya"
            await message.channel.send("Jackson's hero #1 is now Freya! :hammer: ")
        if message.content == "!ml hero1 add Guinevere":
            jxhero1 = "Guinevere"
            await message.channel.send("Jackson's hero #1 is now Guinevere! :dress:  ")
        if message.content == "!ml hero1 add Jawhead":
            jxhero1 = "Jawhead"
            await message.channel.send("Jackson's hero #1 is now Jawhead! :robot: ")
        if message.content == "!ml hero1 add Kaja":
            jxhero1 = "Kaja"
            await message.channel.send("Jackson's hero #1 is now Kaja! :bird: ")
        if message.content == "!ml hero1 add Lapu-Lapu":
            jxhero1 = "Lapu-Lapu"
            await message.channel.send("Jackson's hero #1 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero1 add Leomord":
            jxhero1 = "Leomord"
            await message.channel.send("Jackson's hero #1 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero1 add Martis":
            jxhero1 = "Martis"
            await message.channel.send("Jackson's hero #1 is now Martis! :crab: ")
        if message.content == "!ml hero1 add Minsitthar":
            jxhero1 = "Minsitthar"
            await message.channel.send("Jackson's hero #1 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero1 add Roger":
            jxhero1 = "Roger"
            await message.channel.send("Jackson's hero #1 is now Roger! :wolf: ")
        if message.content == "!ml hero1 add Ruby":
            jxhero1 = "Ruby"
            await message.channel.send("Jackson's hero #1 is now Ruby! :heart: ")
        if message.content == "!ml hero1 add Sun":
            jxhero1 = "Sun"
            await message.channel.send("Jackson's hero #1 is now Sun! :monkey_face: ")
        if message.content == "!ml hero1 add Thamuz":
            jxhero1 = "Thamuz"
            await message.channel.send("Jackson's hero #1 is now Thamuz! :rage: ")
        if message.content == "!ml hero1 add Terizla":
            jxhero1 = "Terizla"
            await message.channel.send("Jackson's hero #1 is now Terizla! :hammer: ")
        if message.content == "!ml hero1 add Zilong":
            jxhero1 = "Zilong"
            await message.channel.send("Jackson's hero #1 is now Zilong! :dragon: ")
        if message.content == "!ml hero1 add Fanny":
            jxhero1 = "Fanny"
            await message.channel.send("Jackson's hero #1 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero1 add Gusion":
            jxhero1 = "Gusion"
            await message.channel.send(
                "Jackson's hero #1 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero1 add Hanzo":
            jxhero1 = "Hanzo"
            await message.channel.send("Jackson's hero #1 is now Hanzo! :ghost: ")
        if message.content == "!ml hero1 add Hayabusa":
            jxhero1 = "Hayabusa"
            await message.channel.send("Jackson's hero #1 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero1 add Helcurt":
            jxhero1 = "Helcurt"
            await message.channel.send("Jackson's hero #1 is now Helcurt! :mute:  ")
        if message.content == "!ml hero1 add Karina":
            jxhero1 = "Karina"
            await message.channel.send("Jackson's hero #1 is now Karina! :purple_heart: ")
        if message.content == "!ml hero1 add Lancelot":
            jxhero1 = "Lancelot"
            await message.channel.send("Jackson's hero #1 is now Lancelot! :fencer: ")
        if message.content == "!ml hero1 add Lesley":
            jxhero1 = "Lesley"
            await message.channel.send("Jackson's hero #1 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero1 add Natalia":
            jxhero1 = "Natalia"
            await message.channel.send("Jackson's hero #1 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero1 add Saber":
            jxhero1 = "Saber"
            await message.channel.send("Jackson's hero #1 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero1 add Selena":
            jxhero1 = "Selena"
            await message.channel.send("Jackson's hero #1 is now Selena! :sleeping:  ")
        if message.content == "!ml hero1 add Alice":
            jxhero1 = "Alice"
            await message.channel.send("Jackson's hero #1 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero1 add Aurora":
            jxhero1 = "Aurora"
            await message.channel.send("Jackson's hero #1 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jxhero1 = "Chang'e"
            await message.channel.send("Jackson's hero #1 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero1 add Cyclops":
            jxhero1 = "Cyclops"
            await message.channel.send("Jackson's hero #1 is now Cyclops! :eye:  ")
        if message.content == "!ml hero1 add Eudora":
            jxhero1 = "Eudora"
            await message.channel.send("Jackson's hero #1 is now Eudora! :zap: ")
        if message.content == "!ml hero1 add Faramis":
            jxhero1 = "Faramis"
            await message.channel.send("Jackson's hero #1 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero1 add Gord":
            jxhero1 = "Gord"
            await message.channel.send("Jackson's hero #1 is now Gord! :snowboarder:")
        if message.content == "!ml hero1 add Harith":
            jxhero1 = "Harith"
            await message.channel.send("Jackson's hero #1 is now Harith! :older_man: ")
        if message.content == "!ml hero1 add Harley":
            jxhero1 = "Harley"
            await message.channel.send("Jackson's hero #1 is now Harley! :tophat: ")
        if message.content == "!ml hero1 add Kadita":
            jxhero1 = "Kadita"
            await message.channel.send("Jackson's hero #1 is now Kadita! :droplet: ")
        if message.content == "!ml hero1 add Kagura":
            jxhero1 = "Kagura"
            await message.channel.send("Jackson's hero #1 is now Kagura! :umbrella2:  ")
        if message.content == "!ml hero1 add Lunox":
            jxhero1 = "Lunox"
            await message.channel.send("Jackson's hero #1 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero1 add Lylia":
            jxhero1 = "Lylia"
            await message.channel.send("Jackson's hero #1 is now Lylia! :boom: ")
        if message.content == "!ml hero1 add Nana":
            jxhero1 = "Nana"
            await message.channel.send("Jackson's hero #1 is now Nana! :cat:  ")
        if message.content == "!ml hero1 add Odette":
            jxhero1 = "Odette"
            await message.channel.send("Jackson's hero #1 is now Odette! :duck: ")
        if message.content == "!ml hero1 add Pharsa":
            jxhero1 = "Pharsa"
            await message.channel.send("Jackson's hero #1 is now Pharsa! :dove:  ")
        if message.content == "!ml hero1 add Vale":
            jxhero1 = "Vale"
            await message.channel.send("Jackson's hero #1 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero1 add Valir":
            jxhero1 = "Valir"
            await message.channel.send("Jackson's hero #1 is now Valir! :fire:")
        if message.content == "!ml hero1 add Vexanna":
            jxhero1 = "Vexanna"
            await message.channel.send("Jackson's hero #1 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero1 add Bruno":
            jxhero1 = "Bruno"
            await message.channel.send("Jackson's hero #1 is now Bruno! :soccer:  ")
        if message.content == "!ml hero1 add Claude":
            jxhero1 = "Claude"
            await message.channel.send("Jackson's hero #1 is now Claude! :monkey:  ")
        if message.content == "!ml hero1 add Clint":
            jxhero1 = "Clint"
            await message.channel.send("Jackson's hero #1 is now Clint! :cowboy: ")
        if message.content == "!ml hero1 add Granger":
            jxhero1 = "Granger"
            await message.channel.send("Jackson's hero #1 is now Granger! :violin: ")
        if message.content == "!ml hero1 add Hanabi":
            jxhero1 = "Hanabi"
            await message.channel.send("Jackson's hero #1 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero1 add Irithel":
            jxhero1 = "Irithel"
            await message.channel.send("Jackson's hero #1 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero1 add Karrie":
            jxhero1 = "Karrie"
            await message.channel.send(
                "Jackson's hero #1 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero1 add Kimmy":
            jxhero1 = "Kimmy"
            await message.channel.send("Jackson's hero #1 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero1 add Layla":
            jxhero1 = "Layla"
            await message.channel.send("Jackson's hero #1 is now Layla! :haircut:  ")
        if message.content == "!ml hero1 add Miya":
            jxhero1 = "Miya"
            await message.channel.send("Jackson's hero #1 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero1 add Moskov":
            jxhero1 = "Moskov"
            await message.channel.send("Jackson's hero #1 is now Moskov! :imp: ")
        if message.content == "!ml hero1 add Yi Sun-Shin":
            jxhero1 = "Yi Sun-Shin"
            await message.channel.send("Jackson's hero #1 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero1 add Angela":
            jxhero1 = "Angela"
            await message.channel.send("Jackson's hero #1 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero1 add Diggie":
            jxhero1 = "Diggie"
            await message.channel.send("Jackson's hero #1 is now Diggie! :owl: ")
        if message.content == "!ml hero1 add Estes":
            jxhero1 = "Estes"
            await message.channel.send("Jackson's hero #1 is now Estes! :ear:  ")
        if message.content == "!ml hero1 add Rafaela":
            jxhero1 = "Rafaela"
            await message.channel.send("Jackson's hero #1 is now Rafaela! :angel: ")
        if message.content == "!ml hero1 add Rynn":
            jxhero1 = "Rynn"
            await message.channel.send("Jackson's hero #1 is now Rynn! ")
        if message.content == "!ml hero2 add Akai":
            global jxhero2
            jxhero2 = "Akai"
            await message.channel.send("Jackson's hero #2 is now Akai! :panda_face: ")
        if message.content == "!ml hero2 add Balmond":
            jxhero2 = "Balmond"
            await message.channel.send("Jackson's hero #2 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero2 add Belerick":
            jxhero2 = "Belerick"
            await message.channel.send("Jackson's hero #2 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero2 add Franco":
            jxhero2 = "Franco"
            await message.channel.send("Jackson's hero #2 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero2 add Esmerelda":
            jxhero2 = "Esmerelda"
            await message.channel.send("Jackson's hero #2 is now Esmerelda! :shield: ")
        if message.content == "!ml hero2 add Gatotkaca":
            jxhero2 = "Gatotkaca"
            await message.channel.send("Jackson's hero #2 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero2 add Grock":
            jxhero2 = "Grock"
            await message.channel.send("Jackson's hero #2 is now Grock! :european_castle: ")
        if message.content == "!ml hero2 add Hilda":
            jxhero2 = "Hilda"
            await message.channel.send("Jackson's hero #2 is now Hilda! :runner: ")
        if message.content == "!ml hero2 add Hylos":
            jxhero2 = "Hylos"
            await message.channel.send("Jackson's hero #2 is now Hylos! :unicorn: ")
        if message.content == "!ml hero2 add Johnson":
            jxhero2 = "Johnson"
            await message.channel.send("Jackson's hero #2 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero2 add Khufra":
            jxhero2 = "Khufra"
            await message.channel.send("Jackson's hero #2 is now Khufra! :clown: ")
        if message.content == "!ml hero2 add Lolita":
            jxhero2 = "Lolita"
            await message.channel.send("Jackson's hero #2 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jxhero2 = "Masha"
            await message.channel.send("Jackson's hero #2 is now Masha! :bear: ")
        if message.content == "!ml hero2 add Minotaur":
            jxhero2 = "Minotaur"
            await message.channel.send("Jackson's hero #2 is now Minotaur! :cow: ")
        if message.content == "!ml hero2 add Tigreal":
            jxhero2 = "Tigreal"
            await message.channel.send("Jackson's hero #2 is now Tigreal! :moyai: ")
        if message.content == "!ml hero2 add Uranus":
            jxhero2 = "Uranus"
            await message.channel.send("Jackson's hero #2 is now Uranus! :peach: ")
        if message.content == "!ml hero2 add X.Borg":
            jxhero2 = "X.Borg"
            await message.channel.send("Jackson's hero #2 is now X.Borg! :fire: ")
        if message.content == "!ml hero2 add Aldous":
            jxhero2 = "Aldous"
            await message.channel.send("Jackson's hero #2 is now Aldous! :fist: ")
        if message.content == "!ml hero2 add Alpha":
            jxhero2 = "Alpha"
            await message.channel.send("Jackson's hero #2 is now Alpha! :airplane: ")
        if message.content == "!ml hero2 add Alucard":
            jxhero2 = "Alucard"
            await message.channel.send("Jackson's hero #2 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero2 add Argus":
            jxhero2 = "Argus"
            await message.channel.send("Jackson's hero #2 is now Argus! :angel: ")
        if message.content == "!ml hero2 add Badang":
            jxhero2 = "Badang"
            await message.channel.send("Jackson's hero #2 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero2 add Bane":
            jxhero2 = "Bane"
            await message.channel.send("Jackson's hero #2 is now Bane! :octopus: ")
        if message.content == "!ml hero2 add Chou":
            jxhero2 = "Chou"
            await message.channel.send("Jackson's hero #2 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero2 add Dyrroth":
            jxhero2 = "Dyrroth"
            await message.channel.send("Jackson's hero #2 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero2 add Freya":
            jxhero2 = "Freya"
            await message.channel.send("Jackson's hero #2 is now Freya! :hammer: ")
        if message.content == "!ml hero2 add Guinevere":
            jxhero2 = "Guinevere"
            await message.channel.send("Jackson's hero #2 is now Guinevere! :dress:  ")
        if message.content == "!ml hero2 add Jawhead":
            jxhero2 = "Jawhead"
            await message.channel.send("Jackson's hero #2 is now Jawhead! :robot: ")
        if message.content == "!ml hero2 add Kaja":
            jxhero2 = "Kaja"
            await message.channel.send("Jackson's hero #2 is now Kaja! :bird: ")
        if message.content == "!ml hero2 add Lapu-Lapu":
            jxhero2 = "Lapu-Lapu"
            await message.channel.send("Jackson's hero #2 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero2 add Leomord":
            jxhero2 = "Leomord"
            await message.channel.send("Jackson's hero #2 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero2 add Martis":
            jxhero2 = "Martis"
            await message.channel.send("Jackson's hero #2 is now Martis! :crab: ")
        if message.content == "!ml hero2 add Minsitthar":
            jxhero2 = "Minsitthar"
            await message.channel.send("Jackson's hero #2 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero2 add Roger":
            jxhero2 = "Roger"
            await message.channel.send("Jackson's hero #2 is now Roger! :wolf: ")
        if message.content == "!ml hero2 add Ruby":
            jxhero2 = "Ruby"
            await message.channel.send("Jackson's hero #2 is now Ruby! :heart: ")
        if message.content == "!ml hero2 add Sun":
            jxhero2 = "Sun"
            await message.channel.send("Jackson's hero #2 is now Sun! :monkey_face: ")
        if message.content == "!ml hero2 add Thamuz":
            jxhero2 = "Thamuz"
            await message.channel.send("Jackson's hero #2 is now Thamuz! :rage: ")
        if message.content == "!ml hero2 add Terizla":
            jxhero2 = "Terizla"
            await message.channel.send("Jackson's hero #2 is now Terizla! :hammer: ")
        if message.content == "!ml hero2 add Zilong":
            jxhero2 = "Zilong"
            await message.channel.send("Jackson's hero #2 is now Zilong! :dragon: ")
        if message.content == "!ml hero2 add Fanny":
            jxhero2 = "Fanny"
            await message.channel.send("Jackson's hero #2 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero2 add Gusion":
            jxhero2 = "Gusion"
            await message.channel.send(
                "Jackson's hero #2 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero2 add Hanzo":
            jxhero2 = "Hanzo"
            await message.channel.send("Jackson's hero #2 is now Hanzo! :ghost: ")
        if message.content == "!ml hero2 add Hayabusa":
            jxhero2 = "Hayabusa"
            await message.channel.send("Jackson's hero #2 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero2 add Helcurt":
            jxhero2 = "Helcurt"
            await message.channel.send("Jackson's hero #2 is now Helcurt! :mute:  ")
        if message.content == "!ml hero2 add Karina":
            jxhero2 = "Karina"
            await message.channel.send("Jackson's hero #2 is now Karina! :purple_heart: ")
        if message.content == "!ml hero2 add Lancelot":
            jxhero2 = "Lancelot"
            await message.channel.send("Jackson's hero #2 is now Lancelot! :fencer: ")
        if message.content == "!ml hero2 add Lesley":
            jxhero2 = "Lesley"
            await message.channel.send("Jackson's hero #2 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero2 add Natalia":
            jxhero2 = "Natalia"
            await message.channel.send("Jackson's hero #2 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero2 add Saber":
            jxhero2 = "Saber"
            await message.channel.send("Jackson's hero #2 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero2 add Selena":
            jxhero2 = "Selena"
            await message.channel.send("Jackson's hero #2 is now Selena! :sleeping:  ")
        if message.content == "!ml hero2 add Alice":
            jxhero2 = "Alice"
            await message.channel.send("Jackson's hero #2 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero2 add Aurora":
            jxhero2 = "Aurora"
            await message.channel.send("Jackson's hero #2 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jxhero2 = "Chang'e"
            await message.channel.send("Jackson's hero #2 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero2 add Cyclops":
            jxhero2 = "Cyclops"
            await message.channel.send("Jackson's hero #2 is now Cyclops! :eye:  ")
        if message.content == "!ml hero2 add Eudora":
            jxhero2 = "Eudora"
            await message.channel.send("Jackson's hero #2 is now Eudora! :zap: ")
        if message.content == "!ml hero2 add Faramis":
            jxhero2 = "Faramis"
            await message.channel.send("Jackson's hero #2 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero2 add Gord":
            jxhero2 = "Gord"
            await message.channel.send("Jackson's hero #2 is now Gord! :snowboarder:")
        if message.content == "!ml hero2 add Harith":
            jxhero2 = "Harith"
            await message.channel.send("Jackson's hero #2 is now Harith! :older_man: ")
        if message.content == "!ml hero2 add Harley":
            jxhero2 = "Harley"
            await message.channel.send("Jackson's hero #2 is now Harley! :tophat: ")
        if message.content == "!ml hero2 add Kadita":
            jxhero2 = "Kadita"
            await message.channel.send("Jackson's hero #2 is now Kadita! :droplet: ")
        if message.content == "!ml hero2 add Kagura":
            jxhero2 = "Kagura"
            await message.channel.send("Jackson's hero #2 is now Kagura! :umbrella2:  ")
        if message.content == "!ml hero2 add Lunox":
            jxhero2 = "Lunox"
            await message.channel.send("Jackson's hero #2 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero2 add Lylia":
            jxhero2 = "Lylia"
            await message.channel.send("Jackson's hero #2 is now Lylia! :boom: ")
        if message.content == "!ml hero2 add Nana":
            jxhero2 = "Nana"
            await message.channel.send("Jackson's hero #2 is now Nana! :cat:  ")
        if message.content == "!ml hero2 add Odette":
            jxhero2 = "Odette"
            await message.channel.send("Jackson's hero #2 is now Odette! :duck: ")
        if message.content == "!ml hero2 add Pharsa":
            jxhero2 = "Pharsa"
            await message.channel.send("Jackson's hero #2 is now Pharsa! :dove:  ")
        if message.content == "!ml hero2 add Vale":
            jxhero2 = "Vale"
            await message.channel.send("Jackson's hero #2 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero2 add Valir":
            jxhero2 = "Valir"
            await message.channel.send("Jackson's hero #2 is now Valir! :fire:")
        if message.content == "!ml hero2 add Vexanna":
            jxhero2 = "Vexanna"
            await message.channel.send("Jackson's hero #2 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero2 add Bruno":
            jxhero2 = "Bruno"
            await message.channel.send("Jackson's hero #2 is now Bruno! :soccer:  ")
        if message.content == "!ml hero2 add Claude":
            jxhero2 = "Claude"
            await message.channel.send("Jackson's hero #2 is now Claude! :monkey:  ")
        if message.content == "!ml hero2 add Clint":
            jxhero2 = "Clint"
            await message.channel.send("Jackson's hero #2 is now Clint! :cowboy: ")
        if message.content == "!ml hero2 add Granger":
            jxhero2 = "Granger"
            await message.channel.send("Jackson's hero #2 is now Granger! :violin: ")
        if message.content == "!ml hero2 add Hanabi":
            jxhero2 = "Hanabi"
            await message.channel.send("Jackson's hero #2 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero2 add Irithel":
            jxhero2 = "Irithel"
            await message.channel.send("Jackson's hero #2 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero2 add Karrie":
            jxhero2 = "Karrie"
            await message.channel.send(
                "Jackson's hero #2 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero2 add Kimmy":
            jxhero2 = "Kimmy"
            await message.channel.send("Jackson's hero #2 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero2 add Layla":
            jxhero2 = "Layla"
            await message.channel.send("Jackson's hero #2 is now Layla! :haircut:  ")
        if message.content == "!ml hero2 add Miya":
            jxhero2 = "Miya"
            await message.channel.send("Jackson's hero #2 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero2 add Moskov":
            jxhero2 = "Moskov"
            await message.channel.send("Jackson's hero #2 is now Moskov! :imp: ")
        if message.content == "!ml hero2 add Yi Sun-Shin":
            jxhero2 = "Yi Sun-Shin"
            await message.channel.send("Jackson's hero #2 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero2 add Angela":
            jxhero2 = "Angela"
            await message.channel.send("Jackson's hero #2 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero2 add Diggie":
            jxhero2 = "Diggie"
            await message.channel.send("Jackson's hero #2 is now Diggie! :owl: ")
        if message.content == "!ml hero2 add Estes":
            jxhero2 = "Estes"
            await message.channel.send("Jackson's hero #2 is now Estes! :ear:  ")
        if message.content == "!ml hero2 add Rafaela":
            jxhero2 = "Rafaela"
            await message.channel.send("Jackson's hero #2 is now Rafaela! :angel: ")
        if message.content == "!ml hero2 add Rynn":
            jxhero2 = "Rynn"
            await message.channel.send("Jackson's hero #2 is now Rynn! ")
        if message.content == "!ml hero3 add Akai":
            global jxhero3
            jxhero3 = "Akai"
            await message.channel.send("Jackson's hero #3 is now Akai! :panda_face: ")
        if message.content == "!ml hero3 add Balmond":
            jxhero3 = "Balmond"
            await message.channel.send("Jackson's hero #3 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero3 add Belerick":
            jxhero3 = "Belerick"
            await message.channel.send("Jackson's hero #3 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero3 add Franco":
            jxhero3 = "Franco"
            await message.channel.send("Jackson's hero #3 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero3 add Esmerelda":
            jxhero3 = "Esmerelda"
            await message.channel.send("Jackson's hero #3 is now Esmerelda! :shield: ")
        if message.content == "!ml hero3 add Gatotkaca":
            jxhero3 = "Gatotkaca"
            await message.channel.send("Jackson's hero #3 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero3 add Grock":
            jxhero3 = "Grock"
            await message.channel.send("Jackson's hero #3 is now Grock! :european_castle: ")
        if message.content == "!ml hero3 add Hilda":
            jxhero3 = "Hilda"
            await message.channel.send("Jackson's hero #3 is now Hilda! :runner: ")
        if message.content == "!ml hero3 add Hylos":
            jxhero3 = "Hylos"
            await message.channel.send("Jackson's hero #3 is now Hylos! :unicorn: ")
        if message.content == "!ml hero3 add Johnson":
            jxhero3 = "Johnson"
            await message.channel.send("Jackson's hero #3 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero3 add Khufra":
            jxhero3 = "Khufra"
            await message.channel.send("Jackson's hero #3 is now Khufra! :clown: ")
        if message.content == "!ml hero3 add Lolita":
            jxhero3 = "Lolita"
            await message.channel.send("Jackson's hero #3 is now Lolita! :lollipop: ")
        if message.content == "!ml hero3 add Masha":
            jxhero3 = "Masha"
            await message.channel.send("Jackson's hero #3 is now Masha! :bear: ")
        if message.content == "!ml hero3 add Minotaur":
            jxhero3 = "Minotaur"
            await message.channel.send("Jackson's hero #3 is now Minotaur! :cow: ")
        if message.content == "!ml hero3 add Tigreal":
            jxhero3 = "Tigreal"
            await message.channel.send("Jackson's hero #3 is now Tigreal! :moyai: ")
        if message.content == "!ml hero3 add Uranus":
            jxhero3 = "Uranus"
            await message.channel.send("Jackson's hero #3 is now Uranus! :peach: ")
        if message.content == "!ml hero3 add X.Borg":
            jxhero3 = "X.Borg"
            await message.channel.send("Jackson's hero #3 is now X.Borg! :fire: ")
        if message.content == "!ml hero3 add Aldous":
            jxhero3 = "Aldous"
            await message.channel.send("Jackson's hero #3 is now Aldous! :fist: ")
        if message.content == "!ml hero3 add Alpha":
            jxhero3 = "Alpha"
            await message.channel.send("Jackson's hero #3 is now Alpha! :airplane: ")
        if message.content == "!ml hero3 add Alucard":
            jxhero3 = "Alucard"
            await message.channel.send("Jackson's hero #3 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero3 add Argus":
            jxhero3 = "Argus"
            await message.channel.send("Jackson's hero #3 is now Argus! :angel: ")
        if message.content == "!ml hero3 add Badang":
            jxhero3 = "Badang"
            await message.channel.send("Jackson's hero #3 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero3 add Bane":
            jxhero3 = "Bane"
            await message.channel.send("Jackson's hero #3 is now Bane! :octopus: ")
        if message.content == "!ml hero3 add Chou":
            jxhero3 = "Chou"
            await message.channel.send("Jackson's hero #3 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero3 add Dyrroth":
            jxhero3 = "Dyrroth"
            await message.channel.send("Jackson's hero #3 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero3 add Freya":
            jxhero3 = "Freya"
            await message.channel.send("Jackson's hero #3 is now Freya! :hammer: ")
        if message.content == "!ml hero3 add Guinevere":
            jxhero3 = "Guinevere"
            await message.channel.send("Jackson's hero #3 is now Guinevere! :dress:  ")
        if message.content == "!ml hero3 add Jawhead":
            jxhero3 = "Jawhead"
            await message.channel.send("Jackson's hero #3 is now Jawhead! :robot: ")
        if message.content == "!ml hero3 add Kaja":
            jxhero3 = "Kaja"
            await message.channel.send("Jackson's hero #3 is now Kaja! :bird: ")
        if message.content == "!ml hero3 add Lapu-Lapu":
            jxhero3 = "Lapu-Lapu"
            await message.channel.send("Jackson's hero #3 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero3 add Leomord":
            jxhero3 = "Leomord"
            await message.channel.send("Jackson's hero #3 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero3 add Martis":
            jxhero3 = "Martis"
            await message.channel.send("Jackson's hero #3 is now Martis! :crab: ")
        if message.content == "!ml hero3 add Minsitthar":
            jxhero3 = "Minsitthar"
            await message.channel.send("Jackson's hero #3 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero3 add Roger":
            jxhero3 = "Roger"
            await message.channel.send("Jackson's hero #3 is now Roger! :wolf: ")
        if message.content == "!ml hero3 add Ruby":
            jxhero3 = "Ruby"
            await message.channel.send("Jackson's hero #3 is now Ruby! :heart: ")
        if message.content == "!ml hero3 add Sun":
            jxhero3 = "Sun"
            await message.channel.send("Jackson's hero #3 is now Sun! :monkey_face: ")
        if message.content == "!ml hero3 add Thamuz":
            jxhero3 = "Thamuz"
            await message.channel.send("Jackson's hero #3 is now Thamuz! :rage: ")
        if message.content == "!ml hero3 add Terizla":
            jxhero3 = "Terizla"
            await message.channel.send("Jackson's hero #3 is now Terizla! :hammer: ")
        if message.content == "!ml hero3 add Zilong":
            jxhero3 = "Zilong"
            await message.channel.send("Jackson's hero #3 is now Zilong! :dragon: ")
        if message.content == "!ml hero3 add Fanny":
            jxhero3 = "Fanny"
            await message.channel.send("Jackson's hero #3 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero3 add Gusion":
            jxhero3 = "Gusion"
            await message.channel.send(
                "Jackson's hero #3 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero3 add Hanzo":
            jxhero3 = "Hanzo"
            await message.channel.send("Jackson's hero #3 is now Hanzo! :ghost: ")
        if message.content == "!ml hero3 add Hayabusa":
            jxhero3 = "Hayabusa"
            await message.channel.send("Jackson's hero #3 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero3 add Helcurt":
            jxhero3 = "Helcurt"
            await message.channel.send("Jackson's hero #3 is now Helcurt! :mute:  ")
        if message.content == "!ml hero3 add Karina":
            jxhero3 = "Karina"
            await message.channel.send("Jackson's hero #3 is now Karina! :purple_heart: ")
        if message.content == "!ml hero3 add Lancelot":
            jxhero3 = "Lancelot"
            await message.channel.send("Jackson's hero #3 is now Lancelot! :fencer: ")
        if message.content == "!ml hero3 add Lesley":
            jxhero3 = "Lesley"
            await message.channel.send("Jackson's hero #3 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero3 add Natalia":
            jxhero3 = "Natalia"
            await message.channel.send("Jackson's hero #3 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero3 add Saber":
            jxhero3 = "Saber"
            await message.channel.send("Jackson's hero #3 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero3 add Selena":
            jxhero3 = "Selena"
            await message.channel.send("Jackson's hero #3 is now Selena! :sleeping:  ")
        if message.content == "!ml hero3 add Alice":
            jxhero3 = "Alice"
            await message.channel.send("Jackson's hero #3 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero3 add Aurora":
            jxhero3 = "Aurora"
            await message.channel.send("Jackson's hero #3 is now Aurora! :snow: ")
        if message.content == "!ml hero3 add Chang'e":
            jxhero3 = "Chang'e"
            await message.channel.send("Jackson's hero #3 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero3 add Cyclops":
            jxhero3 = "Cyclops"
            await message.channel.send("Jackson's hero #3 is now Cyclops! :eye:  ")
        if message.content == "!ml hero3 add Eudora":
            jxhero3 = "Eudora"
            await message.channel.send("Jackson's hero #3 is now Eudora! :zap: ")
        if message.content == "!ml hero3 add Faramis":
            jxhero3 = "Faramis"
            await message.channel.send("Jackson's hero #3 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero3 add Gord":
            jxhero3 = "Gord"
            await message.channel.send("Jackson's hero #3 is now Gord! :snowboarder:")
        if message.content == "!ml hero3 add Harith":
            jxhero3 = "Harith"
            await message.channel.send("Jackson's hero #3 is now Harith! :older_man: ")
        if message.content == "!ml hero3 add Harley":
            jxhero3 = "Harley"
            await message.channel.send("Jackson's hero #3 is now Harley! :tophat: ")
        if message.content == "!ml hero3 add Kadita":
            jxhero3 = "Kadita"
            await message.channel.send("Jackson's hero #3 is now Kadita! :droplet: ")
        if message.content == "!ml hero3 add Kagura":
            jxhero3 = "Kagura"
            await message.channel.send("Jackson's hero #3 is now Kagura! :umbrella2:  ")
        if message.content == "!ml hero3 add Lunox":
            jxhero3 = "Lunox"
            await message.channel.send("Jackson's hero #3 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero3 add Lylia":
            jxhero3 = "Lylia"
            await message.channel.send("Jackson's hero #3 is now Lylia! :boom: ")
        if message.content == "!ml hero3 add Nana":
            jxhero3 = "Nana"
            await message.channel.send("Jackson's hero #3 is now Nana! :cat:  ")
        if message.content == "!ml hero3 add Odette":
            jxhero3 = "Odette"
            await message.channel.send("Jackson's hero #3 is now Odette! :duck: ")
        if message.content == "!ml hero3 add Pharsa":
            jxhero3 = "Pharsa"
            await message.channel.send("Jackson's hero #3 is now Pharsa! :dove:  ")
        if message.content == "!ml hero3 add Vale":
            jxhero3 = "Vale"
            await message.channel.send("Jackson's hero #3 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero3 add Valir":
            jxhero3 = "Valir"
            await message.channel.send("Jackson's hero #3 is now Valir! :fire:")
        if message.content == "!ml hero3 add Vexanna":
            jxhero3 = "Vexanna"
            await message.channel.send("Jackson's hero #3 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero3 add Bruno":
            jxhero3 = "Bruno"
            await message.channel.send("Jackson's hero #3 is now Bruno! :soccer:  ")
        if message.content == "!ml hero3 add Claude":
            jxhero3 = "Claude"
            await message.channel.send("Jackson's hero #3 is now Claude! :monkey:  ")
        if message.content == "!ml hero3 add Clint":
            jxhero3 = "Clint"
            await message.channel.send("Jackson's hero #3 is now Clint! :cowboy: ")
        if message.content == "!ml hero3 add Granger":
            jxhero3 = "Granger"
            await message.channel.send("Jackson's hero #3 is now Granger! :violin: ")
        if message.content == "!ml hero3 add Hanabi":
            jxhero3 = "Hanabi"
            await message.channel.send("Jackson's hero #3 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero3 add Irithel":
            jxhero3 = "Irithel"
            await message.channel.send("Jackson's hero #3 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero3 add Karrie":
            jxhero3 = "Karrie"
            await message.channel.send(
                "Jackson's hero #3 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero3 add Kimmy":
            jxhero3 = "Kimmy"
            await message.channel.send("Jackson's hero #3 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero3 add Layla":
            jxhero3 = "Layla"
            await message.channel.send("Jackson's hero #3 is now Layla! :haircut:  ")
        if message.content == "!ml hero3 add Miya":
            jxhero3 = "Miya"
            await message.channel.send("Jackson's hero #3 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero3 add Moskov":
            jxhero3 = "Moskov"
            await message.channel.send("Jackson's hero #3 is now Moskov! :imp: ")
        if message.content == "!ml hero3 add Yi Sun-Shin":
            jxhero3 = "Yi Sun-Shin"
            await message.channel.send("Jackson's hero #3 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero3 add Angela":
            jxhero3 = "Angela"
            await message.channel.send("Jackson's hero #3 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero3 add Diggie":
            jxhero3 = "Diggie"
            await message.channel.send("Jackson's hero #3 is now Diggie! :owl: ")
        if message.content == "!ml hero3 add Estes":
            jxhero3 = "Estes"
            await message.channel.send("Jackson's hero #3 is now Estes! :ear:  ")
        if message.content == "!ml hero3 add Rafaela":
            jxhero3 = "Rafaela"
            await message.channel.send("Jackson's hero #3 is now Rafaela! :angel: ")
        if message.content == "!ml hero3 add Rynn":
            jxhero3 = "Rynn"
            await message.channel.send("Jackson's hero #3 is now Rynn! ")
        if message.content == "!ml hero4 add Akai":
            global jxhero4
            jxhero4 = "Akai"
            await message.channel.send("Jackson's hero #4 is now Akai! :panda_face: ")
        if message.content == "!ml hero4 add Balmond":
            jxhero4 = "Balmond"
            await message.channel.send("Jackson's hero #4 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero4 add Belerick":
            jxhero4 = "Belerick"
            await message.channel.send("Jackson's hero #4 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero4 add Franco":
            jxhero4 = "Franco"
            await message.channel.send("Jackson's hero #4 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero4 add Esmerelda":
            jxhero4 = "Esmerelda"
            await message.channel.send("Jackson's hero #4 is now Esmerelda! :shield: ")
        if message.content == "!ml hero4 add Gatotkaca":
            jxhero4 = "Gatotkaca"
            await message.channel.send("Jackson's hero #4 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero4 add Grock":
            jxhero4 = "Grock"
            await message.channel.send("Jackson's hero #4 is now Grock! :european_castle: ")
        if message.content == "!ml hero4 add Hilda":
            jxhero4 = "Hilda"
            await message.channel.send("Jackson's hero #4 is now Hilda! :runner: ")
        if message.content == "!ml hero4 add Hylos":
            jxhero4 = "Hylos"
            await message.channel.send("Jackson's hero #4 is now Hylos! :unicorn: ")
        if message.content == "!ml hero4 add Johnson":
            jxhero4 = "Johnson"
            await message.channel.send("Jackson's hero #4 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero4 add Khufra":
            jxhero4 = "Khufra"
            await message.channel.send("Jackson's hero #4 is now Khufra! :clown: ")
        if message.content == "!ml hero4 add Lolita":
            jxhero4 = "Lolita"
            await message.channel.send("Jackson's hero #4 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jxhero4 = "Masha"
            await message.channel.send("Jackson's hero #4 is now Masha! :bear: ")
        if message.content == "!ml hero4 add Minotaur":
            jxhero4 = "Minotaur"
            await message.channel.send("Jackson's hero #4 is now Minotaur! :cow: ")
        if message.content == "!ml hero4 add Tigreal":
            jxhero4 = "Tigreal"
            await message.channel.send("Jackson's hero #4 is now Tigreal! :moyai: ")
        if message.content == "!ml hero4 add Uranus":
            jxhero4 = "Uranus"
            await message.channel.send("Jackson's hero #4 is now Uranus! :peach: ")
        if message.content == "!ml hero4 add X.Borg":
            jxhero4 = "X.Borg"
            await message.channel.send("Jackson's hero #4 is now X.Borg! :fire: ")
        if message.content == "!ml hero4 add Aldous":
            jxhero4 = "Aldous"
            await message.channel.send("Jackson's hero #4 is now Aldous! :fist: ")
        if message.content == "!ml hero4 add Alpha":
            jxhero4 = "Alpha"
            await message.channel.send("Jackson's hero #4 is now Alpha! :airplane: ")
        if message.content == "!ml hero4 add Alucard":
            jxhero4 = "Alucard"
            await message.channel.send("Jackson's hero #4 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero4 add Argus":
            jxhero4 = "Argus"
            await message.channel.send("Jackson's hero #4 is now Argus! :angel: ")
        if message.content == "!ml hero4 add Badang":
            jxhero4 = "Badang"
            await message.channel.send("Jackson's hero #4 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero4 add Bane":
            jxhero4 = "Bane"
            await message.channel.send("Jackson's hero #4 is now Bane! :octopus: ")
        if message.content == "!ml hero4 add Chou":
            jxhero4 = "Chou"
            await message.channel.send("Jackson's hero #4 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero4 add Dyrroth":
            jxhero4 = "Dyrroth"
            await message.channel.send("Jackson's hero #4 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero4 add Freya":
            jxhero4 = "Freya"
            await message.channel.send("Jackson's hero #4 is now Freya! :hammer: ")
        if message.content == "!ml hero4 add Guinevere":
            jxhero4 = "Guinevere"
            await message.channel.send("Jackson's hero #4 is now Guinevere! :dress:  ")
        if message.content == "!ml hero4 add Jawhead":
            jxhero4 = "Jawhead"
            await message.channel.send("Jackson's hero #4 is now Jawhead! :robot: ")
        if message.content == "!ml hero4 add Kaja":
            jxhero4 = "Kaja"
            await message.channel.send("Jackson's hero #4 is now Kaja! :bird: ")
        if message.content == "!ml hero4 add Lapu-Lapu":
            jxhero4 = "Lapu-Lapu"
            await message.channel.send("Jackson's hero #4 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero4 add Leomord":
            jxhero4 = "Leomord"
            await message.channel.send("Jackson's hero #4 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero4 add Martis":
            jxhero4 = "Martis"
            await message.channel.send("Jackson's hero #4 is now Martis! :crab: ")
        if message.content == "!ml hero4 add Minsitthar":
            jxhero4 = "Minsitthar"
            await message.channel.send("Jackson's hero #4 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero4 add Roger":
            jxhero4 = "Roger"
            await message.channel.send("Jackson's hero #4 is now Roger! :wolf: ")
        if message.content == "!ml hero4 add Ruby":
            jxhero4 = "Ruby"
            await message.channel.send("Jackson's hero #4 is now Ruby! :heart: ")
        if message.content == "!ml hero4 add Sun":
            jxhero4 = "Sun"
            await message.channel.send("Jackson's hero #4 is now Sun! :monkey_face: ")
        if message.content == "!ml hero4 add Thamuz":
            jxhero4 = "Thamuz"
            await message.channel.send("Jackson's hero #4 is now Thamuz! :rage: ")
        if message.content == "!ml hero4 add Terizla":
            jxhero4 = "Terizla"
            await message.channel.send("Jackson's hero #4 is now Terizla! :hammer: ")
        if message.content == "!ml hero4 add Zilong":
            jxhero4 = "Zilong"
            await message.channel.send("Jackson's hero #4 is now Zilong! :dragon: ")
        if message.content == "!ml hero4 add Fanny":
            jxhero4 = "Fanny"
            await message.channel.send("Jackson's hero #4 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero4 add Gusion":
            jxhero4 = "Gusion"
            await message.channel.send(
                "Jackson's hero #4 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero4 add Hanzo":
            jxhero4 = "Hanzo"
            await message.channel.send("Jackson's hero #4 is now Hanzo! :ghost: ")
        if message.content == "!ml hero4 add Hayabusa":
            jxhero4 = "Hayabusa"
            await message.channel.send("Jackson's hero #4 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero4 add Helcurt":
            jxhero4 = "Helcurt"
            await message.channel.send("Jackson's hero #4 is now Helcurt! :mute:  ")
        if message.content == "!ml hero4 add Karina":
            jxhero4 = "Karina"
            await message.channel.send("Jackson's hero #4 is now Karina! :purple_heart: ")
        if message.content == "!ml hero4 add Lancelot":
            jxhero4 = "Lancelot"
            await message.channel.send("Jackson's hero #4 is now Lancelot! :fencer: ")
        if message.content == "!ml hero4 add Lesley":
            jxhero4 = "Lesley"
            await message.channel.send("Jackson's hero #4 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero4 add Natalia":
            jxhero4 = "Natalia"
            await message.channel.send("Jackson's hero #4 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero4 add Saber":
            jxhero4 = "Saber"
            await message.channel.send("Jackson's hero #4 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero4 add Selena":
            jxhero4 = "Selena"
            await message.channel.send("Jackson's hero #4 is now Selena! :sleeping:  ")
        if message.content == "!ml hero4 add Alice":
            jxhero4 = "Alice"
            await message.channel.send("Jackson's hero #4 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero4 add Aurora":
            jxhero4 = "Aurora"
            await message.channel.send("Jackson's hero #4 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jxhero4 = "Chang'e"
            await message.channel.send("Jackson's hero #4 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero4 add Cyclops":
            jxhero4 = "Cyclops"
            await message.channel.send("Jackson's hero #4 is now Cyclops! :eye:  ")
        if message.content == "!ml hero4 add Eudora":
            jxhero4 = "Eudora"
            await message.channel.send("Jackson's hero #4 is now Eudora! :zap: ")
        if message.content == "!ml hero4 add Faramis":
            jxhero4 = "Faramis"
            await message.channel.send("Jackson's hero #4 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero4 add Gord":
            jxhero4 = "Gord"
            await message.channel.send("Jackson's hero #4 is now Gord! :snowboarder:")
        if message.content == "!ml hero4 add Harith":
            jxhero4 = "Harith"
            await message.channel.send("Jackson's hero #4 is now Harith! :older_man: ")
        if message.content == "!ml hero4 add Harley":
            jxhero4 = "Harley"
            await message.channel.send("Jackson's hero #4 is now Harley! :tophat: ")
        if message.content == "!ml hero4 add Kadita":
            jxhero4 = "Kadita"
            await message.channel.send("Jackson's hero #4 is now Kadita! :droplet: ")
        if message.content == "!ml hero4 add Kagura":
            jxhero4 = "Kagura"
            await message.channel.send("Jackson's hero #4 is now Kagura! :umbrella4:  ")
        if message.content == "!ml hero4 add Lunox":
            jxhero4 = "Lunox"
            await message.channel.send("Jackson's hero #4 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero4 add Lylia":
            jxhero4 = "Lylia"
            await message.channel.send("Jackson's hero #4 is now Lylia! :boom: ")
        if message.content == "!ml hero4 add Nana":
            jxhero4 = "Nana"
            await message.channel.send("Jackson's hero #4 is now Nana! :cat:  ")
        if message.content == "!ml hero4 add Odette":
            jxhero4 = "Odette"
            await message.channel.send("Jackson's hero #4 is now Odette! :duck: ")
        if message.content == "!ml hero4 add Pharsa":
            jxhero4 = "Pharsa"
            await message.channel.send("Jackson's hero #4 is now Pharsa! :dove:  ")
        if message.content == "!ml hero4 add Vale":
            jxhero4 = "Vale"
            await message.channel.send("Jackson's hero #4 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero4 add Valir":
            jxhero4 = "Valir"
            await message.channel.send("Jackson's hero #4 is now Valir! :fire:")
        if message.content == "!ml hero4 add Vexanna":
            jxhero4 = "Vexanna"
            await message.channel.send("Jackson's hero #4 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero4 add Bruno":
            jxhero4 = "Bruno"
            await message.channel.send("Jackson's hero #4 is now Bruno! :soccer:  ")
        if message.content == "!ml hero4 add Claude":
            jxhero4 = "Claude"
            await message.channel.send("Jackson's hero #4 is now Claude! :monkey:  ")
        if message.content == "!ml hero4 add Clint":
            jxhero4 = "Clint"
            await message.channel.send("Jackson's hero #4 is now Clint! :cowboy: ")
        if message.content == "!ml hero4 add Granger":
            jxhero4 = "Granger"
            await message.channel.send("Jackson's hero #4 is now Granger! :violin: ")
        if message.content == "!ml hero4 add Hanabi":
            jxhero4 = "Hanabi"
            await message.channel.send("Jackson's hero #4 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero4 add Irithel":
            jxhero4 = "Irithel"
            await message.channel.send("Jackson's hero #4 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero4 add Karrie":
            jxhero4 = "Karrie"
            await message.channel.send(
                "Jackson's hero #4 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero4 add Kimmy":
            jxhero4 = "Kimmy"
            await message.channel.send("Jackson's hero #4 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero4 add Layla":
            jxhero4 = "Layla"
            await message.channel.send("Jackson's hero #4 is now Layla! :haircut:  ")
        if message.content == "!ml hero4 add Miya":
            jxhero4 = "Miya"
            await message.channel.send("Jackson's hero #4 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero4 add Moskov":
            jxhero4 = "Moskov"
            await message.channel.send("Jackson's hero #4 is now Moskov! :imp: ")
        if message.content == "!ml hero4 add Yi Sun-Shin":
            jxhero4 = "Yi Sun-Shin"
            await message.channel.send("Jackson's hero #4 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero4 add Angela":
            jxhero4 = "Angela"
            await message.channel.send("Jackson's hero #4 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero4 add Diggie":
            jxhero4 = "Diggie"
            await message.channel.send("Jackson's hero #4 is now Diggie! :owl: ")
        if message.content == "!ml hero4 add Estes":
            jxhero4 = "Estes"
            await message.channel.send("Jackson's hero #4 is now Estes! :ear:  ")
        if message.content == "!ml hero4 add Rafaela":
            jxhero4 = "Rafaela"
            await message.channel.send("Jackson's hero #4 is now Rafaela! :angel: ")
        if message.content == "!ml hero4 add Rynn":
            jxhero4 = "Rynn"
            await message.channel.send("Jackson's hero #4 is now Rynn! ")
        if message.content == "!ml hero5 add Akai":
            global jxhero5
            jxhero5 = "Akai"
            await message.channel.send("Jackson's hero #5 is now Akai! :panda_face: ")
        if message.content == "!ml hero5 add Balmond":
            jxhero5 = "Balmond"
            await message.channel.send("Jackson's hero #5 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero5 add Belerick":
            jxhero5 = "Belerick"
            await message.channel.send("Jackson's hero #5 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero5 add Franco":
            jxhero5 = "Franco"
            await message.channel.send("Jackson's hero #5 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero5 add Esmerelda":
            jxhero5 = "Esmerelda"
            await message.channel.send("Jackson's hero #5 is now Esmerelda! :shield: ")
        if message.content == "!ml hero5 add Gatotkaca":
            jxhero5 = "Gatotkaca"
            await message.channel.send("Jackson's hero #5 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero5 add Grock":
            jxhero5 = "Grock"
            await message.channel.send("Jackson's hero #5 is now Grock! :european_castle: ")
        if message.content == "!ml hero5 add Hilda":
            jxhero5 = "Hilda"
            await message.channel.send("Jackson's hero #5 is now Hilda! :runner: ")
        if message.content == "!ml hero5 add Hylos":
            jxhero5 = "Hylos"
            await message.channel.send("Jackson's hero #5 is now Hylos! :unicorn: ")
        if message.content == "!ml hero5 add Johnson":
            jxhero5 = "Johnson"
            await message.channel.send("Jackson's hero #5 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero5 add Khufra":
            jxhero5 = "Khufra"
            await message.channel.send("Jackson's hero #5 is now Khufra! :clown: ")
        if message.content == "!ml hero5 add Lolita":
            jxhero5 = "Lolita"
            await message.channel.send("Jackson's hero #5 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jxhero5 = "Masha"
            await message.channel.send("Jackson's hero #5 is now Masha! :bear: ")
        if message.content == "!ml hero5 add Minotaur":
            jxhero5 = "Minotaur"
            await message.channel.send("Jackson's hero #5 is now Minotaur! :cow: ")
        if message.content == "!ml hero5 add Tigreal":
            jxhero5 = "Tigreal"
            await message.channel.send("Jackson's hero #5 is now Tigreal! :moyai: ")
        if message.content == "!ml hero5 add Uranus":
            jxhero5 = "Uranus"
            await message.channel.send("Jackson's hero #5 is now Uranus! :peach: ")
        if message.content == "!ml hero5 add X.Borg":
            jxhero5 = "X.Borg"
            await message.channel.send("Jackson's hero #5 is now X.Borg! :fire: ")
        if message.content == "!ml hero5 add Aldous":
            jxhero5 = "Aldous"
            await message.channel.send("Jackson's hero #5 is now Aldous! :fist: ")
        if message.content == "!ml hero5 add Alpha":
            jxhero5 = "Alpha"
            await message.channel.send("Jackson's hero #5 is now Alpha! :airplane: ")
        if message.content == "!ml hero5 add Alucard":
            jxhero5 = "Alucard"
            await message.channel.send("Jackson's hero #5 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero5 add Argus":
            jxhero5 = "Argus"
            await message.channel.send("Jackson's hero #5 is now Argus! :angel: ")
        if message.content == "!ml hero5 add Badang":
            jxhero5 = "Badang"
            await message.channel.send("Jackson's hero #5 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero5 add Bane":
            jxhero5 = "Bane"
            await message.channel.send("Jackson's hero #5 is now Bane! :octopus: ")
        if message.content == "!ml hero5 add Chou":
            jxhero5 = "Chou"
            await message.channel.send("Jackson's hero #5 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero5 add Dyrroth":
            jxhero5 = "Dyrroth"
            await message.channel.send("Jackson's hero #5 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero5 add Freya":
            jxhero5 = "Freya"
            await message.channel.send("Jackson's hero #5 is now Freya! :hammer: ")
        if message.content == "!ml hero5 add Guinevere":
            jxhero5 = "Guinevere"
            await message.channel.send("Jackson's hero #5 is now Guinevere! :dress:  ")
        if message.content == "!ml hero5 add Jawhead":
            jxhero5 = "Jawhead"
            await message.channel.send("Jackson's hero #5 is now Jawhead! :robot: ")
        if message.content == "!ml hero5 add Kaja":
            jxhero5 = "Kaja"
            await message.channel.send("Jackson's hero #5 is now Kaja! :bird: ")
        if message.content == "!ml hero5 add Lapu-Lapu":
            jxhero5 = "Lapu-Lapu"
            await message.channel.send("Jackson's hero #5 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero5 add Leomord":
            jxhero5 = "Leomord"
            await message.channel.send("Jackson's hero #5 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero5 add Martis":
            jxhero5 = "Martis"
            await message.channel.send("Jackson's hero #5 is now Martis! :crab: ")
        if message.content == "!ml hero5 add Minsitthar":
            jxhero5 = "Minsitthar"
            await message.channel.send("Jackson's hero #5 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero5 add Roger":
            jxhero5 = "Roger"
            await message.channel.send("Jackson's hero #5 is now Roger! :wolf: ")
        if message.content == "!ml hero5 add Ruby":
            jxhero5 = "Ruby"
            await message.channel.send("Jackson's hero #5 is now Ruby! :heart: ")
        if message.content == "!ml hero5 add Sun":
            jxhero5 = "Sun"
            await message.channel.send("Jackson's hero #5 is now Sun! :monkey_face: ")
        if message.content == "!ml hero5 add Thamuz":
            jxhero5 = "Thamuz"
            await message.channel.send("Jackson's hero #5 is now Thamuz! :rage: ")
        if message.content == "!ml hero5 add Terizla":
            jxhero5 = "Terizla"
            await message.channel.send("Jackson's hero #5 is now Terizla! :hammer: ")
        if message.content == "!ml hero5 add Zilong":
            jxhero5 = "Zilong"
            await message.channel.send("Jackson's hero #5 is now Zilong! :dragon: ")
        if message.content == "!ml hero5 add Fanny":
            jxhero5 = "Fanny"
            await message.channel.send("Jackson's hero #5 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero5 add Gusion":
            jxhero5 = "Gusion"
            await message.channel.send(
                "Jackson's hero #5 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero5 add Hanzo":
            jxhero5 = "Hanzo"
            await message.channel.send("Jackson's hero #5 is now Hanzo! :ghost: ")
        if message.content == "!ml hero5 add Hayabusa":
            jxhero5 = "Hayabusa"
            await message.channel.send("Jackson's hero #5 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero5 add Helcurt":
            jxhero5 = "Helcurt"
            await message.channel.send("Jackson's hero #5 is now Helcurt! :mute:  ")
        if message.content == "!ml hero5 add Karina":
            jxhero5 = "Karina"
            await message.channel.send("Jackson's hero #5 is now Karina! :purple_heart: ")
        if message.content == "!ml hero5 add Lancelot":
            jxhero5 = "Lancelot"
            await message.channel.send("Jackson's hero #5 is now Lancelot! :fencer: ")
        if message.content == "!ml hero5 add Lesley":
            jxhero5 = "Lesley"
            await message.channel.send("Jackson's hero #5 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero5 add Natalia":
            jxhero5 = "Natalia"
            await message.channel.send("Jackson's hero #5 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero5 add Saber":
            jxhero5 = "Saber"
            await message.channel.send("Jackson's hero #5 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero5 add Selena":
            jxhero5 = "Selena"
            await message.channel.send("Jackson's hero #5 is now Selena! :sleeping:  ")
        if message.content == "!ml hero5 add Alice":
            jxhero5 = "Alice"
            await message.channel.send("Jackson's hero #5 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero5 add Aurora":
            jxhero5 = "Aurora"
            await message.channel.send("Jackson's hero #5 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jxhero5 = "Chang'e"
            await message.channel.send("Jackson's hero #5 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero5 add Cyclops":
            jxhero5 = "Cyclops"
            await message.channel.send("Jackson's hero #5 is now Cyclops! :eye:  ")
        if message.content == "!ml hero5 add Eudora":
            jxhero5 = "Eudora"
            await message.channel.send("Jackson's hero #5 is now Eudora! :zap: ")
        if message.content == "!ml hero5 add Faramis":
            jxhero5 = "Faramis"
            await message.channel.send("Jackson's hero #5 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero5 add Gord":
            jxhero5 = "Gord"
            await message.channel.send("Jackson's hero #5 is now Gord! :snowboarder:")
        if message.content == "!ml hero5 add Harith":
            jxhero5 = "Harith"
            await message.channel.send("Jackson's hero #5 is now Harith! :older_man: ")
        if message.content == "!ml hero5 add Harley":
            jxhero5 = "Harley"
            await message.channel.send("Jackson's hero #5 is now Harley! :tophat: ")
        if message.content == "!ml hero5 add Kadita":
            jxhero5 = "Kadita"
            await message.channel.send("Jackson's hero #5 is now Kadita! :droplet: ")
        if message.content == "!ml hero5 add Kagura":
            jxhero5 = "Kagura"
            await message.channel.send("Jackson's hero #5 is now Kagura! :umbrella5:  ")
        if message.content == "!ml hero5 add Lunox":
            jxhero5 = "Lunox"
            await message.channel.send("Jackson's hero #5 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero5 add Lylia":
            jxhero5 = "Lylia"
            await message.channel.send("Jackson's hero #5 is now Lylia! :boom: ")
        if message.content == "!ml hero5 add Nana":
            jxhero5 = "Nana"
            await message.channel.send("Jackson's hero #5 is now Nana! :cat:  ")
        if message.content == "!ml hero5 add Odette":
            jxhero5 = "Odette"
            await message.channel.send("Jackson's hero #5 is now Odette! :duck: ")
        if message.content == "!ml hero5 add Pharsa":
            jxhero5 = "Pharsa"
            await message.channel.send("Jackson's hero #5 is now Pharsa! :dove:  ")
        if message.content == "!ml hero5 add Vale":
            jxhero5 = "Vale"
            await message.channel.send("Jackson's hero #5 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero5 add Valir":
            jxhero5 = "Valir"
            await message.channel.send("Jackson's hero #5 is now Valir! :fire:")
        if message.content == "!ml hero5 add Vexanna":
            jxhero5 = "Vexanna"
            await message.channel.send("Jackson's hero #5 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero5 add Bruno":
            jxhero5 = "Bruno"
            await message.channel.send("Jackson's hero #5 is now Bruno! :soccer:  ")
        if message.content == "!ml hero5 add Claude":
            jxhero5 = "Claude"
            await message.channel.send("Jackson's hero #5 is now Claude! :monkey:  ")
        if message.content == "!ml hero5 add Clint":
            jxhero5 = "Clint"
            await message.channel.send("Jackson's hero #5 is now Clint! :cowboy: ")
        if message.content == "!ml hero5 add Granger":
            jxhero5 = "Granger"
            await message.channel.send("Jackson's hero #5 is now Granger! :violin: ")
        if message.content == "!ml hero5 add Hanabi":
            jxhero5 = "Hanabi"
            await message.channel.send("Jackson's hero #5 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero5 add Irithel":
            jxhero5 = "Irithel"
            await message.channel.send("Jackson's hero #5 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero5 add Karrie":
            jxhero5 = "Karrie"
            await message.channel.send(
                "Jackson's hero #5 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero5 add Kimmy":
            jxhero5 = "Kimmy"
            await message.channel.send("Jackson's hero #5 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero5 add Layla":
            jxhero5 = "Layla"
            await message.channel.send("Jackson's hero #5 is now Layla! :haircut:  ")
        if message.content == "!ml hero5 add Miya":
            jxhero5 = "Miya"
            await message.channel.send("Jackson's hero #5 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero5 add Moskov":
            jxhero5 = "Moskov"
            await message.channel.send("Jackson's hero #5 is now Moskov! :imp: ")
        if message.content == "!ml hero5 add Yi Sun-Shin":
            jxhero5 = "Yi Sun-Shin"
            await message.channel.send("Jackson's hero #5 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero5 add Angela":
            jxhero5 = "Angela"
            await message.channel.send("Jackson's hero #5 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero5 add Diggie":
            jxhero5 = "Diggie"
            await message.channel.send("Jackson's hero #5 is now Diggie! :owl: ")
        if message.content == "!ml hero5 add Estes":
            jxhero5 = "Estes"
            await message.channel.send("Jackson's hero #5 is now Estes! :ear:  ")
        if message.content == "!ml hero5 add Rafaela":
            jxhero5 = "Rafaela"
            await message.channel.send("Jackson's hero #5 is now Rafaela! :angel: ")
        if message.content == "!ml hero5 add Rynn":
            jxhero5 = "Rynn"
            await message.channel.send("Jackson's hero #5 is now Rynn! ")
        if message.content == "!ml hero6 add Akai":
            global jxhero6
            jxhero6 = "Akai"
            await message.channel.send("Jackson's hero #6 is now Akai! :panda_face: ")
        if message.content == "!ml hero6 add Balmond":
            jxhero6 = "Balmond"
            await message.channel.send("Jackson's hero #6 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero6 add Belerick":
            jxhero6 = "Belerick"
            await message.channel.send("Jackson's hero #6 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero6 add Franco":
            jxhero6 = "Franco"
            await message.channel.send("Jackson's hero #6 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero6 add Esmerelda":
            jxhero6 = "Esmerelda"
            await message.channel.send("Jackson's hero #6 is now Esmerelda! :shield: ")
        if message.content == "!ml hero6 add Gatotkaca":
            jxhero6 = "Gatotkaca"
            await message.channel.send("Jackson's hero #6 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero6 add Grock":
            jxhero6 = "Grock"
            await message.channel.send("Jackson's hero #6 is now Grock! :european_castle: ")
        if message.content == "!ml hero6 add Hilda":
            jxhero6 = "Hilda"
            await message.channel.send("Jackson's hero #6 is now Hilda! :runner: ")
        if message.content == "!ml hero6 add Hylos":
            jxhero6 = "Hylos"
            await message.channel.send("Jackson's hero #6 is now Hylos! :unicorn: ")
        if message.content == "!ml hero6 add Johnson":
            jxhero6 = "Johnson"
            await message.channel.send("Jackson's hero #6 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero6 add Khufra":
            jxhero6 = "Khufra"
            await message.channel.send("Jackson's hero #6 is now Khufra! :clown: ")
        if message.content == "!ml hero6 add Lolita":
            jxhero6 = "Lolita"
            await message.channel.send("Jackson's hero #6 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jxhero6 = "Masha"
            await message.channel.send("Jackson's hero #6 is now Masha! :bear: ")
        if message.content == "!ml hero6 add Minotaur":
            jxhero6 = "Minotaur"
            await message.channel.send("Jackson's hero #6 is now Minotaur! :cow: ")
        if message.content == "!ml hero6 add Tigreal":
            jxhero6 = "Tigreal"
            await message.channel.send("Jackson's hero #6 is now Tigreal! :moyai: ")
        if message.content == "!ml hero6 add Uranus":
            jxhero6 = "Uranus"
            await message.channel.send("Jackson's hero #6 is now Uranus! :peach: ")
        if message.content == "!ml hero6 add X.Borg":
            jxhero6 = "X.Borg"
            await message.channel.send("Jackson's hero #6 is now X.Borg! :fire: ")
        if message.content == "!ml hero6 add Aldous":
            jxhero6 = "Aldous"
            await message.channel.send("Jackson's hero #6 is now Aldous! :fist: ")
        if message.content == "!ml hero6 add Alpha":
            jxhero6 = "Alpha"
            await message.channel.send("Jackson's hero #6 is now Alpha! :airplane: ")
        if message.content == "!ml hero6 add Alucard":
            jxhero6 = "Alucard"
            await message.channel.send("Jackson's hero #6 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero6 add Argus":
            jxhero6 = "Argus"
            await message.channel.send("Jackson's hero #6 is now Argus! :angel: ")
        if message.content == "!ml hero6 add Badang":
            jxhero6 = "Badang"
            await message.channel.send("Jackson's hero #6 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero6 add Bane":
            jxhero6 = "Bane"
            await message.channel.send("Jackson's hero #6 is now Bane! :octopus: ")
        if message.content == "!ml hero6 add Chou":
            jxhero6 = "Chou"
            await message.channel.send("Jackson's hero #6 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero6 add Dyrroth":
            jxhero6 = "Dyrroth"
            await message.channel.send("Jackson's hero #6 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero6 add Freya":
            jxhero6 = "Freya"
            await message.channel.send("Jackson's hero #6 is now Freya! :hammer: ")
        if message.content == "!ml hero6 add Guinevere":
            jxhero6 = "Guinevere"
            await message.channel.send("Jackson's hero #6 is now Guinevere! :dress:  ")
        if message.content == "!ml hero6 add Jawhead":
            jxhero6 = "Jawhead"
            await message.channel.send("Jackson's hero #6 is now Jawhead! :robot: ")
        if message.content == "!ml hero6 add Kaja":
            jxhero6 = "Kaja"
            await message.channel.send("Jackson's hero #6 is now Kaja! :bird: ")
        if message.content == "!ml hero6 add Lapu-Lapu":
            jxhero6 = "Lapu-Lapu"
            await message.channel.send("Jackson's hero #6 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero6 add Leomord":
            jxhero6 = "Leomord"
            await message.channel.send("Jackson's hero #6 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero6 add Martis":
            jxhero6 = "Martis"
            await message.channel.send("Jackson's hero #6 is now Martis! :crab: ")
        if message.content == "!ml hero6 add Minsitthar":
            jxhero6 = "Minsitthar"
            await message.channel.send("Jackson's hero #6 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero6 add Roger":
            jxhero6 = "Roger"
            await message.channel.send("Jackson's hero #6 is now Roger! :wolf: ")
        if message.content == "!ml hero6 add Ruby":
            jxhero6 = "Ruby"
            await message.channel.send("Jackson's hero #6 is now Ruby! :heart: ")
        if message.content == "!ml hero6 add Sun":
            jxhero6 = "Sun"
            await message.channel.send("Jackson's hero #6 is now Sun! :monkey_face: ")
        if message.content == "!ml hero6 add Thamuz":
            jxhero6 = "Thamuz"
            await message.channel.send("Jackson's hero #6 is now Thamuz! :rage: ")
        if message.content == "!ml hero6 add Terizla":
            jxhero6 = "Terizla"
            await message.channel.send("Jackson's hero #6 is now Terizla! :hammer: ")
        if message.content == "!ml hero6 add Zilong":
            jxhero6 = "Zilong"
            await message.channel.send("Jackson's hero #6 is now Zilong! :dragon: ")
        if message.content == "!ml hero6 add Fanny":
            jxhero6 = "Fanny"
            await message.channel.send("Jackson's hero #6 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero6 add Gusion":
            jxhero6 = "Gusion"
            await message.channel.send(
                "Jackson's hero #6 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero6 add Hanzo":
            jxhero6 = "Hanzo"
            await message.channel.send("Jackson's hero #6 is now Hanzo! :ghost: ")
        if message.content == "!ml hero6 add Hayabusa":
            jxhero6 = "Hayabusa"
            await message.channel.send("Jackson's hero #6 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero6 add Helcurt":
            jxhero6 = "Helcurt"
            await message.channel.send("Jackson's hero #6 is now Helcurt! :mute:  ")
        if message.content == "!ml hero6 add Karina":
            jxhero6 = "Karina"
            await message.channel.send("Jackson's hero #6 is now Karina! :purple_heart: ")
        if message.content == "!ml hero6 add Lancelot":
            jxhero6 = "Lancelot"
            await message.channel.send("Jackson's hero #6 is now Lancelot! :fencer: ")
        if message.content == "!ml hero6 add Lesley":
            jxhero6 = "Lesley"
            await message.channel.send("Jackson's hero #6 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero6 add Natalia":
            jxhero6 = "Natalia"
            await message.channel.send("Jackson's hero #6 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero6 add Saber":
            jxhero6 = "Saber"
            await message.channel.send("Jackson's hero #6 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero6 add Selena":
            jxhero6 = "Selena"
            await message.channel.send("Jackson's hero #6 is now Selena! :sleeping:  ")
        if message.content == "!ml hero6 add Alice":
            jxhero6 = "Alice"
            await message.channel.send("Jackson's hero #6 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero6 add Aurora":
            jxhero6 = "Aurora"
            await message.channel.send("Jackson's hero #6 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jxhero6 = "Chang'e"
            await message.channel.send("Jackson's hero #6 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero6 add Cyclops":
            jxhero6 = "Cyclops"
            await message.channel.send("Jackson's hero #6 is now Cyclops! :eye:  ")
        if message.content == "!ml hero6 add Eudora":
            jxhero6 = "Eudora"
            await message.channel.send("Jackson's hero #6 is now Eudora! :zap: ")
        if message.content == "!ml hero6 add Faramis":
            jxhero6 = "Faramis"
            await message.channel.send("Jackson's hero #6 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero6 add Gord":
            jxhero6 = "Gord"
            await message.channel.send("Jackson's hero #6 is now Gord! :snowboarder:")
        if message.content == "!ml hero6 add Harith":
            jxhero6 = "Harith"
            await message.channel.send("Jackson's hero #6 is now Harith! :older_man: ")
        if message.content == "!ml hero6 add Harley":
            jxhero6 = "Harley"
            await message.channel.send("Jackson's hero #6 is now Harley! :tophat: ")
        if message.content == "!ml hero6 add Kadita":
            jxhero6 = "Kadita"
            await message.channel.send("Jackson's hero #6 is now Kadita! :droplet: ")
        if message.content == "!ml hero6 add Kagura":
            jxhero6 = "Kagura"
            await message.channel.send("Jackson's hero #6 is now Kagura! :umbrella6:  ")
        if message.content == "!ml hero6 add Lunox":
            jxhero6 = "Lunox"
            await message.channel.send("Jackson's hero #6 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero6 add Lylia":
            jxhero6 = "Lylia"
            await message.channel.send("Jackson's hero #6 is now Lylia! :boom: ")
        if message.content == "!ml hero6 add Nana":
            jxhero6 = "Nana"
            await message.channel.send("Jackson's hero #6 is now Nana! :cat:  ")
        if message.content == "!ml hero6 add Odette":
            jxhero6 = "Odette"
            await message.channel.send("Jackson's hero #6 is now Odette! :duck: ")
        if message.content == "!ml hero6 add Pharsa":
            jxhero6 = "Pharsa"
            await message.channel.send("Jackson's hero #6 is now Pharsa! :dove:  ")
        if message.content == "!ml hero6 add Vale":
            jxhero6 = "Vale"
            await message.channel.send("Jackson's hero #6 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero6 add Valir":
            jxhero6 = "Valir"
            await message.channel.send("Jackson's hero #6 is now Valir! :fire:")
        if message.content == "!ml hero6 add Vexanna":
            jxhero6 = "Vexanna"
            await message.channel.send("Jackson's hero #6 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero6 add Bruno":
            jxhero6 = "Bruno"
            await message.channel.send("Jackson's hero #6 is now Bruno! :soccer:  ")
        if message.content == "!ml hero6 add Claude":
            jxhero6 = "Claude"
            await message.channel.send("Jackson's hero #6 is now Claude! :monkey:  ")
        if message.content == "!ml hero6 add Clint":
            jxhero6 = "Clint"
            await message.channel.send("Jackson's hero #6 is now Clint! :cowboy: ")
        if message.content == "!ml hero6 add Granger":
            jxhero6 = "Granger"
            await message.channel.send("Jackson's hero #6 is now Granger! :violin: ")
        if message.content == "!ml hero6 add Hanabi":
            jxhero6 = "Hanabi"
            await message.channel.send("Jackson's hero #6 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero6 add Irithel":
            jxhero6 = "Irithel"
            await message.channel.send("Jackson's hero #6 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero6 add Karrie":
            jxhero6 = "Karrie"
            await message.channel.send(
                "Jackson's hero #6 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero6 add Kimmy":
            jxhero6 = "Kimmy"
            await message.channel.send("Jackson's hero #6 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero6 add Layla":
            jxhero6 = "Layla"
            await message.channel.send("Jackson's hero #6 is now Layla! :haircut:  ")
        if message.content == "!ml hero6 add Miya":
            jxhero6 = "Miya"
            await message.channel.send("Jackson's hero #6 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero6 add Moskov":
            jxhero6 = "Moskov"
            await message.channel.send("Jackson's hero #6 is now Moskov! :imp: ")
        if message.content == "!ml hero6 add Yi Sun-Shin":
            jxhero6 = "Yi Sun-Shin"
            await message.channel.send("Jackson's hero #6 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero6 add Angela":
            jxhero6 = "Angela"
            await message.channel.send("Jackson's hero #6 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero6 add Diggie":
            jxhero6 = "Diggie"
            await message.channel.send("Jackson's hero #6 is now Diggie! :owl: ")
        if message.content == "!ml hero6 add Estes":
            jxhero6 = "Estes"
            await message.channel.send("Jackson's hero #6 is now Estes! :ear:  ")
        if message.content == "!ml hero6 add Rafaela":
            jxhero6 = "Rafaela"
            await message.channel.send("Jackson's hero #6 is now Rafaela! :angel: ")
        if message.content == "!ml hero6 add Rynn":
            jxhero6 = "Rynn"
            await message.channel.send("Jackson's hero #6 is now Rynn! ")
        if message.content == "!ml hero7 add Akai":
            global jxhero7
            jxhero7 = "Akai"
            await message.channel.send("Jackson's hero #7 is now Akai! :panda_face: ")
        if message.content == "!ml hero7 add Balmond":
            jxhero7 = "Balmond"
            await message.channel.send("Jackson's hero #7 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero7 add Belerick":
            jxhero7 = "Belerick"
            await message.channel.send("Jackson's hero #7 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero7 add Franco":
            jxhero7 = "Franco"
            await message.channel.send("Jackson's hero #7 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero7 add Esmerelda":
            jxhero7 = "Esmerelda"
            await message.channel.send("Jackson's hero #7 is now Esmerelda! :shield: ")
        if message.content == "!ml hero7 add Gatotkaca":
            jxhero7 = "Gatotkaca"
            await message.channel.send("Jackson's hero #7 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero7 add Grock":
            jxhero7 = "Grock"
            await message.channel.send("Jackson's hero #7 is now Grock! :european_castle: ")
        if message.content == "!ml hero7 add Hilda":
            jxhero7 = "Hilda"
            await message.channel.send("Jackson's hero #7 is now Hilda! :runner: ")
        if message.content == "!ml hero7 add Hylos":
            jxhero7 = "Hylos"
            await message.channel.send("Jackson's hero #7 is now Hylos! :unicorn: ")
        if message.content == "!ml hero7 add Johnson":
            jxhero7 = "Johnson"
            await message.channel.send("Jackson's hero #7 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero7 add Khufra":
            jxhero7 = "Khufra"
            await message.channel.send("Jackson's hero #7 is now Khufra! :clown: ")
        if message.content == "!ml hero7 add Lolita":
            jxhero7 = "Lolita"
            await message.channel.send("Jackson's hero #7 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jxhero7 = "Masha"
            await message.channel.send("Jackson's hero #7 is now Masha! :bear: ")
        if message.content == "!ml hero7 add Minotaur":
            jxhero7 = "Minotaur"
            await message.channel.send("Jackson's hero #7 is now Minotaur! :cow: ")
        if message.content == "!ml hero7 add Tigreal":
            jxhero7 = "Tigreal"
            await message.channel.send("Jackson's hero #7 is now Tigreal! :moyai: ")
        if message.content == "!ml hero7 add Uranus":
            jxhero7 = "Uranus"
            await message.channel.send("Jackson's hero #7 is now Uranus! :peach: ")
        if message.content == "!ml hero7 add X.Borg":
            jxhero7 = "X.Borg"
            await message.channel.send("Jackson's hero #7 is now X.Borg! :fire: ")
        if message.content == "!ml hero7 add Aldous":
            jxhero7 = "Aldous"
            await message.channel.send("Jackson's hero #7 is now Aldous! :fist: ")
        if message.content == "!ml hero7 add Alpha":
            jxhero7 = "Alpha"
            await message.channel.send("Jackson's hero #7 is now Alpha! :airplane: ")
        if message.content == "!ml hero7 add Alucard":
            jxhero7 = "Alucard"
            await message.channel.send("Jackson's hero #7 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero7 add Argus":
            jxhero7 = "Argus"
            await message.channel.send("Jackson's hero #7 is now Argus! :angel: ")
        if message.content == "!ml hero7 add Badang":
            jxhero7 = "Badang"
            await message.channel.send("Jackson's hero #7 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero7 add Bane":
            jxhero7 = "Bane"
            await message.channel.send("Jackson's hero #7 is now Bane! :octopus: ")
        if message.content == "!ml hero7 add Chou":
            jxhero7 = "Chou"
            await message.channel.send("Jackson's hero #7 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero7 add Dyrroth":
            jxhero7 = "Dyrroth"
            await message.channel.send("Jackson's hero #7 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero7 add Freya":
            jxhero7 = "Freya"
            await message.channel.send("Jackson's hero #7 is now Freya! :hammer: ")
        if message.content == "!ml hero7 add Guinevere":
            jxhero7 = "Guinevere"
            await message.channel.send("Jackson's hero #7 is now Guinevere! :dress:  ")
        if message.content == "!ml hero7 add Jawhead":
            jxhero7 = "Jawhead"
            await message.channel.send("Jackson's hero #7 is now Jawhead! :robot: ")
        if message.content == "!ml hero7 add Kaja":
            jxhero7 = "Kaja"
            await message.channel.send("Jackson's hero #7 is now Kaja! :bird: ")
        if message.content == "!ml hero7 add Lapu-Lapu":
            jxhero7 = "Lapu-Lapu"
            await message.channel.send("Jackson's hero #7 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero7 add Leomord":
            jxhero7 = "Leomord"
            await message.channel.send("Jackson's hero #7 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero7 add Martis":
            jxhero7 = "Martis"
            await message.channel.send("Jackson's hero #7 is now Martis! :crab: ")
        if message.content == "!ml hero7 add Minsitthar":
            jxhero7 = "Minsitthar"
            await message.channel.send("Jackson's hero #7 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero7 add Roger":
            jxhero7 = "Roger"
            await message.channel.send("Jackson's hero #7 is now Roger! :wolf: ")
        if message.content == "!ml hero7 add Ruby":
            jxhero7 = "Ruby"
            await message.channel.send("Jackson's hero #7 is now Ruby! :heart: ")
        if message.content == "!ml hero7 add Sun":
            jxhero7 = "Sun"
            await message.channel.send("Jackson's hero #7 is now Sun! :monkey_face: ")
        if message.content == "!ml hero7 add Thamuz":
            jxhero7 = "Thamuz"
            await message.channel.send("Jackson's hero #7 is now Thamuz! :rage: ")
        if message.content == "!ml hero7 add Terizla":
            jxhero7 = "Terizla"
            await message.channel.send("Jackson's hero #7 is now Terizla! :hammer: ")
        if message.content == "!ml hero7 add Zilong":
            jxhero7 = "Zilong"
            await message.channel.send("Jackson's hero #7 is now Zilong! :dragon: ")
        if message.content == "!ml hero7 add Fanny":
            jxhero7 = "Fanny"
            await message.channel.send("Jackson's hero #7 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero7 add Gusion":
            jxhero7 = "Gusion"
            await message.channel.send(
                "Jackson's hero #7 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero7 add Hanzo":
            jxhero7 = "Hanzo"
            await message.channel.send("Jackson's hero #7 is now Hanzo! :ghost: ")
        if message.content == "!ml hero7 add Hayabusa":
            jxhero7 = "Hayabusa"
            await message.channel.send("Jackson's hero #7 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero7 add Helcurt":
            jxhero7 = "Helcurt"
            await message.channel.send("Jackson's hero #7 is now Helcurt! :mute:  ")
        if message.content == "!ml hero7 add Karina":
            jxhero7 = "Karina"
            await message.channel.send("Jackson's hero #7 is now Karina! :purple_heart: ")
        if message.content == "!ml hero7 add Lancelot":
            jxhero7 = "Lancelot"
            await message.channel.send("Jackson's hero #7 is now Lancelot! :fencer: ")
        if message.content == "!ml hero7 add Lesley":
            jxhero7 = "Lesley"
            await message.channel.send("Jackson's hero #7 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero7 add Natalia":
            jxhero7 = "Natalia"
            await message.channel.send("Jackson's hero #7 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero7 add Saber":
            jxhero7 = "Saber"
            await message.channel.send("Jackson's hero #7 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero7 add Selena":
            jxhero7 = "Selena"
            await message.channel.send("Jackson's hero #7 is now Selena! :sleeping:  ")
        if message.content == "!ml hero7 add Alice":
            jxhero7 = "Alice"
            await message.channel.send("Jackson's hero #7 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero7 add Aurora":
            jxhero7 = "Aurora"
            await message.channel.send("Jackson's hero #7 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jxhero7 = "Chang'e"
            await message.channel.send("Jackson's hero #7 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero7 add Cyclops":
            jxhero7 = "Cyclops"
            await message.channel.send("Jackson's hero #7 is now Cyclops! :eye:  ")
        if message.content == "!ml hero7 add Eudora":
            jxhero7 = "Eudora"
            await message.channel.send("Jackson's hero #7 is now Eudora! :zap: ")
        if message.content == "!ml hero7 add Faramis":
            jxhero7 = "Faramis"
            await message.channel.send("Jackson's hero #7 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero7 add Gord":
            jxhero7 = "Gord"
            await message.channel.send("Jackson's hero #7 is now Gord! :snowboarder:")
        if message.content == "!ml hero7 add Harith":
            jxhero7 = "Harith"
            await message.channel.send("Jackson's hero #7 is now Harith! :older_man: ")
        if message.content == "!ml hero7 add Harley":
            jxhero7 = "Harley"
            await message.channel.send("Jackson's hero #7 is now Harley! :tophat: ")
        if message.content == "!ml hero7 add Kadita":
            jxhero7 = "Kadita"
            await message.channel.send("Jackson's hero #7 is now Kadita! :droplet: ")
        if message.content == "!ml hero7 add Kagura":
            jxhero7 = "Kagura"
            await message.channel.send("Jackson's hero #7 is now Kagura! :umbrella7:  ")
        if message.content == "!ml hero7 add Lunox":
            jxhero7 = "Lunox"
            await message.channel.send("Jackson's hero #7 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero7 add Lylia":
            jxhero7 = "Lylia"
            await message.channel.send("Jackson's hero #7 is now Lylia! :boom: ")
        if message.content == "!ml hero7 add Nana":
            jxhero7 = "Nana"
            await message.channel.send("Jackson's hero #7 is now Nana! :cat:  ")
        if message.content == "!ml hero7 add Odette":
            jxhero7 = "Odette"
            await message.channel.send("Jackson's hero #7 is now Odette! :duck: ")
        if message.content == "!ml hero7 add Pharsa":
            jxhero7 = "Pharsa"
            await message.channel.send("Jackson's hero #7 is now Pharsa! :dove:  ")
        if message.content == "!ml hero7 add Vale":
            jxhero7 = "Vale"
            await message.channel.send("Jackson's hero #7 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero7 add Valir":
            jxhero7 = "Valir"
            await message.channel.send("Jackson's hero #7 is now Valir! :fire:")
        if message.content == "!ml hero7 add Vexanna":
            jxhero7 = "Vexanna"
            await message.channel.send("Jackson's hero #7 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero7 add Bruno":
            jxhero7 = "Bruno"
            await message.channel.send("Jackson's hero #7 is now Bruno! :soccer:  ")
        if message.content == "!ml hero7 add Claude":
            jxhero7 = "Claude"
            await message.channel.send("Jackson's hero #7 is now Claude! :monkey:  ")
        if message.content == "!ml hero7 add Clint":
            jxhero7 = "Clint"
            await message.channel.send("Jackson's hero #7 is now Clint! :cowboy: ")
        if message.content == "!ml hero7 add Granger":
            jxhero7 = "Granger"
            await message.channel.send("Jackson's hero #7 is now Granger! :violin: ")
        if message.content == "!ml hero7 add Hanabi":
            jxhero7 = "Hanabi"
            await message.channel.send("Jackson's hero #7 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero7 add Irithel":
            jxhero7 = "Irithel"
            await message.channel.send("Jackson's hero #7 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero7 add Karrie":
            jxhero7 = "Karrie"
            await message.channel.send(
                "Jackson's hero #7 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero7 add Kimmy":
            jxhero7 = "Kimmy"
            await message.channel.send("Jackson's hero #7 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero7 add Layla":
            jxhero7 = "Layla"
            await message.channel.send("Jackson's hero #7 is now Layla! :haircut:  ")
        if message.content == "!ml hero7 add Miya":
            jxhero7 = "Miya"
            await message.channel.send("Jackson's hero #7 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero7 add Moskov":
            jxhero7 = "Moskov"
            await message.channel.send("Jackson's hero #7 is now Moskov! :imp: ")
        if message.content == "!ml hero7 add Yi Sun-Shin":
            jxhero7 = "Yi Sun-Shin"
            await message.channel.send("Jackson's hero #7 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero7 add Angela":
            jxhero7 = "Angela"
            await message.channel.send("Jackson's hero #7 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero7 add Diggie":
            jxhero7 = "Diggie"
            await message.channel.send("Jackson's hero #7 is now Diggie! :owl: ")
        if message.content == "!ml hero7 add Estes":
            jxhero7 = "Estes"
            await message.channel.send("Jackson's hero #7 is now Estes! :ear:  ")
        if message.content == "!ml hero7 add Rafaela":
            jxhero7 = "Rafaela"
            await message.channel.send("Jackson's hero #7 is now Rafaela! :angel: ")
        if message.content == "!ml hero7 add Rynn":
            jxhero7 = "Rynn"
            await message.channel.send("Jackson's hero #7 is now Rynn! ")
        if message.content == "!ml hero8 add Akai":
            global jxhero8
            jxhero8 = "Akai"
            await message.channel.send("Jackson's hero #8 is now Akai! :panda_face: ")
        if message.content == "!ml hero8 add Balmond":
            jxhero8 = "Balmond"
            await message.channel.send("Jackson's hero #8 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero8 add Belerick":
            jxhero8 = "Belerick"
            await message.channel.send("Jackson's hero #8 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero8 add Franco":
            jxhero8 = "Franco"
            await message.channel.send("Jackson's hero #8 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero8 add Esmerelda":
            jxhero8 = "Esmerelda"
            await message.channel.send("Jackson's hero #8 is now Esmerelda! :shield: ")
        if message.content == "!ml hero8 add Gatotkaca":
            jxhero8 = "Gatotkaca"
            await message.channel.send("Jackson's hero #8 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero8 add Grock":
            jxhero8 = "Grock"
            await message.channel.send("Jackson's hero #8 is now Grock! :european_castle: ")
        if message.content == "!ml hero8 add Hilda":
            jxhero8 = "Hilda"
            await message.channel.send("Jackson's hero #8 is now Hilda! :runner: ")
        if message.content == "!ml hero8 add Hylos":
            jxhero8 = "Hylos"
            await message.channel.send("Jackson's hero #8 is now Hylos! :unicorn: ")
        if message.content == "!ml hero8 add Johnson":
            jxhero8 = "Johnson"
            await message.channel.send("Jackson's hero #8 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero8 add Khufra":
            jxhero8 = "Khufra"
            await message.channel.send("Jackson's hero #8 is now Khufra! :clown: ")
        if message.content == "!ml hero8 add Lolita":
            jxhero8 = "Lolita"
            await message.channel.send("Jackson's hero #8 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jxhero8 = "Masha"
            await message.channel.send("Jackson's hero #8 is now Masha! :bear: ")
        if message.content == "!ml hero8 add Minotaur":
            jxhero8 = "Minotaur"
            await message.channel.send("Jackson's hero #8 is now Minotaur! :cow: ")
        if message.content == "!ml hero8 add Tigreal":
            jxhero8 = "Tigreal"
            await message.channel.send("Jackson's hero #8 is now Tigreal! :moyai: ")
        if message.content == "!ml hero8 add Uranus":
            jxhero8 = "Uranus"
            await message.channel.send("Jackson's hero #8 is now Uranus! :peach: ")
        if message.content == "!ml hero8 add X.Borg":
            jxhero8 = "X.Borg"
            await message.channel.send("Jackson's hero #8 is now X.Borg! :fire: ")
        if message.content == "!ml hero8 add Aldous":
            jxhero8 = "Aldous"
            await message.channel.send("Jackson's hero #8 is now Aldous! :fist: ")
        if message.content == "!ml hero8 add Alpha":
            jxhero8 = "Alpha"
            await message.channel.send("Jackson's hero #8 is now Alpha! :airplane: ")
        if message.content == "!ml hero8 add Alucard":
            jxhero8 = "Alucard"
            await message.channel.send("Jackson's hero #8 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero8 add Argus":
            jxhero8 = "Argus"
            await message.channel.send("Jackson's hero #8 is now Argus! :angel: ")
        if message.content == "!ml hero8 add Badang":
            jxhero8 = "Badang"
            await message.channel.send("Jackson's hero #8 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero8 add Bane":
            jxhero8 = "Bane"
            await message.channel.send("Jackson's hero #8 is now Bane! :octopus: ")
        if message.content == "!ml hero8 add Chou":
            jxhero8 = "Chou"
            await message.channel.send("Jackson's hero #8 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero8 add Dyrroth":
            jxhero8 = "Dyrroth"
            await message.channel.send("Jackson's hero #8 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero8 add Freya":
            jxhero8 = "Freya"
            await message.channel.send("Jackson's hero #8 is now Freya! :hammer: ")
        if message.content == "!ml hero8 add Guinevere":
            jxhero8 = "Guinevere"
            await message.channel.send("Jackson's hero #8 is now Guinevere! :dress:  ")
        if message.content == "!ml hero8 add Jawhead":
            jxhero8 = "Jawhead"
            await message.channel.send("Jackson's hero #8 is now Jawhead! :robot: ")
        if message.content == "!ml hero8 add Kaja":
            jxhero8 = "Kaja"
            await message.channel.send("Jackson's hero #8 is now Kaja! :bird: ")
        if message.content == "!ml hero8 add Lapu-Lapu":
            jxhero8 = "Lapu-Lapu"
            await message.channel.send("Jackson's hero #8 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero8 add Leomord":
            jxhero8 = "Leomord"
            await message.channel.send("Jackson's hero #8 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero8 add Martis":
            jxhero8 = "Martis"
            await message.channel.send("Jackson's hero #8 is now Martis! :crab: ")
        if message.content == "!ml hero8 add Minsitthar":
            jxhero8 = "Minsitthar"
            await message.channel.send("Jackson's hero #8 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero8 add Roger":
            jxhero8 = "Roger"
            await message.channel.send("Jackson's hero #8 is now Roger! :wolf: ")
        if message.content == "!ml hero8 add Ruby":
            jxhero8 = "Ruby"
            await message.channel.send("Jackson's hero #8 is now Ruby! :heart: ")
        if message.content == "!ml hero8 add Sun":
            jxhero8 = "Sun"
            await message.channel.send("Jackson's hero #8 is now Sun! :monkey_face: ")
        if message.content == "!ml hero8 add Thamuz":
            jxhero8 = "Thamuz"
            await message.channel.send("Jackson's hero #8 is now Thamuz! :rage: ")
        if message.content == "!ml hero8 add Terizla":
            jxhero8 = "Terizla"
            await message.channel.send("Jackson's hero #8 is now Terizla! :hammer: ")
        if message.content == "!ml hero8 add Zilong":
            jxhero8 = "Zilong"
            await message.channel.send("Jackson's hero #8 is now Zilong! :dragon: ")
        if message.content == "!ml hero8 add Fanny":
            jxhero8 = "Fanny"
            await message.channel.send("Jackson's hero #8 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero8 add Gusion":
            jxhero8 = "Gusion"
            await message.channel.send(
                "Jackson's hero #8 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero8 add Hanzo":
            jxhero8 = "Hanzo"
            await message.channel.send("Jackson's hero #8 is now Hanzo! :ghost: ")
        if message.content == "!ml hero8 add Hayabusa":
            jxhero8 = "Hayabusa"
            await message.channel.send("Jackson's hero #8 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero8 add Helcurt":
            jxhero8 = "Helcurt"
            await message.channel.send("Jackson's hero #8 is now Helcurt! :mute:  ")
        if message.content == "!ml hero8 add Karina":
            jxhero8 = "Karina"
            await message.channel.send("Jackson's hero #8 is now Karina! :purple_heart: ")
        if message.content == "!ml hero8 add Lancelot":
            jxhero8 = "Lancelot"
            await message.channel.send("Jackson's hero #8 is now Lancelot! :fencer: ")
        if message.content == "!ml hero8 add Lesley":
            jxhero8 = "Lesley"
            await message.channel.send("Jackson's hero #8 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero8 add Natalia":
            jxhero8 = "Natalia"
            await message.channel.send("Jackson's hero #8 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero8 add Saber":
            jxhero8 = "Saber"
            await message.channel.send("Jackson's hero #8 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero8 add Selena":
            jxhero8 = "Selena"
            await message.channel.send("Jackson's hero #8 is now Selena! :sleeping:  ")
        if message.content == "!ml hero8 add Alice":
            jxhero8 = "Alice"
            await message.channel.send("Jackson's hero #8 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero8 add Aurora":
            jxhero8 = "Aurora"
            await message.channel.send("Jackson's hero #8 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jxhero8 = "Chang'e"
            await message.channel.send("Jackson's hero #8 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero8 add Cyclops":
            jxhero8 = "Cyclops"
            await message.channel.send("Jackson's hero #8 is now Cyclops! :eye:  ")
        if message.content == "!ml hero8 add Eudora":
            jxhero8 = "Eudora"
            await message.channel.send("Jackson's hero #8 is now Eudora! :zap: ")
        if message.content == "!ml hero8 add Faramis":
            jxhero8 = "Faramis"
            await message.channel.send("Jackson's hero #8 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero8 add Gord":
            jxhero8 = "Gord"
            await message.channel.send("Jackson's hero #8 is now Gord! :snowboarder:")
        if message.content == "!ml hero8 add Harith":
            jxhero8 = "Harith"
            await message.channel.send("Jackson's hero #8 is now Harith! :older_man: ")
        if message.content == "!ml hero8 add Harley":
            jxhero8 = "Harley"
            await message.channel.send("Jackson's hero #8 is now Harley! :tophat: ")
        if message.content == "!ml hero8 add Kadita":
            jxhero8 = "Kadita"
            await message.channel.send("Jackson's hero #8 is now Kadita! :droplet: ")
        if message.content == "!ml hero8 add Kagura":
            jxhero8 = "Kagura"
            await message.channel.send("Jackson's hero #8 is now Kagura! :umbrella8:  ")
        if message.content == "!ml hero8 add Lunox":
            jxhero8 = "Lunox"
            await message.channel.send("Jackson's hero #8 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero8 add Lylia":
            jxhero8 = "Lylia"
            await message.channel.send("Jackson's hero #8 is now Lylia! :boom: ")
        if message.content == "!ml hero8 add Nana":
            jxhero8 = "Nana"
            await message.channel.send("Jackson's hero #8 is now Nana! :cat:  ")
        if message.content == "!ml hero8 add Odette":
            jxhero8 = "Odette"
            await message.channel.send("Jackson's hero #8 is now Odette! :duck: ")
        if message.content == "!ml hero8 add Pharsa":
            jxhero8 = "Pharsa"
            await message.channel.send("Jackson's hero #8 is now Pharsa! :dove:  ")
        if message.content == "!ml hero8 add Vale":
            jxhero8 = "Vale"
            await message.channel.send("Jackson's hero #8 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero8 add Valir":
            jxhero8 = "Valir"
            await message.channel.send("Jackson's hero #8 is now Valir! :fire:")
        if message.content == "!ml hero8 add Vexanna":
            jxhero8 = "Vexanna"
            await message.channel.send("Jackson's hero #8 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero8 add Bruno":
            jxhero8 = "Bruno"
            await message.channel.send("Jackson's hero #8 is now Bruno! :soccer:  ")
        if message.content == "!ml hero8 add Claude":
            jxhero8 = "Claude"
            await message.channel.send("Jackson's hero #8 is now Claude! :monkey:  ")
        if message.content == "!ml hero8 add Clint":
            jxhero8 = "Clint"
            await message.channel.send("Jackson's hero #8 is now Clint! :cowboy: ")
        if message.content == "!ml hero8 add Granger":
            jxhero8 = "Granger"
            await message.channel.send("Jackson's hero #8 is now Granger! :violin: ")
        if message.content == "!ml hero8 add Hanabi":
            jxhero8 = "Hanabi"
            await message.channel.send("Jackson's hero #8 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero8 add Irithel":
            jxhero8 = "Irithel"
            await message.channel.send("Jackson's hero #8 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero8 add Karrie":
            jxhero8 = "Karrie"
            await message.channel.send(
                "Jackson's hero #8 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero8 add Kimmy":
            jxhero8 = "Kimmy"
            await message.channel.send("Jackson's hero #8 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero8 add Layla":
            jxhero8 = "Layla"
            await message.channel.send("Jackson's hero #8 is now Layla! :haircut:  ")
        if message.content == "!ml hero8 add Miya":
            jxhero8 = "Miya"
            await message.channel.send("Jackson's hero #8 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero8 add Moskov":
            jxhero8 = "Moskov"
            await message.channel.send("Jackson's hero #8 is now Moskov! :imp: ")
        if message.content == "!ml hero8 add Yi Sun-Shin":
            jxhero8 = "Yi Sun-Shin"
            await message.channel.send("Jackson's hero #8 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero8 add Angela":
            jxhero8 = "Angela"
            await message.channel.send("Jackson's hero #8 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero8 add Diggie":
            jxhero8 = "Diggie"
            await message.channel.send("Jackson's hero #8 is now Diggie! :owl: ")
        if message.content == "!ml hero8 add Estes":
            jxhero8 = "Estes"
            await message.channel.send("Jackson's hero #8 is now Estes! :ear:  ")
        if message.content == "!ml hero8 add Rafaela":
            jxhero8 = "Rafaela"
            await message.channel.send("Jackson's hero #8 is now Rafaela! :angel: ")
        if message.content == "!ml hero8 add Rynn":
            jxhero8 = "Rynn"
            await message.channel.send("Jackson's hero #8 is now Rynn! ")
        if message.content == "!ml hero9 add Akai":
            global jxhero9
            jxhero9 = "Akai"
            await message.channel.send("Jackson's hero #9 is now Akai! :panda_face: ")
        if message.content == "!ml hero9 add Balmond":
            jxhero9 = "Balmond"
            await message.channel.send("Jackson's hero #9 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero9 add Belerick":
            jxhero9 = "Belerick"
            await message.channel.send("Jackson's hero #9 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero9 add Franco":
            jxhero9 = "Franco"
            await message.channel.send("Jackson's hero #9 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero9 add Esmerelda":
            jxhero9 = "Esmerelda"
            await message.channel.send("Jackson's hero #9 is now Esmerelda! :shield: ")
        if message.content == "!ml hero9 add Gatotkaca":
            jxhero9 = "Gatotkaca"
            await message.channel.send("Jackson's hero #9 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero9 add Grock":
            jxhero9 = "Grock"
            await message.channel.send("Jackson's hero #9 is now Grock! :european_castle: ")
        if message.content == "!ml hero9 add Hilda":
            jxhero9 = "Hilda"
            await message.channel.send("Jackson's hero #9 is now Hilda! :runner: ")
        if message.content == "!ml hero9 add Hylos":
            jxhero9 = "Hylos"
            await message.channel.send("Jackson's hero #9 is now Hylos! :unicorn: ")
        if message.content == "!ml hero9 add Johnson":
            jxhero9 = "Johnson"
            await message.channel.send("Jackson's hero #9 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero9 add Khufra":
            jxhero9 = "Khufra"
            await message.channel.send("Jackson's hero #9 is now Khufra! :clown: ")
        if message.content == "!ml hero9 add Lolita":
            jxhero9 = "Lolita"
            await message.channel.send("Jackson's hero #9 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jxhero9 = "Masha"
            await message.channel.send("Jackson's hero #9 is now Masha! :bear: ")
        if message.content == "!ml hero9 add Minotaur":
            jxhero9 = "Minotaur"
            await message.channel.send("Jackson's hero #9 is now Minotaur! :cow: ")
        if message.content == "!ml hero9 add Tigreal":
            jxhero9 = "Tigreal"
            await message.channel.send("Jackson's hero #9 is now Tigreal! :moyai: ")
        if message.content == "!ml hero9 add Uranus":
            jxhero9 = "Uranus"
            await message.channel.send("Jackson's hero #9 is now Uranus! :peach: ")
        if message.content == "!ml hero9 add X.Borg":
            jxhero9 = "X.Borg"
            await message.channel.send("Jackson's hero #9 is now X.Borg! :fire: ")
        if message.content == "!ml hero9 add Aldous":
            jxhero9 = "Aldous"
            await message.channel.send("Jackson's hero #9 is now Aldous! :fist: ")
        if message.content == "!ml hero9 add Alpha":
            jxhero9 = "Alpha"
            await message.channel.send("Jackson's hero #9 is now Alpha! :airplane: ")
        if message.content == "!ml hero9 add Alucard":
            jxhero9 = "Alucard"
            await message.channel.send("Jackson's hero #9 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero9 add Argus":
            jxhero9 = "Argus"
            await message.channel.send("Jackson's hero #9 is now Argus! :angel: ")
        if message.content == "!ml hero9 add Badang":
            jxhero9 = "Badang"
            await message.channel.send("Jackson's hero #9 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero9 add Bane":
            jxhero9 = "Bane"
            await message.channel.send("Jackson's hero #9 is now Bane! :octopus: ")
        if message.content == "!ml hero9 add Chou":
            jxhero9 = "Chou"
            await message.channel.send("Jackson's hero #9 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero9 add Dyrroth":
            jxhero9 = "Dyrroth"
            await message.channel.send("Jackson's hero #9 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero9 add Freya":
            jxhero9 = "Freya"
            await message.channel.send("Jackson's hero #9 is now Freya! :hammer: ")
        if message.content == "!ml hero9 add Guinevere":
            jxhero9 = "Guinevere"
            await message.channel.send("Jackson's hero #9 is now Guinevere! :dress:  ")
        if message.content == "!ml hero9 add Jawhead":
            jxhero9 = "Jawhead"
            await message.channel.send("Jackson's hero #9 is now Jawhead! :robot: ")
        if message.content == "!ml hero9 add Kaja":
            jxhero9 = "Kaja"
            await message.channel.send("Jackson's hero #9 is now Kaja! :bird: ")
        if message.content == "!ml hero9 add Lapu-Lapu":
            jxhero9 = "Lapu-Lapu"
            await message.channel.send("Jackson's hero #9 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero9 add Leomord":
            jxhero9 = "Leomord"
            await message.channel.send("Jackson's hero #9 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero9 add Martis":
            jxhero9 = "Martis"
            await message.channel.send("Jackson's hero #9 is now Martis! :crab: ")
        if message.content == "!ml hero9 add Minsitthar":
            jxhero9 = "Minsitthar"
            await message.channel.send("Jackson's hero #9 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero9 add Roger":
            jxhero9 = "Roger"
            await message.channel.send("Jackson's hero #9 is now Roger! :wolf: ")
        if message.content == "!ml hero9 add Ruby":
            jxhero9 = "Ruby"
            await message.channel.send("Jackson's hero #9 is now Ruby! :heart: ")
        if message.content == "!ml hero9 add Sun":
            jxhero9 = "Sun"
            await message.channel.send("Jackson's hero #9 is now Sun! :monkey_face: ")
        if message.content == "!ml hero9 add Thamuz":
            jxhero9 = "Thamuz"
            await message.channel.send("Jackson's hero #9 is now Thamuz! :rage: ")
        if message.content == "!ml hero9 add Terizla":
            jxhero9 = "Terizla"
            await message.channel.send("Jackson's hero #9 is now Terizla! :hammer: ")
        if message.content == "!ml hero9 add Zilong":
            jxhero9 = "Zilong"
            await message.channel.send("Jackson's hero #9 is now Zilong! :dragon: ")
        if message.content == "!ml hero9 add Fanny":
            jxhero9 = "Fanny"
            await message.channel.send("Jackson's hero #9 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero9 add Gusion":
            jxhero9 = "Gusion"
            await message.channel.send(
                "Jackson's hero #9 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero9 add Hanzo":
            jxhero9 = "Hanzo"
            await message.channel.send("Jackson's hero #9 is now Hanzo! :ghost: ")
        if message.content == "!ml hero9 add Hayabusa":
            jxhero9 = "Hayabusa"
            await message.channel.send("Jackson's hero #9 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero9 add Helcurt":
            jxhero9 = "Helcurt"
            await message.channel.send("Jackson's hero #9 is now Helcurt! :mute:  ")
        if message.content == "!ml hero9 add Karina":
            jxhero9 = "Karina"
            await message.channel.send("Jackson's hero #9 is now Karina! :purple_heart: ")
        if message.content == "!ml hero9 add Lancelot":
            jxhero9 = "Lancelot"
            await message.channel.send("Jackson's hero #9 is now Lancelot! :fencer: ")
        if message.content == "!ml hero9 add Lesley":
            jxhero9 = "Lesley"
            await message.channel.send("Jackson's hero #9 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero9 add Natalia":
            jxhero9 = "Natalia"
            await message.channel.send("Jackson's hero #9 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero9 add Saber":
            jxhero9 = "Saber"
            await message.channel.send("Jackson's hero #9 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero9 add Selena":
            jxhero9 = "Selena"
            await message.channel.send("Jackson's hero #9 is now Selena! :sleeping:  ")
        if message.content == "!ml hero9 add Alice":
            jxhero9 = "Alice"
            await message.channel.send("Jackson's hero #9 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero9 add Aurora":
            jxhero9 = "Aurora"
            await message.channel.send("Jackson's hero #9 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jxhero9 = "Chang'e"
            await message.channel.send("Jackson's hero #9 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero9 add Cyclops":
            jxhero9 = "Cyclops"
            await message.channel.send("Jackson's hero #9 is now Cyclops! :eye:  ")
        if message.content == "!ml hero9 add Eudora":
            jxhero9 = "Eudora"
            await message.channel.send("Jackson's hero #9 is now Eudora! :zap: ")
        if message.content == "!ml hero9 add Faramis":
            jxhero9 = "Faramis"
            await message.channel.send("Jackson's hero #9 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero9 add Gord":
            jxhero9 = "Gord"
            await message.channel.send("Jackson's hero #9 is now Gord! :snowboarder:")
        if message.content == "!ml hero9 add Harith":
            jxhero9 = "Harith"
            await message.channel.send("Jackson's hero #9 is now Harith! :older_man: ")
        if message.content == "!ml hero9 add Harley":
            jxhero9 = "Harley"
            await message.channel.send("Jackson's hero #9 is now Harley! :tophat: ")
        if message.content == "!ml hero9 add Kadita":
            jxhero9 = "Kadita"
            await message.channel.send("Jackson's hero #9 is now Kadita! :droplet: ")
        if message.content == "!ml hero9 add Kagura":
            jxhero9 = "Kagura"
            await message.channel.send("Jackson's hero #9 is now Kagura! :umbrella9:  ")
        if message.content == "!ml hero9 add Lunox":
            jxhero9 = "Lunox"
            await message.channel.send("Jackson's hero #9 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero9 add Lylia":
            jxhero9 = "Lylia"
            await message.channel.send("Jackson's hero #9 is now Lylia! :boom: ")
        if message.content == "!ml hero9 add Nana":
            jxhero9 = "Nana"
            await message.channel.send("Jackson's hero #9 is now Nana! :cat:  ")
        if message.content == "!ml hero9 add Odette":
            jxhero9 = "Odette"
            await message.channel.send("Jackson's hero #9 is now Odette! :duck: ")
        if message.content == "!ml hero9 add Pharsa":
            jxhero9 = "Pharsa"
            await message.channel.send("Jackson's hero #9 is now Pharsa! :dove:  ")
        if message.content == "!ml hero9 add Vale":
            jxhero9 = "Vale"
            await message.channel.send("Jackson's hero #9 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero9 add Valir":
            jxhero9 = "Valir"
            await message.channel.send("Jackson's hero #9 is now Valir! :fire:")
        if message.content == "!ml hero9 add Vexanna":
            jxhero9 = "Vexanna"
            await message.channel.send("Jackson's hero #9 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero9 add Bruno":
            jxhero9 = "Bruno"
            await message.channel.send("Jackson's hero #9 is now Bruno! :soccer:  ")
        if message.content == "!ml hero9 add Claude":
            jxhero9 = "Claude"
            await message.channel.send("Jackson's hero #9 is now Claude! :monkey:  ")
        if message.content == "!ml hero9 add Clint":
            jxhero9 = "Clint"
            await message.channel.send("Jackson's hero #9 is now Clint! :cowboy: ")
        if message.content == "!ml hero9 add Granger":
            jxhero9 = "Granger"
            await message.channel.send("Jackson's hero #9 is now Granger! :violin: ")
        if message.content == "!ml hero9 add Hanabi":
            jxhero9 = "Hanabi"
            await message.channel.send("Jackson's hero #9 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero9 add Irithel":
            jxhero9 = "Irithel"
            await message.channel.send("Jackson's hero #9 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero9 add Karrie":
            jxhero9 = "Karrie"
            await message.channel.send(
                "Jackson's hero #9 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero9 add Kimmy":
            jxhero9 = "Kimmy"
            await message.channel.send("Jackson's hero #9 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero9 add Layla":
            jxhero9 = "Layla"
            await message.channel.send("Jackson's hero #9 is now Layla! :haircut:  ")
        if message.content == "!ml hero9 add Miya":
            jxhero9 = "Miya"
            await message.channel.send("Jackson's hero #9 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero9 add Moskov":
            jxhero9 = "Moskov"
            await message.channel.send("Jackson's hero #9 is now Moskov! :imp: ")
        if message.content == "!ml hero9 add Yi Sun-Shin":
            jxhero9 = "Yi Sun-Shin"
            await message.channel.send("Jackson's hero #9 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero9 add Angela":
            jxhero9 = "Angela"
            await message.channel.send("Jackson's hero #9 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero9 add Diggie":
            jxhero9 = "Diggie"
            await message.channel.send("Jackson's hero #9 is now Diggie! :owl: ")
        if message.content == "!ml hero9 add Estes":
            jxhero9 = "Estes"
            await message.channel.send("Jackson's hero #9 is now Estes! :ear:  ")
        if message.content == "!ml hero9 add Rafaela":
            jxhero9 = "Rafaela"
            await message.channel.send("Jackson's hero #9 is now Rafaela! :angel: ")
        if message.content == "!ml hero9 add Rynn":
            jxhero9 = "Rynn"
            await message.channel.send("Jackson's hero #9 is now Rynn! ")
        if message.content == "!ml hero10 add Akai":
            global jxhero10
            jxhero10 = "Akai"
            await message.channel.send("Jackson's hero #10 is now Akai! :panda_face: ")
        if message.content == "!ml hero10 add Balmond":
            jxhero10 = "Balmond"
            await message.channel.send("Jackson's hero #10 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero10 add Belerick":
            jxhero10 = "Belerick"
            await message.channel.send("Jackson's hero #10 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero10 add Franco":
            jxhero10 = "Franco"
            await message.channel.send("Jackson's hero #10 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero10 add Esmerelda":
            jxhero10 = "Esmerelda"
            await message.channel.send("Jackson's hero #10 is now Esmerelda! :shield: ")
        if message.content == "!ml hero10 add Gatotkaca":
            jxhero10 = "Gatotkaca"
            await message.channel.send("Jackson's hero #10 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero10 add Grock":
            jxhero10 = "Grock"
            await message.channel.send("Jackson's hero #10 is now Grock! :european_castle: ")
        if message.content == "!ml hero10 add Hilda":
            jxhero10 = "Hilda"
            await message.channel.send("Jackson's hero #10 is now Hilda! :runner: ")
        if message.content == "!ml hero10 add Hylos":
            jxhero10 = "Hylos"
            await message.channel.send("Jackson's hero #10 is now Hylos! :unicorn: ")
        if message.content == "!ml hero10 add Johnson":
            jxhero10 = "Johnson"
            await message.channel.send("Jackson's hero #10 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero10 add Khufra":
            jxhero10 = "Khufra"
            await message.channel.send("Jackson's hero #10 is now Khufra! :clown: ")
        if message.content == "!ml hero10 add Lolita":
            jxhero10 = "Lolita"
            await message.channel.send("Jackson's hero #10 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jxhero10 = "Masha"
            await message.channel.send("Jackson's hero #10 is now Masha! :bear: ")
        if message.content == "!ml hero10 add Minotaur":
            jxhero10 = "Minotaur"
            await message.channel.send("Jackson's hero #10 is now Minotaur! :cow: ")
        if message.content == "!ml hero10 add Tigreal":
            jxhero10 = "Tigreal"
            await message.channel.send("Jackson's hero #10 is now Tigreal! :moyai: ")
        if message.content == "!ml hero10 add Uranus":
            jxhero10 = "Uranus"
            await message.channel.send("Jackson's hero #10 is now Uranus! :peach: ")
        if message.content == "!ml hero10 add X.Borg":
            jxhero10 = "X.Borg"
            await message.channel.send("Jackson's hero #10 is now X.Borg! :fire: ")
        if message.content == "!ml hero10 add Aldous":
            jxhero10 = "Aldous"
            await message.channel.send("Jackson's hero #10 is now Aldous! :fist: ")
        if message.content == "!ml hero10 add Alpha":
            jxhero10 = "Alpha"
            await message.channel.send("Jackson's hero #10 is now Alpha! :airplane: ")
        if message.content == "!ml hero10 add Alucard":
            jxhero10 = "Alucard"
            await message.channel.send("Jackson's hero #10 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero10 add Argus":
            jxhero10 = "Argus"
            await message.channel.send("Jackson's hero #10 is now Argus! :angel: ")
        if message.content == "!ml hero10 add Badang":
            jxhero10 = "Badang"
            await message.channel.send("Jackson's hero #10 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero10 add Bane":
            jxhero10 = "Bane"
            await message.channel.send("Jackson's hero #10 is now Bane! :octopus: ")
        if message.content == "!ml hero10 add Chou":
            jxhero10 = "Chou"
            await message.channel.send("Jackson's hero #10 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero10 add Dyrroth":
            jxhero10 = "Dyrroth"
            await message.channel.send("Jackson's hero #10 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero10 add Freya":
            jxhero10 = "Freya"
            await message.channel.send("Jackson's hero #10 is now Freya! :hammer: ")
        if message.content == "!ml hero10 add Guinevere":
            jxhero10 = "Guinevere"
            await message.channel.send("Jackson's hero #10 is now Guinevere! :dress:  ")
        if message.content == "!ml hero10 add Jawhead":
            jxhero10 = "Jawhead"
            await message.channel.send("Jackson's hero #10 is now Jawhead! :robot: ")
        if message.content == "!ml hero10 add Kaja":
            jxhero10 = "Kaja"
            await message.channel.send("Jackson's hero #10 is now Kaja! :bird: ")
        if message.content == "!ml hero10 add Lapu-Lapu":
            jxhero10 = "Lapu-Lapu"
            await message.channel.send("Jackson's hero #10 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero10 add Leomord":
            jxhero10 = "Leomord"
            await message.channel.send("Jackson's hero #10 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero10 add Martis":
            jxhero10 = "Martis"
            await message.channel.send("Jackson's hero #10 is now Martis! :crab: ")
        if message.content == "!ml hero10 add Minsitthar":
            jxhero10 = "Minsitthar"
            await message.channel.send("Jackson's hero #10 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero10 add Roger":
            jxhero10 = "Roger"
            await message.channel.send("Jackson's hero #10 is now Roger! :wolf: ")
        if message.content == "!ml hero10 add Ruby":
            jxhero10 = "Ruby"
            await message.channel.send("Jackson's hero #10 is now Ruby! :heart: ")
        if message.content == "!ml hero10 add Sun":
            jxhero10 = "Sun"
            await message.channel.send("Jackson's hero #10 is now Sun! :monkey_face: ")
        if message.content == "!ml hero10 add Thamuz":
            jxhero10 = "Thamuz"
            await message.channel.send("Jackson's hero #10 is now Thamuz! :rage: ")
        if message.content == "!ml hero10 add Terizla":
            jxhero10 = "Terizla"
            await message.channel.send("Jackson's hero #10 is now Terizla! :hammer: ")
        if message.content == "!ml hero10 add Zilong":
            jxhero10 = "Zilong"
            await message.channel.send("Jackson's hero #10 is now Zilong! :dragon: ")
        if message.content == "!ml hero10 add Fanny":
            jxhero10 = "Fanny"
            await message.channel.send("Jackson's hero #10 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero10 add Gusion":
            jxhero10 = "Gusion"
            await message.channel.send(
                "Jackson's hero #10 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero10 add Hanzo":
            jxhero10 = "Hanzo"
            await message.channel.send("Jackson's hero #10 is now Hanzo! :ghost: ")
        if message.content == "!ml hero10 add Hayabusa":
            jxhero10 = "Hayabusa"
            await message.channel.send("Jackson's hero #10 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero10 add Helcurt":
            jxhero10 = "Helcurt"
            await message.channel.send("Jackson's hero #10 is now Helcurt! :mute:  ")
        if message.content == "!ml hero10 add Karina":
            jxhero10 = "Karina"
            await message.channel.send("Jackson's hero #10 is now Karina! :purple_heart: ")
        if message.content == "!ml hero10 add Lancelot":
            jxhero10 = "Lancelot"
            await message.channel.send("Jackson's hero #10 is now Lancelot! :fencer: ")
        if message.content == "!ml hero10 add Lesley":
            jxhero10 = "Lesley"
            await message.channel.send("Jackson's hero #10 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero10 add Natalia":
            jxhero10 = "Natalia"
            await message.channel.send("Jackson's hero #10 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero10 add Saber":
            jxhero10 = "Saber"
            await message.channel.send("Jackson's hero #10 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero10 add Selena":
            jxhero10 = "Selena"
            await message.channel.send("Jackson's hero #10 is now Selena! :sleeping:  ")
        if message.content == "!ml hero10 add Alice":
            jxhero10 = "Alice"
            await message.channel.send("Jackson's hero #10 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero10 add Aurora":
            jxhero10 = "Aurora"
            await message.channel.send("Jackson's hero #10 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jxhero10 = "Chang'e"
            await message.channel.send("Jackson's hero #10 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero10 add Cyclops":
            jxhero10 = "Cyclops"
            await message.channel.send("Jackson's hero #10 is now Cyclops! :eye:  ")
        if message.content == "!ml hero10 add Eudora":
            jxhero10 = "Eudora"
            await message.channel.send("Jackson's hero #10 is now Eudora! :zap: ")
        if message.content == "!ml hero10 add Faramis":
            jxhero10 = "Faramis"
            await message.channel.send("Jackson's hero #10 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero10 add Gord":
            jxhero10 = "Gord"
            await message.channel.send("Jackson's hero #10 is now Gord! :snowboarder:")
        if message.content == "!ml hero10 add Harith":
            jxhero10 = "Harith"
            await message.channel.send("Jackson's hero #10 is now Harith! :older_man: ")
        if message.content == "!ml hero10 add Harley":
            jxhero10 = "Harley"
            await message.channel.send("Jackson's hero #10 is now Harley! :tophat: ")
        if message.content == "!ml hero10 add Kadita":
            jxhero10 = "Kadita"
            await message.channel.send("Jackson's hero #10 is now Kadita! :droplet: ")
        if message.content == "!ml hero10 add Kagura":
            jxhero10 = "Kagura"
            await message.channel.send("Jackson's hero #10 is now Kagura! :umbrella10:  ")
        if message.content == "!ml hero10 add Lunox":
            jxhero10 = "Lunox"
            await message.channel.send("Jackson's hero #10 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero10 add Lylia":
            jxhero10 = "Lylia"
            await message.channel.send("Jackson's hero #10 is now Lylia! :boom: ")
        if message.content == "!ml hero10 add Nana":
            jxhero10 = "Nana"
            await message.channel.send("Jackson's hero #10 is now Nana! :cat:  ")
        if message.content == "!ml hero10 add Odette":
            jxhero10 = "Odette"
            await message.channel.send("Jackson's hero #10 is now Odette! :duck: ")
        if message.content == "!ml hero10 add Pharsa":
            jxhero10 = "Pharsa"
            await message.channel.send("Jackson's hero #10 is now Pharsa! :dove:  ")
        if message.content == "!ml hero10 add Vale":
            jxhero10 = "Vale"
            await message.channel.send("Jackson's hero #10 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero10 add Valir":
            jxhero10 = "Valir"
            await message.channel.send("Jackson's hero #10 is now Valir! :fire:")
        if message.content == "!ml hero10 add Vexanna":
            jxhero10 = "Vexanna"
            await message.channel.send("Jackson's hero #10 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero10 add Bruno":
            jxhero10 = "Bruno"
            await message.channel.send("Jackson's hero #10 is now Bruno! :soccer:  ")
        if message.content == "!ml hero10 add Claude":
            jxhero10 = "Claude"
            await message.channel.send("Jackson's hero #10 is now Claude! :monkey:  ")
        if message.content == "!ml hero10 add Clint":
            jxhero10 = "Clint"
            await message.channel.send("Jackson's hero #10 is now Clint! :cowboy: ")
        if message.content == "!ml hero10 add Granger":
            jxhero10 = "Granger"
            await message.channel.send("Jackson's hero #10 is now Granger! :violin: ")
        if message.content == "!ml hero10 add Hanabi":
            jxhero10 = "Hanabi"
            await message.channel.send("Jackson's hero #10 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero10 add Irithel":
            jxhero10 = "Irithel"
            await message.channel.send("Jackson's hero #10 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero10 add Karrie":
            jxhero10 = "Karrie"
            await message.channel.send(
                "Jackson's hero #10 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero10 add Kimmy":
            jxhero10 = "Kimmy"
            await message.channel.send("Jackson's hero #10 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero10 add Layla":
            jxhero10 = "Layla"
            await message.channel.send("Jackson's hero #10 is now Layla! :haircut:  ")
        if message.content == "!ml hero10 add Miya":
            jxhero10 = "Miya"
            await message.channel.send("Jackson's hero #10 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero10 add Moskov":
            jxhero10 = "Moskov"
            await message.channel.send("Jackson's hero #10 is now Moskov! :imp: ")
        if message.content == "!ml hero10 add Yi Sun-Shin":
            jxhero10 = "Yi Sun-Shin"
            await message.channel.send("Jackson's hero #10 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero10 add Angela":
            jxhero10 = "Angela"
            await message.channel.send("Jackson's hero #10 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero10 add Diggie":
            jxhero10 = "Diggie"
            await message.channel.send("Jackson's hero #10 is now Diggie! :owl: ")
        if message.content == "!ml hero10 add Estes":
            jxhero10 = "Estes"
            await message.channel.send("Jackson's hero #10 is now Estes! :ear:  ")
        if message.content == "!ml hero10 add Rafaela":
            jxhero10 = "Rafaela"
            await message.channel.send("Jackson's hero #10 is now Rafaela! :angel: ")
        if message.content == "!ml hero10 add Rynn":
            jxhero10 = "Rynn"
            await message.channel.send("Jackson's hero #10 is now Rynn! ")
        if message.content == "!ml hero1 clear":
            jxhero1 = "Not Chosen"
            await message.channel.send("Jackson's hero #1 slot has been cleared!")
        if message.content == "!ml hero2 clear":
            jxhero2 = "Not Chosen"
            await message.channel.send("Jackson's hero #2 slot has been cleared!")
        if message.content == "!ml hero3 clear":
            jxhero3 = "Not Chosen"
            await message.channel.send("Jackson's hero #3 slot has been cleared!")
        if message.content == "!ml hero3 clear":
            jxhero3 = "Not Chosen"
            await message.channel.send("Jackson's hero #3 slot has been cleared!")
        if message.content == "!ml hero4 clear":
            jxhero4 = "Not Chosen"
            await message.channel.send("Jackson's hero #4 slot has been cleared!")
        if message.content == "!ml hero5 clear":
            jxhero5 = "Not Chosen"
            await message.channel.send("Jackson's hero #5 slot has been cleared!")
        if message.content == "!ml hero6 clear":
            jxhero6 = "Not Chosen"
            await message.channel.send("Jackson's hero #6 slot has been cleared!")
        if message.content == "!ml hero7 clear":
            jxhero7 = "Not Chosen"
            await message.channel.send("Jackson's hero #7 slot has been cleared!")
        if message.content == "!ml hero8 clear":
            jxhero8 = "Not Chosen"
            await message.channel.send("Jackson's hero #8 slot has been cleared!")
        if message.content == "!ml hero9 clear":
            jxhero9 = "Not Chosen"
            await message.channel.send("Jackson's hero #9 slot has been cleared!")
        if message.content == "!ml hero10 clear":
            jxhero10 = "Not Chosen"
            await message.channel.send("Jackson's hero #10 slot has been cleared!")
        if message.content == "!ml hlist Jackson":
            jxembed = discord.Embed(title="Heroes Jackson Plays",
                                    description="Here are the top 10 heroes Jackson is willing to play in ranked")
            jxembed.add_field(name="1", value=jx1hero1)
            jxembed.add_field(name="2", value=jxhero2)
            jxembed.add_field(name="3", value=jxhero3)
            jxembed.add_field(name="4", value=jxhero4)
            jxembed.add_field(name="5", value=jx1hero5)
            jxembed.add_field(name="6", value=jxhero6)
            jxembed.add_field(name="7", value=jxhero7)
            jxembed.add_field(name="8", value=jxhero8)
            jxembed.add_field(name="9", value=jxhero9)
            jxembed.add_field(name="10", value=jxhero10)
            await message.channel.send(content=None, embed=jxembed)
    if str(message.channel) not in clean_channels and str(message.author) in Jack_Hlist:
        if message.content.find("hello") != -1:
            await message.channel.send("Hey Jack, how are you?")
        if message.content.find("!gay") != -1:
            await message.channel.send("Really? You too?")
        if message.content.find("!nigga") != -1:
            await message.channel.send("Are you trying to summon the great one?")
        if message.content.find("nigga") != -1:
            global nwbraydenchance
            global nwbraydenbonus
            global nwbraydentotal
            nwbraydenchance = random.randrange(0, 20, 1)
            nwbraydentotal = nwbraydenchance + nwbraydenbonus
            if nwbraydentotal > 15:
                await message.channel.send("Are you out of your mind? What if Brayden heard you?")
                nwbraydentotal = 0
                nwbraydenchance = 0
                nwbraydenbonus = 0
            else:
                nwbraydenbonus += 1
                nwbraydentotal = 0
                nwbraydenchance = 0
            nwordcount
            nwordcount += 1
        if message.content.find("Nigga") != -1:
            nwbraydenchance = random.randrange(0, 20, 1)
            nwbraydentotal = nwbraydenchance + nwbraydenbonus
            if nwbraydentotal > 15:
                await message.channel.send("You fool! Do you want Brayden to T-pose on you?")
                nwbraydentotal = 0
                nwbraydenchance = 0
                nwbraydenbonus = 0
            else:
                nwbraydenbonus += 1
                nwbraydentotal = 0
                nwbraydenchance = 0
            nwordcount
            nwordcount += 1
        if message.content.find("NIGGA") != -1:
            nwbraydenchance = random.randrange(0, 20, 1)
            nwbraydentotal = nwbraydenchance + nwbraydenbonus
            if nwbraydentotal > 15:
                await message.channel.send("May Jah have mercy on your soul")
                nwbraydentotal = 0
                nwbraydenchance = 0
                nwbraydenbonus = 0
            else:
                nwbraydenbonus += 1
                nwbraydentotal = 0
                nwbraydenchance = 0
            nwordcount
            nwordcount += 2
        if message.content.find("nigger") != -1:
            nwbraydenchance = random.randrange(0, 20, 1)
            nwbraydentotal = nwbraydenchance + nwbraydenbonus
            if nwbraydentotal > 15:
                await message.channel.send("Those words belong in the cotton fields, not this sever")
                nwbraydentotal = 0
                nwbraydenchance = 0
                nwbraydenbonus = 0
            else:
                nwbraydenbonus += 2
                nwbraydentotal = 0
                nwbraydenchance = 0
            nwordcount
            nwordcount += 2
        if message.content.find("Nigger") != -1:
            nwbraydenchance = random.randrange(0, 20, 1)
            nwbraydentotal = nwbraydenchance + nwbraydenbonus
            if nwbraydentotal > 15:
                await message.channel.send("**Whip cracking noises**")
                nwbraydentotal = 0
                nwbraydenchance = 0
                nwbraydenbonus = 0
            else:
                nwbraydenbonus += 2
                nwbraydentotal = 0
                nwbraydenchance = 0
            nwordcount
            nwordcount += 2
        if message.content.find("NIGGER") != -1:
            nwbraydenchance = random.randrange(0, 20, 1)
            nwbraydentotal = nwbraydenchance + nwbraydenbonus
            if nwbraydentotal > 15:
                await message.channel.send("***Brayden is coming.*** I suggest you run.")
                nwbraydentotal = 0
                nwbraydenchance = 0
                nwbraydenbonus = 0
            else:
                nwbraydenbonus += 2
                nwbraydentotal = 0
                nwbraydenchance = 0
            nwordcount
            nwordcount += 3
        if message.content == "!ml hero1 add Akai":
            global jahero1
            jahero1 = "Akai"
            await message.channel.send("Jack's hero #1 is now Akai! :panda_face: ")
        if message.content == "!ml hero1 add Balmond":
            jahero1 = "Balmond"
            await message.channel.send("Jack's hero #1 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero1 add Belerick":
            jahero1 = "Belerick"
            await message.channel.send("Jack's hero #1 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero1 add Franco":
            jahero1 = "Franco"
            await message.channel.send("Jack's hero #1 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero1 add Esmerelda":
            jahero1 = "Esmerelda"
            await message.channel.send("Jack's hero #1 is now Esmerelda! :shield: ")
        if message.content == "!ml hero1 add Gatotkaca":
            jahero1 = "Gatotkaca"
            await message.channel.send("Jack's hero #1 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero1 add Grock":
            jahero1 = "Grock"
            await message.channel.send("Jack's hero #1 is now Grock! :european_castle: ")
        if message.content == "!ml hero1 add Hilda":
            jahero1 = "Hilda"
            await message.channel.send("Jack's hero #1 is now Hilda! :runner: ")
        if message.content == "!ml hero1 add Hylos":
            jahero1 = "Hylos"
            await message.channel.send("Jack's hero #1 is now Hylos! :unicorn: ")
        if message.content == "!ml hero1 add Johnson":
            jahero1 = "Johnson"
            await message.channel.send("Jack's hero #1 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero1 add Khufra":
            jahero1 = "Khufra"
            await message.channel.send("Jack's hero #1 is now Khufra! :clown: ")
        if message.content == "!ml hero1 add Lolita":
            jahero1 = "Lolita"
            await message.channel.send("Jack's hero #1 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jahero1 = "Masha"
            await message.channel.send("Jack's hero #1 is now Masha! :bear: ")
        if message.content == "!ml hero1 add Minotaur":
            jahero1 = "Minotaur"
            await message.channel.send("Jack's hero #1 is now Minotaur! :cow: ")
        if message.content == "!ml hero1 add Tigreal":
            jahero1 = "Tigreal"
            await message.channel.send("Jack's hero #1 is now Tigreal! :moyai: ")
        if message.content == "!ml hero1 add Uranus":
            jahero1 = "Uranus"
            await message.channel.send("Jack's hero #1 is now Uranus! :peach: ")
        if message.content == "!ml hero1 add X.Borg":
            jahero1 = "X.Borg"
            await message.channel.send("Jack's hero #1 is now X.Borg! :fire: ")
        if message.content == "!ml hero1 add Aldous":
            jahero1 = "Aldous"
            await message.channel.send("Jack's hero #1 is now Aldous! :fist: ")
        if message.content == "!ml hero1 add Alpha":
            jahero1 = "Alpha"
            await message.channel.send("Jack's hero #1 is now Alpha! :airplane: ")
        if message.content == "!ml hero1 add Alucard":
            jahero1 = "Alucard"
            await message.channel.send("Jack's hero #1 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero1 add Argus":
            jahero1 = "Argus"
            await message.channel.send("Jack's hero #1 is now Argus! :angel: ")
        if message.content == "!ml hero1 add Badang":
            jahero1 = "Badang"
            await message.channel.send("Jack's hero #1 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero1 add Bane":
            jahero1 = "Bane"
            await message.channel.send("Jack's hero #1 is now Bane! :octopus: ")
        if message.content == "!ml hero1 add Chou":
            jahero1 = "Chou"
            await message.channel.send("Jack's hero #1 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero1 add Dyrroth":
            jahero1 = "Dyrroth"
            await message.channel.send("Jack's hero #1 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero1 add Freya":
            jahero1 = "Freya"
            await message.channel.send("Jack's hero #1 is now Freya! :hammer: ")
        if message.content == "!ml hero1 add Guinevere":
            jahero1 = "Guinevere"
            await message.channel.send("Jack's hero #1 is now Guinevere! :dress:  ")
        if message.content == "!ml hero1 add Jawhead":
            jahero1 = "Jawhead"
            await message.channel.send("Jack's hero #1 is now Jawhead! :robot: ")
        if message.content == "!ml hero1 add Kaja":
            jahero1 = "Kaja"
            await message.channel.send("Jack's hero #1 is now Kaja! :bird: ")
        if message.content == "!ml hero1 add Lapu-Lapu":
            jahero1 = "Lapu-Lapu"
            await message.channel.send("Jack's hero #1 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero1 add Leomord":
            jahero1 = "Leomord"
            await message.channel.send("Jack's hero #1 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero1 add Martis":
            jahero1 = "Martis"
            await message.channel.send("Jack's hero #1 is now Martis! :crab: ")
        if message.content == "!ml hero1 add Minsitthar":
            jahero1 = "Minsitthar"
            await message.channel.send("Jack's hero #1 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero1 add Roger":
            jahero1 = "Roger"
            await message.channel.send("Jack's hero #1 is now Roger! :wolf: ")
        if message.content == "!ml hero1 add Ruby":
            jahero1 = "Ruby"
            await message.channel.send("Jack's hero #1 is now Ruby! :heart: ")
        if message.content == "!ml hero1 add Sun":
            jahero1 = "Sun"
            await message.channel.send("Jack's hero #1 is now Sun! :monkey_face: ")
        if message.content == "!ml hero1 add Thamuz":
            jahero1 = "Thamuz"
            await message.channel.send("Jack's hero #1 is now Thamuz! :rage: ")
        if message.content == "!ml hero1 add Terizla":
            jahero1 = "Terizla"
            await message.channel.send("Jack's hero #1 is now Terizla! :hammer: ")
        if message.content == "!ml hero1 add Zilong":
            jahero1 = "Zilong"
            await message.channel.send("Jack's hero #1 is now Zilong! :dragon: ")
        if message.content == "!ml hero1 add Fanny":
            jahero1 = "Fanny"
            await message.channel.send("Jack's hero #1 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero1 add Gusion":
            jahero1 = "Gusion"
            await message.channel.send(
                "Jack's hero #1 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero1 add Hanzo":
            jahero1 = "Hanzo"
            await message.channel.send("Jack's hero #1 is now Hanzo! :ghost: ")
        if message.content == "!ml hero1 add Hayabusa":
            jahero1 = "Hayabusa"
            await message.channel.send("Jack's hero #1 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero1 add Helcurt":
            jahero1 = "Helcurt"
            await message.channel.send("Jack's hero #1 is now Helcurt! :mute:  ")
        if message.content == "!ml hero1 add Karina":
            jahero1 = "Karina"
            await message.channel.send("Jack's hero #1 is now Karina! :purple_heart: ")
        if message.content == "!ml hero1 add Lancelot":
            jahero1 = "Lancelot"
            await message.channel.send("Jack's hero #1 is now Lancelot! :fencer: ")
        if message.content == "!ml hero1 add Lesley":
            jahero1 = "Lesley"
            await message.channel.send("Jack's hero #1 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero1 add Natalia":
            jahero1 = "Natalia"
            await message.channel.send("Jack's hero #1 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero1 add Saber":
            jahero1 = "Saber"
            await message.channel.send("Jack's hero #1 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero1 add Selena":
            jahero1 = "Selena"
            await message.channel.send("Jack's hero #1 is now Selena! :sleeping:  ")
        if message.content == "!ml hero1 add Alice":
            jahero1 = "Alice"
            await message.channel.send("Jack's hero #1 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero1 add Aurora":
            jahero1 = "Aurora"
            await message.channel.send("Jack's hero #1 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jahero1 = "Chang'e"
            await message.channel.send("Jack's hero #1 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero1 add Cyclops":
            jahero1 = "Cyclops"
            await message.channel.send("Jack's hero #1 is now Cyclops! :eye:  ")
        if message.content == "!ml hero1 add Eudora":
            jahero1 = "Eudora"
            await message.channel.send("Jack's hero #1 is now Eudora! :zap: ")
        if message.content == "!ml hero1 add Faramis":
            jahero1 = "Faramis"
            await message.channel.send("Jack's hero #1 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero1 add Gord":
            jahero1 = "Gord"
            await message.channel.send("Jack's hero #1 is now Gord! :snowboarder:")
        if message.content == "!ml hero1 add Harith":
            jahero1 = "Harith"
            await message.channel.send("Jack's hero #1 is now Harith! :older_man: ")
        if message.content == "!ml hero1 add Harley":
            jahero1 = "Harley"
            await message.channel.send("Jack's hero #1 is now Harley! :tophat: ")
        if message.content == "!ml hero1 add Kadita":
            jahero1 = "Kadita"
            await message.channel.send("Jack's hero #1 is now Kadita! :droplet: ")
        if message.content == "!ml hero1 add Kagura":
            jahero1 = "Kagura"
            await message.channel.send("Jack's hero #1 is now Kagura! :umbrella2:  ")
        if message.content == "!ml hero1 add Lunox":
            jahero1 = "Lunox"
            await message.channel.send("Jack's hero #1 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero1 add Lylia":
            jahero1 = "Lylia"
            await message.channel.send("Jack's hero #1 is now Lylia! :boom: ")
        if message.content == "!ml hero1 add Nana":
            jahero1 = "Nana"
            await message.channel.send("Jack's hero #1 is now Nana! :cat:  ")
        if message.content == "!ml hero1 add Odette":
            jahero1 = "Odette"
            await message.channel.send("Jack's hero #1 is now Odette! :duck: ")
        if message.content == "!ml hero1 add Pharsa":
            jahero1 = "Pharsa"
            await message.channel.send("Jack's hero #1 is now Pharsa! :dove:  ")
        if message.content == "!ml hero1 add Vale":
            jahero1 = "Vale"
            await message.channel.send("Jack's hero #1 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero1 add Valir":
            jahero1 = "Valir"
            await message.channel.send("Jack's hero #1 is now Valir! :fire:")
        if message.content == "!ml hero1 add Vexanna":
            jahero1 = "Vexanna"
            await message.channel.send("Jack's hero #1 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero1 add Bruno":
            jahero1 = "Bruno"
            await message.channel.send("Jack's hero #1 is now Bruno! :soccer:  ")
        if message.content == "!ml hero1 add Claude":
            jahero1 = "Claude"
            await message.channel.send("Jack's hero #1 is now Claude! :monkey:  ")
        if message.content == "!ml hero1 add Clint":
            jahero1 = "Clint"
            await message.channel.send("Jack's hero #1 is now Clint! :cowboy: ")
        if message.content == "!ml hero1 add Granger":
            jahero1 = "Granger"
            await message.channel.send("Jack's hero #1 is now Granger! :violin: ")
        if message.content == "!ml hero1 add Hanabi":
            jahero1 = "Hanabi"
            await message.channel.send("Jack's hero #1 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero1 add Irithel":
            jahero1 = "Irithel"
            await message.channel.send("Jack's hero #1 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero1 add Karrie":
            jahero1 = "Karrie"
            await message.channel.send(
                "Jack's hero #1 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero1 add Kimmy":
            jahero1 = "Kimmy"
            await message.channel.send("Jack's hero #1 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero1 add Layla":
            jahero1 = "Layla"
            await message.channel.send("Jack's hero #1 is now Layla! :haircut:  ")
        if message.content == "!ml hero1 add Miya":
            jahero1 = "Miya"
            await message.channel.send("Jack's hero #1 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero1 add Moskov":
            jahero1 = "Moskov"
            await message.channel.send("Jack's hero #1 is now Moskov! :imp: ")
        if message.content == "!ml hero1 add Yi Sun-Shin":
            jahero1 = "Yi Sun-Shin"
            await message.channel.send("Jack's hero #1 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero1 add Angela":
            jahero1 = "Angela"
            await message.channel.send("Jack's hero #1 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero1 add Diggie":
            jahero1 = "Diggie"
            await message.channel.send("Jack's hero #1 is now Diggie! :owl: ")
        if message.content == "!ml hero1 add Estes":
            jahero1 = "Estes"
            await message.channel.send("Jack's hero #1 is now Estes! :ear:  ")
        if message.content == "!ml hero1 add Rafaela":
            jahero1 = "Rafaela"
            await message.channel.send("Jack's hero #1 is now Rafaela! :angel: ")
        if message.content == "!ml hero1 add Rynn":
            jahero1 = "Rynn"
            await message.channel.send("Jack's hero #1 is now Rynn! ")
        if message.content == "!ml hero2 add Akai":
            global jahero2
            jahero2 = "Akai"
            await message.channel.send("Jack's hero #2 is now Akai! :panda_face: ")
        if message.content == "!ml hero2 add Balmond":
            jahero2 = "Balmond"
            await message.channel.send("Jack's hero #2 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero2 add Belerick":
            jahero2 = "Belerick"
            await message.channel.send("Jack's hero #2 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero2 add Franco":
            jahero2 = "Franco"
            await message.channel.send("Jack's hero #2 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero2 add Esmerelda":
            jahero2 = "Esmerelda"
            await message.channel.send("Jack's hero #2 is now Esmerelda! :shield: ")
        if message.content == "!ml hero2 add Gatotkaca":
            jahero2 = "Gatotkaca"
            await message.channel.send("Jack's hero #2 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero2 add Grock":
            jahero2 = "Grock"
            await message.channel.send("Jack's hero #2 is now Grock! :european_castle: ")
        if message.content == "!ml hero2 add Hilda":
            jahero2 = "Hilda"
            await message.channel.send("Jack's hero #2 is now Hilda! :runner: ")
        if message.content == "!ml hero2 add Hylos":
            jahero2 = "Hylos"
            await message.channel.send("Jack's hero #2 is now Hylos! :unicorn: ")
        if message.content == "!ml hero2 add Johnson":
            jahero2 = "Johnson"
            await message.channel.send("Jack's hero #2 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero2 add Khufra":
            jahero2 = "Khufra"
            await message.channel.send("Jack's hero #2 is now Khufra! :clown: ")
        if message.content == "!ml hero2 add Lolita":
            jahero2 = "Lolita"
            await message.channel.send("Jack's hero #2 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jahero2 = "Masha"
            await message.channel.send("Jack's hero #2 is now Masha! :bear: ")
        if message.content == "!ml hero2 add Minotaur":
            jahero2 = "Minotaur"
            await message.channel.send("Jack's hero #2 is now Minotaur! :cow: ")
        if message.content == "!ml hero2 add Tigreal":
            jahero2 = "Tigreal"
            await message.channel.send("Jack's hero #2 is now Tigreal! :moyai: ")
        if message.content == "!ml hero2 add Uranus":
            jahero2 = "Uranus"
            await message.channel.send("Jack's hero #2 is now Uranus! :peach: ")
        if message.content == "!ml hero2 add X.Borg":
            jahero2 = "X.Borg"
            await message.channel.send("Jack's hero #2 is now X.Borg! :fire: ")
        if message.content == "!ml hero2 add Aldous":
            jahero2 = "Aldous"
            await message.channel.send("Jack's hero #2 is now Aldous! :fist: ")
        if message.content == "!ml hero2 add Alpha":
            jahero2 = "Alpha"
            await message.channel.send("Jack's hero #2 is now Alpha! :airplane: ")
        if message.content == "!ml hero2 add Alucard":
            jahero2 = "Alucard"
            await message.channel.send("Jack's hero #2 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero2 add Argus":
            jahero2 = "Argus"
            await message.channel.send("Jack's hero #2 is now Argus! :angel: ")
        if message.content == "!ml hero2 add Badang":
            jahero2 = "Badang"
            await message.channel.send("Jack's hero #2 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero2 add Bane":
            jahero2 = "Bane"
            await message.channel.send("Jack's hero #2 is now Bane! :octopus: ")
        if message.content == "!ml hero2 add Chou":
            jahero2 = "Chou"
            await message.channel.send("Jack's hero #2 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero2 add Dyrroth":
            jahero2 = "Dyrroth"
            await message.channel.send("Jack's hero #2 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero2 add Freya":
            jahero2 = "Freya"
            await message.channel.send("Jack's hero #2 is now Freya! :hammer: ")
        if message.content == "!ml hero2 add Guinevere":
            jahero2 = "Guinevere"
            await message.channel.send("Jack's hero #2 is now Guinevere! :dress:  ")
        if message.content == "!ml hero2 add Jawhead":
            jahero2 = "Jawhead"
            await message.channel.send("Jack's hero #2 is now Jawhead! :robot: ")
        if message.content == "!ml hero2 add Kaja":
            jahero2 = "Kaja"
            await message.channel.send("Jack's hero #2 is now Kaja! :bird: ")
        if message.content == "!ml hero2 add Lapu-Lapu":
            jahero2 = "Lapu-Lapu"
            await message.channel.send("Jack's hero #2 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero2 add Leomord":
            jahero2 = "Leomord"
            await message.channel.send("Jack's hero #2 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero2 add Martis":
            jahero2 = "Martis"
            await message.channel.send("Jack's hero #2 is now Martis! :crab: ")
        if message.content == "!ml hero2 add Minsitthar":
            jahero2 = "Minsitthar"
            await message.channel.send("Jack's hero #2 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero2 add Roger":
            jahero2 = "Roger"
            await message.channel.send("Jack's hero #2 is now Roger! :wolf: ")
        if message.content == "!ml hero2 add Ruby":
            jahero2 = "Ruby"
            await message.channel.send("Jack's hero #2 is now Ruby! :heart: ")
        if message.content == "!ml hero2 add Sun":
            jahero2 = "Sun"
            await message.channel.send("Jack's hero #2 is now Sun! :monkey_face: ")
        if message.content == "!ml hero2 add Thamuz":
            jahero2 = "Thamuz"
            await message.channel.send("Jack's hero #2 is now Thamuz! :rage: ")
        if message.content == "!ml hero2 add Terizla":
            jahero2 = "Terizla"
            await message.channel.send("Jack's hero #2 is now Terizla! :hammer: ")
        if message.content == "!ml hero2 add Zilong":
            jahero2 = "Zilong"
            await message.channel.send("Jack's hero #2 is now Zilong! :dragon: ")
        if message.content == "!ml hero2 add Fanny":
            jahero2 = "Fanny"
            await message.channel.send("Jack's hero #2 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero2 add Gusion":
            jahero2 = "Gusion"
            await message.channel.send(
                "Jack's hero #2 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero2 add Hanzo":
            jahero2 = "Hanzo"
            await message.channel.send("Jack's hero #2 is now Hanzo! :ghost: ")
        if message.content == "!ml hero2 add Hayabusa":
            jahero2 = "Hayabusa"
            await message.channel.send("Jack's hero #2 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero2 add Helcurt":
            jahero2 = "Helcurt"
            await message.channel.send("Jack's hero #2 is now Helcurt! :mute:  ")
        if message.content == "!ml hero2 add Karina":
            jahero2 = "Karina"
            await message.channel.send("Jack's hero #2 is now Karina! :purple_heart: ")
        if message.content == "!ml hero2 add Lancelot":
            jahero2 = "Lancelot"
            await message.channel.send("Jack's hero #2 is now Lancelot! :fencer: ")
        if message.content == "!ml hero2 add Lesley":
            jahero2 = "Lesley"
            await message.channel.send("Jack's hero #2 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero2 add Natalia":
            jahero2 = "Natalia"
            await message.channel.send("Jack's hero #2 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero2 add Saber":
            jahero2 = "Saber"
            await message.channel.send("Jack's hero #2 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero2 add Selena":
            jahero2 = "Selena"
            await message.channel.send("Jack's hero #2 is now Selena! :sleeping:  ")
        if message.content == "!ml hero2 add Alice":
            jahero2 = "Alice"
            await message.channel.send("Jack's hero #2 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero2 add Aurora":
            jahero2 = "Aurora"
            await message.channel.send("Jack's hero #2 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jahero2 = "Chang'e"
            await message.channel.send("Jack's hero #2 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero2 add Cyclops":
            jahero2 = "Cyclops"
            await message.channel.send("Jack's hero #2 is now Cyclops! :eye:  ")
        if message.content == "!ml hero2 add Eudora":
            jahero2 = "Eudora"
            await message.channel.send("Jack's hero #2 is now Eudora! :zap: ")
        if message.content == "!ml hero2 add Faramis":
            jahero2 = "Faramis"
            await message.channel.send("Jack's hero #2 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero2 add Gord":
            jahero2 = "Gord"
            await message.channel.send("Jack's hero #2 is now Gord! :snowboarder:")
        if message.content == "!ml hero2 add Harith":
            jahero2 = "Harith"
            await message.channel.send("Jack's hero #2 is now Harith! :older_man: ")
        if message.content == "!ml hero2 add Harley":
            jahero2 = "Harley"
            await message.channel.send("Jack's hero #2 is now Harley! :tophat: ")
        if message.content == "!ml hero2 add Kadita":
            jahero2 = "Kadita"
            await message.channel.send("Jack's hero #2 is now Kadita! :droplet: ")
        if message.content == "!ml hero2 add Kagura":
            jahero2 = "Kagura"
            await message.channel.send("Jack's hero #2 is now Kagura! :umbrella2:  ")
        if message.content == "!ml hero2 add Lunox":
            jahero2 = "Lunox"
            await message.channel.send("Jack's hero #2 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero2 add Lylia":
            jahero2 = "Lylia"
            await message.channel.send("Jack's hero #2 is now Lylia! :boom: ")
        if message.content == "!ml hero2 add Nana":
            jahero2 = "Nana"
            await message.channel.send("Jack's hero #2 is now Nana! :cat:  ")
        if message.content == "!ml hero2 add Odette":
            jahero2 = "Odette"
            await message.channel.send("Jack's hero #2 is now Odette! :duck: ")
        if message.content == "!ml hero2 add Pharsa":
            jahero2 = "Pharsa"
            await message.channel.send("Jack's hero #2 is now Pharsa! :dove:  ")
        if message.content == "!ml hero2 add Vale":
            jahero2 = "Vale"
            await message.channel.send("Jack's hero #2 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero2 add Valir":
            jahero2 = "Valir"
            await message.channel.send("Jack's hero #2 is now Valir! :fire:")
        if message.content == "!ml hero2 add Vexanna":
            jahero2 = "Vexanna"
            await message.channel.send("Jack's hero #2 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero2 add Bruno":
            jahero2 = "Bruno"
            await message.channel.send("Jack's hero #2 is now Bruno! :soccer:  ")
        if message.content == "!ml hero2 add Claude":
            jahero2 = "Claude"
            await message.channel.send("Jack's hero #2 is now Claude! :monkey:  ")
        if message.content == "!ml hero2 add Clint":
            jahero2 = "Clint"
            await message.channel.send("Jack's hero #2 is now Clint! :cowboy: ")
        if message.content == "!ml hero2 add Granger":
            jahero2 = "Granger"
            await message.channel.send("Jack's hero #2 is now Granger! :violin: ")
        if message.content == "!ml hero2 add Hanabi":
            jahero2 = "Hanabi"
            await message.channel.send("Jack's hero #2 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero2 add Irithel":
            jahero2 = "Irithel"
            await message.channel.send("Jack's hero #2 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero2 add Karrie":
            jahero2 = "Karrie"
            await message.channel.send(
                "Jack's hero #2 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero2 add Kimmy":
            jahero2 = "Kimmy"
            await message.channel.send("Jack's hero #2 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero2 add Layla":
            jahero2 = "Layla"
            await message.channel.send("Jack's hero #2 is now Layla! :haircut:  ")
        if message.content == "!ml hero2 add Miya":
            jahero2 = "Miya"
            await message.channel.send("Jack's hero #2 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero2 add Moskov":
            jahero2 = "Moskov"
            await message.channel.send("Jack's hero #2 is now Moskov! :imp: ")
        if message.content == "!ml hero2 add Yi Sun-Shin":
            jahero2 = "Yi Sun-Shin"
            await message.channel.send("Jack's hero #2 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero2 add Angela":
            jahero2 = "Angela"
            await message.channel.send("Jack's hero #2 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero2 add Diggie":
            jahero2 = "Diggie"
            await message.channel.send("Jack's hero #2 is now Diggie! :owl: ")
        if message.content == "!ml hero2 add Estes":
            jahero2 = "Estes"
            await message.channel.send("Jack's hero #2 is now Estes! :ear:  ")
        if message.content == "!ml hero2 add Rafaela":
            jahero2 = "Rafaela"
            await message.channel.send("Jack's hero #2 is now Rafaela! :angel: ")
        if message.content == "!ml hero2 add Rynn":
            jahero2 = "Rynn"
            await message.channel.send("Jack's hero #2 is now Rynn! ")
        if message.content == "!ml hero3 add Akai":
            global jahero3
            jahero3 = "Akai"
            await message.channel.send("Jack's hero #3 is now Akai! :panda_face: ")
        if message.content == "!ml hero3 add Balmond":
            jahero3 = "Balmond"
            await message.channel.send("Jack's hero #3 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero3 add Belerick":
            jahero3 = "Belerick"
            await message.channel.send("Jack's hero #3 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero3 add Franco":
            jahero3 = "Franco"
            await message.channel.send("Jack's hero #3 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero3 add Esmerelda":
            jahero3 = "Esmerelda"
            await message.channel.send("Jack's hero #3 is now Esmerelda! :shield: ")
        if message.content == "!ml hero3 add Gatotkaca":
            jahero3 = "Gatotkaca"
            await message.channel.send("Jack's hero #3 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero3 add Grock":
            jahero3 = "Grock"
            await message.channel.send("Jack's hero #3 is now Grock! :european_castle: ")
        if message.content == "!ml hero3 add Hilda":
            jahero3 = "Hilda"
            await message.channel.send("Jack's hero #3 is now Hilda! :runner: ")
        if message.content == "!ml hero3 add Hylos":
            jahero3 = "Hylos"
            await message.channel.send("Jack's hero #3 is now Hylos! :unicorn: ")
        if message.content == "!ml hero3 add Johnson":
            jahero3 = "Johnson"
            await message.channel.send("Jack's hero #3 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero3 add Khufra":
            jahero3 = "Khufra"
            await message.channel.send("Jack's hero #3 is now Khufra! :clown: ")
        if message.content == "!ml hero3 add Lolita":
            jahero3 = "Lolita"
            await message.channel.send("Jack's hero #3 is now Lolita! :lollipop: ")
        if message.content == "!ml hero3 add Masha":
            jahero3 = "Masha"
            await message.channel.send("Jack's hero #3 is now Masha! :bear: ")
        if message.content == "!ml hero3 add Minotaur":
            jahero3 = "Minotaur"
            await message.channel.send("Jack's hero #3 is now Minotaur! :cow: ")
        if message.content == "!ml hero3 add Tigreal":
            jahero3 = "Tigreal"
            await message.channel.send("Jack's hero #3 is now Tigreal! :moyai: ")
        if message.content == "!ml hero3 add Uranus":
            jahero3 = "Uranus"
            await message.channel.send("Jack's hero #3 is now Uranus! :peach: ")
        if message.content == "!ml hero3 add X.Borg":
            jahero3 = "X.Borg"
            await message.channel.send("Jack's hero #3 is now X.Borg! :fire: ")
        if message.content == "!ml hero3 add Aldous":
            jahero3 = "Aldous"
            await message.channel.send("Jack's hero #3 is now Aldous! :fist: ")
        if message.content == "!ml hero3 add Alpha":
            jahero3 = "Alpha"
            await message.channel.send("Jack's hero #3 is now Alpha! :airplane: ")
        if message.content == "!ml hero3 add Alucard":
            jahero3 = "Alucard"
            await message.channel.send("Jack's hero #3 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero3 add Argus":
            jahero3 = "Argus"
            await message.channel.send("Jack's hero #3 is now Argus! :angel: ")
        if message.content == "!ml hero3 add Badang":
            jahero3 = "Badang"
            await message.channel.send("Jack's hero #3 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero3 add Bane":
            jahero3 = "Bane"
            await message.channel.send("Jack's hero #3 is now Bane! :octopus: ")
        if message.content == "!ml hero3 add Chou":
            jahero3 = "Chou"
            await message.channel.send("Jack's hero #3 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero3 add Dyrroth":
            jahero3 = "Dyrroth"
            await message.channel.send("Jack's hero #3 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero3 add Freya":
            jahero3 = "Freya"
            await message.channel.send("Jack's hero #3 is now Freya! :hammer: ")
        if message.content == "!ml hero3 add Guinevere":
            jahero3 = "Guinevere"
            await message.channel.send("Jack's hero #3 is now Guinevere! :dress:  ")
        if message.content == "!ml hero3 add Jawhead":
            jahero3 = "Jawhead"
            await message.channel.send("Jack's hero #3 is now Jawhead! :robot: ")
        if message.content == "!ml hero3 add Kaja":
            jahero3 = "Kaja"
            await message.channel.send("Jack's hero #3 is now Kaja! :bird: ")
        if message.content == "!ml hero3 add Lapu-Lapu":
            jahero3 = "Lapu-Lapu"
            await message.channel.send("Jack's hero #3 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero3 add Leomord":
            jahero3 = "Leomord"
            await message.channel.send("Jack's hero #3 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero3 add Martis":
            jahero3 = "Martis"
            await message.channel.send("Jack's hero #3 is now Martis! :crab: ")
        if message.content == "!ml hero3 add Minsitthar":
            jahero3 = "Minsitthar"
            await message.channel.send("Jack's hero #3 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero3 add Roger":
            jahero3 = "Roger"
            await message.channel.send("Jack's hero #3 is now Roger! :wolf: ")
        if message.content == "!ml hero3 add Ruby":
            jahero3 = "Ruby"
            await message.channel.send("Jack's hero #3 is now Ruby! :heart: ")
        if message.content == "!ml hero3 add Sun":
            jahero3 = "Sun"
            await message.channel.send("Jack's hero #3 is now Sun! :monkey_face: ")
        if message.content == "!ml hero3 add Thamuz":
            jahero3 = "Thamuz"
            await message.channel.send("Jack's hero #3 is now Thamuz! :rage: ")
        if message.content == "!ml hero3 add Terizla":
            jahero3 = "Terizla"
            await message.channel.send("Jack's hero #3 is now Terizla! :hammer: ")
        if message.content == "!ml hero3 add Zilong":
            jahero3 = "Zilong"
            await message.channel.send("Jack's hero #3 is now Zilong! :dragon: ")
        if message.content == "!ml hero3 add Fanny":
            jahero3 = "Fanny"
            await message.channel.send("Jack's hero #3 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero3 add Gusion":
            jahero3 = "Gusion"
            await message.channel.send(
                "Jack's hero #3 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero3 add Hanzo":
            jahero3 = "Hanzo"
            await message.channel.send("Jack's hero #3 is now Hanzo! :ghost: ")
        if message.content == "!ml hero3 add Hayabusa":
            jahero3 = "Hayabusa"
            await message.channel.send("Jack's hero #3 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero3 add Helcurt":
            jahero3 = "Helcurt"
            await message.channel.send("Jack's hero #3 is now Helcurt! :mute:  ")
        if message.content == "!ml hero3 add Karina":
            jahero3 = "Karina"
            await message.channel.send("Jack's hero #3 is now Karina! :purple_heart: ")
        if message.content == "!ml hero3 add Lancelot":
            jahero3 = "Lancelot"
            await message.channel.send("Jack's hero #3 is now Lancelot! :fencer: ")
        if message.content == "!ml hero3 add Lesley":
            jahero3 = "Lesley"
            await message.channel.send("Jack's hero #3 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero3 add Natalia":
            jahero3 = "Natalia"
            await message.channel.send("Jack's hero #3 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero3 add Saber":
            jahero3 = "Saber"
            await message.channel.send("Jack's hero #3 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero3 add Selena":
            jahero3 = "Selena"
            await message.channel.send("Jack's hero #3 is now Selena! :sleeping:  ")
        if message.content == "!ml hero3 add Alice":
            jahero3 = "Alice"
            await message.channel.send("Jack's hero #3 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero3 add Aurora":
            jahero3 = "Aurora"
            await message.channel.send("Jack's hero #3 is now Aurora! :snow: ")
        if message.content == "!ml hero3 add Chang'e":
            jahero3 = "Chang'e"
            await message.channel.send("Jack's hero #3 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero3 add Cyclops":
            jahero3 = "Cyclops"
            await message.channel.send("Jack's hero #3 is now Cyclops! :eye:  ")
        if message.content == "!ml hero3 add Eudora":
            jahero3 = "Eudora"
            await message.channel.send("Jack's hero #3 is now Eudora! :zap: ")
        if message.content == "!ml hero3 add Faramis":
            jahero3 = "Faramis"
            await message.channel.send("Jack's hero #3 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero3 add Gord":
            jahero3 = "Gord"
            await message.channel.send("Jack's hero #3 is now Gord! :snowboarder:")
        if message.content == "!ml hero3 add Harith":
            jahero3 = "Harith"
            await message.channel.send("Jack's hero #3 is now Harith! :older_man: ")
        if message.content == "!ml hero3 add Harley":
            jahero3 = "Harley"
            await message.channel.send("Jack's hero #3 is now Harley! :tophat: ")
        if message.content == "!ml hero3 add Kadita":
            jahero3 = "Kadita"
            await message.channel.send("Jack's hero #3 is now Kadita! :droplet: ")
        if message.content == "!ml hero3 add Kagura":
            jahero3 = "Kagura"
            await message.channel.send("Jack's hero #3 is now Kagura! :umbrella2:  ")
        if message.content == "!ml hero3 add Lunox":
            jahero3 = "Lunox"
            await message.channel.send("Jack's hero #3 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero3 add Lylia":
            jahero3 = "Lylia"
            await message.channel.send("Jack's hero #3 is now Lylia! :boom: ")
        if message.content == "!ml hero3 add Nana":
            jahero3 = "Nana"
            await message.channel.send("Jack's hero #3 is now Nana! :cat:  ")
        if message.content == "!ml hero3 add Odette":
            jahero3 = "Odette"
            await message.channel.send("Jack's hero #3 is now Odette! :duck: ")
        if message.content == "!ml hero3 add Pharsa":
            jahero3 = "Pharsa"
            await message.channel.send("Jack's hero #3 is now Pharsa! :dove:  ")
        if message.content == "!ml hero3 add Vale":
            jahero3 = "Vale"
            await message.channel.send("Jack's hero #3 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero3 add Valir":
            jahero3 = "Valir"
            await message.channel.send("Jack's hero #3 is now Valir! :fire:")
        if message.content == "!ml hero3 add Vexanna":
            jahero3 = "Vexanna"
            await message.channel.send("Jack's hero #3 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero3 add Bruno":
            jahero3 = "Bruno"
            await message.channel.send("Jack's hero #3 is now Bruno! :soccer:  ")
        if message.content == "!ml hero3 add Claude":
            jahero3 = "Claude"
            await message.channel.send("Jack's hero #3 is now Claude! :monkey:  ")
        if message.content == "!ml hero3 add Clint":
            jahero3 = "Clint"
            await message.channel.send("Jack's hero #3 is now Clint! :cowboy: ")
        if message.content == "!ml hero3 add Granger":
            jahero3 = "Granger"
            await message.channel.send("Jack's hero #3 is now Granger! :violin: ")
        if message.content == "!ml hero3 add Hanabi":
            jahero3 = "Hanabi"
            await message.channel.send("Jack's hero #3 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero3 add Irithel":
            jahero3 = "Irithel"
            await message.channel.send("Jack's hero #3 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero3 add Karrie":
            jahero3 = "Karrie"
            await message.channel.send(
                "Jack's hero #3 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero3 add Kimmy":
            jahero3 = "Kimmy"
            await message.channel.send("Jack's hero #3 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero3 add Layla":
            jahero3 = "Layla"
            await message.channel.send("Jack's hero #3 is now Layla! :haircut:  ")
        if message.content == "!ml hero3 add Miya":
            jahero3 = "Miya"
            await message.channel.send("Jack's hero #3 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero3 add Moskov":
            jahero3 = "Moskov"
            await message.channel.send("Jack's hero #3 is now Moskov! :imp: ")
        if message.content == "!ml hero3 add Yi Sun-Shin":
            jahero3 = "Yi Sun-Shin"
            await message.channel.send("Jack's hero #3 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero3 add Angela":
            jahero3 = "Angela"
            await message.channel.send("Jack's hero #3 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero3 add Diggie":
            jahero3 = "Diggie"
            await message.channel.send("Jack's hero #3 is now Diggie! :owl: ")
        if message.content == "!ml hero3 add Estes":
            jahero3 = "Estes"
            await message.channel.send("Jack's hero #3 is now Estes! :ear:  ")
        if message.content == "!ml hero3 add Rafaela":
            jahero3 = "Rafaela"
            await message.channel.send("Jack's hero #3 is now Rafaela! :angel: ")
        if message.content == "!ml hero3 add Rynn":
            jahero3 = "Rynn"
            await message.channel.send("Jack's hero #3 is now Rynn! ")
        if message.content == "!ml hero4 add Akai":
            global jahero4
            jahero4 = "Akai"
            await message.channel.send("Jack's hero #4 is now Akai! :panda_face: ")
        if message.content == "!ml hero4 add Balmond":
            jahero4 = "Balmond"
            await message.channel.send("Jack's hero #4 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero4 add Belerick":
            jahero4 = "Belerick"
            await message.channel.send("Jack's hero #4 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero4 add Franco":
            jahero4 = "Franco"
            await message.channel.send("Jack's hero #4 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero4 add Esmerelda":
            jahero4 = "Esmerelda"
            await message.channel.send("Jack's hero #4 is now Esmerelda! :shield: ")
        if message.content == "!ml hero4 add Gatotkaca":
            jahero4 = "Gatotkaca"
            await message.channel.send("Jack's hero #4 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero4 add Grock":
            jahero4 = "Grock"
            await message.channel.send("Jack's hero #4 is now Grock! :european_castle: ")
        if message.content == "!ml hero4 add Hilda":
            jahero4 = "Hilda"
            await message.channel.send("Jack's hero #4 is now Hilda! :runner: ")
        if message.content == "!ml hero4 add Hylos":
            jahero4 = "Hylos"
            await message.channel.send("Jack's hero #4 is now Hylos! :unicorn: ")
        if message.content == "!ml hero4 add Johnson":
            jahero4 = "Johnson"
            await message.channel.send("Jack's hero #4 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero4 add Khufra":
            jahero4 = "Khufra"
            await message.channel.send("Jack's hero #4 is now Khufra! :clown: ")
        if message.content == "!ml hero4 add Lolita":
            jahero4 = "Lolita"
            await message.channel.send("Jack's hero #4 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jahero4 = "Masha"
            await message.channel.send("Jack's hero #4 is now Masha! :bear: ")
        if message.content == "!ml hero4 add Minotaur":
            jahero4 = "Minotaur"
            await message.channel.send("Jack's hero #4 is now Minotaur! :cow: ")
        if message.content == "!ml hero4 add Tigreal":
            jahero4 = "Tigreal"
            await message.channel.send("Jack's hero #4 is now Tigreal! :moyai: ")
        if message.content == "!ml hero4 add Uranus":
            jahero4 = "Uranus"
            await message.channel.send("Jack's hero #4 is now Uranus! :peach: ")
        if message.content == "!ml hero4 add X.Borg":
            jahero4 = "X.Borg"
            await message.channel.send("Jack's hero #4 is now X.Borg! :fire: ")
        if message.content == "!ml hero4 add Aldous":
            jahero4 = "Aldous"
            await message.channel.send("Jack's hero #4 is now Aldous! :fist: ")
        if message.content == "!ml hero4 add Alpha":
            jahero4 = "Alpha"
            await message.channel.send("Jack's hero #4 is now Alpha! :airplane: ")
        if message.content == "!ml hero4 add Alucard":
            jahero4 = "Alucard"
            await message.channel.send("Jack's hero #4 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero4 add Argus":
            jahero4 = "Argus"
            await message.channel.send("Jack's hero #4 is now Argus! :angel: ")
        if message.content == "!ml hero4 add Badang":
            jahero4 = "Badang"
            await message.channel.send("Jack's hero #4 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero4 add Bane":
            jahero4 = "Bane"
            await message.channel.send("Jack's hero #4 is now Bane! :octopus: ")
        if message.content == "!ml hero4 add Chou":
            jahero4 = "Chou"
            await message.channel.send("Jack's hero #4 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero4 add Dyrroth":
            jahero4 = "Dyrroth"
            await message.channel.send("Jack's hero #4 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero4 add Freya":
            jahero4 = "Freya"
            await message.channel.send("Jack's hero #4 is now Freya! :hammer: ")
        if message.content == "!ml hero4 add Guinevere":
            jahero4 = "Guinevere"
            await message.channel.send("Jack's hero #4 is now Guinevere! :dress:  ")
        if message.content == "!ml hero4 add Jawhead":
            jahero4 = "Jawhead"
            await message.channel.send("Jack's hero #4 is now Jawhead! :robot: ")
        if message.content == "!ml hero4 add Kaja":
            jahero4 = "Kaja"
            await message.channel.send("Jack's hero #4 is now Kaja! :bird: ")
        if message.content == "!ml hero4 add Lapu-Lapu":
            jahero4 = "Lapu-Lapu"
            await message.channel.send("Jack's hero #4 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero4 add Leomord":
            jahero4 = "Leomord"
            await message.channel.send("Jack's hero #4 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero4 add Martis":
            jahero4 = "Martis"
            await message.channel.send("Jack's hero #4 is now Martis! :crab: ")
        if message.content == "!ml hero4 add Minsitthar":
            jahero4 = "Minsitthar"
            await message.channel.send("Jack's hero #4 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero4 add Roger":
            jahero4 = "Roger"
            await message.channel.send("Jack's hero #4 is now Roger! :wolf: ")
        if message.content == "!ml hero4 add Ruby":
            jahero4 = "Ruby"
            await message.channel.send("Jack's hero #4 is now Ruby! :heart: ")
        if message.content == "!ml hero4 add Sun":
            jahero4 = "Sun"
            await message.channel.send("Jack's hero #4 is now Sun! :monkey_face: ")
        if message.content == "!ml hero4 add Thamuz":
            jahero4 = "Thamuz"
            await message.channel.send("Jack's hero #4 is now Thamuz! :rage: ")
        if message.content == "!ml hero4 add Terizla":
            jahero4 = "Terizla"
            await message.channel.send("Jack's hero #4 is now Terizla! :hammer: ")
        if message.content == "!ml hero4 add Zilong":
            jahero4 = "Zilong"
            await message.channel.send("Jack's hero #4 is now Zilong! :dragon: ")
        if message.content == "!ml hero4 add Fanny":
            jahero4 = "Fanny"
            await message.channel.send("Jack's hero #4 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero4 add Gusion":
            jahero4 = "Gusion"
            await message.channel.send(
                "Jack's hero #4 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero4 add Hanzo":
            jahero4 = "Hanzo"
            await message.channel.send("Jack's hero #4 is now Hanzo! :ghost: ")
        if message.content == "!ml hero4 add Hayabusa":
            jahero4 = "Hayabusa"
            await message.channel.send("Jack's hero #4 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero4 add Helcurt":
            jahero4 = "Helcurt"
            await message.channel.send("Jack's hero #4 is now Helcurt! :mute:  ")
        if message.content == "!ml hero4 add Karina":
            jahero4 = "Karina"
            await message.channel.send("Jack's hero #4 is now Karina! :purple_heart: ")
        if message.content == "!ml hero4 add Lancelot":
            jahero4 = "Lancelot"
            await message.channel.send("Jack's hero #4 is now Lancelot! :fencer: ")
        if message.content == "!ml hero4 add Lesley":
            jahero4 = "Lesley"
            await message.channel.send("Jack's hero #4 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero4 add Natalia":
            jahero4 = "Natalia"
            await message.channel.send("Jack's hero #4 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero4 add Saber":
            jahero4 = "Saber"
            await message.channel.send("Jack's hero #4 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero4 add Selena":
            jahero4 = "Selena"
            await message.channel.send("Jack's hero #4 is now Selena! :sleeping:  ")
        if message.content == "!ml hero4 add Alice":
            jahero4 = "Alice"
            await message.channel.send("Jack's hero #4 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero4 add Aurora":
            jahero4 = "Aurora"
            await message.channel.send("Jack's hero #4 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jahero4 = "Chang'e"
            await message.channel.send("Jack's hero #4 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero4 add Cyclops":
            jahero4 = "Cyclops"
            await message.channel.send("Jack's hero #4 is now Cyclops! :eye:  ")
        if message.content == "!ml hero4 add Eudora":
            jahero4 = "Eudora"
            await message.channel.send("Jack's hero #4 is now Eudora! :zap: ")
        if message.content == "!ml hero4 add Faramis":
            jahero4 = "Faramis"
            await message.channel.send("Jack's hero #4 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero4 add Gord":
            jahero4 = "Gord"
            await message.channel.send("Jack's hero #4 is now Gord! :snowboarder:")
        if message.content == "!ml hero4 add Harith":
            jahero4 = "Harith"
            await message.channel.send("Jack's hero #4 is now Harith! :older_man: ")
        if message.content == "!ml hero4 add Harley":
            jahero4 = "Harley"
            await message.channel.send("Jack's hero #4 is now Harley! :tophat: ")
        if message.content == "!ml hero4 add Kadita":
            jahero4 = "Kadita"
            await message.channel.send("Jack's hero #4 is now Kadita! :droplet: ")
        if message.content == "!ml hero4 add Kagura":
            jahero4 = "Kagura"
            await message.channel.send("Jack's hero #4 is now Kagura! :umbrella4:  ")
        if message.content == "!ml hero4 add Lunox":
            jahero4 = "Lunox"
            await message.channel.send("Jack's hero #4 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero4 add Lylia":
            jahero4 = "Lylia"
            await message.channel.send("Jack's hero #4 is now Lylia! :boom: ")
        if message.content == "!ml hero4 add Nana":
            jahero4 = "Nana"
            await message.channel.send("Jack's hero #4 is now Nana! :cat:  ")
        if message.content == "!ml hero4 add Odette":
            jahero4 = "Odette"
            await message.channel.send("Jack's hero #4 is now Odette! :duck: ")
        if message.content == "!ml hero4 add Pharsa":
            jahero4 = "Pharsa"
            await message.channel.send("Jack's hero #4 is now Pharsa! :dove:  ")
        if message.content == "!ml hero4 add Vale":
            jahero4 = "Vale"
            await message.channel.send("Jack's hero #4 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero4 add Valir":
            jahero4 = "Valir"
            await message.channel.send("Jack's hero #4 is now Valir! :fire:")
        if message.content == "!ml hero4 add Vexanna":
            jahero4 = "Vexanna"
            await message.channel.send("Jack's hero #4 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero4 add Bruno":
            jahero4 = "Bruno"
            await message.channel.send("Jack's hero #4 is now Bruno! :soccer:  ")
        if message.content == "!ml hero4 add Claude":
            jahero4 = "Claude"
            await message.channel.send("Jack's hero #4 is now Claude! :monkey:  ")
        if message.content == "!ml hero4 add Clint":
            jahero4 = "Clint"
            await message.channel.send("Jack's hero #4 is now Clint! :cowboy: ")
        if message.content == "!ml hero4 add Granger":
            jahero4 = "Granger"
            await message.channel.send("Jack's hero #4 is now Granger! :violin: ")
        if message.content == "!ml hero4 add Hanabi":
            jahero4 = "Hanabi"
            await message.channel.send("Jack's hero #4 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero4 add Irithel":
            jahero4 = "Irithel"
            await message.channel.send("Jack's hero #4 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero4 add Karrie":
            jahero4 = "Karrie"
            await message.channel.send(
                "Jack's hero #4 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero3 add Kimmy":
            jahero3 = "Kimmy"
            await message.channel.send("Jack's hero #3 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero4 add Layla":
            jahero4 = "Layla"
            await message.channel.send("Jack's hero #4 is now Layla! :haircut:  ")
        if message.content == "!ml hero4 add Miya":
            jahero4 = "Miya"
            await message.channel.send("Jack's hero #4 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero4 add Moskov":
            jahero4 = "Moskov"
            await message.channel.send("Jack's hero #4 is now Moskov! :imp: ")
        if message.content == "!ml hero4 add Yi Sun-Shin":
            jahero4 = "Yi Sun-Shin"
            await message.channel.send("Jack's hero #4 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero4 add Angela":
            jahero4 = "Angela"
            await message.channel.send("Jack's hero #4 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero4 add Diggie":
            jahero4 = "Diggie"
            await message.channel.send("Jack's hero #4 is now Diggie! :owl: ")
        if message.content == "!ml hero4 add Estes":
            jahero4 = "Estes"
            await message.channel.send("Jack's hero #4 is now Estes! :ear:  ")
        if message.content == "!ml hero4 add Rafaela":
            jahero4 = "Rafaela"
            await message.channel.send("Jack's hero #4 is now Rafaela! :angel: ")
        if message.content == "!ml hero4 add Rynn":
            jahero4 = "Rynn"
            await message.channel.send("Jack's hero #4 is now Rynn! ")
        if message.content == "!ml hero5 add Akai":
            global jahero5
            jahero5 = "Akai"
            await message.channel.send("Jack's hero #5 is now Akai! :panda_face: ")
        if message.content == "!ml hero5 add Balmond":
            jahero5 = "Balmond"
            await message.channel.send("Jack's hero #5 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero5 add Belerick":
            jahero5 = "Belerick"
            await message.channel.send("Jack's hero #5 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero5 add Franco":
            jahero5 = "Franco"
            await message.channel.send("Jack's hero #5 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero5 add Esmerelda":
            jahero5 = "Esmerelda"
            await message.channel.send("Jack's hero #5 is now Esmerelda! :shield: ")
        if message.content == "!ml hero5 add Gatotkaca":
            jahero5 = "Gatotkaca"
            await message.channel.send("Jack's hero #5 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero5 add Grock":
            jahero5 = "Grock"
            await message.channel.send("Jack's hero #5 is now Grock! :european_castle: ")
        if message.content == "!ml hero5 add Hilda":
            jahero5 = "Hilda"
            await message.channel.send("Jack's hero #5 is now Hilda! :runner: ")
        if message.content == "!ml hero5 add Hylos":
            jahero5 = "Hylos"
            await message.channel.send("Jack's hero #5 is now Hylos! :unicorn: ")
        if message.content == "!ml hero5 add Johnson":
            jahero5 = "Johnson"
            await message.channel.send("Jack's hero #5 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero5 add Khufra":
            jahero5 = "Khufra"
            await message.channel.send("Jack's hero #5 is now Khufra! :clown: ")
        if message.content == "!ml hero5 add Lolita":
            jahero5 = "Lolita"
            await message.channel.send("Jack's hero #5 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jahero5 = "Masha"
            await message.channel.send("Jack's hero #5 is now Masha! :bear: ")
        if message.content == "!ml hero5 add Minotaur":
            jahero5 = "Minotaur"
            await message.channel.send("Jack's hero #5 is now Minotaur! :cow: ")
        if message.content == "!ml hero5 add Tigreal":
            jahero5 = "Tigreal"
            await message.channel.send("Jack's hero #5 is now Tigreal! :moyai: ")
        if message.content == "!ml hero5 add Uranus":
            jahero5 = "Uranus"
            await message.channel.send("Jack's hero #5 is now Uranus! :peach: ")
        if message.content == "!ml hero5 add X.Borg":
            jahero5 = "X.Borg"
            await message.channel.send("Jack's hero #5 is now X.Borg! :fire: ")
        if message.content == "!ml hero5 add Aldous":
            jahero5 = "Aldous"
            await message.channel.send("Jack's hero #5 is now Aldous! :fist: ")
        if message.content == "!ml hero5 add Alpha":
            jahero5 = "Alpha"
            await message.channel.send("Jack's hero #5 is now Alpha! :airplane: ")
        if message.content == "!ml hero5 add Alucard":
            jahero5 = "Alucard"
            await message.channel.send("Jack's hero #5 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero5 add Argus":
            jahero5 = "Argus"
            await message.channel.send("Jack's hero #5 is now Argus! :angel: ")
        if message.content == "!ml hero5 add Badang":
            jahero5 = "Badang"
            await message.channel.send("Jack's hero #5 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero5 add Bane":
            jahero5 = "Bane"
            await message.channel.send("Jack's hero #5 is now Bane! :octopus: ")
        if message.content == "!ml hero5 add Chou":
            jahero5 = "Chou"
            await message.channel.send("Jack's hero #5 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero5 add Dyrroth":
            jahero5 = "Dyrroth"
            await message.channel.send("Jack's hero #5 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero5 add Freya":
            jahero5 = "Freya"
            await message.channel.send("Jack's hero #5 is now Freya! :hammer: ")
        if message.content == "!ml hero5 add Guinevere":
            jahero5 = "Guinevere"
            await message.channel.send("Jack's hero #5 is now Guinevere! :dress:  ")
        if message.content == "!ml hero5 add Jawhead":
            jahero5 = "Jawhead"
            await message.channel.send("Jack's hero #5 is now Jawhead! :robot: ")
        if message.content == "!ml hero5 add Kaja":
            jahero5 = "Kaja"
            await message.channel.send("Jack's hero #5 is now Kaja! :bird: ")
        if message.content == "!ml hero5 add Lapu-Lapu":
            jahero5 = "Lapu-Lapu"
            await message.channel.send("Jack's hero #5 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero5 add Leomord":
            jahero5 = "Leomord"
            await message.channel.send("Jack's hero #5 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero5 add Martis":
            jahero5 = "Martis"
            await message.channel.send("Jack's hero #5 is now Martis! :crab: ")
        if message.content == "!ml hero5 add Minsitthar":
            jahero5 = "Minsitthar"
            await message.channel.send("Jack's hero #5 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero5 add Roger":
            jahero5 = "Roger"
            await message.channel.send("Jack's hero #5 is now Roger! :wolf: ")
        if message.content == "!ml hero5 add Ruby":
            jahero5 = "Ruby"
            await message.channel.send("Jack's hero #5 is now Ruby! :heart: ")
        if message.content == "!ml hero5 add Sun":
            jahero5 = "Sun"
            await message.channel.send("Jack's hero #5 is now Sun! :monkey_face: ")
        if message.content == "!ml hero5 add Thamuz":
            jahero5 = "Thamuz"
            await message.channel.send("Jack's hero #5 is now Thamuz! :rage: ")
        if message.content == "!ml hero5 add Terizla":
            jahero5 = "Terizla"
            await message.channel.send("Jack's hero #5 is now Terizla! :hammer: ")
        if message.content == "!ml hero5 add Zilong":
            jahero5 = "Zilong"
            await message.channel.send("Jack's hero #5 is now Zilong! :dragon: ")
        if message.content == "!ml hero5 add Fanny":
            jahero5 = "Fanny"
            await message.channel.send("Jack's hero #5 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero5 add Gusion":
            jahero5 = "Gusion"
            await message.channel.send(
                "Jack's hero #5 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero5 add Hanzo":
            jahero5 = "Hanzo"
            await message.channel.send("Jack's hero #5 is now Hanzo! :ghost: ")
        if message.content == "!ml hero5 add Hayabusa":
            jahero5 = "Hayabusa"
            await message.channel.send("Jack's hero #5 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero5 add Helcurt":
            jahero5 = "Helcurt"
            await message.channel.send("Jack's hero #5 is now Helcurt! :mute:  ")
        if message.content == "!ml hero5 add Karina":
            jahero5 = "Karina"
            await message.channel.send("Jack's hero #5 is now Karina! :purple_heart: ")
        if message.content == "!ml hero5 add Lancelot":
            jahero5 = "Lancelot"
            await message.channel.send("Jack's hero #5 is now Lancelot! :fencer: ")
        if message.content == "!ml hero5 add Lesley":
            jahero5 = "Lesley"
            await message.channel.send("Jack's hero #5 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero5 add Natalia":
            jahero5 = "Natalia"
            await message.channel.send("Jack's hero #5 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero5 add Saber":
            jahero5 = "Saber"
            await message.channel.send("Jack's hero #5 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero5 add Selena":
            jahero5 = "Selena"
            await message.channel.send("Jack's hero #5 is now Selena! :sleeping:  ")
        if message.content == "!ml hero5 add Alice":
            jahero5 = "Alice"
            await message.channel.send("Jack's hero #5 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero5 add Aurora":
            jahero5 = "Aurora"
            await message.channel.send("Jack's hero #5 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jahero5 = "Chang'e"
            await message.channel.send("Jack's hero #5 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero5 add Cyclops":
            jahero5 = "Cyclops"
            await message.channel.send("Jack's hero #5 is now Cyclops! :eye:  ")
        if message.content == "!ml hero5 add Eudora":
            jahero5 = "Eudora"
            await message.channel.send("Jack's hero #5 is now Eudora! :zap: ")
        if message.content == "!ml hero5 add Faramis":
            jahero5 = "Faramis"
            await message.channel.send("Jack's hero #5 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero5 add Gord":
            jahero5 = "Gord"
            await message.channel.send("Jack's hero #5 is now Gord! :snowboarder:")
        if message.content == "!ml hero5 add Harith":
            jahero5 = "Harith"
            await message.channel.send("Jack's hero #5 is now Harith! :older_man: ")
        if message.content == "!ml hero5 add Harley":
            jahero5 = "Harley"
            await message.channel.send("Jack's hero #5 is now Harley! :tophat: ")
        if message.content == "!ml hero5 add Kadita":
            jahero5 = "Kadita"
            await message.channel.send("Jack's hero #5 is now Kadita! :droplet: ")
        if message.content == "!ml hero5 add Kagura":
            jahero5 = "Kagura"
            await message.channel.send("Jack's hero #5 is now Kagura! :umbrella5:  ")
        if message.content == "!ml hero5 add Lunox":
            jahero5 = "Lunox"
            await message.channel.send("Jack's hero #5 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero5 add Lylia":
            jahero5 = "Lylia"
            await message.channel.send("Jack's hero #5 is now Lylia! :boom: ")
        if message.content == "!ml hero5 add Nana":
            jahero5 = "Nana"
            await message.channel.send("Jack's hero #5 is now Nana! :cat:  ")
        if message.content == "!ml hero5 add Odette":
            jahero5 = "Odette"
            await message.channel.send("Jack's hero #5 is now Odette! :duck: ")
        if message.content == "!ml hero5 add Pharsa":
            jahero5 = "Pharsa"
            await message.channel.send("Jack's hero #5 is now Pharsa! :dove:  ")
        if message.content == "!ml hero5 add Vale":
            jahero5 = "Vale"
            await message.channel.send("Jack's hero #5 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero5 add Valir":
            jahero5 = "Valir"
            await message.channel.send("Jack's hero #5 is now Valir! :fire:")
        if message.content == "!ml hero5 add Vexanna":
            jahero5 = "Vexanna"
            await message.channel.send("Jack's hero #5 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero5 add Bruno":
            jahero5 = "Bruno"
            await message.channel.send("Jack's hero #5 is now Bruno! :soccer:  ")
        if message.content == "!ml hero5 add Claude":
            jahero5 = "Claude"
            await message.channel.send("Jack's hero #5 is now Claude! :monkey:  ")
        if message.content == "!ml hero5 add Clint":
            jahero5 = "Clint"
            await message.channel.send("Jack's hero #5 is now Clint! :cowboy: ")
        if message.content == "!ml hero5 add Granger":
            jahero5 = "Granger"
            await message.channel.send("Jack's hero #5 is now Granger! :violin: ")
        if message.content == "!ml hero5 add Hanabi":
            jahero5 = "Hanabi"
            await message.channel.send("Jack's hero #5 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero5 add Irithel":
            jahero5 = "Irithel"
            await message.channel.send("Jack's hero #5 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero5 add Karrie":
            jahero5 = "Karrie"
            await message.channel.send(
                "Jack's hero #5 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero5 add Kimmy":
            jahero5 = "Kimmy"
            await message.channel.send("Jack's hero #5 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero5 add Layla":
            jahero5 = "Layla"
            await message.channel.send("Jack's hero #5 is now Layla! :haircut:  ")
        if message.content == "!ml hero5 add Miya":
            jahero5 = "Miya"
            await message.channel.send("Jack's hero #5 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero5 add Moskov":
            jahero5 = "Moskov"
            await message.channel.send("Jack's hero #5 is now Moskov! :imp: ")
        if message.content == "!ml hero5 add Yi Sun-Shin":
            jahero5 = "Yi Sun-Shin"
            await message.channel.send("Jack's hero #5 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero5 add Angela":
            jahero5 = "Angela"
            await message.channel.send("Jack's hero #5 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero5 add Diggie":
            jahero5 = "Diggie"
            await message.channel.send("Jack's hero #5 is now Diggie! :owl: ")
        if message.content == "!ml hero5 add Estes":
            jahero5 = "Estes"
            await message.channel.send("Jack's hero #5 is now Estes! :ear:  ")
        if message.content == "!ml hero5 add Rafaela":
            jahero5 = "Rafaela"
            await message.channel.send("Jack's hero #5 is now Rafaela! :angel: ")
        if message.content == "!ml hero5 add Rynn":
            jahero5 = "Rynn"
            await message.channel.send("Jack's hero #5 is now Rynn! ")
        if message.content == "!ml hero6 add Akai":
            global jahero6
            jahero6 = "Akai"
            await message.channel.send("Jack's hero #6 is now Akai! :panda_face: ")
        if message.content == "!ml hero6 add Balmond":
            jahero6 = "Balmond"
            await message.channel.send("Jack's hero #6 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero6 add Belerick":
            jahero6 = "Belerick"
            await message.channel.send("Jack's hero #6 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero6 add Franco":
            jahero6 = "Franco"
            await message.channel.send("Jack's hero #6 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero6 add Esmerelda":
            jahero6 = "Esmerelda"
            await message.channel.send("Jack's hero #6 is now Esmerelda! :shield: ")
        if message.content == "!ml hero6 add Gatotkaca":
            jahero6 = "Gatotkaca"
            await message.channel.send("Jack's hero #6 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero6 add Grock":
            jahero6 = "Grock"
            await message.channel.send("Jack's hero #6 is now Grock! :european_castle: ")
        if message.content == "!ml hero6 add Hilda":
            jahero6 = "Hilda"
            await message.channel.send("Jack's hero #6 is now Hilda! :runner: ")
        if message.content == "!ml hero6 add Hylos":
            jahero6 = "Hylos"
            await message.channel.send("Jack's hero #6 is now Hylos! :unicorn: ")
        if message.content == "!ml hero6 add Johnson":
            jahero6 = "Johnson"
            await message.channel.send("Jack's hero #6 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero6 add Khufra":
            jahero6 = "Khufra"
            await message.channel.send("Jack's hero #6 is now Khufra! :clown: ")
        if message.content == "!ml hero6 add Lolita":
            jahero6 = "Lolita"
            await message.channel.send("Jack's hero #6 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jahero6 = "Masha"
            await message.channel.send("Jack's hero #6 is now Masha! :bear: ")
        if message.content == "!ml hero6 add Minotaur":
            jahero6 = "Minotaur"
            await message.channel.send("Jack's hero #6 is now Minotaur! :cow: ")
        if message.content == "!ml hero6 add Tigreal":
            jahero6 = "Tigreal"
            await message.channel.send("Jack's hero #6 is now Tigreal! :moyai: ")
        if message.content == "!ml hero6 add Uranus":
            jahero6 = "Uranus"
            await message.channel.send("Jack's hero #6 is now Uranus! :peach: ")
        if message.content == "!ml hero6 add X.Borg":
            jahero6 = "X.Borg"
            await message.channel.send("Jack's hero #6 is now X.Borg! :fire: ")
        if message.content == "!ml hero6 add Aldous":
            jahero6 = "Aldous"
            await message.channel.send("Jack's hero #6 is now Aldous! :fist: ")
        if message.content == "!ml hero6 add Alpha":
            jahero6 = "Alpha"
            await message.channel.send("Jack's hero #6 is now Alpha! :airplane: ")
        if message.content == "!ml hero6 add Alucard":
            jahero6 = "Alucard"
            await message.channel.send("Jack's hero #6 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero6 add Argus":
            jahero6 = "Argus"
            await message.channel.send("Jack's hero #6 is now Argus! :angel: ")
        if message.content == "!ml hero6 add Badang":
            jahero6 = "Badang"
            await message.channel.send("Jack's hero #6 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero6 add Bane":
            jahero6 = "Bane"
            await message.channel.send("Jack's hero #6 is now Bane! :octopus: ")
        if message.content == "!ml hero6 add Chou":
            jahero6 = "Chou"
            await message.channel.send("Jack's hero #6 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero6 add Dyrroth":
            jahero6 = "Dyrroth"
            await message.channel.send("Jack's hero #6 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero6 add Freya":
            jahero6 = "Freya"
            await message.channel.send("Jack's hero #6 is now Freya! :hammer: ")
        if message.content == "!ml hero6 add Guinevere":
            jahero6 = "Guinevere"
            await message.channel.send("Jack's hero #6 is now Guinevere! :dress:  ")
        if message.content == "!ml hero6 add Jawhead":
            jahero6 = "Jawhead"
            await message.channel.send("Jack's hero #6 is now Jawhead! :robot: ")
        if message.content == "!ml hero6 add Kaja":
            jahero6 = "Kaja"
            await message.channel.send("Jack's hero #6 is now Kaja! :bird: ")
        if message.content == "!ml hero6 add Lapu-Lapu":
            jahero6 = "Lapu-Lapu"
            await message.channel.send("Jack's hero #6 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero6 add Leomord":
            jahero6 = "Leomord"
            await message.channel.send("Jack's hero #6 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero6 add Martis":
            jahero6 = "Martis"
            await message.channel.send("Jack's hero #6 is now Martis! :crab: ")
        if message.content == "!ml hero6 add Minsitthar":
            jahero6 = "Minsitthar"
            await message.channel.send("Jack's hero #6 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero6 add Roger":
            jahero6 = "Roger"
            await message.channel.send("Jack's hero #6 is now Roger! :wolf: ")
        if message.content == "!ml hero6 add Ruby":
            jahero6 = "Ruby"
            await message.channel.send("Jack's hero #6 is now Ruby! :heart: ")
        if message.content == "!ml hero6 add Sun":
            jahero6 = "Sun"
            await message.channel.send("Jack's hero #6 is now Sun! :monkey_face: ")
        if message.content == "!ml hero6 add Thamuz":
            jahero6 = "Thamuz"
            await message.channel.send("Jack's hero #6 is now Thamuz! :rage: ")
        if message.content == "!ml hero6 add Terizla":
            jahero6 = "Terizla"
            await message.channel.send("Jack's hero #6 is now Terizla! :hammer: ")
        if message.content == "!ml hero6 add Zilong":
            jahero6 = "Zilong"
            await message.channel.send("Jack's hero #6 is now Zilong! :dragon: ")
        if message.content == "!ml hero6 add Fanny":
            jahero6 = "Fanny"
            await message.channel.send("Jack's hero #6 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero6 add Gusion":
            jahero6 = "Gusion"
            await message.channel.send(
                "Jack's hero #6 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero6 add Hanzo":
            jahero6 = "Hanzo"
            await message.channel.send("Jack's hero #6 is now Hanzo! :ghost: ")
        if message.content == "!ml hero6 add Hayabusa":
            jahero6 = "Hayabusa"
            await message.channel.send("Jack's hero #6 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero6 add Helcurt":
            jahero6 = "Helcurt"
            await message.channel.send("Jack's hero #6 is now Helcurt! :mute:  ")
        if message.content == "!ml hero6 add Karina":
            jahero6 = "Karina"
            await message.channel.send("Jack's hero #6 is now Karina! :purple_heart: ")
        if message.content == "!ml hero6 add Lancelot":
            jahero6 = "Lancelot"
            await message.channel.send("Jack's hero #6 is now Lancelot! :fencer: ")
        if message.content == "!ml hero6 add Lesley":
            jahero6 = "Lesley"
            await message.channel.send("Jack's hero #6 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero6 add Natalia":
            jahero6 = "Natalia"
            await message.channel.send("Jack's hero #6 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero6 add Saber":
            jahero6 = "Saber"
            await message.channel.send("Jack's hero #6 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero6 add Selena":
            jahero6 = "Selena"
            await message.channel.send("Jack's hero #6 is now Selena! :sleeping:  ")
        if message.content == "!ml hero6 add Alice":
            jahero6 = "Alice"
            await message.channel.send("Jack's hero #6 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero6 add Aurora":
            jahero6 = "Aurora"
            await message.channel.send("Jack's hero #6 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jahero6 = "Chang'e"
            await message.channel.send("Jack's hero #6 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero6 add Cyclops":
            jahero6 = "Cyclops"
            await message.channel.send("Jack's hero #6 is now Cyclops! :eye:  ")
        if message.content == "!ml hero6 add Eudora":
            jahero6 = "Eudora"
            await message.channel.send("Jack's hero #6 is now Eudora! :zap: ")
        if message.content == "!ml hero6 add Faramis":
            jahero6 = "Faramis"
            await message.channel.send("Jack's hero #6 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero6 add Gord":
            jahero6 = "Gord"
            await message.channel.send("Jack's hero #6 is now Gord! :snowboarder:")
        if message.content == "!ml hero6 add Harith":
            jahero6 = "Harith"
            await message.channel.send("Jack's hero #6 is now Harith! :older_man: ")
        if message.content == "!ml hero6 add Harley":
            jahero6 = "Harley"
            await message.channel.send("Jack's hero #6 is now Harley! :tophat: ")
        if message.content == "!ml hero6 add Kadita":
            jahero6 = "Kadita"
            await message.channel.send("Jack's hero #6 is now Kadita! :droplet: ")
        if message.content == "!ml hero6 add Kagura":
            jahero6 = "Kagura"
            await message.channel.send("Jack's hero #6 is now Kagura! :umbrella6:  ")
        if message.content == "!ml hero6 add Lunox":
            jahero6 = "Lunox"
            await message.channel.send("Jack's hero #6 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero6 add Lylia":
            jahero6 = "Lylia"
            await message.channel.send("Jack's hero #6 is now Lylia! :boom: ")
        if message.content == "!ml hero6 add Nana":
            jahero6 = "Nana"
            await message.channel.send("Jack's hero #6 is now Nana! :cat:  ")
        if message.content == "!ml hero6 add Odette":
            jahero6 = "Odette"
            await message.channel.send("Jack's hero #6 is now Odette! :duck: ")
        if message.content == "!ml hero6 add Pharsa":
            jahero6 = "Pharsa"
            await message.channel.send("Jack's hero #6 is now Pharsa! :dove:  ")
        if message.content == "!ml hero6 add Vale":
            jahero6 = "Vale"
            await message.channel.send("Jack's hero #6 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero6 add Valir":
            jahero6 = "Valir"
            await message.channel.send("Jack's hero #6 is now Valir! :fire:")
        if message.content == "!ml hero6 add Vexanna":
            jahero6 = "Vexanna"
            await message.channel.send("Jack's hero #6 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero6 add Bruno":
            jahero6 = "Bruno"
            await message.channel.send("Jack's hero #6 is now Bruno! :soccer:  ")
        if message.content == "!ml hero6 add Claude":
            jahero6 = "Claude"
            await message.channel.send("Jack's hero #6 is now Claude! :monkey:  ")
        if message.content == "!ml hero6 add Clint":
            jahero6 = "Clint"
            await message.channel.send("Jack's hero #6 is now Clint! :cowboy: ")
        if message.content == "!ml hero6 add Granger":
            jahero6 = "Granger"
            await message.channel.send("Jack's hero #6 is now Granger! :violin: ")
        if message.content == "!ml hero6 add Hanabi":
            jahero6 = "Hanabi"
            await message.channel.send("Jack's hero #6 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero6 add Irithel":
            jahero6 = "Irithel"
            await message.channel.send("Jack's hero #6 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero6 add Karrie":
            jahero6 = "Karrie"
            await message.channel.send(
                "Jack's hero #6 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero6 add Kimmy":
            jahero6 = "Kimmy"
            await message.channel.send("Jack's hero #6 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero6 add Layla":
            jahero6 = "Layla"
            await message.channel.send("Jack's hero #6 is now Layla! :haircut:  ")
        if message.content == "!ml hero6 add Miya":
            jahero6 = "Miya"
            await message.channel.send("Jack's hero #6 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero6 add Moskov":
            jahero6 = "Moskov"
            await message.channel.send("Jack's hero #6 is now Moskov! :imp: ")
        if message.content == "!ml hero6 add Yi Sun-Shin":
            jahero6 = "Yi Sun-Shin"
            await message.channel.send("Jack's hero #6 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero6 add Angela":
            jahero6 = "Angela"
            await message.channel.send("Jack's hero #6 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero6 add Diggie":
            jahero6 = "Diggie"
            await message.channel.send("Jack's hero #6 is now Diggie! :owl: ")
        if message.content == "!ml hero6 add Estes":
            jahero6 = "Estes"
            await message.channel.send("Jack's hero #6 is now Estes! :ear:  ")
        if message.content == "!ml hero6 add Rafaela":
            jahero6 = "Rafaela"
            await message.channel.send("Jack's hero #6 is now Rafaela! :angel: ")
        if message.content == "!ml hero6 add Rynn":
            jahero6 = "Rynn"
            await message.channel.send("Jack's hero #6 is now Rynn! ")
        if message.content == "!ml hero7 add Akai":
            global jahero7
            jahero7 = "Akai"
            await message.channel.send("Jack's hero #7 is now Akai! :panda_face: ")
        if message.content == "!ml hero7 add Balmond":
            jahero7 = "Balmond"
            await message.channel.send("Jack's hero #7 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero7 add Belerick":
            jahero7 = "Belerick"
            await message.channel.send("Jack's hero #7 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero7 add Franco":
            jahero7 = "Franco"
            await message.channel.send("Jack's hero #7 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero7 add Esmerelda":
            jahero7 = "Esmerelda"
            await message.channel.send("Jack's hero #7 is now Esmerelda! :shield: ")
        if message.content == "!ml hero7 add Gatotkaca":
            jahero7 = "Gatotkaca"
            await message.channel.send("Jack's hero #7 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero7 add Grock":
            jahero7 = "Grock"
            await message.channel.send("Jack's hero #7 is now Grock! :european_castle: ")
        if message.content == "!ml hero7 add Hilda":
            jahero7 = "Hilda"
            await message.channel.send("Jack's hero #7 is now Hilda! :runner: ")
        if message.content == "!ml hero7 add Hylos":
            jahero7 = "Hylos"
            await message.channel.send("Jack's hero #7 is now Hylos! :unicorn: ")
        if message.content == "!ml hero7 add Johnson":
            jahero7 = "Johnson"
            await message.channel.send("Jack's hero #7 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero7 add Khufra":
            jahero7 = "Khufra"
            await message.channel.send("Jack's hero #7 is now Khufra! :clown: ")
        if message.content == "!ml hero7 add Lolita":
            jahero7 = "Lolita"
            await message.channel.send("Jack's hero #7 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jahero7 = "Masha"
            await message.channel.send("Jack's hero #7 is now Masha! :bear: ")
        if message.content == "!ml hero7 add Minotaur":
            jahero7 = "Minotaur"
            await message.channel.send("Jack's hero #7 is now Minotaur! :cow: ")
        if message.content == "!ml hero7 add Tigreal":
            jahero7 = "Tigreal"
            await message.channel.send("Jack's hero #7 is now Tigreal! :moyai: ")
        if message.content == "!ml hero7 add Uranus":
            jahero7 = "Uranus"
            await message.channel.send("Jack's hero #7 is now Uranus! :peach: ")
        if message.content == "!ml hero7 add X.Borg":
            jahero7 = "X.Borg"
            await message.channel.send("Jack's hero #7 is now X.Borg! :fire: ")
        if message.content == "!ml hero7 add Aldous":
            jahero7 = "Aldous"
            await message.channel.send("Jack's hero #7 is now Aldous! :fist: ")
        if message.content == "!ml hero7 add Alpha":
            jahero7 = "Alpha"
            await message.channel.send("Jack's hero #7 is now Alpha! :airplane: ")
        if message.content == "!ml hero7 add Alucard":
            jahero7 = "Alucard"
            await message.channel.send("Jack's hero #7 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero7 add Argus":
            jahero7 = "Argus"
            await message.channel.send("Jack's hero #7 is now Argus! :angel: ")
        if message.content == "!ml hero7 add Badang":
            jahero7 = "Badang"
            await message.channel.send("Jack's hero #7 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero7 add Bane":
            jahero7 = "Bane"
            await message.channel.send("Jack's hero #7 is now Bane! :octopus: ")
        if message.content == "!ml hero7 add Chou":
            jahero7 = "Chou"
            await message.channel.send("Jack's hero #7 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero7 add Dyrroth":
            jahero7 = "Dyrroth"
            await message.channel.send("Jack's hero #7 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero7 add Freya":
            jahero7 = "Freya"
            await message.channel.send("Jack's hero #7 is now Freya! :hammer: ")
        if message.content == "!ml hero7 add Guinevere":
            jahero7 = "Guinevere"
            await message.channel.send("Jack's hero #7 is now Guinevere! :dress:  ")
        if message.content == "!ml hero7 add Jawhead":
            jahero7 = "Jawhead"
            await message.channel.send("Jack's hero #7 is now Jawhead! :robot: ")
        if message.content == "!ml hero7 add Kaja":
            jahero7 = "Kaja"
            await message.channel.send("Jack's hero #7 is now Kaja! :bird: ")
        if message.content == "!ml hero7 add Lapu-Lapu":
            jahero7 = "Lapu-Lapu"
            await message.channel.send("Jack's hero #7 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero7 add Leomord":
            jahero7 = "Leomord"
            await message.channel.send("Jack's hero #7 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero7 add Martis":
            jahero7 = "Martis"
            await message.channel.send("Jack's hero #7 is now Martis! :crab: ")
        if message.content == "!ml hero7 add Minsitthar":
            jahero7 = "Minsitthar"
            await message.channel.send("Jack's hero #7 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero7 add Roger":
            jahero7 = "Roger"
            await message.channel.send("Jack's hero #7 is now Roger! :wolf: ")
        if message.content == "!ml hero7 add Ruby":
            jahero7 = "Ruby"
            await message.channel.send("Jack's hero #7 is now Ruby! :heart: ")
        if message.content == "!ml hero7 add Sun":
            jahero7 = "Sun"
            await message.channel.send("Jack's hero #7 is now Sun! :monkey_face: ")
        if message.content == "!ml hero7 add Thamuz":
            jahero7 = "Thamuz"
            await message.channel.send("Jack's hero #7 is now Thamuz! :rage: ")
        if message.content == "!ml hero7 add Terizla":
            jahero7 = "Terizla"
            await message.channel.send("Jack's hero #7 is now Terizla! :hammer: ")
        if message.content == "!ml hero7 add Zilong":
            jahero7 = "Zilong"
            await message.channel.send("Jack's hero #7 is now Zilong! :dragon: ")
        if message.content == "!ml hero7 add Fanny":
            jahero7 = "Fanny"
            await message.channel.send("Jack's hero #7 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero7 add Gusion":
            jahero7 = "Gusion"
            await message.channel.send(
                "Jack's hero #7 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero7 add Hanzo":
            jahero7 = "Hanzo"
            await message.channel.send("Jack's hero #7 is now Hanzo! :ghost: ")
        if message.content == "!ml hero7 add Hayabusa":
            jahero7 = "Hayabusa"
            await message.channel.send("Jack's hero #7 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero7 add Helcurt":
            jahero7 = "Helcurt"
            await message.channel.send("Jack's hero #7 is now Helcurt! :mute:  ")
        if message.content == "!ml hero7 add Karina":
            jahero7 = "Karina"
            await message.channel.send("Jack's hero #7 is now Karina! :purple_heart: ")
        if message.content == "!ml hero7 add Lancelot":
            jahero7 = "Lancelot"
            await message.channel.send("Jack's hero #7 is now Lancelot! :fencer: ")
        if message.content == "!ml hero7 add Lesley":
            jahero7 = "Lesley"
            await message.channel.send("Jack's hero #7 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero7 add Natalia":
            jahero7 = "Natalia"
            await message.channel.send("Jack's hero #7 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero7 add Saber":
            jahero7 = "Saber"
            await message.channel.send("Jack's hero #7 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero7 add Selena":
            jahero7 = "Selena"
            await message.channel.send("Jack's hero #7 is now Selena! :sleeping:  ")
        if message.content == "!ml hero7 add Alice":
            jahero7 = "Alice"
            await message.channel.send("Jack's hero #7 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero7 add Aurora":
            jahero7 = "Aurora"
            await message.channel.send("Jack's hero #7 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jahero7 = "Chang'e"
            await message.channel.send("Jack's hero #7 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero7 add Cyclops":
            jahero7 = "Cyclops"
            await message.channel.send("Jack's hero #7 is now Cyclops! :eye:  ")
        if message.content == "!ml hero7 add Eudora":
            jahero7 = "Eudora"
            await message.channel.send("Jack's hero #7 is now Eudora! :zap: ")
        if message.content == "!ml hero7 add Faramis":
            jahero7 = "Faramis"
            await message.channel.send("Jack's hero #7 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero7 add Gord":
            jahero7 = "Gord"
            await message.channel.send("Jack's hero #7 is now Gord! :snowboarder:")
        if message.content == "!ml hero7 add Harith":
            jahero7 = "Harith"
            await message.channel.send("Jack's hero #7 is now Harith! :older_man: ")
        if message.content == "!ml hero7 add Harley":
            jahero7 = "Harley"
            await message.channel.send("Jack's hero #7 is now Harley! :tophat: ")
        if message.content == "!ml hero7 add Kadita":
            jahero7 = "Kadita"
            await message.channel.send("Jack's hero #7 is now Kadita! :droplet: ")
        if message.content == "!ml hero7 add Kagura":
            jahero7 = "Kagura"
            await message.channel.send("Jack's hero #7 is now Kagura! :umbrella7:  ")
        if message.content == "!ml hero7 add Lunox":
            jahero7 = "Lunox"
            await message.channel.send("Jack's hero #7 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero7 add Lylia":
            jahero7 = "Lylia"
            await message.channel.send("Jack's hero #7 is now Lylia! :boom: ")
        if message.content == "!ml hero7 add Nana":
            jahero7 = "Nana"
            await message.channel.send("Jack's hero #7 is now Nana! :cat:  ")
        if message.content == "!ml hero7 add Odette":
            jahero7 = "Odette"
            await message.channel.send("Jack's hero #7 is now Odette! :duck: ")
        if message.content == "!ml hero7 add Pharsa":
            jahero7 = "Pharsa"
            await message.channel.send("Jack's hero #7 is now Pharsa! :dove:  ")
        if message.content == "!ml hero7 add Vale":
            jahero7 = "Vale"
            await message.channel.send("Jack's hero #7 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero7 add Valir":
            jahero7 = "Valir"
            await message.channel.send("Jack's hero #7 is now Valir! :fire:")
        if message.content == "!ml hero7 add Vexanna":
            jahero7 = "Vexanna"
            await message.channel.send("Jack's hero #7 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero7 add Bruno":
            jahero7 = "Bruno"
            await message.channel.send("Jack's hero #7 is now Bruno! :soccer:  ")
        if message.content == "!ml hero7 add Claude":
            jahero7 = "Claude"
            await message.channel.send("Jack's hero #7 is now Claude! :monkey:  ")
        if message.content == "!ml hero7 add Clint":
            jahero7 = "Clint"
            await message.channel.send("Jack's hero #7 is now Clint! :cowboy: ")
        if message.content == "!ml hero7 add Granger":
            jahero7 = "Granger"
            await message.channel.send("Jack's hero #7 is now Granger! :violin: ")
        if message.content == "!ml hero7 add Hanabi":
            jahero7 = "Hanabi"
            await message.channel.send("Jack's hero #7 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero7 add Irithel":
            jahero7 = "Irithel"
            await message.channel.send("Jack's hero #7 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero7 add Karrie":
            jahero7 = "Karrie"
            await message.channel.send(
                "Jack's hero #7 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero7 add Kimmy":
            jahero7 = "Kimmy"
            await message.channel.send("Jack's hero #7 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero7 add Layla":
            jahero7 = "Layla"
            await message.channel.send("Jack's hero #7 is now Layla! :haircut:  ")
        if message.content == "!ml hero7 add Miya":
            jahero7 = "Miya"
            await message.channel.send("Jack's hero #7 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero7 add Moskov":
            jahero7 = "Moskov"
            await message.channel.send("Jack's hero #7 is now Moskov! :imp: ")
        if message.content == "!ml hero7 add Yi Sun-Shin":
            jahero7 = "Yi Sun-Shin"
            await message.channel.send("Jack's hero #7 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero7 add Angela":
            jahero7 = "Angela"
            await message.channel.send("Jack's hero #7 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero7 add Diggie":
            jahero7 = "Diggie"
            await message.channel.send("Jack's hero #7 is now Diggie! :owl: ")
        if message.content == "!ml hero7 add Estes":
            jahero7 = "Estes"
            await message.channel.send("Jack's hero #7 is now Estes! :ear:  ")
        if message.content == "!ml hero7 add Rafaela":
            jahero7 = "Rafaela"
            await message.channel.send("Jack's hero #7 is now Rafaela! :angel: ")
        if message.content == "!ml hero7 add Rynn":
            jahero7 = "Rynn"
            await message.channel.send("Jack's hero #7 is now Rynn! ")
        if message.content == "!ml hero8 add Akai":
            global jahero8
            jahero8 = "Akai"
            await message.channel.send("Jack's hero #8 is now Akai! :panda_face: ")
        if message.content == "!ml hero8 add Balmond":
            jahero8 = "Balmond"
            await message.channel.send("Jack's hero #8 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero8 add Belerick":
            jahero8 = "Belerick"
            await message.channel.send("Jack's hero #8 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero8 add Franco":
            jahero8 = "Franco"
            await message.channel.send("Jack's hero #8 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero8 add Esmerelda":
            jahero8 = "Esmerelda"
            await message.channel.send("Jack's hero #8 is now Esmerelda! :shield: ")
        if message.content == "!ml hero8 add Gatotkaca":
            jahero8 = "Gatotkaca"
            await message.channel.send("Jack's hero #8 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero8 add Grock":
            jahero8 = "Grock"
            await message.channel.send("Jack's hero #8 is now Grock! :european_castle: ")
        if message.content == "!ml hero8 add Hilda":
            jahero8 = "Hilda"
            await message.channel.send("Jack's hero #8 is now Hilda! :runner: ")
        if message.content == "!ml hero8 add Hylos":
            jahero8 = "Hylos"
            await message.channel.send("Jack's hero #8 is now Hylos! :unicorn: ")
        if message.content == "!ml hero8 add Johnson":
            jahero8 = "Johnson"
            await message.channel.send("Jack's hero #8 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero8 add Khufra":
            jahero8 = "Khufra"
            await message.channel.send("Jack's hero #8 is now Khufra! :clown: ")
        if message.content == "!ml hero8 add Lolita":
            jahero8 = "Lolita"
            await message.channel.send("Jack's hero #8 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jahero8 = "Masha"
            await message.channel.send("Jack's hero #8 is now Masha! :bear: ")
        if message.content == "!ml hero8 add Minotaur":
            jahero8 = "Minotaur"
            await message.channel.send("Jack's hero #8 is now Minotaur! :cow: ")
        if message.content == "!ml hero8 add Tigreal":
            jahero8 = "Tigreal"
            await message.channel.send("Jack's hero #8 is now Tigreal! :moyai: ")
        if message.content == "!ml hero8 add Uranus":
            jahero8 = "Uranus"
            await message.channel.send("Jack's hero #8 is now Uranus! :peach: ")
        if message.content == "!ml hero8 add X.Borg":
            jahero8 = "X.Borg"
            await message.channel.send("Jack's hero #8 is now X.Borg! :fire: ")
        if message.content == "!ml hero8 add Aldous":
            jahero8 = "Aldous"
            await message.channel.send("Jack's hero #8 is now Aldous! :fist: ")
        if message.content == "!ml hero8 add Alpha":
            jahero8 = "Alpha"
            await message.channel.send("Jack's hero #8 is now Alpha! :airplane: ")
        if message.content == "!ml hero8 add Alucard":
            jahero8 = "Alucard"
            await message.channel.send("Jack's hero #8 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero8 add Argus":
            jahero8 = "Argus"
            await message.channel.send("Jack's hero #8 is now Argus! :angel: ")
        if message.content == "!ml hero8 add Badang":
            jahero8 = "Badang"
            await message.channel.send("Jack's hero #8 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero8 add Bane":
            jahero8 = "Bane"
            await message.channel.send("Jack's hero #8 is now Bane! :octopus: ")
        if message.content == "!ml hero8 add Chou":
            jahero8 = "Chou"
            await message.channel.send("Jack's hero #8 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero8 add Dyrroth":
            jahero8 = "Dyrroth"
            await message.channel.send("Jack's hero #8 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero8 add Freya":
            jahero8 = "Freya"
            await message.channel.send("Jack's hero #8 is now Freya! :hammer: ")
        if message.content == "!ml hero8 add Guinevere":
            jahero8 = "Guinevere"
            await message.channel.send("Jack's hero #8 is now Guinevere! :dress:  ")
        if message.content == "!ml hero8 add Jawhead":
            jahero8 = "Jawhead"
            await message.channel.send("Jack's hero #8 is now Jawhead! :robot: ")
        if message.content == "!ml hero8 add Kaja":
            jahero8 = "Kaja"
            await message.channel.send("Jack's hero #8 is now Kaja! :bird: ")
        if message.content == "!ml hero8 add Lapu-Lapu":
            jahero8 = "Lapu-Lapu"
            await message.channel.send("Jack's hero #8 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero8 add Leomord":
            jahero8 = "Leomord"
            await message.channel.send("Jack's hero #8 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero8 add Martis":
            jahero8 = "Martis"
            await message.channel.send("Jack's hero #8 is now Martis! :crab: ")
        if message.content == "!ml hero8 add Minsitthar":
            jahero8 = "Minsitthar"
            await message.channel.send("Jack's hero #8 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero8 add Roger":
            jahero8 = "Roger"
            await message.channel.send("Jack's hero #8 is now Roger! :wolf: ")
        if message.content == "!ml hero8 add Ruby":
            jahero8 = "Ruby"
            await message.channel.send("Jack's hero #8 is now Ruby! :heart: ")
        if message.content == "!ml hero8 add Sun":
            jahero8 = "Sun"
            await message.channel.send("Jack's hero #8 is now Sun! :monkey_face: ")
        if message.content == "!ml hero8 add Thamuz":
            jahero8 = "Thamuz"
            await message.channel.send("Jack's hero #8 is now Thamuz! :rage: ")
        if message.content == "!ml hero8 add Terizla":
            jahero8 = "Terizla"
            await message.channel.send("Jack's hero #8 is now Terizla! :hammer: ")
        if message.content == "!ml hero8 add Zilong":
            jahero8 = "Zilong"
            await message.channel.send("Jack's hero #8 is now Zilong! :dragon: ")
        if message.content == "!ml hero8 add Fanny":
            jahero8 = "Fanny"
            await message.channel.send("Jack's hero #8 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero8 add Gusion":
            jahero8 = "Gusion"
            await message.channel.send(
                "Jack's hero #8 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero8 add Hanzo":
            jahero8 = "Hanzo"
            await message.channel.send("Jack's hero #8 is now Hanzo! :ghost: ")
        if message.content == "!ml hero8 add Hayabusa":
            jahero8 = "Hayabusa"
            await message.channel.send("Jack's hero #8 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero8 add Helcurt":
            jahero8 = "Helcurt"
            await message.channel.send("Jack's hero #8 is now Helcurt! :mute:  ")
        if message.content == "!ml hero8 add Karina":
            jahero8 = "Karina"
            await message.channel.send("Jack's hero #8 is now Karina! :purple_heart: ")
        if message.content == "!ml hero8 add Lancelot":
            jahero8 = "Lancelot"
            await message.channel.send("Jack's hero #8 is now Lancelot! :fencer: ")
        if message.content == "!ml hero8 add Lesley":
            jahero8 = "Lesley"
            await message.channel.send("Jack's hero #8 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero8 add Natalia":
            jahero8 = "Natalia"
            await message.channel.send("Jack's hero #8 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero8 add Saber":
            jahero8 = "Saber"
            await message.channel.send("Jack's hero #8 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero8 add Selena":
            jahero8 = "Selena"
            await message.channel.send("Jack's hero #8 is now Selena! :sleeping:  ")
        if message.content == "!ml hero8 add Alice":
            jahero8 = "Alice"
            await message.channel.send("Jack's hero #8 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero8 add Aurora":
            jahero8 = "Aurora"
            await message.channel.send("Jack's hero #8 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jahero8 = "Chang'e"
            await message.channel.send("Jack's hero #8 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero8 add Cyclops":
            jahero8 = "Cyclops"
            await message.channel.send("Jack's hero #8 is now Cyclops! :eye:  ")
        if message.content == "!ml hero8 add Eudora":
            jahero8 = "Eudora"
            await message.channel.send("Jack's hero #8 is now Eudora! :zap: ")
        if message.content == "!ml hero8 add Faramis":
            jahero8 = "Faramis"
            await message.channel.send("Jack's hero #8 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero8 add Gord":
            jahero8 = "Gord"
            await message.channel.send("Jack's hero #8 is now Gord! :snowboarder:")
        if message.content == "!ml hero8 add Harith":
            jahero8 = "Harith"
            await message.channel.send("Jack's hero #8 is now Harith! :older_man: ")
        if message.content == "!ml hero8 add Harley":
            jahero8 = "Harley"
            await message.channel.send("Jack's hero #8 is now Harley! :tophat: ")
        if message.content == "!ml hero8 add Kadita":
            jahero8 = "Kadita"
            await message.channel.send("Jack's hero #8 is now Kadita! :droplet: ")
        if message.content == "!ml hero8 add Kagura":
            jahero8 = "Kagura"
            await message.channel.send("Jack's hero #8 is now Kagura! :umbrella8:  ")
        if message.content == "!ml hero8 add Lunox":
            jahero8 = "Lunox"
            await message.channel.send("Jack's hero #8 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero8 add Lylia":
            jahero8 = "Lylia"
            await message.channel.send("Jack's hero #8 is now Lylia! :boom: ")
        if message.content == "!ml hero8 add Nana":
            jahero8 = "Nana"
            await message.channel.send("Jack's hero #8 is now Nana! :cat:  ")
        if message.content == "!ml hero8 add Odette":
            jahero8 = "Odette"
            await message.channel.send("Jack's hero #8 is now Odette! :duck: ")
        if message.content == "!ml hero8 add Pharsa":
            jahero8 = "Pharsa"
            await message.channel.send("Jack's hero #8 is now Pharsa! :dove:  ")
        if message.content == "!ml hero8 add Vale":
            jahero8 = "Vale"
            await message.channel.send("Jack's hero #8 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero8 add Valir":
            jahero8 = "Valir"
            await message.channel.send("Jack's hero #8 is now Valir! :fire:")
        if message.content == "!ml hero8 add Vexanna":
            jahero8 = "Vexanna"
            await message.channel.send("Jack's hero #8 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero8 add Bruno":
            jahero8 = "Bruno"
            await message.channel.send("Jack's hero #8 is now Bruno! :soccer:  ")
        if message.content == "!ml hero8 add Claude":
            jahero8 = "Claude"
            await message.channel.send("Jack's hero #8 is now Claude! :monkey:  ")
        if message.content == "!ml hero8 add Clint":
            jahero8 = "Clint"
            await message.channel.send("Jack's hero #8 is now Clint! :cowboy: ")
        if message.content == "!ml hero8 add Granger":
            jahero8 = "Granger"
            await message.channel.send("Jack's hero #8 is now Granger! :violin: ")
        if message.content == "!ml hero8 add Hanabi":
            jahero8 = "Hanabi"
            await message.channel.send("Jack's hero #8 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero8 add Irithel":
            jahero8 = "Irithel"
            await message.channel.send("Jack's hero #8 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero8 add Karrie":
            jahero8 = "Karrie"
            await message.channel.send(
                "Jack's hero #8 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero8 add Kimmy":
            jahero8 = "Kimmy"
            await message.channel.send("Jack's hero #8 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero8 add Layla":
            jahero8 = "Layla"
            await message.channel.send("Jack's hero #8 is now Layla! :haircut:  ")
        if message.content == "!ml hero8 add Miya":
            jahero8 = "Miya"
            await message.channel.send("Jack's hero #8 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero8 add Moskov":
            jahero8 = "Moskov"
            await message.channel.send("Jack's hero #8 is now Moskov! :imp: ")
        if message.content == "!ml hero8 add Yi Sun-Shin":
            jahero8 = "Yi Sun-Shin"
            await message.channel.send("Jack's hero #8 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero8 add Angela":
            jahero8 = "Angela"
            await message.channel.send("Jack's hero #8 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero8 add Diggie":
            jahero8 = "Diggie"
            await message.channel.send("Jack's hero #8 is now Diggie! :owl: ")
        if message.content == "!ml hero8 add Estes":
            jahero8 = "Estes"
            await message.channel.send("Jack's hero #8 is now Estes! :ear:  ")
        if message.content == "!ml hero8 add Rafaela":
            jahero8 = "Rafaela"
            await message.channel.send("Jack's hero #8 is now Rafaela! :angel: ")
        if message.content == "!ml hero8 add Rynn":
            jahero8 = "Rynn"
            await message.channel.send("Jack's hero #8 is now Rynn! ")
        if message.content == "!ml hero9 add Akai":
            global jahero9
            jahero9 = "Akai"
            await message.channel.send("Jack's hero #9 is now Akai! :panda_face: ")
        if message.content == "!ml hero9 add Balmond":
            jahero9 = "Balmond"
            await message.channel.send("Jack's hero #9 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero9 add Belerick":
            jahero9 = "Belerick"
            await message.channel.send("Jack's hero #9 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero9 add Franco":
            jahero9 = "Franco"
            await message.channel.send("Jack's hero #9 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero9 add Esmerelda":
            jahero9 = "Esmerelda"
            await message.channel.send("Jack's hero #9 is now Esmerelda! :shield: ")
        if message.content == "!ml hero9 add Gatotkaca":
            jahero9 = "Gatotkaca"
            await message.channel.send("Jack's hero #9 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero9 add Grock":
            jahero9 = "Grock"
            await message.channel.send("Jack's hero #9 is now Grock! :european_castle: ")
        if message.content == "!ml hero9 add Hilda":
            jahero9 = "Hilda"
            await message.channel.send("Jack's hero #9 is now Hilda! :runner: ")
        if message.content == "!ml hero9 add Hylos":
            jahero9 = "Hylos"
            await message.channel.send("Jack's hero #9 is now Hylos! :unicorn: ")
        if message.content == "!ml hero9 add Johnson":
            jahero9 = "Johnson"
            await message.channel.send("Jack's hero #9 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero9 add Khufra":
            jahero9 = "Khufra"
            await message.channel.send("Jack's hero #9 is now Khufra! :clown: ")
        if message.content == "!ml hero9 add Lolita":
            jahero9 = "Lolita"
            await message.channel.send("Jack's hero #9 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jahero9 = "Masha"
            await message.channel.send("Jack's hero #9 is now Masha! :bear: ")
        if message.content == "!ml hero9 add Minotaur":
            jahero9 = "Minotaur"
            await message.channel.send("Jack's hero #9 is now Minotaur! :cow: ")
        if message.content == "!ml hero9 add Tigreal":
            jahero9 = "Tigreal"
            await message.channel.send("Jack's hero #9 is now Tigreal! :moyai: ")
        if message.content == "!ml hero9 add Uranus":
            jahero9 = "Uranus"
            await message.channel.send("Jack's hero #9 is now Uranus! :peach: ")
        if message.content == "!ml hero9 add X.Borg":
            jahero9 = "X.Borg"
            await message.channel.send("Jack's hero #9 is now X.Borg! :fire: ")
        if message.content == "!ml hero9 add Aldous":
            jahero9 = "Aldous"
            await message.channel.send("Jack's hero #9 is now Aldous! :fist: ")
        if message.content == "!ml hero9 add Alpha":
            jahero9 = "Alpha"
            await message.channel.send("Jack's hero #9 is now Alpha! :airplane: ")
        if message.content == "!ml hero9 add Alucard":
            jahero9 = "Alucard"
            await message.channel.send("Jack's hero #9 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero9 add Argus":
            jahero9 = "Argus"
            await message.channel.send("Jack's hero #9 is now Argus! :angel: ")
        if message.content == "!ml hero9 add Badang":
            jahero9 = "Badang"
            await message.channel.send("Jack's hero #9 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero9 add Bane":
            jahero9 = "Bane"
            await message.channel.send("Jack's hero #9 is now Bane! :octopus: ")
        if message.content == "!ml hero9 add Chou":
            jahero9 = "Chou"
            await message.channel.send("Jack's hero #9 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero9 add Dyrroth":
            jahero9 = "Dyrroth"
            await message.channel.send("Jack's hero #9 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero9 add Freya":
            jahero9 = "Freya"
            await message.channel.send("Jack's hero #9 is now Freya! :hammer: ")
        if message.content == "!ml hero9 add Guinevere":
            jahero9 = "Guinevere"
            await message.channel.send("Jack's hero #9 is now Guinevere! :dress:  ")
        if message.content == "!ml hero9 add Jawhead":
            jahero9 = "Jawhead"
            await message.channel.send("Jack's hero #9 is now Jawhead! :robot: ")
        if message.content == "!ml hero9 add Kaja":
            jahero9 = "Kaja"
            await message.channel.send("Jack's hero #9 is now Kaja! :bird: ")
        if message.content == "!ml hero9 add Lapu-Lapu":
            jahero9 = "Lapu-Lapu"
            await message.channel.send("Jack's hero #9 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero9 add Leomord":
            jahero9 = "Leomord"
            await message.channel.send("Jack's hero #9 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero9 add Martis":
            jahero9 = "Martis"
            await message.channel.send("Jack's hero #9 is now Martis! :crab: ")
        if message.content == "!ml hero9 add Minsitthar":
            jahero9 = "Minsitthar"
            await message.channel.send("Jack's hero #9 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero9 add Roger":
            jahero9 = "Roger"
            await message.channel.send("Jack's hero #9 is now Roger! :wolf: ")
        if message.content == "!ml hero9 add Ruby":
            jahero9 = "Ruby"
            await message.channel.send("Jack's hero #9 is now Ruby! :heart: ")
        if message.content == "!ml hero9 add Sun":
            jahero9 = "Sun"
            await message.channel.send("Jack's hero #9 is now Sun! :monkey_face: ")
        if message.content == "!ml hero9 add Thamuz":
            jahero9 = "Thamuz"
            await message.channel.send("Jack's hero #9 is now Thamuz! :rage: ")
        if message.content == "!ml hero9 add Terizla":
            jahero9 = "Terizla"
            await message.channel.send("Jack's hero #9 is now Terizla! :hammer: ")
        if message.content == "!ml hero9 add Zilong":
            jahero9 = "Zilong"
            await message.channel.send("Jack's hero #9 is now Zilong! :dragon: ")
        if message.content == "!ml hero9 add Fanny":
            jahero9 = "Fanny"
            await message.channel.send("Jack's hero #9 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero9 add Gusion":
            jahero9 = "Gusion"
            await message.channel.send(
                "Jack's hero #9 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero9 add Hanzo":
            jahero9 = "Hanzo"
            await message.channel.send("Jack's hero #9 is now Hanzo! :ghost: ")
        if message.content == "!ml hero9 add Hayabusa":
            jahero9 = "Hayabusa"
            await message.channel.send("Jack's hero #9 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero9 add Helcurt":
            jahero9 = "Helcurt"
            await message.channel.send("Jack's hero #9 is now Helcurt! :mute:  ")
        if message.content == "!ml hero9 add Karina":
            jahero9 = "Karina"
            await message.channel.send("Jack's hero #9 is now Karina! :purple_heart: ")
        if message.content == "!ml hero9 add Lancelot":
            jahero9 = "Lancelot"
            await message.channel.send("Jack's hero #9 is now Lancelot! :fencer: ")
        if message.content == "!ml hero9 add Lesley":
            jahero9 = "Lesley"
            await message.channel.send("Jack's hero #9 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero9 add Natalia":
            jahero9 = "Natalia"
            await message.channel.send("Jack's hero #9 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero9 add Saber":
            jahero9 = "Saber"
            await message.channel.send("Jack's hero #9 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero9 add Selena":
            jahero9 = "Selena"
            await message.channel.send("Jack's hero #9 is now Selena! :sleeping:  ")
        if message.content == "!ml hero9 add Alice":
            jahero9 = "Alice"
            await message.channel.send("Jack's hero #9 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero9 add Aurora":
            jahero9 = "Aurora"
            await message.channel.send("Jack's hero #9 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jahero9 = "Chang'e"
            await message.channel.send("Jack's hero #9 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero9 add Cyclops":
            jahero9 = "Cyclops"
            await message.channel.send("Jack's hero #9 is now Cyclops! :eye:  ")
        if message.content == "!ml hero9 add Eudora":
            jahero9 = "Eudora"
            await message.channel.send("Jack's hero #9 is now Eudora! :zap: ")
        if message.content == "!ml hero9 add Faramis":
            jahero9 = "Faramis"
            await message.channel.send("Jack's hero #9 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero9 add Gord":
            jahero9 = "Gord"
            await message.channel.send("Jack's hero #9 is now Gord! :snowboarder:")
        if message.content == "!ml hero9 add Harith":
            jahero9 = "Harith"
            await message.channel.send("Jack's hero #9 is now Harith! :older_man: ")
        if message.content == "!ml hero9 add Harley":
            jahero9 = "Harley"
            await message.channel.send("Jack's hero #9 is now Harley! :tophat: ")
        if message.content == "!ml hero9 add Kadita":
            jahero9 = "Kadita"
            await message.channel.send("Jack's hero #9 is now Kadita! :droplet: ")
        if message.content == "!ml hero9 add Kagura":
            jahero9 = "Kagura"
            await message.channel.send("Jack's hero #9 is now Kagura! :umbrella9:  ")
        if message.content == "!ml hero9 add Lunox":
            jahero9 = "Lunox"
            await message.channel.send("Jack's hero #9 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero9 add Lylia":
            jahero9 = "Lylia"
            await message.channel.send("Jack's hero #9 is now Lylia! :boom: ")
        if message.content == "!ml hero9 add Nana":
            jahero9 = "Nana"
            await message.channel.send("Jack's hero #9 is now Nana! :cat:  ")
        if message.content == "!ml hero9 add Odette":
            jahero9 = "Odette"
            await message.channel.send("Jack's hero #9 is now Odette! :duck: ")
        if message.content == "!ml hero9 add Pharsa":
            jahero9 = "Pharsa"
            await message.channel.send("Jack's hero #9 is now Pharsa! :dove:  ")
        if message.content == "!ml hero9 add Vale":
            jahero9 = "Vale"
            await message.channel.send("Jack's hero #9 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero9 add Valir":
            jahero9 = "Valir"
            await message.channel.send("Jack's hero #9 is now Valir! :fire:")
        if message.content == "!ml hero9 add Vexanna":
            jahero9 = "Vexanna"
            await message.channel.send("Jack's hero #9 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero9 add Bruno":
            jahero9 = "Bruno"
            await message.channel.send("Jack's hero #9 is now Bruno! :soccer:  ")
        if message.content == "!ml hero9 add Claude":
            jahero9 = "Claude"
            await message.channel.send("Jack's hero #9 is now Claude! :monkey:  ")
        if message.content == "!ml hero9 add Clint":
            jahero9 = "Clint"
            await message.channel.send("Jack's hero #9 is now Clint! :cowboy: ")
        if message.content == "!ml hero9 add Granger":
            jahero9 = "Granger"
            await message.channel.send("Jack's hero #9 is now Granger! :violin: ")
        if message.content == "!ml hero9 add Hanabi":
            jahero9 = "Hanabi"
            await message.channel.send("Jack's hero #9 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero9 add Irithel":
            jahero9 = "Irithel"
            await message.channel.send("Jack's hero #9 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero9 add Karrie":
            jahero9 = "Karrie"
            await message.channel.send(
                "Jack's hero #9 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero9 add Kimmy":
            jahero9 = "Kimmy"
            await message.channel.send("Jack's hero #9 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero9 add Layla":
            jahero9 = "Layla"
            await message.channel.send("Jack's hero #9 is now Layla! :haircut:  ")
        if message.content == "!ml hero9 add Miya":
            jahero9 = "Miya"
            await message.channel.send("Jack's hero #9 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero9 add Moskov":
            jahero9 = "Moskov"
            await message.channel.send("Jack's hero #9 is now Moskov! :imp: ")
        if message.content == "!ml hero9 add Yi Sun-Shin":
            jahero9 = "Yi Sun-Shin"
            await message.channel.send("Jack's hero #9 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero9 add Angela":
            jahero9 = "Angela"
            await message.channel.send("Jack's hero #9 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero9 add Diggie":
            jahero9 = "Diggie"
            await message.channel.send("Jack's hero #9 is now Diggie! :owl: ")
        if message.content == "!ml hero9 add Estes":
            jahero9 = "Estes"
            await message.channel.send("Jack's hero #9 is now Estes! :ear:  ")
        if message.content == "!ml hero9 add Rafaela":
            jahero9 = "Rafaela"
            await message.channel.send("Jack's hero #9 is now Rafaela! :angel: ")
        if message.content == "!ml hero9 add Rynn":
            jahero9 = "Rynn"
            await message.channel.send("Jack's hero #9 is now Rynn! ")
        if message.content == "!ml hero10 add Akai":
            global jahero10
            jahero10 = "Akai"
            await message.channel.send("Jack's hero #10 is now Akai! :panda_face: ")
        if message.content == "!ml hero10 add Balmond":
            jahero10 = "Balmond"
            await message.channel.send("Jack's hero #10 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero10 add Belerick":
            jahero10 = "Belerick"
            await message.channel.send("Jack's hero #10 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero10 add Franco":
            jahero10 = "Franco"
            await message.channel.send("Jack's hero #10 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero10 add Esmerelda":
            jahero10 = "Esmerelda"
            await message.channel.send("Jack's hero #10 is now Esmerelda! :shield: ")
        if message.content == "!ml hero10 add Gatotkaca":
            jahero10 = "Gatotkaca"
            await message.channel.send("Jack's hero #10 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero10 add Grock":
            jahero10 = "Grock"
            await message.channel.send("Jack's hero #10 is now Grock! :european_castle: ")
        if message.content == "!ml hero10 add Hilda":
            jahero10 = "Hilda"
            await message.channel.send("Jack's hero #10 is now Hilda! :runner: ")
        if message.content == "!ml hero10 add Hylos":
            jahero10 = "Hylos"
            await message.channel.send("Jack's hero #10 is now Hylos! :unicorn: ")
        if message.content == "!ml hero10 add Johnson":
            jahero10 = "Johnson"
            await message.channel.send("Jack's hero #10 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero10 add Khufra":
            jahero10 = "Khufra"
            await message.channel.send("Jack's hero #10 is now Khufra! :clown: ")
        if message.content == "!ml hero10 add Lolita":
            jahero10 = "Lolita"
            await message.channel.send("Jack's hero #10 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jahero10 = "Masha"
            await message.channel.send("Jack's hero #10 is now Masha! :bear: ")
        if message.content == "!ml hero10 add Minotaur":
            jahero10 = "Minotaur"
            await message.channel.send("Jack's hero #10 is now Minotaur! :cow: ")
        if message.content == "!ml hero10 add Tigreal":
            jahero10 = "Tigreal"
            await message.channel.send("Jack's hero #10 is now Tigreal! :moyai: ")
        if message.content == "!ml hero10 add Uranus":
            jahero10 = "Uranus"
            await message.channel.send("Jack's hero #10 is now Uranus! :peach: ")
        if message.content == "!ml hero10 add X.Borg":
            jahero10 = "X.Borg"
            await message.channel.send("Jack's hero #10 is now X.Borg! :fire: ")
        if message.content == "!ml hero10 add Aldous":
            jahero10 = "Aldous"
            await message.channel.send("Jack's hero #10 is now Aldous! :fist: ")
        if message.content == "!ml hero10 add Alpha":
            jahero10 = "Alpha"
            await message.channel.send("Jack's hero #10 is now Alpha! :airplane: ")
        if message.content == "!ml hero10 add Alucard":
            jahero10 = "Alucard"
            await message.channel.send("Jack's hero #10 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero10 add Argus":
            jahero10 = "Argus"
            await message.channel.send("Jack's hero #10 is now Argus! :angel: ")
        if message.content == "!ml hero10 add Badang":
            jahero10 = "Badang"
            await message.channel.send("Jack's hero #10 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero10 add Bane":
            jahero10 = "Bane"
            await message.channel.send("Jack's hero #10 is now Bane! :octopus: ")
        if message.content == "!ml hero10 add Chou":
            jahero10 = "Chou"
            await message.channel.send("Jack's hero #10 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero10 add Dyrroth":
            jahero10 = "Dyrroth"
            await message.channel.send("Jack's hero #10 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero10 add Freya":
            jahero10 = "Freya"
            await message.channel.send("Jack's hero #10 is now Freya! :hammer: ")
        if message.content == "!ml hero10 add Guinevere":
            jahero10 = "Guinevere"
            await message.channel.send("Jack's hero #10 is now Guinevere! :dress:  ")
        if message.content == "!ml hero10 add Jawhead":
            jahero10 = "Jawhead"
            await message.channel.send("Jack's hero #10 is now Jawhead! :robot: ")
        if message.content == "!ml hero10 add Kaja":
            jahero10 = "Kaja"
            await message.channel.send("Jack's hero #10 is now Kaja! :bird: ")
        if message.content == "!ml hero10 add Lapu-Lapu":
            jahero10 = "Lapu-Lapu"
            await message.channel.send("Jack's hero #10 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero10 add Leomord":
            jahero10 = "Leomord"
            await message.channel.send("Jack's hero #10 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero10 add Martis":
            jahero10 = "Martis"
            await message.channel.send("Jack's hero #10 is now Martis! :crab: ")
        if message.content == "!ml hero10 add Minsitthar":
            jahero10 = "Minsitthar"
            await message.channel.send("Jack's hero #10 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero10 add Roger":
            jahero10 = "Roger"
            await message.channel.send("Jack's hero #10 is now Roger! :wolf: ")
        if message.content == "!ml hero10 add Ruby":
            jahero10 = "Ruby"
            await message.channel.send("Jack's hero #10 is now Ruby! :heart: ")
        if message.content == "!ml hero10 add Sun":
            jahero10 = "Sun"
            await message.channel.send("Jack's hero #10 is now Sun! :monkey_face: ")
        if message.content == "!ml hero10 add Thamuz":
            jahero10 = "Thamuz"
            await message.channel.send("Jack's hero #10 is now Thamuz! :rage: ")
        if message.content == "!ml hero10 add Terizla":
            jahero10 = "Terizla"
            await message.channel.send("Jack's hero #10 is now Terizla! :hammer: ")
        if message.content == "!ml hero10 add Zilong":
            jahero10 = "Zilong"
            await message.channel.send("Jack's hero #10 is now Zilong! :dragon: ")
        if message.content == "!ml hero10 add Fanny":
            jahero10 = "Fanny"
            await message.channel.send("Jack's hero #10 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero10 add Gusion":
            jahero10 = "Gusion"
            await message.channel.send(
                "Jack's hero #10 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero10 add Hanzo":
            jahero10 = "Hanzo"
            await message.channel.send("Jack's hero #10 is now Hanzo! :ghost: ")
        if message.content == "!ml hero10 add Hayabusa":
            jahero10 = "Hayabusa"
            await message.channel.send("Jack's hero #10 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero10 add Helcurt":
            jahero10 = "Helcurt"
            await message.channel.send("Jack's hero #10 is now Helcurt! :mute:  ")
        if message.content == "!ml hero10 add Karina":
            jahero10 = "Karina"
            await message.channel.send("Jack's hero #10 is now Karina! :purple_heart: ")
        if message.content == "!ml hero10 add Lancelot":
            jahero10 = "Lancelot"
            await message.channel.send("Jack's hero #10 is now Lancelot! :fencer: ")
        if message.content == "!ml hero10 add Lesley":
            jahero10 = "Lesley"
            await message.channel.send("Jack's hero #10 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero10 add Natalia":
            jahero10 = "Natalia"
            await message.channel.send("Jack's hero #10 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero10 add Saber":
            jahero10 = "Saber"
            await message.channel.send("Jack's hero #10 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero10 add Selena":
            jahero10 = "Selena"
            await message.channel.send("Jack's hero #10 is now Selena! :sleeping:  ")
        if message.content == "!ml hero10 add Alice":
            jahero10 = "Alice"
            await message.channel.send("Jack's hero #10 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero10 add Aurora":
            jahero10 = "Aurora"
            await message.channel.send("Jack's hero #10 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jahero10 = "Chang'e"
            await message.channel.send("Jack's hero #10 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero10 add Cyclops":
            jahero10 = "Cyclops"
            await message.channel.send("Jack's hero #10 is now Cyclops! :eye:  ")
        if message.content == "!ml hero10 add Eudora":
            jahero10 = "Eudora"
            await message.channel.send("Jack's hero #10 is now Eudora! :zap: ")
        if message.content == "!ml hero10 add Faramis":
            jahero10 = "Faramis"
            await message.channel.send("Jack's hero #10 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero10 add Gord":
            jahero10 = "Gord"
            await message.channel.send("Jack's hero #10 is now Gord! :snowboarder:")
        if message.content == "!ml hero10 add Harith":
            jahero10 = "Harith"
            await message.channel.send("Jack's hero #10 is now Harith! :older_man: ")
        if message.content == "!ml hero10 add Harley":
            jahero10 = "Harley"
            await message.channel.send("Jack's hero #10 is now Harley! :tophat: ")
        if message.content == "!ml hero10 add Kadita":
            jahero10 = "Kadita"
            await message.channel.send("Jack's hero #10 is now Kadita! :droplet: ")
        if message.content == "!ml hero10 add Kagura":
            jahero10 = "Kagura"
            await message.channel.send("Jack's hero #10 is now Kagura! :umbrella10:  ")
        if message.content == "!ml hero10 add Lunox":
            jahero10 = "Lunox"
            await message.channel.send("Jack's hero #10 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero10 add Lylia":
            jahero10 = "Lylia"
            await message.channel.send("Jack's hero #10 is now Lylia! :boom: ")
        if message.content == "!ml hero10 add Nana":
            jahero10 = "Nana"
            await message.channel.send("Jack's hero #10 is now Nana! :cat:  ")
        if message.content == "!ml hero10 add Odette":
            jahero10 = "Odette"
            await message.channel.send("Jack's hero #10 is now Odette! :duck: ")
        if message.content == "!ml hero10 add Pharsa":
            jahero10 = "Pharsa"
            await message.channel.send("Jack's hero #10 is now Pharsa! :dove:  ")
        if message.content == "!ml hero10 add Vale":
            jahero10 = "Vale"
            await message.channel.send("Jack's hero #10 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero10 add Valir":
            jahero10 = "Valir"
            await message.channel.send("Jack's hero #10 is now Valir! :fire:")
        if message.content == "!ml hero10 add Vexanna":
            jahero10 = "Vexanna"
            await message.channel.send("Jack's hero #10 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero10 add Bruno":
            jahero10 = "Bruno"
            await message.channel.send("Jack's hero #10 is now Bruno! :soccer:  ")
        if message.content == "!ml hero10 add Claude":
            jahero10 = "Claude"
            await message.channel.send("Jack's hero #10 is now Claude! :monkey:  ")
        if message.content == "!ml hero10 add Clint":
            jahero10 = "Clint"
            await message.channel.send("Jack's hero #10 is now Clint! :cowboy: ")
        if message.content == "!ml hero10 add Granger":
            jahero10 = "Granger"
            await message.channel.send("Jack's hero #10 is now Granger! :violin: ")
        if message.content == "!ml hero10 add Hanabi":
            jahero10 = "Hanabi"
            await message.channel.send("Jack's hero #10 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero10 add Irithel":
            jahero10 = "Irithel"
            await message.channel.send("Jack's hero #10 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero10 add Karrie":
            jahero10 = "Karrie"
            await message.channel.send(
                "Jack's hero #10 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero10 add Kimmy":
            jahero10 = "Kimmy"
            await message.channel.send("Jack's hero #10 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero10 add Layla":
            jahero10 = "Layla"
            await message.channel.send("Jack's hero #10 is now Layla! :haircut:  ")
        if message.content == "!ml hero10 add Miya":
            jahero10 = "Miya"
            await message.channel.send("Jack's hero #10 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero10 add Moskov":
            jahero10 = "Moskov"
            await message.channel.send("Jack's hero #10 is now Moskov! :imp: ")
        if message.content == "!ml hero10 add Yi Sun-Shin":
            jahero10 = "Yi Sun-Shin"
            await message.channel.send("Jack's hero #10 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero10 add Angela":
            jahero10 = "Angela"
            await message.channel.send("Jack's hero #10 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero10 add Diggie":
            jahero10 = "Diggie"
            await message.channel.send("Jack's hero #10 is now Diggie! :owl: ")
        if message.content == "!ml hero10 add Estes":
            jahero10 = "Estes"
            await message.channel.send("Jack's hero #10 is now Estes! :ear:  ")
        if message.content == "!ml hero10 add Rafaela":
            jahero10 = "Rafaela"
            await message.channel.send("Jack's hero #10 is now Rafaela! :angel: ")
        if message.content == "!ml hero10 add Rynn":
            jahero10 = "Rynn"
            await message.channel.send("Jack's hero #10 is now Rynn! ")
        if message.content == "!ml hero1 clear":
            jahero1 = "Not Chosen"
            await message.channel.send("Jack's hero #1 slot has been cleared!")
        if message.content == "!ml hero2 clear":
            jahero2 = "Not Chosen"
            await message.channel.send("Jack's hero #2 slot has been cleared!")
        if message.content == "!ml hero3 clear":
            jahero3 = "Not Chosen"
            await message.channel.send("Jack's hero #3 slot has been cleared!")
        if message.content == "!ml hero3 clear":
            jahero3 = "Not Chosen"
            await message.channel.send("Jack's hero #3 slot has been cleared!")
        if message.content == "!ml hero4 clear":
            jahero4 = "Not Chosen"
            await message.channel.send("Jack's hero #4 slot has been cleared!")
        if message.content == "!ml hero5 clear":
            jahero5 = "Not Chosen"
            await message.channel.send("Jack's hero #5 slot has been cleared!")
        if message.content == "!ml hero6 clear":
            jahero6 = "Not Chosen"
            await message.channel.send("Jack's hero #6 slot has been cleared!")
        if message.content == "!ml hero7 clear":
            jahero7 = "Not Chosen"
            await message.channel.send("Jack's hero #7 slot has been cleared!")
        if message.content == "!ml hero8 clear":
            jahero8 = "Not Chosen"
            await message.channel.send("Jack's hero #8 slot has been cleared!")
        if message.content == "!ml hero9 clear":
            jahero9 = "Not Chosen"
            await message.channel.send("Jack's hero #9 slot has been cleared!")
        if message.content == "!ml hero10 clear":
            jahero10 = "Not Chosen"
            await message.channel.send("Jack's hero #10 slot has been cleared!")
        if message.content == "!ml hlist Jack":
            jaembed = discord.Embed(title="Heroes Jack Plays",
                                    description="Here are the top 10 heroes Jack is willing to play in ranked")
            jaembed.add_field(name="1", value=jahero1)
            jaembed.add_field(name="2", value=jahero2)
            jaembed.add_field(name="3", value=jahero3)
            jaembed.add_field(name="4", value=jahero4)
            jaembed.add_field(name="5", value=jahero5)
            jaembed.add_field(name="6", value=jahero6)
            jaembed.add_field(name="7", value=jahero7)
            jaembed.add_field(name="8", value=jahero8)
            jaembed.add_field(name="9", value=jahero9)
            jaembed.add_field(name="10", value=jahero10)
            await message.channel.send(content=None, embed=jaembed)
    if str(message.channel) not in clean_channels and str(message.author) in Jeremy_Hlist:
        if message.content.find("hello") != -1:
            await message.channel.send("Hey Jeremy, how are you?")
        if message.content.find("!gay") != -1:
            await message.channel.send("What a nay gigga")
        if message.content.find("!nigga") != -1:
            await message.channel.send(":monkey:")
        if message.content.find("nigga") != -1:
            global nwmonkeychance
            global nwmonkeybonus
            global nwmonkeytotal
            nwmonkeychance = random.randrange(0,20,1)
            nwmonkeytotal = nwmonkeychance+nwmonkeybonus
            if nwmonkeytotal > 15:
                await message.channel.send(":monkey:")
                nwmonkeytotal = 0
                nwmonkeychance = 0
                nwmonkeybonus = 0
            else:
                nwmonkeybonus += 1
                nwmonkeytotal = 0
                nwmonkeychance = 0
            nwordcount
            nwordcount += 1
        if message.content.find("Nigga") != -1:
            nwmonkeychance = random.randrange(0,20,1)
            nwmonkeytotal = nwmonkeychance+nwmonkeybonus
            if nwmonkeytotal > 15:
                await message.channel.send("What are you saying my brudha?")
                nwmonkeytotal = 0
                nwmonkeychance = 0
                nwmonkeybonus = 0
            else:
                nwmonkeybonus += 1
                nwmonkeytotal = 0
                nwmonkeychance = 0
            nwordcount
            nwordcount += 1
        if message.content.find("NIGGA") != -1:
            nwmonkeychance = random.randrange(0,20,1)
            nwmonkeytotal = nwmonkeychance+nwmonkeybonus
            if nwmonkeytotal > 15:
                await message.channel.send(":monkey::monkey::monkey:")
                nwmonkeytotal = 0
                nwmonkeychance = 0
                nwmonkeybonus = 0
            else:
                nwmonkeybonus += 1
                nwmonkeytotal = 0
                nwmonkeychance = 0
            nwordcount
            nwordcount += 2
        if message.content.find("nigger") != -1:
            nwmonkeychance = random.randrange(0,20,1)
            nwmonkeytotal = nwmonkeychance+nwmonkeybonus
            if nwmonkeytotal > 15:
                await message.channel.send("wakanda vir ewig!")
                nwmonkeytotal = 0
                nwmonkeychance = 0
                nwmonkeybonus = 0
            else:
                nwmonkeybonus += 2
                nwmonkeytotal = 0
                nwmonkeychance = 0
            nwordcount
            nwordcount += 2
        if message.content.find("Nigger") != -1:
            nwmonkeychance = random.randrange(0,20,1)
            nwmonkeytotal = nwmonkeychance+nwmonkeybonus
            if nwmonkeytotal > 15:
                await message.channel.send("Are bụ ebe gbara ọchịchịrị na usoro ọmụmụ gị")
                nwmonkeytotal = 0
                nwmonkeychance = 0
                nwmonkeybonus = 0
            else:
                nwmonkeybonus += 2
                nwmonkeytotal = 0
                nwmonkeychance = 0
            nwordcount
            nwordcount += 2
        if message.content.find("NIGGER") != -1:
            nwmonkeychance = random.randrange(0,20,1)
            nwmonkeytotal = nwmonkeychance+nwmonkeybonus
            if nwmonkeytotal > 15:
                await message.channel.send("Niggle me this, What accounts for...")
                nwmonkeytotal = 0
                nwmonkeychance = 0
                nwmonkeybonus = 0
            else:
                nwmonkeybonus += 2
                nwmonkeytotal = 0
                nwmonkeychance = 0
            nwordcount
            nwordcount += 3
        if message.content == "!ml hero1 add Akai":
            global jehero1
            jehero1 = "Akai"
            await message.channel.send("Jeremy's hero #1 is now Akai! :panda_face: ")
        if message.content == "!ml hero1 add Balmond":
            jehero1 = "Balmond"
            await message.channel.send("Jeremy's hero #1 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero1 add Belerick":
            jehero1 = "Belerick"
            await message.channel.send("Jeremy's hero #1 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero1 add Franco":
            jehero1 = "Franco"
            await message.channel.send("Jeremy's hero #1 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero1 add Esmerelda":
            jehero1 = "Esmerelda"
            await message.channel.send("Jeremy's hero #1 is now Esmerelda! :shield: ")
        if message.content == "!ml hero1 add Gatotkaca":
            jehero1 = "Gatotkaca"
            await message.channel.send("Jeremy's hero #1 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero1 add Grock":
            jehero1 = "Grock"
            await message.channel.send("Jeremy's hero #1 is now Grock! :european_castle: ")
        if message.content == "!ml hero1 add Hilda":
            jehero1 = "Hilda"
            await message.channel.send("Jeremy's hero #1 is now Hilda! :runner: ")
        if message.content == "!ml hero1 add Hylos":
            jehero1 = "Hylos"
            await message.channel.send("Jeremy's hero #1 is now Hylos! :unicorn: ")
        if message.content == "!ml hero1 add Johnson":
            jehero1 = "Johnson"
            await message.channel.send("Jeremy's hero #1 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero1 add Khufra":
            jehero1 = "Khufra"
            await message.channel.send("Jeremy's hero #1 is now Khufra! :clown: ")
        if message.content == "!ml hero1 add Lolita":
            jehero1 = "Lolita"
            await message.channel.send("Jeremy's hero #1 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jehero1 = "Masha"
            await message.channel.send("Jeremy's hero #1 is now Masha! :bear: ")
        if message.content == "!ml hero1 add Minotaur":
            jehero1 = "Minotaur"
            await message.channel.send("Jeremy's hero #1 is now Minotaur! :cow: ")
        if message.content == "!ml hero1 add Tigreal":
            jehero1 = "Tigreal"
            await message.channel.send("Jeremy's hero #1 is now Tigreal! :moyai: ")
        if message.content == "!ml hero1 add Uranus":
            jehero1 = "Uranus"
            await message.channel.send("Jeremy's hero #1 is now Uranus! :peach: ")
        if message.content == "!ml hero1 add X.Borg":
            jehero1 = "X.Borg"
            await message.channel.send("Jeremy's hero #1 is now X.Borg! :fire: ")
        if message.content == "!ml hero1 add Aldous":
            jehero1 = "Aldous"
            await message.channel.send("Jeremy's hero #1 is now Aldous! :fist: ")
        if message.content == "!ml hero1 add Alpha":
            jehero1 = "Alpha"
            await message.channel.send("Jeremy's hero #1 is now Alpha! :airplane: ")
        if message.content == "!ml hero1 add Alucard":
            jehero1 = "Alucard"
            await message.channel.send("Jeremy's hero #1 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero1 add Argus":
            jehero1 = "Argus"
            await message.channel.send("Jeremy's hero #1 is now Argus! :angel: ")
        if message.content == "!ml hero1 add Badang":
            jehero1 = "Badang"
            await message.channel.send("Jeremy's hero #1 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero1 add Bane":
            jehero1 = "Bane"
            await message.channel.send("Jeremy's hero #1 is now Bane! :octopus: ")
        if message.content == "!ml hero1 add Chou":
            jehero1 = "Chou"
            await message.channel.send("Jeremy's hero #1 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero1 add Dyrroth":
            jehero1 = "Dyrroth"
            await message.channel.send("Jeremy's hero #1 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero1 add Freya":
            jehero1 = "Freya"
            await message.channel.send("Jeremy's hero #1 is now Freya! :hammer: ")
        if message.content == "!ml hero1 add Guinevere":
            jehero1 = "Guinevere"
            await message.channel.send("Jeremy's hero #1 is now Guinevere! :dress:  ")
        if message.content == "!ml hero1 add Jawhead":
            jehero1 = "Jawhead"
            await message.channel.send("Jeremy's hero #1 is now Jawhead! :robot: ")
        if message.content == "!ml hero1 add Kaja":
            jehero1 = "Kaja"
            await message.channel.send("Jeremy's hero #1 is now Kaja! :bird: ")
        if message.content == "!ml hero1 add Lapu-Lapu":
            jehero1 = "Lapu-Lapu"
            await message.channel.send("Jeremy's hero #1 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero1 add Leomord":
            jehero1 = "Leomord"
            await message.channel.send("Jeremy's hero #1 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero1 add Martis":
            jehero1 = "Martis"
            await message.channel.send("Jeremy's hero #1 is now Martis! :crab: ")
        if message.content == "!ml hero1 add Minsitthar":
            jehero1 = "Minsitthar"
            await message.channel.send("Jeremy's hero #1 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero1 add Roger":
            jehero1 = "Roger"
            await message.channel.send("Jeremy's hero #1 is now Roger! :wolf: ")
        if message.content == "!ml hero1 add Ruby":
            jehero1 = "Ruby"
            await message.channel.send("Jeremy's hero #1 is now Ruby! :heart: ")
        if message.content == "!ml hero1 add Sun":
            jehero1 = "Sun"
            await message.channel.send("Jeremy's hero #1 is now Sun! :monkey_face: ")
        if message.content == "!ml hero1 add Thamuz":
            jehero1 = "Thamuz"
            await message.channel.send("Jeremy's hero #1 is now Thamuz! :rage: ")
        if message.content == "!ml hero1 add Terizla":
            jehero1 = "Terizla"
            await message.channel.send("Jeremy's hero #1 is now Terizla! :hammer: ")
        if message.content == "!ml hero1 add Zilong":
            jehero1 = "Zilong"
            await message.channel.send("Jeremy's hero #1 is now Zilong! :dragon: ")
        if message.content == "!ml hero1 add Fanny":
            jehero1 = "Fanny"
            await message.channel.send("Jeremy's hero #1 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero1 add Gusion":
            jehero1 = "Gusion"
            await message.channel.send(
                "Jeremy's hero #1 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero1 add Hanzo":
            jehero1 = "Hanzo"
            await message.channel.send("Jeremy's hero #1 is now Hanzo! :ghost: ")
        if message.content == "!ml hero1 add Hayabusa":
            jehero1 = "Hayabusa"
            await message.channel.send("Jeremy's hero #1 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero1 add Helcurt":
            jehero1 = "Helcurt"
            await message.channel.send("Jeremy's hero #1 is now Helcurt! :mute:  ")
        if message.content == "!ml hero1 add Karina":
            jehero1 = "Karina"
            await message.channel.send("Jeremy's hero #1 is now Karina! :purple_heart: ")
        if message.content == "!ml hero1 add Lancelot":
            jehero1 = "Lancelot"
            await message.channel.send("Jeremy's hero #1 is now Lancelot! :fencer: ")
        if message.content == "!ml hero1 add Lesley":
            jehero1 = "Lesley"
            await message.channel.send("Jeremy's hero #1 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero1 add Natalia":
            jehero1 = "Natalia"
            await message.channel.send("Jeremy's hero #1 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero1 add Saber":
            jehero1 = "Saber"
            await message.channel.send("Jeremy's hero #1 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero1 add Selena":
            jehero1 = "Selena"
            await message.channel.send("Jeremy's hero #1 is now Selena! :sleeping:  ")
        if message.content == "!ml hero1 add Alice":
            jehero1 = "Alice"
            await message.channel.send("Jeremy's hero #1 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero1 add Aurora":
            jehero1 = "Aurora"
            await message.channel.send("Jeremy's hero #1 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jehero1 = "Chang'e"
            await message.channel.send("Jeremy's hero #1 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero1 add Cyclops":
            jehero1 = "Cyclops"
            await message.channel.send("Jeremy's hero #1 is now Cyclops! :eye:  ")
        if message.content == "!ml hero1 add Eudora":
            jehero1 = "Eudora"
            await message.channel.send("Jeremy's hero #1 is now Eudora! :zap: ")
        if message.content == "!ml hero1 add Faramis":
            jehero1 = "Faramis"
            await message.channel.send("Jeremy's hero #1 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero1 add Gord":
            jehero1 = "Gord"
            await message.channel.send("Jeremy's hero #1 is now Gord! :snowboarder:")
        if message.content == "!ml hero1 add Harith":
            jehero1 = "Harith"
            await message.channel.send("Jeremy's hero #1 is now Harith! :older_man: ")
        if message.content == "!ml hero1 add Harley":
            jehero1 = "Harley"
            await message.channel.send("Jeremy's hero #1 is now Harley! :tophat: ")
        if message.content == "!ml hero1 add Kadita":
            jehero1 = "Kadita"
            await message.channel.send("Jeremy's hero #1 is now Kadita! :droplet: ")
        if message.content == "!ml hero1 add Kagura":
            jehero1 = "Kagura"
            await message.channel.send("Jeremy's hero #1 is now Kagura! :umbrella2:  ")
        if message.content == "!ml hero1 add Lunox":
            jehero1 = "Lunox"
            await message.channel.send("Jeremy's hero #1 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero1 add Lylia":
            jehero1 = "Lylia"
            await message.channel.send("Jeremy's hero #1 is now Lylia! :boom: ")
        if message.content == "!ml hero1 add Nana":
            jehero1 = "Nana"
            await message.channel.send("Jeremy's hero #1 is now Nana! :cat:  ")
        if message.content == "!ml hero1 add Odette":
            jehero1 = "Odette"
            await message.channel.send("Jeremy's hero #1 is now Odette! :duck: ")
        if message.content == "!ml hero1 add Pharsa":
            jehero1 = "Pharsa"
            await message.channel.send("Jeremy's hero #1 is now Pharsa! :dove:  ")
        if message.content == "!ml hero1 add Vale":
            jehero1 = "Vale"
            await message.channel.send("Jeremy's hero #1 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero1 add Valir":
            jehero1 = "Valir"
            await message.channel.send("Jeremy's hero #1 is now Valir! :fire:")
        if message.content == "!ml hero1 add Vexanna":
            jehero1 = "Vexanna"
            await message.channel.send("Jeremy's hero #1 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero1 add Bruno":
            jehero1 = "Bruno"
            await message.channel.send("Jeremy's hero #1 is now Bruno! :soccer:  ")
        if message.content == "!ml hero1 add Claude":
            jehero1 = "Claude"
            await message.channel.send("Jeremy's hero #1 is now Claude! :monkey:  ")
        if message.content == "!ml hero1 add Clint":
            jehero1 = "Clint"
            await message.channel.send("Jeremy's hero #1 is now Clint! :cowboy: ")
        if message.content == "!ml hero1 add Granger":
            jehero1 = "Granger"
            await message.channel.send("Jeremy's hero #1 is now Granger! :violin: ")
        if message.content == "!ml hero1 add Hanabi":
            jehero1 = "Hanabi"
            await message.channel.send("Jeremy's hero #1 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero1 add Irithel":
            jehero1 = "Irithel"
            await message.channel.send("Jeremy's hero #1 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero1 add Karrie":
            jehero1 = "Karrie"
            await message.channel.send(
                "Jeremy's hero #1 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero1 add Kimmy":
            jehero1 = "Kimmy"
            await message.channel.send("Jeremy's hero #1 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero1 add Layla":
            jehero1 = "Layla"
            await message.channel.send("Jeremy's hero #1 is now Layla! :haircut:  ")
        if message.content == "!ml hero1 add Miya":
            jehero1 = "Miya"
            await message.channel.send("Jeremy's hero #1 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero1 add Moskov":
            jehero1 = "Moskov"
            await message.channel.send("Jeremy's hero #1 is now Moskov! :imp: ")
        if message.content == "!ml hero1 add Yi Sun-Shin":
            jehero1 = "Yi Sun-Shin"
            await message.channel.send("Jeremy's hero #1 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero1 add Angela":
            jehero1 = "Angela"
            await message.channel.send("Jeremy's hero #1 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero1 add Diggie":
            jehero1 = "Diggie"
            await message.channel.send("Jeremy's hero #1 is now Diggie! :owl: ")
        if message.content == "!ml hero1 add Estes":
            jehero1 = "Estes"
            await message.channel.send("Jeremy's hero #1 is now Estes! :ear:  ")
        if message.content == "!ml hero1 add Rafaela":
            jehero1 = "Rafaela"
            await message.channel.send("Jeremy's hero #1 is now Rafaela! :angel: ")
        if message.content == "!ml hero1 add Rynn":
            jehero1 = "Rynn"
            await message.channel.send("Jeremy's hero #1 is now Rynn! ")
        if message.content == "!ml hero2 add Akai":
            global jehero2
            jehero2 = "Akai"
            await message.channel.send("Jeremy's hero #2 is now Akai! :panda_face: ")
        if message.content == "!ml hero2 add Balmond":
            jehero2 = "Balmond"
            await message.channel.send("Jeremy's hero #2 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero2 add Belerick":
            jehero2 = "Belerick"
            await message.channel.send("Jeremy's hero #2 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero2 add Franco":
            jehero2 = "Franco"
            await message.channel.send("Jeremy's hero #2 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero2 add Esmerelda":
            jehero2 = "Esmerelda"
            await message.channel.send("Jeremy's hero #2 is now Esmerelda! :shield: ")
        if message.content == "!ml hero2 add Gatotkaca":
            jehero2 = "Gatotkaca"
            await message.channel.send("Jeremy's hero #2 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero2 add Grock":
            jehero2 = "Grock"
            await message.channel.send("Jeremy's hero #2 is now Grock! :european_castle: ")
        if message.content == "!ml hero2 add Hilda":
            jehero2 = "Hilda"
            await message.channel.send("Jeremy's hero #2 is now Hilda! :runner: ")
        if message.content == "!ml hero2 add Hylos":
            jehero2 = "Hylos"
            await message.channel.send("Jeremy's hero #2 is now Hylos! :unicorn: ")
        if message.content == "!ml hero2 add Johnson":
            jehero2 = "Johnson"
            await message.channel.send("Jeremy's hero #2 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero2 add Khufra":
            jehero2 = "Khufra"
            await message.channel.send("Jeremy's hero #2 is now Khufra! :clown: ")
        if message.content == "!ml hero2 add Lolita":
            jehero2 = "Lolita"
            await message.channel.send("Jeremy's hero #2 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jehero2 = "Masha"
            await message.channel.send("Jeremy's hero #2 is now Masha! :bear: ")
        if message.content == "!ml hero2 add Minotaur":
            jehero2 = "Minotaur"
            await message.channel.send("Jeremy's hero #2 is now Minotaur! :cow: ")
        if message.content == "!ml hero2 add Tigreal":
            jehero2 = "Tigreal"
            await message.channel.send("Jeremy's hero #2 is now Tigreal! :moyai: ")
        if message.content == "!ml hero2 add Uranus":
            jehero2 = "Uranus"
            await message.channel.send("Jeremy's hero #2 is now Uranus! :peach: ")
        if message.content == "!ml hero2 add X.Borg":
            jehero2 = "X.Borg"
            await message.channel.send("Jeremy's hero #2 is now X.Borg! :fire: ")
        if message.content == "!ml hero2 add Aldous":
            jehero2 = "Aldous"
            await message.channel.send("Jeremy's hero #2 is now Aldous! :fist: ")
        if message.content == "!ml hero2 add Alpha":
            jehero2 = "Alpha"
            await message.channel.send("Jeremy's hero #2 is now Alpha! :airplane: ")
        if message.content == "!ml hero2 add Alucard":
            jehero2 = "Alucard"
            await message.channel.send("Jeremy's hero #2 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero2 add Argus":
            jehero2 = "Argus"
            await message.channel.send("Jeremy's hero #2 is now Argus! :angel: ")
        if message.content == "!ml hero2 add Badang":
            jehero2 = "Badang"
            await message.channel.send("Jeremy's hero #2 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero2 add Bane":
            jehero2 = "Bane"
            await message.channel.send("Jeremy's hero #2 is now Bane! :octopus: ")
        if message.content == "!ml hero2 add Chou":
            jehero2 = "Chou"
            await message.channel.send("Jeremy's hero #2 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero2 add Dyrroth":
            jehero2 = "Dyrroth"
            await message.channel.send("Jeremy's hero #2 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero2 add Freya":
            jehero2 = "Freya"
            await message.channel.send("Jeremy's hero #2 is now Freya! :hammer: ")
        if message.content == "!ml hero2 add Guinevere":
            jehero2 = "Guinevere"
            await message.channel.send("Jeremy's hero #2 is now Guinevere! :dress:  ")
        if message.content == "!ml hero2 add Jawhead":
            jehero2 = "Jawhead"
            await message.channel.send("Jeremy's hero #2 is now Jawhead! :robot: ")
        if message.content == "!ml hero2 add Kaja":
            jehero2 = "Kaja"
            await message.channel.send("Jeremy's hero #2 is now Kaja! :bird: ")
        if message.content == "!ml hero2 add Lapu-Lapu":
            jehero2 = "Lapu-Lapu"
            await message.channel.send("Jeremy's hero #2 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero2 add Leomord":
            jehero2 = "Leomord"
            await message.channel.send("Jeremy's hero #2 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero2 add Martis":
            jehero2 = "Martis"
            await message.channel.send("Jeremy's hero #2 is now Martis! :crab: ")
        if message.content == "!ml hero2 add Minsitthar":
            jehero2 = "Minsitthar"
            await message.channel.send("Jeremy's hero #2 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero2 add Roger":
            jehero2 = "Roger"
            await message.channel.send("Jeremy's hero #2 is now Roger! :wolf: ")
        if message.content == "!ml hero2 add Ruby":
            jehero2 = "Ruby"
            await message.channel.send("Jeremy's hero #2 is now Ruby! :heart: ")
        if message.content == "!ml hero2 add Sun":
            jehero2 = "Sun"
            await message.channel.send("Jeremy's hero #2 is now Sun! :monkey_face: ")
        if message.content == "!ml hero2 add Thamuz":
            jehero2 = "Thamuz"
            await message.channel.send("Jeremy's hero #2 is now Thamuz! :rage: ")
        if message.content == "!ml hero2 add Terizla":
            jehero2 = "Terizla"
            await message.channel.send("Jeremy's hero #2 is now Terizla! :hammer: ")
        if message.content == "!ml hero2 add Zilong":
            jehero2 = "Zilong"
            await message.channel.send("Jeremy's hero #2 is now Zilong! :dragon: ")
        if message.content == "!ml hero2 add Fanny":
            jehero2 = "Fanny"
            await message.channel.send("Jeremy's hero #2 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero2 add Gusion":
            jehero2 = "Gusion"
            await message.channel.send(
                "Jeremy's hero #2 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero2 add Hanzo":
            jehero2 = "Hanzo"
            await message.channel.send("Jeremy's hero #2 is now Hanzo! :ghost: ")
        if message.content == "!ml hero2 add Hayabusa":
            jehero2 = "Hayabusa"
            await message.channel.send("Jeremy's hero #2 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero2 add Helcurt":
            jehero2 = "Helcurt"
            await message.channel.send("Jeremy's hero #2 is now Helcurt! :mute:  ")
        if message.content == "!ml hero2 add Karina":
            jehero2 = "Karina"
            await message.channel.send("Jeremy's hero #2 is now Karina! :purple_heart: ")
        if message.content == "!ml hero2 add Lancelot":
            jehero2 = "Lancelot"
            await message.channel.send("Jeremy's hero #2 is now Lancelot! :fencer: ")
        if message.content == "!ml hero2 add Lesley":
            jehero2 = "Lesley"
            await message.channel.send("Jeremy's hero #2 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero2 add Natalia":
            jehero2 = "Natalia"
            await message.channel.send("Jeremy's hero #2 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero2 add Saber":
            jehero2 = "Saber"
            await message.channel.send("Jeremy's hero #2 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero2 add Selena":
            jehero2 = "Selena"
            await message.channel.send("Jeremy's hero #2 is now Selena! :sleeping:  ")
        if message.content == "!ml hero2 add Alice":
            jehero2 = "Alice"
            await message.channel.send("Jeremy's hero #2 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero2 add Aurora":
            jehero2 = "Aurora"
            await message.channel.send("Jeremy's hero #2 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jehero2 = "Chang'e"
            await message.channel.send("Jeremy's hero #2 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero2 add Cyclops":
            jehero2 = "Cyclops"
            await message.channel.send("Jeremy's hero #2 is now Cyclops! :eye:  ")
        if message.content == "!ml hero2 add Eudora":
            jehero2 = "Eudora"
            await message.channel.send("Jeremy's hero #2 is now Eudora! :zap: ")
        if message.content == "!ml hero2 add Faramis":
            jehero2 = "Faramis"
            await message.channel.send("Jeremy's hero #2 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero2 add Gord":
            jehero2 = "Gord"
            await message.channel.send("Jeremy's hero #2 is now Gord! :snowboarder:")
        if message.content == "!ml hero2 add Harith":
            jehero2 = "Harith"
            await message.channel.send("Jeremy's hero #2 is now Harith! :older_man: ")
        if message.content == "!ml hero2 add Harley":
            jehero2 = "Harley"
            await message.channel.send("Jeremy's hero #2 is now Harley! :tophat: ")
        if message.content == "!ml hero2 add Kadita":
            jehero2 = "Kadita"
            await message.channel.send("Jeremy's hero #2 is now Kadita! :droplet: ")
        if message.content == "!ml hero2 add Kagura":
            jehero2 = "Kagura"
            await message.channel.send("Jeremy's hero #2 is now Kagura! :umbrella2:  ")
        if message.content == "!ml hero2 add Lunox":
            jehero2 = "Lunox"
            await message.channel.send("Jeremy's hero #2 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero2 add Lylia":
            jehero2 = "Lylia"
            await message.channel.send("Jeremy's hero #2 is now Lylia! :boom: ")
        if message.content == "!ml hero2 add Nana":
            jehero2 = "Nana"
            await message.channel.send("Jeremy's hero #2 is now Nana! :cat:  ")
        if message.content == "!ml hero2 add Odette":
            jehero2 = "Odette"
            await message.channel.send("Jeremy's hero #2 is now Odette! :duck: ")
        if message.content == "!ml hero2 add Pharsa":
            jehero2 = "Pharsa"
            await message.channel.send("Jeremy's hero #2 is now Pharsa! :dove:  ")
        if message.content == "!ml hero2 add Vale":
            jehero2 = "Vale"
            await message.channel.send("Jeremy's hero #2 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero2 add Valir":
            jehero2 = "Valir"
            await message.channel.send("Jeremy's hero #2 is now Valir! :fire:")
        if message.content == "!ml hero2 add Vexanna":
            jehero2 = "Vexanna"
            await message.channel.send("Jeremy's hero #2 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero2 add Bruno":
            jehero2 = "Bruno"
            await message.channel.send("Jeremy's hero #2 is now Bruno! :soccer:  ")
        if message.content == "!ml hero2 add Claude":
            jehero2 = "Claude"
            await message.channel.send("Jeremy's hero #2 is now Claude! :monkey:  ")
        if message.content == "!ml hero2 add Clint":
            jehero2 = "Clint"
            await message.channel.send("Jeremy's hero #2 is now Clint! :cowboy: ")
        if message.content == "!ml hero2 add Granger":
            jehero2 = "Granger"
            await message.channel.send("Jeremy's hero #2 is now Granger! :violin: ")
        if message.content == "!ml hero2 add Hanabi":
            jehero2 = "Hanabi"
            await message.channel.send("Jeremy's hero #2 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero2 add Irithel":
            jehero2 = "Irithel"
            await message.channel.send("Jeremy's hero #2 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero2 add Karrie":
            jehero2 = "Karrie"
            await message.channel.send(
                "Jeremy's hero #2 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero2 add Kimmy":
            jehero2 = "Kimmy"
            await message.channel.send("Jeremy's hero #2 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero2 add Layla":
            jehero2 = "Layla"
            await message.channel.send("Jeremy's hero #2 is now Layla! :haircut:  ")
        if message.content == "!ml hero2 add Miya":
            jehero2 = "Miya"
            await message.channel.send("Jeremy's hero #2 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero2 add Moskov":
            jehero2 = "Moskov"
            await message.channel.send("Jeremy's hero #2 is now Moskov! :imp: ")
        if message.content == "!ml hero2 add Yi Sun-Shin":
            jehero2 = "Yi Sun-Shin"
            await message.channel.send("Jeremy's hero #2 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero2 add Angela":
            jehero2 = "Angela"
            await message.channel.send("Jeremy's hero #2 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero2 add Diggie":
            jehero2 = "Diggie"
            await message.channel.send("Jeremy's hero #2 is now Diggie! :owl: ")
        if message.content == "!ml hero2 add Estes":
            jehero2 = "Estes"
            await message.channel.send("Jeremy's hero #2 is now Estes! :ear:  ")
        if message.content == "!ml hero2 add Rafaela":
            jehero2 = "Rafaela"
            await message.channel.send("Jeremy's hero #2 is now Rafaela! :angel: ")
        if message.content == "!ml hero2 add Rynn":
            jehero2 = "Rynn"
            await message.channel.send("Jeremy's hero #2 is now Rynn! ")
        if message.content == "!ml hero3 add Akai":
            global jehero3
            jehero3 = "Akai"
            await message.channel.send("Jeremy's hero #3 is now Akai! :panda_face: ")
        if message.content == "!ml hero3 add Balmond":
            jehero3 = "Balmond"
            await message.channel.send("Jeremy's hero #3 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero3 add Belerick":
            jehero3 = "Belerick"
            await message.channel.send("Jeremy's hero #3 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero3 add Franco":
            jehero3 = "Franco"
            await message.channel.send("Jeremy's hero #3 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero3 add Esmerelda":
            jehero3 = "Esmerelda"
            await message.channel.send("Jeremy's hero #3 is now Esmerelda! :shield: ")
        if message.content == "!ml hero3 add Gatotkaca":
            jehero3 = "Gatotkaca"
            await message.channel.send("Jeremy's hero #3 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero3 add Grock":
            jehero3 = "Grock"
            await message.channel.send("Jeremy's hero #3 is now Grock! :european_castle: ")
        if message.content == "!ml hero3 add Hilda":
            jehero3 = "Hilda"
            await message.channel.send("Jeremy's hero #3 is now Hilda! :runner: ")
        if message.content == "!ml hero3 add Hylos":
            jehero3 = "Hylos"
            await message.channel.send("Jeremy's hero #3 is now Hylos! :unicorn: ")
        if message.content == "!ml hero3 add Johnson":
            jehero3 = "Johnson"
            await message.channel.send("Jeremy's hero #3 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero3 add Khufra":
            jehero3 = "Khufra"
            await message.channel.send("Jeremy's hero #3 is now Khufra! :clown: ")
        if message.content == "!ml hero3 add Lolita":
            jehero3 = "Lolita"
            await message.channel.send("Jeremy's hero #3 is now Lolita! :lollipop: ")
        if message.content == "!ml hero3 add Masha":
            jehero3 = "Masha"
            await message.channel.send("Jeremy's hero #3 is now Masha! :bear: ")
        if message.content == "!ml hero3 add Minotaur":
            jehero3 = "Minotaur"
            await message.channel.send("Jeremy's hero #3 is now Minotaur! :cow: ")
        if message.content == "!ml hero3 add Tigreal":
            jehero3 = "Tigreal"
            await message.channel.send("Jeremy's hero #3 is now Tigreal! :moyai: ")
        if message.content == "!ml hero3 add Uranus":
            jehero3 = "Uranus"
            await message.channel.send("Jeremy's hero #3 is now Uranus! :peach: ")
        if message.content == "!ml hero3 add X.Borg":
            jehero3 = "X.Borg"
            await message.channel.send("Jeremy's hero #3 is now X.Borg! :fire: ")
        if message.content == "!ml hero3 add Aldous":
            jehero3 = "Aldous"
            await message.channel.send("Jeremy's hero #3 is now Aldous! :fist: ")
        if message.content == "!ml hero3 add Alpha":
            jehero3 = "Alpha"
            await message.channel.send("Jeremy's hero #3 is now Alpha! :airplane: ")
        if message.content == "!ml hero3 add Alucard":
            jehero3 = "Alucard"
            await message.channel.send("Jeremy's hero #3 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero3 add Argus":
            jehero3 = "Argus"
            await message.channel.send("Jeremy's hero #3 is now Argus! :angel: ")
        if message.content == "!ml hero3 add Badang":
            jehero3 = "Badang"
            await message.channel.send("Jeremy's hero #3 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero3 add Bane":
            jehero3 = "Bane"
            await message.channel.send("Jeremy's hero #3 is now Bane! :octopus: ")
        if message.content == "!ml hero3 add Chou":
            jehero3 = "Chou"
            await message.channel.send("Jeremy's hero #3 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero3 add Dyrroth":
            jehero3 = "Dyrroth"
            await message.channel.send("Jeremy's hero #3 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero3 add Freya":
            jehero3 = "Freya"
            await message.channel.send("Jeremy's hero #3 is now Freya! :hammer: ")
        if message.content == "!ml hero3 add Guinevere":
            jehero3 = "Guinevere"
            await message.channel.send("Jeremy's hero #3 is now Guinevere! :dress:  ")
        if message.content == "!ml hero3 add Jawhead":
            jehero3 = "Jawhead"
            await message.channel.send("Jeremy's hero #3 is now Jawhead! :robot: ")
        if message.content == "!ml hero3 add Kaja":
            jehero3 = "Kaja"
            await message.channel.send("Jeremy's hero #3 is now Kaja! :bird: ")
        if message.content == "!ml hero3 add Lapu-Lapu":
            jehero3 = "Lapu-Lapu"
            await message.channel.send("Jeremy's hero #3 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero3 add Leomord":
            jehero3 = "Leomord"
            await message.channel.send("Jeremy's hero #3 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero3 add Martis":
            jehero3 = "Martis"
            await message.channel.send("Jeremy's hero #3 is now Martis! :crab: ")
        if message.content == "!ml hero3 add Minsitthar":
            jehero3 = "Minsitthar"
            await message.channel.send("Jeremy's hero #3 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero3 add Roger":
            jehero3 = "Roger"
            await message.channel.send("Jeremy's hero #3 is now Roger! :wolf: ")
        if message.content == "!ml hero3 add Ruby":
            jehero3 = "Ruby"
            await message.channel.send("Jeremy's hero #3 is now Ruby! :heart: ")
        if message.content == "!ml hero3 add Sun":
            jehero3 = "Sun"
            await message.channel.send("Jeremy's hero #3 is now Sun! :monkey_face: ")
        if message.content == "!ml hero3 add Thamuz":
            jehero3 = "Thamuz"
            await message.channel.send("Jeremy's hero #3 is now Thamuz! :rage: ")
        if message.content == "!ml hero3 add Terizla":
            jehero3 = "Terizla"
            await message.channel.send("Jeremy's hero #3 is now Terizla! :hammer: ")
        if message.content == "!ml hero3 add Zilong":
            jehero3 = "Zilong"
            await message.channel.send("Jeremy's hero #3 is now Zilong! :dragon: ")
        if message.content == "!ml hero3 add Fanny":
            jehero3 = "Fanny"
            await message.channel.send("Jeremy's hero #3 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero3 add Gusion":
            jehero3 = "Gusion"
            await message.channel.send(
                "Jeremy's hero #3 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero3 add Hanzo":
            jehero3 = "Hanzo"
            await message.channel.send("Jeremy's hero #3 is now Hanzo! :ghost: ")
        if message.content == "!ml hero3 add Hayabusa":
            jehero3 = "Hayabusa"
            await message.channel.send("Jeremy's hero #3 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero3 add Helcurt":
            jehero3 = "Helcurt"
            await message.channel.send("Jeremy's hero #3 is now Helcurt! :mute:  ")
        if message.content == "!ml hero3 add Karina":
            jehero3 = "Karina"
            await message.channel.send("Jeremy's hero #3 is now Karina! :purple_heart: ")
        if message.content == "!ml hero3 add Lancelot":
            jehero3 = "Lancelot"
            await message.channel.send("Jeremy's hero #3 is now Lancelot! :fencer: ")
        if message.content == "!ml hero3 add Lesley":
            jehero3 = "Lesley"
            await message.channel.send("Jeremy's hero #3 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero3 add Natalia":
            jehero3 = "Natalia"
            await message.channel.send("Jeremy's hero #3 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero3 add Saber":
            jehero3 = "Saber"
            await message.channel.send("Jeremy's hero #3 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero3 add Selena":
            jehero3 = "Selena"
            await message.channel.send("Jeremy's hero #3 is now Selena! :sleeping:  ")
        if message.content == "!ml hero3 add Alice":
            jehero3 = "Alice"
            await message.channel.send("Jeremy's hero #3 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero3 add Aurora":
            jehero3 = "Aurora"
            await message.channel.send("Jeremy's hero #3 is now Aurora! :snow: ")
        if message.content == "!ml hero3 add Chang'e":
            jehero3 = "Chang'e"
            await message.channel.send("Jeremy's hero #3 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero3 add Cyclops":
            jehero3 = "Cyclops"
            await message.channel.send("Jeremy's hero #3 is now Cyclops! :eye:  ")
        if message.content == "!ml hero3 add Eudora":
            jehero3 = "Eudora"
            await message.channel.send("Jeremy's hero #3 is now Eudora! :zap: ")
        if message.content == "!ml hero3 add Faramis":
            jehero3 = "Faramis"
            await message.channel.send("Jeremy's hero #3 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero3 add Gord":
            jehero3 = "Gord"
            await message.channel.send("Jeremy's hero #3 is now Gord! :snowboarder:")
        if message.content == "!ml hero3 add Harith":
            jehero3 = "Harith"
            await message.channel.send("Jeremy's hero #3 is now Harith! :older_man: ")
        if message.content == "!ml hero3 add Harley":
            jehero3 = "Harley"
            await message.channel.send("Jeremy's hero #3 is now Harley! :tophat: ")
        if message.content == "!ml hero3 add Kadita":
            jehero3 = "Kadita"
            await message.channel.send("Jeremy's hero #3 is now Kadita! :droplet: ")
        if message.content == "!ml hero3 add Kagura":
            jehero3 = "Kagura"
            await message.channel.send("Jeremy's hero #3 is now Kagura! :umbrella2:  ")
        if message.content == "!ml hero3 add Lunox":
            jehero3 = "Lunox"
            await message.channel.send("Jeremy's hero #3 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero3 add Lylia":
            jehero3 = "Lylia"
            await message.channel.send("Jeremy's hero #3 is now Lylia! :boom: ")
        if message.content == "!ml hero3 add Nana":
            jehero3 = "Nana"
            await message.channel.send("Jeremy's hero #3 is now Nana! :cat:  ")
        if message.content == "!ml hero3 add Odette":
            jehero3 = "Odette"
            await message.channel.send("Jeremy's hero #3 is now Odette! :duck: ")
        if message.content == "!ml hero3 add Pharsa":
            jehero3 = "Pharsa"
            await message.channel.send("Jeremy's hero #3 is now Pharsa! :dove:  ")
        if message.content == "!ml hero3 add Vale":
            jehero3 = "Vale"
            await message.channel.send("Jeremy's hero #3 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero3 add Valir":
            jehero3 = "Valir"
            await message.channel.send("Jeremy's hero #3 is now Valir! :fire:")
        if message.content == "!ml hero3 add Vexanna":
            jehero3 = "Vexanna"
            await message.channel.send("Jeremy's hero #3 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero3 add Bruno":
            jehero3 = "Bruno"
            await message.channel.send("Jeremy's hero #3 is now Bruno! :soccer:  ")
        if message.content == "!ml hero3 add Claude":
            jehero3 = "Claude"
            await message.channel.send("Jeremy's hero #3 is now Claude! :monkey:  ")
        if message.content == "!ml hero3 add Clint":
            jehero3 = "Clint"
            await message.channel.send("Jeremy's hero #3 is now Clint! :cowboy: ")
        if message.content == "!ml hero3 add Granger":
            jehero3 = "Granger"
            await message.channel.send("Jeremy's hero #3 is now Granger! :violin: ")
        if message.content == "!ml hero3 add Hanabi":
            jehero3 = "Hanabi"
            await message.channel.send("Jeremy's hero #3 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero3 add Irithel":
            jehero3 = "Irithel"
            await message.channel.send("Jeremy's hero #3 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero3 add Karrie":
            jehero3 = "Karrie"
            await message.channel.send(
                "Jeremy's hero #3 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero3 add Kimmy":
            jehero3 = "Kimmy"
            await message.channel.send("Jeremy's hero #3 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero3 add Layla":
            jehero3 = "Layla"
            await message.channel.send("Jeremy's hero #3 is now Layla! :haircut:  ")
        if message.content == "!ml hero3 add Miya":
            jehero3 = "Miya"
            await message.channel.send("Jeremy's hero #3 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero3 add Moskov":
            jehero3 = "Moskov"
            await message.channel.send("Jeremy's hero #3 is now Moskov! :imp: ")
        if message.content == "!ml hero3 add Yi Sun-Shin":
            jehero3 = "Yi Sun-Shin"
            await message.channel.send("Jeremy's hero #3 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero3 add Angela":
            jehero3 = "Angela"
            await message.channel.send("Jeremy's hero #3 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero3 add Diggie":
            jehero3 = "Diggie"
            await message.channel.send("Jeremy's hero #3 is now Diggie! :owl: ")
        if message.content == "!ml hero3 add Estes":
            jehero3 = "Estes"
            await message.channel.send("Jeremy's hero #3 is now Estes! :ear:  ")
        if message.content == "!ml hero3 add Rafaela":
            jehero3 = "Rafaela"
            await message.channel.send("Jeremy's hero #3 is now Rafaela! :angel: ")
        if message.content == "!ml hero3 add Rynn":
            jehero3 = "Rynn"
            await message.channel.send("Jeremy's hero #3 is now Rynn! ")
        if message.content == "!ml hero4 add Akai":
            global jehero4
            jehero4 = "Akai"
            await message.channel.send("Jeremy's hero #4 is now Akai! :panda_face: ")
        if message.content == "!ml hero4 add Balmond":
            jehero4 = "Balmond"
            await message.channel.send("Jeremy's hero #4 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero4 add Belerick":
            jehero4 = "Belerick"
            await message.channel.send("Jeremy's hero #4 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero4 add Franco":
            jehero4 = "Franco"
            await message.channel.send("Jeremy's hero #4 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero4 add Esmerelda":
            jehero4 = "Esmerelda"
            await message.channel.send("Jeremy's hero #4 is now Esmerelda! :shield: ")
        if message.content == "!ml hero4 add Gatotkaca":
            jehero4 = "Gatotkaca"
            await message.channel.send("Jeremy's hero #4 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero4 add Grock":
            jehero4 = "Grock"
            await message.channel.send("Jeremy's hero #4 is now Grock! :european_castle: ")
        if message.content == "!ml hero4 add Hilda":
            jehero4 = "Hilda"
            await message.channel.send("Jeremy's hero #4 is now Hilda! :runner: ")
        if message.content == "!ml hero4 add Hylos":
            jehero4 = "Hylos"
            await message.channel.send("Jeremy's hero #4 is now Hylos! :unicorn: ")
        if message.content == "!ml hero4 add Johnson":
            jehero4 = "Johnson"
            await message.channel.send("Jeremy's hero #4 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero4 add Khufra":
            jehero4 = "Khufra"
            await message.channel.send("Jeremy's hero #4 is now Khufra! :clown: ")
        if message.content == "!ml hero4 add Lolita":
            jehero4 = "Lolita"
            await message.channel.send("Jeremy's hero #4 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jehero4 = "Masha"
            await message.channel.send("Jeremy's hero #4 is now Masha! :bear: ")
        if message.content == "!ml hero4 add Minotaur":
            jehero4 = "Minotaur"
            await message.channel.send("Jeremy's hero #4 is now Minotaur! :cow: ")
        if message.content == "!ml hero4 add Tigreal":
            jehero4 = "Tigreal"
            await message.channel.send("Jeremy's hero #4 is now Tigreal! :moyai: ")
        if message.content == "!ml hero4 add Uranus":
            jehero4 = "Uranus"
            await message.channel.send("Jeremy's hero #4 is now Uranus! :peach: ")
        if message.content == "!ml hero4 add X.Borg":
            jehero4 = "X.Borg"
            await message.channel.send("Jeremy's hero #4 is now X.Borg! :fire: ")
        if message.content == "!ml hero4 add Aldous":
            jehero4 = "Aldous"
            await message.channel.send("Jeremy's hero #4 is now Aldous! :fist: ")
        if message.content == "!ml hero4 add Alpha":
            jehero4 = "Alpha"
            await message.channel.send("Jeremy's hero #4 is now Alpha! :airplane: ")
        if message.content == "!ml hero4 add Alucard":
            jehero4 = "Alucard"
            await message.channel.send("Jeremy's hero #4 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero4 add Argus":
            jehero4 = "Argus"
            await message.channel.send("Jeremy's hero #4 is now Argus! :angel: ")
        if message.content == "!ml hero4 add Badang":
            jehero4 = "Badang"
            await message.channel.send("Jeremy's hero #4 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero4 add Bane":
            jehero4 = "Bane"
            await message.channel.send("Jeremy's hero #4 is now Bane! :octopus: ")
        if message.content == "!ml hero4 add Chou":
            jehero4 = "Chou"
            await message.channel.send("Jeremy's hero #4 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero4 add Dyrroth":
            jehero4 = "Dyrroth"
            await message.channel.send("Jeremy's hero #4 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero4 add Freya":
            jehero4 = "Freya"
            await message.channel.send("Jeremy's hero #4 is now Freya! :hammer: ")
        if message.content == "!ml hero4 add Guinevere":
            jehero4 = "Guinevere"
            await message.channel.send("Jeremy's hero #4 is now Guinevere! :dress:  ")
        if message.content == "!ml hero4 add Jawhead":
            jehero4 = "Jawhead"
            await message.channel.send("Jeremy's hero #4 is now Jawhead! :robot: ")
        if message.content == "!ml hero4 add Kaja":
            jehero4 = "Kaja"
            await message.channel.send("Jeremy's hero #4 is now Kaja! :bird: ")
        if message.content == "!ml hero4 add Lapu-Lapu":
            jehero4 = "Lapu-Lapu"
            await message.channel.send("Jeremy's hero #4 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero4 add Leomord":
            jehero4 = "Leomord"
            await message.channel.send("Jeremy's hero #4 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero4 add Martis":
            jehero4 = "Martis"
            await message.channel.send("Jeremy's hero #4 is now Martis! :crab: ")
        if message.content == "!ml hero4 add Minsitthar":
            jehero4 = "Minsitthar"
            await message.channel.send("Jeremy's hero #4 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero4 add Roger":
            jehero4 = "Roger"
            await message.channel.send("Jeremy's hero #4 is now Roger! :wolf: ")
        if message.content == "!ml hero4 add Ruby":
            jehero4 = "Ruby"
            await message.channel.send("Jeremy's hero #4 is now Ruby! :heart: ")
        if message.content == "!ml hero4 add Sun":
            jehero4 = "Sun"
            await message.channel.send("Jeremy's hero #4 is now Sun! :monkey_face: ")
        if message.content == "!ml hero4 add Thamuz":
            jehero4 = "Thamuz"
            await message.channel.send("Jeremy's hero #4 is now Thamuz! :rage: ")
        if message.content == "!ml hero4 add Terizla":
            jehero4 = "Terizla"
            await message.channel.send("Jeremy's hero #4 is now Terizla! :hammer: ")
        if message.content == "!ml hero4 add Zilong":
            jehero4 = "Zilong"
            await message.channel.send("Jeremy's hero #4 is now Zilong! :dragon: ")
        if message.content == "!ml hero4 add Fanny":
            jehero4 = "Fanny"
            await message.channel.send("Jeremy's hero #4 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero4 add Gusion":
            jehero4 = "Gusion"
            await message.channel.send(
                "Jeremy's hero #4 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero4 add Hanzo":
            jehero4 = "Hanzo"
            await message.channel.send("Jeremy's hero #4 is now Hanzo! :ghost: ")
        if message.content == "!ml hero4 add Hayabusa":
            jehero4 = "Hayabusa"
            await message.channel.send("Jeremy's hero #4 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero4 add Helcurt":
            jehero4 = "Helcurt"
            await message.channel.send("Jeremy's hero #4 is now Helcurt! :mute:  ")
        if message.content == "!ml hero4 add Karina":
            jehero4 = "Karina"
            await message.channel.send("Jeremy's hero #4 is now Karina! :purple_heart: ")
        if message.content == "!ml hero4 add Lancelot":
            jehero4 = "Lancelot"
            await message.channel.send("Jeremy's hero #4 is now Lancelot! :fencer: ")
        if message.content == "!ml hero4 add Lesley":
            jehero4 = "Lesley"
            await message.channel.send("Jeremy's hero #4 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero4 add Natalia":
            jehero4 = "Natalia"
            await message.channel.send("Jeremy's hero #4 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero4 add Saber":
            jehero4 = "Saber"
            await message.channel.send("Jeremy's hero #4 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero4 add Selena":
            jehero4 = "Selena"
            await message.channel.send("Jeremy's hero #4 is now Selena! :sleeping:  ")
        if message.content == "!ml hero4 add Alice":
            jehero4 = "Alice"
            await message.channel.send("Jeremy's hero #4 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero4 add Aurora":
            jehero4 = "Aurora"
            await message.channel.send("Jeremy's hero #4 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jehero4 = "Chang'e"
            await message.channel.send("Jeremy's hero #4 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero4 add Cyclops":
            jehero4 = "Cyclops"
            await message.channel.send("Jeremy's hero #4 is now Cyclops! :eye:  ")
        if message.content == "!ml hero4 add Eudora":
            jehero4 = "Eudora"
            await message.channel.send("Jeremy's hero #4 is now Eudora! :zap: ")
        if message.content == "!ml hero4 add Faramis":
            jehero4 = "Faramis"
            await message.channel.send("Jeremy's hero #4 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero4 add Gord":
            jehero4 = "Gord"
            await message.channel.send("Jeremy's hero #4 is now Gord! :snowboarder:")
        if message.content == "!ml hero4 add Harith":
            jehero4 = "Harith"
            await message.channel.send("Jeremy's hero #4 is now Harith! :older_man: ")
        if message.content == "!ml hero4 add Harley":
            jehero4 = "Harley"
            await message.channel.send("Jeremy's hero #4 is now Harley! :tophat: ")
        if message.content == "!ml hero4 add Kadita":
            jehero4 = "Kadita"
            await message.channel.send("Jeremy's hero #4 is now Kadita! :droplet: ")
        if message.content == "!ml hero4 add Kagura":
            jehero4 = "Kagura"
            await message.channel.send("Jeremy's hero #4 is now Kagura! :umbrella4:  ")
        if message.content == "!ml hero4 add Lunox":
            jehero4 = "Lunox"
            await message.channel.send("Jeremy's hero #4 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero4 add Lylia":
            jehero4 = "Lylia"
            await message.channel.send("Jeremy's hero #4 is now Lylia! :boom: ")
        if message.content == "!ml hero4 add Nana":
            jehero4 = "Nana"
            await message.channel.send("Jeremy's hero #4 is now Nana! :cat:  ")
        if message.content == "!ml hero4 add Odette":
            jehero4 = "Odette"
            await message.channel.send("Jeremy's hero #4 is now Odette! :duck: ")
        if message.content == "!ml hero4 add Pharsa":
            jehero4 = "Pharsa"
            await message.channel.send("Jeremy's hero #4 is now Pharsa! :dove:  ")
        if message.content == "!ml hero4 add Vale":
            jehero4 = "Vale"
            await message.channel.send("Jeremy's hero #4 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero4 add Valir":
            jehero4 = "Valir"
            await message.channel.send("Jeremy's hero #4 is now Valir! :fire:")
        if message.content == "!ml hero4 add Vexanna":
            jehero4 = "Vexanna"
            await message.channel.send("Jeremy's hero #4 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero4 add Bruno":
            jehero4 = "Bruno"
            await message.channel.send("Jeremy's hero #4 is now Bruno! :soccer:  ")
        if message.content == "!ml hero4 add Claude":
            jehero4 = "Claude"
            await message.channel.send("Jeremy's hero #4 is now Claude! :monkey:  ")
        if message.content == "!ml hero4 add Clint":
            jehero4 = "Clint"
            await message.channel.send("Jeremy's hero #4 is now Clint! :cowboy: ")
        if message.content == "!ml hero4 add Granger":
            jehero4 = "Granger"
            await message.channel.send("Jeremy's hero #4 is now Granger! :violin: ")
        if message.content == "!ml hero4 add Hanabi":
            jehero4 = "Hanabi"
            await message.channel.send("Jeremy's hero #4 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero4 add Irithel":
            jehero4 = "Irithel"
            await message.channel.send("Jeremy's hero #4 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero4 add Karrie":
            jehero4 = "Karrie"
            await message.channel.send(
                "Jeremy's hero #4 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero4 add Kimmy":
            jehero4 = "Kimmy"
            await message.channel.send("Jeremy's hero #4 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero4 add Layla":
            jehero4 = "Layla"
            await message.channel.send("Jeremy's hero #4 is now Layla! :haircut:  ")
        if message.content == "!ml hero4 add Miya":
            jehero4 = "Miya"
            await message.channel.send("Jeremy's hero #4 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero4 add Moskov":
            jehero4 = "Moskov"
            await message.channel.send("Jeremy's hero #4 is now Moskov! :imp: ")
        if message.content == "!ml hero4 add Yi Sun-Shin":
            jehero4 = "Yi Sun-Shin"
            await message.channel.send("Jeremy's hero #4 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero4 add Angela":
            jehero4 = "Angela"
            await message.channel.send("Jeremy's hero #4 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero4 add Diggie":
            jehero4 = "Diggie"
            await message.channel.send("Jeremy's hero #4 is now Diggie! :owl: ")
        if message.content == "!ml hero4 add Estes":
            jehero4 = "Estes"
            await message.channel.send("Jeremy's hero #4 is now Estes! :ear:  ")
        if message.content == "!ml hero4 add Rafaela":
            jehero4 = "Rafaela"
            await message.channel.send("Jeremy's hero #4 is now Rafaela! :angel: ")
        if message.content == "!ml hero4 add Rynn":
            jehero4 = "Rynn"
            await message.channel.send("Jeremy's hero #4 is now Rynn! ")
        if message.content == "!ml hero5 add Akai":
            global jehero5
            jehero5 = "Akai"
            await message.channel.send("Jeremy's hero #5 is now Akai! :panda_face: ")
        if message.content == "!ml hero5 add Balmond":
            jehero5 = "Balmond"
            await message.channel.send("Jeremy's hero #5 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero5 add Belerick":
            jehero5 = "Belerick"
            await message.channel.send("Jeremy's hero #5 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero5 add Franco":
            jehero5 = "Franco"
            await message.channel.send("Jeremy's hero #5 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero5 add Esmerelda":
            jehero5 = "Esmerelda"
            await message.channel.send("Jeremy's hero #5 is now Esmerelda! :shield: ")
        if message.content == "!ml hero5 add Gatotkaca":
            jehero5 = "Gatotkaca"
            await message.channel.send("Jeremy's hero #5 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero5 add Grock":
            jehero5 = "Grock"
            await message.channel.send("Jeremy's hero #5 is now Grock! :european_castle: ")
        if message.content == "!ml hero5 add Hilda":
            jehero5 = "Hilda"
            await message.channel.send("Jeremy's hero #5 is now Hilda! :runner: ")
        if message.content == "!ml hero5 add Hylos":
            jehero5 = "Hylos"
            await message.channel.send("Jeremy's hero #5 is now Hylos! :unicorn: ")
        if message.content == "!ml hero5 add Johnson":
            jehero5 = "Johnson"
            await message.channel.send("Jeremy's hero #5 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero5 add Khufra":
            jehero5 = "Khufra"
            await message.channel.send("Jeremy's hero #5 is now Khufra! :clown: ")
        if message.content == "!ml hero5 add Lolita":
            jehero5 = "Lolita"
            await message.channel.send("Jeremy's hero #5 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jehero5 = "Masha"
            await message.channel.send("Jeremy's hero #5 is now Masha! :bear: ")
        if message.content == "!ml hero5 add Minotaur":
            jehero5 = "Minotaur"
            await message.channel.send("Jeremy's hero #5 is now Minotaur! :cow: ")
        if message.content == "!ml hero5 add Tigreal":
            jehero5 = "Tigreal"
            await message.channel.send("Jeremy's hero #5 is now Tigreal! :moyai: ")
        if message.content == "!ml hero5 add Uranus":
            jehero5 = "Uranus"
            await message.channel.send("Jeremy's hero #5 is now Uranus! :peach: ")
        if message.content == "!ml hero5 add X.Borg":
            jehero5 = "X.Borg"
            await message.channel.send("Jeremy's hero #5 is now X.Borg! :fire: ")
        if message.content == "!ml hero5 add Aldous":
            jehero5 = "Aldous"
            await message.channel.send("Jeremy's hero #5 is now Aldous! :fist: ")
        if message.content == "!ml hero5 add Alpha":
            jehero5 = "Alpha"
            await message.channel.send("Jeremy's hero #5 is now Alpha! :airplane: ")
        if message.content == "!ml hero5 add Alucard":
            jehero5 = "Alucard"
            await message.channel.send("Jeremy's hero #5 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero5 add Argus":
            jehero5 = "Argus"
            await message.channel.send("Jeremy's hero #5 is now Argus! :angel: ")
        if message.content == "!ml hero5 add Badang":
            jehero5 = "Badang"
            await message.channel.send("Jeremy's hero #5 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero5 add Bane":
            jehero5 = "Bane"
            await message.channel.send("Jeremy's hero #5 is now Bane! :octopus: ")
        if message.content == "!ml hero5 add Chou":
            jehero5 = "Chou"
            await message.channel.send("Jeremy's hero #5 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero5 add Dyrroth":
            jehero5 = "Dyrroth"
            await message.channel.send("Jeremy's hero #5 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero5 add Freya":
            jehero5 = "Freya"
            await message.channel.send("Jeremy's hero #5 is now Freya! :hammer: ")
        if message.content == "!ml hero5 add Guinevere":
            jehero5 = "Guinevere"
            await message.channel.send("Jeremy's hero #5 is now Guinevere! :dress:  ")
        if message.content == "!ml hero5 add Jawhead":
            jehero5 = "Jawhead"
            await message.channel.send("Jeremy's hero #5 is now Jawhead! :robot: ")
        if message.content == "!ml hero5 add Kaja":
            jehero5 = "Kaja"
            await message.channel.send("Jeremy's hero #5 is now Kaja! :bird: ")
        if message.content == "!ml hero5 add Lapu-Lapu":
            jehero5 = "Lapu-Lapu"
            await message.channel.send("Jeremy's hero #5 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero5 add Leomord":
            jehero5 = "Leomord"
            await message.channel.send("Jeremy's hero #5 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero5 add Martis":
            jehero5 = "Martis"
            await message.channel.send("Jeremy's hero #5 is now Martis! :crab: ")
        if message.content == "!ml hero5 add Minsitthar":
            jehero5 = "Minsitthar"
            await message.channel.send("Jeremy's hero #5 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero5 add Roger":
            jehero5 = "Roger"
            await message.channel.send("Jeremy's hero #5 is now Roger! :wolf: ")
        if message.content == "!ml hero5 add Ruby":
            jehero5 = "Ruby"
            await message.channel.send("Jeremy's hero #5 is now Ruby! :heart: ")
        if message.content == "!ml hero5 add Sun":
            jehero5 = "Sun"
            await message.channel.send("Jeremy's hero #5 is now Sun! :monkey_face: ")
        if message.content == "!ml hero5 add Thamuz":
            jehero5 = "Thamuz"
            await message.channel.send("Jeremy's hero #5 is now Thamuz! :rage: ")
        if message.content == "!ml hero5 add Terizla":
            jehero5 = "Terizla"
            await message.channel.send("Jeremy's hero #5 is now Terizla! :hammer: ")
        if message.content == "!ml hero5 add Zilong":
            jehero5 = "Zilong"
            await message.channel.send("Jeremy's hero #5 is now Zilong! :dragon: ")
        if message.content == "!ml hero5 add Fanny":
            jehero5 = "Fanny"
            await message.channel.send("Jeremy's hero #5 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero5 add Gusion":
            jehero5 = "Gusion"
            await message.channel.send(
                "Jeremy's hero #5 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero5 add Hanzo":
            jehero5 = "Hanzo"
            await message.channel.send("Jeremy's hero #5 is now Hanzo! :ghost: ")
        if message.content == "!ml hero5 add Hayabusa":
            jehero5 = "Hayabusa"
            await message.channel.send("Jeremy's hero #5 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero5 add Helcurt":
            jehero5 = "Helcurt"
            await message.channel.send("Jeremy's hero #5 is now Helcurt! :mute:  ")
        if message.content == "!ml hero5 add Karina":
            jehero5 = "Karina"
            await message.channel.send("Jeremy's hero #5 is now Karina! :purple_heart: ")
        if message.content == "!ml hero5 add Lancelot":
            jehero5 = "Lancelot"
            await message.channel.send("Jeremy's hero #5 is now Lancelot! :fencer: ")
        if message.content == "!ml hero5 add Lesley":
            jehero5 = "Lesley"
            await message.channel.send("Jeremy's hero #5 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero5 add Natalia":
            jehero5 = "Natalia"
            await message.channel.send("Jeremy's hero #5 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero5 add Saber":
            jehero5 = "Saber"
            await message.channel.send("Jeremy's hero #5 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero5 add Selena":
            jehero5 = "Selena"
            await message.channel.send("Jeremy's hero #5 is now Selena! :sleeping:  ")
        if message.content == "!ml hero5 add Alice":
            jehero5 = "Alice"
            await message.channel.send("Jeremy's hero #5 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero5 add Aurora":
            jehero5 = "Aurora"
            await message.channel.send("Jeremy's hero #5 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jehero5 = "Chang'e"
            await message.channel.send("Jeremy's hero #5 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero5 add Cyclops":
            jehero5 = "Cyclops"
            await message.channel.send("Jeremy's hero #5 is now Cyclops! :eye:  ")
        if message.content == "!ml hero5 add Eudora":
            jehero5 = "Eudora"
            await message.channel.send("Jeremy's hero #5 is now Eudora! :zap: ")
        if message.content == "!ml hero5 add Faramis":
            jehero5 = "Faramis"
            await message.channel.send("Jeremy's hero #5 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero5 add Gord":
            jehero5 = "Gord"
            await message.channel.send("Jeremy's hero #5 is now Gord! :snowboarder:")
        if message.content == "!ml hero5 add Harith":
            jehero5 = "Harith"
            await message.channel.send("Jeremy's hero #5 is now Harith! :older_man: ")
        if message.content == "!ml hero5 add Harley":
            jehero5 = "Harley"
            await message.channel.send("Jeremy's hero #5 is now Harley! :tophat: ")
        if message.content == "!ml hero5 add Kadita":
            jehero5 = "Kadita"
            await message.channel.send("Jeremy's hero #5 is now Kadita! :droplet: ")
        if message.content == "!ml hero5 add Kagura":
            jehero5 = "Kagura"
            await message.channel.send("Jeremy's hero #5 is now Kagura! :umbrella5:  ")
        if message.content == "!ml hero5 add Lunox":
            jehero5 = "Lunox"
            await message.channel.send("Jeremy's hero #5 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero5 add Lylia":
            jehero5 = "Lylia"
            await message.channel.send("Jeremy's hero #5 is now Lylia! :boom: ")
        if message.content == "!ml hero5 add Nana":
            jehero5 = "Nana"
            await message.channel.send("Jeremy's hero #5 is now Nana! :cat:  ")
        if message.content == "!ml hero5 add Odette":
            jehero5 = "Odette"
            await message.channel.send("Jeremy's hero #5 is now Odette! :duck: ")
        if message.content == "!ml hero5 add Pharsa":
            jehero5 = "Pharsa"
            await message.channel.send("Jeremy's hero #5 is now Pharsa! :dove:  ")
        if message.content == "!ml hero5 add Vale":
            jehero5 = "Vale"
            await message.channel.send("Jeremy's hero #5 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero5 add Valir":
            jehero5 = "Valir"
            await message.channel.send("Jeremy's hero #5 is now Valir! :fire:")
        if message.content == "!ml hero5 add Vexanna":
            jehero5 = "Vexanna"
            await message.channel.send("Jeremy's hero #5 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero5 add Bruno":
            jehero5 = "Bruno"
            await message.channel.send("Jeremy's hero #5 is now Bruno! :soccer:  ")
        if message.content == "!ml hero5 add Claude":
            jehero5 = "Claude"
            await message.channel.send("Jeremy's hero #5 is now Claude! :monkey:  ")
        if message.content == "!ml hero5 add Clint":
            jehero5 = "Clint"
            await message.channel.send("Jeremy's hero #5 is now Clint! :cowboy: ")
        if message.content == "!ml hero5 add Granger":
            jehero5 = "Granger"
            await message.channel.send("Jeremy's hero #5 is now Granger! :violin: ")
        if message.content == "!ml hero5 add Hanabi":
            jehero5 = "Hanabi"
            await message.channel.send("Jeremy's hero #5 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero5 add Irithel":
            jehero5 = "Irithel"
            await message.channel.send("Jeremy's hero #5 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero5 add Karrie":
            jehero5 = "Karrie"
            await message.channel.send(
                "Jeremy's hero #5 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero5 add Kimmy":
            jehero5 = "Kimmy"
            await message.channel.send("Jeremy's hero #5 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero5 add Layla":
            jehero5 = "Layla"
            await message.channel.send("Jeremy's hero #5 is now Layla! :haircut:  ")
        if message.content == "!ml hero5 add Miya":
            jehero5 = "Miya"
            await message.channel.send("Jeremy's hero #5 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero5 add Moskov":
            jehero5 = "Moskov"
            await message.channel.send("Jeremy's hero #5 is now Moskov! :imp: ")
        if message.content == "!ml hero5 add Yi Sun-Shin":
            jehero5 = "Yi Sun-Shin"
            await message.channel.send("Jeremy's hero #5 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero5 add Angela":
            jehero5 = "Angela"
            await message.channel.send("Jeremy's hero #5 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero5 add Diggie":
            jehero5 = "Diggie"
            await message.channel.send("Jeremy's hero #5 is now Diggie! :owl: ")
        if message.content == "!ml hero5 add Estes":
            jehero5 = "Estes"
            await message.channel.send("Jeremy's hero #5 is now Estes! :ear:  ")
        if message.content == "!ml hero5 add Rafaela":
            jehero5 = "Rafaela"
            await message.channel.send("Jeremy's hero #5 is now Rafaela! :angel: ")
        if message.content == "!ml hero5 add Rynn":
            jehero5 = "Rynn"
            await message.channel.send("Jeremy's hero #5 is now Rynn! ")
        if message.content == "!ml hero6 add Akai":
            global jehero6
            jehero6 = "Akai"
            await message.channel.send("Jeremy's hero #6 is now Akai! :panda_face: ")
        if message.content == "!ml hero6 add Balmond":
            jehero6 = "Balmond"
            await message.channel.send("Jeremy's hero #6 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero6 add Belerick":
            jehero6 = "Belerick"
            await message.channel.send("Jeremy's hero #6 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero6 add Franco":
            jehero6 = "Franco"
            await message.channel.send("Jeremy's hero #6 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero6 add Esmerelda":
            jehero6 = "Esmerelda"
            await message.channel.send("Jeremy's hero #6 is now Esmerelda! :shield: ")
        if message.content == "!ml hero6 add Gatotkaca":
            jehero6 = "Gatotkaca"
            await message.channel.send("Jeremy's hero #6 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero6 add Grock":
            jehero6 = "Grock"
            await message.channel.send("Jeremy's hero #6 is now Grock! :european_castle: ")
        if message.content == "!ml hero6 add Hilda":
            jehero6 = "Hilda"
            await message.channel.send("Jeremy's hero #6 is now Hilda! :runner: ")
        if message.content == "!ml hero6 add Hylos":
            jehero6 = "Hylos"
            await message.channel.send("Jeremy's hero #6 is now Hylos! :unicorn: ")
        if message.content == "!ml hero6 add Johnson":
            jehero6 = "Johnson"
            await message.channel.send("Jeremy's hero #6 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero6 add Khufra":
            jehero6 = "Khufra"
            await message.channel.send("Jeremy's hero #6 is now Khufra! :clown: ")
        if message.content == "!ml hero6 add Lolita":
            jehero6 = "Lolita"
            await message.channel.send("Jeremy's hero #6 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jehero6 = "Masha"
            await message.channel.send("Jeremy's hero #6 is now Masha! :bear: ")
        if message.content == "!ml hero6 add Minotaur":
            jehero6 = "Minotaur"
            await message.channel.send("Jeremy's hero #6 is now Minotaur! :cow: ")
        if message.content == "!ml hero6 add Tigreal":
            jehero6 = "Tigreal"
            await message.channel.send("Jeremy's hero #6 is now Tigreal! :moyai: ")
        if message.content == "!ml hero6 add Uranus":
            jehero6 = "Uranus"
            await message.channel.send("Jeremy's hero #6 is now Uranus! :peach: ")
        if message.content == "!ml hero6 add X.Borg":
            jehero6 = "X.Borg"
            await message.channel.send("Jeremy's hero #6 is now X.Borg! :fire: ")
        if message.content == "!ml hero6 add Aldous":
            jehero6 = "Aldous"
            await message.channel.send("Jeremy's hero #6 is now Aldous! :fist: ")
        if message.content == "!ml hero6 add Alpha":
            jehero6 = "Alpha"
            await message.channel.send("Jeremy's hero #6 is now Alpha! :airplane: ")
        if message.content == "!ml hero6 add Alucard":
            jehero6 = "Alucard"
            await message.channel.send("Jeremy's hero #6 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero6 add Argus":
            jehero6 = "Argus"
            await message.channel.send("Jeremy's hero #6 is now Argus! :angel: ")
        if message.content == "!ml hero6 add Badang":
            jehero6 = "Badang"
            await message.channel.send("Jeremy's hero #6 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero6 add Bane":
            jehero6 = "Bane"
            await message.channel.send("Jeremy's hero #6 is now Bane! :octopus: ")
        if message.content == "!ml hero6 add Chou":
            jehero6 = "Chou"
            await message.channel.send("Jeremy's hero #6 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero6 add Dyrroth":
            jehero6 = "Dyrroth"
            await message.channel.send("Jeremy's hero #6 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero6 add Freya":
            jehero6 = "Freya"
            await message.channel.send("Jeremy's hero #6 is now Freya! :hammer: ")
        if message.content == "!ml hero6 add Guinevere":
            jehero6 = "Guinevere"
            await message.channel.send("Jeremy's hero #6 is now Guinevere! :dress:  ")
        if message.content == "!ml hero6 add Jawhead":
            jehero6 = "Jawhead"
            await message.channel.send("Jeremy's hero #6 is now Jawhead! :robot: ")
        if message.content == "!ml hero6 add Kaja":
            jehero6 = "Kaja"
            await message.channel.send("Jeremy's hero #6 is now Kaja! :bird: ")
        if message.content == "!ml hero6 add Lapu-Lapu":
            jehero6 = "Lapu-Lapu"
            await message.channel.send("Jeremy's hero #6 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero6 add Leomord":
            jehero6 = "Leomord"
            await message.channel.send("Jeremy's hero #6 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero6 add Martis":
            jehero6 = "Martis"
            await message.channel.send("Jeremy's hero #6 is now Martis! :crab: ")
        if message.content == "!ml hero6 add Minsitthar":
            jehero6 = "Minsitthar"
            await message.channel.send("Jeremy's hero #6 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero6 add Roger":
            jehero6 = "Roger"
            await message.channel.send("Jeremy's hero #6 is now Roger! :wolf: ")
        if message.content == "!ml hero6 add Ruby":
            jehero6 = "Ruby"
            await message.channel.send("Jeremy's hero #6 is now Ruby! :heart: ")
        if message.content == "!ml hero6 add Sun":
            jehero6 = "Sun"
            await message.channel.send("Jeremy's hero #6 is now Sun! :monkey_face: ")
        if message.content == "!ml hero6 add Thamuz":
            jehero6 = "Thamuz"
            await message.channel.send("Jeremy's hero #6 is now Thamuz! :rage: ")
        if message.content == "!ml hero6 add Terizla":
            jehero6 = "Terizla"
            await message.channel.send("Jeremy's hero #6 is now Terizla! :hammer: ")
        if message.content == "!ml hero6 add Zilong":
            jehero6 = "Zilong"
            await message.channel.send("Jeremy's hero #6 is now Zilong! :dragon: ")
        if message.content == "!ml hero6 add Fanny":
            jehero6 = "Fanny"
            await message.channel.send("Jeremy's hero #6 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero6 add Gusion":
            jehero6 = "Gusion"
            await message.channel.send(
                "Jeremy's hero #6 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero6 add Hanzo":
            jehero6 = "Hanzo"
            await message.channel.send("Jeremy's hero #6 is now Hanzo! :ghost: ")
        if message.content == "!ml hero6 add Hayabusa":
            jehero6 = "Hayabusa"
            await message.channel.send("Jeremy's hero #6 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero6 add Helcurt":
            jehero6 = "Helcurt"
            await message.channel.send("Jeremy's hero #6 is now Helcurt! :mute:  ")
        if message.content == "!ml hero6 add Karina":
            jehero6 = "Karina"
            await message.channel.send("Jeremy's hero #6 is now Karina! :purple_heart: ")
        if message.content == "!ml hero6 add Lancelot":
            jehero6 = "Lancelot"
            await message.channel.send("Jeremy's hero #6 is now Lancelot! :fencer: ")
        if message.content == "!ml hero6 add Lesley":
            jehero6 = "Lesley"
            await message.channel.send("Jeremy's hero #6 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero6 add Natalia":
            jehero6 = "Natalia"
            await message.channel.send("Jeremy's hero #6 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero6 add Saber":
            jehero6 = "Saber"
            await message.channel.send("Jeremy's hero #6 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero6 add Selena":
            jehero6 = "Selena"
            await message.channel.send("Jeremy's hero #6 is now Selena! :sleeping:  ")
        if message.content == "!ml hero6 add Alice":
            jehero6 = "Alice"
            await message.channel.send("Jeremy's hero #6 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero6 add Aurora":
            jehero6 = "Aurora"
            await message.channel.send("Jeremy's hero #6 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jehero6 = "Chang'e"
            await message.channel.send("Jeremy's hero #6 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero6 add Cyclops":
            jehero6 = "Cyclops"
            await message.channel.send("Jeremy's hero #6 is now Cyclops! :eye:  ")
        if message.content == "!ml hero6 add Eudora":
            jehero6 = "Eudora"
            await message.channel.send("Jeremy's hero #6 is now Eudora! :zap: ")
        if message.content == "!ml hero6 add Faramis":
            jehero6 = "Faramis"
            await message.channel.send("Jeremy's hero #6 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero6 add Gord":
            jehero6 = "Gord"
            await message.channel.send("Jeremy's hero #6 is now Gord! :snowboarder:")
        if message.content == "!ml hero6 add Harith":
            jehero6 = "Harith"
            await message.channel.send("Jeremy's hero #6 is now Harith! :older_man: ")
        if message.content == "!ml hero6 add Harley":
            jehero6 = "Harley"
            await message.channel.send("Jeremy's hero #6 is now Harley! :tophat: ")
        if message.content == "!ml hero6 add Kadita":
            jehero6 = "Kadita"
            await message.channel.send("Jeremy's hero #6 is now Kadita! :droplet: ")
        if message.content == "!ml hero6 add Kagura":
            jehero6 = "Kagura"
            await message.channel.send("Jeremy's hero #6 is now Kagura! :umbrella6:  ")
        if message.content == "!ml hero6 add Lunox":
            jehero6 = "Lunox"
            await message.channel.send("Jeremy's hero #6 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero6 add Lylia":
            jehero6 = "Lylia"
            await message.channel.send("Jeremy's hero #6 is now Lylia! :boom: ")
        if message.content == "!ml hero6 add Nana":
            jehero6 = "Nana"
            await message.channel.send("Jeremy's hero #6 is now Nana! :cat:  ")
        if message.content == "!ml hero6 add Odette":
            jehero6 = "Odette"
            await message.channel.send("Jeremy's hero #6 is now Odette! :duck: ")
        if message.content == "!ml hero6 add Pharsa":
            jehero6 = "Pharsa"
            await message.channel.send("Jeremy's hero #6 is now Pharsa! :dove:  ")
        if message.content == "!ml hero6 add Vale":
            jehero6 = "Vale"
            await message.channel.send("Jeremy's hero #6 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero6 add Valir":
            jehero6 = "Valir"
            await message.channel.send("Jeremy's hero #6 is now Valir! :fire:")
        if message.content == "!ml hero6 add Vexanna":
            jehero6 = "Vexanna"
            await message.channel.send("Jeremy's hero #6 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero6 add Bruno":
            jehero6 = "Bruno"
            await message.channel.send("Jeremy's hero #6 is now Bruno! :soccer:  ")
        if message.content == "!ml hero6 add Claude":
            jehero6 = "Claude"
            await message.channel.send("Jeremy's hero #6 is now Claude! :monkey:  ")
        if message.content == "!ml hero6 add Clint":
            jehero6 = "Clint"
            await message.channel.send("Jeremy's hero #6 is now Clint! :cowboy: ")
        if message.content == "!ml hero6 add Granger":
            jehero6 = "Granger"
            await message.channel.send("Jeremy's hero #6 is now Granger! :violin: ")
        if message.content == "!ml hero6 add Hanabi":
            jehero6 = "Hanabi"
            await message.channel.send("Jeremy's hero #6 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero6 add Irithel":
            jehero6 = "Irithel"
            await message.channel.send("Jeremy's hero #6 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero6 add Karrie":
            jehero6 = "Karrie"
            await message.channel.send(
                "Jeremy's hero #6 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero6 add Kimmy":
            jehero6 = "Kimmy"
            await message.channel.send("Jeremy's hero #6 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero6 add Layla":
            jehero6 = "Layla"
            await message.channel.send("Jeremy's hero #6 is now Layla! :haircut:  ")
        if message.content == "!ml hero6 add Miya":
            jehero6 = "Miya"
            await message.channel.send("Jeremy's hero #6 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero6 add Moskov":
            jehero6 = "Moskov"
            await message.channel.send("Jeremy's hero #6 is now Moskov! :imp: ")
        if message.content == "!ml hero6 add Yi Sun-Shin":
            jehero6 = "Yi Sun-Shin"
            await message.channel.send("Jeremy's hero #6 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero6 add Angela":
            jehero6 = "Angela"
            await message.channel.send("Jeremy's hero #6 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero6 add Diggie":
            jehero6 = "Diggie"
            await message.channel.send("Jeremy's hero #6 is now Diggie! :owl: ")
        if message.content == "!ml hero6 add Estes":
            jehero6 = "Estes"
            await message.channel.send("Jeremy's hero #6 is now Estes! :ear:  ")
        if message.content == "!ml hero6 add Rafaela":
            jehero6 = "Rafaela"
            await message.channel.send("Jeremy's hero #6 is now Rafaela! :angel: ")
        if message.content == "!ml hero6 add Rynn":
            jehero6 = "Rynn"
            await message.channel.send("Jeremy's hero #6 is now Rynn! ")
        if message.content == "!ml hero7 add Akai":
            global jehero7
            jehero7 = "Akai"
            await message.channel.send("Jeremy's hero #7 is now Akai! :panda_face: ")
        if message.content == "!ml hero7 add Balmond":
            jehero7 = "Balmond"
            await message.channel.send("Jeremy's hero #7 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero7 add Belerick":
            jehero7 = "Belerick"
            await message.channel.send("Jeremy's hero #7 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero7 add Franco":
            jehero7 = "Franco"
            await message.channel.send("Jeremy's hero #7 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero7 add Esmerelda":
            jehero7 = "Esmerelda"
            await message.channel.send("Jeremy's hero #7 is now Esmerelda! :shield: ")
        if message.content == "!ml hero7 add Gatotkaca":
            jehero7 = "Gatotkaca"
            await message.channel.send("Jeremy's hero #7 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero7 add Grock":
            jehero7 = "Grock"
            await message.channel.send("Jeremy's hero #7 is now Grock! :european_castle: ")
        if message.content == "!ml hero7 add Hilda":
            jehero7 = "Hilda"
            await message.channel.send("Jeremy's hero #7 is now Hilda! :runner: ")
        if message.content == "!ml hero7 add Hylos":
            jehero7 = "Hylos"
            await message.channel.send("Jeremy's hero #7 is now Hylos! :unicorn: ")
        if message.content == "!ml hero7 add Johnson":
            jehero7 = "Johnson"
            await message.channel.send("Jeremy's hero #7 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero7 add Khufra":
            jehero7 = "Khufra"
            await message.channel.send("Jeremy's hero #7 is now Khufra! :clown: ")
        if message.content == "!ml hero7 add Lolita":
            jehero7 = "Lolita"
            await message.channel.send("Jeremy's hero #7 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jehero7 = "Masha"
            await message.channel.send("Jeremy's hero #7 is now Masha! :bear: ")
        if message.content == "!ml hero7 add Minotaur":
            jehero7 = "Minotaur"
            await message.channel.send("Jeremy's hero #7 is now Minotaur! :cow: ")
        if message.content == "!ml hero7 add Tigreal":
            jehero7 = "Tigreal"
            await message.channel.send("Jeremy's hero #7 is now Tigreal! :moyai: ")
        if message.content == "!ml hero7 add Uranus":
            jehero7 = "Uranus"
            await message.channel.send("Jeremy's hero #7 is now Uranus! :peach: ")
        if message.content == "!ml hero7 add X.Borg":
            jehero7 = "X.Borg"
            await message.channel.send("Jeremy's hero #7 is now X.Borg! :fire: ")
        if message.content == "!ml hero7 add Aldous":
            jehero7 = "Aldous"
            await message.channel.send("Jeremy's hero #7 is now Aldous! :fist: ")
        if message.content == "!ml hero7 add Alpha":
            jehero7 = "Alpha"
            await message.channel.send("Jeremy's hero #7 is now Alpha! :airplane: ")
        if message.content == "!ml hero7 add Alucard":
            jehero7 = "Alucard"
            await message.channel.send("Jeremy's hero #7 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero7 add Argus":
            jehero7 = "Argus"
            await message.channel.send("Jeremy's hero #7 is now Argus! :angel: ")
        if message.content == "!ml hero7 add Badang":
            jehero7 = "Badang"
            await message.channel.send("Jeremy's hero #7 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero7 add Bane":
            jehero7 = "Bane"
            await message.channel.send("Jeremy's hero #7 is now Bane! :octopus: ")
        if message.content == "!ml hero7 add Chou":
            jehero7 = "Chou"
            await message.channel.send("Jeremy's hero #7 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero7 add Dyrroth":
            jehero7 = "Dyrroth"
            await message.channel.send("Jeremy's hero #7 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero7 add Freya":
            jehero7 = "Freya"
            await message.channel.send("Jeremy's hero #7 is now Freya! :hammer: ")
        if message.content == "!ml hero7 add Guinevere":
            jehero7 = "Guinevere"
            await message.channel.send("Jeremy's hero #7 is now Guinevere! :dress:  ")
        if message.content == "!ml hero7 add Jawhead":
            jehero7 = "Jawhead"
            await message.channel.send("Jeremy's hero #7 is now Jawhead! :robot: ")
        if message.content == "!ml hero7 add Kaja":
            jehero7 = "Kaja"
            await message.channel.send("Jeremy's hero #7 is now Kaja! :bird: ")
        if message.content == "!ml hero7 add Lapu-Lapu":
            jehero7 = "Lapu-Lapu"
            await message.channel.send("Jeremy's hero #7 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero7 add Leomord":
            jehero7 = "Leomord"
            await message.channel.send("Jeremy's hero #7 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero7 add Martis":
            jehero7 = "Martis"
            await message.channel.send("Jeremy's hero #7 is now Martis! :crab: ")
        if message.content == "!ml hero7 add Minsitthar":
            jehero7 = "Minsitthar"
            await message.channel.send("Jeremy's hero #7 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero7 add Roger":
            jehero7 = "Roger"
            await message.channel.send("Jeremy's hero #7 is now Roger! :wolf: ")
        if message.content == "!ml hero7 add Ruby":
            jehero7 = "Ruby"
            await message.channel.send("Jeremy's hero #7 is now Ruby! :heart: ")
        if message.content == "!ml hero7 add Sun":
            jehero7 = "Sun"
            await message.channel.send("Jeremy's hero #7 is now Sun! :monkey_face: ")
        if message.content == "!ml hero7 add Thamuz":
            jehero7 = "Thamuz"
            await message.channel.send("Jeremy's hero #7 is now Thamuz! :rage: ")
        if message.content == "!ml hero7 add Terizla":
            jehero7 = "Terizla"
            await message.channel.send("Jeremy's hero #7 is now Terizla! :hammer: ")
        if message.content == "!ml hero7 add Zilong":
            jehero7 = "Zilong"
            await message.channel.send("Jeremy's hero #7 is now Zilong! :dragon: ")
        if message.content == "!ml hero7 add Fanny":
            jehero7 = "Fanny"
            await message.channel.send("Jeremy's hero #7 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero7 add Gusion":
            jehero7 = "Gusion"
            await message.channel.send(
                "Jeremy's hero #7 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero7 add Hanzo":
            jehero7 = "Hanzo"
            await message.channel.send("Jeremy's hero #7 is now Hanzo! :ghost: ")
        if message.content == "!ml hero7 add Hayabusa":
            jehero7 = "Hayabusa"
            await message.channel.send("Jeremy's hero #7 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero7 add Helcurt":
            jehero7 = "Helcurt"
            await message.channel.send("Jeremy's hero #7 is now Helcurt! :mute:  ")
        if message.content == "!ml hero7 add Karina":
            jehero7 = "Karina"
            await message.channel.send("Jeremy's hero #7 is now Karina! :purple_heart: ")
        if message.content == "!ml hero7 add Lancelot":
            jehero7 = "Lancelot"
            await message.channel.send("Jeremy's hero #7 is now Lancelot! :fencer: ")
        if message.content == "!ml hero7 add Lesley":
            jehero7 = "Lesley"
            await message.channel.send("Jeremy's hero #7 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero7 add Natalia":
            jehero7 = "Natalia"
            await message.channel.send("Jeremy's hero #7 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero7 add Saber":
            jehero7 = "Saber"
            await message.channel.send("Jeremy's hero #7 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero7 add Selena":
            jehero7 = "Selena"
            await message.channel.send("Jeremy's hero #7 is now Selena! :sleeping:  ")
        if message.content == "!ml hero7 add Alice":
            jehero7 = "Alice"
            await message.channel.send("Jeremy's hero #7 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero7 add Aurora":
            jehero7 = "Aurora"
            await message.channel.send("Jeremy's hero #7 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jehero7 = "Chang'e"
            await message.channel.send("Jeremy's hero #7 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero7 add Cyclops":
            jehero7 = "Cyclops"
            await message.channel.send("Jeremy's hero #7 is now Cyclops! :eye:  ")
        if message.content == "!ml hero7 add Eudora":
            jehero7 = "Eudora"
            await message.channel.send("Jeremy's hero #7 is now Eudora! :zap: ")
        if message.content == "!ml hero7 add Faramis":
            jehero7 = "Faramis"
            await message.channel.send("Jeremy's hero #7 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero7 add Gord":
            jehero7 = "Gord"
            await message.channel.send("Jeremy's hero #7 is now Gord! :snowboarder:")
        if message.content == "!ml hero7 add Harith":
            jehero7 = "Harith"
            await message.channel.send("Jeremy's hero #7 is now Harith! :older_man: ")
        if message.content == "!ml hero7 add Harley":
            jehero7 = "Harley"
            await message.channel.send("Jeremy's hero #7 is now Harley! :tophat: ")
        if message.content == "!ml hero7 add Kadita":
            jehero7 = "Kadita"
            await message.channel.send("Jeremy's hero #7 is now Kadita! :droplet: ")
        if message.content == "!ml hero7 add Kagura":
            jehero7 = "Kagura"
            await message.channel.send("Jeremy's hero #7 is now Kagura! :umbrella7:  ")
        if message.content == "!ml hero7 add Lunox":
            jehero7 = "Lunox"
            await message.channel.send("Jeremy's hero #7 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero7 add Lylia":
            jehero7 = "Lylia"
            await message.channel.send("Jeremy's hero #7 is now Lylia! :boom: ")
        if message.content == "!ml hero7 add Nana":
            jehero7 = "Nana"
            await message.channel.send("Jeremy's hero #7 is now Nana! :cat:  ")
        if message.content == "!ml hero7 add Odette":
            jehero7 = "Odette"
            await message.channel.send("Jeremy's hero #7 is now Odette! :duck: ")
        if message.content == "!ml hero7 add Pharsa":
            jehero7 = "Pharsa"
            await message.channel.send("Jeremy's hero #7 is now Pharsa! :dove:  ")
        if message.content == "!ml hero7 add Vale":
            jehero7 = "Vale"
            await message.channel.send("Jeremy's hero #7 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero7 add Valir":
            jehero7 = "Valir"
            await message.channel.send("Jeremy's hero #7 is now Valir! :fire:")
        if message.content == "!ml hero7 add Vexanna":
            jehero7 = "Vexanna"
            await message.channel.send("Jeremy's hero #7 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero7 add Bruno":
            jehero7 = "Bruno"
            await message.channel.send("Jeremy's hero #7 is now Bruno! :soccer:  ")
        if message.content == "!ml hero7 add Claude":
            jehero7 = "Claude"
            await message.channel.send("Jeremy's hero #7 is now Claude! :monkey:  ")
        if message.content == "!ml hero7 add Clint":
            jehero7 = "Clint"
            await message.channel.send("Jeremy's hero #7 is now Clint! :cowboy: ")
        if message.content == "!ml hero7 add Granger":
            jehero7 = "Granger"
            await message.channel.send("Jeremy's hero #7 is now Granger! :violin: ")
        if message.content == "!ml hero7 add Hanabi":
            jehero7 = "Hanabi"
            await message.channel.send("Jeremy's hero #7 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero7 add Irithel":
            jehero7 = "Irithel"
            await message.channel.send("Jeremy's hero #7 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero7 add Karrie":
            jehero7 = "Karrie"
            await message.channel.send(
                "Jeremy's hero #7 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero7 add Kimmy":
            jehero7 = "Kimmy"
            await message.channel.send("Jeremy's hero #7 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero7 add Layla":
            jehero7 = "Layla"
            await message.channel.send("Jeremy's hero #7 is now Layla! :haircut:  ")
        if message.content == "!ml hero7 add Miya":
            jehero7 = "Miya"
            await message.channel.send("Jeremy's hero #7 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero7 add Moskov":
            jehero7 = "Moskov"
            await message.channel.send("Jeremy's hero #7 is now Moskov! :imp: ")
        if message.content == "!ml hero7 add Yi Sun-Shin":
            jehero7 = "Yi Sun-Shin"
            await message.channel.send("Jeremy's hero #7 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero7 add Angela":
            jehero7 = "Angela"
            await message.channel.send("Jeremy's hero #7 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero7 add Diggie":
            jehero7 = "Diggie"
            await message.channel.send("Jeremy's hero #7 is now Diggie! :owl: ")
        if message.content == "!ml hero7 add Estes":
            jehero7 = "Estes"
            await message.channel.send("Jeremy's hero #7 is now Estes! :ear:  ")
        if message.content == "!ml hero7 add Rafaela":
            jehero7 = "Rafaela"
            await message.channel.send("Jeremy's hero #7 is now Rafaela! :angel: ")
        if message.content == "!ml hero7 add Rynn":
            jehero7 = "Rynn"
            await message.channel.send("Jeremy's hero #7 is now Rynn! ")
        if message.content == "!ml hero8 add Akai":
            global jehero8
            jehero8 = "Akai"
            await message.channel.send("Jeremy's hero #8 is now Akai! :panda_face: ")
        if message.content == "!ml hero8 add Balmond":
            jehero8 = "Balmond"
            await message.channel.send("Jeremy's hero #8 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero8 add Belerick":
            jehero8 = "Belerick"
            await message.channel.send("Jeremy's hero #8 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero8 add Franco":
            jehero8 = "Franco"
            await message.channel.send("Jeremy's hero #8 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero8 add Esmerelda":
            jehero8 = "Esmerelda"
            await message.channel.send("Jeremy's hero #8 is now Esmerelda! :shield: ")
        if message.content == "!ml hero8 add Gatotkaca":
            jehero8 = "Gatotkaca"
            await message.channel.send("Jeremy's hero #8 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero8 add Grock":
            jehero8 = "Grock"
            await message.channel.send("Jeremy's hero #8 is now Grock! :european_castle: ")
        if message.content == "!ml hero8 add Hilda":
            jehero8 = "Hilda"
            await message.channel.send("Jeremy's hero #8 is now Hilda! :runner: ")
        if message.content == "!ml hero8 add Hylos":
            jehero8 = "Hylos"
            await message.channel.send("Jeremy's hero #8 is now Hylos! :unicorn: ")
        if message.content == "!ml hero8 add Johnson":
            jehero8 = "Johnson"
            await message.channel.send("Jeremy's hero #8 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero8 add Khufra":
            jehero8 = "Khufra"
            await message.channel.send("Jeremy's hero #8 is now Khufra! :clown: ")
        if message.content == "!ml hero8 add Lolita":
            jehero8 = "Lolita"
            await message.channel.send("Jeremy's hero #8 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jehero8 = "Masha"
            await message.channel.send("Jeremy's hero #8 is now Masha! :bear: ")
        if message.content == "!ml hero8 add Minotaur":
            jehero8 = "Minotaur"
            await message.channel.send("Jeremy's hero #8 is now Minotaur! :cow: ")
        if message.content == "!ml hero8 add Tigreal":
            jehero8 = "Tigreal"
            await message.channel.send("Jeremy's hero #8 is now Tigreal! :moyai: ")
        if message.content == "!ml hero8 add Uranus":
            jehero8 = "Uranus"
            await message.channel.send("Jeremy's hero #8 is now Uranus! :peach: ")
        if message.content == "!ml hero8 add X.Borg":
            jehero8 = "X.Borg"
            await message.channel.send("Jeremy's hero #8 is now X.Borg! :fire: ")
        if message.content == "!ml hero8 add Aldous":
            jehero8 = "Aldous"
            await message.channel.send("Jeremy's hero #8 is now Aldous! :fist: ")
        if message.content == "!ml hero8 add Alpha":
            jehero8 = "Alpha"
            await message.channel.send("Jeremy's hero #8 is now Alpha! :airplane: ")
        if message.content == "!ml hero8 add Alucard":
            jehero8 = "Alucard"
            await message.channel.send("Jeremy's hero #8 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero8 add Argus":
            jehero8 = "Argus"
            await message.channel.send("Jeremy's hero #8 is now Argus! :angel: ")
        if message.content == "!ml hero8 add Badang":
            jehero8 = "Badang"
            await message.channel.send("Jeremy's hero #8 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero8 add Bane":
            jehero8 = "Bane"
            await message.channel.send("Jeremy's hero #8 is now Bane! :octopus: ")
        if message.content == "!ml hero8 add Chou":
            jehero8 = "Chou"
            await message.channel.send("Jeremy's hero #8 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero8 add Dyrroth":
            jehero8 = "Dyrroth"
            await message.channel.send("Jeremy's hero #8 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero8 add Freya":
            jehero8 = "Freya"
            await message.channel.send("Jeremy's hero #8 is now Freya! :hammer: ")
        if message.content == "!ml hero8 add Guinevere":
            jehero8 = "Guinevere"
            await message.channel.send("Jeremy's hero #8 is now Guinevere! :dress:  ")
        if message.content == "!ml hero8 add Jawhead":
            jehero8 = "Jawhead"
            await message.channel.send("Jeremy's hero #8 is now Jawhead! :robot: ")
        if message.content == "!ml hero8 add Kaja":
            jehero8 = "Kaja"
            await message.channel.send("Jeremy's hero #8 is now Kaja! :bird: ")
        if message.content == "!ml hero8 add Lapu-Lapu":
            jehero8 = "Lapu-Lapu"
            await message.channel.send("Jeremy's hero #8 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero8 add Leomord":
            jehero8 = "Leomord"
            await message.channel.send("Jeremy's hero #8 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero8 add Martis":
            jehero8 = "Martis"
            await message.channel.send("Jeremy's hero #8 is now Martis! :crab: ")
        if message.content == "!ml hero8 add Minsitthar":
            jehero8 = "Minsitthar"
            await message.channel.send("Jeremy's hero #8 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero8 add Roger":
            jehero8 = "Roger"
            await message.channel.send("Jeremy's hero #8 is now Roger! :wolf: ")
        if message.content == "!ml hero8 add Ruby":
            jehero8 = "Ruby"
            await message.channel.send("Jeremy's hero #8 is now Ruby! :heart: ")
        if message.content == "!ml hero8 add Sun":
            jehero8 = "Sun"
            await message.channel.send("Jeremy's hero #8 is now Sun! :monkey_face: ")
        if message.content == "!ml hero8 add Thamuz":
            jehero8 = "Thamuz"
            await message.channel.send("Jeremy's hero #8 is now Thamuz! :rage: ")
        if message.content == "!ml hero8 add Terizla":
            jehero8 = "Terizla"
            await message.channel.send("Jeremy's hero #8 is now Terizla! :hammer: ")
        if message.content == "!ml hero8 add Zilong":
            jehero8 = "Zilong"
            await message.channel.send("Jeremy's hero #8 is now Zilong! :dragon: ")
        if message.content == "!ml hero8 add Fanny":
            jehero8 = "Fanny"
            await message.channel.send("Jeremy's hero #8 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero8 add Gusion":
            jehero8 = "Gusion"
            await message.channel.send(
                "Jeremy's hero #8 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero8 add Hanzo":
            jehero8 = "Hanzo"
            await message.channel.send("Jeremy's hero #8 is now Hanzo! :ghost: ")
        if message.content == "!ml hero8 add Hayabusa":
            jehero8 = "Hayabusa"
            await message.channel.send("Jeremy's hero #8 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero8 add Helcurt":
            jehero8 = "Helcurt"
            await message.channel.send("Jeremy's hero #8 is now Helcurt! :mute:  ")
        if message.content == "!ml hero8 add Karina":
            jehero8 = "Karina"
            await message.channel.send("Jeremy's hero #8 is now Karina! :purple_heart: ")
        if message.content == "!ml hero8 add Lancelot":
            jehero8 = "Lancelot"
            await message.channel.send("Jeremy's hero #8 is now Lancelot! :fencer: ")
        if message.content == "!ml hero8 add Lesley":
            jehero8 = "Lesley"
            await message.channel.send("Jeremy's hero #8 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero8 add Natalia":
            jehero8 = "Natalia"
            await message.channel.send("Jeremy's hero #8 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero8 add Saber":
            jehero8 = "Saber"
            await message.channel.send("Jeremy's hero #8 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero8 add Selena":
            jehero8 = "Selena"
            await message.channel.send("Jeremy's hero #8 is now Selena! :sleeping:  ")
        if message.content == "!ml hero8 add Alice":
            jehero8 = "Alice"
            await message.channel.send("Jeremy's hero #8 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero8 add Aurora":
            jehero8 = "Aurora"
            await message.channel.send("Jeremy's hero #8 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jehero8 = "Chang'e"
            await message.channel.send("Jeremy's hero #8 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero8 add Cyclops":
            jehero8 = "Cyclops"
            await message.channel.send("Jeremy's hero #8 is now Cyclops! :eye:  ")
        if message.content == "!ml hero8 add Eudora":
            jehero8 = "Eudora"
            await message.channel.send("Jeremy's hero #8 is now Eudora! :zap: ")
        if message.content == "!ml hero8 add Faramis":
            jehero8 = "Faramis"
            await message.channel.send("Jeremy's hero #8 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero8 add Gord":
            jehero8 = "Gord"
            await message.channel.send("Jeremy's hero #8 is now Gord! :snowboarder:")
        if message.content == "!ml hero8 add Harith":
            jehero8 = "Harith"
            await message.channel.send("Jeremy's hero #8 is now Harith! :older_man: ")
        if message.content == "!ml hero8 add Harley":
            jehero8 = "Harley"
            await message.channel.send("Jeremy's hero #8 is now Harley! :tophat: ")
        if message.content == "!ml hero8 add Kadita":
            jehero8 = "Kadita"
            await message.channel.send("Jeremy's hero #8 is now Kadita! :droplet: ")
        if message.content == "!ml hero8 add Kagura":
            jehero8 = "Kagura"
            await message.channel.send("Jeremy's hero #8 is now Kagura! :umbrella8:  ")
        if message.content == "!ml hero8 add Lunox":
            jehero8 = "Lunox"
            await message.channel.send("Jeremy's hero #8 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero8 add Lylia":
            jehero8 = "Lylia"
            await message.channel.send("Jeremy's hero #8 is now Lylia! :boom: ")
        if message.content == "!ml hero8 add Nana":
            jehero8 = "Nana"
            await message.channel.send("Jeremy's hero #8 is now Nana! :cat:  ")
        if message.content == "!ml hero8 add Odette":
            jehero8 = "Odette"
            await message.channel.send("Jeremy's hero #8 is now Odette! :duck: ")
        if message.content == "!ml hero8 add Pharsa":
            jehero8 = "Pharsa"
            await message.channel.send("Jeremy's hero #8 is now Pharsa! :dove:  ")
        if message.content == "!ml hero8 add Vale":
            jehero8 = "Vale"
            await message.channel.send("Jeremy's hero #8 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero8 add Valir":
            jehero8 = "Valir"
            await message.channel.send("Jeremy's hero #8 is now Valir! :fire:")
        if message.content == "!ml hero8 add Vexanna":
            jehero8 = "Vexanna"
            await message.channel.send("Jeremy's hero #8 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero8 add Bruno":
            jehero8 = "Bruno"
            await message.channel.send("Jeremy's hero #8 is now Bruno! :soccer:  ")
        if message.content == "!ml hero8 add Claude":
            jehero8 = "Claude"
            await message.channel.send("Jeremy's hero #8 is now Claude! :monkey:  ")
        if message.content == "!ml hero8 add Clint":
            jehero8 = "Clint"
            await message.channel.send("Jeremy's hero #8 is now Clint! :cowboy: ")
        if message.content == "!ml hero8 add Granger":
            jehero8 = "Granger"
            await message.channel.send("Jeremy's hero #8 is now Granger! :violin: ")
        if message.content == "!ml hero8 add Hanabi":
            jehero8 = "Hanabi"
            await message.channel.send("Jeremy's hero #8 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero8 add Irithel":
            jehero8 = "Irithel"
            await message.channel.send("Jeremy's hero #8 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero8 add Karrie":
            jehero8 = "Karrie"
            await message.channel.send(
                "Jeremy's hero #8 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero8 add Kimmy":
            jehero8 = "Kimmy"
            await message.channel.send("Jeremy's hero #8 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero8 add Layla":
            jehero8 = "Layla"
            await message.channel.send("Jeremy's hero #8 is now Layla! :haircut:  ")
        if message.content == "!ml hero8 add Miya":
            jehero8 = "Miya"
            await message.channel.send("Jeremy's hero #8 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero8 add Moskov":
            jehero8 = "Moskov"
            await message.channel.send("Jeremy's hero #8 is now Moskov! :imp: ")
        if message.content == "!ml hero8 add Yi Sun-Shin":
            jehero8 = "Yi Sun-Shin"
            await message.channel.send("Jeremy's hero #8 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero8 add Angela":
            jehero8 = "Angela"
            await message.channel.send("Jeremy's hero #8 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero8 add Diggie":
            jehero8 = "Diggie"
            await message.channel.send("Jeremy's hero #8 is now Diggie! :owl: ")
        if message.content == "!ml hero8 add Estes":
            jehero8 = "Estes"
            await message.channel.send("Jeremy's hero #8 is now Estes! :ear:  ")
        if message.content == "!ml hero8 add Rafaela":
            jehero8 = "Rafaela"
            await message.channel.send("Jeremy's hero #8 is now Rafaela! :angel: ")
        if message.content == "!ml hero8 add Rynn":
            jehero8 = "Rynn"
            await message.channel.send("Jeremy's hero #8 is now Rynn! ")
        if message.content == "!ml hero9 add Akai":
            global jehero9
            jehero9 = "Akai"
            await message.channel.send("Jeremy's hero #9 is now Akai! :panda_face: ")
        if message.content == "!ml hero9 add Balmond":
            jehero9 = "Balmond"
            await message.channel.send("Jeremy's hero #9 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero9 add Belerick":
            jehero9 = "Belerick"
            await message.channel.send("Jeremy's hero #9 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero9 add Franco":
            jehero9 = "Franco"
            await message.channel.send("Jeremy's hero #9 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero9 add Esmerelda":
            jehero9 = "Esmerelda"
            await message.channel.send("Jeremy's hero #9 is now Esmerelda! :shield: ")
        if message.content == "!ml hero9 add Gatotkaca":
            jehero9 = "Gatotkaca"
            await message.channel.send("Jeremy's hero #9 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero9 add Grock":
            jehero9 = "Grock"
            await message.channel.send("Jeremy's hero #9 is now Grock! :european_castle: ")
        if message.content == "!ml hero9 add Hilda":
            jehero9 = "Hilda"
            await message.channel.send("Jeremy's hero #9 is now Hilda! :runner: ")
        if message.content == "!ml hero9 add Hylos":
            jehero9 = "Hylos"
            await message.channel.send("Jeremy's hero #9 is now Hylos! :unicorn: ")
        if message.content == "!ml hero9 add Johnson":
            jehero9 = "Johnson"
            await message.channel.send("Jeremy's hero #9 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero9 add Khufra":
            jehero9 = "Khufra"
            await message.channel.send("Jeremy's hero #9 is now Khufra! :clown: ")
        if message.content == "!ml hero9 add Lolita":
            jehero9 = "Lolita"
            await message.channel.send("Jeremy's hero #9 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jehero9 = "Masha"
            await message.channel.send("Jeremy's hero #9 is now Masha! :bear: ")
        if message.content == "!ml hero9 add Minotaur":
            jehero9 = "Minotaur"
            await message.channel.send("Jeremy's hero #9 is now Minotaur! :cow: ")
        if message.content == "!ml hero9 add Tigreal":
            jehero9 = "Tigreal"
            await message.channel.send("Jeremy's hero #9 is now Tigreal! :moyai: ")
        if message.content == "!ml hero9 add Uranus":
            jehero9 = "Uranus"
            await message.channel.send("Jeremy's hero #9 is now Uranus! :peach: ")
        if message.content == "!ml hero9 add X.Borg":
            jehero9 = "X.Borg"
            await message.channel.send("Jeremy's hero #9 is now X.Borg! :fire: ")
        if message.content == "!ml hero9 add Aldous":
            jehero9 = "Aldous"
            await message.channel.send("Jeremy's hero #9 is now Aldous! :fist: ")
        if message.content == "!ml hero9 add Alpha":
            jehero9 = "Alpha"
            await message.channel.send("Jeremy's hero #9 is now Alpha! :airplane: ")
        if message.content == "!ml hero9 add Alucard":
            jehero9 = "Alucard"
            await message.channel.send("Jeremy's hero #9 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero9 add Argus":
            jehero9 = "Argus"
            await message.channel.send("Jeremy's hero #9 is now Argus! :angel: ")
        if message.content == "!ml hero9 add Badang":
            jehero9 = "Badang"
            await message.channel.send("Jeremy's hero #9 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero9 add Bane":
            jehero9 = "Bane"
            await message.channel.send("Jeremy's hero #9 is now Bane! :octopus: ")
        if message.content == "!ml hero9 add Chou":
            jehero9 = "Chou"
            await message.channel.send("Jeremy's hero #9 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero9 add Dyrroth":
            jehero9 = "Dyrroth"
            await message.channel.send("Jeremy's hero #9 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero9 add Freya":
            jehero9 = "Freya"
            await message.channel.send("Jeremy's hero #9 is now Freya! :hammer: ")
        if message.content == "!ml hero9 add Guinevere":
            jehero9 = "Guinevere"
            await message.channel.send("Jeremy's hero #9 is now Guinevere! :dress:  ")
        if message.content == "!ml hero9 add Jawhead":
            jehero9 = "Jawhead"
            await message.channel.send("Jeremy's hero #9 is now Jawhead! :robot: ")
        if message.content == "!ml hero9 add Kaja":
            jehero9 = "Kaja"
            await message.channel.send("Jeremy's hero #9 is now Kaja! :bird: ")
        if message.content == "!ml hero9 add Lapu-Lapu":
            jehero9 = "Lapu-Lapu"
            await message.channel.send("Jeremy's hero #9 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero9 add Leomord":
            jehero9 = "Leomord"
            await message.channel.send("Jeremy's hero #9 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero9 add Martis":
            jehero9 = "Martis"
            await message.channel.send("Jeremy's hero #9 is now Martis! :crab: ")
        if message.content == "!ml hero9 add Minsitthar":
            jehero9 = "Minsitthar"
            await message.channel.send("Jeremy's hero #9 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero9 add Roger":
            jehero9 = "Roger"
            await message.channel.send("Jeremy's hero #9 is now Roger! :wolf: ")
        if message.content == "!ml hero9 add Ruby":
            jehero9 = "Ruby"
            await message.channel.send("Jeremy's hero #9 is now Ruby! :heart: ")
        if message.content == "!ml hero9 add Sun":
            jehero9 = "Sun"
            await message.channel.send("Jeremy's hero #9 is now Sun! :monkey_face: ")
        if message.content == "!ml hero9 add Thamuz":
            jehero9 = "Thamuz"
            await message.channel.send("Jeremy's hero #9 is now Thamuz! :rage: ")
        if message.content == "!ml hero9 add Terizla":
            jehero9 = "Terizla"
            await message.channel.send("Jeremy's hero #9 is now Terizla! :hammer: ")
        if message.content == "!ml hero9 add Zilong":
            jehero9 = "Zilong"
            await message.channel.send("Jeremy's hero #9 is now Zilong! :dragon: ")
        if message.content == "!ml hero9 add Fanny":
            jehero9 = "Fanny"
            await message.channel.send("Jeremy's hero #9 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero9 add Gusion":
            jehero9 = "Gusion"
            await message.channel.send(
                "Jeremy's hero #9 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero9 add Hanzo":
            jehero9 = "Hanzo"
            await message.channel.send("Jeremy's hero #9 is now Hanzo! :ghost: ")
        if message.content == "!ml hero9 add Hayabusa":
            jehero9 = "Hayabusa"
            await message.channel.send("Jeremy's hero #9 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero9 add Helcurt":
            jehero9 = "Helcurt"
            await message.channel.send("Jeremy's hero #9 is now Helcurt! :mute:  ")
        if message.content == "!ml hero9 add Karina":
            jehero9 = "Karina"
            await message.channel.send("Jeremy's hero #9 is now Karina! :purple_heart: ")
        if message.content == "!ml hero9 add Lancelot":
            jehero9 = "Lancelot"
            await message.channel.send("Jeremy's hero #9 is now Lancelot! :fencer: ")
        if message.content == "!ml hero9 add Lesley":
            jehero9 = "Lesley"
            await message.channel.send("Jeremy's hero #9 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero9 add Natalia":
            jehero9 = "Natalia"
            await message.channel.send("Jeremy's hero #9 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero9 add Saber":
            jehero9 = "Saber"
            await message.channel.send("Jeremy's hero #9 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero9 add Selena":
            jehero9 = "Selena"
            await message.channel.send("Jeremy's hero #9 is now Selena! :sleeping:  ")
        if message.content == "!ml hero9 add Alice":
            jehero9 = "Alice"
            await message.channel.send("Jeremy's hero #9 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero9 add Aurora":
            jehero9 = "Aurora"
            await message.channel.send("Jeremy's hero #9 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jehero9 = "Chang'e"
            await message.channel.send("Jeremy's hero #9 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero9 add Cyclops":
            jehero9 = "Cyclops"
            await message.channel.send("Jeremy's hero #9 is now Cyclops! :eye:  ")
        if message.content == "!ml hero9 add Eudora":
            jehero9 = "Eudora"
            await message.channel.send("Jeremy's hero #9 is now Eudora! :zap: ")
        if message.content == "!ml hero9 add Faramis":
            jehero9 = "Faramis"
            await message.channel.send("Jeremy's hero #9 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero9 add Gord":
            jehero9 = "Gord"
            await message.channel.send("Jeremy's hero #9 is now Gord! :snowboarder:")
        if message.content == "!ml hero9 add Harith":
            jehero9 = "Harith"
            await message.channel.send("Jeremy's hero #9 is now Harith! :older_man: ")
        if message.content == "!ml hero9 add Harley":
            jehero9 = "Harley"
            await message.channel.send("Jeremy's hero #9 is now Harley! :tophat: ")
        if message.content == "!ml hero9 add Kadita":
            jehero9 = "Kadita"
            await message.channel.send("Jeremy's hero #9 is now Kadita! :droplet: ")
        if message.content == "!ml hero9 add Kagura":
            jehero9 = "Kagura"
            await message.channel.send("Jeremy's hero #9 is now Kagura! :umbrella9:  ")
        if message.content == "!ml hero9 add Lunox":
            jehero9 = "Lunox"
            await message.channel.send("Jeremy's hero #9 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero9 add Lylia":
            jehero9 = "Lylia"
            await message.channel.send("Jeremy's hero #9 is now Lylia! :boom: ")
        if message.content == "!ml hero9 add Nana":
            jehero9 = "Nana"
            await message.channel.send("Jeremy's hero #9 is now Nana! :cat:  ")
        if message.content == "!ml hero9 add Odette":
            jehero9 = "Odette"
            await message.channel.send("Jeremy's hero #9 is now Odette! :duck: ")
        if message.content == "!ml hero9 add Pharsa":
            jehero9 = "Pharsa"
            await message.channel.send("Jeremy's hero #9 is now Pharsa! :dove:  ")
        if message.content == "!ml hero9 add Vale":
            jehero9 = "Vale"
            await message.channel.send("Jeremy's hero #9 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero9 add Valir":
            jehero9 = "Valir"
            await message.channel.send("Jeremy's hero #9 is now Valir! :fire:")
        if message.content == "!ml hero9 add Vexanna":
            jehero9 = "Vexanna"
            await message.channel.send("Jeremy's hero #9 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero9 add Bruno":
            jehero9 = "Bruno"
            await message.channel.send("Jeremy's hero #9 is now Bruno! :soccer:  ")
        if message.content == "!ml hero9 add Claude":
            jehero9 = "Claude"
            await message.channel.send("Jeremy's hero #9 is now Claude! :monkey:  ")
        if message.content == "!ml hero9 add Clint":
            jehero9 = "Clint"
            await message.channel.send("Jeremy's hero #9 is now Clint! :cowboy: ")
        if message.content == "!ml hero9 add Granger":
            jehero9 = "Granger"
            await message.channel.send("Jeremy's hero #9 is now Granger! :violin: ")
        if message.content == "!ml hero9 add Hanabi":
            jehero9 = "Hanabi"
            await message.channel.send("Jeremy's hero #9 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero9 add Irithel":
            jehero9 = "Irithel"
            await message.channel.send("Jeremy's hero #9 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero9 add Karrie":
            jehero9 = "Karrie"
            await message.channel.send(
                "Jeremy's hero #9 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero9 add Kimmy":
            jehero9 = "Kimmy"
            await message.channel.send("Jeremy's hero #9 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero9 add Layla":
            jehero9 = "Layla"
            await message.channel.send("Jeremy's hero #9 is now Layla! :haircut:  ")
        if message.content == "!ml hero9 add Miya":
            jehero9 = "Miya"
            await message.channel.send("Jeremy's hero #9 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero9 add Moskov":
            jehero9 = "Moskov"
            await message.channel.send("Jeremy's hero #9 is now Moskov! :imp: ")
        if message.content == "!ml hero9 add Yi Sun-Shin":
            jehero9 = "Yi Sun-Shin"
            await message.channel.send("Jeremy's hero #9 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero9 add Angela":
            jehero9 = "Angela"
            await message.channel.send("Jeremy's hero #9 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero9 add Diggie":
            jehero9 = "Diggie"
            await message.channel.send("Jeremy's hero #9 is now Diggie! :owl: ")
        if message.content == "!ml hero9 add Estes":
            jehero9 = "Estes"
            await message.channel.send("Jeremy's hero #9 is now Estes! :ear:  ")
        if message.content == "!ml hero9 add Rafaela":
            jehero9 = "Rafaela"
            await message.channel.send("Jeremy's hero #9 is now Rafaela! :angel: ")
        if message.content == "!ml hero9 add Rynn":
            jehero9 = "Rynn"
            await message.channel.send("Jeremy's hero #9 is now Rynn! ")
        if message.content == "!ml hero10 add Akai":
            global jehero10
            jehero10 = "Akai"
            await message.channel.send("Jeremy's hero #10 is now Akai! :panda_face: ")
        if message.content == "!ml hero10 add Balmond":
            jehero10 = "Balmond"
            await message.channel.send("Jeremy's hero #10 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero10 add Belerick":
            jehero10 = "Belerick"
            await message.channel.send("Jeremy's hero #10 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero10 add Franco":
            jehero10 = "Franco"
            await message.channel.send("Jeremy's hero #10 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero10 add Esmerelda":
            jehero10 = "Esmerelda"
            await message.channel.send("Jeremy's hero #10 is now Esmerelda! :shield: ")
        if message.content == "!ml hero10 add Gatotkaca":
            jehero10 = "Gatotkaca"
            await message.channel.send("Jeremy's hero #10 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero10 add Grock":
            jehero10 = "Grock"
            await message.channel.send("Jeremy's hero #10 is now Grock! :european_castle: ")
        if message.content == "!ml hero10 add Hilda":
            jehero10 = "Hilda"
            await message.channel.send("Jeremy's hero #10 is now Hilda! :runner: ")
        if message.content == "!ml hero10 add Hylos":
            jehero10 = "Hylos"
            await message.channel.send("Jeremy's hero #10 is now Hylos! :unicorn: ")
        if message.content == "!ml hero10 add Johnson":
            jehero10 = "Johnson"
            await message.channel.send("Jeremy's hero #10 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero10 add Khufra":
            jehero10 = "Khufra"
            await message.channel.send("Jeremy's hero #10 is now Khufra! :clown: ")
        if message.content == "!ml hero10 add Lolita":
            jehero10 = "Lolita"
            await message.channel.send("Jeremy's hero #10 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            jehero10 = "Masha"
            await message.channel.send("Jeremy's hero #10 is now Masha! :bear: ")
        if message.content == "!ml hero10 add Minotaur":
            jehero10 = "Minotaur"
            await message.channel.send("Jeremy's hero #10 is now Minotaur! :cow: ")
        if message.content == "!ml hero10 add Tigreal":
            jehero10 = "Tigreal"
            await message.channel.send("Jeremy's hero #10 is now Tigreal! :moyai: ")
        if message.content == "!ml hero10 add Uranus":
            jehero10 = "Uranus"
            await message.channel.send("Jeremy's hero #10 is now Uranus! :peach: ")
        if message.content == "!ml hero10 add X.Borg":
            jehero10 = "X.Borg"
            await message.channel.send("Jeremy's hero #10 is now X.Borg! :fire: ")
        if message.content == "!ml hero10 add Aldous":
            jehero10 = "Aldous"
            await message.channel.send("Jeremy's hero #10 is now Aldous! :fist: ")
        if message.content == "!ml hero10 add Alpha":
            jehero10 = "Alpha"
            await message.channel.send("Jeremy's hero #10 is now Alpha! :airplane: ")
        if message.content == "!ml hero10 add Alucard":
            jehero10 = "Alucard"
            await message.channel.send("Jeremy's hero #10 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero10 add Argus":
            jehero10 = "Argus"
            await message.channel.send("Jeremy's hero #10 is now Argus! :angel: ")
        if message.content == "!ml hero10 add Badang":
            jehero10 = "Badang"
            await message.channel.send("Jeremy's hero #10 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero10 add Bane":
            jehero10 = "Bane"
            await message.channel.send("Jeremy's hero #10 is now Bane! :octopus: ")
        if message.content == "!ml hero10 add Chou":
            jehero10 = "Chou"
            await message.channel.send("Jeremy's hero #10 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero10 add Dyrroth":
            jehero10 = "Dyrroth"
            await message.channel.send("Jeremy's hero #10 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero10 add Freya":
            jehero10 = "Freya"
            await message.channel.send("Jeremy's hero #10 is now Freya! :hammer: ")
        if message.content == "!ml hero10 add Guinevere":
            jehero10 = "Guinevere"
            await message.channel.send("Jeremy's hero #10 is now Guinevere! :dress:  ")
        if message.content == "!ml hero10 add Jawhead":
            jehero10 = "Jawhead"
            await message.channel.send("Jeremy's hero #10 is now Jawhead! :robot: ")
        if message.content == "!ml hero10 add Kaja":
            jehero10 = "Kaja"
            await message.channel.send("Jeremy's hero #10 is now Kaja! :bird: ")
        if message.content == "!ml hero10 add Lapu-Lapu":
            jehero10 = "Lapu-Lapu"
            await message.channel.send("Jeremy's hero #10 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero10 add Leomord":
            jehero10 = "Leomord"
            await message.channel.send("Jeremy's hero #10 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero10 add Martis":
            jehero10 = "Martis"
            await message.channel.send("Jeremy's hero #10 is now Martis! :crab: ")
        if message.content == "!ml hero10 add Minsitthar":
            jehero10 = "Minsitthar"
            await message.channel.send("Jeremy's hero #10 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero10 add Roger":
            jehero10 = "Roger"
            await message.channel.send("Jeremy's hero #10 is now Roger! :wolf: ")
        if message.content == "!ml hero10 add Ruby":
            jehero10 = "Ruby"
            await message.channel.send("Jeremy's hero #10 is now Ruby! :heart: ")
        if message.content == "!ml hero10 add Sun":
            jehero10 = "Sun"
            await message.channel.send("Jeremy's hero #10 is now Sun! :monkey_face: ")
        if message.content == "!ml hero10 add Thamuz":
            jehero10 = "Thamuz"
            await message.channel.send("Jeremy's hero #10 is now Thamuz! :rage: ")
        if message.content == "!ml hero10 add Terizla":
            jehero10 = "Terizla"
            await message.channel.send("Jeremy's hero #10 is now Terizla! :hammer: ")
        if message.content == "!ml hero10 add Zilong":
            jehero10 = "Zilong"
            await message.channel.send("Jeremy's hero #10 is now Zilong! :dragon: ")
        if message.content == "!ml hero10 add Fanny":
            jehero10 = "Fanny"
            await message.channel.send("Jeremy's hero #10 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero10 add Gusion":
            jehero10 = "Gusion"
            await message.channel.send(
                "Jeremy's hero #10 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero10 add Hanzo":
            jehero10 = "Hanzo"
            await message.channel.send("Jeremy's hero #10 is now Hanzo! :ghost: ")
        if message.content == "!ml hero10 add Hayabusa":
            jehero10 = "Hayabusa"
            await message.channel.send("Jeremy's hero #10 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero10 add Helcurt":
            jehero10 = "Helcurt"
            await message.channel.send("Jeremy's hero #10 is now Helcurt! :mute:  ")
        if message.content == "!ml hero10 add Karina":
            jehero10 = "Karina"
            await message.channel.send("Jeremy's hero #10 is now Karina! :purple_heart: ")
        if message.content == "!ml hero10 add Lancelot":
            jehero10 = "Lancelot"
            await message.channel.send("Jeremy's hero #10 is now Lancelot! :fencer: ")
        if message.content == "!ml hero10 add Lesley":
            jehero10 = "Lesley"
            await message.channel.send("Jeremy's hero #10 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero10 add Natalia":
            jehero10 = "Natalia"
            await message.channel.send("Jeremy's hero #10 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero10 add Saber":
            jehero10 = "Saber"
            await message.channel.send("Jeremy's hero #10 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero10 add Selena":
            jehero10 = "Selena"
            await message.channel.send("Jeremy's hero #10 is now Selena! :sleeping:  ")
        if message.content == "!ml hero10 add Alice":
            jehero10 = "Alice"
            await message.channel.send("Jeremy's hero #10 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero10 add Aurora":
            jehero10 = "Aurora"
            await message.channel.send("Jeremy's hero #10 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            jehero10 = "Chang'e"
            await message.channel.send("Jeremy's hero #10 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero10 add Cyclops":
            jehero10 = "Cyclops"
            await message.channel.send("Jeremy's hero #10 is now Cyclops! :eye:  ")
        if message.content == "!ml hero10 add Eudora":
            jehero10 = "Eudora"
            await message.channel.send("Jeremy's hero #10 is now Eudora! :zap: ")
        if message.content == "!ml hero10 add Faramis":
            jehero10 = "Faramis"
            await message.channel.send("Jeremy's hero #10 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero10 add Gord":
            jehero10 = "Gord"
            await message.channel.send("Jeremy's hero #10 is now Gord! :snowboarder:")
        if message.content == "!ml hero10 add Harith":
            jehero10 = "Harith"
            await message.channel.send("Jeremy's hero #10 is now Harith! :older_man: ")
        if message.content == "!ml hero10 add Harley":
            jehero10 = "Harley"
            await message.channel.send("Jeremy's hero #10 is now Harley! :tophat: ")
        if message.content == "!ml hero10 add Kadita":
            jehero10 = "Kadita"
            await message.channel.send("Jeremy's hero #10 is now Kadita! :droplet: ")
        if message.content == "!ml hero10 add Kagura":
            jehero10 = "Kagura"
            await message.channel.send("Jeremy's hero #10 is now Kagura! :umbrella10:  ")
        if message.content == "!ml hero10 add Lunox":
            jehero10 = "Lunox"
            await message.channel.send("Jeremy's hero #10 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero10 add Lylia":
            jehero10 = "Lylia"
            await message.channel.send("Jeremy's hero #10 is now Lylia! :boom: ")
        if message.content == "!ml hero10 add Nana":
            jehero10 = "Nana"
            await message.channel.send("Jeremy's hero #10 is now Nana! :cat:  ")
        if message.content == "!ml hero10 add Odette":
            jehero10 = "Odette"
            await message.channel.send("Jeremy's hero #10 is now Odette! :duck: ")
        if message.content == "!ml hero10 add Pharsa":
            jehero10 = "Pharsa"
            await message.channel.send("Jeremy's hero #10 is now Pharsa! :dove:  ")
        if message.content == "!ml hero10 add Vale":
            jehero10 = "Vale"
            await message.channel.send("Jeremy's hero #10 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero10 add Valir":
            jehero10 = "Valir"
            await message.channel.send("Jeremy's hero #10 is now Valir! :fire:")
        if message.content == "!ml hero10 add Vexanna":
            jehero10 = "Vexanna"
            await message.channel.send("Jeremy's hero #10 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero10 add Bruno":
            jehero10 = "Bruno"
            await message.channel.send("Jeremy's hero #10 is now Bruno! :soccer:  ")
        if message.content == "!ml hero10 add Claude":
            jehero10 = "Claude"
            await message.channel.send("Jeremy's hero #10 is now Claude! :monkey:  ")
        if message.content == "!ml hero10 add Clint":
            jehero10 = "Clint"
            await message.channel.send("Jeremy's hero #10 is now Clint! :cowboy: ")
        if message.content == "!ml hero10 add Granger":
            jehero10 = "Granger"
            await message.channel.send("Jeremy's hero #10 is now Granger! :violin: ")
        if message.content == "!ml hero10 add Hanabi":
            jehero10 = "Hanabi"
            await message.channel.send("Jeremy's hero #10 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero10 add Irithel":
            jehero10 = "Irithel"
            await message.channel.send("Jeremy's hero #10 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero10 add Karrie":
            jehero10 = "Karrie"
            await message.channel.send(
                "Jeremy's hero #10 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero10 add Kimmy":
            jehero10 = "Kimmy"
            await message.channel.send("Jeremy's hero #10 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero10 add Layla":
            jehero10 = "Layla"
            await message.channel.send("Jeremy's hero #10 is now Layla! :haircut:  ")
        if message.content == "!ml hero10 add Miya":
            jehero10 = "Miya"
            await message.channel.send("Jeremy's hero #10 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero10 add Moskov":
            jehero10 = "Moskov"
            await message.channel.send("Jeremy's hero #10 is now Moskov! :imp: ")
        if message.content == "!ml hero10 add Yi Sun-Shin":
            jehero10 = "Yi Sun-Shin"
            await message.channel.send("Jeremy's hero #10 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero10 add Angela":
            jehero10 = "Angela"
            await message.channel.send("Jeremy's hero #10 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero10 add Diggie":
            jehero10 = "Diggie"
            await message.channel.send("Jeremy's hero #10 is now Diggie! :owl: ")
        if message.content == "!ml hero10 add Estes":
            jehero10 = "Estes"
            await message.channel.send("Jeremy's hero #10 is now Estes! :ear:  ")
        if message.content == "!ml hero10 add Rafaela":
            jehero10 = "Rafaela"
            await message.channel.send("Jeremy's hero #10 is now Rafaela! :angel: ")
        if message.content == "!ml hero10 add Rynn":
            jehero10 = "Rynn"
            await message.channel.send("Jeremy's hero #10 is now Rynn! ")
        if message.content == "!ml hero1 clear":
            jehero1 = "Not Chosen"
            await message.channel.send("Jeremy's hero #1 slot has been cleared!")
        if message.content == "!ml hero2 clear":
            jehero2 = "Not Chosen"
            await message.channel.send("Jeremy's hero #2 slot has been cleared!")
        if message.content == "!ml hero3 clear":
            jehero3 = "Not Chosen"
            await message.channel.send("Jeremy's hero #3 slot has been cleared!")
        if message.content == "!ml hero3 clear":
            jehero3 = "Not Chosen"
            await message.channel.send("Jeremy's hero #3 slot has been cleared!")
        if message.content == "!ml hero4 clear":
            jehero4 = "Not Chosen"
            await message.channel.send("Jeremy's hero #4 slot has been cleared!")
        if message.content == "!ml hero5 clear":
            jehero5 = "Not Chosen"
            await message.channel.send("Jeremy's hero #5 slot has been cleared!")
        if message.content == "!ml hero6 clear":
            jehero6 = "Not Chosen"
            await message.channel.send("Jeremy's hero #6 slot has been cleared!")
        if message.content == "!ml hero7 clear":
            jehero7 = "Not Chosen"
            await message.channel.send("Jeremy's hero #7 slot has been cleared!")
        if message.content == "!ml hero8 clear":
            jehero8 = "Not Chosen"
            await message.channel.send("Jeremy's hero #8 slot has been cleared!")
        if message.content == "!ml hero9 clear":
            jehero9 = "Not Chosen"
            await message.channel.send("Jeremy's hero #9 slot has been cleared!")
        if message.content == "!ml hero10 clear":
            jehero10 = "Not Chosen"
            await message.channel.send("Jeremy's hero #10 slot has been cleared!")
        if message.content == "!ml hlist Jeremy":
            jeembed = discord.Embed(title="Heroes Jeremy Plays",
                                    description="Here are the top 10 heroes Jeremy is willing to play in ranked")
            jeembed.add_field(name="1", value=jehero1)
            jeembed.add_field(name="2", value=jehero2)
            jeembed.add_field(name="3", value=jehero3)
            jeembed.add_field(name="4", value=jehero4)
            jeembed.add_field(name="5", value=jehero5)
            jeembed.add_field(name="6", value=jehero6)
            jeembed.add_field(name="7", value=jehero7)
            jeembed.add_field(name="8", value=jehero8)
            jeembed.add_field(name="9", value=jehero9)
            jeembed.add_field(name="10", value=jehero10)
            await message.channel.send(content=None, embed=jeembed)
    if str(message.channel) not in clean_channels and str(message.author) in Matthew_Hlist:
        if message.content.find("hello") != -1:
            await message.channel.send("Hey Matthew, how are you?")
        if message.content.find("!gay") != -1:
            await message.channel.send("Wow, the man with the girlfriend is gay? HMMMM????")
        if message.content.find("!nigga") != -1:
            await message.channel.send(":moyai:")
        if message.content.find("nigga") != -1:
            global nwmoyaichance
            global nwmoyaibonus
            global nwmoyaitotal
            nwmoyaichance = random.randrange(0, 20, 1)
            nwmoyaitotal = nwmoyaichance + nwmoyaibonus
            if nwmoyaitotal > 15:
                await message.channel.send(":moyai:")
                nwmoyaitotal = 0
                nwmoyaichance = 0
                nwmoyaibonus = 0
            else:
                nwmoyaibonus += 1
                nwmoyaitotal = 0
                nwmoyaichance = 0
            nwordcount
            nwordcount += 1
        if message.content.find("Nigga") != -1:
            nwmoyaichance = random.randrange(0, 20, 1)
            nwmoyaitotal = nwmoyaichance + nwmoyaibonus
            if nwmoyaitotal > 15:
                await message.channel.send(":moyai:")
                nwmoyaitotal = 0
                nwmoyaichance = 0
                nwmoyaibonus = 0
            else:
                nwmoyaibonus += 1
                nwmoyaitotal = 0
                nwmoyaichance = 0
            nwordcount
            nwordcount += 1
        if message.content.find("NIGGA") != -1:
            nwmoyaichance = random.randrange(0, 20, 1)
            nwmoyaitotal = nwmoyaichance + nwmoyaibonus
            if nwmoyaitotal > 15:
                await message.channel.send(":moyai:")
                nwmoyaitotal = 0
                nwmoyaichance = 0
                nwmoyaibonus = 0
            else:
                nwmoyaibonus += 1
                nwmoyaitotal = 0
                nwmoyaichance = 0
            nwordcount
            nwordcount += 2
        if message.content.find("nigger") != -1:
            nwmoyaichance = random.randrange(0, 20, 1)
            nwmoyaitotal = nwmoyaichance + nwmoyaibonus
            if nwmoyaitotal > 15:
                await message.channel.send(":moyai:")
                nwmoyaitotal = 0
                nwmoyaichance = 0
                nwmoyaibonus = 0
            else:
                nwmoyaibonus += 2
                nwmoyaitotal = 0
                nwmoyaichance = 0
            nwordcount
            nwordcount += 2
        if message.content.find("Nigger") != -1:
            nwmoyaichance = random.randrange(0, 20, 1)
            nwmoyaitotal = nwmoyaichance + nwmoyaibonus
            if nwmoyaitotal > 15:
                await message.channel.send(":moyai:")
                nwmoyaitotal = 0
                nwmoyaichance = 0
                nwmoyaibonus = 0
            else:
                nwmoyaibonus += 2
                nwmoyaitotal = 0
                nwmoyaichance = 0
            nwordcount
            nwordcount += 2
        if message.content.find("NIGGER") != -1:
            nwmoyaichance = random.randrange(0, 20, 1)
            nwmoyaitotal = nwmoyaichance + nwmoyaibonus
            if nwmoyaitotal > 15:
                await message.channel.send(":moyai:")
                nwmoyaitotal = 0
                nwmoyaichance = 0
                nwmoyaibonus = 0
            else:
                nwmoyaibonus += 2
                nwmoyaitotal = 0
                nwmoyaichance = 0
            nwordcount
            nwordcount += 3
        if message.content == "!ml hero1 add Akai":
            global mahero1
            mahero1 = "Akai"
            await message.channel.send("Matthew's hero #1 is now Akai! :panda_face: ")
        if message.content == "!ml hero1 add Balmond":
            mahero1 = "Balmond"
            await message.channel.send("Matthew's hero #1 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero1 add Belerick":
            mahero1 = "Belerick"
            await message.channel.send("Matthew's hero #1 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero1 add Franco":
            mahero1 = "Franco"
            await message.channel.send("Matthew's hero #1 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero1 add Esmerelda":
            mahero1 = "Esmerelda"
            await message.channel.send("Matthew's hero #1 is now Esmerelda! :shield: ")
        if message.content == "!ml hero1 add Gatotkaca":
            mahero1 = "Gatotkaca"
            await message.channel.send("Matthew's hero #1 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero1 add Grock":
            mahero1 = "Grock"
            await message.channel.send("Matthew's hero #1 is now Grock! :european_castle: ")
        if message.content == "!ml hero1 add Hilda":
            mahero1 = "Hilda"
            await message.channel.send("Matthew's hero #1 is now Hilda! :runner: ")
        if message.content == "!ml hero1 add Hylos":
            mahero1 = "Hylos"
            await message.channel.send("Matthew's hero #1 is now Hylos! :unicorn: ")
        if message.content == "!ml hero1 add Johnson":
            mahero1 = "Johnson"
            await message.channel.send("Matthew's hero #1 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero1 add Khufra":
            mahero1 = "Khufra"
            await message.channel.send("Matthew's hero #1 is now Khufra! :clown: ")
        if message.content == "!ml hero1 add Lolita":
            mahero1 = "Lolita"
            await message.channel.send("Matthew's hero #1 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            mahero1 = "Masha"
            await message.channel.send("Matthew's hero #1 is now Masha! :bear: ")
        if message.content == "!ml hero1 add Minotaur":
            mahero1 = "Minotaur"
            await message.channel.send("Matthew's hero #1 is now Minotaur! :cow: ")
        if message.content == "!ml hero1 add Tigreal":
            mahero1 = "Tigreal"
            await message.channel.send("Matthew's hero #1 is now Tigreal! :moyai: ")
        if message.content == "!ml hero1 add Uranus":
            mahero1 = "Uranus"
            await message.channel.send("Matthew's hero #1 is now Uranus! :peach: ")
        if message.content == "!ml hero1 add X.Borg":
            mahero1 = "X.Borg"
            await message.channel.send("Matthew's hero #1 is now X.Borg! :fire: ")
        if message.content == "!ml hero1 add Aldous":
            mahero1 = "Aldous"
            await message.channel.send("Matthew's hero #1 is now Aldous! :fist: ")
        if message.content == "!ml hero1 add Alpha":
            mahero1 = "Alpha"
            await message.channel.send("Matthew's hero #1 is now Alpha! :airplane: ")
        if message.content == "!ml hero1 add Alucard":
            mahero1 = "Alucard"
            await message.channel.send("Matthew's hero #1 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero1 add Argus":
            mahero1 = "Argus"
            await message.channel.send("Matthew's hero #1 is now Argus! :angel: ")
        if message.content == "!ml hero1 add Badang":
            mahero1 = "Badang"
            await message.channel.send("Matthew's hero #1 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero1 add Bane":
            mahero1 = "Bane"
            await message.channel.send("Matthew's hero #1 is now Bane! :octopus: ")
        if message.content == "!ml hero1 add Chou":
            mahero1 = "Chou"
            await message.channel.send("Matthew's hero #1 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero1 add Dyrroth":
            mahero1 = "Dyrroth"
            await message.channel.send("Matthew's hero #1 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero1 add Freya":
            mahero1 = "Freya"
            await message.channel.send("Matthew's hero #1 is now Freya! :hammer: ")
        if message.content == "!ml hero1 add Guinevere":
            mahero1 = "Guinevere"
            await message.channel.send("Matthew's hero #1 is now Guinevere! :dress:  ")
        if message.content == "!ml hero1 add Jawhead":
            mahero1 = "Jawhead"
            await message.channel.send("Matthew's hero #1 is now Jawhead! :robot: ")
        if message.content == "!ml hero1 add Kaja":
            mahero1 = "Kaja"
            await message.channel.send("Matthew's hero #1 is now Kaja! :bird: ")
        if message.content == "!ml hero1 add Lapu-Lapu":
            mahero1 = "Lapu-Lapu"
            await message.channel.send("Matthew's hero #1 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero1 add Leomord":
            mahero1 = "Leomord"
            await message.channel.send("Matthew's hero #1 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero1 add Martis":
            mahero1 = "Martis"
            await message.channel.send("Matthew's hero #1 is now Martis! :crab: ")
        if message.content == "!ml hero1 add Minsitthar":
            mahero1 = "Minsitthar"
            await message.channel.send("Matthew's hero #1 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero1 add Roger":
            mahero1 = "Roger"
            await message.channel.send("Matthew's hero #1 is now Roger! :wolf: ")
        if message.content == "!ml hero1 add Ruby":
            mahero1 = "Ruby"
            await message.channel.send("Matthew's hero #1 is now Ruby! :heart: ")
        if message.content == "!ml hero1 add Sun":
            mahero1 = "Sun"
            await message.channel.send("Matthew's hero #1 is now Sun! :monkey_face: ")
        if message.content == "!ml hero1 add Thamuz":
            mahero1 = "Thamuz"
            await message.channel.send("Matthew's hero #1 is now Thamuz! :rage: ")
        if message.content == "!ml hero1 add Terizla":
            mahero1 = "Terizla"
            await message.channel.send("Matthew's hero #1 is now Terizla! :hammer: ")
        if message.content == "!ml hero1 add Zilong":
            mahero1 = "Zilong"
            await message.channel.send("Matthew's hero #1 is now Zilong! :dragon: ")
        if message.content == "!ml hero1 add Fanny":
            mahero1 = "Fanny"
            await message.channel.send("Matthew's hero #1 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero1 add Gusion":
            mahero1 = "Gusion"
            await message.channel.send(
                "Matthew's hero #1 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero1 add Hanzo":
            mahero1 = "Hanzo"
            await message.channel.send("Matthew's hero #1 is now Hanzo! :ghost: ")
        if message.content == "!ml hero1 add Hayabusa":
            mahero1 = "Hayabusa"
            await message.channel.send("Matthew's hero #1 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero1 add Helcurt":
            mahero1 = "Helcurt"
            await message.channel.send("Matthew's hero #1 is now Helcurt! :mute:  ")
        if message.content == "!ml hero1 add Karina":
            mahero1 = "Karina"
            await message.channel.send("Matthew's hero #1 is now Karina! :purple_heart: ")
        if message.content == "!ml hero1 add Lancelot":
            mahero1 = "Lancelot"
            await message.channel.send("Matthew's hero #1 is now Lancelot! :fencer: ")
        if message.content == "!ml hero1 add Lesley":
            mahero1 = "Lesley"
            await message.channel.send("Matthew's hero #1 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero1 add Natalia":
            mahero1 = "Natalia"
            await message.channel.send("Matthew's hero #1 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero1 add Saber":
            mahero1 = "Saber"
            await message.channel.send("Matthew's hero #1 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero1 add Selena":
            mahero1 = "Selena"
            await message.channel.send("Matthew's hero #1 is now Selena! :sleeping:  ")
        if message.content == "!ml hero1 add Alice":
            mahero1 = "Alice"
            await message.channel.send("Matthew's hero #1 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero1 add Aurora":
            mahero1 = "Aurora"
            await message.channel.send("Matthew's hero #1 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            mahero1 = "Chang'e"
            await message.channel.send("Matthew's hero #1 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero1 add Cyclops":
            mahero1 = "Cyclops"
            await message.channel.send("Matthew's hero #1 is now Cyclops! :eye:  ")
        if message.content == "!ml hero1 add Eudora":
            mahero1 = "Eudora"
            await message.channel.send("Matthew's hero #1 is now Eudora! :zap: ")
        if message.content == "!ml hero1 add Faramis":
            mahero1 = "Faramis"
            await message.channel.send("Matthew's hero #1 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero1 add Gord":
            mahero1 = "Gord"
            await message.channel.send("Matthew's hero #1 is now Gord! :snowboarder:")
        if message.content == "!ml hero1 add Harith":
            mahero1 = "Harith"
            await message.channel.send("Matthew's hero #1 is now Harith! :older_man: ")
        if message.content == "!ml hero1 add Harley":
            mahero1 = "Harley"
            await message.channel.send("Matthew's hero #1 is now Harley! :tophat: ")
        if message.content == "!ml hero1 add Kadita":
            mahero1 = "Kadita"
            await message.channel.send("Matthew's hero #1 is now Kadita! :droplet: ")
        if message.content == "!ml hero1 add Kagura":
            mahero1 = "Kagura"
            await message.channel.send("Matthew's hero #1 is now Kagura! :umbrella2:  ")
        if message.content == "!ml hero1 add Lunox":
            mahero1 = "Lunox"
            await message.channel.send("Matthew's hero #1 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero1 add Lylia":
            mahero1 = "Lylia"
            await message.channel.send("Matthew's hero #1 is now Lylia! :boom: ")
        if message.content == "!ml hero1 add Nana":
            mahero1 = "Nana"
            await message.channel.send("Matthew's hero #1 is now Nana! :cat:  ")
        if message.content == "!ml hero1 add Odette":
            mahero1 = "Odette"
            await message.channel.send("Matthew's hero #1 is now Odette! :duck: ")
        if message.content == "!ml hero1 add Pharsa":
            mahero1 = "Pharsa"
            await message.channel.send("Matthew's hero #1 is now Pharsa! :dove:  ")
        if message.content == "!ml hero1 add Vale":
            mahero1 = "Vale"
            await message.channel.send("Matthew's hero #1 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero1 add Valir":
            mahero1 = "Valir"
            await message.channel.send("Matthew's hero #1 is now Valir! :fire:")
        if message.content == "!ml hero1 add Vexanna":
            mahero1 = "Vexanna"
            await message.channel.send("Matthew's hero #1 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero1 add Bruno":
            mahero1 = "Bruno"
            await message.channel.send("Matthew's hero #1 is now Bruno! :soccer:  ")
        if message.content == "!ml hero1 add Claude":
            mahero1 = "Claude"
            await message.channel.send("Matthew's hero #1 is now Claude! :monkey:  ")
        if message.content == "!ml hero1 add Clint":
            mahero1 = "Clint"
            await message.channel.send("Matthew's hero #1 is now Clint! :cowboy: ")
        if message.content == "!ml hero1 add Granger":
            mahero1 = "Granger"
            await message.channel.send("Matthew's hero #1 is now Granger! :violin: ")
        if message.content == "!ml hero1 add Hanabi":
            mahero1 = "Hanabi"
            await message.channel.send("Matthew's hero #1 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero1 add Irithel":
            mahero1 = "Irithel"
            await message.channel.send("Matthew's hero #1 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero1 add Karrie":
            mahero1 = "Karrie"
            await message.channel.send(
                "Matthew's hero #1 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero1 add Kimmy":
            mahero1 = "Kimmy"
            await message.channel.send("Matthew's hero #1 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero1 add Layla":
            mahero1 = "Layla"
            await message.channel.send("Matthew's hero #1 is now Layla! :haircut:  ")
        if message.content == "!ml hero1 add Miya":
            mahero1 = "Miya"
            await message.channel.send("Matthew's hero #1 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero1 add Moskov":
            mahero1 = "Moskov"
            await message.channel.send("Matthew's hero #1 is now Moskov! :imp: ")
        if message.content == "!ml hero1 add Yi Sun-Shin":
            mahero1 = "Yi Sun-Shin"
            await message.channel.send("Matthew's hero #1 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero1 add Angela":
            mahero1 = "Angela"
            await message.channel.send("Matthew's hero #1 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero1 add Diggie":
            mahero1 = "Diggie"
            await message.channel.send("Matthew's hero #1 is now Diggie! :owl: ")
        if message.content == "!ml hero1 add Estes":
            mahero1 = "Estes"
            await message.channel.send("Matthew's hero #1 is now Estes! :ear:  ")
        if message.content == "!ml hero1 add Rafaela":
            mahero1 = "Rafaela"
            await message.channel.send("Matthew's hero #1 is now Rafaela! :angel: ")
        if message.content == "!ml hero1 add Rynn":
            mahero1 = "Rynn"
            await message.channel.send("Matthew's hero #1 is now Rynn! ")
        if message.content == "!ml hero2 add Akai":
            global mahero2
            mahero2 = "Akai"
            await message.channel.send("Matthew's hero #2 is now Akai! :panda_face: ")
        if message.content == "!ml hero2 add Balmond":
            mahero2 = "Balmond"
            await message.channel.send("Matthew's hero #2 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero2 add Belerick":
            mahero2 = "Belerick"
            await message.channel.send("Matthew's hero #2 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero2 add Franco":
            mahero2 = "Franco"
            await message.channel.send("Matthew's hero #2 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero2 add Esmerelda":
            mahero2 = "Esmerelda"
            await message.channel.send("Matthew's hero #2 is now Esmerelda! :shield: ")
        if message.content == "!ml hero2 add Gatotkaca":
            mahero2 = "Gatotkaca"
            await message.channel.send("Matthew's hero #2 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero2 add Grock":
            mahero2 = "Grock"
            await message.channel.send("Matthew's hero #2 is now Grock! :european_castle: ")
        if message.content == "!ml hero2 add Hilda":
            mahero2 = "Hilda"
            await message.channel.send("Matthew's hero #2 is now Hilda! :runner: ")
        if message.content == "!ml hero2 add Hylos":
            mahero2 = "Hylos"
            await message.channel.send("Matthew's hero #2 is now Hylos! :unicorn: ")
        if message.content == "!ml hero2 add Johnson":
            mahero2 = "Johnson"
            await message.channel.send("Matthew's hero #2 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero2 add Khufra":
            mahero2 = "Khufra"
            await message.channel.send("Matthew's hero #2 is now Khufra! :clown: ")
        if message.content == "!ml hero2 add Lolita":
            mahero2 = "Lolita"
            await message.channel.send("Matthew's hero #2 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            mahero2 = "Masha"
            await message.channel.send("Matthew's hero #2 is now Masha! :bear: ")
        if message.content == "!ml hero2 add Minotaur":
            mahero2 = "Minotaur"
            await message.channel.send("Matthew's hero #2 is now Minotaur! :cow: ")
        if message.content == "!ml hero2 add Tigreal":
            mahero2 = "Tigreal"
            await message.channel.send("Matthew's hero #2 is now Tigreal! :moyai: ")
        if message.content == "!ml hero2 add Uranus":
            mahero2 = "Uranus"
            await message.channel.send("Matthew's hero #2 is now Uranus! :peach: ")
        if message.content == "!ml hero2 add X.Borg":
            mahero2 = "X.Borg"
            await message.channel.send("Matthew's hero #2 is now X.Borg! :fire: ")
        if message.content == "!ml hero2 add Aldous":
            mahero2 = "Aldous"
            await message.channel.send("Matthew's hero #2 is now Aldous! :fist: ")
        if message.content == "!ml hero2 add Alpha":
            mahero2 = "Alpha"
            await message.channel.send("Matthew's hero #2 is now Alpha! :airplane: ")
        if message.content == "!ml hero2 add Alucard":
            mahero2 = "Alucard"
            await message.channel.send("Matthew's hero #2 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero2 add Argus":
            mahero2 = "Argus"
            await message.channel.send("Matthew's hero #2 is now Argus! :angel: ")
        if message.content == "!ml hero2 add Badang":
            mahero2 = "Badang"
            await message.channel.send("Matthew's hero #2 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero2 add Bane":
            mahero2 = "Bane"
            await message.channel.send("Matthew's hero #2 is now Bane! :octopus: ")
        if message.content == "!ml hero2 add Chou":
            mahero2 = "Chou"
            await message.channel.send("Matthew's hero #2 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero2 add Dyrroth":
            mahero2 = "Dyrroth"
            await message.channel.send("Matthew's hero #2 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero2 add Freya":
            mahero2 = "Freya"
            await message.channel.send("Matthew's hero #2 is now Freya! :hammer: ")
        if message.content == "!ml hero2 add Guinevere":
            mahero2 = "Guinevere"
            await message.channel.send("Matthew's hero #2 is now Guinevere! :dress:  ")
        if message.content == "!ml hero2 add Jawhead":
            mahero2 = "Jawhead"
            await message.channel.send("Matthew's hero #2 is now Jawhead! :robot: ")
        if message.content == "!ml hero2 add Kaja":
            mahero2 = "Kaja"
            await message.channel.send("Matthew's hero #2 is now Kaja! :bird: ")
        if message.content == "!ml hero2 add Lapu-Lapu":
            mahero2 = "Lapu-Lapu"
            await message.channel.send("Matthew's hero #2 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero2 add Leomord":
            mahero2 = "Leomord"
            await message.channel.send("Matthew's hero #2 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero2 add Martis":
            mahero2 = "Martis"
            await message.channel.send("Matthew's hero #2 is now Martis! :crab: ")
        if message.content == "!ml hero2 add Minsitthar":
            mahero2 = "Minsitthar"
            await message.channel.send("Matthew's hero #2 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero2 add Roger":
            mahero2 = "Roger"
            await message.channel.send("Matthew's hero #2 is now Roger! :wolf: ")
        if message.content == "!ml hero2 add Ruby":
            mahero2 = "Ruby"
            await message.channel.send("Matthew's hero #2 is now Ruby! :heart: ")
        if message.content == "!ml hero2 add Sun":
            mahero2 = "Sun"
            await message.channel.send("Matthew's hero #2 is now Sun! :monkey_face: ")
        if message.content == "!ml hero2 add Thamuz":
            mahero2 = "Thamuz"
            await message.channel.send("Matthew's hero #2 is now Thamuz! :rage: ")
        if message.content == "!ml hero2 add Terizla":
            mahero2 = "Terizla"
            await message.channel.send("Matthew's hero #2 is now Terizla! :hammer: ")
        if message.content == "!ml hero2 add Zilong":
            mahero2 = "Zilong"
            await message.channel.send("Matthew's hero #2 is now Zilong! :dragon: ")
        if message.content == "!ml hero2 add Fanny":
            mahero2 = "Fanny"
            await message.channel.send("Matthew's hero #2 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero2 add Gusion":
            mahero2 = "Gusion"
            await message.channel.send(
                "Matthew's hero #2 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero2 add Hanzo":
            mahero2 = "Hanzo"
            await message.channel.send("Matthew's hero #2 is now Hanzo! :ghost: ")
        if message.content == "!ml hero2 add Hayabusa":
            mahero2 = "Hayabusa"
            await message.channel.send("Matthew's hero #2 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero2 add Helcurt":
            mahero2 = "Helcurt"
            await message.channel.send("Matthew's hero #2 is now Helcurt! :mute:  ")
        if message.content == "!ml hero2 add Karina":
            mahero2 = "Karina"
            await message.channel.send("Matthew's hero #2 is now Karina! :purple_heart: ")
        if message.content == "!ml hero2 add Lancelot":
            mahero2 = "Lancelot"
            await message.channel.send("Matthew's hero #2 is now Lancelot! :fencer: ")
        if message.content == "!ml hero2 add Lesley":
            mahero2 = "Lesley"
            await message.channel.send("Matthew's hero #2 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero2 add Natalia":
            mahero2 = "Natalia"
            await message.channel.send("Matthew's hero #2 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero2 add Saber":
            mahero2 = "Saber"
            await message.channel.send("Matthew's hero #2 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero2 add Selena":
            mahero2 = "Selena"
            await message.channel.send("Matthew's hero #2 is now Selena! :sleeping:  ")
        if message.content == "!ml hero2 add Alice":
            mahero2 = "Alice"
            await message.channel.send("Matthew's hero #2 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero2 add Aurora":
            mahero2 = "Aurora"
            await message.channel.send("Matthew's hero #2 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            mahero2 = "Chang'e"
            await message.channel.send("Matthew's hero #2 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero2 add Cyclops":
            mahero2 = "Cyclops"
            await message.channel.send("Matthew's hero #2 is now Cyclops! :eye:  ")
        if message.content == "!ml hero2 add Eudora":
            mahero2 = "Eudora"
            await message.channel.send("Matthew's hero #2 is now Eudora! :zap: ")
        if message.content == "!ml hero2 add Faramis":
            mahero2 = "Faramis"
            await message.channel.send("Matthew's hero #2 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero2 add Gord":
            mahero2 = "Gord"
            await message.channel.send("Matthew's hero #2 is now Gord! :snowboarder:")
        if message.content == "!ml hero2 add Harith":
            mahero2 = "Harith"
            await message.channel.send("Matthew's hero #2 is now Harith! :older_man: ")
        if message.content == "!ml hero2 add Harley":
            mahero2 = "Harley"
            await message.channel.send("Matthew's hero #2 is now Harley! :tophat: ")
        if message.content == "!ml hero2 add Kadita":
            mahero2 = "Kadita"
            await message.channel.send("Matthew's hero #2 is now Kadita! :droplet: ")
        if message.content == "!ml hero2 add Kagura":
            mahero2 = "Kagura"
            await message.channel.send("Matthew's hero #2 is now Kagura! :umbrella2:  ")
        if message.content == "!ml hero2 add Lunox":
            mahero2 = "Lunox"
            await message.channel.send("Matthew's hero #2 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero2 add Lylia":
            mahero2 = "Lylia"
            await message.channel.send("Matthew's hero #2 is now Lylia! :boom: ")
        if message.content == "!ml hero2 add Nana":
            mahero2 = "Nana"
            await message.channel.send("Matthew's hero #2 is now Nana! :cat:  ")
        if message.content == "!ml hero2 add Odette":
            mahero2 = "Odette"
            await message.channel.send("Matthew's hero #2 is now Odette! :duck: ")
        if message.content == "!ml hero2 add Pharsa":
            mahero2 = "Pharsa"
            await message.channel.send("Matthew's hero #2 is now Pharsa! :dove:  ")
        if message.content == "!ml hero2 add Vale":
            mahero2 = "Vale"
            await message.channel.send("Matthew's hero #2 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero2 add Valir":
            mahero2 = "Valir"
            await message.channel.send("Matthew's hero #2 is now Valir! :fire:")
        if message.content == "!ml hero2 add Vexanna":
            mahero2 = "Vexanna"
            await message.channel.send("Matthew's hero #2 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero2 add Bruno":
            mahero2 = "Bruno"
            await message.channel.send("Matthew's hero #2 is now Bruno! :soccer:  ")
        if message.content == "!ml hero2 add Claude":
            mahero2 = "Claude"
            await message.channel.send("Matthew's hero #2 is now Claude! :monkey:  ")
        if message.content == "!ml hero2 add Clint":
            mahero2 = "Clint"
            await message.channel.send("Matthew's hero #2 is now Clint! :cowboy: ")
        if message.content == "!ml hero2 add Granger":
            mahero2 = "Granger"
            await message.channel.send("Matthew's hero #2 is now Granger! :violin: ")
        if message.content == "!ml hero2 add Hanabi":
            mahero2 = "Hanabi"
            await message.channel.send("Matthew's hero #2 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero2 add Irithel":
            mahero2 = "Irithel"
            await message.channel.send("Matthew's hero #2 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero2 add Karrie":
            mahero2 = "Karrie"
            await message.channel.send(
                "Matthew's hero #2 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero2 add Kimmy":
            mahero2 = "Kimmy"
            await message.channel.send("Matthew's hero #2 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero2 add Layla":
            mahero2 = "Layla"
            await message.channel.send("Matthew's hero #2 is now Layla! :haircut:  ")
        if message.content == "!ml hero2 add Miya":
            mahero2 = "Miya"
            await message.channel.send("Matthew's hero #2 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero2 add Moskov":
            mahero2 = "Moskov"
            await message.channel.send("Matthew's hero #2 is now Moskov! :imp: ")
        if message.content == "!ml hero2 add Yi Sun-Shin":
            mahero2 = "Yi Sun-Shin"
            await message.channel.send("Matthew's hero #2 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero2 add Angela":
            mahero2 = "Angela"
            await message.channel.send("Matthew's hero #2 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero2 add Diggie":
            mahero2 = "Diggie"
            await message.channel.send("Matthew's hero #2 is now Diggie! :owl: ")
        if message.content == "!ml hero2 add Estes":
            mahero2 = "Estes"
            await message.channel.send("Matthew's hero #2 is now Estes! :ear:  ")
        if message.content == "!ml hero2 add Rafaela":
            mahero2 = "Rafaela"
            await message.channel.send("Matthew's hero #2 is now Rafaela! :angel: ")
        if message.content == "!ml hero2 add Rynn":
            mahero2 = "Rynn"
            await message.channel.send("Matthew's hero #2 is now Rynn! ")
        if message.content == "!ml hero3 add Akai":
            global mahero3
            mahero3 = "Akai"
            await message.channel.send("Matthew's hero #3 is now Akai! :panda_face: ")
        if message.content == "!ml hero3 add Balmond":
            mahero3 = "Balmond"
            await message.channel.send("Matthew's hero #3 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero3 add Belerick":
            mahero3 = "Belerick"
            await message.channel.send("Matthew's hero #3 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero3 add Franco":
            mahero3 = "Franco"
            await message.channel.send("Matthew's hero #3 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero3 add Esmerelda":
            mahero3 = "Esmerelda"
            await message.channel.send("Matthew's hero #3 is now Esmerelda! :shield: ")
        if message.content == "!ml hero3 add Gatotkaca":
            mahero3 = "Gatotkaca"
            await message.channel.send("Matthew's hero #3 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero3 add Grock":
            mahero3 = "Grock"
            await message.channel.send("Matthew's hero #3 is now Grock! :european_castle: ")
        if message.content == "!ml hero3 add Hilda":
            mahero3 = "Hilda"
            await message.channel.send("Matthew's hero #3 is now Hilda! :runner: ")
        if message.content == "!ml hero3 add Hylos":
            mahero3 = "Hylos"
            await message.channel.send("Matthew's hero #3 is now Hylos! :unicorn: ")
        if message.content == "!ml hero3 add Johnson":
            mahero3 = "Johnson"
            await message.channel.send("Matthew's hero #3 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero3 add Khufra":
            mahero3 = "Khufra"
            await message.channel.send("Matthew's hero #3 is now Khufra! :clown: ")
        if message.content == "!ml hero3 add Lolita":
            mahero3 = "Lolita"
            await message.channel.send("Matthew's hero #3 is now Lolita! :lollipop: ")
        if message.content == "!ml hero3 add Masha":
            mahero3 = "Masha"
            await message.channel.send("Matthew's hero #3 is now Masha! :bear: ")
        if message.content == "!ml hero3 add Minotaur":
            mahero3 = "Minotaur"
            await message.channel.send("Matthew's hero #3 is now Minotaur! :cow: ")
        if message.content == "!ml hero3 add Tigreal":
            mahero3 = "Tigreal"
            await message.channel.send("Matthew's hero #3 is now Tigreal! :moyai: ")
        if message.content == "!ml hero3 add Uranus":
            mahero3 = "Uranus"
            await message.channel.send("Matthew's hero #3 is now Uranus! :peach: ")
        if message.content == "!ml hero3 add X.Borg":
            mahero3 = "X.Borg"
            await message.channel.send("Matthew's hero #3 is now X.Borg! :fire: ")
        if message.content == "!ml hero3 add Aldous":
            mahero3 = "Aldous"
            await message.channel.send("Matthew's hero #3 is now Aldous! :fist: ")
        if message.content == "!ml hero3 add Alpha":
            mahero3 = "Alpha"
            await message.channel.send("Matthew's hero #3 is now Alpha! :airplane: ")
        if message.content == "!ml hero3 add Alucard":
            mahero3 = "Alucard"
            await message.channel.send("Matthew's hero #3 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero3 add Argus":
            mahero3 = "Argus"
            await message.channel.send("Matthew's hero #3 is now Argus! :angel: ")
        if message.content == "!ml hero3 add Badang":
            mahero3 = "Badang"
            await message.channel.send("Matthew's hero #3 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero3 add Bane":
            mahero3 = "Bane"
            await message.channel.send("Matthew's hero #3 is now Bane! :octopus: ")
        if message.content == "!ml hero3 add Chou":
            mahero3 = "Chou"
            await message.channel.send("Matthew's hero #3 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero3 add Dyrroth":
            mahero3 = "Dyrroth"
            await message.channel.send("Matthew's hero #3 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero3 add Freya":
            mahero3 = "Freya"
            await message.channel.send("Matthew's hero #3 is now Freya! :hammer: ")
        if message.content == "!ml hero3 add Guinevere":
            mahero3 = "Guinevere"
            await message.channel.send("Matthew's hero #3 is now Guinevere! :dress:  ")
        if message.content == "!ml hero3 add Jawhead":
            mahero3 = "Jawhead"
            await message.channel.send("Matthew's hero #3 is now Jawhead! :robot: ")
        if message.content == "!ml hero3 add Kaja":
            mahero3 = "Kaja"
            await message.channel.send("Matthew's hero #3 is now Kaja! :bird: ")
        if message.content == "!ml hero3 add Lapu-Lapu":
            mahero3 = "Lapu-Lapu"
            await message.channel.send("Matthew's hero #3 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero3 add Leomord":
            mahero3 = "Leomord"
            await message.channel.send("Matthew's hero #3 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero3 add Martis":
            mahero3 = "Martis"
            await message.channel.send("Matthew's hero #3 is now Martis! :crab: ")
        if message.content == "!ml hero3 add Minsitthar":
            mahero3 = "Minsitthar"
            await message.channel.send("Matthew's hero #3 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero3 add Roger":
            mahero3 = "Roger"
            await message.channel.send("Matthew's hero #3 is now Roger! :wolf: ")
        if message.content == "!ml hero3 add Ruby":
            mahero3 = "Ruby"
            await message.channel.send("Matthew's hero #3 is now Ruby! :heart: ")
        if message.content == "!ml hero3 add Sun":
            mahero3 = "Sun"
            await message.channel.send("Matthew's hero #3 is now Sun! :monkey_face: ")
        if message.content == "!ml hero3 add Thamuz":
            mahero3 = "Thamuz"
            await message.channel.send("Matthew's hero #3 is now Thamuz! :rage: ")
        if message.content == "!ml hero3 add Terizla":
            mahero3 = "Terizla"
            await message.channel.send("Matthew's hero #3 is now Terizla! :hammer: ")
        if message.content == "!ml hero3 add Zilong":
            mahero3 = "Zilong"
            await message.channel.send("Matthew's hero #3 is now Zilong! :dragon: ")
        if message.content == "!ml hero3 add Fanny":
            mahero3 = "Fanny"
            await message.channel.send("Matthew's hero #3 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero3 add Gusion":
            mahero3 = "Gusion"
            await message.channel.send(
                "Matthew's hero #3 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero3 add Hanzo":
            mahero3 = "Hanzo"
            await message.channel.send("Matthew's hero #3 is now Hanzo! :ghost: ")
        if message.content == "!ml hero3 add Hayabusa":
            mahero3 = "Hayabusa"
            await message.channel.send("Matthew's hero #3 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero3 add Helcurt":
            mahero3 = "Helcurt"
            await message.channel.send("Matthew's hero #3 is now Helcurt! :mute:  ")
        if message.content == "!ml hero3 add Karina":
            mahero3 = "Karina"
            await message.channel.send("Matthew's hero #3 is now Karina! :purple_heart: ")
        if message.content == "!ml hero3 add Lancelot":
            mahero3 = "Lancelot"
            await message.channel.send("Matthew's hero #3 is now Lancelot! :fencer: ")
        if message.content == "!ml hero3 add Lesley":
            mahero3 = "Lesley"
            await message.channel.send("Matthew's hero #3 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero3 add Natalia":
            mahero3 = "Natalia"
            await message.channel.send("Matthew's hero #3 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero3 add Saber":
            mahero3 = "Saber"
            await message.channel.send("Matthew's hero #3 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero3 add Selena":
            mahero3 = "Selena"
            await message.channel.send("Matthew's hero #3 is now Selena! :sleeping:  ")
        if message.content == "!ml hero3 add Alice":
            mahero3 = "Alice"
            await message.channel.send("Matthew's hero #3 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero3 add Aurora":
            mahero3 = "Aurora"
            await message.channel.send("Matthew's hero #3 is now Aurora! :snow: ")
        if message.content == "!ml hero3 add Chang'e":
            mahero3 = "Chang'e"
            await message.channel.send("Matthew's hero #3 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero3 add Cyclops":
            mahero3 = "Cyclops"
            await message.channel.send("Matthew's hero #3 is now Cyclops! :eye:  ")
        if message.content == "!ml hero3 add Eudora":
            mahero3 = "Eudora"
            await message.channel.send("Matthew's hero #3 is now Eudora! :zap: ")
        if message.content == "!ml hero3 add Faramis":
            mahero3 = "Faramis"
            await message.channel.send("Matthew's hero #3 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero3 add Gord":
            mahero3 = "Gord"
            await message.channel.send("Matthew's hero #3 is now Gord! :snowboarder:")
        if message.content == "!ml hero3 add Harith":
            mahero3 = "Harith"
            await message.channel.send("Matthew's hero #3 is now Harith! :older_man: ")
        if message.content == "!ml hero3 add Harley":
            mahero3 = "Harley"
            await message.channel.send("Matthew's hero #3 is now Harley! :tophat: ")
        if message.content == "!ml hero3 add Kadita":
            mahero3 = "Kadita"
            await message.channel.send("Matthew's hero #3 is now Kadita! :droplet: ")
        if message.content == "!ml hero3 add Kagura":
            mahero3 = "Kagura"
            await message.channel.send("Matthew's hero #3 is now Kagura! :umbrella2:  ")
        if message.content == "!ml hero3 add Lunox":
            mahero3 = "Lunox"
            await message.channel.send("Matthew's hero #3 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero3 add Lylia":
            mahero3 = "Lylia"
            await message.channel.send("Matthew's hero #3 is now Lylia! :boom: ")
        if message.content == "!ml hero3 add Nana":
            mahero3 = "Nana"
            await message.channel.send("Matthew's hero #3 is now Nana! :cat:  ")
        if message.content == "!ml hero3 add Odette":
            mahero3 = "Odette"
            await message.channel.send("Matthew's hero #3 is now Odette! :duck: ")
        if message.content == "!ml hero3 add Pharsa":
            mahero3 = "Pharsa"
            await message.channel.send("Matthew's hero #3 is now Pharsa! :dove:  ")
        if message.content == "!ml hero3 add Vale":
            mahero3 = "Vale"
            await message.channel.send("Matthew's hero #3 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero3 add Valir":
            mahero3 = "Valir"
            await message.channel.send("Matthew's hero #3 is now Valir! :fire:")
        if message.content == "!ml hero3 add Vexanna":
            mahero3 = "Vexanna"
            await message.channel.send("Matthew's hero #3 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero3 add Bruno":
            mahero3 = "Bruno"
            await message.channel.send("Matthew's hero #3 is now Bruno! :soccer:  ")
        if message.content == "!ml hero3 add Claude":
            mahero3 = "Claude"
            await message.channel.send("Matthew's hero #3 is now Claude! :monkey:  ")
        if message.content == "!ml hero3 add Clint":
            mahero3 = "Clint"
            await message.channel.send("Matthew's hero #3 is now Clint! :cowboy: ")
        if message.content == "!ml hero3 add Granger":
            mahero3 = "Granger"
            await message.channel.send("Matthew's hero #3 is now Granger! :violin: ")
        if message.content == "!ml hero3 add Hanabi":
            mahero3 = "Hanabi"
            await message.channel.send("Matthew's hero #3 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero3 add Irithel":
            mahero3 = "Irithel"
            await message.channel.send("Matthew's hero #3 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero3 add Karrie":
            mahero3 = "Karrie"
            await message.channel.send(
                "Matthew's hero #3 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero3 add Kimmy":
            mahero3 = "Kimmy"
            await message.channel.send("Matthew's hero #3 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero3 add Layla":
            mahero3 = "Layla"
            await message.channel.send("Matthew's hero #3 is now Layla! :haircut:  ")
        if message.content == "!ml hero3 add Miya":
            mahero3 = "Miya"
            await message.channel.send("Matthew's hero #3 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero3 add Moskov":
            mahero3 = "Moskov"
            await message.channel.send("Matthew's hero #3 is now Moskov! :imp: ")
        if message.content == "!ml hero3 add Yi Sun-Shin":
            mahero3 = "Yi Sun-Shin"
            await message.channel.send("Matthew's hero #3 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero3 add Angela":
            mahero3 = "Angela"
            await message.channel.send("Matthew's hero #3 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero3 add Diggie":
            mahero3 = "Diggie"
            await message.channel.send("Matthew's hero #3 is now Diggie! :owl: ")
        if message.content == "!ml hero3 add Estes":
            mahero3 = "Estes"
            await message.channel.send("Matthew's hero #3 is now Estes! :ear:  ")
        if message.content == "!ml hero3 add Rafaela":
            mahero3 = "Rafaela"
            await message.channel.send("Matthew's hero #3 is now Rafaela! :angel: ")
        if message.content == "!ml hero3 add Rynn":
            mahero3 = "Rynn"
            await message.channel.send("Matthew's hero #3 is now Rynn! ")
        if message.content == "!ml hero4 add Akai":
            global mahero4
            mahero4 = "Akai"
            await message.channel.send("Matthew's hero #4 is now Akai! :panda_face: ")
        if message.content == "!ml hero4 add Balmond":
            mahero4 = "Balmond"
            await message.channel.send("Matthew's hero #4 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero4 add Belerick":
            mahero4 = "Belerick"
            await message.channel.send("Matthew's hero #4 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero4 add Franco":
            mahero4 = "Franco"
            await message.channel.send("Matthew's hero #4 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero4 add Esmerelda":
            mahero4 = "Esmerelda"
            await message.channel.send("Matthew's hero #4 is now Esmerelda! :shield: ")
        if message.content == "!ml hero4 add Gatotkaca":
            mahero4 = "Gatotkaca"
            await message.channel.send("Matthew's hero #4 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero4 add Grock":
            mahero4 = "Grock"
            await message.channel.send("Matthew's hero #4 is now Grock! :european_castle: ")
        if message.content == "!ml hero4 add Hilda":
            mahero4 = "Hilda"
            await message.channel.send("Matthew's hero #4 is now Hilda! :runner: ")
        if message.content == "!ml hero4 add Hylos":
            mahero4 = "Hylos"
            await message.channel.send("Matthew's hero #4 is now Hylos! :unicorn: ")
        if message.content == "!ml hero4 add Johnson":
            mahero4 = "Johnson"
            await message.channel.send("Matthew's hero #4 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero4 add Khufra":
            mahero4 = "Khufra"
            await message.channel.send("Matthew's hero #4 is now Khufra! :clown: ")
        if message.content == "!ml hero4 add Lolita":
            mahero4 = "Lolita"
            await message.channel.send("Matthew's hero #4 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            mahero4 = "Masha"
            await message.channel.send("Matthew's hero #4 is now Masha! :bear: ")
        if message.content == "!ml hero4 add Minotaur":
            mahero4 = "Minotaur"
            await message.channel.send("Matthew's hero #4 is now Minotaur! :cow: ")
        if message.content == "!ml hero4 add Tigreal":
            mahero4 = "Tigreal"
            await message.channel.send("Matthew's hero #4 is now Tigreal! :moyai: ")
        if message.content == "!ml hero4 add Uranus":
            mahero4 = "Uranus"
            await message.channel.send("Matthew's hero #4 is now Uranus! :peach: ")
        if message.content == "!ml hero4 add X.Borg":
            mahero4 = "X.Borg"
            await message.channel.send("Matthew's hero #4 is now X.Borg! :fire: ")
        if message.content == "!ml hero4 add Aldous":
            mahero4 = "Aldous"
            await message.channel.send("Matthew's hero #4 is now Aldous! :fist: ")
        if message.content == "!ml hero4 add Alpha":
            mahero4 = "Alpha"
            await message.channel.send("Matthew's hero #4 is now Alpha! :airplane: ")
        if message.content == "!ml hero4 add Alucard":
            mahero4 = "Alucard"
            await message.channel.send("Matthew's hero #4 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero4 add Argus":
            mahero4 = "Argus"
            await message.channel.send("Matthew's hero #4 is now Argus! :angel: ")
        if message.content == "!ml hero4 add Badang":
            mahero4 = "Badang"
            await message.channel.send("Matthew's hero #4 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero4 add Bane":
            mahero4 = "Bane"
            await message.channel.send("Matthew's hero #4 is now Bane! :octopus: ")
        if message.content == "!ml hero4 add Chou":
            mahero4 = "Chou"
            await message.channel.send("Matthew's hero #4 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero4 add Dyrroth":
            mahero4 = "Dyrroth"
            await message.channel.send("Matthew's hero #4 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero4 add Freya":
            mahero4 = "Freya"
            await message.channel.send("Matthew's hero #4 is now Freya! :hammer: ")
        if message.content == "!ml hero4 add Guinevere":
            mahero4 = "Guinevere"
            await message.channel.send("Matthew's hero #4 is now Guinevere! :dress:  ")
        if message.content == "!ml hero4 add Jawhead":
            mahero4 = "Jawhead"
            await message.channel.send("Matthew's hero #4 is now Jawhead! :robot: ")
        if message.content == "!ml hero4 add Kaja":
            mahero4 = "Kaja"
            await message.channel.send("Matthew's hero #4 is now Kaja! :bird: ")
        if message.content == "!ml hero4 add Lapu-Lapu":
            mahero4 = "Lapu-Lapu"
            await message.channel.send("Matthew's hero #4 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero4 add Leomord":
            mahero4 = "Leomord"
            await message.channel.send("Matthew's hero #4 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero4 add Martis":
            mahero4 = "Martis"
            await message.channel.send("Matthew's hero #4 is now Martis! :crab: ")
        if message.content == "!ml hero4 add Minsitthar":
            mahero4 = "Minsitthar"
            await message.channel.send("Matthew's hero #4 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero4 add Roger":
            mahero4 = "Roger"
            await message.channel.send("Matthew's hero #4 is now Roger! :wolf: ")
        if message.content == "!ml hero4 add Ruby":
            mahero4 = "Ruby"
            await message.channel.send("Matthew's hero #4 is now Ruby! :heart: ")
        if message.content == "!ml hero4 add Sun":
            mahero4 = "Sun"
            await message.channel.send("Matthew's hero #4 is now Sun! :monkey_face: ")
        if message.content == "!ml hero4 add Thamuz":
            mahero4 = "Thamuz"
            await message.channel.send("Matthew's hero #4 is now Thamuz! :rage: ")
        if message.content == "!ml hero4 add Terizla":
            mahero4 = "Terizla"
            await message.channel.send("Matthew's hero #4 is now Terizla! :hammer: ")
        if message.content == "!ml hero4 add Zilong":
            mahero4 = "Zilong"
            await message.channel.send("Matthew's hero #4 is now Zilong! :dragon: ")
        if message.content == "!ml hero4 add Fanny":
            mahero4 = "Fanny"
            await message.channel.send("Matthew's hero #4 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero4 add Gusion":
            mahero4 = "Gusion"
            await message.channel.send(
                "Matthew's hero #4 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero4 add Hanzo":
            mahero4 = "Hanzo"
            await message.channel.send("Matthew's hero #4 is now Hanzo! :ghost: ")
        if message.content == "!ml hero4 add Hayabusa":
            mahero4 = "Hayabusa"
            await message.channel.send("Matthew's hero #4 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero4 add Helcurt":
            mahero4 = "Helcurt"
            await message.channel.send("Matthew's hero #4 is now Helcurt! :mute:  ")
        if message.content == "!ml hero4 add Karina":
            mahero4 = "Karina"
            await message.channel.send("Matthew's hero #4 is now Karina! :purple_heart: ")
        if message.content == "!ml hero4 add Lancelot":
            mahero4 = "Lancelot"
            await message.channel.send("Matthew's hero #4 is now Lancelot! :fencer: ")
        if message.content == "!ml hero4 add Lesley":
            mahero4 = "Lesley"
            await message.channel.send("Matthew's hero #4 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero4 add Natalia":
            mahero4 = "Natalia"
            await message.channel.send("Matthew's hero #4 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero4 add Saber":
            mahero4 = "Saber"
            await message.channel.send("Matthew's hero #4 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero4 add Selena":
            mahero4 = "Selena"
            await message.channel.send("Matthew's hero #4 is now Selena! :sleeping:  ")
        if message.content == "!ml hero4 add Alice":
            mahero4 = "Alice"
            await message.channel.send("Matthew's hero #4 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero4 add Aurora":
            mahero4 = "Aurora"
            await message.channel.send("Matthew's hero #4 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            mahero4 = "Chang'e"
            await message.channel.send("Matthew's hero #4 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero4 add Cyclops":
            mahero4 = "Cyclops"
            await message.channel.send("Matthew's hero #4 is now Cyclops! :eye:  ")
        if message.content == "!ml hero4 add Eudora":
            mahero4 = "Eudora"
            await message.channel.send("Matthew's hero #4 is now Eudora! :zap: ")
        if message.content == "!ml hero4 add Faramis":
            mahero4 = "Faramis"
            await message.channel.send("Matthew's hero #4 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero4 add Gord":
            mahero4 = "Gord"
            await message.channel.send("Matthew's hero #4 is now Gord! :snowboarder:")
        if message.content == "!ml hero4 add Harith":
            mahero4 = "Harith"
            await message.channel.send("Matthew's hero #4 is now Harith! :older_man: ")
        if message.content == "!ml hero4 add Harley":
            mahero4 = "Harley"
            await message.channel.send("Matthew's hero #4 is now Harley! :tophat: ")
        if message.content == "!ml hero4 add Kadita":
            mahero4 = "Kadita"
            await message.channel.send("Matthew's hero #4 is now Kadita! :droplet: ")
        if message.content == "!ml hero4 add Kagura":
            mahero4 = "Kagura"
            await message.channel.send("Matthew's hero #4 is now Kagura! :umbrella4:  ")
        if message.content == "!ml hero4 add Lunox":
            mahero4 = "Lunox"
            await message.channel.send("Matthew's hero #4 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero4 add Lylia":
            mahero4 = "Lylia"
            await message.channel.send("Matthew's hero #4 is now Lylia! :boom: ")
        if message.content == "!ml hero4 add Nana":
            mahero4 = "Nana"
            await message.channel.send("Matthew's hero #4 is now Nana! :cat:  ")
        if message.content == "!ml hero4 add Odette":
            mahero4 = "Odette"
            await message.channel.send("Matthew's hero #4 is now Odette! :duck: ")
        if message.content == "!ml hero4 add Pharsa":
            mahero4 = "Pharsa"
            await message.channel.send("Matthew's hero #4 is now Pharsa! :dove:  ")
        if message.content == "!ml hero4 add Vale":
            mahero4 = "Vale"
            await message.channel.send("Matthew's hero #4 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero4 add Valir":
            mahero4 = "Valir"
            await message.channel.send("Matthew's hero #4 is now Valir! :fire:")
        if message.content == "!ml hero4 add Vexanna":
            mahero4 = "Vexanna"
            await message.channel.send("Matthew's hero #4 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero4 add Bruno":
            mahero4 = "Bruno"
            await message.channel.send("Matthew's hero #4 is now Bruno! :soccer:  ")
        if message.content == "!ml hero4 add Claude":
            mahero4 = "Claude"
            await message.channel.send("Matthew's hero #4 is now Claude! :monkey:  ")
        if message.content == "!ml hero4 add Clint":
            mahero4 = "Clint"
            await message.channel.send("Matthew's hero #4 is now Clint! :cowboy: ")
        if message.content == "!ml hero4 add Granger":
            mahero4 = "Granger"
            await message.channel.send("Matthew's hero #4 is now Granger! :violin: ")
        if message.content == "!ml hero4 add Hanabi":
            mahero4 = "Hanabi"
            await message.channel.send("Matthew's hero #4 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero4 add Irithel":
            mahero4 = "Irithel"
            await message.channel.send("Matthew's hero #4 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero4 add Karrie":
            mahero4 = "Karrie"
            await message.channel.send(
                "Matthew's hero #4 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero4 add Kimmy":
            mahero4 = "Kimmy"
            await message.channel.send("Matthew's hero #4 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero4 add Layla":
            mahero4 = "Layla"
            await message.channel.send("Matthew's hero #4 is now Layla! :haircut:  ")
        if message.content == "!ml hero4 add Miya":
            mahero4 = "Miya"
            await message.channel.send("Matthew's hero #4 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero4 add Moskov":
            mahero4 = "Moskov"
            await message.channel.send("Matthew's hero #4 is now Moskov! :imp: ")
        if message.content == "!ml hero4 add Yi Sun-Shin":
            mahero4 = "Yi Sun-Shin"
            await message.channel.send("Matthew's hero #4 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero4 add Angela":
            mahero4 = "Angela"
            await message.channel.send("Matthew's hero #4 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero4 add Diggie":
            mahero4 = "Diggie"
            await message.channel.send("Matthew's hero #4 is now Diggie! :owl: ")
        if message.content == "!ml hero4 add Estes":
            mahero4 = "Estes"
            await message.channel.send("Matthew's hero #4 is now Estes! :ear:  ")
        if message.content == "!ml hero4 add Rafaela":
            mahero4 = "Rafaela"
            await message.channel.send("Matthew's hero #4 is now Rafaela! :angel: ")
        if message.content == "!ml hero4 add Rynn":
            mahero4 = "Rynn"
            await message.channel.send("Matthew's hero #4 is now Rynn! ")
        if message.content == "!ml hero5 add Akai":
            global mahero5
            mahero5 = "Akai"
            await message.channel.send("Matthew's hero #5 is now Akai! :panda_face: ")
        if message.content == "!ml hero5 add Balmond":
            mahero5 = "Balmond"
            await message.channel.send("Matthew's hero #5 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero5 add Belerick":
            mahero5 = "Belerick"
            await message.channel.send("Matthew's hero #5 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero5 add Franco":
            mahero5 = "Franco"
            await message.channel.send("Matthew's hero #5 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero5 add Esmerelda":
            mahero5 = "Esmerelda"
            await message.channel.send("Matthew's hero #5 is now Esmerelda! :shield: ")
        if message.content == "!ml hero5 add Gatotkaca":
            mahero5 = "Gatotkaca"
            await message.channel.send("Matthew's hero #5 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero5 add Grock":
            mahero5 = "Grock"
            await message.channel.send("Matthew's hero #5 is now Grock! :european_castle: ")
        if message.content == "!ml hero5 add Hilda":
            mahero5 = "Hilda"
            await message.channel.send("Matthew's hero #5 is now Hilda! :runner: ")
        if message.content == "!ml hero5 add Hylos":
            mahero5 = "Hylos"
            await message.channel.send("Matthew's hero #5 is now Hylos! :unicorn: ")
        if message.content == "!ml hero5 add Johnson":
            mahero5 = "Johnson"
            await message.channel.send("Matthew's hero #5 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero5 add Khufra":
            mahero5 = "Khufra"
            await message.channel.send("Matthew's hero #5 is now Khufra! :clown: ")
        if message.content == "!ml hero5 add Lolita":
            mahero5 = "Lolita"
            await message.channel.send("Matthew's hero #5 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            mahero5 = "Masha"
            await message.channel.send("Matthew's hero #5 is now Masha! :bear: ")
        if message.content == "!ml hero5 add Minotaur":
            mahero5 = "Minotaur"
            await message.channel.send("Matthew's hero #5 is now Minotaur! :cow: ")
        if message.content == "!ml hero5 add Tigreal":
            mahero5 = "Tigreal"
            await message.channel.send("Matthew's hero #5 is now Tigreal! :moyai: ")
        if message.content == "!ml hero5 add Uranus":
            mahero5 = "Uranus"
            await message.channel.send("Matthew's hero #5 is now Uranus! :peach: ")
        if message.content == "!ml hero5 add X.Borg":
            mahero5 = "X.Borg"
            await message.channel.send("Matthew's hero #5 is now X.Borg! :fire: ")
        if message.content == "!ml hero5 add Aldous":
            mahero5 = "Aldous"
            await message.channel.send("Matthew's hero #5 is now Aldous! :fist: ")
        if message.content == "!ml hero5 add Alpha":
            mahero5 = "Alpha"
            await message.channel.send("Matthew's hero #5 is now Alpha! :airplane: ")
        if message.content == "!ml hero5 add Alucard":
            mahero5 = "Alucard"
            await message.channel.send("Matthew's hero #5 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero5 add Argus":
            mahero5 = "Argus"
            await message.channel.send("Matthew's hero #5 is now Argus! :angel: ")
        if message.content == "!ml hero5 add Badang":
            mahero5 = "Badang"
            await message.channel.send("Matthew's hero #5 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero5 add Bane":
            mahero5 = "Bane"
            await message.channel.send("Matthew's hero #5 is now Bane! :octopus: ")
        if message.content == "!ml hero5 add Chou":
            mahero5 = "Chou"
            await message.channel.send("Matthew's hero #5 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero5 add Dyrroth":
            mahero5 = "Dyrroth"
            await message.channel.send("Matthew's hero #5 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero5 add Freya":
            mahero5 = "Freya"
            await message.channel.send("Matthew's hero #5 is now Freya! :hammer: ")
        if message.content == "!ml hero5 add Guinevere":
            mahero5 = "Guinevere"
            await message.channel.send("Matthew's hero #5 is now Guinevere! :dress:  ")
        if message.content == "!ml hero5 add Jawhead":
            mahero5 = "Jawhead"
            await message.channel.send("Matthew's hero #5 is now Jawhead! :robot: ")
        if message.content == "!ml hero5 add Kaja":
            mahero5 = "Kaja"
            await message.channel.send("Matthew's hero #5 is now Kaja! :bird: ")
        if message.content == "!ml hero5 add Lapu-Lapu":
            mahero5 = "Lapu-Lapu"
            await message.channel.send("Matthew's hero #5 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero5 add Leomord":
            mahero5 = "Leomord"
            await message.channel.send("Matthew's hero #5 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero5 add Martis":
            mahero5 = "Martis"
            await message.channel.send("Matthew's hero #5 is now Martis! :crab: ")
        if message.content == "!ml hero5 add Minsitthar":
            mahero5 = "Minsitthar"
            await message.channel.send("Matthew's hero #5 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero5 add Roger":
            mahero5 = "Roger"
            await message.channel.send("Matthew's hero #5 is now Roger! :wolf: ")
        if message.content == "!ml hero5 add Ruby":
            mahero5 = "Ruby"
            await message.channel.send("Matthew's hero #5 is now Ruby! :heart: ")
        if message.content == "!ml hero5 add Sun":
            mahero5 = "Sun"
            await message.channel.send("Matthew's hero #5 is now Sun! :monkey_face: ")
        if message.content == "!ml hero5 add Thamuz":
            mahero5 = "Thamuz"
            await message.channel.send("Matthew's hero #5 is now Thamuz! :rage: ")
        if message.content == "!ml hero5 add Terizla":
            mahero5 = "Terizla"
            await message.channel.send("Matthew's hero #5 is now Terizla! :hammer: ")
        if message.content == "!ml hero5 add Zilong":
            mahero5 = "Zilong"
            await message.channel.send("Matthew's hero #5 is now Zilong! :dragon: ")
        if message.content == "!ml hero5 add Fanny":
            mahero5 = "Fanny"
            await message.channel.send("Matthew's hero #5 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero5 add Gusion":
            mahero5 = "Gusion"
            await message.channel.send(
                "Matthew's hero #5 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero5 add Hanzo":
            mahero5 = "Hanzo"
            await message.channel.send("Matthew's hero #5 is now Hanzo! :ghost: ")
        if message.content == "!ml hero5 add Hayabusa":
            mahero5 = "Hayabusa"
            await message.channel.send("Matthew's hero #5 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero5 add Helcurt":
            mahero5 = "Helcurt"
            await message.channel.send("Matthew's hero #5 is now Helcurt! :mute:  ")
        if message.content == "!ml hero5 add Karina":
            mahero5 = "Karina"
            await message.channel.send("Matthew's hero #5 is now Karina! :purple_heart: ")
        if message.content == "!ml hero5 add Lancelot":
            mahero5 = "Lancelot"
            await message.channel.send("Matthew's hero #5 is now Lancelot! :fencer: ")
        if message.content == "!ml hero5 add Lesley":
            mahero5 = "Lesley"
            await message.channel.send("Matthew's hero #5 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero5 add Natalia":
            mahero5 = "Natalia"
            await message.channel.send("Matthew's hero #5 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero5 add Saber":
            mahero5 = "Saber"
            await message.channel.send("Matthew's hero #5 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero5 add Selena":
            mahero5 = "Selena"
            await message.channel.send("Matthew's hero #5 is now Selena! :sleeping:  ")
        if message.content == "!ml hero5 add Alice":
            mahero5 = "Alice"
            await message.channel.send("Matthew's hero #5 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero5 add Aurora":
            mahero5 = "Aurora"
            await message.channel.send("Matthew's hero #5 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            mahero5 = "Chang'e"
            await message.channel.send("Matthew's hero #5 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero5 add Cyclops":
            mahero5 = "Cyclops"
            await message.channel.send("Matthew's hero #5 is now Cyclops! :eye:  ")
        if message.content == "!ml hero5 add Eudora":
            mahero5 = "Eudora"
            await message.channel.send("Matthew's hero #5 is now Eudora! :zap: ")
        if message.content == "!ml hero5 add Faramis":
            mahero5 = "Faramis"
            await message.channel.send("Matthew's hero #5 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero5 add Gord":
            mahero5 = "Gord"
            await message.channel.send("Matthew's hero #5 is now Gord! :snowboarder:")
        if message.content == "!ml hero5 add Harith":
            mahero5 = "Harith"
            await message.channel.send("Matthew's hero #5 is now Harith! :older_man: ")
        if message.content == "!ml hero5 add Harley":
            mahero5 = "Harley"
            await message.channel.send("Matthew's hero #5 is now Harley! :tophat: ")
        if message.content == "!ml hero5 add Kadita":
            mahero5 = "Kadita"
            await message.channel.send("Matthew's hero #5 is now Kadita! :droplet: ")
        if message.content == "!ml hero5 add Kagura":
            mahero5 = "Kagura"
            await message.channel.send("Matthew's hero #5 is now Kagura! :umbrella5:  ")
        if message.content == "!ml hero5 add Lunox":
            mahero5 = "Lunox"
            await message.channel.send("Matthew's hero #5 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero5 add Lylia":
            mahero5 = "Lylia"
            await message.channel.send("Matthew's hero #5 is now Lylia! :boom: ")
        if message.content == "!ml hero5 add Nana":
            mahero5 = "Nana"
            await message.channel.send("Matthew's hero #5 is now Nana! :cat:  ")
        if message.content == "!ml hero5 add Odette":
            mahero5 = "Odette"
            await message.channel.send("Matthew's hero #5 is now Odette! :duck: ")
        if message.content == "!ml hero5 add Pharsa":
            mahero5 = "Pharsa"
            await message.channel.send("Matthew's hero #5 is now Pharsa! :dove:  ")
        if message.content == "!ml hero5 add Vale":
            mahero5 = "Vale"
            await message.channel.send("Matthew's hero #5 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero5 add Valir":
            mahero5 = "Valir"
            await message.channel.send("Matthew's hero #5 is now Valir! :fire:")
        if message.content == "!ml hero5 add Vexanna":
            mahero5 = "Vexanna"
            await message.channel.send("Matthew's hero #5 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero5 add Bruno":
            mahero5 = "Bruno"
            await message.channel.send("Matthew's hero #5 is now Bruno! :soccer:  ")
        if message.content == "!ml hero5 add Claude":
            mahero5 = "Claude"
            await message.channel.send("Matthew's hero #5 is now Claude! :monkey:  ")
        if message.content == "!ml hero5 add Clint":
            mahero5 = "Clint"
            await message.channel.send("Matthew's hero #5 is now Clint! :cowboy: ")
        if message.content == "!ml hero5 add Granger":
            mahero5 = "Granger"
            await message.channel.send("Matthew's hero #5 is now Granger! :violin: ")
        if message.content == "!ml hero5 add Hanabi":
            mahero5 = "Hanabi"
            await message.channel.send("Matthew's hero #5 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero5 add Irithel":
            mahero5 = "Irithel"
            await message.channel.send("Matthew's hero #5 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero5 add Karrie":
            mahero5 = "Karrie"
            await message.channel.send(
                "Matthew's hero #5 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero5 add Kimmy":
            mahero5 = "Kimmy"
            await message.channel.send("Matthew's hero #5 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero5 add Layla":
            mahero5 = "Layla"
            await message.channel.send("Matthew's hero #5 is now Layla! :haircut:  ")
        if message.content == "!ml hero5 add Miya":
            mahero5 = "Miya"
            await message.channel.send("Matthew's hero #5 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero5 add Moskov":
            mahero5 = "Moskov"
            await message.channel.send("Matthew's hero #5 is now Moskov! :imp: ")
        if message.content == "!ml hero5 add Yi Sun-Shin":
            mahero5 = "Yi Sun-Shin"
            await message.channel.send("Matthew's hero #5 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero5 add Angela":
            mahero5 = "Angela"
            await message.channel.send("Matthew's hero #5 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero5 add Diggie":
            mahero5 = "Diggie"
            await message.channel.send("Matthew's hero #5 is now Diggie! :owl: ")
        if message.content == "!ml hero5 add Estes":
            mahero5 = "Estes"
            await message.channel.send("Matthew's hero #5 is now Estes! :ear:  ")
        if message.content == "!ml hero5 add Rafaela":
            mahero5 = "Rafaela"
            await message.channel.send("Matthew's hero #5 is now Rafaela! :angel: ")
        if message.content == "!ml hero5 add Rynn":
            mahero5 = "Rynn"
            await message.channel.send("Matthew's hero #5 is now Rynn! ")
        if message.content == "!ml hero6 add Akai":
            global mahero6
            mahero6 = "Akai"
            await message.channel.send("Matthew's hero #6 is now Akai! :panda_face: ")
        if message.content == "!ml hero6 add Balmond":
            mahero6 = "Balmond"
            await message.channel.send("Matthew's hero #6 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero6 add Belerick":
            mahero6 = "Belerick"
            await message.channel.send("Matthew's hero #6 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero6 add Franco":
            mahero6 = "Franco"
            await message.channel.send("Matthew's hero #6 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero6 add Esmerelda":
            mahero6 = "Esmerelda"
            await message.channel.send("Matthew's hero #6 is now Esmerelda! :shield: ")
        if message.content == "!ml hero6 add Gatotkaca":
            mahero6 = "Gatotkaca"
            await message.channel.send("Matthew's hero #6 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero6 add Grock":
            mahero6 = "Grock"
            await message.channel.send("Matthew's hero #6 is now Grock! :european_castle: ")
        if message.content == "!ml hero6 add Hilda":
            mahero6 = "Hilda"
            await message.channel.send("Matthew's hero #6 is now Hilda! :runner: ")
        if message.content == "!ml hero6 add Hylos":
            mahero6 = "Hylos"
            await message.channel.send("Matthew's hero #6 is now Hylos! :unicorn: ")
        if message.content == "!ml hero6 add Johnson":
            mahero6 = "Johnson"
            await message.channel.send("Matthew's hero #6 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero6 add Khufra":
            mahero6 = "Khufra"
            await message.channel.send("Matthew's hero #6 is now Khufra! :clown: ")
        if message.content == "!ml hero6 add Lolita":
            mahero6 = "Lolita"
            await message.channel.send("Matthew's hero #6 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            mahero6 = "Masha"
            await message.channel.send("Matthew's hero #6 is now Masha! :bear: ")
        if message.content == "!ml hero6 add Minotaur":
            mahero6 = "Minotaur"
            await message.channel.send("Matthew's hero #6 is now Minotaur! :cow: ")
        if message.content == "!ml hero6 add Tigreal":
            mahero6 = "Tigreal"
            await message.channel.send("Matthew's hero #6 is now Tigreal! :moyai: ")
        if message.content == "!ml hero6 add Uranus":
            mahero6 = "Uranus"
            await message.channel.send("Matthew's hero #6 is now Uranus! :peach: ")
        if message.content == "!ml hero6 add X.Borg":
            mahero6 = "X.Borg"
            await message.channel.send("Matthew's hero #6 is now X.Borg! :fire: ")
        if message.content == "!ml hero6 add Aldous":
            mahero6 = "Aldous"
            await message.channel.send("Matthew's hero #6 is now Aldous! :fist: ")
        if message.content == "!ml hero6 add Alpha":
            mahero6 = "Alpha"
            await message.channel.send("Matthew's hero #6 is now Alpha! :airplane: ")
        if message.content == "!ml hero6 add Alucard":
            mahero6 = "Alucard"
            await message.channel.send("Matthew's hero #6 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero6 add Argus":
            mahero6 = "Argus"
            await message.channel.send("Matthew's hero #6 is now Argus! :angel: ")
        if message.content == "!ml hero6 add Badang":
            mahero6 = "Badang"
            await message.channel.send("Matthew's hero #6 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero6 add Bane":
            mahero6 = "Bane"
            await message.channel.send("Matthew's hero #6 is now Bane! :octopus: ")
        if message.content == "!ml hero6 add Chou":
            mahero6 = "Chou"
            await message.channel.send("Matthew's hero #6 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero6 add Dyrroth":
            mahero6 = "Dyrroth"
            await message.channel.send("Matthew's hero #6 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero6 add Freya":
            mahero6 = "Freya"
            await message.channel.send("Matthew's hero #6 is now Freya! :hammer: ")
        if message.content == "!ml hero6 add Guinevere":
            mahero6 = "Guinevere"
            await message.channel.send("Matthew's hero #6 is now Guinevere! :dress:  ")
        if message.content == "!ml hero6 add Jawhead":
            mahero6 = "Jawhead"
            await message.channel.send("Matthew's hero #6 is now Jawhead! :robot: ")
        if message.content == "!ml hero6 add Kaja":
            mahero6 = "Kaja"
            await message.channel.send("Matthew's hero #6 is now Kaja! :bird: ")
        if message.content == "!ml hero6 add Lapu-Lapu":
            mahero6 = "Lapu-Lapu"
            await message.channel.send("Matthew's hero #6 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero6 add Leomord":
            mahero6 = "Leomord"
            await message.channel.send("Matthew's hero #6 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero6 add Martis":
            mahero6 = "Martis"
            await message.channel.send("Matthew's hero #6 is now Martis! :crab: ")
        if message.content == "!ml hero6 add Minsitthar":
            mahero6 = "Minsitthar"
            await message.channel.send("Matthew's hero #6 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero6 add Roger":
            mahero6 = "Roger"
            await message.channel.send("Matthew's hero #6 is now Roger! :wolf: ")
        if message.content == "!ml hero6 add Ruby":
            mahero6 = "Ruby"
            await message.channel.send("Matthew's hero #6 is now Ruby! :heart: ")
        if message.content == "!ml hero6 add Sun":
            mahero6 = "Sun"
            await message.channel.send("Matthew's hero #6 is now Sun! :monkey_face: ")
        if message.content == "!ml hero6 add Thamuz":
            mahero6 = "Thamuz"
            await message.channel.send("Matthew's hero #6 is now Thamuz! :rage: ")
        if message.content == "!ml hero6 add Terizla":
            mahero6 = "Terizla"
            await message.channel.send("Matthew's hero #6 is now Terizla! :hammer: ")
        if message.content == "!ml hero6 add Zilong":
            mahero6 = "Zilong"
            await message.channel.send("Matthew's hero #6 is now Zilong! :dragon: ")
        if message.content == "!ml hero6 add Fanny":
            mahero6 = "Fanny"
            await message.channel.send("Matthew's hero #6 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero6 add Gusion":
            mahero6 = "Gusion"
            await message.channel.send(
                "Matthew's hero #6 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero6 add Hanzo":
            mahero6 = "Hanzo"
            await message.channel.send("Matthew's hero #6 is now Hanzo! :ghost: ")
        if message.content == "!ml hero6 add Hayabusa":
            mahero6 = "Hayabusa"
            await message.channel.send("Matthew's hero #6 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero6 add Helcurt":
            mahero6 = "Helcurt"
            await message.channel.send("Matthew's hero #6 is now Helcurt! :mute:  ")
        if message.content == "!ml hero6 add Karina":
            mahero6 = "Karina"
            await message.channel.send("Matthew's hero #6 is now Karina! :purple_heart: ")
        if message.content == "!ml hero6 add Lancelot":
            mahero6 = "Lancelot"
            await message.channel.send("Matthew's hero #6 is now Lancelot! :fencer: ")
        if message.content == "!ml hero6 add Lesley":
            mahero6 = "Lesley"
            await message.channel.send("Matthew's hero #6 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero6 add Natalia":
            mahero6 = "Natalia"
            await message.channel.send("Matthew's hero #6 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero6 add Saber":
            mahero6 = "Saber"
            await message.channel.send("Matthew's hero #6 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero6 add Selena":
            mahero6 = "Selena"
            await message.channel.send("Matthew's hero #6 is now Selena! :sleeping:  ")
        if message.content == "!ml hero6 add Alice":
            mahero6 = "Alice"
            await message.channel.send("Matthew's hero #6 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero6 add Aurora":
            mahero6 = "Aurora"
            await message.channel.send("Matthew's hero #6 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            mahero6 = "Chang'e"
            await message.channel.send("Matthew's hero #6 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero6 add Cyclops":
            mahero6 = "Cyclops"
            await message.channel.send("Matthew's hero #6 is now Cyclops! :eye:  ")
        if message.content == "!ml hero6 add Eudora":
            mahero6 = "Eudora"
            await message.channel.send("Matthew's hero #6 is now Eudora! :zap: ")
        if message.content == "!ml hero6 add Faramis":
            mahero6 = "Faramis"
            await message.channel.send("Matthew's hero #6 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero6 add Gord":
            mahero6 = "Gord"
            await message.channel.send("Matthew's hero #6 is now Gord! :snowboarder:")
        if message.content == "!ml hero6 add Harith":
            mahero6 = "Harith"
            await message.channel.send("Matthew's hero #6 is now Harith! :older_man: ")
        if message.content == "!ml hero6 add Harley":
            mahero6 = "Harley"
            await message.channel.send("Matthew's hero #6 is now Harley! :tophat: ")
        if message.content == "!ml hero6 add Kadita":
            mahero6 = "Kadita"
            await message.channel.send("Matthew's hero #6 is now Kadita! :droplet: ")
        if message.content == "!ml hero6 add Kagura":
            mahero6 = "Kagura"
            await message.channel.send("Matthew's hero #6 is now Kagura! :umbrella6:  ")
        if message.content == "!ml hero6 add Lunox":
            mahero6 = "Lunox"
            await message.channel.send("Matthew's hero #6 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero6 add Lylia":
            mahero6 = "Lylia"
            await message.channel.send("Matthew's hero #6 is now Lylia! :boom: ")
        if message.content == "!ml hero6 add Nana":
            mahero6 = "Nana"
            await message.channel.send("Matthew's hero #6 is now Nana! :cat:  ")
        if message.content == "!ml hero6 add Odette":
            mahero6 = "Odette"
            await message.channel.send("Matthew's hero #6 is now Odette! :duck: ")
        if message.content == "!ml hero6 add Pharsa":
            mahero6 = "Pharsa"
            await message.channel.send("Matthew's hero #6 is now Pharsa! :dove:  ")
        if message.content == "!ml hero6 add Vale":
            mahero6 = "Vale"
            await message.channel.send("Matthew's hero #6 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero6 add Valir":
            mahero6 = "Valir"
            await message.channel.send("Matthew's hero #6 is now Valir! :fire:")
        if message.content == "!ml hero6 add Vexanna":
            mahero6 = "Vexanna"
            await message.channel.send("Matthew's hero #6 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero6 add Bruno":
            mahero6 = "Bruno"
            await message.channel.send("Matthew's hero #6 is now Bruno! :soccer:  ")
        if message.content == "!ml hero6 add Claude":
            mahero6 = "Claude"
            await message.channel.send("Matthew's hero #6 is now Claude! :monkey:  ")
        if message.content == "!ml hero6 add Clint":
            mahero6 = "Clint"
            await message.channel.send("Matthew's hero #6 is now Clint! :cowboy: ")
        if message.content == "!ml hero6 add Granger":
            mahero6 = "Granger"
            await message.channel.send("Matthew's hero #6 is now Granger! :violin: ")
        if message.content == "!ml hero6 add Hanabi":
            mahero6 = "Hanabi"
            await message.channel.send("Matthew's hero #6 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero6 add Irithel":
            mahero6 = "Irithel"
            await message.channel.send("Matthew's hero #6 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero6 add Karrie":
            mahero6 = "Karrie"
            await message.channel.send(
                "Matthew's hero #6 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero6 add Kimmy":
            mahero6 = "Kimmy"
            await message.channel.send("Matthew's hero #6 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero6 add Layla":
            mahero6 = "Layla"
            await message.channel.send("Matthew's hero #6 is now Layla! :haircut:  ")
        if message.content == "!ml hero6 add Miya":
            mahero6 = "Miya"
            await message.channel.send("Matthew's hero #6 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero6 add Moskov":
            mahero6 = "Moskov"
            await message.channel.send("Matthew's hero #6 is now Moskov! :imp: ")
        if message.content == "!ml hero6 add Yi Sun-Shin":
            mahero6 = "Yi Sun-Shin"
            await message.channel.send("Matthew's hero #6 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero6 add Angela":
            mahero6 = "Angela"
            await message.channel.send("Matthew's hero #6 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero6 add Diggie":
            mahero6 = "Diggie"
            await message.channel.send("Matthew's hero #6 is now Diggie! :owl: ")
        if message.content == "!ml hero6 add Estes":
            mahero6 = "Estes"
            await message.channel.send("Matthew's hero #6 is now Estes! :ear:  ")
        if message.content == "!ml hero6 add Rafaela":
            mahero6 = "Rafaela"
            await message.channel.send("Matthew's hero #6 is now Rafaela! :angel: ")
        if message.content == "!ml hero6 add Rynn":
            mahero6 = "Rynn"
            await message.channel.send("Matthew's hero #6 is now Rynn! ")
        if message.content == "!ml hero7 add Akai":
            global mahero7
            mahero7 = "Akai"
            await message.channel.send("Matthew's hero #7 is now Akai! :panda_face: ")
        if message.content == "!ml hero7 add Balmond":
            mahero7 = "Balmond"
            await message.channel.send("Matthew's hero #7 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero7 add Belerick":
            mahero7 = "Belerick"
            await message.channel.send("Matthew's hero #7 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero7 add Franco":
            mahero7 = "Franco"
            await message.channel.send("Matthew's hero #7 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero7 add Esmerelda":
            mahero7 = "Esmerelda"
            await message.channel.send("Matthew's hero #7 is now Esmerelda! :shield: ")
        if message.content == "!ml hero7 add Gatotkaca":
            mahero7 = "Gatotkaca"
            await message.channel.send("Matthew's hero #7 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero7 add Grock":
            mahero7 = "Grock"
            await message.channel.send("Matthew's hero #7 is now Grock! :european_castle: ")
        if message.content == "!ml hero7 add Hilda":
            mahero7 = "Hilda"
            await message.channel.send("Matthew's hero #7 is now Hilda! :runner: ")
        if message.content == "!ml hero7 add Hylos":
            mahero7 = "Hylos"
            await message.channel.send("Matthew's hero #7 is now Hylos! :unicorn: ")
        if message.content == "!ml hero7 add Johnson":
            mahero7 = "Johnson"
            await message.channel.send("Matthew's hero #7 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero7 add Khufra":
            mahero7 = "Khufra"
            await message.channel.send("Matthew's hero #7 is now Khufra! :clown: ")
        if message.content == "!ml hero7 add Lolita":
            mahero7 = "Lolita"
            await message.channel.send("Matthew's hero #7 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            mahero7 = "Masha"
            await message.channel.send("Matthew's hero #7 is now Masha! :bear: ")
        if message.content == "!ml hero7 add Minotaur":
            mahero7 = "Minotaur"
            await message.channel.send("Matthew's hero #7 is now Minotaur! :cow: ")
        if message.content == "!ml hero7 add Tigreal":
            mahero7 = "Tigreal"
            await message.channel.send("Matthew's hero #7 is now Tigreal! :moyai: ")
        if message.content == "!ml hero7 add Uranus":
            mahero7 = "Uranus"
            await message.channel.send("Matthew's hero #7 is now Uranus! :peach: ")
        if message.content == "!ml hero7 add X.Borg":
            mahero7 = "X.Borg"
            await message.channel.send("Matthew's hero #7 is now X.Borg! :fire: ")
        if message.content == "!ml hero7 add Aldous":
            mahero7 = "Aldous"
            await message.channel.send("Matthew's hero #7 is now Aldous! :fist: ")
        if message.content == "!ml hero7 add Alpha":
            mahero7 = "Alpha"
            await message.channel.send("Matthew's hero #7 is now Alpha! :airplane: ")
        if message.content == "!ml hero7 add Alucard":
            mahero7 = "Alucard"
            await message.channel.send("Matthew's hero #7 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero7 add Argus":
            mahero7 = "Argus"
            await message.channel.send("Matthew's hero #7 is now Argus! :angel: ")
        if message.content == "!ml hero7 add Badang":
            mahero7 = "Badang"
            await message.channel.send("Matthew's hero #7 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero7 add Bane":
            mahero7 = "Bane"
            await message.channel.send("Matthew's hero #7 is now Bane! :octopus: ")
        if message.content == "!ml hero7 add Chou":
            mahero7 = "Chou"
            await message.channel.send("Matthew's hero #7 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero7 add Dyrroth":
            mahero7 = "Dyrroth"
            await message.channel.send("Matthew's hero #7 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero7 add Freya":
            mahero7 = "Freya"
            await message.channel.send("Matthew's hero #7 is now Freya! :hammer: ")
        if message.content == "!ml hero7 add Guinevere":
            mahero7 = "Guinevere"
            await message.channel.send("Matthew's hero #7 is now Guinevere! :dress:  ")
        if message.content == "!ml hero7 add Jawhead":
            mahero7 = "Jawhead"
            await message.channel.send("Matthew's hero #7 is now Jawhead! :robot: ")
        if message.content == "!ml hero7 add Kaja":
            mahero7 = "Kaja"
            await message.channel.send("Matthew's hero #7 is now Kaja! :bird: ")
        if message.content == "!ml hero7 add Lapu-Lapu":
            mahero7 = "Lapu-Lapu"
            await message.channel.send("Matthew's hero #7 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero7 add Leomord":
            mahero7 = "Leomord"
            await message.channel.send("Matthew's hero #7 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero7 add Martis":
            mahero7 = "Martis"
            await message.channel.send("Matthew's hero #7 is now Martis! :crab: ")
        if message.content == "!ml hero7 add Minsitthar":
            mahero7 = "Minsitthar"
            await message.channel.send("Matthew's hero #7 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero7 add Roger":
            mahero7 = "Roger"
            await message.channel.send("Matthew's hero #7 is now Roger! :wolf: ")
        if message.content == "!ml hero7 add Ruby":
            mahero7 = "Ruby"
            await message.channel.send("Matthew's hero #7 is now Ruby! :heart: ")
        if message.content == "!ml hero7 add Sun":
            mahero7 = "Sun"
            await message.channel.send("Matthew's hero #7 is now Sun! :monkey_face: ")
        if message.content == "!ml hero7 add Thamuz":
            mahero7 = "Thamuz"
            await message.channel.send("Matthew's hero #7 is now Thamuz! :rage: ")
        if message.content == "!ml hero7 add Terizla":
            mahero7 = "Terizla"
            await message.channel.send("Matthew's hero #7 is now Terizla! :hammer: ")
        if message.content == "!ml hero7 add Zilong":
            mahero7 = "Zilong"
            await message.channel.send("Matthew's hero #7 is now Zilong! :dragon: ")
        if message.content == "!ml hero7 add Fanny":
            mahero7 = "Fanny"
            await message.channel.send("Matthew's hero #7 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero7 add Gusion":
            mahero7 = "Gusion"
            await message.channel.send(
                "Matthew's hero #7 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero7 add Hanzo":
            mahero7 = "Hanzo"
            await message.channel.send("Matthew's hero #7 is now Hanzo! :ghost: ")
        if message.content == "!ml hero7 add Hayabusa":
            mahero7 = "Hayabusa"
            await message.channel.send("Matthew's hero #7 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero7 add Helcurt":
            mahero7 = "Helcurt"
            await message.channel.send("Matthew's hero #7 is now Helcurt! :mute:  ")
        if message.content == "!ml hero7 add Karina":
            mahero7 = "Karina"
            await message.channel.send("Matthew's hero #7 is now Karina! :purple_heart: ")
        if message.content == "!ml hero7 add Lancelot":
            mahero7 = "Lancelot"
            await message.channel.send("Matthew's hero #7 is now Lancelot! :fencer: ")
        if message.content == "!ml hero7 add Lesley":
            mahero7 = "Lesley"
            await message.channel.send("Matthew's hero #7 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero7 add Natalia":
            mahero7 = "Natalia"
            await message.channel.send("Matthew's hero #7 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero7 add Saber":
            mahero7 = "Saber"
            await message.channel.send("Matthew's hero #7 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero7 add Selena":
            mahero7 = "Selena"
            await message.channel.send("Matthew's hero #7 is now Selena! :sleeping:  ")
        if message.content == "!ml hero7 add Alice":
            mahero7 = "Alice"
            await message.channel.send("Matthew's hero #7 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero7 add Aurora":
            mahero7 = "Aurora"
            await message.channel.send("Matthew's hero #7 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            mahero7 = "Chang'e"
            await message.channel.send("Matthew's hero #7 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero7 add Cyclops":
            mahero7 = "Cyclops"
            await message.channel.send("Matthew's hero #7 is now Cyclops! :eye:  ")
        if message.content == "!ml hero7 add Eudora":
            mahero7 = "Eudora"
            await message.channel.send("Matthew's hero #7 is now Eudora! :zap: ")
        if message.content == "!ml hero7 add Faramis":
            mahero7 = "Faramis"
            await message.channel.send("Matthew's hero #7 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero7 add Gord":
            mahero7 = "Gord"
            await message.channel.send("Matthew's hero #7 is now Gord! :snowboarder:")
        if message.content == "!ml hero7 add Harith":
            mahero7 = "Harith"
            await message.channel.send("Matthew's hero #7 is now Harith! :older_man: ")
        if message.content == "!ml hero7 add Harley":
            mahero7 = "Harley"
            await message.channel.send("Matthew's hero #7 is now Harley! :tophat: ")
        if message.content == "!ml hero7 add Kadita":
            mahero7 = "Kadita"
            await message.channel.send("Matthew's hero #7 is now Kadita! :droplet: ")
        if message.content == "!ml hero7 add Kagura":
            mahero7 = "Kagura"
            await message.channel.send("Matthew's hero #7 is now Kagura! :umbrella7:  ")
        if message.content == "!ml hero7 add Lunox":
            mahero7 = "Lunox"
            await message.channel.send("Matthew's hero #7 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero7 add Lylia":
            mahero7 = "Lylia"
            await message.channel.send("Matthew's hero #7 is now Lylia! :boom: ")
        if message.content == "!ml hero7 add Nana":
            mahero7 = "Nana"
            await message.channel.send("Matthew's hero #7 is now Nana! :cat:  ")
        if message.content == "!ml hero7 add Odette":
            mahero7 = "Odette"
            await message.channel.send("Matthew's hero #7 is now Odette! :duck: ")
        if message.content == "!ml hero7 add Pharsa":
            mahero7 = "Pharsa"
            await message.channel.send("Matthew's hero #7 is now Pharsa! :dove:  ")
        if message.content == "!ml hero7 add Vale":
            mahero7 = "Vale"
            await message.channel.send("Matthew's hero #7 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero7 add Valir":
            mahero7 = "Valir"
            await message.channel.send("Matthew's hero #7 is now Valir! :fire:")
        if message.content == "!ml hero7 add Vexanna":
            mahero7 = "Vexanna"
            await message.channel.send("Matthew's hero #7 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero7 add Bruno":
            mahero7 = "Bruno"
            await message.channel.send("Matthew's hero #7 is now Bruno! :soccer:  ")
        if message.content == "!ml hero7 add Claude":
            mahero7 = "Claude"
            await message.channel.send("Matthew's hero #7 is now Claude! :monkey:  ")
        if message.content == "!ml hero7 add Clint":
            mahero7 = "Clint"
            await message.channel.send("Matthew's hero #7 is now Clint! :cowboy: ")
        if message.content == "!ml hero7 add Granger":
            mahero7 = "Granger"
            await message.channel.send("Matthew's hero #7 is now Granger! :violin: ")
        if message.content == "!ml hero7 add Hanabi":
            mahero7 = "Hanabi"
            await message.channel.send("Matthew's hero #7 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero7 add Irithel":
            mahero7 = "Irithel"
            await message.channel.send("Matthew's hero #7 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero7 add Karrie":
            mahero7 = "Karrie"
            await message.channel.send(
                "Matthew's hero #7 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero7 add Kimmy":
            mahero7 = "Kimmy"
            await message.channel.send("Matthew's hero #7 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero7 add Layla":
            mahero7 = "Layla"
            await message.channel.send("Matthew's hero #7 is now Layla! :haircut:  ")
        if message.content == "!ml hero7 add Miya":
            mahero7 = "Miya"
            await message.channel.send("Matthew's hero #7 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero7 add Moskov":
            mahero7 = "Moskov"
            await message.channel.send("Matthew's hero #7 is now Moskov! :imp: ")
        if message.content == "!ml hero7 add Yi Sun-Shin":
            mahero7 = "Yi Sun-Shin"
            await message.channel.send("Matthew's hero #7 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero7 add Angela":
            mahero7 = "Angela"
            await message.channel.send("Matthew's hero #7 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero7 add Diggie":
            mahero7 = "Diggie"
            await message.channel.send("Matthew's hero #7 is now Diggie! :owl: ")
        if message.content == "!ml hero7 add Estes":
            mahero7 = "Estes"
            await message.channel.send("Matthew's hero #7 is now Estes! :ear:  ")
        if message.content == "!ml hero7 add Rafaela":
            mahero7 = "Rafaela"
            await message.channel.send("Matthew's hero #7 is now Rafaela! :angel: ")
        if message.content == "!ml hero7 add Rynn":
            mahero7 = "Rynn"
            await message.channel.send("Matthew's hero #7 is now Rynn! ")
        if message.content == "!ml hero8 add Akai":
            global mahero8
            mahero8 = "Akai"
            await message.channel.send("Matthew's hero #8 is now Akai! :panda_face: ")
        if message.content == "!ml hero8 add Balmond":
            mahero8 = "Balmond"
            await message.channel.send("Matthew's hero #8 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero8 add Belerick":
            mahero8 = "Belerick"
            await message.channel.send("Matthew's hero #8 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero8 add Franco":
            mahero8 = "Franco"
            await message.channel.send("Matthew's hero #8 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero8 add Esmerelda":
            mahero8 = "Esmerelda"
            await message.channel.send("Matthew's hero #8 is now Esmerelda! :shield: ")
        if message.content == "!ml hero8 add Gatotkaca":
            mahero8 = "Gatotkaca"
            await message.channel.send("Matthew's hero #8 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero8 add Grock":
            mahero8 = "Grock"
            await message.channel.send("Matthew's hero #8 is now Grock! :european_castle: ")
        if message.content == "!ml hero8 add Hilda":
            mahero8 = "Hilda"
            await message.channel.send("Matthew's hero #8 is now Hilda! :runner: ")
        if message.content == "!ml hero8 add Hylos":
            mahero8 = "Hylos"
            await message.channel.send("Matthew's hero #8 is now Hylos! :unicorn: ")
        if message.content == "!ml hero8 add Johnson":
            mahero8 = "Johnson"
            await message.channel.send("Matthew's hero #8 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero8 add Khufra":
            mahero8 = "Khufra"
            await message.channel.send("Matthew's hero #8 is now Khufra! :clown: ")
        if message.content == "!ml hero8 add Lolita":
            mahero8 = "Lolita"
            await message.channel.send("Matthew's hero #8 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            mahero8 = "Masha"
            await message.channel.send("Matthew's hero #8 is now Masha! :bear: ")
        if message.content == "!ml hero8 add Minotaur":
            mahero8 = "Minotaur"
            await message.channel.send("Matthew's hero #8 is now Minotaur! :cow: ")
        if message.content == "!ml hero8 add Tigreal":
            mahero8 = "Tigreal"
            await message.channel.send("Matthew's hero #8 is now Tigreal! :moyai: ")
        if message.content == "!ml hero8 add Uranus":
            mahero8 = "Uranus"
            await message.channel.send("Matthew's hero #8 is now Uranus! :peach: ")
        if message.content == "!ml hero8 add X.Borg":
            mahero8 = "X.Borg"
            await message.channel.send("Matthew's hero #8 is now X.Borg! :fire: ")
        if message.content == "!ml hero8 add Aldous":
            mahero8 = "Aldous"
            await message.channel.send("Matthew's hero #8 is now Aldous! :fist: ")
        if message.content == "!ml hero8 add Alpha":
            mahero8 = "Alpha"
            await message.channel.send("Matthew's hero #8 is now Alpha! :airplane: ")
        if message.content == "!ml hero8 add Alucard":
            mahero8 = "Alucard"
            await message.channel.send("Matthew's hero #8 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero8 add Argus":
            mahero8 = "Argus"
            await message.channel.send("Matthew's hero #8 is now Argus! :angel: ")
        if message.content == "!ml hero8 add Badang":
            mahero8 = "Badang"
            await message.channel.send("Matthew's hero #8 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero8 add Bane":
            mahero8 = "Bane"
            await message.channel.send("Matthew's hero #8 is now Bane! :octopus: ")
        if message.content == "!ml hero8 add Chou":
            mahero8 = "Chou"
            await message.channel.send("Matthew's hero #8 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero8 add Dyrroth":
            mahero8 = "Dyrroth"
            await message.channel.send("Matthew's hero #8 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero8 add Freya":
            mahero8 = "Freya"
            await message.channel.send("Matthew's hero #8 is now Freya! :hammer: ")
        if message.content == "!ml hero8 add Guinevere":
            mahero8 = "Guinevere"
            await message.channel.send("Matthew's hero #8 is now Guinevere! :dress:  ")
        if message.content == "!ml hero8 add Jawhead":
            mahero8 = "Jawhead"
            await message.channel.send("Matthew's hero #8 is now Jawhead! :robot: ")
        if message.content == "!ml hero8 add Kaja":
            mahero8 = "Kaja"
            await message.channel.send("Matthew's hero #8 is now Kaja! :bird: ")
        if message.content == "!ml hero8 add Lapu-Lapu":
            mahero8 = "Lapu-Lapu"
            await message.channel.send("Matthew's hero #8 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero8 add Leomord":
            mahero8 = "Leomord"
            await message.channel.send("Matthew's hero #8 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero8 add Martis":
            mahero8 = "Martis"
            await message.channel.send("Matthew's hero #8 is now Martis! :crab: ")
        if message.content == "!ml hero8 add Minsitthar":
            mahero8 = "Minsitthar"
            await message.channel.send("Matthew's hero #8 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero8 add Roger":
            mahero8 = "Roger"
            await message.channel.send("Matthew's hero #8 is now Roger! :wolf: ")
        if message.content == "!ml hero8 add Ruby":
            mahero8 = "Ruby"
            await message.channel.send("Matthew's hero #8 is now Ruby! :heart: ")
        if message.content == "!ml hero8 add Sun":
            mahero8 = "Sun"
            await message.channel.send("Matthew's hero #8 is now Sun! :monkey_face: ")
        if message.content == "!ml hero8 add Thamuz":
            mahero8 = "Thamuz"
            await message.channel.send("Matthew's hero #8 is now Thamuz! :rage: ")
        if message.content == "!ml hero8 add Terizla":
            mahero8 = "Terizla"
            await message.channel.send("Matthew's hero #8 is now Terizla! :hammer: ")
        if message.content == "!ml hero8 add Zilong":
            mahero8 = "Zilong"
            await message.channel.send("Matthew's hero #8 is now Zilong! :dragon: ")
        if message.content == "!ml hero8 add Fanny":
            mahero8 = "Fanny"
            await message.channel.send("Matthew's hero #8 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero8 add Gusion":
            mahero8 = "Gusion"
            await message.channel.send(
                "Matthew's hero #8 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero8 add Hanzo":
            mahero8 = "Hanzo"
            await message.channel.send("Matthew's hero #8 is now Hanzo! :ghost: ")
        if message.content == "!ml hero8 add Hayabusa":
            mahero8 = "Hayabusa"
            await message.channel.send("Matthew's hero #8 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero8 add Helcurt":
            mahero8 = "Helcurt"
            await message.channel.send("Matthew's hero #8 is now Helcurt! :mute:  ")
        if message.content == "!ml hero8 add Karina":
            mahero8 = "Karina"
            await message.channel.send("Matthew's hero #8 is now Karina! :purple_heart: ")
        if message.content == "!ml hero8 add Lancelot":
            mahero8 = "Lancelot"
            await message.channel.send("Matthew's hero #8 is now Lancelot! :fencer: ")
        if message.content == "!ml hero8 add Lesley":
            mahero8 = "Lesley"
            await message.channel.send("Matthew's hero #8 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero8 add Natalia":
            mahero8 = "Natalia"
            await message.channel.send("Matthew's hero #8 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero8 add Saber":
            mahero8 = "Saber"
            await message.channel.send("Matthew's hero #8 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero8 add Selena":
            mahero8 = "Selena"
            await message.channel.send("Matthew's hero #8 is now Selena! :sleeping:  ")
        if message.content == "!ml hero8 add Alice":
            mahero8 = "Alice"
            await message.channel.send("Matthew's hero #8 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero8 add Aurora":
            mahero8 = "Aurora"
            await message.channel.send("Matthew's hero #8 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            mahero8 = "Chang'e"
            await message.channel.send("Matthew's hero #8 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero8 add Cyclops":
            mahero8 = "Cyclops"
            await message.channel.send("Matthew's hero #8 is now Cyclops! :eye:  ")
        if message.content == "!ml hero8 add Eudora":
            mahero8 = "Eudora"
            await message.channel.send("Matthew's hero #8 is now Eudora! :zap: ")
        if message.content == "!ml hero8 add Faramis":
            mahero8 = "Faramis"
            await message.channel.send("Matthew's hero #8 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero8 add Gord":
            mahero8 = "Gord"
            await message.channel.send("Matthew's hero #8 is now Gord! :snowboarder:")
        if message.content == "!ml hero8 add Harith":
            mahero8 = "Harith"
            await message.channel.send("Matthew's hero #8 is now Harith! :older_man: ")
        if message.content == "!ml hero8 add Harley":
            mahero8 = "Harley"
            await message.channel.send("Matthew's hero #8 is now Harley! :tophat: ")
        if message.content == "!ml hero8 add Kadita":
            mahero8 = "Kadita"
            await message.channel.send("Matthew's hero #8 is now Kadita! :droplet: ")
        if message.content == "!ml hero8 add Kagura":
            mahero8 = "Kagura"
            await message.channel.send("Matthew's hero #8 is now Kagura! :umbrella8:  ")
        if message.content == "!ml hero8 add Lunox":
            mahero8 = "Lunox"
            await message.channel.send("Matthew's hero #8 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero8 add Lylia":
            mahero8 = "Lylia"
            await message.channel.send("Matthew's hero #8 is now Lylia! :boom: ")
        if message.content == "!ml hero8 add Nana":
            mahero8 = "Nana"
            await message.channel.send("Matthew's hero #8 is now Nana! :cat:  ")
        if message.content == "!ml hero8 add Odette":
            mahero8 = "Odette"
            await message.channel.send("Matthew's hero #8 is now Odette! :duck: ")
        if message.content == "!ml hero8 add Pharsa":
            mahero8 = "Pharsa"
            await message.channel.send("Matthew's hero #8 is now Pharsa! :dove:  ")
        if message.content == "!ml hero8 add Vale":
            mahero8 = "Vale"
            await message.channel.send("Matthew's hero #8 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero8 add Valir":
            mahero8 = "Valir"
            await message.channel.send("Matthew's hero #8 is now Valir! :fire:")
        if message.content == "!ml hero8 add Vexanna":
            mahero8 = "Vexanna"
            await message.channel.send("Matthew's hero #8 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero8 add Bruno":
            mahero8 = "Bruno"
            await message.channel.send("Matthew's hero #8 is now Bruno! :soccer:  ")
        if message.content == "!ml hero8 add Claude":
            mahero8 = "Claude"
            await message.channel.send("Matthew's hero #8 is now Claude! :monkey:  ")
        if message.content == "!ml hero8 add Clint":
            mahero8 = "Clint"
            await message.channel.send("Matthew's hero #8 is now Clint! :cowboy: ")
        if message.content == "!ml hero8 add Granger":
            mahero8 = "Granger"
            await message.channel.send("Matthew's hero #8 is now Granger! :violin: ")
        if message.content == "!ml hero8 add Hanabi":
            mahero8 = "Hanabi"
            await message.channel.send("Matthew's hero #8 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero8 add Irithel":
            mahero8 = "Irithel"
            await message.channel.send("Matthew's hero #8 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero8 add Karrie":
            mahero8 = "Karrie"
            await message.channel.send(
                "Matthew's hero #8 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero8 add Kimmy":
            mahero8 = "Kimmy"
            await message.channel.send("Matthew's hero #8 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero8 add Layla":
            mahero8 = "Layla"
            await message.channel.send("Matthew's hero #8 is now Layla! :haircut:  ")
        if message.content == "!ml hero8 add Miya":
            mahero8 = "Miya"
            await message.channel.send("Matthew's hero #8 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero8 add Moskov":
            mahero8 = "Moskov"
            await message.channel.send("Matthew's hero #8 is now Moskov! :imp: ")
        if message.content == "!ml hero8 add Yi Sun-Shin":
            mahero8 = "Yi Sun-Shin"
            await message.channel.send("Matthew's hero #8 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero8 add Angela":
            mahero8 = "Angela"
            await message.channel.send("Matthew's hero #8 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero8 add Diggie":
            mahero8 = "Diggie"
            await message.channel.send("Matthew's hero #8 is now Diggie! :owl: ")
        if message.content == "!ml hero8 add Estes":
            mahero8 = "Estes"
            await message.channel.send("Matthew's hero #8 is now Estes! :ear:  ")
        if message.content == "!ml hero8 add Rafaela":
            mahero8 = "Rafaela"
            await message.channel.send("Matthew's hero #8 is now Rafaela! :angel: ")
        if message.content == "!ml hero8 add Rynn":
            mahero8 = "Rynn"
            await message.channel.send("Matthew's hero #8 is now Rynn! ")
        if message.content == "!ml hero9 add Akai":
            global mahero9
            mahero9 = "Akai"
            await message.channel.send("Matthew's hero #9 is now Akai! :panda_face: ")
        if message.content == "!ml hero9 add Balmond":
            mahero9 = "Balmond"
            await message.channel.send("Matthew's hero #9 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero9 add Belerick":
            mahero9 = "Belerick"
            await message.channel.send("Matthew's hero #9 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero9 add Franco":
            mahero9 = "Franco"
            await message.channel.send("Matthew's hero #9 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero9 add Esmerelda":
            mahero9 = "Esmerelda"
            await message.channel.send("Matthew's hero #9 is now Esmerelda! :shield: ")
        if message.content == "!ml hero9 add Gatotkaca":
            mahero9 = "Gatotkaca"
            await message.channel.send("Matthew's hero #9 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero9 add Grock":
            mahero9 = "Grock"
            await message.channel.send("Matthew's hero #9 is now Grock! :european_castle: ")
        if message.content == "!ml hero9 add Hilda":
            mahero9 = "Hilda"
            await message.channel.send("Matthew's hero #9 is now Hilda! :runner: ")
        if message.content == "!ml hero9 add Hylos":
            mahero9 = "Hylos"
            await message.channel.send("Matthew's hero #9 is now Hylos! :unicorn: ")
        if message.content == "!ml hero9 add Johnson":
            mahero9 = "Johnson"
            await message.channel.send("Matthew's hero #9 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero9 add Khufra":
            mahero9 = "Khufra"
            await message.channel.send("Matthew's hero #9 is now Khufra! :clown: ")
        if message.content == "!ml hero9 add Lolita":
            mahero9 = "Lolita"
            await message.channel.send("Matthew's hero #9 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            mahero9 = "Masha"
            await message.channel.send("Matthew's hero #9 is now Masha! :bear: ")
        if message.content == "!ml hero9 add Minotaur":
            mahero9 = "Minotaur"
            await message.channel.send("Matthew's hero #9 is now Minotaur! :cow: ")
        if message.content == "!ml hero9 add Tigreal":
            mahero9 = "Tigreal"
            await message.channel.send("Matthew's hero #9 is now Tigreal! :moyai: ")
        if message.content == "!ml hero9 add Uranus":
            mahero9 = "Uranus"
            await message.channel.send("Matthew's hero #9 is now Uranus! :peach: ")
        if message.content == "!ml hero9 add X.Borg":
            mahero9 = "X.Borg"
            await message.channel.send("Matthew's hero #9 is now X.Borg! :fire: ")
        if message.content == "!ml hero9 add Aldous":
            mahero9 = "Aldous"
            await message.channel.send("Matthew's hero #9 is now Aldous! :fist: ")
        if message.content == "!ml hero9 add Alpha":
            mahero9 = "Alpha"
            await message.channel.send("Matthew's hero #9 is now Alpha! :airplane: ")
        if message.content == "!ml hero9 add Alucard":
            mahero9 = "Alucard"
            await message.channel.send("Matthew's hero #9 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero9 add Argus":
            mahero9 = "Argus"
            await message.channel.send("Matthew's hero #9 is now Argus! :angel: ")
        if message.content == "!ml hero9 add Badang":
            mahero9 = "Badang"
            await message.channel.send("Matthew's hero #9 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero9 add Bane":
            mahero9 = "Bane"
            await message.channel.send("Matthew's hero #9 is now Bane! :octopus: ")
        if message.content == "!ml hero9 add Chou":
            mahero9 = "Chou"
            await message.channel.send("Matthew's hero #9 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero9 add Dyrroth":
            mahero9 = "Dyrroth"
            await message.channel.send("Matthew's hero #9 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero9 add Freya":
            mahero9 = "Freya"
            await message.channel.send("Matthew's hero #9 is now Freya! :hammer: ")
        if message.content == "!ml hero9 add Guinevere":
            mahero9 = "Guinevere"
            await message.channel.send("Matthew's hero #9 is now Guinevere! :dress:  ")
        if message.content == "!ml hero9 add Jawhead":
            mahero9 = "Jawhead"
            await message.channel.send("Matthew's hero #9 is now Jawhead! :robot: ")
        if message.content == "!ml hero9 add Kaja":
            mahero9 = "Kaja"
            await message.channel.send("Matthew's hero #9 is now Kaja! :bird: ")
        if message.content == "!ml hero9 add Lapu-Lapu":
            mahero9 = "Lapu-Lapu"
            await message.channel.send("Matthew's hero #9 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero9 add Leomord":
            mahero9 = "Leomord"
            await message.channel.send("Matthew's hero #9 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero9 add Martis":
            mahero9 = "Martis"
            await message.channel.send("Matthew's hero #9 is now Martis! :crab: ")
        if message.content == "!ml hero9 add Minsitthar":
            mahero9 = "Minsitthar"
            await message.channel.send("Matthew's hero #9 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero9 add Roger":
            mahero9 = "Roger"
            await message.channel.send("Matthew's hero #9 is now Roger! :wolf: ")
        if message.content == "!ml hero9 add Ruby":
            mahero9 = "Ruby"
            await message.channel.send("Matthew's hero #9 is now Ruby! :heart: ")
        if message.content == "!ml hero9 add Sun":
            mahero9 = "Sun"
            await message.channel.send("Matthew's hero #9 is now Sun! :monkey_face: ")
        if message.content == "!ml hero9 add Thamuz":
            mahero9 = "Thamuz"
            await message.channel.send("Matthew's hero #9 is now Thamuz! :rage: ")
        if message.content == "!ml hero9 add Terizla":
            mahero9 = "Terizla"
            await message.channel.send("Matthew's hero #9 is now Terizla! :hammer: ")
        if message.content == "!ml hero9 add Zilong":
            mahero9 = "Zilong"
            await message.channel.send("Matthew's hero #9 is now Zilong! :dragon: ")
        if message.content == "!ml hero9 add Fanny":
            mahero9 = "Fanny"
            await message.channel.send("Matthew's hero #9 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero9 add Gusion":
            mahero9 = "Gusion"
            await message.channel.send(
                "Matthew's hero #9 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero9 add Hanzo":
            mahero9 = "Hanzo"
            await message.channel.send("Matthew's hero #9 is now Hanzo! :ghost: ")
        if message.content == "!ml hero9 add Hayabusa":
            mahero9 = "Hayabusa"
            await message.channel.send("Matthew's hero #9 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero9 add Helcurt":
            mahero9 = "Helcurt"
            await message.channel.send("Matthew's hero #9 is now Helcurt! :mute:  ")
        if message.content == "!ml hero9 add Karina":
            mahero9 = "Karina"
            await message.channel.send("Matthew's hero #9 is now Karina! :purple_heart: ")
        if message.content == "!ml hero9 add Lancelot":
            mahero9 = "Lancelot"
            await message.channel.send("Matthew's hero #9 is now Lancelot! :fencer: ")
        if message.content == "!ml hero9 add Lesley":
            mahero9 = "Lesley"
            await message.channel.send("Matthew's hero #9 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero9 add Natalia":
            mahero9 = "Natalia"
            await message.channel.send("Matthew's hero #9 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero9 add Saber":
            mahero9 = "Saber"
            await message.channel.send("Matthew's hero #9 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero9 add Selena":
            mahero9 = "Selena"
            await message.channel.send("Matthew's hero #9 is now Selena! :sleeping:  ")
        if message.content == "!ml hero9 add Alice":
            mahero9 = "Alice"
            await message.channel.send("Matthew's hero #9 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero9 add Aurora":
            mahero9 = "Aurora"
            await message.channel.send("Matthew's hero #9 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            mahero9 = "Chang'e"
            await message.channel.send("Matthew's hero #9 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero9 add Cyclops":
            mahero9 = "Cyclops"
            await message.channel.send("Matthew's hero #9 is now Cyclops! :eye:  ")
        if message.content == "!ml hero9 add Eudora":
            mahero9 = "Eudora"
            await message.channel.send("Matthew's hero #9 is now Eudora! :zap: ")
        if message.content == "!ml hero9 add Faramis":
            mahero9 = "Faramis"
            await message.channel.send("Matthew's hero #9 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero9 add Gord":
            mahero9 = "Gord"
            await message.channel.send("Matthew's hero #9 is now Gord! :snowboarder:")
        if message.content == "!ml hero9 add Harith":
            mahero9 = "Harith"
            await message.channel.send("Matthew's hero #9 is now Harith! :older_man: ")
        if message.content == "!ml hero9 add Harley":
            mahero9 = "Harley"
            await message.channel.send("Matthew's hero #9 is now Harley! :tophat: ")
        if message.content == "!ml hero9 add Kadita":
            mahero9 = "Kadita"
            await message.channel.send("Matthew's hero #9 is now Kadita! :droplet: ")
        if message.content == "!ml hero9 add Kagura":
            mahero9 = "Kagura"
            await message.channel.send("Matthew's hero #9 is now Kagura! :umbrella9:  ")
        if message.content == "!ml hero9 add Lunox":
            mahero9 = "Lunox"
            await message.channel.send("Matthew's hero #9 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero9 add Lylia":
            mahero9 = "Lylia"
            await message.channel.send("Matthew's hero #9 is now Lylia! :boom: ")
        if message.content == "!ml hero9 add Nana":
            mahero9 = "Nana"
            await message.channel.send("Matthew's hero #9 is now Nana! :cat:  ")
        if message.content == "!ml hero9 add Odette":
            mahero9 = "Odette"
            await message.channel.send("Matthew's hero #9 is now Odette! :duck: ")
        if message.content == "!ml hero9 add Pharsa":
            mahero9 = "Pharsa"
            await message.channel.send("Matthew's hero #9 is now Pharsa! :dove:  ")
        if message.content == "!ml hero9 add Vale":
            mahero9 = "Vale"
            await message.channel.send("Matthew's hero #9 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero9 add Valir":
            mahero9 = "Valir"
            await message.channel.send("Matthew's hero #9 is now Valir! :fire:")
        if message.content == "!ml hero9 add Vexanna":
            mahero9 = "Vexanna"
            await message.channel.send("Matthew's hero #9 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero9 add Bruno":
            mahero9 = "Bruno"
            await message.channel.send("Matthew's hero #9 is now Bruno! :soccer:  ")
        if message.content == "!ml hero9 add Claude":
            mahero9 = "Claude"
            await message.channel.send("Matthew's hero #9 is now Claude! :monkey:  ")
        if message.content == "!ml hero9 add Clint":
            mahero9 = "Clint"
            await message.channel.send("Matthew's hero #9 is now Clint! :cowboy: ")
        if message.content == "!ml hero9 add Granger":
            mahero9 = "Granger"
            await message.channel.send("Matthew's hero #9 is now Granger! :violin: ")
        if message.content == "!ml hero9 add Hanabi":
            mahero9 = "Hanabi"
            await message.channel.send("Matthew's hero #9 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero9 add Irithel":
            mahero9 = "Irithel"
            await message.channel.send("Matthew's hero #9 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero9 add Karrie":
            mahero9 = "Karrie"
            await message.channel.send(
                "Matthew's hero #9 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero9 add Kimmy":
            mahero9 = "Kimmy"
            await message.channel.send("Matthew's hero #9 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero9 add Layla":
            mahero9 = "Layla"
            await message.channel.send("Matthew's hero #9 is now Layla! :haircut:  ")
        if message.content == "!ml hero9 add Miya":
            mahero9 = "Miya"
            await message.channel.send("Matthew's hero #9 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero9 add Moskov":
            mahero9 = "Moskov"
            await message.channel.send("Matthew's hero #9 is now Moskov! :imp: ")
        if message.content == "!ml hero9 add Yi Sun-Shin":
            mahero9 = "Yi Sun-Shin"
            await message.channel.send("Matthew's hero #9 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero9 add Angela":
            mahero9 = "Angela"
            await message.channel.send("Matthew's hero #9 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero9 add Diggie":
            mahero9 = "Diggie"
            await message.channel.send("Matthew's hero #9 is now Diggie! :owl: ")
        if message.content == "!ml hero9 add Estes":
            mahero9 = "Estes"
            await message.channel.send("Matthew's hero #9 is now Estes! :ear:  ")
        if message.content == "!ml hero9 add Rafaela":
            mahero9 = "Rafaela"
            await message.channel.send("Matthew's hero #9 is now Rafaela! :angel: ")
        if message.content == "!ml hero9 add Rynn":
            mahero9 = "Rynn"
            await message.channel.send("Matthew's hero #9 is now Rynn! ")
        if message.content == "!ml hero10 add Akai":
            global mahero10
            mahero10 = "Akai"
            await message.channel.send("Matthew's hero #10 is now Akai! :panda_face: ")
        if message.content == "!ml hero10 add Balmond":
            mahero10 = "Balmond"
            await message.channel.send("Matthew's hero #10 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero10 add Belerick":
            mahero10 = "Belerick"
            await message.channel.send("Matthew's hero #10 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero10 add Franco":
            mahero10 = "Franco"
            await message.channel.send("Matthew's hero #10 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero10 add Esmerelda":
            mahero10 = "Esmerelda"
            await message.channel.send("Matthew's hero #10 is now Esmerelda! :shield: ")
        if message.content == "!ml hero10 add Gatotkaca":
            mahero10 = "Gatotkaca"
            await message.channel.send("Matthew's hero #10 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero10 add Grock":
            mahero10 = "Grock"
            await message.channel.send("Matthew's hero #10 is now Grock! :european_castle: ")
        if message.content == "!ml hero10 add Hilda":
            mahero10 = "Hilda"
            await message.channel.send("Matthew's hero #10 is now Hilda! :runner: ")
        if message.content == "!ml hero10 add Hylos":
            mahero10 = "Hylos"
            await message.channel.send("Matthew's hero #10 is now Hylos! :unicorn: ")
        if message.content == "!ml hero10 add Johnson":
            mahero10 = "Johnson"
            await message.channel.send("Matthew's hero #10 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero10 add Khufra":
            mahero10 = "Khufra"
            await message.channel.send("Matthew's hero #10 is now Khufra! :clown: ")
        if message.content == "!ml hero10 add Lolita":
            mahero10 = "Lolita"
            await message.channel.send("Matthew's hero #10 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            mahero10 = "Masha"
            await message.channel.send("Matthew's hero #10 is now Masha! :bear: ")
        if message.content == "!ml hero10 add Minotaur":
            mahero10 = "Minotaur"
            await message.channel.send("Matthew's hero #10 is now Minotaur! :cow: ")
        if message.content == "!ml hero10 add Tigreal":
            mahero10 = "Tigreal"
            await message.channel.send("Matthew's hero #10 is now Tigreal! :moyai: ")
        if message.content == "!ml hero10 add Uranus":
            mahero10 = "Uranus"
            await message.channel.send("Matthew's hero #10 is now Uranus! :peach: ")
        if message.content == "!ml hero10 add X.Borg":
            mahero10 = "X.Borg"
            await message.channel.send("Matthew's hero #10 is now X.Borg! :fire: ")
        if message.content == "!ml hero10 add Aldous":
            mahero10 = "Aldous"
            await message.channel.send("Matthew's hero #10 is now Aldous! :fist: ")
        if message.content == "!ml hero10 add Alpha":
            mahero10 = "Alpha"
            await message.channel.send("Matthew's hero #10 is now Alpha! :airplane: ")
        if message.content == "!ml hero10 add Alucard":
            mahero10 = "Alucard"
            await message.channel.send("Matthew's hero #10 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero10 add Argus":
            mahero10 = "Argus"
            await message.channel.send("Matthew's hero #10 is now Argus! :angel: ")
        if message.content == "!ml hero10 add Badang":
            mahero10 = "Badang"
            await message.channel.send("Matthew's hero #10 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero10 add Bane":
            mahero10 = "Bane"
            await message.channel.send("Matthew's hero #10 is now Bane! :octopus: ")
        if message.content == "!ml hero10 add Chou":
            mahero10 = "Chou"
            await message.channel.send("Matthew's hero #10 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero10 add Dyrroth":
            mahero10 = "Dyrroth"
            await message.channel.send("Matthew's hero #10 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero10 add Freya":
            mahero10 = "Freya"
            await message.channel.send("Matthew's hero #10 is now Freya! :hammer: ")
        if message.content == "!ml hero10 add Guinevere":
            mahero10 = "Guinevere"
            await message.channel.send("Matthew's hero #10 is now Guinevere! :dress:  ")
        if message.content == "!ml hero10 add Jawhead":
            mahero10 = "Jawhead"
            await message.channel.send("Matthew's hero #10 is now Jawhead! :robot: ")
        if message.content == "!ml hero10 add Kaja":
            mahero10 = "Kaja"
            await message.channel.send("Matthew's hero #10 is now Kaja! :bird: ")
        if message.content == "!ml hero10 add Lapu-Lapu":
            mahero10 = "Lapu-Lapu"
            await message.channel.send("Matthew's hero #10 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero10 add Leomord":
            mahero10 = "Leomord"
            await message.channel.send("Matthew's hero #10 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero10 add Martis":
            mahero10 = "Martis"
            await message.channel.send("Matthew's hero #10 is now Martis! :crab: ")
        if message.content == "!ml hero10 add Minsitthar":
            mahero10 = "Minsitthar"
            await message.channel.send("Matthew's hero #10 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero10 add Roger":
            mahero10 = "Roger"
            await message.channel.send("Matthew's hero #10 is now Roger! :wolf: ")
        if message.content == "!ml hero10 add Ruby":
            mahero10 = "Ruby"
            await message.channel.send("Matthew's hero #10 is now Ruby! :heart: ")
        if message.content == "!ml hero10 add Sun":
            mahero10 = "Sun"
            await message.channel.send("Matthew's hero #10 is now Sun! :monkey_face: ")
        if message.content == "!ml hero10 add Thamuz":
            mahero10 = "Thamuz"
            await message.channel.send("Matthew's hero #10 is now Thamuz! :rage: ")
        if message.content == "!ml hero10 add Terizla":
            mahero10 = "Terizla"
            await message.channel.send("Matthew's hero #10 is now Terizla! :hammer: ")
        if message.content == "!ml hero10 add Zilong":
            mahero10 = "Zilong"
            await message.channel.send("Matthew's hero #10 is now Zilong! :dragon: ")
        if message.content == "!ml hero10 add Fanny":
            mahero10 = "Fanny"
            await message.channel.send("Matthew's hero #10 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero10 add Gusion":
            mahero10 = "Gusion"
            await message.channel.send(
                "Matthew's hero #10 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero10 add Hanzo":
            mahero10 = "Hanzo"
            await message.channel.send("Matthew's hero #10 is now Hanzo! :ghost: ")
        if message.content == "!ml hero10 add Hayabusa":
            mahero10 = "Hayabusa"
            await message.channel.send("Matthew's hero #10 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero10 add Helcurt":
            mahero10 = "Helcurt"
            await message.channel.send("Matthew's hero #10 is now Helcurt! :mute:  ")
        if message.content == "!ml hero10 add Karina":
            mahero10 = "Karina"
            await message.channel.send("Matthew's hero #10 is now Karina! :purple_heart: ")
        if message.content == "!ml hero10 add Lancelot":
            mahero10 = "Lancelot"
            await message.channel.send("Matthew's hero #10 is now Lancelot! :fencer: ")
        if message.content == "!ml hero10 add Lesley":
            mahero10 = "Lesley"
            await message.channel.send("Matthew's hero #10 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero10 add Natalia":
            mahero10 = "Natalia"
            await message.channel.send("Matthew's hero #10 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero10 add Saber":
            mahero10 = "Saber"
            await message.channel.send("Matthew's hero #10 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero10 add Selena":
            mahero10 = "Selena"
            await message.channel.send("Matthew's hero #10 is now Selena! :sleeping:  ")
        if message.content == "!ml hero10 add Alice":
            mahero10 = "Alice"
            await message.channel.send("Matthew's hero #10 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero10 add Aurora":
            mahero10 = "Aurora"
            await message.channel.send("Matthew's hero #10 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            mahero10 = "Chang'e"
            await message.channel.send("Matthew's hero #10 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero10 add Cyclops":
            mahero10 = "Cyclops"
            await message.channel.send("Matthew's hero #10 is now Cyclops! :eye:  ")
        if message.content == "!ml hero10 add Eudora":
            mahero10 = "Eudora"
            await message.channel.send("Matthew's hero #10 is now Eudora! :zap: ")
        if message.content == "!ml hero10 add Faramis":
            mahero10 = "Faramis"
            await message.channel.send("Matthew's hero #10 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero10 add Gord":
            mahero10 = "Gord"
            await message.channel.send("Matthew's hero #10 is now Gord! :snowboarder:")
        if message.content == "!ml hero10 add Harith":
            mahero10 = "Harith"
            await message.channel.send("Matthew's hero #10 is now Harith! :older_man: ")
        if message.content == "!ml hero10 add Harley":
            mahero10 = "Harley"
            await message.channel.send("Matthew's hero #10 is now Harley! :tophat: ")
        if message.content == "!ml hero10 add Kadita":
            mahero10 = "Kadita"
            await message.channel.send("Matthew's hero #10 is now Kadita! :droplet: ")
        if message.content == "!ml hero10 add Kagura":
            mahero10 = "Kagura"
            await message.channel.send("Matthew's hero #10 is now Kagura! :umbrella10:  ")
        if message.content == "!ml hero10 add Lunox":
            mahero10 = "Lunox"
            await message.channel.send("Matthew's hero #10 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero10 add Lylia":
            mahero10 = "Lylia"
            await message.channel.send("Matthew's hero #10 is now Lylia! :boom: ")
        if message.content == "!ml hero10 add Nana":
            mahero10 = "Nana"
            await message.channel.send("Matthew's hero #10 is now Nana! :cat:  ")
        if message.content == "!ml hero10 add Odette":
            mahero10 = "Odette"
            await message.channel.send("Matthew's hero #10 is now Odette! :duck: ")
        if message.content == "!ml hero10 add Pharsa":
            mahero10 = "Pharsa"
            await message.channel.send("Matthew's hero #10 is now Pharsa! :dove:  ")
        if message.content == "!ml hero10 add Vale":
            mahero10 = "Vale"
            await message.channel.send("Matthew's hero #10 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero10 add Valir":
            mahero10 = "Valir"
            await message.channel.send("Matthew's hero #10 is now Valir! :fire:")
        if message.content == "!ml hero10 add Vexanna":
            mahero10 = "Vexanna"
            await message.channel.send("Matthew's hero #10 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero10 add Bruno":
            mahero10 = "Bruno"
            await message.channel.send("Matthew's hero #10 is now Bruno! :soccer:  ")
        if message.content == "!ml hero10 add Claude":
            mahero10 = "Claude"
            await message.channel.send("Matthew's hero #10 is now Claude! :monkey:  ")
        if message.content == "!ml hero10 add Clint":
            mahero10 = "Clint"
            await message.channel.send("Matthew's hero #10 is now Clint! :cowboy: ")
        if message.content == "!ml hero10 add Granger":
            mahero10 = "Granger"
            await message.channel.send("Matthew's hero #10 is now Granger! :violin: ")
        if message.content == "!ml hero10 add Hanabi":
            mahero10 = "Hanabi"
            await message.channel.send("Matthew's hero #10 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero10 add Irithel":
            mahero10 = "Irithel"
            await message.channel.send("Matthew's hero #10 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero10 add Karrie":
            mahero10 = "Karrie"
            await message.channel.send(
                "Matthew's hero #10 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero10 add Kimmy":
            mahero10 = "Kimmy"
            await message.channel.send("Matthew's hero #10 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero10 add Layla":
            mahero10 = "Layla"
            await message.channel.send("Matthew's hero #10 is now Layla! :haircut:  ")
        if message.content == "!ml hero10 add Miya":
            mahero10 = "Miya"
            await message.channel.send("Matthew's hero #10 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero10 add Moskov":
            mahero10 = "Moskov"
            await message.channel.send("Matthew's hero #10 is now Moskov! :imp: ")
        if message.content == "!ml hero10 add Yi Sun-Shin":
            mahero10 = "Yi Sun-Shin"
            await message.channel.send("Matthew's hero #10 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero10 add Angela":
            mahero10 = "Angela"
            await message.channel.send("Matthew's hero #10 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero10 add Diggie":
            mahero10 = "Diggie"
            await message.channel.send("Matthew's hero #10 is now Diggie! :owl: ")
        if message.content == "!ml hero10 add Estes":
            mahero10 = "Estes"
            await message.channel.send("Matthew's hero #10 is now Estes! :ear:  ")
        if message.content == "!ml hero10 add Rafaela":
            mahero10 = "Rafaela"
            await message.channel.send("Matthew's hero #10 is now Rafaela! :angel: ")
        if message.content == "!ml hero10 add Rynn":
            mahero10 = "Rynn"
            await message.channel.send("Matthew's hero #10 is now Rynn! ")
        if message.content == "!ml hero1 clear":
            mahero1 = "Not Chosen"
            await message.channel.send("Matthew's hero #1 slot has been cleared!")
        if message.content == "!ml hero2 clear":
            mahero2 = "Not Chosen"
            await message.channel.send("Matthew's hero #2 slot has been cleared!")
        if message.content == "!ml hero3 clear":
            mahero3 = "Not Chosen"
            await message.channel.send("Matthew's hero #3 slot has been cleared!")
        if message.content == "!ml hero3 clear":
            mahero3 = "Not Chosen"
            await message.channel.send("Matthew's hero #3 slot has been cleared!")
        if message.content == "!ml hero4 clear":
            mahero4 = "Not Chosen"
            await message.channel.send("Matthew's hero #4 slot has been cleared!")
        if message.content == "!ml hero5 clear":
            mahero5 = "Not Chosen"
            await message.channel.send("Matthew's hero #5 slot has been cleared!")
        if message.content == "!ml hero6 clear":
            mahero6 = "Not Chosen"
            await message.channel.send("Matthew's hero #6 slot has been cleared!")
        if message.content == "!ml hero7 clear":
            mahero7 = "Not Chosen"
            await message.channel.send("Matthew's hero #7 slot has been cleared!")
        if message.content == "!ml hero8 clear":
            mahero8 = "Not Chosen"
            await message.channel.send("Matthew's hero #8 slot has been cleared!")
        if message.content == "!ml hero9 clear":
            mahero9 = "Not Chosen"
            await message.channel.send("Matthew's hero #9 slot has been cleared!")
        if message.content == "!ml hero10 clear":
            mahero10 = "Not Chosen"
            await message.channel.send("Matthew's hero #10 slot has been cleared!")
        if message.content == "!ml hlist Matthew":
            maembed = discord.Embed(title="Heroes Matthew Plays",
                                    description="Here are the top 10 heroes Matthew is willing to play in ranked")
            maembed.add_field(name="1", value=mahero1)
            maembed.add_field(name="2", value=mahero2)
            maembed.add_field(name="3", value=mahero3)
            maembed.add_field(name="4", value=mahero4)
            maembed.add_field(name="5", value=mahero5)
            maembed.add_field(name="6", value=mahero6)
            maembed.add_field(name="7", value=mahero7)
            maembed.add_field(name="8", value=mahero8)
            maembed.add_field(name="9", value=mahero9)
            maembed.add_field(name="10", value=mahero10)
            await message.channel.send(content=None, embed=maembed)
    if str(message.channel) not in clean_channels and str(message.author) in Dillon_Hlist:
        if message.content.find("hello") != -1:
            await message.channel.send("Hey Dillon, how are you?")
        if message.content.find("!gay") != -1:
            await message.channel.send("Soulless people can't be gay! They don't mix.")
        if message.content.find("!nigga") != -1:
            await message.channel.send("The soulless need no pass, carry on")
        if message.content.find("nigga") != -1:
            global nwsoulesschance
            global nwsoulessbonus
            global nwsoulesstotal
            nwsoulesschance = random.randrange(0, 20, 1)
            nwsoulesstotal = nwsoulesschance + nwsoulessbonus
            if nwsoulesstotal > 15:
                await message.channel.send("No soul? No pass. Sorry, those are the rules")
                nwsoulesstotal = 0
                nwsoulesschance = 0
                nwsoulessbonus = 0
            else:
                nwsoulessbonus += 1
                nwsoulesstotal = 0
                nwsoulesschance = 0
            nwordcount
            nwordcount += 1
        if message.content.find("Nigga") != -1:
            nwsoulesschance = random.randrange(0, 20, 1)
            nwsoulesstotal = nwsoulesschance + nwsoulessbonus
            if nwsoulesstotal > 15:
                await message.channel.send("Just because you don't have a soul doesn't mean you're exempt from consequences")
                nwsoulesstotal = 0
                nwsoulesschance = 0
                nwsoulessbonus = 0
            else:
                nwsoulessbonus += 1
                nwsoulesstotal = 0
                nwsoulesschance = 0
            nwordcount
            nwordcount += 1
        if message.content.find("NIGGA") != -1:
            nwsoulesschance = random.randrange(0, 20, 1)
            nwsoulesstotal = nwsoulesschance + nwsoulessbonus
            if nwsoulesstotal > 15:
                await message.channel.send("Woah dude, chill out. You'll never get a soul with that potty mouth")
                nwsoulesstotal = 0
                nwsoulesschance = 0
                nwsoulessbonus = 0
            else:
                nwsoulessbonus += 2
                nwsoulesstotal = 0
                nwsoulesschance = 0
            nwordcount
            nwordcount += 2
        if message.content.find("nigger") != -1:
            nwsoulesschance = random.randrange(0, 20, 1)
            nwsoulesstotal = nwsoulesschance + nwsoulessbonus
            if nwsoulesstotal > 15:
                await message.channel.send("Hard R? I didn't expect you'd get this far")
                nwsoulesstotal = 0
                nwsoulesschance = 0
                nwsoulessbonus = 0
            else:
                nwsoulessbonus += 3
                nwsoulesstotal = 0
                nwsoulesschance = 0
            nwordcount
            nwordcount += 10
        if message.content.find("Nigger") != -1:
            nwsoulesschance = random.randrange(0, 20, 1)
            nwsoulesstotal = nwsoulesschance + nwsoulessbonus
            if nwsoulesstotal > 15:
                await message.channel.send("I see you mean business")
                nwsoulesstotal = 0
                nwsoulesschance = 0
                nwsoulessbonus = 0
            else:
                nwsoulessbonus += 3
                nwsoulesstotal = 0
                nwsoulesschance = 0
            nwordcount
            nwordcount += 10
        if message.content.find("NIGGER") != -1:
            nwsoulesschance = random.randrange(0, 20, 1)
            nwsoulesstotal = nwsoulesschance + nwsoulessbonus
            if nwsoulesstotal > 15:
                await message.channel.send("Wait, did dillon actually just say the N-Word hard R with all caps?")
                nwsoulesstotal = 0
                nwsoulesschance = 0
                nwsoulessbonus = 0
            else:
                nwsoulessbonus += 10
                nwsoulesstotal = 0
                nwsoulesschance = 0
            nwordcount
            nwordcount += 100
        if message.content == "!ml hero1 add Akai":
            global dihero1
            dihero1 = "Akai"
            await message.channel.send("Dillon's hero #1 is now Akai! :panda_face: ")
        if message.content == "!ml hero1 add Balmond":
            dihero1 = "Balmond"
            await message.channel.send("Dillon's hero #1 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero1 add Belerick":
            dihero1 = "Belerick"
            await message.channel.send("Dillon's hero #1 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero1 add Franco":
            dihero1 = "Franco"
            await message.channel.send("Dillon's hero #1 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero1 add Esmerelda":
            dihero1 = "Esmerelda"
            await message.channel.send("Dillon's hero #1 is now Esmerelda! :shield: ")
        if message.content == "!ml hero1 add Gatotkaca":
            dihero1 = "Gatotkaca"
            await message.channel.send("Dillon's hero #1 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero1 add Grock":
            dihero1 = "Grock"
            await message.channel.send("Dillon's hero #1 is now Grock! :european_castle: ")
        if message.content == "!ml hero1 add Hilda":
            dihero1 = "Hilda"
            await message.channel.send("Dillon's hero #1 is now Hilda! :runner: ")
        if message.content == "!ml hero1 add Hylos":
            dihero1 = "Hylos"
            await message.channel.send("Dillon's hero #1 is now Hylos! :unicorn: ")
        if message.content == "!ml hero1 add Johnson":
            dihero1 = "Johnson"
            await message.channel.send("Dillon's hero #1 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero1 add Khufra":
            dihero1 = "Khufra"
            await message.channel.send("Dillon's hero #1 is now Khufra! :clown: ")
        if message.content == "!ml hero1 add Lolita":
            dihero1 = "Lolita"
            await message.channel.send("Dillon's hero #1 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            dihero1 = "Masha"
            await message.channel.send("Dillon's hero #1 is now Masha! :bear: ")
        if message.content == "!ml hero1 add Minotaur":
            dihero1 = "Minotaur"
            await message.channel.send("Dillon's hero #1 is now Minotaur! :cow: ")
        if message.content == "!ml hero1 add Tigreal":
            dihero1 = "Tigreal"
            await message.channel.send("Dillon's hero #1 is now Tigreal! :moyai: ")
        if message.content == "!ml hero1 add Uranus":
            dihero1 = "Uranus"
            await message.channel.send("Dillon's hero #1 is now Uranus! :peach: ")
        if message.content == "!ml hero1 add X.Borg":
            dihero1 = "X.Borg"
            await message.channel.send("Dillon's hero #1 is now X.Borg! :fire: ")
        if message.content == "!ml hero1 add Aldous":
            dihero1 = "Aldous"
            await message.channel.send("Dillon's hero #1 is now Aldous! :fist: ")
        if message.content == "!ml hero1 add Alpha":
            dihero1 = "Alpha"
            await message.channel.send("Dillon's hero #1 is now Alpha! :airplane: ")
        if message.content == "!ml hero1 add Alucard":
            dihero1 = "Alucard"
            await message.channel.send("Dillon's hero #1 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero1 add Argus":
            dihero1 = "Argus"
            await message.channel.send("Dillon's hero #1 is now Argus! :angel: ")
        if message.content == "!ml hero1 add Badang":
            dihero1 = "Badang"
            await message.channel.send("Dillon's hero #1 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero1 add Bane":
            dihero1 = "Bane"
            await message.channel.send("Dillon's hero #1 is now Bane! :octopus: ")
        if message.content == "!ml hero1 add Chou":
            dihero1 = "Chou"
            await message.channel.send("Dillon's hero #1 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero1 add Dyrroth":
            dihero1 = "Dyrroth"
            await message.channel.send("Dillon's hero #1 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero1 add Freya":
            dihero1 = "Freya"
            await message.channel.send("Dillon's hero #1 is now Freya! :hammer: ")
        if message.content == "!ml hero1 add Guinevere":
            dihero1 = "Guinevere"
            await message.channel.send("Dillon's hero #1 is now Guinevere! :dress:  ")
        if message.content == "!ml hero1 add Jawhead":
            dihero1 = "Jawhead"
            await message.channel.send("Dillon's hero #1 is now Jawhead! :robot: ")
        if message.content == "!ml hero1 add Kaja":
            dihero1 = "Kaja"
            await message.channel.send("Dillon's hero #1 is now Kaja! :bird: ")
        if message.content == "!ml hero1 add Lapu-Lapu":
            dihero1 = "Lapu-Lapu"
            await message.channel.send("Dillon's hero #1 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero1 add Leomord":
            dihero1 = "Leomord"
            await message.channel.send("Dillon's hero #1 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero1 add Martis":
            dihero1 = "Martis"
            await message.channel.send("Dillon's hero #1 is now Martis! :crab: ")
        if message.content == "!ml hero1 add Minsitthar":
            dihero1 = "Minsitthar"
            await message.channel.send("Dillon's hero #1 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero1 add Roger":
            dihero1 = "Roger"
            await message.channel.send("Dillon's hero #1 is now Roger! :wolf: ")
        if message.content == "!ml hero1 add Ruby":
            dihero1 = "Ruby"
            await message.channel.send("Dillon's hero #1 is now Ruby! :heart: ")
        if message.content == "!ml hero1 add Sun":
            dihero1 = "Sun"
            await message.channel.send("Dillon's hero #1 is now Sun! :monkey_face: ")
        if message.content == "!ml hero1 add Thamuz":
            dihero1 = "Thamuz"
            await message.channel.send("Dillon's hero #1 is now Thamuz! :rage: ")
        if message.content == "!ml hero1 add Terizla":
            dihero1 = "Terizla"
            await message.channel.send("Dillon's hero #1 is now Terizla! :hammer: ")
        if message.content == "!ml hero1 add Zilong":
            dihero1 = "Zilong"
            await message.channel.send("Dillon's hero #1 is now Zilong! :dragon: ")
        if message.content == "!ml hero1 add Fanny":
            dihero1 = "Fanny"
            await message.channel.send("Dillon's hero #1 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero1 add Gusion":
            dihero1 = "Gusion"
            await message.channel.send(
                "Dillon's hero #1 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero1 add Hanzo":
            dihero1 = "Hanzo"
            await message.channel.send("Dillon's hero #1 is now Hanzo! :ghost: ")
        if message.content == "!ml hero1 add Hayabusa":
            dihero1 = "Hayabusa"
            await message.channel.send("Dillon's hero #1 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero1 add Helcurt":
            dihero1 = "Helcurt"
            await message.channel.send("Dillon's hero #1 is now Helcurt! :mute:  ")
        if message.content == "!ml hero1 add Karina":
            dihero1 = "Karina"
            await message.channel.send("Dillon's hero #1 is now Karina! :purple_heart: ")
        if message.content == "!ml hero1 add Lancelot":
            dihero1 = "Lancelot"
            await message.channel.send("Dillon's hero #1 is now Lancelot! :fencer: ")
        if message.content == "!ml hero1 add Lesley":
            dihero1 = "Lesley"
            await message.channel.send("Dillon's hero #1 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero1 add Natalia":
            dihero1 = "Natalia"
            await message.channel.send("Dillon's hero #1 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero1 add Saber":
            dihero1 = "Saber"
            await message.channel.send("Dillon's hero #1 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero1 add Selena":
            dihero1 = "Selena"
            await message.channel.send("Dillon's hero #1 is now Selena! :sleeping:  ")
        if message.content == "!ml hero1 add Alice":
            dihero1 = "Alice"
            await message.channel.send("Dillon's hero #1 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero1 add Aurora":
            dihero1 = "Aurora"
            await message.channel.send("Dillon's hero #1 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            dihero1 = "Chang'e"
            await message.channel.send("Dillon's hero #1 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero1 add Cyclops":
            dihero1 = "Cyclops"
            await message.channel.send("Dillon's hero #1 is now Cyclops! :eye:  ")
        if message.content == "!ml hero1 add Eudora":
            dihero1 = "Eudora"
            await message.channel.send("Dillon's hero #1 is now Eudora! :zap: ")
        if message.content == "!ml hero1 add Faramis":
            dihero1 = "Faramis"
            await message.channel.send("Dillon's hero #1 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero1 add Gord":
            dihero1 = "Gord"
            await message.channel.send("Dillon's hero #1 is now Gord! :snowboarder:")
        if message.content == "!ml hero1 add Harith":
            dihero1 = "Harith"
            await message.channel.send("Dillon's hero #1 is now Harith! :older_man: ")
        if message.content == "!ml hero1 add Harley":
            dihero1 = "Harley"
            await message.channel.send("Dillon's hero #1 is now Harley! :tophat: ")
        if message.content == "!ml hero1 add Kadita":
            dihero1 = "Kadita"
            await message.channel.send("Dillon's hero #1 is now Kadita! :droplet: ")
        if message.content == "!ml hero1 add Kagura":
            dihero1 = "Kagura"
            await message.channel.send("Dillon's hero #1 is now Kagura! :umbrella2:  ")
        if message.content == "!ml hero1 add Lunox":
            dihero1 = "Lunox"
            await message.channel.send("Dillon's hero #1 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero1 add Lylia":
            dihero1 = "Lylia"
            await message.channel.send("Dillon's hero #1 is now Lylia! :boom: ")
        if message.content == "!ml hero1 add Nana":
            dihero1 = "Nana"
            await message.channel.send("Dillon's hero #1 is now Nana! :cat:  ")
        if message.content == "!ml hero1 add Odette":
            dihero1 = "Odette"
            await message.channel.send("Dillon's hero #1 is now Odette! :duck: ")
        if message.content == "!ml hero1 add Pharsa":
            dihero1 = "Pharsa"
            await message.channel.send("Dillon's hero #1 is now Pharsa! :dove:  ")
        if message.content == "!ml hero1 add Vale":
            dihero1 = "Vale"
            await message.channel.send("Dillon's hero #1 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero1 add Valir":
            dihero1 = "Valir"
            await message.channel.send("Dillon's hero #1 is now Valir! :fire:")
        if message.content == "!ml hero1 add Vexanna":
            dihero1 = "Vexanna"
            await message.channel.send("Dillon's hero #1 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero1 add Bruno":
            dihero1 = "Bruno"
            await message.channel.send("Dillon's hero #1 is now Bruno! :soccer:  ")
        if message.content == "!ml hero1 add Claude":
            dihero1 = "Claude"
            await message.channel.send("Dillon's hero #1 is now Claude! :monkey:  ")
        if message.content == "!ml hero1 add Clint":
            dihero1 = "Clint"
            await message.channel.send("Dillon's hero #1 is now Clint! :cowboy: ")
        if message.content == "!ml hero1 add Granger":
            dihero1 = "Granger"
            await message.channel.send("Dillon's hero #1 is now Granger! :violin: ")
        if message.content == "!ml hero1 add Hanabi":
            dihero1 = "Hanabi"
            await message.channel.send("Dillon's hero #1 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero1 add Irithel":
            dihero1 = "Irithel"
            await message.channel.send("Dillon's hero #1 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero1 add Karrie":
            dihero1 = "Karrie"
            await message.channel.send(
                "Dillon's hero #1 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero1 add Kimmy":
            dihero1 = "Kimmy"
            await message.channel.send("Dillon's hero #1 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero1 add Layla":
            dihero1 = "Layla"
            await message.channel.send("Dillon's hero #1 is now Layla! :haircut:  ")
        if message.content == "!ml hero1 add Miya":
            dihero1 = "Miya"
            await message.channel.send("Dillon's hero #1 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero1 add Moskov":
            dihero1 = "Moskov"
            await message.channel.send("Dillon's hero #1 is now Moskov! :imp: ")
        if message.content == "!ml hero1 add Yi Sun-Shin":
            dihero1 = "Yi Sun-Shin"
            await message.channel.send("Dillon's hero #1 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero1 add Angela":
            dihero1 = "Angela"
            await message.channel.send("Dillon's hero #1 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero1 add Diggie":
            dihero1 = "Diggie"
            await message.channel.send("Dillon's hero #1 is now Diggie! :owl: ")
        if message.content == "!ml hero1 add Estes":
            dihero1 = "Estes"
            await message.channel.send("Dillon's hero #1 is now Estes! :ear:  ")
        if message.content == "!ml hero1 add Rafaela":
            dihero1 = "Rafaela"
            await message.channel.send("Dillon's hero #1 is now Rafaela! :angel: ")
        if message.content == "!ml hero1 add Rynn":
            dihero1 = "Rynn"
            await message.channel.send("Dillon's hero #1 is now Rynn! ")
        if message.content == "!ml hero2 add Akai":
            global dihero2
            dihero2 = "Akai"
            await message.channel.send("Dillon's hero #2 is now Akai! :panda_face: ")
        if message.content == "!ml hero2 add Balmond":
            dihero2 = "Balmond"
            await message.channel.send("Dillon's hero #2 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero2 add Belerick":
            dihero2 = "Belerick"
            await message.channel.send("Dillon's hero #2 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero2 add Franco":
            dihero2 = "Franco"
            await message.channel.send("Dillon's hero #2 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero2 add Esmerelda":
            dihero2 = "Esmerelda"
            await message.channel.send("Dillon's hero #2 is now Esmerelda! :shield: ")
        if message.content == "!ml hero2 add Gatotkaca":
            dihero2 = "Gatotkaca"
            await message.channel.send("Dillon's hero #2 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero2 add Grock":
            dihero2 = "Grock"
            await message.channel.send("Dillon's hero #2 is now Grock! :european_castle: ")
        if message.content == "!ml hero2 add Hilda":
            dihero2 = "Hilda"
            await message.channel.send("Dillon's hero #2 is now Hilda! :runner: ")
        if message.content == "!ml hero2 add Hylos":
            dihero2 = "Hylos"
            await message.channel.send("Dillon's hero #2 is now Hylos! :unicorn: ")
        if message.content == "!ml hero2 add Johnson":
            dihero2 = "Johnson"
            await message.channel.send("Dillon's hero #2 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero2 add Khufra":
            dihero2 = "Khufra"
            await message.channel.send("Dillon's hero #2 is now Khufra! :clown: ")
        if message.content == "!ml hero2 add Lolita":
            dihero2 = "Lolita"
            await message.channel.send("Dillon's hero #2 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            dihero2 = "Masha"
            await message.channel.send("Dillon's hero #2 is now Masha! :bear: ")
        if message.content == "!ml hero2 add Minotaur":
            dihero2 = "Minotaur"
            await message.channel.send("Dillon's hero #2 is now Minotaur! :cow: ")
        if message.content == "!ml hero2 add Tigreal":
            dihero2 = "Tigreal"
            await message.channel.send("Dillon's hero #2 is now Tigreal! :moyai: ")
        if message.content == "!ml hero2 add Uranus":
            dihero2 = "Uranus"
            await message.channel.send("Dillon's hero #2 is now Uranus! :peach: ")
        if message.content == "!ml hero2 add X.Borg":
            dihero2 = "X.Borg"
            await message.channel.send("Dillon's hero #2 is now X.Borg! :fire: ")
        if message.content == "!ml hero2 add Aldous":
            dihero2 = "Aldous"
            await message.channel.send("Dillon's hero #2 is now Aldous! :fist: ")
        if message.content == "!ml hero2 add Alpha":
            dihero2 = "Alpha"
            await message.channel.send("Dillon's hero #2 is now Alpha! :airplane: ")
        if message.content == "!ml hero2 add Alucard":
            dihero2 = "Alucard"
            await message.channel.send("Dillon's hero #2 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero2 add Argus":
            dihero2 = "Argus"
            await message.channel.send("Dillon's hero #2 is now Argus! :angel: ")
        if message.content == "!ml hero2 add Badang":
            dihero2 = "Badang"
            await message.channel.send("Dillon's hero #2 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero2 add Bane":
            dihero2 = "Bane"
            await message.channel.send("Dillon's hero #2 is now Bane! :octopus: ")
        if message.content == "!ml hero2 add Chou":
            dihero2 = "Chou"
            await message.channel.send("Dillon's hero #2 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero2 add Dyrroth":
            dihero2 = "Dyrroth"
            await message.channel.send("Dillon's hero #2 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero2 add Freya":
            dihero2 = "Freya"
            await message.channel.send("Dillon's hero #2 is now Freya! :hammer: ")
        if message.content == "!ml hero2 add Guinevere":
            dihero2 = "Guinevere"
            await message.channel.send("Dillon's hero #2 is now Guinevere! :dress:  ")
        if message.content == "!ml hero2 add Jawhead":
            dihero2 = "Jawhead"
            await message.channel.send("Dillon's hero #2 is now Jawhead! :robot: ")
        if message.content == "!ml hero2 add Kaja":
            dihero2 = "Kaja"
            await message.channel.send("Dillon's hero #2 is now Kaja! :bird: ")
        if message.content == "!ml hero2 add Lapu-Lapu":
            dihero2 = "Lapu-Lapu"
            await message.channel.send("Dillon's hero #2 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero2 add Leomord":
            dihero2 = "Leomord"
            await message.channel.send("Dillon's hero #2 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero2 add Martis":
            dihero2 = "Martis"
            await message.channel.send("Dillon's hero #2 is now Martis! :crab: ")
        if message.content == "!ml hero2 add Minsitthar":
            dihero2 = "Minsitthar"
            await message.channel.send("Dillon's hero #2 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero2 add Roger":
            dihero2 = "Roger"
            await message.channel.send("Dillon's hero #2 is now Roger! :wolf: ")
        if message.content == "!ml hero2 add Ruby":
            dihero2 = "Ruby"
            await message.channel.send("Dillon's hero #2 is now Ruby! :heart: ")
        if message.content == "!ml hero2 add Sun":
            dihero2 = "Sun"
            await message.channel.send("Dillon's hero #2 is now Sun! :monkey_face: ")
        if message.content == "!ml hero2 add Thamuz":
            dihero2 = "Thamuz"
            await message.channel.send("Dillon's hero #2 is now Thamuz! :rage: ")
        if message.content == "!ml hero2 add Terizla":
            dihero2 = "Terizla"
            await message.channel.send("Dillon's hero #2 is now Terizla! :hammer: ")
        if message.content == "!ml hero2 add Zilong":
            dihero2 = "Zilong"
            await message.channel.send("Dillon's hero #2 is now Zilong! :dragon: ")
        if message.content == "!ml hero2 add Fanny":
            dihero2 = "Fanny"
            await message.channel.send("Dillon's hero #2 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero2 add Gusion":
            dihero2 = "Gusion"
            await message.channel.send(
                "Dillon's hero #2 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero2 add Hanzo":
            dihero2 = "Hanzo"
            await message.channel.send("Dillon's hero #2 is now Hanzo! :ghost: ")
        if message.content == "!ml hero2 add Hayabusa":
            dihero2 = "Hayabusa"
            await message.channel.send("Dillon's hero #2 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero2 add Helcurt":
            dihero2 = "Helcurt"
            await message.channel.send("Dillon's hero #2 is now Helcurt! :mute:  ")
        if message.content == "!ml hero2 add Karina":
            dihero2 = "Karina"
            await message.channel.send("Dillon's hero #2 is now Karina! :purple_heart: ")
        if message.content == "!ml hero2 add Lancelot":
            dihero2 = "Lancelot"
            await message.channel.send("Dillon's hero #2 is now Lancelot! :fencer: ")
        if message.content == "!ml hero2 add Lesley":
            dihero2 = "Lesley"
            await message.channel.send("Dillon's hero #2 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero2 add Natalia":
            dihero2 = "Natalia"
            await message.channel.send("Dillon's hero #2 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero2 add Saber":
            dihero2 = "Saber"
            await message.channel.send("Dillon's hero #2 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero2 add Selena":
            dihero2 = "Selena"
            await message.channel.send("Dillon's hero #2 is now Selena! :sleeping:  ")
        if message.content == "!ml hero2 add Alice":
            dihero2 = "Alice"
            await message.channel.send("Dillon's hero #2 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero2 add Aurora":
            dihero2 = "Aurora"
            await message.channel.send("Dillon's hero #2 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            dihero2 = "Chang'e"
            await message.channel.send("Dillon's hero #2 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero2 add Cyclops":
            dihero2 = "Cyclops"
            await message.channel.send("Dillon's hero #2 is now Cyclops! :eye:  ")
        if message.content == "!ml hero2 add Eudora":
            dihero2 = "Eudora"
            await message.channel.send("Dillon's hero #2 is now Eudora! :zap: ")
        if message.content == "!ml hero2 add Faramis":
            dihero2 = "Faramis"
            await message.channel.send("Dillon's hero #2 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero2 add Gord":
            dihero2 = "Gord"
            await message.channel.send("Dillon's hero #2 is now Gord! :snowboarder:")
        if message.content == "!ml hero2 add Harith":
            dihero2 = "Harith"
            await message.channel.send("Dillon's hero #2 is now Harith! :older_man: ")
        if message.content == "!ml hero2 add Harley":
            dihero2 = "Harley"
            await message.channel.send("Dillon's hero #2 is now Harley! :tophat: ")
        if message.content == "!ml hero2 add Kadita":
            dihero2 = "Kadita"
            await message.channel.send("Dillon's hero #2 is now Kadita! :droplet: ")
        if message.content == "!ml hero2 add Kagura":
            dihero2 = "Kagura"
            await message.channel.send("Dillon's hero #2 is now Kagura! :umbrella2:  ")
        if message.content == "!ml hero2 add Lunox":
            dihero2 = "Lunox"
            await message.channel.send("Dillon's hero #2 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero2 add Lylia":
            dihero2 = "Lylia"
            await message.channel.send("Dillon's hero #2 is now Lylia! :boom: ")
        if message.content == "!ml hero2 add Nana":
            dihero2 = "Nana"
            await message.channel.send("Dillon's hero #2 is now Nana! :cat:  ")
        if message.content == "!ml hero2 add Odette":
            dihero2 = "Odette"
            await message.channel.send("Dillon's hero #2 is now Odette! :duck: ")
        if message.content == "!ml hero2 add Pharsa":
            dihero2 = "Pharsa"
            await message.channel.send("Dillon's hero #2 is now Pharsa! :dove:  ")
        if message.content == "!ml hero2 add Vale":
            dihero2 = "Vale"
            await message.channel.send("Dillon's hero #2 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero2 add Valir":
            dihero2 = "Valir"
            await message.channel.send("Dillon's hero #2 is now Valir! :fire:")
        if message.content == "!ml hero2 add Vexanna":
            dihero2 = "Vexanna"
            await message.channel.send("Dillon's hero #2 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero2 add Bruno":
            dihero2 = "Bruno"
            await message.channel.send("Dillon's hero #2 is now Bruno! :soccer:  ")
        if message.content == "!ml hero2 add Claude":
            dihero2 = "Claude"
            await message.channel.send("Dillon's hero #2 is now Claude! :monkey:  ")
        if message.content == "!ml hero2 add Clint":
            dihero2 = "Clint"
            await message.channel.send("Dillon's hero #2 is now Clint! :cowboy: ")
        if message.content == "!ml hero2 add Granger":
            dihero2 = "Granger"
            await message.channel.send("Dillon's hero #2 is now Granger! :violin: ")
        if message.content == "!ml hero2 add Hanabi":
            dihero2 = "Hanabi"
            await message.channel.send("Dillon's hero #2 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero2 add Irithel":
            dihero2 = "Irithel"
            await message.channel.send("Dillon's hero #2 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero2 add Karrie":
            dihero2 = "Karrie"
            await message.channel.send(
                "Dillon's hero #2 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero2 add Kimmy":
            dihero2 = "Kimmy"
            await message.channel.send("Dillon's hero #2 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero2 add Layla":
            dihero2 = "Layla"
            await message.channel.send("Dillon's hero #2 is now Layla! :haircut:  ")
        if message.content == "!ml hero2 add Miya":
            dihero2 = "Miya"
            await message.channel.send("Dillon's hero #2 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero2 add Moskov":
            dihero2 = "Moskov"
            await message.channel.send("Dillon's hero #2 is now Moskov! :imp: ")
        if message.content == "!ml hero2 add Yi Sun-Shin":
            dihero2 = "Yi Sun-Shin"
            await message.channel.send("Dillon's hero #2 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero2 add Angela":
            dihero2 = "Angela"
            await message.channel.send("Dillon's hero #2 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero2 add Diggie":
            dihero2 = "Diggie"
            await message.channel.send("Dillon's hero #2 is now Diggie! :owl: ")
        if message.content == "!ml hero2 add Estes":
            dihero2 = "Estes"
            await message.channel.send("Dillon's hero #2 is now Estes! :ear:  ")
        if message.content == "!ml hero2 add Rafaela":
            dihero2 = "Rafaela"
            await message.channel.send("Dillon's hero #2 is now Rafaela! :angel: ")
        if message.content == "!ml hero2 add Rynn":
            dihero2 = "Rynn"
            await message.channel.send("Dillon's hero #2 is now Rynn! ")
        if message.content == "!ml hero3 add Akai":
            global dihero3
            dihero3 = "Akai"
            await message.channel.send("Dillon's hero #3 is now Akai! :panda_face: ")
        if message.content == "!ml hero3 add Balmond":
            dihero3 = "Balmond"
            await message.channel.send("Dillon's hero #3 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero3 add Belerick":
            dihero3 = "Belerick"
            await message.channel.send("Dillon's hero #3 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero3 add Franco":
            dihero3 = "Franco"
            await message.channel.send("Dillon's hero #3 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero3 add Esmerelda":
            dihero3 = "Esmerelda"
            await message.channel.send("Dillon's hero #3 is now Esmerelda! :shield: ")
        if message.content == "!ml hero3 add Gatotkaca":
            dihero3 = "Gatotkaca"
            await message.channel.send("Dillon's hero #3 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero3 add Grock":
            dihero3 = "Grock"
            await message.channel.send("Dillon's hero #3 is now Grock! :european_castle: ")
        if message.content == "!ml hero3 add Hilda":
            dihero3 = "Hilda"
            await message.channel.send("Dillon's hero #3 is now Hilda! :runner: ")
        if message.content == "!ml hero3 add Hylos":
            dihero3 = "Hylos"
            await message.channel.send("Dillon's hero #3 is now Hylos! :unicorn: ")
        if message.content == "!ml hero3 add Johnson":
            dihero3 = "Johnson"
            await message.channel.send("Dillon's hero #3 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero3 add Khufra":
            dihero3 = "Khufra"
            await message.channel.send("Dillon's hero #3 is now Khufra! :clown: ")
        if message.content == "!ml hero3 add Lolita":
            dihero3 = "Lolita"
            await message.channel.send("Dillon's hero #3 is now Lolita! :lollipop: ")
        if message.content == "!ml hero3 add Masha":
            dihero3 = "Masha"
            await message.channel.send("Dillon's hero #3 is now Masha! :bear: ")
        if message.content == "!ml hero3 add Minotaur":
            dihero3 = "Minotaur"
            await message.channel.send("Dillon's hero #3 is now Minotaur! :cow: ")
        if message.content == "!ml hero3 add Tigreal":
            dihero3 = "Tigreal"
            await message.channel.send("Dillon's hero #3 is now Tigreal! :moyai: ")
        if message.content == "!ml hero3 add Uranus":
            dihero3 = "Uranus"
            await message.channel.send("Dillon's hero #3 is now Uranus! :peach: ")
        if message.content == "!ml hero3 add X.Borg":
            dihero3 = "X.Borg"
            await message.channel.send("Dillon's hero #3 is now X.Borg! :fire: ")
        if message.content == "!ml hero3 add Aldous":
            dihero3 = "Aldous"
            await message.channel.send("Dillon's hero #3 is now Aldous! :fist: ")
        if message.content == "!ml hero3 add Alpha":
            dihero3 = "Alpha"
            await message.channel.send("Dillon's hero #3 is now Alpha! :airplane: ")
        if message.content == "!ml hero3 add Alucard":
            dihero3 = "Alucard"
            await message.channel.send("Dillon's hero #3 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero3 add Argus":
            dihero3 = "Argus"
            await message.channel.send("Dillon's hero #3 is now Argus! :angel: ")
        if message.content == "!ml hero3 add Badang":
            dihero3 = "Badang"
            await message.channel.send("Dillon's hero #3 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero3 add Bane":
            dihero3 = "Bane"
            await message.channel.send("Dillon's hero #3 is now Bane! :octopus: ")
        if message.content == "!ml hero3 add Chou":
            dihero3 = "Chou"
            await message.channel.send("Dillon's hero #3 is now Chou! :martial_arts_uniform: ")
        if message.content == "!ml hero3 add Dyrroth":
            dihero3 = "Dyrroth"
            await message.channel.send("Dillon's hero #3 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero3 add Freya":
            dihero3 = "Freya"
            await message.channel.send("Dillon's hero #3 is now Freya! :hammer: ")
        if message.content == "!ml hero3 add Guinevere":
            dihero3 = "Guinevere"
            await message.channel.send("Dillon's hero #3 is now Guinevere! :dress:  ")
        if message.content == "!ml hero3 add Jawhead":
            dihero3 = "Jawhead"
            await message.channel.send("Dillon's hero #3 is now Jawhead! :robot: ")
        if message.content == "!ml hero3 add Kaja":
            dihero3 = "Kaja"
            await message.channel.send("Dillon's hero #3 is now Kaja! :bird: ")
        if message.content == "!ml hero3 add Lapu-Lapu":
            dihero3 = "Lapu-Lapu"
            await message.channel.send("Dillon's hero #3 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero3 add Leomord":
            dihero3 = "Leomord"
            await message.channel.send("Dillon's hero #3 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero3 add Martis":
            dihero3 = "Martis"
            await message.channel.send("Dillon's hero #3 is now Martis! :crab: ")
        if message.content == "!ml hero3 add Minsitthar":
            dihero3 = "Minsitthar"
            await message.channel.send("Dillon's hero #3 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero3 add Roger":
            dihero3 = "Roger"
            await message.channel.send("Dillon's hero #3 is now Roger! :wolf: ")
        if message.content == "!ml hero3 add Ruby":
            dihero3 = "Ruby"
            await message.channel.send("Dillon's hero #3 is now Ruby! :heart: ")
        if message.content == "!ml hero3 add Sun":
            dihero3 = "Sun"
            await message.channel.send("Dillon's hero #3 is now Sun! :monkey_face: ")
        if message.content == "!ml hero3 add Thamuz":
            dihero3 = "Thamuz"
            await message.channel.send("Dillon's hero #3 is now Thamuz! :rage: ")
        if message.content == "!ml hero3 add Terizla":
            dihero3 = "Terizla"
            await message.channel.send("Dillon's hero #3 is now Terizla! :hammer: ")
        if message.content == "!ml hero3 add Zilong":
            dihero3 = "Zilong"
            await message.channel.send("Dillon's hero #3 is now Zilong! :dragon: ")
        if message.content == "!ml hero3 add Fanny":
            dihero3 = "Fanny"
            await message.channel.send("Dillon's hero #3 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero3 add Gusion":
            dihero3 = "Gusion"
            await message.channel.send(
                "Dillon's hero #3 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero3 add Hanzo":
            dihero3 = "Hanzo"
            await message.channel.send("Dillon's hero #3 is now Hanzo! :ghost: ")
        if message.content == "!ml hero3 add Hayabusa":
            dihero3 = "Hayabusa"
            await message.channel.send("Dillon's hero #3 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero3 add Helcurt":
            dihero3 = "Helcurt"
            await message.channel.send("Dillon's hero #3 is now Helcurt! :mute:  ")
        if message.content == "!ml hero3 add Karina":
            dihero3 = "Karina"
            await message.channel.send("Dillon's hero #3 is now Karina! :purple_heart: ")
        if message.content == "!ml hero3 add Lancelot":
            dihero3 = "Lancelot"
            await message.channel.send("Dillon's hero #3 is now Lancelot! :fencer: ")
        if message.content == "!ml hero3 add Lesley":
            dihero3 = "Lesley"
            await message.channel.send("Dillon's hero #3 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero3 add Natalia":
            dihero3 = "Natalia"
            await message.channel.send("Dillon's hero #3 is now Natalia! :spy::exclamation: ")
        if message.content == "!ml hero3 add Saber":
            dihero3 = "Saber"
            await message.channel.send("Dillon's hero #3 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero3 add Selena":
            dihero3 = "Selena"
            await message.channel.send("Dillon's hero #3 is now Selena! :sleeping:  ")
        if message.content == "!ml hero3 add Alice":
            dihero3 = "Alice"
            await message.channel.send("Dillon's hero #3 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero3 add Aurora":
            dihero3 = "Aurora"
            await message.channel.send("Dillon's hero #3 is now Aurora! :snow: ")
        if message.content == "!ml hero3 add Chang'e":
            dihero3 = "Chang'e"
            await message.channel.send("Dillon's hero #3 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero3 add Cyclops":
            dihero3 = "Cyclops"
            await message.channel.send("Dillon's hero #3 is now Cyclops! :eye:  ")
        if message.content == "!ml hero3 add Eudora":
            dihero3 = "Eudora"
            await message.channel.send("Dillon's hero #3 is now Eudora! :zap: ")
        if message.content == "!ml hero3 add Faramis":
            dihero3 = "Faramis"
            await message.channel.send("Dillon's hero #3 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero3 add Gord":
            dihero3 = "Gord"
            await message.channel.send("Dillon's hero #3 is now Gord! :snowboarder:")
        if message.content == "!ml hero3 add Harith":
            dihero3 = "Harith"
            await message.channel.send("Dillon's hero #3 is now Harith! :older_man: ")
        if message.content == "!ml hero3 add Harley":
            dihero3 = "Harley"
            await message.channel.send("Dillon's hero #3 is now Harley! :tophat: ")
        if message.content == "!ml hero3 add Kadita":
            dihero3 = "Kadita"
            await message.channel.send("Dillon's hero #3 is now Kadita! :droplet: ")
        if message.content == "!ml hero3 add Kagura":
            dihero3 = "Kagura"
            await message.channel.send("Dillon's hero #3 is now Kagura! :umbrella2:  ")
        if message.content == "!ml hero3 add Lunox":
            dihero3 = "Lunox"
            await message.channel.send("Dillon's hero #3 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero3 add Lylia":
            dihero3 = "Lylia"
            await message.channel.send("Dillon's hero #3 is now Lylia! :boom: ")
        if message.content == "!ml hero3 add Nana":
            dihero3 = "Nana"
            await message.channel.send("Dillon's hero #3 is now Nana! :cat:  ")
        if message.content == "!ml hero3 add Odette":
            dihero3 = "Odette"
            await message.channel.send("Dillon's hero #3 is now Odette! :duck: ")
        if message.content == "!ml hero3 add Pharsa":
            dihero3 = "Pharsa"
            await message.channel.send("Dillon's hero #3 is now Pharsa! :dove:  ")
        if message.content == "!ml hero3 add Vale":
            dihero3 = "Vale"
            await message.channel.send("Dillon's hero #3 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero3 add Valir":
            dihero3 = "Valir"
            await message.channel.send("Dillon's hero #3 is now Valir! :fire:")
        if message.content == "!ml hero3 add Vexanna":
            dihero3 = "Vexanna"
            await message.channel.send("Dillon's hero #3 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero3 add Bruno":
            dihero3 = "Bruno"
            await message.channel.send("Dillon's hero #3 is now Bruno! :soccer:  ")
        if message.content == "!ml hero3 add Claude":
            dihero3 = "Claude"
            await message.channel.send("Dillon's hero #3 is now Claude! :monkey:  ")
        if message.content == "!ml hero3 add Clint":
            dihero3 = "Clint"
            await message.channel.send("Dillon's hero #3 is now Clint! :cowboy: ")
        if message.content == "!ml hero3 add Granger":
            dihero3 = "Granger"
            await message.channel.send("Dillon's hero #3 is now Granger! :violin: ")
        if message.content == "!ml hero3 add Hanabi":
            dihero3 = "Hanabi"
            await message.channel.send("Dillon's hero #3 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero3 add Irithel":
            dihero3 = "Irithel"
            await message.channel.send("Dillon's hero #3 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero3 add Karrie":
            dihero3 = "Karrie"
            await message.channel.send(
                "Dillon's hero #3 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero3 add Kimmy":
            dihero3 = "Kimmy"
            await message.channel.send("Dillon's hero #3 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero3 add Layla":
            dihero3 = "Layla"
            await message.channel.send("Dillon's hero #3 is now Layla! :haircut:  ")
        if message.content == "!ml hero3 add Miya":
            dihero3 = "Miya"
            await message.channel.send("Dillon's hero #3 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero3 add Moskov":
            dihero3 = "Moskov"
            await message.channel.send("Dillon's hero #3 is now Moskov! :imp: ")
        if message.content == "!ml hero3 add Yi Sun-Shin":
            dihero3 = "Yi Sun-Shin"
            await message.channel.send("Dillon's hero #3 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero3 add Angela":
            dihero3 = "Angela"
            await message.channel.send("Dillon's hero #3 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero3 add Diggie":
            dihero3 = "Diggie"
            await message.channel.send("Dillon's hero #3 is now Diggie! :owl: ")
        if message.content == "!ml hero3 add Estes":
            dihero3 = "Estes"
            await message.channel.send("Dillon's hero #3 is now Estes! :ear:  ")
        if message.content == "!ml hero3 add Rafaela":
            dihero3 = "Rafaela"
            await message.channel.send("Dillon's hero #3 is now Rafaela! :angel: ")
        if message.content == "!ml hero3 add Rynn":
            dihero3 = "Rynn"
            await message.channel.send("Dillon's hero #3 is now Rynn! ")

        if message.content == "!ml hero4 add Akai":
            global dihero4
            dihero4 = "Akai"
            await message.channel.send("Dillon's hero #4 is now Akai! :panda_face: ")
        if message.content == "!ml hero4 add Balmond":
            dihero4 = "Balmond"
            await message.channel.send("Dillon's hero #4 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero4 add Belerick":
            dihero4 = "Belerick"
            await message.channel.send("Dillon's hero #4 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero4 add Franco":
            dihero4 = "Franco"
            await message.channel.send("Dillon's hero #4 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero4 add Esmerelda":
            dihero4 = "Esmerelda"
            await message.channel.send("Dillon's hero #4 is now Esmerelda! :shield: ")
        if message.content == "!ml hero4 add Gatotkaca":
            dihero4 = "Gatotkaca"
            await message.channel.send("Dillon's hero #4 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero4 add Grock":
            dihero4 = "Grock"
            await message.channel.send("Dillon's hero #4 is now Grock! :european_castle: ")
        if message.content == "!ml hero4 add Hilda":
            dihero4 = "Hilda"
            await message.channel.send("Dillon's hero #4 is now Hilda! :runner: ")
        if message.content == "!ml hero4 add Hylos":
            dihero4 = "Hylos"
            await message.channel.send("Dillon's hero #4 is now Hylos! :unicorn: ")
        if message.content == "!ml hero4 add Johnson":
            dihero4 = "Johnson"
            await message.channel.send("Dillon's hero #4 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero4 add Khufra":
            dihero4 = "Khufra"
            await message.channel.send("Dillon's hero #4 is now Khufra! :clown: ")
        if message.content == "!ml hero4 add Lolita":
            dihero4 = "Lolita"
            await message.channel.send("Dillon's hero #4 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            dihero4 = "Masha"
            await message.channel.send("Dillon's hero #4 is now Masha! :bear: ")
        if message.content == "!ml hero4 add Minotaur":
            dihero4 = "Minotaur"
            await message.channel.send("Dillon's hero #4 is now Minotaur! :cow: ")
        if message.content == "!ml hero4 add Tigreal":
            dihero4 = "Tigreal"
            await message.channel.send("Dillon's hero #4 is now Tigreal! :moyai: ")
        if message.content == "!ml hero4 add Uranus":
            dihero4 = "Uranus"
            await message.channel.send("Dillon's hero #4 is now Uranus! :peach: ")
        if message.content == "!ml hero4 add X.Borg":
            dihero4 = "X.Borg"
            await message.channel.send("Dillon's hero #4 is now X.Borg! :fire: ")
        if message.content == "!ml hero4 add Aldous":
            dihero4 = "Aldous"
            await message.channel.send("Dillon's hero #4 is now Aldous! :fist: ")
        if message.content == "!ml hero4 add Alpha":
            dihero4 = "Alpha"
            await message.channel.send("Dillon's hero #4 is now Alpha! :airplane: ")
        if message.content == "!ml hero4 add Alucard":
            dihero4 = "Alucard"
            await message.channel.send("Dillon's hero #4 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero4 add Argus":
            dihero4 = "Argus"
            await message.channel.send("Dillon's hero #4 is now Argus! :angel: ")
        if message.content == "!ml hero4 add Badang":
            dihero4 = "Badang"
            await message.channel.send("Dillon's hero #4 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero4 add Bane":
            dihero4 = "Bane"
            await message.channel.send("Dillon's hero #4 is now Bane! :octopus: ")
        if message.content == "!ml hero4 add Chou":
            dihero4 = "Chou"
            await message.channel.send("Dillon's hero #4 is now Chou! :dirtial_arts_uniform: ")
        if message.content == "!ml hero4 add Dyrroth":
            dihero4 = "Dyrroth"
            await message.channel.send("Dillon's hero #4 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero4 add Freya":
            dihero4 = "Freya"
            await message.channel.send("Dillon's hero #4 is now Freya! :hammer: ")
        if message.content == "!ml hero4 add Guinevere":
            dihero4 = "Guinevere"
            await message.channel.send("Dillon's hero #4 is now Guinevere! :dress:  ")
        if message.content == "!ml hero4 add Jawhead":
            dihero4 = "Jawhead"
            await message.channel.send("Dillon's hero #4 is now Jawhead! :robot: ")
        if message.content == "!ml hero4 add Kaja":
            dihero4 = "Kaja"
            await message.channel.send("Dillon's hero #4 is now Kaja! :bird: ")
        if message.content == "!ml hero4 add Lapu-Lapu":
            dihero4 = "Lapu-Lapu"
            await message.channel.send("Dillon's hero #4 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero4 add Leomord":
            dihero4 = "Leomord"
            await message.channel.send("Dillon's hero #4 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero4 add Martis":
            dihero4 = "Martis"
            await message.channel.send("Dillon's hero #4 is now Martis! :crab: ")
        if message.content == "!ml hero4 add Minsitthar":
            dihero4 = "Minsitthar"
            await message.channel.send("Dillon's hero #4 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero4 add Roger":
            dihero4 = "Roger"
            await message.channel.send("Dillon's hero #4 is now Roger! :wolf: ")
        if message.content == "!ml hero4 add Ruby":
            dihero4 = "Ruby"
            await message.channel.send("Dillon's hero #4 is now Ruby! :heart: ")
        if message.content == "!ml hero4 add Sun":
            dihero4 = "Sun"
            await message.channel.send("Dillon's hero #4 is now Sun! :monkey_face: ")
        if message.content == "!ml hero4 add Thamuz":
            dihero4 = "Thamuz"
            await message.channel.send("Dillon's hero #4 is now Thamuz! :rage: ")
        if message.content == "!ml hero4 add Terizla":
            dihero4 = "Terizla"
            await message.channel.send("Dillon's hero #4 is now Terizla! :hammer: ")
        if message.content == "!ml hero4 add Zilong":
            dihero4 = "Zilong"
            await message.channel.send("Dillon's hero #4 is now Zilong! :dragon: ")
        if message.content == "!ml hero4 add Fanny":
            dihero4 = "Fanny"
            await message.channel.send("Dillon's hero #4 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero4 add Gusion":
            dihero4 = "Gusion"
            await message.channel.send(
                "Dillon's hero #4 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero4 add Hanzo":
            dihero4 = "Hanzo"
            await message.channel.send("Dillon's hero #4 is now Hanzo! :ghost: ")
        if message.content == "!ml hero4 add Hayabusa":
            dihero4 = "Hayabusa"
            await message.channel.send("Dillon's hero #4 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero4 add Helcurt":
            dihero4 = "Helcurt"
            await message.channel.send("Dillon's hero #4 is now Helcurt! :mute:  ")
        if message.content == "!ml hero4 add Karina":
            dihero4 = "Karina"
            await message.channel.send("Dillon's hero #4 is now Karina! :purple_heart: ")
        if message.content == "!ml hero4 add Lancelot":
            dihero4 = "Lancelot"
            await message.channel.send("Dillon's hero #4 is now Lancelot! :fencer: ")
        if message.content == "!ml hero4 add Lesley":
            dihero4 = "Lesley"
            await message.channel.send("Dillon's hero #4 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero4 add Natalia":
            dihero4 = "Natalia"
            await message.channel.send("Dillon's hero #4 is now Natalia! :spy::excladition: ")
        if message.content == "!ml hero4 add Saber":
            dihero4 = "Saber"
            await message.channel.send("Dillon's hero #4 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero4 add Selena":
            dihero4 = "Selena"
            await message.channel.send("Dillon's hero #4 is now Selena! :sleeping:  ")
        if message.content == "!ml hero4 add Alice":
            dihero4 = "Alice"
            await message.channel.send("Dillon's hero #4 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero4 add Aurora":
            dihero4 = "Aurora"
            await message.channel.send("Dillon's hero #4 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            dihero4 = "Chang'e"
            await message.channel.send("Dillon's hero #4 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero4 add Cyclops":
            dihero4 = "Cyclops"
            await message.channel.send("Dillon's hero #4 is now Cyclops! :eye:  ")
        if message.content == "!ml hero4 add Eudora":
            dihero4 = "Eudora"
            await message.channel.send("Dillon's hero #4 is now Eudora! :zap: ")
        if message.content == "!ml hero4 add Faramis":
            dihero4 = "Faramis"
            await message.channel.send("Dillon's hero #4 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero4 add Gord":
            dihero4 = "Gord"
            await message.channel.send("Dillon's hero #4 is now Gord! :snowboarder:")
        if message.content == "!ml hero4 add Harith":
            dihero4 = "Harith"
            await message.channel.send("Dillon's hero #4 is now Harith! :older_din: ")
        if message.content == "!ml hero4 add Harley":
            dihero4 = "Harley"
            await message.channel.send("Dillon's hero #4 is now Harley! :tophat: ")
        if message.content == "!ml hero4 add Kadita":
            dihero4 = "Kadita"
            await message.channel.send("Dillon's hero #4 is now Kadita! :droplet: ")
        if message.content == "!ml hero4 add Kagura":
            dihero4 = "Kagura"
            await message.channel.send("Dillon's hero #4 is now Kagura! :umbrella4:  ")
        if message.content == "!ml hero4 add Lunox":
            dihero4 = "Lunox"
            await message.channel.send("Dillon's hero #4 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero4 add Lylia":
            dihero4 = "Lylia"
            await message.channel.send("Dillon's hero #4 is now Lylia! :boom: ")
        if message.content == "!ml hero4 add Nana":
            dihero4 = "Nana"
            await message.channel.send("Dillon's hero #4 is now Nana! :cat:  ")
        if message.content == "!ml hero4 add Odette":
            dihero4 = "Odette"
            await message.channel.send("Dillon's hero #4 is now Odette! :duck: ")
        if message.content == "!ml hero4 add Pharsa":
            dihero4 = "Pharsa"
            await message.channel.send("Dillon's hero #4 is now Pharsa! :dove:  ")
        if message.content == "!ml hero4 add Vale":
            dihero4 = "Vale"
            await message.channel.send("Dillon's hero #4 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero4 add Valir":
            dihero4 = "Valir"
            await message.channel.send("Dillon's hero #4 is now Valir! :fire:")
        if message.content == "!ml hero4 add Vexanna":
            dihero4 = "Vexanna"
            await message.channel.send("Dillon's hero #4 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero4 add Bruno":
            dihero4 = "Bruno"
            await message.channel.send("Dillon's hero #4 is now Bruno! :soccer:  ")
        if message.content == "!ml hero4 add Claude":
            dihero4 = "Claude"
            await message.channel.send("Dillon's hero #4 is now Claude! :monkey:  ")
        if message.content == "!ml hero4 add Clint":
            dihero4 = "Clint"
            await message.channel.send("Dillon's hero #4 is now Clint! :cowboy: ")
        if message.content == "!ml hero4 add Granger":
            dihero4 = "Granger"
            await message.channel.send("Dillon's hero #4 is now Granger! :violin: ")
        if message.content == "!ml hero4 add Hanabi":
            dihero4 = "Hanabi"
            await message.channel.send("Dillon's hero #4 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero4 add Irithel":
            dihero4 = "Irithel"
            await message.channel.send("Dillon's hero #4 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero4 add Karrie":
            dihero4 = "Karrie"
            await message.channel.send(
                "Dillon's hero #4 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero4 add Kimmy":
            dihero4 = "Kimmy"
            await message.channel.send("Dillon's hero #4 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero4 add Layla":
            dihero4 = "Layla"
            await message.channel.send("Dillon's hero #4 is now Layla! :haircut:  ")
        if message.content == "!ml hero4 add Miya":
            dihero4 = "Miya"
            await message.channel.send("Dillon's hero #4 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero4 add Moskov":
            dihero4 = "Moskov"
            await message.channel.send("Dillon's hero #4 is now Moskov! :imp: ")
        if message.content == "!ml hero4 add Yi Sun-Shin":
            dihero4 = "Yi Sun-Shin"
            await message.channel.send("Dillon's hero #4 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero4 add Angela":
            dihero4 = "Angela"
            await message.channel.send("Dillon's hero #4 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero4 add Diggie":
            dihero4 = "Diggie"
            await message.channel.send("Dillon's hero #4 is now Diggie! :owl: ")
        if message.content == "!ml hero4 add Estes":
            dihero4 = "Estes"
            await message.channel.send("Dillon's hero #4 is now Estes! :ear:  ")
        if message.content == "!ml hero4 add Rafaela":
            dihero4 = "Rafaela"
            await message.channel.send("Dillon's hero #4 is now Rafaela! :angel: ")
        if message.content == "!ml hero4 add Rynn":
            dihero4 = "Rynn"
            await message.channel.send("Dillon's hero #4 is now Rynn! ")
        if message.content == "!ml hero5 add Akai":
            global dihero5
            dihero5 = "Akai"
            await message.channel.send("Dillon's hero #5 is now Akai! :panda_face: ")
        if message.content == "!ml hero5 add Balmond":
            dihero5 = "Balmond"
            await message.channel.send("Dillon's hero #5 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero5 add Belerick":
            dihero5 = "Belerick"
            await message.channel.send("Dillon's hero #5 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero5 add Franco":
            dihero5 = "Franco"
            await message.channel.send("Dillon's hero #5 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero5 add Esmerelda":
            dihero5 = "Esmerelda"
            await message.channel.send("Dillon's hero #5 is now Esmerelda! :shield: ")
        if message.content == "!ml hero5 add Gatotkaca":
            dihero5 = "Gatotkaca"
            await message.channel.send("Dillon's hero #5 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero5 add Grock":
            dihero5 = "Grock"
            await message.channel.send("Dillon's hero #5 is now Grock! :european_castle: ")
        if message.content == "!ml hero5 add Hilda":
            dihero5 = "Hilda"
            await message.channel.send("Dillon's hero #5 is now Hilda! :runner: ")
        if message.content == "!ml hero5 add Hylos":
            dihero5 = "Hylos"
            await message.channel.send("Dillon's hero #5 is now Hylos! :unicorn: ")
        if message.content == "!ml hero5 add Johnson":
            dihero5 = "Johnson"
            await message.channel.send("Dillon's hero #5 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero5 add Khufra":
            dihero5 = "Khufra"
            await message.channel.send("Dillon's hero #5 is now Khufra! :clown: ")
        if message.content == "!ml hero5 add Lolita":
            dihero5 = "Lolita"
            await message.channel.send("Dillon's hero #5 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            dihero5 = "Masha"
            await message.channel.send("Dillon's hero #5 is now Masha! :bear: ")
        if message.content == "!ml hero5 add Minotaur":
            dihero5 = "Minotaur"
            await message.channel.send("Dillon's hero #5 is now Minotaur! :cow: ")
        if message.content == "!ml hero5 add Tigreal":
            dihero5 = "Tigreal"
            await message.channel.send("Dillon's hero #5 is now Tigreal! :moyai: ")
        if message.content == "!ml hero5 add Uranus":
            dihero5 = "Uranus"
            await message.channel.send("Dillon's hero #5 is now Uranus! :peach: ")
        if message.content == "!ml hero5 add X.Borg":
            dihero5 = "X.Borg"
            await message.channel.send("Dillon's hero #5 is now X.Borg! :fire: ")
        if message.content == "!ml hero5 add Aldous":
            dihero5 = "Aldous"
            await message.channel.send("Dillon's hero #5 is now Aldous! :fist: ")
        if message.content == "!ml hero5 add Alpha":
            dihero5 = "Alpha"
            await message.channel.send("Dillon's hero #5 is now Alpha! :airplane: ")
        if message.content == "!ml hero5 add Alucard":
            dihero5 = "Alucard"
            await message.channel.send("Dillon's hero #5 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero5 add Argus":
            dihero5 = "Argus"
            await message.channel.send("Dillon's hero #5 is now Argus! :angel: ")
        if message.content == "!ml hero5 add Badang":
            dihero5 = "Badang"
            await message.channel.send("Dillon's hero #5 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero5 add Bane":
            dihero5 = "Bane"
            await message.channel.send("Dillon's hero #5 is now Bane! :octopus: ")
        if message.content == "!ml hero5 add Chou":
            dihero5 = "Chou"
            await message.channel.send("Dillon's hero #5 is now Chou! :dirtial_arts_uniform: ")
        if message.content == "!ml hero5 add Dyrroth":
            dihero5 = "Dyrroth"
            await message.channel.send("Dillon's hero #5 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero5 add Freya":
            dihero5 = "Freya"
            await message.channel.send("Dillon's hero #5 is now Freya! :hammer: ")
        if message.content == "!ml hero5 add Guinevere":
            dihero5 = "Guinevere"
            await message.channel.send("Dillon's hero #5 is now Guinevere! :dress:  ")
        if message.content == "!ml hero5 add Jawhead":
            dihero5 = "Jawhead"
            await message.channel.send("Dillon's hero #5 is now Jawhead! :robot: ")
        if message.content == "!ml hero5 add Kaja":
            dihero5 = "Kaja"
            await message.channel.send("Dillon's hero #5 is now Kaja! :bird: ")
        if message.content == "!ml hero5 add Lapu-Lapu":
            dihero5 = "Lapu-Lapu"
            await message.channel.send("Dillon's hero #5 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero5 add Leomord":
            dihero5 = "Leomord"
            await message.channel.send("Dillon's hero #5 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero5 add Martis":
            dihero5 = "Martis"
            await message.channel.send("Dillon's hero #5 is now Martis! :crab: ")
        if message.content == "!ml hero5 add Minsitthar":
            dihero5 = "Minsitthar"
            await message.channel.send("Dillon's hero #5 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero5 add Roger":
            dihero5 = "Roger"
            await message.channel.send("Dillon's hero #5 is now Roger! :wolf: ")
        if message.content == "!ml hero5 add Ruby":
            dihero5 = "Ruby"
            await message.channel.send("Dillon's hero #5 is now Ruby! :heart: ")
        if message.content == "!ml hero5 add Sun":
            dihero5 = "Sun"
            await message.channel.send("Dillon's hero #5 is now Sun! :monkey_face: ")
        if message.content == "!ml hero5 add Thamuz":
            dihero5 = "Thamuz"
            await message.channel.send("Dillon's hero #5 is now Thamuz! :rage: ")
        if message.content == "!ml hero5 add Terizla":
            dihero5 = "Terizla"
            await message.channel.send("Dillon's hero #5 is now Terizla! :hammer: ")
        if message.content == "!ml hero5 add Zilong":
            dihero5 = "Zilong"
            await message.channel.send("Dillon's hero #5 is now Zilong! :dragon: ")
        if message.content == "!ml hero5 add Fanny":
            dihero5 = "Fanny"
            await message.channel.send("Dillon's hero #5 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero5 add Gusion":
            dihero5 = "Gusion"
            await message.channel.send(
                "Dillon's hero #5 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero5 add Hanzo":
            dihero5 = "Hanzo"
            await message.channel.send("Dillon's hero #5 is now Hanzo! :ghost: ")
        if message.content == "!ml hero5 add Hayabusa":
            dihero5 = "Hayabusa"
            await message.channel.send("Dillon's hero #5 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero5 add Helcurt":
            dihero5 = "Helcurt"
            await message.channel.send("Dillon's hero #5 is now Helcurt! :mute:  ")
        if message.content == "!ml hero5 add Karina":
            dihero5 = "Karina"
            await message.channel.send("Dillon's hero #5 is now Karina! :purple_heart: ")
        if message.content == "!ml hero5 add Lancelot":
            dihero5 = "Lancelot"
            await message.channel.send("Dillon's hero #5 is now Lancelot! :fencer: ")
        if message.content == "!ml hero5 add Lesley":
            dihero5 = "Lesley"
            await message.channel.send("Dillon's hero #5 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero5 add Natalia":
            dihero5 = "Natalia"
            await message.channel.send("Dillon's hero #5 is now Natalia! :spy::excladition: ")
        if message.content == "!ml hero5 add Saber":
            dihero5 = "Saber"
            await message.channel.send("Dillon's hero #5 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero5 add Selena":
            dihero5 = "Selena"
            await message.channel.send("Dillon's hero #5 is now Selena! :sleeping:  ")
        if message.content == "!ml hero5 add Alice":
            dihero5 = "Alice"
            await message.channel.send("Dillon's hero #5 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero5 add Aurora":
            dihero5 = "Aurora"
            await message.channel.send("Dillon's hero #5 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            dihero5 = "Chang'e"
            await message.channel.send("Dillon's hero #5 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero5 add Cyclops":
            dihero5 = "Cyclops"
            await message.channel.send("Dillon's hero #5 is now Cyclops! :eye:  ")
        if message.content == "!ml hero5 add Eudora":
            dihero5 = "Eudora"
            await message.channel.send("Dillon's hero #5 is now Eudora! :zap: ")
        if message.content == "!ml hero5 add Faramis":
            dihero5 = "Faramis"
            await message.channel.send("Dillon's hero #5 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero5 add Gord":
            dihero5 = "Gord"
            await message.channel.send("Dillon's hero #5 is now Gord! :snowboarder:")
        if message.content == "!ml hero5 add Harith":
            dihero5 = "Harith"
            await message.channel.send("Dillon's hero #5 is now Harith! :older_din: ")
        if message.content == "!ml hero5 add Harley":
            dihero5 = "Harley"
            await message.channel.send("Dillon's hero #5 is now Harley! :tophat: ")
        if message.content == "!ml hero5 add Kadita":
            dihero5 = "Kadita"
            await message.channel.send("Dillon's hero #5 is now Kadita! :droplet: ")
        if message.content == "!ml hero5 add Kagura":
            dihero5 = "Kagura"
            await message.channel.send("Dillon's hero #5 is now Kagura! :umbrella5:  ")
        if message.content == "!ml hero5 add Lunox":
            dihero5 = "Lunox"
            await message.channel.send("Dillon's hero #5 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero5 add Lylia":
            dihero5 = "Lylia"
            await message.channel.send("Dillon's hero #5 is now Lylia! :boom: ")
        if message.content == "!ml hero5 add Nana":
            dihero5 = "Nana"
            await message.channel.send("Dillon's hero #5 is now Nana! :cat:  ")
        if message.content == "!ml hero5 add Odette":
            dihero5 = "Odette"
            await message.channel.send("Dillon's hero #5 is now Odette! :duck: ")
        if message.content == "!ml hero5 add Pharsa":
            dihero5 = "Pharsa"
            await message.channel.send("Dillon's hero #5 is now Pharsa! :dove:  ")
        if message.content == "!ml hero5 add Vale":
            dihero5 = "Vale"
            await message.channel.send("Dillon's hero #5 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero5 add Valir":
            dihero5 = "Valir"
            await message.channel.send("Dillon's hero #5 is now Valir! :fire:")
        if message.content == "!ml hero5 add Vexanna":
            dihero5 = "Vexanna"
            await message.channel.send("Dillon's hero #5 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero5 add Bruno":
            dihero5 = "Bruno"
            await message.channel.send("Dillon's hero #5 is now Bruno! :soccer:  ")
        if message.content == "!ml hero5 add Claude":
            dihero5 = "Claude"
            await message.channel.send("Dillon's hero #5 is now Claude! :monkey:  ")
        if message.content == "!ml hero5 add Clint":
            dihero5 = "Clint"
            await message.channel.send("Dillon's hero #5 is now Clint! :cowboy: ")
        if message.content == "!ml hero5 add Granger":
            dihero5 = "Granger"
            await message.channel.send("Dillon's hero #5 is now Granger! :violin: ")
        if message.content == "!ml hero5 add Hanabi":
            dihero5 = "Hanabi"
            await message.channel.send("Dillon's hero #5 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero5 add Irithel":
            dihero5 = "Irithel"
            await message.channel.send("Dillon's hero #5 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero5 add Karrie":
            dihero5 = "Karrie"
            await message.channel.send(
                "Dillon's hero #5 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero5 add Kimmy":
            dihero5 = "Kimmy"
            await message.channel.send("Dillon's hero #5 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero5 add Layla":
            dihero5 = "Layla"
            await message.channel.send("Dillon's hero #5 is now Layla! :haircut:  ")
        if message.content == "!ml hero5 add Miya":
            dihero5 = "Miya"
            await message.channel.send("Dillon's hero #5 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero5 add Moskov":
            dihero5 = "Moskov"
            await message.channel.send("Dillon's hero #5 is now Moskov! :imp: ")
        if message.content == "!ml hero5 add Yi Sun-Shin":
            dihero5 = "Yi Sun-Shin"
            await message.channel.send("Dillon's hero #5 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero5 add Angela":
            dihero5 = "Angela"
            await message.channel.send("Dillon's hero #5 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero5 add Diggie":
            dihero5 = "Diggie"
            await message.channel.send("Dillon's hero #5 is now Diggie! :owl: ")
        if message.content == "!ml hero5 add Estes":
            dihero5 = "Estes"
            await message.channel.send("Dillon's hero #5 is now Estes! :ear:  ")
        if message.content == "!ml hero5 add Rafaela":
            dihero5 = "Rafaela"
            await message.channel.send("Dillon's hero #5 is now Rafaela! :angel: ")
        if message.content == "!ml hero5 add Rynn":
            dihero5 = "Rynn"
            await message.channel.send("Dillon's hero #5 is now Rynn! ")
        if message.content == "!ml hero6 add Akai":
            global dihero6
            dihero6 = "Akai"
            await message.channel.send("Dillon's hero #6 is now Akai! :panda_face: ")
        if message.content == "!ml hero6 add Balmond":
            dihero6 = "Balmond"
            await message.channel.send("Dillon's hero #6 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero6 add Belerick":
            dihero6 = "Belerick"
            await message.channel.send("Dillon's hero #6 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero6 add Franco":
            dihero6 = "Franco"
            await message.channel.send("Dillon's hero #6 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero6 add Esmerelda":
            dihero6 = "Esmerelda"
            await message.channel.send("Dillon's hero #6 is now Esmerelda! :shield: ")
        if message.content == "!ml hero6 add Gatotkaca":
            dihero6 = "Gatotkaca"
            await message.channel.send("Dillon's hero #6 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero6 add Grock":
            dihero6 = "Grock"
            await message.channel.send("Dillon's hero #6 is now Grock! :european_castle: ")
        if message.content == "!ml hero6 add Hilda":
            dihero6 = "Hilda"
            await message.channel.send("Dillon's hero #6 is now Hilda! :runner: ")
        if message.content == "!ml hero6 add Hylos":
            dihero6 = "Hylos"
            await message.channel.send("Dillon's hero #6 is now Hylos! :unicorn: ")
        if message.content == "!ml hero6 add Johnson":
            dihero6 = "Johnson"
            await message.channel.send("Dillon's hero #6 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero6 add Khufra":
            dihero6 = "Khufra"
            await message.channel.send("Dillon's hero #6 is now Khufra! :clown: ")
        if message.content == "!ml hero6 add Lolita":
            dihero6 = "Lolita"
            await message.channel.send("Dillon's hero #6 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            dihero6 = "Masha"
            await message.channel.send("Dillon's hero #6 is now Masha! :bear: ")
        if message.content == "!ml hero6 add Minotaur":
            dihero6 = "Minotaur"
            await message.channel.send("Dillon's hero #6 is now Minotaur! :cow: ")
        if message.content == "!ml hero6 add Tigreal":
            dihero6 = "Tigreal"
            await message.channel.send("Dillon's hero #6 is now Tigreal! :moyai: ")
        if message.content == "!ml hero6 add Uranus":
            dihero6 = "Uranus"
            await message.channel.send("Dillon's hero #6 is now Uranus! :peach: ")
        if message.content == "!ml hero6 add X.Borg":
            dihero6 = "X.Borg"
            await message.channel.send("Dillon's hero #6 is now X.Borg! :fire: ")
        if message.content == "!ml hero6 add Aldous":
            dihero6 = "Aldous"
            await message.channel.send("Dillon's hero #6 is now Aldous! :fist: ")
        if message.content == "!ml hero6 add Alpha":
            dihero6 = "Alpha"
            await message.channel.send("Dillon's hero #6 is now Alpha! :airplane: ")
        if message.content == "!ml hero6 add Alucard":
            dihero6 = "Alucard"
            await message.channel.send("Dillon's hero #6 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero6 add Argus":
            dihero6 = "Argus"
            await message.channel.send("Dillon's hero #6 is now Argus! :angel: ")
        if message.content == "!ml hero6 add Badang":
            dihero6 = "Badang"
            await message.channel.send("Dillon's hero #6 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero6 add Bane":
            dihero6 = "Bane"
            await message.channel.send("Dillon's hero #6 is now Bane! :octopus: ")
        if message.content == "!ml hero6 add Chou":
            dihero6 = "Chou"
            await message.channel.send("Dillon's hero #6 is now Chou! :dirtial_arts_uniform: ")
        if message.content == "!ml hero6 add Dyrroth":
            dihero6 = "Dyrroth"
            await message.channel.send("Dillon's hero #6 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero6 add Freya":
            dihero6 = "Freya"
            await message.channel.send("Dillon's hero #6 is now Freya! :hammer: ")
        if message.content == "!ml hero6 add Guinevere":
            dihero6 = "Guinevere"
            await message.channel.send("Dillon's hero #6 is now Guinevere! :dress:  ")
        if message.content == "!ml hero6 add Jawhead":
            dihero6 = "Jawhead"
            await message.channel.send("Dillon's hero #6 is now Jawhead! :robot: ")
        if message.content == "!ml hero6 add Kaja":
            dihero6 = "Kaja"
            await message.channel.send("Dillon's hero #6 is now Kaja! :bird: ")
        if message.content == "!ml hero6 add Lapu-Lapu":
            dihero6 = "Lapu-Lapu"
            await message.channel.send("Dillon's hero #6 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero6 add Leomord":
            dihero6 = "Leomord"
            await message.channel.send("Dillon's hero #6 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero6 add Martis":
            dihero6 = "Martis"
            await message.channel.send("Dillon's hero #6 is now Martis! :crab: ")
        if message.content == "!ml hero6 add Minsitthar":
            dihero6 = "Minsitthar"
            await message.channel.send("Dillon's hero #6 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero6 add Roger":
            dihero6 = "Roger"
            await message.channel.send("Dillon's hero #6 is now Roger! :wolf: ")
        if message.content == "!ml hero6 add Ruby":
            dihero6 = "Ruby"
            await message.channel.send("Dillon's hero #6 is now Ruby! :heart: ")
        if message.content == "!ml hero6 add Sun":
            dihero6 = "Sun"
            await message.channel.send("Dillon's hero #6 is now Sun! :monkey_face: ")
        if message.content == "!ml hero6 add Thamuz":
            dihero6 = "Thamuz"
            await message.channel.send("Dillon's hero #6 is now Thamuz! :rage: ")
        if message.content == "!ml hero6 add Terizla":
            dihero6 = "Terizla"
            await message.channel.send("Dillon's hero #6 is now Terizla! :hammer: ")
        if message.content == "!ml hero6 add Zilong":
            dihero6 = "Zilong"
            await message.channel.send("Dillon's hero #6 is now Zilong! :dragon: ")
        if message.content == "!ml hero6 add Fanny":
            dihero6 = "Fanny"
            await message.channel.send("Dillon's hero #6 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero6 add Gusion":
            dihero6 = "Gusion"
            await message.channel.send(
                "Dillon's hero #6 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero6 add Hanzo":
            dihero6 = "Hanzo"
            await message.channel.send("Dillon's hero #6 is now Hanzo! :ghost: ")
        if message.content == "!ml hero6 add Hayabusa":
            dihero6 = "Hayabusa"
            await message.channel.send("Dillon's hero #6 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero6 add Helcurt":
            dihero6 = "Helcurt"
            await message.channel.send("Dillon's hero #6 is now Helcurt! :mute:  ")
        if message.content == "!ml hero6 add Karina":
            dihero6 = "Karina"
            await message.channel.send("Dillon's hero #6 is now Karina! :purple_heart: ")
        if message.content == "!ml hero6 add Lancelot":
            dihero6 = "Lancelot"
            await message.channel.send("Dillon's hero #6 is now Lancelot! :fencer: ")
        if message.content == "!ml hero6 add Lesley":
            dihero6 = "Lesley"
            await message.channel.send("Dillon's hero #6 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero6 add Natalia":
            dihero6 = "Natalia"
            await message.channel.send("Dillon's hero #6 is now Natalia! :spy::excladition: ")
        if message.content == "!ml hero6 add Saber":
            dihero6 = "Saber"
            await message.channel.send("Dillon's hero #6 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero6 add Selena":
            dihero6 = "Selena"
            await message.channel.send("Dillon's hero #6 is now Selena! :sleeping:  ")
        if message.content == "!ml hero6 add Alice":
            dihero6 = "Alice"
            await message.channel.send("Dillon's hero #6 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero6 add Aurora":
            dihero6 = "Aurora"
            await message.channel.send("Dillon's hero #6 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            dihero6 = "Chang'e"
            await message.channel.send("Dillon's hero #6 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero6 add Cyclops":
            dihero6 = "Cyclops"
            await message.channel.send("Dillon's hero #6 is now Cyclops! :eye:  ")
        if message.content == "!ml hero6 add Eudora":
            dihero6 = "Eudora"
            await message.channel.send("Dillon's hero #6 is now Eudora! :zap: ")
        if message.content == "!ml hero6 add Faramis":
            dihero6 = "Faramis"
            await message.channel.send("Dillon's hero #6 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero6 add Gord":
            dihero6 = "Gord"
            await message.channel.send("Dillon's hero #6 is now Gord! :snowboarder:")
        if message.content == "!ml hero6 add Harith":
            dihero6 = "Harith"
            await message.channel.send("Dillon's hero #6 is now Harith! :older_din: ")
        if message.content == "!ml hero6 add Harley":
            dihero6 = "Harley"
            await message.channel.send("Dillon's hero #6 is now Harley! :tophat: ")
        if message.content == "!ml hero6 add Kadita":
            dihero6 = "Kadita"
            await message.channel.send("Dillon's hero #6 is now Kadita! :droplet: ")
        if message.content == "!ml hero6 add Kagura":
            dihero6 = "Kagura"
            await message.channel.send("Dillon's hero #6 is now Kagura! :umbrella6:  ")
        if message.content == "!ml hero6 add Lunox":
            dihero6 = "Lunox"
            await message.channel.send("Dillon's hero #6 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero6 add Lylia":
            dihero6 = "Lylia"
            await message.channel.send("Dillon's hero #6 is now Lylia! :boom: ")
        if message.content == "!ml hero6 add Nana":
            dihero6 = "Nana"
            await message.channel.send("Dillon's hero #6 is now Nana! :cat:  ")
        if message.content == "!ml hero6 add Odette":
            dihero6 = "Odette"
            await message.channel.send("Dillon's hero #6 is now Odette! :duck: ")
        if message.content == "!ml hero6 add Pharsa":
            dihero6 = "Pharsa"
            await message.channel.send("Dillon's hero #6 is now Pharsa! :dove:  ")
        if message.content == "!ml hero6 add Vale":
            dihero6 = "Vale"
            await message.channel.send("Dillon's hero #6 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero6 add Valir":
            dihero6 = "Valir"
            await message.channel.send("Dillon's hero #6 is now Valir! :fire:")
        if message.content == "!ml hero6 add Vexanna":
            dihero6 = "Vexanna"
            await message.channel.send("Dillon's hero #6 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero6 add Bruno":
            dihero6 = "Bruno"
            await message.channel.send("Dillon's hero #6 is now Bruno! :soccer:  ")
        if message.content == "!ml hero6 add Claude":
            dihero6 = "Claude"
            await message.channel.send("Dillon's hero #6 is now Claude! :monkey:  ")
        if message.content == "!ml hero6 add Clint":
            dihero6 = "Clint"
            await message.channel.send("Dillon's hero #6 is now Clint! :cowboy: ")
        if message.content == "!ml hero6 add Granger":
            dihero6 = "Granger"
            await message.channel.send("Dillon's hero #6 is now Granger! :violin: ")
        if message.content == "!ml hero6 add Hanabi":
            dihero6 = "Hanabi"
            await message.channel.send("Dillon's hero #6 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero6 add Irithel":
            dihero6 = "Irithel"
            await message.channel.send("Dillon's hero #6 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero6 add Karrie":
            dihero6 = "Karrie"
            await message.channel.send(
                "Dillon's hero #6 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero6 add Kimmy":
            dihero6 = "Kimmy"
            await message.channel.send("Dillon's hero #6 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero6 add Layla":
            dihero6 = "Layla"
            await message.channel.send("Dillon's hero #6 is now Layla! :haircut:  ")
        if message.content == "!ml hero6 add Miya":
            dihero6 = "Miya"
            await message.channel.send("Dillon's hero #6 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero6 add Moskov":
            dihero6 = "Moskov"
            await message.channel.send("Dillon's hero #6 is now Moskov! :imp: ")
        if message.content == "!ml hero6 add Yi Sun-Shin":
            dihero6 = "Yi Sun-Shin"
            await message.channel.send("Dillon's hero #6 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero6 add Angela":
            dihero6 = "Angela"
            await message.channel.send("Dillon's hero #6 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero6 add Diggie":
            dihero6 = "Diggie"
            await message.channel.send("Dillon's hero #6 is now Diggie! :owl: ")
        if message.content == "!ml hero6 add Estes":
            dihero6 = "Estes"
            await message.channel.send("Dillon's hero #6 is now Estes! :ear:  ")
        if message.content == "!ml hero6 add Rafaela":
            dihero6 = "Rafaela"
            await message.channel.send("Dillon's hero #6 is now Rafaela! :angel: ")
        if message.content == "!ml hero6 add Rynn":
            dihero6 = "Rynn"
            await message.channel.send("Dillon's hero #6 is now Rynn! ")
        if message.content == "!ml hero7 add Akai":
            global dihero7
            dihero7 = "Akai"
            await message.channel.send("Dillon's hero #7 is now Akai! :panda_face: ")
        if message.content == "!ml hero7 add Balmond":
            dihero7 = "Balmond"
            await message.channel.send("Dillon's hero #7 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero7 add Belerick":
            dihero7 = "Belerick"
            await message.channel.send("Dillon's hero #7 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero7 add Franco":
            dihero7 = "Franco"
            await message.channel.send("Dillon's hero #7 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero7 add Esmerelda":
            dihero7 = "Esmerelda"
            await message.channel.send("Dillon's hero #7 is now Esmerelda! :shield: ")
        if message.content == "!ml hero7 add Gatotkaca":
            dihero7 = "Gatotkaca"
            await message.channel.send("Dillon's hero #7 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero7 add Grock":
            dihero7 = "Grock"
            await message.channel.send("Dillon's hero #7 is now Grock! :european_castle: ")
        if message.content == "!ml hero7 add Hilda":
            dihero7 = "Hilda"
            await message.channel.send("Dillon's hero #7 is now Hilda! :runner: ")
        if message.content == "!ml hero7 add Hylos":
            dihero7 = "Hylos"
            await message.channel.send("Dillon's hero #7 is now Hylos! :unicorn: ")
        if message.content == "!ml hero7 add Johnson":
            dihero7 = "Johnson"
            await message.channel.send("Dillon's hero #7 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero7 add Khufra":
            dihero7 = "Khufra"
            await message.channel.send("Dillon's hero #7 is now Khufra! :clown: ")
        if message.content == "!ml hero7 add Lolita":
            dihero7 = "Lolita"
            await message.channel.send("Dillon's hero #7 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            dihero7 = "Masha"
            await message.channel.send("Dillon's hero #7 is now Masha! :bear: ")
        if message.content == "!ml hero7 add Minotaur":
            dihero7 = "Minotaur"
            await message.channel.send("Dillon's hero #7 is now Minotaur! :cow: ")
        if message.content == "!ml hero7 add Tigreal":
            dihero7 = "Tigreal"
            await message.channel.send("Dillon's hero #7 is now Tigreal! :moyai: ")
        if message.content == "!ml hero7 add Uranus":
            dihero7 = "Uranus"
            await message.channel.send("Dillon's hero #7 is now Uranus! :peach: ")
        if message.content == "!ml hero7 add X.Borg":
            dihero7 = "X.Borg"
            await message.channel.send("Dillon's hero #7 is now X.Borg! :fire: ")
        if message.content == "!ml hero7 add Aldous":
            dihero7 = "Aldous"
            await message.channel.send("Dillon's hero #7 is now Aldous! :fist: ")
        if message.content == "!ml hero7 add Alpha":
            dihero7 = "Alpha"
            await message.channel.send("Dillon's hero #7 is now Alpha! :airplane: ")
        if message.content == "!ml hero7 add Alucard":
            dihero7 = "Alucard"
            await message.channel.send("Dillon's hero #7 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero7 add Argus":
            dihero7 = "Argus"
            await message.channel.send("Dillon's hero #7 is now Argus! :angel: ")
        if message.content == "!ml hero7 add Badang":
            dihero7 = "Badang"
            await message.channel.send("Dillon's hero #7 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero7 add Bane":
            dihero7 = "Bane"
            await message.channel.send("Dillon's hero #7 is now Bane! :octopus: ")
        if message.content == "!ml hero7 add Chou":
            dihero7 = "Chou"
            await message.channel.send("Dillon's hero #7 is now Chou! :dirtial_arts_uniform: ")
        if message.content == "!ml hero7 add Dyrroth":
            dihero7 = "Dyrroth"
            await message.channel.send("Dillon's hero #7 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero7 add Freya":
            dihero7 = "Freya"
            await message.channel.send("Dillon's hero #7 is now Freya! :hammer: ")
        if message.content == "!ml hero7 add Guinevere":
            dihero7 = "Guinevere"
            await message.channel.send("Dillon's hero #7 is now Guinevere! :dress:  ")
        if message.content == "!ml hero7 add Jawhead":
            dihero7 = "Jawhead"
            await message.channel.send("Dillon's hero #7 is now Jawhead! :robot: ")
        if message.content == "!ml hero7 add Kaja":
            dihero7 = "Kaja"
            await message.channel.send("Dillon's hero #7 is now Kaja! :bird: ")
        if message.content == "!ml hero7 add Lapu-Lapu":
            dihero7 = "Lapu-Lapu"
            await message.channel.send("Dillon's hero #7 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero7 add Leomord":
            dihero7 = "Leomord"
            await message.channel.send("Dillon's hero #7 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero7 add Martis":
            dihero7 = "Martis"
            await message.channel.send("Dillon's hero #7 is now Martis! :crab: ")
        if message.content == "!ml hero7 add Minsitthar":
            dihero7 = "Minsitthar"
            await message.channel.send("Dillon's hero #7 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero7 add Roger":
            dihero7 = "Roger"
            await message.channel.send("Dillon's hero #7 is now Roger! :wolf: ")
        if message.content == "!ml hero7 add Ruby":
            dihero7 = "Ruby"
            await message.channel.send("Dillon's hero #7 is now Ruby! :heart: ")
        if message.content == "!ml hero7 add Sun":
            dihero7 = "Sun"
            await message.channel.send("Dillon's hero #7 is now Sun! :monkey_face: ")
        if message.content == "!ml hero7 add Thamuz":
            dihero7 = "Thamuz"
            await message.channel.send("Dillon's hero #7 is now Thamuz! :rage: ")
        if message.content == "!ml hero7 add Terizla":
            dihero7 = "Terizla"
            await message.channel.send("Dillon's hero #7 is now Terizla! :hammer: ")
        if message.content == "!ml hero7 add Zilong":
            dihero7 = "Zilong"
            await message.channel.send("Dillon's hero #7 is now Zilong! :dragon: ")
        if message.content == "!ml hero7 add Fanny":
            dihero7 = "Fanny"
            await message.channel.send("Dillon's hero #7 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero7 add Gusion":
            dihero7 = "Gusion"
            await message.channel.send(
                "Dillon's hero #7 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero7 add Hanzo":
            dihero7 = "Hanzo"
            await message.channel.send("Dillon's hero #7 is now Hanzo! :ghost: ")
        if message.content == "!ml hero7 add Hayabusa":
            dihero7 = "Hayabusa"
            await message.channel.send("Dillon's hero #7 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero7 add Helcurt":
            dihero7 = "Helcurt"
            await message.channel.send("Dillon's hero #7 is now Helcurt! :mute:  ")
        if message.content == "!ml hero7 add Karina":
            dihero7 = "Karina"
            await message.channel.send("Dillon's hero #7 is now Karina! :purple_heart: ")
        if message.content == "!ml hero7 add Lancelot":
            dihero7 = "Lancelot"
            await message.channel.send("Dillon's hero #7 is now Lancelot! :fencer: ")
        if message.content == "!ml hero7 add Lesley":
            dihero7 = "Lesley"
            await message.channel.send("Dillon's hero #7 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero7 add Natalia":
            dihero7 = "Natalia"
            await message.channel.send("Dillon's hero #7 is now Natalia! :spy::excladition: ")
        if message.content == "!ml hero7 add Saber":
            dihero7 = "Saber"
            await message.channel.send("Dillon's hero #7 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero7 add Selena":
            dihero7 = "Selena"
            await message.channel.send("Dillon's hero #7 is now Selena! :sleeping:  ")
        if message.content == "!ml hero7 add Alice":
            dihero7 = "Alice"
            await message.channel.send("Dillon's hero #7 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero7 add Aurora":
            dihero7 = "Aurora"
            await message.channel.send("Dillon's hero #7 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            dihero7 = "Chang'e"
            await message.channel.send("Dillon's hero #7 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero7 add Cyclops":
            dihero7 = "Cyclops"
            await message.channel.send("Dillon's hero #7 is now Cyclops! :eye:  ")
        if message.content == "!ml hero7 add Eudora":
            dihero7 = "Eudora"
            await message.channel.send("Dillon's hero #7 is now Eudora! :zap: ")
        if message.content == "!ml hero7 add Faramis":
            dihero7 = "Faramis"
            await message.channel.send("Dillon's hero #7 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero7 add Gord":
            dihero7 = "Gord"
            await message.channel.send("Dillon's hero #7 is now Gord! :snowboarder:")
        if message.content == "!ml hero7 add Harith":
            dihero7 = "Harith"
            await message.channel.send("Dillon's hero #7 is now Harith! :older_din: ")
        if message.content == "!ml hero7 add Harley":
            dihero7 = "Harley"
            await message.channel.send("Dillon's hero #7 is now Harley! :tophat: ")
        if message.content == "!ml hero7 add Kadita":
            dihero7 = "Kadita"
            await message.channel.send("Dillon's hero #7 is now Kadita! :droplet: ")
        if message.content == "!ml hero7 add Kagura":
            dihero7 = "Kagura"
            await message.channel.send("Dillon's hero #7 is now Kagura! :umbrella7:  ")
        if message.content == "!ml hero7 add Lunox":
            dihero7 = "Lunox"
            await message.channel.send("Dillon's hero #7 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero7 add Lylia":
            dihero7 = "Lylia"
            await message.channel.send("Dillon's hero #7 is now Lylia! :boom: ")
        if message.content == "!ml hero7 add Nana":
            dihero7 = "Nana"
            await message.channel.send("Dillon's hero #7 is now Nana! :cat:  ")
        if message.content == "!ml hero7 add Odette":
            dihero7 = "Odette"
            await message.channel.send("Dillon's hero #7 is now Odette! :duck: ")
        if message.content == "!ml hero7 add Pharsa":
            dihero7 = "Pharsa"
            await message.channel.send("Dillon's hero #7 is now Pharsa! :dove:  ")
        if message.content == "!ml hero7 add Vale":
            dihero7 = "Vale"
            await message.channel.send("Dillon's hero #7 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero7 add Valir":
            dihero7 = "Valir"
            await message.channel.send("Dillon's hero #7 is now Valir! :fire:")
        if message.content == "!ml hero7 add Vexanna":
            dihero7 = "Vexanna"
            await message.channel.send("Dillon's hero #7 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero7 add Bruno":
            dihero7 = "Bruno"
            await message.channel.send("Dillon's hero #7 is now Bruno! :soccer:  ")
        if message.content == "!ml hero7 add Claude":
            dihero7 = "Claude"
            await message.channel.send("Dillon's hero #7 is now Claude! :monkey:  ")
        if message.content == "!ml hero7 add Clint":
            dihero7 = "Clint"
            await message.channel.send("Dillon's hero #7 is now Clint! :cowboy: ")
        if message.content == "!ml hero7 add Granger":
            dihero7 = "Granger"
            await message.channel.send("Dillon's hero #7 is now Granger! :violin: ")
        if message.content == "!ml hero7 add Hanabi":
            dihero7 = "Hanabi"
            await message.channel.send("Dillon's hero #7 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero7 add Irithel":
            dihero7 = "Irithel"
            await message.channel.send("Dillon's hero #7 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero7 add Karrie":
            dihero7 = "Karrie"
            await message.channel.send(
                "Dillon's hero #7 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero7 add Kimmy":
            dihero7 = "Kimmy"
            await message.channel.send("Dillon's hero #7 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero7 add Layla":
            dihero7 = "Layla"
            await message.channel.send("Dillon's hero #7 is now Layla! :haircut:  ")
        if message.content == "!ml hero7 add Miya":
            dihero7 = "Miya"
            await message.channel.send("Dillon's hero #7 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero7 add Moskov":
            dihero7 = "Moskov"
            await message.channel.send("Dillon's hero #7 is now Moskov! :imp: ")
        if message.content == "!ml hero7 add Yi Sun-Shin":
            dihero7 = "Yi Sun-Shin"
            await message.channel.send("Dillon's hero #7 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero7 add Angela":
            dihero7 = "Angela"
            await message.channel.send("Dillon's hero #7 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero7 add Diggie":
            dihero7 = "Diggie"
            await message.channel.send("Dillon's hero #7 is now Diggie! :owl: ")
        if message.content == "!ml hero7 add Estes":
            dihero7 = "Estes"
            await message.channel.send("Dillon's hero #7 is now Estes! :ear:  ")
        if message.content == "!ml hero7 add Rafaela":
            dihero7 = "Rafaela"
            await message.channel.send("Dillon's hero #7 is now Rafaela! :angel: ")
        if message.content == "!ml hero7 add Rynn":
            dihero7 = "Rynn"
            await message.channel.send("Dillon's hero #7 is now Rynn! ")
        if message.content == "!ml hero8 add Akai":
            global dihero8
            dihero8 = "Akai"
            await message.channel.send("Dillon's hero #8 is now Akai! :panda_face: ")
        if message.content == "!ml hero8 add Balmond":
            dihero8 = "Balmond"
            await message.channel.send("Dillon's hero #8 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero8 add Belerick":
            dihero8 = "Belerick"
            await message.channel.send("Dillon's hero #8 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero8 add Franco":
            dihero8 = "Franco"
            await message.channel.send("Dillon's hero #8 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero8 add Esmerelda":
            dihero8 = "Esmerelda"
            await message.channel.send("Dillon's hero #8 is now Esmerelda! :shield: ")
        if message.content == "!ml hero8 add Gatotkaca":
            dihero8 = "Gatotkaca"
            await message.channel.send("Dillon's hero #8 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero8 add Grock":
            dihero8 = "Grock"
            await message.channel.send("Dillon's hero #8 is now Grock! :european_castle: ")
        if message.content == "!ml hero8 add Hilda":
            dihero8 = "Hilda"
            await message.channel.send("Dillon's hero #8 is now Hilda! :runner: ")
        if message.content == "!ml hero8 add Hylos":
            dihero8 = "Hylos"
            await message.channel.send("Dillon's hero #8 is now Hylos! :unicorn: ")
        if message.content == "!ml hero8 add Johnson":
            dihero8 = "Johnson"
            await message.channel.send("Dillon's hero #8 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero8 add Khufra":
            dihero8 = "Khufra"
            await message.channel.send("Dillon's hero #8 is now Khufra! :clown: ")
        if message.content == "!ml hero8 add Lolita":
            dihero8 = "Lolita"
            await message.channel.send("Dillon's hero #8 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            dihero8 = "Masha"
            await message.channel.send("Dillon's hero #8 is now Masha! :bear: ")
        if message.content == "!ml hero8 add Minotaur":
            dihero8 = "Minotaur"
            await message.channel.send("Dillon's hero #8 is now Minotaur! :cow: ")
        if message.content == "!ml hero8 add Tigreal":
            dihero8 = "Tigreal"
            await message.channel.send("Dillon's hero #8 is now Tigreal! :moyai: ")
        if message.content == "!ml hero8 add Uranus":
            dihero8 = "Uranus"
            await message.channel.send("Dillon's hero #8 is now Uranus! :peach: ")
        if message.content == "!ml hero8 add X.Borg":
            dihero8 = "X.Borg"
            await message.channel.send("Dillon's hero #8 is now X.Borg! :fire: ")
        if message.content == "!ml hero8 add Aldous":
            dihero8 = "Aldous"
            await message.channel.send("Dillon's hero #8 is now Aldous! :fist: ")
        if message.content == "!ml hero8 add Alpha":
            dihero8 = "Alpha"
            await message.channel.send("Dillon's hero #8 is now Alpha! :airplane: ")
        if message.content == "!ml hero8 add Alucard":
            dihero8 = "Alucard"
            await message.channel.send("Dillon's hero #8 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero8 add Argus":
            dihero8 = "Argus"
            await message.channel.send("Dillon's hero #8 is now Argus! :angel: ")
        if message.content == "!ml hero8 add Badang":
            dihero8 = "Badang"
            await message.channel.send("Dillon's hero #8 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero8 add Bane":
            dihero8 = "Bane"
            await message.channel.send("Dillon's hero #8 is now Bane! :octopus: ")
        if message.content == "!ml hero8 add Chou":
            dihero8 = "Chou"
            await message.channel.send("Dillon's hero #8 is now Chou! :dirtial_arts_uniform: ")
        if message.content == "!ml hero8 add Dyrroth":
            dihero8 = "Dyrroth"
            await message.channel.send("Dillon's hero #8 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero8 add Freya":
            dihero8 = "Freya"
            await message.channel.send("Dillon's hero #8 is now Freya! :hammer: ")
        if message.content == "!ml hero8 add Guinevere":
            dihero8 = "Guinevere"
            await message.channel.send("Dillon's hero #8 is now Guinevere! :dress:  ")
        if message.content == "!ml hero8 add Jawhead":
            dihero8 = "Jawhead"
            await message.channel.send("Dillon's hero #8 is now Jawhead! :robot: ")
        if message.content == "!ml hero8 add Kaja":
            dihero8 = "Kaja"
            await message.channel.send("Dillon's hero #8 is now Kaja! :bird: ")
        if message.content == "!ml hero8 add Lapu-Lapu":
            dihero8 = "Lapu-Lapu"
            await message.channel.send("Dillon's hero #8 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero8 add Leomord":
            dihero8 = "Leomord"
            await message.channel.send("Dillon's hero #8 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero8 add Martis":
            dihero8 = "Martis"
            await message.channel.send("Dillon's hero #8 is now Martis! :crab: ")
        if message.content == "!ml hero8 add Minsitthar":
            dihero8 = "Minsitthar"
            await message.channel.send("Dillon's hero #8 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero8 add Roger":
            dihero8 = "Roger"
            await message.channel.send("Dillon's hero #8 is now Roger! :wolf: ")
        if message.content == "!ml hero8 add Ruby":
            dihero8 = "Ruby"
            await message.channel.send("Dillon's hero #8 is now Ruby! :heart: ")
        if message.content == "!ml hero8 add Sun":
            dihero8 = "Sun"
            await message.channel.send("Dillon's hero #8 is now Sun! :monkey_face: ")
        if message.content == "!ml hero8 add Thamuz":
            dihero8 = "Thamuz"
            await message.channel.send("Dillon's hero #8 is now Thamuz! :rage: ")
        if message.content == "!ml hero8 add Terizla":
            dihero8 = "Terizla"
            await message.channel.send("Dillon's hero #8 is now Terizla! :hammer: ")
        if message.content == "!ml hero8 add Zilong":
            dihero8 = "Zilong"
            await message.channel.send("Dillon's hero #8 is now Zilong! :dragon: ")
        if message.content == "!ml hero8 add Fanny":
            dihero8 = "Fanny"
            await message.channel.send("Dillon's hero #8 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero8 add Gusion":
            dihero8 = "Gusion"
            await message.channel.send(
                "Dillon's hero #8 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero8 add Hanzo":
            dihero8 = "Hanzo"
            await message.channel.send("Dillon's hero #8 is now Hanzo! :ghost: ")
        if message.content == "!ml hero8 add Hayabusa":
            dihero8 = "Hayabusa"
            await message.channel.send("Dillon's hero #8 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero8 add Helcurt":
            dihero8 = "Helcurt"
            await message.channel.send("Dillon's hero #8 is now Helcurt! :mute:  ")
        if message.content == "!ml hero8 add Karina":
            dihero8 = "Karina"
            await message.channel.send("Dillon's hero #8 is now Karina! :purple_heart: ")
        if message.content == "!ml hero8 add Lancelot":
            dihero8 = "Lancelot"
            await message.channel.send("Dillon's hero #8 is now Lancelot! :fencer: ")
        if message.content == "!ml hero8 add Lesley":
            dihero8 = "Lesley"
            await message.channel.send("Dillon's hero #8 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero8 add Natalia":
            dihero8 = "Natalia"
            await message.channel.send("Dillon's hero #8 is now Natalia! :spy::excladition: ")
        if message.content == "!ml hero8 add Saber":
            dihero8 = "Saber"
            await message.channel.send("Dillon's hero #8 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero8 add Selena":
            dihero8 = "Selena"
            await message.channel.send("Dillon's hero #8 is now Selena! :sleeping:  ")
        if message.content == "!ml hero8 add Alice":
            dihero8 = "Alice"
            await message.channel.send("Dillon's hero #8 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero8 add Aurora":
            dihero8 = "Aurora"
            await message.channel.send("Dillon's hero #8 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            dihero8 = "Chang'e"
            await message.channel.send("Dillon's hero #8 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero8 add Cyclops":
            dihero8 = "Cyclops"
            await message.channel.send("Dillon's hero #8 is now Cyclops! :eye:  ")
        if message.content == "!ml hero8 add Eudora":
            dihero8 = "Eudora"
            await message.channel.send("Dillon's hero #8 is now Eudora! :zap: ")
        if message.content == "!ml hero8 add Faramis":
            dihero8 = "Faramis"
            await message.channel.send("Dillon's hero #8 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero8 add Gord":
            dihero8 = "Gord"
            await message.channel.send("Dillon's hero #8 is now Gord! :snowboarder:")
        if message.content == "!ml hero8 add Harith":
            dihero8 = "Harith"
            await message.channel.send("Dillon's hero #8 is now Harith! :older_din: ")
        if message.content == "!ml hero8 add Harley":
            dihero8 = "Harley"
            await message.channel.send("Dillon's hero #8 is now Harley! :tophat: ")
        if message.content == "!ml hero8 add Kadita":
            dihero8 = "Kadita"
            await message.channel.send("Dillon's hero #8 is now Kadita! :droplet: ")
        if message.content == "!ml hero8 add Kagura":
            dihero8 = "Kagura"
            await message.channel.send("Dillon's hero #8 is now Kagura! :umbrella8:  ")
        if message.content == "!ml hero8 add Lunox":
            dihero8 = "Lunox"
            await message.channel.send("Dillon's hero #8 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero8 add Lylia":
            dihero8 = "Lylia"
            await message.channel.send("Dillon's hero #8 is now Lylia! :boom: ")
        if message.content == "!ml hero8 add Nana":
            dihero8 = "Nana"
            await message.channel.send("Dillon's hero #8 is now Nana! :cat:  ")
        if message.content == "!ml hero8 add Odette":
            dihero8 = "Odette"
            await message.channel.send("Dillon's hero #8 is now Odette! :duck: ")
        if message.content == "!ml hero8 add Pharsa":
            dihero8 = "Pharsa"
            await message.channel.send("Dillon's hero #8 is now Pharsa! :dove:  ")
        if message.content == "!ml hero8 add Vale":
            dihero8 = "Vale"
            await message.channel.send("Dillon's hero #8 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero8 add Valir":
            dihero8 = "Valir"
            await message.channel.send("Dillon's hero #8 is now Valir! :fire:")
        if message.content == "!ml hero8 add Vexanna":
            dihero8 = "Vexanna"
            await message.channel.send("Dillon's hero #8 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero8 add Bruno":
            dihero8 = "Bruno"
            await message.channel.send("Dillon's hero #8 is now Bruno! :soccer:  ")
        if message.content == "!ml hero8 add Claude":
            dihero8 = "Claude"
            await message.channel.send("Dillon's hero #8 is now Claude! :monkey:  ")
        if message.content == "!ml hero8 add Clint":
            dihero8 = "Clint"
            await message.channel.send("Dillon's hero #8 is now Clint! :cowboy: ")
        if message.content == "!ml hero8 add Granger":
            dihero8 = "Granger"
            await message.channel.send("Dillon's hero #8 is now Granger! :violin: ")
        if message.content == "!ml hero8 add Hanabi":
            dihero8 = "Hanabi"
            await message.channel.send("Dillon's hero #8 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero8 add Irithel":
            dihero8 = "Irithel"
            await message.channel.send("Dillon's hero #8 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero8 add Karrie":
            dihero8 = "Karrie"
            await message.channel.send(
                "Dillon's hero #8 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero8 add Kimmy":
            dihero8 = "Kimmy"
            await message.channel.send("Dillon's hero #8 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero8 add Layla":
            dihero8 = "Layla"
            await message.channel.send("Dillon's hero #8 is now Layla! :haircut:  ")
        if message.content == "!ml hero8 add Miya":
            dihero8 = "Miya"
            await message.channel.send("Dillon's hero #8 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero8 add Moskov":
            dihero8 = "Moskov"
            await message.channel.send("Dillon's hero #8 is now Moskov! :imp: ")
        if message.content == "!ml hero8 add Yi Sun-Shin":
            dihero8 = "Yi Sun-Shin"
            await message.channel.send("Dillon's hero #8 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero8 add Angela":
            dihero8 = "Angela"
            await message.channel.send("Dillon's hero #8 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero8 add Diggie":
            dihero8 = "Diggie"
            await message.channel.send("Dillon's hero #8 is now Diggie! :owl: ")
        if message.content == "!ml hero8 add Estes":
            dihero8 = "Estes"
            await message.channel.send("Dillon's hero #8 is now Estes! :ear:  ")
        if message.content == "!ml hero8 add Rafaela":
            dihero8 = "Rafaela"
            await message.channel.send("Dillon's hero #8 is now Rafaela! :angel: ")
        if message.content == "!ml hero8 add Rynn":
            dihero8 = "Rynn"
            await message.channel.send("Dillon's hero #8 is now Rynn! ")
        if message.content == "!ml hero9 add Akai":
            global dihero9
            dihero9 = "Akai"
            await message.channel.send("Dillon's hero #9 is now Akai! :panda_face: ")
        if message.content == "!ml hero9 add Balmond":
            dihero9 = "Balmond"
            await message.channel.send("Dillon's hero #9 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero9 add Belerick":
            dihero9 = "Belerick"
            await message.channel.send("Dillon's hero #9 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero9 add Franco":
            dihero9 = "Franco"
            await message.channel.send("Dillon's hero #9 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero9 add Esmerelda":
            dihero9 = "Esmerelda"
            await message.channel.send("Dillon's hero #9 is now Esmerelda! :shield: ")
        if message.content == "!ml hero9 add Gatotkaca":
            dihero9 = "Gatotkaca"
            await message.channel.send("Dillon's hero #9 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero9 add Grock":
            dihero9 = "Grock"
            await message.channel.send("Dillon's hero #9 is now Grock! :european_castle: ")
        if message.content == "!ml hero9 add Hilda":
            dihero9 = "Hilda"
            await message.channel.send("Dillon's hero #9 is now Hilda! :runner: ")
        if message.content == "!ml hero9 add Hylos":
            dihero9 = "Hylos"
            await message.channel.send("Dillon's hero #9 is now Hylos! :unicorn: ")
        if message.content == "!ml hero9 add Johnson":
            dihero9 = "Johnson"
            await message.channel.send("Dillon's hero #9 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero9 add Khufra":
            dihero9 = "Khufra"
            await message.channel.send("Dillon's hero #9 is now Khufra! :clown: ")
        if message.content == "!ml hero9 add Lolita":
            dihero9 = "Lolita"
            await message.channel.send("Dillon's hero #9 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            dihero9 = "Masha"
            await message.channel.send("Dillon's hero #9 is now Masha! :bear: ")
        if message.content == "!ml hero9 add Minotaur":
            dihero9 = "Minotaur"
            await message.channel.send("Dillon's hero #9 is now Minotaur! :cow: ")
        if message.content == "!ml hero9 add Tigreal":
            dihero9 = "Tigreal"
            await message.channel.send("Dillon's hero #9 is now Tigreal! :moyai: ")
        if message.content == "!ml hero9 add Uranus":
            dihero9 = "Uranus"
            await message.channel.send("Dillon's hero #9 is now Uranus! :peach: ")
        if message.content == "!ml hero9 add X.Borg":
            dihero9 = "X.Borg"
            await message.channel.send("Dillon's hero #9 is now X.Borg! :fire: ")
        if message.content == "!ml hero9 add Aldous":
            dihero9 = "Aldous"
            await message.channel.send("Dillon's hero #9 is now Aldous! :fist: ")
        if message.content == "!ml hero9 add Alpha":
            dihero9 = "Alpha"
            await message.channel.send("Dillon's hero #9 is now Alpha! :airplane: ")
        if message.content == "!ml hero9 add Alucard":
            dihero9 = "Alucard"
            await message.channel.send("Dillon's hero #9 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero9 add Argus":
            dihero9 = "Argus"
            await message.channel.send("Dillon's hero #9 is now Argus! :angel: ")
        if message.content == "!ml hero9 add Badang":
            dihero9 = "Badang"
            await message.channel.send("Dillon's hero #9 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero9 add Bane":
            dihero9 = "Bane"
            await message.channel.send("Dillon's hero #9 is now Bane! :octopus: ")
        if message.content == "!ml hero9 add Chou":
            dihero9 = "Chou"
            await message.channel.send("Dillon's hero #9 is now Chou! :dirtial_arts_uniform: ")
        if message.content == "!ml hero9 add Dyrroth":
            dihero9 = "Dyrroth"
            await message.channel.send("Dillon's hero #9 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero9 add Freya":
            dihero9 = "Freya"
            await message.channel.send("Dillon's hero #9 is now Freya! :hammer: ")
        if message.content == "!ml hero9 add Guinevere":
            dihero9 = "Guinevere"
            await message.channel.send("Dillon's hero #9 is now Guinevere! :dress:  ")
        if message.content == "!ml hero9 add Jawhead":
            dihero9 = "Jawhead"
            await message.channel.send("Dillon's hero #9 is now Jawhead! :robot: ")
        if message.content == "!ml hero9 add Kaja":
            dihero9 = "Kaja"
            await message.channel.send("Dillon's hero #9 is now Kaja! :bird: ")
        if message.content == "!ml hero9 add Lapu-Lapu":
            dihero9 = "Lapu-Lapu"
            await message.channel.send("Dillon's hero #9 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero9 add Leomord":
            dihero9 = "Leomord"
            await message.channel.send("Dillon's hero #9 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero9 add Martis":
            dihero9 = "Martis"
            await message.channel.send("Dillon's hero #9 is now Martis! :crab: ")
        if message.content == "!ml hero9 add Minsitthar":
            dihero9 = "Minsitthar"
            await message.channel.send("Dillon's hero #9 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero9 add Roger":
            dihero9 = "Roger"
            await message.channel.send("Dillon's hero #9 is now Roger! :wolf: ")
        if message.content == "!ml hero9 add Ruby":
            dihero9 = "Ruby"
            await message.channel.send("Dillon's hero #9 is now Ruby! :heart: ")
        if message.content == "!ml hero9 add Sun":
            dihero9 = "Sun"
            await message.channel.send("Dillon's hero #9 is now Sun! :monkey_face: ")
        if message.content == "!ml hero9 add Thamuz":
            dihero9 = "Thamuz"
            await message.channel.send("Dillon's hero #9 is now Thamuz! :rage: ")
        if message.content == "!ml hero9 add Terizla":
            dihero9 = "Terizla"
            await message.channel.send("Dillon's hero #9 is now Terizla! :hammer: ")
        if message.content == "!ml hero9 add Zilong":
            dihero9 = "Zilong"
            await message.channel.send("Dillon's hero #9 is now Zilong! :dragon: ")
        if message.content == "!ml hero9 add Fanny":
            dihero9 = "Fanny"
            await message.channel.send("Dillon's hero #9 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero9 add Gusion":
            dihero9 = "Gusion"
            await message.channel.send(
                "Dillon's hero #9 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero9 add Hanzo":
            dihero9 = "Hanzo"
            await message.channel.send("Dillon's hero #9 is now Hanzo! :ghost: ")
        if message.content == "!ml hero9 add Hayabusa":
            dihero9 = "Hayabusa"
            await message.channel.send("Dillon's hero #9 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero9 add Helcurt":
            dihero9 = "Helcurt"
            await message.channel.send("Dillon's hero #9 is now Helcurt! :mute:  ")
        if message.content == "!ml hero9 add Karina":
            dihero9 = "Karina"
            await message.channel.send("Dillon's hero #9 is now Karina! :purple_heart: ")
        if message.content == "!ml hero9 add Lancelot":
            dihero9 = "Lancelot"
            await message.channel.send("Dillon's hero #9 is now Lancelot! :fencer: ")
        if message.content == "!ml hero9 add Lesley":
            dihero9 = "Lesley"
            await message.channel.send("Dillon's hero #9 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero9 add Natalia":
            dihero9 = "Natalia"
            await message.channel.send("Dillon's hero #9 is now Natalia! :spy::excladition: ")
        if message.content == "!ml hero9 add Saber":
            dihero9 = "Saber"
            await message.channel.send("Dillon's hero #9 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero9 add Selena":
            dihero9 = "Selena"
            await message.channel.send("Dillon's hero #9 is now Selena! :sleeping:  ")
        if message.content == "!ml hero9 add Alice":
            dihero9 = "Alice"
            await message.channel.send("Dillon's hero #9 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero9 add Aurora":
            dihero9 = "Aurora"
            await message.channel.send("Dillon's hero #9 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            dihero9 = "Chang'e"
            await message.channel.send("Dillon's hero #9 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero9 add Cyclops":
            dihero9 = "Cyclops"
            await message.channel.send("Dillon's hero #9 is now Cyclops! :eye:  ")
        if message.content == "!ml hero9 add Eudora":
            dihero9 = "Eudora"
            await message.channel.send("Dillon's hero #9 is now Eudora! :zap: ")
        if message.content == "!ml hero9 add Faramis":
            dihero9 = "Faramis"
            await message.channel.send("Dillon's hero #9 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero9 add Gord":
            dihero9 = "Gord"
            await message.channel.send("Dillon's hero #9 is now Gord! :snowboarder:")
        if message.content == "!ml hero9 add Harith":
            dihero9 = "Harith"
            await message.channel.send("Dillon's hero #9 is now Harith! :older_din: ")
        if message.content == "!ml hero9 add Harley":
            dihero9 = "Harley"
            await message.channel.send("Dillon's hero #9 is now Harley! :tophat: ")
        if message.content == "!ml hero9 add Kadita":
            dihero9 = "Kadita"
            await message.channel.send("Dillon's hero #9 is now Kadita! :droplet: ")
        if message.content == "!ml hero9 add Kagura":
            dihero9 = "Kagura"
            await message.channel.send("Dillon's hero #9 is now Kagura! :umbrella9:  ")
        if message.content == "!ml hero9 add Lunox":
            dihero9 = "Lunox"
            await message.channel.send("Dillon's hero #9 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero9 add Lylia":
            dihero9 = "Lylia"
            await message.channel.send("Dillon's hero #9 is now Lylia! :boom: ")
        if message.content == "!ml hero9 add Nana":
            dihero9 = "Nana"
            await message.channel.send("Dillon's hero #9 is now Nana! :cat:  ")
        if message.content == "!ml hero9 add Odette":
            dihero9 = "Odette"
            await message.channel.send("Dillon's hero #9 is now Odette! :duck: ")
        if message.content == "!ml hero9 add Pharsa":
            dihero9 = "Pharsa"
            await message.channel.send("Dillon's hero #9 is now Pharsa! :dove:  ")
        if message.content == "!ml hero9 add Vale":
            dihero9 = "Vale"
            await message.channel.send("Dillon's hero #9 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero9 add Valir":
            dihero9 = "Valir"
            await message.channel.send("Dillon's hero #9 is now Valir! :fire:")
        if message.content == "!ml hero9 add Vexanna":
            dihero9 = "Vexanna"
            await message.channel.send("Dillon's hero #9 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero9 add Bruno":
            dihero9 = "Bruno"
            await message.channel.send("Dillon's hero #9 is now Bruno! :soccer:  ")
        if message.content == "!ml hero9 add Claude":
            dihero9 = "Claude"
            await message.channel.send("Dillon's hero #9 is now Claude! :monkey:  ")
        if message.content == "!ml hero9 add Clint":
            dihero9 = "Clint"
            await message.channel.send("Dillon's hero #9 is now Clint! :cowboy: ")
        if message.content == "!ml hero9 add Granger":
            dihero9 = "Granger"
            await message.channel.send("Dillon's hero #9 is now Granger! :violin: ")
        if message.content == "!ml hero9 add Hanabi":
            dihero9 = "Hanabi"
            await message.channel.send("Dillon's hero #9 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero9 add Irithel":
            dihero9 = "Irithel"
            await message.channel.send("Dillon's hero #9 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero9 add Karrie":
            dihero9 = "Karrie"
            await message.channel.send(
                "Dillon's hero #9 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero9 add Kimmy":
            dihero9 = "Kimmy"
            await message.channel.send("Dillon's hero #9 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero9 add Layla":
            dihero9 = "Layla"
            await message.channel.send("Dillon's hero #9 is now Layla! :haircut:  ")
        if message.content == "!ml hero9 add Miya":
            dihero9 = "Miya"
            await message.channel.send("Dillon's hero #9 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero9 add Moskov":
            dihero9 = "Moskov"
            await message.channel.send("Dillon's hero #9 is now Moskov! :imp: ")
        if message.content == "!ml hero9 add Yi Sun-Shin":
            dihero9 = "Yi Sun-Shin"
            await message.channel.send("Dillon's hero #9 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero9 add Angela":
            dihero9 = "Angela"
            await message.channel.send("Dillon's hero #9 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero9 add Diggie":
            dihero9 = "Diggie"
            await message.channel.send("Dillon's hero #9 is now Diggie! :owl: ")
        if message.content == "!ml hero9 add Estes":
            dihero9 = "Estes"
            await message.channel.send("Dillon's hero #9 is now Estes! :ear:  ")
        if message.content == "!ml hero9 add Rafaela":
            dihero9 = "Rafaela"
            await message.channel.send("Dillon's hero #9 is now Rafaela! :angel: ")
        if message.content == "!ml hero9 add Rynn":
            dihero9 = "Rynn"
            await message.channel.send("Dillon's hero #9 is now Rynn! ")
        if message.content == "!ml hero10 add Akai":
            global dihero10
            dihero10 = "Akai"
            await message.channel.send("Dillon's hero #10 is now Akai! :panda_face: ")
        if message.content == "!ml hero10 add Balmond":
            dihero10 = "Balmond"
            await message.channel.send("Dillon's hero #10 is now Balmond! :cloud_tornado: ")
        if message.content == "!ml hero10 add Belerick":
            dihero10 = "Belerick"
            await message.channel.send("Dillon's hero #10 is now Belerick! :tanabata_tree: ")
        if message.content == "!ml hero10 add Franco":
            dihero10 = "Franco"
            await message.channel.send("Dillon's hero #10 is now Franco! :fishing_pole_and_fish: ")
        if message.content == "!ml hero10 add Esmerelda":
            dihero10 = "Esmerelda"
            await message.channel.send("Dillon's hero #10 is now Esmerelda! :shield: ")
        if message.content == "!ml hero10 add Gatotkaca":
            dihero10 = "Gatotkaca"
            await message.channel.send("Dillon's hero #10 is now Gatotkaca! :cloud_lightning: ")
        if message.content == "!ml hero10 add Grock":
            dihero10 = "Grock"
            await message.channel.send("Dillon's hero #10 is now Grock! :european_castle: ")
        if message.content == "!ml hero10 add Hilda":
            dihero10 = "Hilda"
            await message.channel.send("Dillon's hero #10 is now Hilda! :runner: ")
        if message.content == "!ml hero10 add Hylos":
            dihero10 = "Hylos"
            await message.channel.send("Dillon's hero #10 is now Hylos! :unicorn: ")
        if message.content == "!ml hero10 add Johnson":
            dihero10 = "Johnson"
            await message.channel.send("Dillon's hero #10 is now Johnson! :fire_engine: ")
        if message.content == "!ml hero10 add Khufra":
            dihero10 = "Khufra"
            await message.channel.send("Dillon's hero #10 is now Khufra! :clown: ")
        if message.content == "!ml hero10 add Lolita":
            dihero10 = "Lolita"
            await message.channel.send("Dillon's hero #10 is now Lolita! :lollipop: ")
        if message.content == "!ml hero1 add Masha":
            dihero10 = "Masha"
            await message.channel.send("Dillon's hero #10 is now Masha! :bear: ")
        if message.content == "!ml hero10 add Minotaur":
            dihero10 = "Minotaur"
            await message.channel.send("Dillon's hero #10 is now Minotaur! :cow: ")
        if message.content == "!ml hero10 add Tigreal":
            dihero10 = "Tigreal"
            await message.channel.send("Dillon's hero #10 is now Tigreal! :moyai: ")
        if message.content == "!ml hero10 add Uranus":
            dihero10 = "Uranus"
            await message.channel.send("Dillon's hero #10 is now Uranus! :peach: ")
        if message.content == "!ml hero10 add X.Borg":
            dihero10 = "X.Borg"
            await message.channel.send("Dillon's hero #10 is now X.Borg! :fire: ")
        if message.content == "!ml hero10 add Aldous":
            dihero10 = "Aldous"
            await message.channel.send("Dillon's hero #10 is now Aldous! :fist: ")
        if message.content == "!ml hero10 add Alpha":
            dihero10 = "Alpha"
            await message.channel.send("Dillon's hero #10 is now Alpha! :airplane: ")
        if message.content == "!ml hero10 add Alucard":
            dihero10 = "Alucard"
            await message.channel.send("Dillon's hero #10 is now Alucard! :cartwheel: ")
        if message.content == "!ml hero10 add Argus":
            dihero10 = "Argus"
            await message.channel.send("Dillon's hero #10 is now Argus! :angel: ")
        if message.content == "!ml hero10 add Badang":
            dihero10 = "Badang"
            await message.channel.send("Dillon's hero #10 is now Badang! :right_facing_fist: ")
        if message.content == "!ml hero10 add Bane":
            dihero10 = "Bane"
            await message.channel.send("Dillon's hero #10 is now Bane! :octopus: ")
        if message.content == "!ml hero10 add Chou":
            dihero10 = "Chou"
            await message.channel.send("Dillon's hero #10 is now Chou! :dirtial_arts_uniform: ")
        if message.content == "!ml hero10 add Dyrroth":
            dihero10 = "Dyrroth"
            await message.channel.send("Dillon's hero #10 is now Dyrroth! :smiling_imp: ")
        if message.content == "!ml hero10 add Freya":
            dihero10 = "Freya"
            await message.channel.send("Dillon's hero #10 is now Freya! :hammer: ")
        if message.content == "!ml hero10 add Guinevere":
            dihero10 = "Guinevere"
            await message.channel.send("Dillon's hero #10 is now Guinevere! :dress:  ")
        if message.content == "!ml hero10 add Jawhead":
            dihero10 = "Jawhead"
            await message.channel.send("Dillon's hero #10 is now Jawhead! :robot: ")
        if message.content == "!ml hero10 add Kaja":
            dihero10 = "Kaja"
            await message.channel.send("Dillon's hero #10 is now Kaja! :bird: ")
        if message.content == "!ml hero10 add Lapu-Lapu":
            dihero10 = "Lapu-Lapu"
            await message.channel.send("Dillon's hero #10 is now Lapu-Lapu!:high_brightness: ")
        if message.content == "!ml hero10 add Leomord":
            dihero10 = "Leomord"
            await message.channel.send("Dillon's hero #10 is now Leomord! :horse_racing: ")
        if message.content == "!ml hero10 add Martis":
            dihero10 = "Martis"
            await message.channel.send("Dillon's hero #10 is now Martis! :crab: ")
        if message.content == "!ml hero10 add Minsitthar":
            dihero10 = "Minsitthar"
            await message.channel.send("Dillon's hero #10 is now Minsitthar! :star_of_david: ")
        if message.content == "!ml hero10 add Roger":
            dihero10 = "Roger"
            await message.channel.send("Dillon's hero #10 is now Roger! :wolf: ")
        if message.content == "!ml hero10 add Ruby":
            dihero10 = "Ruby"
            await message.channel.send("Dillon's hero #10 is now Ruby! :heart: ")
        if message.content == "!ml hero10 add Sun":
            dihero10 = "Sun"
            await message.channel.send("Dillon's hero #10 is now Sun! :monkey_face: ")
        if message.content == "!ml hero10 add Thamuz":
            dihero10 = "Thamuz"
            await message.channel.send("Dillon's hero #10 is now Thamuz! :rage: ")
        if message.content == "!ml hero10 add Terizla":
            dihero10 = "Terizla"
            await message.channel.send("Dillon's hero #10 is now Terizla! :hammer: ")
        if message.content == "!ml hero10 add Zilong":
            dihero10 = "Zilong"
            await message.channel.send("Dillon's hero #10 is now Zilong! :dragon: ")
        if message.content == "!ml hero10 add Fanny":
            dihero10 = "Fanny"
            await message.channel.send("Dillon's hero #10 is now Fanny! :crossed_swords: ")
        if message.content == "!ml hero10 add Gusion":
            dihero10 = "Gusion"
            await message.channel.send(
                "Dillon's hero #10 is now Gusion! :dagger: :dagger: :dagger: :dagger: :dagger:  ")
        if message.content == "!ml hero10 add Hanzo":
            dihero10 = "Hanzo"
            await message.channel.send("Dillon's hero #10 is now Hanzo! :ghost: ")
        if message.content == "!ml hero10 add Hayabusa":
            dihero10 = "Hayabusa"
            await message.channel.send("Dillon's hero #10 is now Hayabusa! :bust_in_silhouette:  ")
        if message.content == "!ml hero10 add Helcurt":
            dihero10 = "Helcurt"
            await message.channel.send("Dillon's hero #10 is now Helcurt! :mute:  ")
        if message.content == "!ml hero10 add Karina":
            dihero10 = "Karina"
            await message.channel.send("Dillon's hero #10 is now Karina! :purple_heart: ")
        if message.content == "!ml hero10 add Lancelot":
            dihero10 = "Lancelot"
            await message.channel.send("Dillon's hero #10 is now Lancelot! :fencer: ")
        if message.content == "!ml hero10 add Lesley":
            dihero10 = "Lesley"
            await message.channel.send("Dillon's hero #10 is now Lesley! :skull_crossbones: ")
        if message.content == "!ml hero10 add Natalia":
            dihero10 = "Natalia"
            await message.channel.send("Dillon's hero #10 is now Natalia! :spy::excladition: ")
        if message.content == "!ml hero10 add Saber":
            dihero10 = "Saber"
            await message.channel.send("Dillon's hero #10 is now Saber! :diamond_shape_with_a_dot_inside:  ")
        if message.content == "!ml hero10 add Selena":
            dihero10 = "Selena"
            await message.channel.send("Dillon's hero #10 is now Selena! :sleeping:  ")
        if message.content == "!ml hero10 add Alice":
            dihero10 = "Alice"
            await message.channel.send("Dillon's hero #10 is now Alice! :lips: :kiss: ")
        if message.content == "!ml hero10 add Aurora":
            dihero10 = "Aurora"
            await message.channel.send("Dillon's hero #10 is now Aurora! :snow: ")
        if message.content == "!ml hero1 add Chang'e":
            dihero10 = "Chang'e"
            await message.channel.send("Dillon's hero #10 is now Chang'e! :cloud_rain:  ")
        if message.content == "!ml hero10 add Cyclops":
            dihero10 = "Cyclops"
            await message.channel.send("Dillon's hero #10 is now Cyclops! :eye:  ")
        if message.content == "!ml hero10 add Eudora":
            dihero10 = "Eudora"
            await message.channel.send("Dillon's hero #10 is now Eudora! :zap: ")
        if message.content == "!ml hero10 add Faramis":
            dihero10 = "Faramis"
            await message.channel.send("Dillon's hero #10 is now Faramis! :arrows_counterclockwise: ")
        if message.content == "!ml hero10 add Gord":
            dihero10 = "Gord"
            await message.channel.send("Dillon's hero #10 is now Gord! :snowboarder:")
        if message.content == "!ml hero10 add Harith":
            dihero10 = "Harith"
            await message.channel.send("Dillon's hero #10 is now Harith! :older_din: ")
        if message.content == "!ml hero10 add Harley":
            dihero10 = "Harley"
            await message.channel.send("Dillon's hero #10 is now Harley! :tophat: ")
        if message.content == "!ml hero10 add Kadita":
            dihero10 = "Kadita"
            await message.channel.send("Dillon's hero #10 is now Kadita! :droplet: ")
        if message.content == "!ml hero10 add Kagura":
            dihero10 = "Kagura"
            await message.channel.send("Dillon's hero #10 is now Kagura! :umbrella10:  ")
        if message.content == "!ml hero10 add Lunox":
            dihero10 = "Lunox"
            await message.channel.send("Dillon's hero #10 is now Lunox! :yin_yang: ")
        if message.content == "!ml hero10 add Lylia":
            dihero10 = "Lylia"
            await message.channel.send("Dillon's hero #10 is now Lylia! :boom: ")
        if message.content == "!ml hero10 add Nana":
            dihero10 = "Nana"
            await message.channel.send("Dillon's hero #10 is now Nana! :cat:  ")
        if message.content == "!ml hero10 add Odette":
            dihero10 = "Odette"
            await message.channel.send("Dillon's hero #10 is now Odette! :duck: ")
        if message.content == "!ml hero10 add Pharsa":
            dihero10 = "Pharsa"
            await message.channel.send("Dillon's hero #10 is now Pharsa! :dove:  ")
        if message.content == "!ml hero10 add Vale":
            dihero10 = "Vale"
            await message.channel.send("Dillon's hero #10 is now Vale! :wind_blowing_face:  ")
        if message.content == "!ml hero10 add Valir":
            dihero10 = "Valir"
            await message.channel.send("Dillon's hero #10 is now Valir! :fire:")
        if message.content == "!ml hero10 add Vexanna":
            dihero10 = "Vexanna"
            await message.channel.send("Dillon's hero #10 is now Zhask! :orthodox_cross: ")
        if message.content == "!ml hero10 add Bruno":
            dihero10 = "Bruno"
            await message.channel.send("Dillon's hero #10 is now Bruno! :soccer:  ")
        if message.content == "!ml hero10 add Claude":
            dihero10 = "Claude"
            await message.channel.send("Dillon's hero #10 is now Claude! :monkey:  ")
        if message.content == "!ml hero10 add Clint":
            dihero10 = "Clint"
            await message.channel.send("Dillon's hero #10 is now Clint! :cowboy: ")
        if message.content == "!ml hero10 add Granger":
            dihero10 = "Granger"
            await message.channel.send("Dillon's hero #10 is now Granger! :violin: ")
        if message.content == "!ml hero10 add Hanabi":
            dihero10 = "Hanabi"
            await message.channel.send("Dillon's hero #10 is now Hanabi!:nut_and_bolt:  ")
        if message.content == "!ml hero10 add Irithel":
            dihero10 = "Irithel"
            await message.channel.send("Dillon's hero #10 is now Irithel! :wolf: :girl:  ")
        if message.content == "!ml hero10 add Karrie":
            dihero10 = "Karrie"
            await message.channel.send(
                "Dillon's hero #10 is now Karrie! :diamond_shape_with_a_dot_inside:  :cartwheel: :diamond_shape_with_a_dot_inside:   ")
        if message.content == "!ml hero10 add Kimmy":
            dihero10 = "Kimmy"
            await message.channel.send("Dillon's hero #10 is now Kimmy! :haircut:  ")
        if message.content == "!ml hero10 add Layla":
            dihero10 = "Layla"
            await message.channel.send("Dillon's hero #10 is now Layla! :haircut:  ")
        if message.content == "!ml hero10 add Miya":
            dihero10 = "Miya"
            await message.channel.send("Dillon's hero #10 is now Miya! :bow_and_arrow: ")
        if message.content == "!ml hero10 add Moskov":
            dihero10 = "Moskov"
            await message.channel.send("Dillon's hero #10 is now Moskov! :imp: ")
        if message.content == "!ml hero10 add Yi Sun-Shin":
            dihero10 = "Yi Sun-Shin"
            await message.channel.send("Dillon's hero #10 is now Yi Sun-Shin! :crossed_swords: :bow_and_arrow:  ")
        if message.content == "!ml hero10 add Angela":
            dihero10 = "Angela"
            await message.channel.send("Dillon's hero #10 is now Angela! :helmet_with_cross: ")
        if message.content == "!ml hero10 add Diggie":
            dihero10 = "Diggie"
            await message.channel.send("Dillon's hero #10 is now Diggie! :owl: ")
        if message.content == "!ml hero10 add Estes":
            dihero10 = "Estes"
            await message.channel.send("Dillon's hero #10 is now Estes! :ear:  ")
        if message.content == "!ml hero10 add Rafaela":
            dihero10 = "Rafaela"
            await message.channel.send("Dillon's hero #10 is now Rafaela! :angel: ")
        if message.content == "!ml hero10 add Rynn":
            dihero10 = "Rynn"
            await message.channel.send("Dillon's hero #10 is now Rynn! ")
        if message.content == "!ml hero1 clear":
            dihero1 = "Not Chosen"
            await message.channel.send("Dillon's hero #1 slot has been cleared!")
        if message.content == "!ml hero2 clear":
            dihero2 = "Not Chosen"
            await message.channel.send("Dillon's hero #2 slot has been cleared!")
        if message.content == "!ml hero3 clear":
            dihero3 = "Not Chosen"
            await message.channel.send("Dillon's hero #3 slot has been cleared!")
        if message.content == "!ml hero3 clear":
            dihero3 = "Not Chosen"
            await message.channel.send("Dillon's hero #3 slot has been cleared!")
        if message.content == "!ml hero4 clear":
            dihero4 = "Not Chosen"
            await message.channel.send("Dillon's hero #4 slot has been cleared!")
        if message.content == "!ml hero5 clear":
            dihero5 = "Not Chosen"
            await message.channel.send("Dillon's hero #5 slot has been cleared!")
        if message.content == "!ml hero6 clear":
            dihero6 = "Not Chosen"
            await message.channel.send("Dillon's hero #6 slot has been cleared!")
        if message.content == "!ml hero7 clear":
            dihero7 = "Not Chosen"
            await message.channel.send("Dillon's hero #7 slot has been cleared!")
        if message.content == "!ml hero8 clear":
            dihero8 = "Not Chosen"
            await message.channel.send("Dillon's hero #8 slot has been cleared!")
        if message.content == "!ml hero9 clear":
            dihero9 = "Not Chosen"
            await message.channel.send("Dillon's hero #9 slot has been cleared!")
        if message.content == "!ml hero10 clear":
            dihero10 = "Not Chosen"
            await message.channel.send("Dillon's hero #10 slot has been cleared!")
        if message.content == "!ml hlist Dillon":
            diembed = discord.Embed(title="Heroes Dillon Plays",
                                    description="Here are the top 10 heroes Dillon is willing to play in ranked")
            diembed.add_field(name="1", value=dihero1)
            diembed.add_field(name="2", value=dihero2)
            diembed.add_field(name="3", value=dihero3)
            diembed.add_field(name="4", value=dihero4)
            diembed.add_field(name="5", value=dihero5)
            diembed.add_field(name="6", value=dihero6)
            diembed.add_field(name="7", value=dihero7)
            diembed.add_field(name="8", value=dihero8)
            diembed.add_field(name="9", value=dihero9)
            diembed.add_field(name="10", value=dihero10)
            await message.channel.send(content=None, embed=diembed)
client.loop.create_task(update_stats())
client.run("NjAyNTY3NTgwMTAzOTk5NTE4.XTc5Qg.zOh86aWE41MkmbqmiEoS5ycVSNA")
