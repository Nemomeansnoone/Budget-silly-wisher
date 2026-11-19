import random
import time

sincelastfivestar = 0
sincelastfourstar = 0

fivestarchance: float = (.006)
fourstarchance: float = (.051)
crapchance: float = (.943)

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

def pull(fivestarlim, fourstarlim):
    global sincelastfivestar
    global sincelastfourstar
    global fivestarlist
    global fourstarlist
    limfour = fourstarlim
    limfive = fivestarlim
    star = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])
    if (star == "fivestar") or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        fifty = random.choice(["yes", "no"])
        if (fifty == "yes"):
            return limfive
        elif (fifty == "no"):
            choice = random.choice(fivestarlist)
            return choice
        else:
            print("scheise")
    elif (star == "fourstar") or (sincelastfourstar >= 9):
        sincelastfourstar = 0
        sincelastfivestar += 1
        fifty = random.choice(["yes", "no"])
        if (fifty == "yes"):
            choice = random.choice(limfour)
            return choice
        elif (fifty == "no"):
            choice = random.choice(fourstarlist)
            return choice
        else:
            print("scheise")
    else:
        sincelastfivestar += 1
        sincelastfourstar += 1
        choice = "crap"
        return choice
