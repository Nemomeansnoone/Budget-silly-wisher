import random
import time

sincelastfivestar = 0
sincelastfourstar = 0

fivestarchance: float = (.006)
fourstarchance: float = (.051)
crapchance: float = (.943)

fivestarimglist = {
    "Keqing": ("keqingimg.png"),
    "Mona": ("monaimg.png"),
    "Diluc": ("dilucimg.png"),
    "Qiqi": ("qiqiimg.png"),
    "Yumemizuki Mizuki": ("mizukiimg.png"),
    "Dehya": ("dehyaimg.png"),
    "Jean": ("jeanimg.png"),
    "Tighnari": ("tighnariimg.png"),
    "Venti": ("ventiimg.png"),
    "Klee": ("kleeimg.png"),
    "Tartaglia": ("tartagliaimg.png"),
    "Zhongli": ("zhongliimg.png"),
    "Albedo": ("albedoimg.png"),
    "Ganyu": ("ganyuimg.png"),
    "Xiao": ("xiaoimg.png"),
    "Hutao": ("hutaoimg.png"),
    "Eula": ("eulaimg.png"),
    "Kazuha": ("kazuhaimg.png"),
    "Ayaka": ("ayakaimg.png"),
    "Yoimiya": ("yoimiyaimg.png"),
    "Raiden Shogun": ("raidenimg.png"),
    "Kokomi": ("kokomiimg.png"),
    "Itto": ("ittoimg.png"),
    "Shenhe": ("shenheimg.png"),
    "Yae Miko": ("yaemikoimg.png"),
    "Ayato": ("ayatoimg.png"),
    "Yelan": ("yelanimg.png"),
    "Cyno": ("cynoimg.png"),
    "Nilou": ("nilouimg.png"),
    "Nahida": ("nahidaimg.png"),
    "Wanderer": ("wandererimg.png"),
    "Alhaitham": ("alhaithamimg.png"),
    "Baizhu": ("baizhuimg.png")
}

fourstarimglist = {
    "Aino": ("ainoimg.png"),
    "Aloysha": ("aloyshaimg.png"),
    "Amber": ("amberimg.png"),
    "Barbara": ("barbaraimg.png"),
    "Beidou": ("beidouimg.png"),
    "Bennett": ("bennetimg.png"),
    "Candace": ("candaceimg.png"),
    "Charlotte": ("charlotteimg.png"),
    "Chevreuse": ("chevreuseimg.png"),
    "Chongyun": ("chongyunimg.png"),
    "Collei": ("colleiimg.png"),
    "Dahlia": ("dahliaimg.png"),
    "Diona": ("dionaimg.png"),
    "Faruzan": ("faruzanimg.png"),
    "Fischl": ("fischlimg.png"),
    "Freminet": ("freminetimg.png"),
    "Gaming": ("gamingimg.png"),
    "Gorou": ("gorouimg.png"),
    "Iansan": ("iansanimg.png"),
    "Ifa": ("ifaimg.png"),
    "Illuga": ("illugaimg.png"),
    "Jahoda": ("jahodaimg.png"),
    "Kachina": ("kachinaimg.png"),
    "Kaeya": ("kaeyaimg.png"),
    "Kaveh": ("kavehimg.png"),
    "Kirara": ("kiraraimg.png"),
    "Kujou Sara": ("kujouimg.png"),
    "Kuki Shinobu": ("kukiimg.png"),
    "Lan Yan": ("lanyanimg.png"),
    "Layla": ("laylaimg.png"),
    "Lisa": ("lisaimg.png"),
    "Lynette": ("lynetteimg.png"),
    "Mika": ("mikaimg.png"),
    "Ningguang": ("ningguangimg.png"),
    "Noelle": ("noelleimg.png"),
    "Ororon": ("ororonimg.png"),
    "Prune": ("pruneimg.png"),
    "Razor": ("razorimg.png"),
    "Rosaria": ("rpsariaimg.png"),
    "Sayu": ("sayuimg.png"),
    "Sethos": ("sethosimg.png"),
    "Shikanoin Heizou": ("shikanoinimg.png"),
    "Sucrose": ("sucroseimg.png"),
    "Thoma": ("thomaimg.png"),
    "Xiangling": ("xianglingimg.png"),
    "Xingqiu": ("xingqiuimg.png"),
    "Xinyan": ("xinyanimg.png"),
    "Yanfei": ("yanfeiimg.png"),
    "Yaoyao": ("yaoyaoimg.png"),
    "Yun Jun": ("yunjunimg.png")
}

fivestarlist = (
    "Keqing",
    "Mona",
    "Diluc",
    "Qiqi",
    "Yumemizuki Mizuki",
    "Dehya",
    "Jean",
    "Tighnari"
)

fourstarlist = (
    "Aino", 
    "Aloysha", 
    "Amber", 
    "Barbara", 
    "Beidou", 
    "Bennett",
    "Candace",
    "Charlotte",
    "Chevreuse",
    "Chongyun",
    "Collei",
    "Dahlia",
    "Diona",
    "Faruzan",
    "Fischl",
    "Freminet",
    "Gaming",
    "Gorou",
    "Iansan",
    "Ifa",
    "Illuga",
    "Jahoda",
    "Kachina",
    "Kaeya",
    "Kaveh",
    "Kirara",
    "Kujou Sara",
    "Kuki Shinobu",
    "Lan Yan",
    "Layla",
    "Lisa",
    "Lynette",
    "Mika",
    "Ningguang",
    "Noelle",
    "Ororon",
    "Prune",
    "Razor",
    "Rosaria",
    "Sayu",
    "Sethos",
    "Shikanoin Heizou",
    "Sucrose",
    "Thoma",
    "Xiangling",
    "Xingqiu",
    "Xinyan",
    "Yanfei",
    "Yaoyao",
    "Yun Jun"
)

def pullstan():
    global sincelastfivestar
    global sincelastfourstar
    global fivestarlist
    global fivestarlist
    star = "".join(random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance]))
    if (star == "fivestar") or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        choice = random.choice(fivestarlist)
        return star, choice, fivestarimglist.get(str(choice))
    elif (star == "fourstar") or (sincelastfourstar >= 9):
        sincelastfivestar += 1
        sincelastfourstar = 0
        choice = random.choice(fourstarlist)
        return star, choice, fourstarimglist.get(str(choice))
    else: 
        sincelastfivestar += 1
        sincelastfourstar += 0
        choice = "crap"
        return star, choice, "crapimg.png"

def pulllim(fivestarlim, fourstarlim):
    global sincelastfivestar
    global sincelastfourstar
    global fivestarlist
    global fourstarlist
    limfour = fourstarlim
    limfive = fivestarlim
    star = "".join(random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance]))
    if (star == "fivestar") or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        fifty = random.choice(["yes", "no"])
        if (fifty == "yes"):
            return star, "".join(limfive), fivestarimglist.get(str("".join(limfive)))
        elif (fifty == "no"):
            choice = random.choice(fivestarlist)
            return star, choice, fivestarimglist.get(str(choice))
    elif (star == "fourstar") or (sincelastfourstar >= 9):
        sincelastfivestar += 1
        sincelastfourstar = 0
        fifty = random.choice(["yes", "no"])
        if (fifty == "yes"):
            choice = random.choice(limfour)
            return star, choice, fourstarimglist.get(str(choice))
        elif (fifty == "no"):
            choice = random.choice(fourstarlist)
            return star, choice, fourstarimglist.get(str(choice))
    else:
        sincelastfivestar += 1
        sincelastfourstar += 1
        choice = "crap"
        return star, choice, "crapimg.png"
