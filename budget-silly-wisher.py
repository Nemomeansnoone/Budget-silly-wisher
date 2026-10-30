from asyncio import wait
import random

user_input: str = ''
bannerver: str = 'standard'
banner_ver: str = 0
pulls: int = 69420
paidmos: int = 0
fivestarlim: dict[str] =['']
fourstarlim: dict[str] =['']
fivestarstan: dict[str] = ['Keqing', 'Dehya', 'Diluc', 'Qiqi', 'Jean', 'Tighnari', 'Mona', 'Yumemizuki Mizuki']
fourstarstan: dict[str] = ['Aino', 'Aloysha', 'Amber', 'Barbara', 'Beidou', 'Bennett', 'Candace', 'Charlotte', 'Chevreuse', 'Chongyun', 'Collei', 'Dahlia', 'Diona', 'Dori', 'Faruzan', 'Fischl', 'Freminet', 'Gaming', 'Gorou', 'Iansan', 'Ifa', 'Illuga', 'Jahoda', 'Kachina', 'Kaeya', 'Kaveh', 'Kirara', 'Kujou Sara', 'Kuki Shinobu', 'Lan Yan', 'Layla', 'Lisa', 'Lynette', 'Mika', 'Ningguang', 'Noelle', 'Ororon', 'Prune', 'Razor', 'Rosaria', 'Sayu', 'Sethos', 'Shikanoin Heizou', 'Sucrose', 'Thoma', 'Xiangling', 'Xingqiu', 'Xinyan', 'Yanfei', 'Yaoyao', 'Yun Jun']
crap: dict[str] = ['crap']
fivelim: dict[str] = ['fivestarstan', 'fivestarlim']
fourlim: dict[str] = ['fourstarstan', 'fourstarlim']
userinventory = set()
help: str = 'commands: wish10, wish1, inventory, pulls, getmorepulls, getmorepaidmos, seemywallet, changebanner, currentbanner, help, exit'
fivestarchance: float = (.006)
fourstarchance: float = (.051)
previousfivestarwasnotlim: bool = False
previousfourstarwasnotlim: bool = False
crapchance: float = (.943)
pull0 = set()
pull1 = set()
pull2 = set()
pull3 = set()
pull4 = set()
pull5 = set()
pull6 = set()
pull7 = set()
pull8 = set()
pull9 = set()
pull10 = set()
resultingresult = set()
resultingresultingresult = set()
sincelastfivestar: int = (0)
sincelastfourstar: int = (0)

def wishforacharacter1():
    global pull0
    global resultingresult
    global resultingresultingresult
    global sincelastfivestar
    global sincelastfourstar
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresultingresult = [random.choice(fivestarstan)]
        pull0.update(resultingresultingresult)
        return
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfourstar = 0
        sincelastfivestar += 1
        resultingresultingresult = [random.choice(fourstarstan)]
        pull0.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult = [random.choice(crap)]
        pull0.update(resultingresultingresult)

def wishforacharacter1new():
    global pull0
    global resultingresult
    global resultingresultingresult
    global sincelastfivestar
    global sincelastfourstar
    global fivelim
    global fourlim
    global previousfivestarwasnotlim
    global previousfourstarwasnotlim
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresult = [random.choice(fivelim)]
        if (resultingresult == ['fivestarlim']) or (previousfivestarwasnotlim == True):
            resultingresultingresult = [random.choice(fivestarlim)]
            previousfivestarwasnotlim = False
            pull0.update(resultingresultingresult)
        elif (resultingresult == ['fivestarstan']):
            previousfivestarwasnotlim = True
            resultingresultingresult = [random.choice(fivestarstan)]
            pull0.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfourstar = 0
        sincelastfivestar += 1
        resultingresult = [random.choice(fourlim)]
        if (resultingresult == ['fourstarlim']) or (previousfourstarwasnotlim == True):
            previousfourstarwasnotlim = False
            resultingresultingresult = [random.choice(fourstarlim)]
            pull0.update(resultingresultingresult)
        elif (resultingresult == ['fourstarstan']):
            previousfourstarwasnotlim = True
            resultingresultingresult = [random.choice(fourstarstan)]
            pull0.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult = [random.choice(crap)]
        pull0.update(resultingresultingresult)

def wishforacharacter10():
    global pull1
    global pull2
    global pull3
    global pull4
    global pull5
    global pull6
    global pull7
    global pull8
    global pull9
    global pull10
    global resultingresult
    global resultingresultingresult
    global sincelastfivestar
    global sincelastfourstar
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fivestarstan)]
        pull1.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfivestar += 1
        sincelastfourstar = 0
        resultingresult.clear
        resultingresultingresult = [random.choice(fourstarstan)]
        pull1.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(crap)]
        pull1.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fivestarstan)]
        pull2.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfivestar += 1
        sincelastfourstar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fourstarstan)]
        pull2.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(crap)]
        pull2.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fivestarstan)]
        pull3.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfivestar += 1
        sincelastfourstar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fourstarstan)]
        pull3.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(crap)]
        pull3.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fivestarstan)]
        pull4.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfivestar += 1
        sincelastfourstar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fourstarstan)]
        pull4.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(crap)]
        pull4.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fivestarstan)]
        pull5.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfivestar += 1
        sincelastfourstar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fourstarstan)]
        pull5.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(crap)]
        pull5.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fivestarstan)]
        pull6.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfivestar += 1
        sincelastfourstar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fourstarstan)]
        pull6.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(crap)]
        pull6.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fivestarstan)]
        pull7.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfivestar += 1
        sincelastfourstar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fourstarstan)]
        pull7.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(crap)]
        pull7.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fivestarstan)]
        pull8.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfivestar += 1
        sincelastfourstar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fourstarstan)]
        pull8.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(crap)]
        pull8.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fivestarstan)]
        pull9.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfivestar += 1
        sincelastfourstar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fourstarstan)]
        pull9.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(crap)]
        pull9.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fivestarstan)]
        pull10.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfivestar += 1
        sincelastfourstar = 0
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(fourstarstan)]
        pull10.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult.clear
        resultingresultingresult = [random.choice(crap)]
        pull10.update(resultingresultingresult)


def wishforacharacter10new():
    global pull1
    global pull2
    global pull3
    global pull4
    global pull5
    global pull6
    global pull7
    global pull8
    global pull9
    global pull10
    global fivelim
    global fourlim
    global resultingresult
    global resultingresultingresult
    global sincelastfivestar
    global sincelastfourstar
    global previousfivestarwasnotlim
    global previousfourstarwasnotlim
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresult = [random.choice(fivelim)]
        if (resultingresult == ['fivestarlim'] or (previousfivestarwasnotlim == True)):
            previousfivestarwasnotlim = False
            resultingresultingresult = [random.choice(fivestarlim)]
            pull1.update(resultingresultingresult)
        elif (resultingresult == ['fivestarstan']):
            previousfivestarwasnotlim = True
            resultingresultingresult = [random.choice(fivestarstan)]
            pull1.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfourstar = 0
        sincelastfivestar += 1
        resultingresult = [random.choice(fourlim)]
        if (resultingresult == ['fourstarlim']) or (previousfourstarwasnotlim == True):
            previousfourstarwasnotlim = False
            resultingresultingresult = [random.choice(fourstarlim)]
            pull1.update(resultingresultingresult)
        elif (resultingresult == ['fourstarstan']):
            previousfourstarwasnotlim = True
            resultingresultingresult = [random.choice(fourstarstan)]
            pull1.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult = [random.choice(crap)]
        pull1.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresult = [random.choice(fivelim)]
        if (resultingresult == ['fivestarlim']) or (previousfivestarwasnotlim == True):
            previousfivestarwasnotlim = False
            resultingresultingresult = [random.choice(fivestarlim)]
            pull2.update(resultingresultingresult)
        elif (resultingresult == ['fivestarstan']):
            previousfivestarwasnotlim = True
            resultingresultingresult = [random.choice(fivestarstan)]
            pull2.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfourstar = 0
        sincelastfivestar += 1
        resultingresult = [random.choice(fourlim)]
        if (resultingresult == ['fourstarlim']) or (previousfourstarwasnotlim == True):
            previousfourstarwasnotlim = False
            resultingresultingresult = [random.choice(fourstarlim)]
            pull2.update(resultingresultingresult)
        elif (resultingresult == ['fourstarstan']):
            previousfourstarwasnotlim = True
            resultingresultingresult = [random.choice(fourstarstan)]
            pull2.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult = [random.choice(crap)]
        pull2.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresult = [random.choice(fivelim)]
        if (resultingresult == ['fivestarlim']) or (previousfivestarwasnotlim == True):
            previousfivestarwasnotlim = False
            resultingresultingresult = [random.choice(fivestarlim)]
            pull3.update(resultingresultingresult)
        elif (resultingresult == ['fivestarstan']):
            previousfivestarwasnotlim = True
            resultingresultingresult = [random.choice(fivestarstan)]
            pull3.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfourstar = 0
        sincelastfivestar += 1
        resultingresult = [random.choice(fourlim)]
        if (resultingresult == ['fourstarlim']) or (previousfourstarwasnotlim == True):
            previousfourstarwasnotlim = False
            resultingresultingresult = [random.choice(fourstarlim)]
            pull3.update(resultingresultingresult)
        elif (resultingresult == ['fourstarstan']):
            previousfourstarwasnotlim = True
            resultingresultingresult = [random.choice(fourstarstan)]
            pull3.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult = [random.choice(crap)]
        pull3.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresult = [random.choice(fivelim)]
        if (resultingresult == ['fivestarlim']) or (previousfivestarwasnotlim == True):
            previousfivestarwasnotlim = False
            resultingresultingresult = [random.choice(fivestarlim)]
            pull4.update(resultingresultingresult)
        elif (resultingresult == ['fivestarstan']):
            previousfivestarwasnotlim = True
            resultingresultingresult = [random.choice(fivestarstan)]
            pull4.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfourstar = 0
        sincelastfivestar += 1
        resultingresult = [random.choice(fourlim)]
        if (resultingresult == ['fourstarlim']) or (previousfourstarwasnotlim == True):
            previousfourstarwasnotlim = False
            resultingresultingresult = [random.choice(fourstarlim)]
            pull4.update(resultingresultingresult)
        elif (resultingresult == ['fourstarstan']):
            previousfourstarwasnotlim = True
            resultingresultingresult = [random.choice(fourstarstan)]
            pull4.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult = [random.choice(crap)]
        pull4.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresult = [random.choice(fivelim)]
        if (resultingresult == ['fivestarlim']) or (previousfivestarwasnotlim == True):
            previousfivestarwasnotlim = False
            resultingresultingresult = [random.choice(fivestarlim)]
            pull5.update(resultingresultingresult)
        elif (resultingresult == ['fivestarstan']):
            previousfivestarwasnotlim = True
            resultingresultingresult = [random.choice(fivestarstan)]
            pull5.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfourstar = 0
        sincelastfivestar += 1
        resultingresult = [random.choice(fourlim)]
        if (resultingresult == ['fourstarlim']) or (previousfourstarwasnotlim == True):
            previousfourstarwasnotlim = False
            resultingresultingresult = [random.choice(fourstarlim)]
            pull5.update(resultingresultingresult)
        elif (resultingresult == ['fourstarstan']):
            previousfourstarwasnotlim = True
            resultingresultingresult = [random.choice(fourstarstan)]
            pull5.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult = [random.choice(crap)]
        pull5.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresult = [random.choice(fivelim)]
        if (resultingresult == ['fivestarlim']) or (previousfivestarwasnotlim == True):
            previousfivestarwasnotlim = False
            resultingresultingresult = [random.choice(fivestarlim)]
            pull6.update(resultingresultingresult)
        elif (resultingresult == ['fivestarstan']):
            previousfivestarwasnotlim = True
            resultingresultingresult = [random.choice(fivestarstan)]
            pull6.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfourstar = 0
        sincelastfivestar += 1
        resultingresult = [random.choice(fourlim)]
        if (resultingresult == ['fourstarlim']) or (previousfourstarwasnotlim == True):
            previousfourstarwasnotlim = False
            resultingresultingresult = [random.choice(fourstarlim)]
            pull6.update(resultingresultingresult)
        elif (resultingresult == ['fourstarstan']):
            previousfourstarwasnotlim = True
            resultingresultingresult = [random.choice(fourstarstan)]
            pull6.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult = [random.choice(crap)]
        pull6.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresult = [random.choice(fivelim)]
        if (resultingresult == ['fivestarlim']) or (previousfivestarwasnotlim == True):
            previousfivestarwasnotlim = False
            resultingresultingresult = [random.choice(fivestarlim)]
            pull7.update(resultingresultingresult)
        elif (resultingresult == ['fivestarstan']):
            previousfivestarwasnotlim = True
            resultingresultingresult = [random.choice(fivestarstan)]
            pull7.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfourstar = 0
        sincelastfivestar += 1
        resultingresult = [random.choice(fourlim)]
        if (resultingresult == ['fourstarlim']) or (previousfourstarwasnotlim == True):
            previousfourstarwasnotlim = False
            resultingresultingresult = [random.choice(fourstarlim)]
            pull7.update(resultingresultingresult)
        elif (resultingresult == ['fourstarstan']):
            previousfourstarwasnotlim = True
            resultingresultingresult = [random.choice(fourstarstan)]
            pull7.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult = [random.choice(crap)]
        pull7.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresult = [random.choice(fivelim)]
        if (resultingresult == ['fivestarlim']) or (previousfivestarwasnotlim == True):
            previousfivestarwasnotlim = False
            resultingresultingresult = [random.choice(fivestarlim)]
            pull8.update(resultingresultingresult)
        elif (resultingresult == ['fivestarstan']):
            previousfivestarwasnotlim = True
            resultingresultingresult = [random.choice(fivestarstan)]
            pull8.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfourstar = 0
        sincelastfivestar += 1
        resultingresult = [random.choice(fourlim)]
        if (resultingresult == ['fourstarlim']) or (previousfourstarwasnotlim == True):
            previousfourstarwasnotlim = False
            resultingresultingresult = [random.choice(fourstarlim)]
            pull8.update(resultingresultingresult)
        elif (resultingresult == ['fourstarstan']):
            previousfourstarwasnotlim = True
            resultingresultingresult = [random.choice(fourstarstan)]
            pull8.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult = [random.choice(crap)]
        pull8.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresult = [random.choice(fivelim)]
        if (resultingresult == ['fivestarlim']) or (previousfivestarwasnotlim == True):
            previousfivestarwasnotlim = False
            resultingresultingresult = [random.choice(fivestarlim)]
            pull9.update(resultingresultingresult)
        elif (resultingresult == ['fivestarstan']):
            previousfivestarwasnotlim = True
            resultingresultingresult = [random.choice(fivestarstan)]
            pull9.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfourstar = 0
        sincelastfivestar += 1
        resultingresult = [random.choice(fourlim)]
        if (resultingresult == ['fourstarlim']) or (previousfourstarwasnotlim == True):
            previousfourstarwasnotlim = False
            resultingresultingresult = [random.choice(fourstarlim)]
            pull9.update(resultingresultingresult)
        elif (resultingresult == ['fourstarstan']):
            previousfourstarwasnotlim = True
            resultingresultingresult = [random.choice(fourstarstan)]
            pull9.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult = [random.choice(crap)]
        pull9.update(resultingresultingresult)
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresult = [random.choice(fivelim)]
        if (resultingresult == ['fivestarlim']) or (previousfivestarwasnotlim == True):
            previousfivestarwasnotlim = False
            resultingresultingresult = [random.choice(fivestarlim)]
            pull10.update(resultingresultingresult)
        elif (resultingresult == ['fivestarstan']):
            previousfivestarwasnotlim = True
            resultingresultingresult = [random.choice(fivestarstan)]
            pull10.update(resultingresultingresult)
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfourstar = 0
        sincelastfivestar += 1
        resultingresult = [random.choice(fourlim)]
        if (resultingresult == ['fourstarlim']) or (previousfourstarwasnotlim == True):
            previousfourstarwasnotlim = False
            resultingresultingresult = [random.choice(fourstarlim)]
            pull10.update(resultingresultingresult)
        elif (resultingresult == ['fourstarstan']):
            previousfourstarwasnotlim = True
            resultingresultingresult = [random.choice(fourstarstan)]
            pull10.update(resultingresultingresult)
    elif (result == 'crap'):
        sincelastfivestar += 1
        sincelastfourstar += 1
        resultingresultingresult = [random.choice(crap)]
        pull10.update(resultingresultingresult)
        

##start of silly wisher
print('welcome to budget silly wisher v1.0')
print('information accurate as of genshin version 7.1')
print('oh also no weapons cuz i ran out of budget for this')
print('type "help" for a list of commands or "wish10" or "wish1" to start pulling')
print(f'you have {pulls} pulls left')
print(f'current banner: {bannerver}')

def clearpulltable():
    global pull1
    global pull2
    global pull3
    global pull4
    global pull5
    global pull6
    global pull7
    global pull8
    global pull9
    global pull10
    pull1 = set()
    pull2 = set()
    pull3 = set()
    pull4 = set()
    pull5 = set()
    pull6 = set()
    pull7 = set()
    pull8 = set()
    pull9 = set()
    pull10 = set()

def wish10():
    global pulls
    if (pulls >= 10):
        if (banner_ver == 0):
            pulls -= 10
            print ('pulling...')
            wishforacharacter10()
            wait (2)
            print (f'you pulled {pull1}, {pull2}, {pull3}, {pull4}, {pull5}, {pull6}, {pull7}, {pull8}, {pull9}, and {pull10}')
            userinventory.update(pull1)
            userinventory.update(pull2)
            userinventory.update(pull3)
            userinventory.update(pull4)
            userinventory.update(pull5)
            userinventory.update(pull6)
            userinventory.update(pull7)
            userinventory.update(pull8)
            userinventory.update(pull9)
            userinventory.update(pull10)
            clearpulltable()
            print ('' + str(pulls) + ' pulls left')
        elif (banner_ver != 0):
            pulls -= 10
            print ('pulling...')
            wishforacharacter10new()
            wait (2)
            print (f'you pulled {pull1}, {pull2}, {pull3}, {pull4}, {pull5}, {pull6}, {pull7}, {pull8}, {pull9}, and {pull10}')
            userinventory.update(pull1)
            userinventory.update(pull2)
            userinventory.update(pull3)
            userinventory.update(pull4)
            userinventory.update(pull5)
            userinventory.update(pull6)
            userinventory.update(pull7)
            userinventory.update(pull8)
            userinventory.update(pull9)
            userinventory.update(pull10)
            clearpulltable()
            print ('' + str(pulls) + ' pulls left')
        return
    elif (pulls < 10):
        print ('out of pulls you br0kie, go away')
        return
    return

def wish1():
    global pulls
    if (pulls < 1):
        print ('out of pulls you br0kie, go away')
        return
    elif (pulls >= 1):
        if (banner_ver == 0):
            pulls  -= 1
            print ('pulling...')
            wishforacharacter1()
            wait (2)
            print (f'you pulled {pull0}')
            userinventory.update(pull0)
            wait (0.2)
            pull0.clear()
            resultingresultingresult.clear()
            print ('' + str(pulls) + ' pulls left')
        elif (banner_ver != 0):
            pulls  -= 1
            print ('pulling...')
            wishforacharacter1new()
            wait (2)
            print (f'you pulled {pull0}')
            userinventory.update(pull0)
            wait (0.2)
            pull0.clear()
            resultingresultingresult.clear()
            print ('' + str(pulls) + ' pulls left')
        return
    return

def inventory():
    print (f'{userinventory}')
    return

def pull():
    global pulls
    print (f'you have {pulls} pull(s) left, use "getmorepulls" for more pulls')
    return

def wait(seconds: int):
    import time
    time.sleep(seconds)
    return

def getmorepaidmos():
    global paidmos
    print (f'please choose a payment method (type "b" for bank account and "c" for credit/debit card)')
    try:
        paymentinfo: str = str(input())
        if (paymentinfo == ('b')):
            print (f'please enter your bank account number (dont)')
            bankaccount: str = input()
            print (f'using bank account with number "{bankaccount}"...')
        elif (paymentinfo == ('c')):
            print (f'please enter your credit/debit card details (dont)')
            creditcard: str = input()
            print (f'using credit/debit card with number "{creditcard}"...')
    except ValueError:
        print (f'please choose a payment method')
    print ('how many paidmos would you like?')
    try:
        more_paidmos: int = int(input())
        paidmos += more_paidmos
        print (f'deducting $' + str(more_paidmos * 2) + '...')
        wait (3)
        print (f'you have been given {more_paidmos} more paidmos! thanks for the free moneh :)')
    except ValueError:
        print (f'please enter a valid number')

def getmorepulls():
    global pulls
    global paidmos
    print (f'how many pulls would you like? (one pull costs 160 paidmos)')
    try:
        more_pulls: int = int(input())
        if paidmos >= (160 * more_pulls):
            paidmos -= (160 * more_pulls)
            pulls += (more_pulls)
            print (f'processing...')
            wait (1)
            print (f'{more_pulls} has been added to your balance')
        elif paidmos <= (160 * more_pulls):
            print (f'you dont have enough paidmos, go away!')
        else:
            print (f'please enter a valid amount!')
    except ValueError:
        print (f'please enter a valid amount!')

def changebanner():
    global fivestarlim
    global fourstarlim
    global bannerver
    global banner_ver
    print (f'please enter the banner in the following format: <version (without decimal)><banner phase><banner number (if applicable)>')
    print (f'e.g. "6021" for version 6.0 phase 2 (yelan) banner, type 0 for standard banner')
    try:
        bannerinput: int = int(input())
        if (bannerinput == 0):
            banner_ver = bannerinput
            fivestarlim = ([''])
            fourstarlim = ([''])
            bannerver = str('standard')
        elif (bannerinput == 101):
            fivestarlim = (['Venti'])
            fourstarlim = (['Barbara', 'Fischl', 'Xiangling'])
            banner_ver = bannerinput
            bannerver = str('1.0 phase 1 (venti)')
        elif (bannerinput == 102):
            fivestarlim = (['Klee'])
            fourstarlim = (['Noelle', 'Sucrose', 'Xingqiu'])
            banner_ver = bannerinput
            bannerver = str('1.0 phase 2 (klee)')
        elif (bannerinput == 111):
            fivestarlim = (['tartaglia'])
            fourstarlim = (['Beidou', 'Ningguang', 'Diona'])
            banner_ver = bannerinput
            bannerver = str('1.1 phase 1 (tartaglia)')
        elif (bannerinput == 112):
            fivestarlim = (['Zhongli'])
            fourstarlim = (['Razor', 'Chongyun', 'Xinyan'])
            banner_ver = bannerinput
            bannerver = str('1.1 phase 2 (zhongli)')
        elif (bannerinput == 121):
            fivestarlim = (['Albedo'])
            fourstarlim = (['Bennett', 'Fischl', 'Sucrose'])
            banner_ver = bannerinput
            bannerver = str('1.2 phase 1 (albedo)')
        elif (bannerinput == 122):
            fivestarlim = (['Ganyu'])
            fourstarlim = (['Noelle', 'Xiangling', 'Xingqiu'])
            banner_ver = bannerinput
            bannerver = str ('1.2 phase 2 (ganyu)')
        elif (bannerinput == 131):
            fivestarlim = (['Xiao'])
            fourstarlim = (['Beidou', 'Diona', 'Xinyan'])
            banner_ver = bannerinput
            bannerver = str('1.3 phase 1 (xiao)')
        elif (bannerinput == 132):
            fivestarlim = (['Keqing'])
            fourstarlim = (['Barbara', 'Bennett', 'Ningguang'])
            banner_ver = bannerinput
            bannerver = str('1.3 phase 2 (keqing)')
        elif (bannerinput == 133):
            fivestarlim = (['Hutao'])
            fourstarlim = (['Xiangling', 'Xingqiu', 'Chongyun'])
            banner_ver = bannerinput
            bannerver = str('1.3 phase 3 (hutao)')
        elif (bannerinput == 141):
            fivestarlim = (['Venti'])
            fourstarlim = (['Razor', 'Noelle', 'Sucrose'])
            banner_ver = bannerinput
            bannerver = str('1.4 phase 1 (venti)')
        elif (bannerinput == 142):
            fivestarlim = (['Tartaglia'])
            fourstarlim = (['Barbara', 'Fischl', 'Rosaria'])
            banner_ver = bannerinput
            bannerver = str('1.4 phase 2 (tartaglia)')
        elif (bannerinput == 151):
            fivestarlim = (['Zhongli'])
            fourstarlim = (['Noelle', 'Diona', 'Yanfei'])
            banner_ver = bannerinput
            bannerver = str('1.5 phase 1 (zhongli)')
        elif (bannerinput == 152):
            fivestarlim = (['Eula'])
            fourstarlim = (['Beidou', 'Xingqiu', 'Xinyan'])
            banner_ver = bannerinput
            bannerver = str('1.5 phase 2 (eula)')
        elif (bannerinput == 161):
            fivestarlim = (['Klee'])
            fourstarlim = (['Barbara', 'Fischl', 'Sucrose'])
            banner_ver = bannerinput
            bannerver = str('1.6 phase 1 (klee)')
        elif (bannerinput == 162):
            fivestarlim = (['Kazuha'])
            fourstarlim = (['Razor', 'Bennett', 'Rosaria'])
            banner_ver = bannerinput
            banner_ver = str('1.6 phase 2 (kazuha)')
        elif (bannerinput == 201):
            fivestarlim = (['Ayaka'])
            fourstarlim = (['Ningguang', 'Chongyun', 'Yanfei'])
            banner_ver = bannerinput
            bannerver = str('2.0 phase 1 (ayaka)')
        elif (bannerinput == 202):
            fivestarlim = (['Yoimiya'])
            fourstarlim = (['Diona', 'Xinyan', 'Sayu'])
            banner_ver = bannerinput
            bannerver = str('2.0 phase 2 (yoimiya)')
        elif (bannerinput == 211):
            fivestarlim = (['Raiden Shogun'])
            fourstarlim = (['Sucrose', ' Xiangling', 'Kujou Sara'])
            banner_ver = bannerinput
            bannerver = str('2.1 phase 1 (raiden shogun)')
        elif (bannerinput == 212):
            fivestarlim = (['Kokomi'])
            fourstarlim = (['Beidou', 'Xingqiu', 'Rosaria'])
            banner_ver = bannerinput
            bannerver = str('2.1 phase 2 (kokomi)')
        elif (bannerinput == 221):
            fivestarlim = (['Tartaglia'])
            fourstarlim = (['Ningguang', 'Chongyun', 'Yanfei'])
            banner_ver = bannerinput
            bannerver = str('2.2 phase 1 (tartaglia)')
        elif (bannerinput == 222):
            fivestarlim = (['Hutao'])
            fourstarlim = (['Diona', 'Sayu', 'Thoma'])
            banner_ver = bannerinput
            bannerver = str('2.2 phase 2 (hutao)')
        elif (bannerinput == 2311):
            fivestarlim = (['Eula'])
            fourstarlim = (['Bennett', 'Noelle', 'Rosaria'])
            banner_ver = bannerinput
            bannerver = str('2.3 phase 1 (eula)')
        elif (bannerinput == 2312):
            fivestarlim = (['Albedo'])
            fourstarlim = (['Bennett', 'Noelle', 'Rosaria'])
            banner_ver = bannerinput
            bannerver = str('2.3 phase 1 (albedo)')
        elif (bannerinput == 232):
            fivestarlim = (['Itto'])
            fourstarlim = (['Barbara', 'Xiangling', 'Gorou'])
            banner_ver = bannerinput
            bannerver = str('2.3 phase 2 (itto)')
        elif (bannerinput == 2411):
            fivestarlim = (['Xiao'])
            fourstarlim = (['Ningguang', 'Chongyun', 'Yun Jun'])
            banner_ver = bannerinput
            bannerver = str('2.4 phase 1 (xiao)')
        elif (bannerinput == 2412):
            fivestarlim = (['Shenhe'])
            fourstarlim = (['Ningguang', 'Chongyun', 'Yun Jun'])
            banner_ver = bannerinput
            bannerver = str('2.4 phase 2 (shenhe)')
        elif (bannerinput == 2421):
            fivestarlim = (['Ganyu'])
            fourstarlim = (['Beidou', 'Xingqiu', 'Yanfei'])
            banner_ver = bannerinput
            bannerver = str('2.4 phase 2 (ganyu)')
        elif (bannerinput == 2422):
            fivestarlim = (['Zhongli'])
            fourstarlim = (['Beidou', 'Xingqiu', 'Yanfei'])
            banner_ver = bannerinput
            bannerver = str('2.4 phase 2 (zhongli)')
        elif (bannerinput == 251):
            fivestarlim = (['Yae Miko'])
            fourstarlim = (['Fischl', 'Diona', 'Thoma'])
            banner_ver = bannerinput
            bannerver = str('2.5 phase 1 (yae miko)')
        elif (bannerinput == 2521):
            fivestarlim = (['Kokomi'])
            fourstarlim = (['Bennett', 'Xinyan', 'Kujou Sara'])
            banner_ver = bannerinput
            bannerver = str('2.5 phase 2 (kokomi)')
        elif (bannerinput == 2522):
            fivestarlim = (['Raiden Shogun'])
            fourstarlim = (['Bennett', 'Xinyan', 'Kujou Sara'])
            banner_ver = bannerinput
            bannerver = str('2.5 phase 2 (raiden shogun)')
        elif (bannerinput == 2611):
            fivestarlim = (['Ayato'])
            fourstarlim = (['Sucrose', 'Xiangling', 'Yun Jun'])
            banner_ver = bannerinput
            bannerver = str('2.6 phase 1 (ayato)')
        elif (bannerinput == 2612):
            fivestarlim = (['Venti'])
            fourstarlim = (['Sucrose', 'Xiangling', 'Yun Jun'])
            banner_ver = bannerinput
            bannerver = str('2.6 phase 1 (venti)')
        elif (bannerinput == 262):
            fivestarlim = (['Ayaka'])
            fourstarlim = (['Razor', 'Rosaria', 'Sayu'])
            banner_ver = bannerinput
            bannerver == str('2.6 phase 2 (ayaka)')
        elif (bannerinput == 2711):
            fivestarlim = (['Yelan'])
            fourstarlim = (['Barbara', 'Noelle', 'Yanfei'])
            banner_ver = bannerinput
            bannerver = str('2.7 phase 1 (yelan)')
        elif (bannerinput == 2712):
            fivestarlim = (['Xiao'])
            fourstarlim = (['Barbara', 'Noelle', 'Yanfei'])
            banner_ver = bannerinput
            bannerver = str('2.7 phase 1 (xiao)')
        elif (bannerinput == 272):
            fivestarlim = (['Itto'])
            fourstarlim = (['Chongyun', 'Gorou', 'Kuki Shinobu'])
            banner_ver = bannerinput
            bannerver = str('2.7 phase 2 (itto)')
        elif (bannerinput == 2811):
            fivestarlim = (['Kazuha'])
            fourstarlim = (['Ningguang', 'Thoma', 'Shikanoin Heizou'])
            banner_ver = bannerinput
            bannerver = str('2.8 phase 1 (kazuha)')
        elif (bannerinput == 2812):
            fivestarlim = (['Klee'])
            fourstarlim = (['Ningguang', 'Thoma', 'Shikanoin Heizou'])
            banner_ver = bannerinput
            bannerver = str('2.8 phase 1 (klee)')
        elif (bannerinput == 282):
            fivestarlim = (['Yoimiya'])
            fourstarlim = (['Bennett', 'Xinyan', 'Yun Jun'])
            banner_ver = bannerinput
            bannerver = str('2.8 phase 1')
        elif (bannerinput == 3011):
            fivestarlim = (['Zhongli'])
            fourstarlim = (['Fischl', 'Diona', 'Collei'])
            banner_ver = bannerinput
            bannerver = str('3.0 phase 1 (zhongli)')
        elif (bannerinput == 3012):
            fivestarlim = (['Tighnari'])
            fourstarlim = (['Fischl', 'Diona', 'Collei'])
            banner_ver = bannerinput
            bannerver = str('3.0 phase 1 (tighnari)')
        elif (bannerinput == 3021):
            fivestarlim = (['Kokomi'])
            fourstarlim = (['Sucrose', 'Xingqiu', 'Dori'])
            banner_ver = bannerinput
            bannerver = str('3.0 phase 2 (kokomi)')
        elif (bannerinput == 3022):
            fivestarlim = (['Ganyu'])
            fourstarlim = (['Sucrose', 'Xingqiu', 'Dori'])
            banner_ver = bannerinput
            bannerver = str('3.0 Phase 2 (ganyu)')
        elif (bannerinput == 3111):
            fivestarlim = (['Venti'])
            fourstarlim = (['Sayu', 'Kuki Shinobu', 'Candace'])
            banner_ver = bannerinput
            bannerver = str('3.1 phase 1 (venti)')
        elif (bannerinput == 3112):
            fivestarlim = (['Cyno'])
            fourstarlim = (['Sayu', 'Kuki Shinobu' 'Candace'])
            banner_ver = bannerinput
            bannerver = str('3.1 phase 1 (cyno)')
        elif (bannerinput == 3121):
            fivestarlim = (['Albedo'])
            fourstarlim = (['Barbara', 'Beidou', 'Xiangling'])
            banner_ver = bannerinput
            bannerver = str('3.1 phase 2 (albedo)')
        elif (bannerinput == 3122):
            fivestarlim = (['Nilou'])
            fourstarlim = (['Barbara', 'Beidou', 'Xiangling'])
            banner_ver = bannerinput
            bannerver = str('3.1 phase 2 (nilou)')
        elif (bannerinput == 3211):
            fivestarlim = (['Nahida'])
            fourstarlim = (['Razor', 'Bennett', 'Noelle'])
            banner_ver = bannerinput
            bannerver = str('3.2 phase 1 (nahida)')
        elif (bannerinput == 3212):
            fivestarlim = (['Yoimiya'])
            fourstarlim = (['Razor', 'Bennett', 'Noelle'])
            banner_ver = bannerinput
            bannerver = str('3.2 phase 1 (yoimiya)')
        elif (bannerinput == 3221):
            fivestarlim = (['Tartaglia'])
            fourstarlim = (['Thoma', 'Shikanoin Heizou', 'Layla'])
            banner_ver = bannerinput
            bannerver = str('3.2 phase 2 (tartaglia)')
        elif (bannerinput == 3222):
            fivestarlim = (['Yae Miko'])
            fourstarlim = (['Thoma', 'Shikanoin Heizou', 'Layla'])
            banner_ver = bannerinput
            bannerver = str('3.2 phase 2 (yae miko)')
        elif (bannerinput == 3311):
            fivestarlim = (['Itto'])
            fourstarlim = (['Yanfei', 'Gorou', 'Faruzan'])
            banner_ver = bannerinput
            bannerver = str('3.3 phase 1 (itto)')
        elif (bannerinput == 3312):
            fivestarlim = (['Wanderer'])
            fourstarlim = (['Yanfei', 'Gorou', 'Faruzan'])
            banner_ver = bannerinput
            bannerver = str('3.3 phase 1 (wanderer)')
        elif (bannerinput == 3321):
            fivestarlim = (['Raiden Shogun'])
            fourstarlim = (['Rosaria', 'Sayu', 'Kujou Sara'])
            banner_ver = bannerinput
            bannerver = str('3.3 phase 2 (raiden shogun)')
        elif (bannerinput == 3322):
            fivestarlim = (['Ayato'])
            fourstarlim = (['Rosaria', 'Sayu' 'Kujou Sara'])
            banner_ver = bannerinput
            bannerver = str('3.3 phase 2 (ayato)')
        elif (bannerinput == 3411):
            fivestarlim = (['Yelan'])
            fourstarlim = (['Beidou', 'Ningguang', 'Xingqiu'])
            banner_ver = bannerinput
            bannerver = str('3.4 phase 1 (yelan)')
        elif (bannerinput == 3412):
            fivestarlim = (['Hutao'])
            fourstarlim = (['Beidou', 'Ningguang', 'Xingqiu'])
            banner_ver = bannerinput
            bannerver = str('3.4 phase 1 (hutao)')
        elif (bannerinput == 3421):
            fivestarlim = (['Xiao'])
            fourstarlim = (['Barbara', 'Bennett', 'Collei'])
            banner_ver = bannerinput
            bannerver = str('3.4 phase 2 (xiao)')
        elif (bannerinput == 3422):
            fivestarlim = (['Alhaitham'])
            fourstarlim = (['Barbara', 'Bennett', 'Collei'])
            banner_ver = bannerinput
            bannerver = str('3.4 phase 2 (alhaitham)')
        elif (bannerinput == 3511):
            fivestarlim = (['Ayaka'])
            fourstarlim = (['Sucrose', 'Diona', 'Mika'])
            banner_ver = bannerinput
            bannerver = str('3.5 phase 1 (ayaka)')
        elif (bannerinput == 3512):
            fivestarlim = (['Shenhe'])
            fourstarlim = (['Sucrose', 'Diona', 'Mika'])
            banner_ver = bannerinput
            bannerver = str('3.5 phase 1 (shenhe)')
        elif (bannerinput == 3521):
            fivestarlim = (['Cyno'])
            fourstarlim = (['Barbara', 'Bennett', 'Collei'])
            banner_ver = bannerinput
            bannerver = str('3.5 phase 2 (cyno)')
        elif (bannerinput == 3522):
            fivestarlim = (['Dehya'])
            fourstarlim = (['Barbara', 'Bennett', 'Collei'])
            banner_ver = bannerinput
            bannerver = str('3.5 phase 2 (dehya)')
        elif (bannerinput == 3611):
            fivestarlim = (['Ganyu'])
            fourstarlim = (['Fischl', 'Candace', 'Kaveh'])
            banner_ver = bannerinput
            bannerver = str('3.6 phase 1 (ganyu)')
        elif (bannerinput == 3612):
            fivestarlim = (['Baizhu'])
            fourstarlim = (['Fischl', 'Candace', 'Kaveh'])
            banner_ver = bannerinput
            bannerver = str('3.6 phase 1 (baizhu)')
        elif (bannerinput == 3621):
            fivestarlim = (['Nilou'])
            fourstarlim = (['Kuki Shinobu', 'Dori', 'Layla'])
            banner_ver = bannerinput
            bannerver = str('3.6 phase 2 (nilou)')
        elif (bannerinput == 3622):
            fivestarlim = (['Nahida'])
            fourstarlim = (['Kuki Shinobu', 'Dori', 'Layla'])
            banner_ver = bannerinput
            bannerver = str('3.6 phase 2 (nahida)')
        elif (bannerinput == 3711):
            fivestarlim = (['Alhaitham'])
            fourstarlim = (['Xiangling', 'Shikanoin Heizou', 'Yaoyao'])
            banner_ver = bannerinput
            bannerver = str('3.7 phase 1 (alhaitham)')
        elif (bannerinput == 3712):
            fivestarlim = (['Kazuha'])
            fourstarlim = (['Xiangling', 'Shikanoin Heizou', 'Yaoyao'])
            banner_ver = bannerinput
            bannerver = str('3.7 phase 1 (kazuha)')
        elif (bannerinput == 3721):
            fivestarlim = (['Yae Miko'])
            fourstarlim = (['Chongyun', 'Yun Jun', 'Kirara'])
            banner_ver = bannerinput
            bannerver = str('3.7 phase 2 (yae miko)')
        elif (bannerinput == 3722):
            fivestarlim = (['Yoimiya'])
            fourstarlim = (['Chongyun', 'Yun Jun', 'Kirara'])
            banner_ver = bannerinput
            bannerver = str('3.7 phase 2 (yoimiya)')
        elif (bannerinput == 3811):
            fivestarlim = (['Klee'])
            fourstarlim = (['Razor', 'Thoma', 'Mika'])
            banner_ver = bannerinput
            bannerver = str('3.8 phase 1 (klee)')
        elif (bannerinput == 3812):
            fivestarlim = (['Eula'])
            fourstarlim = (['Razor', 'Thoma', 'Mika'])
            banner_ver = bannerinput
            bannerver = str('3.8 phase 1 (eula)')
        elif (bannerinput == 3821):
            fivestarlim = (['Wanderer'])
            fourstarlim = (['Rosaria', 'Yanfei', 'Faruzan'])
            banner_ver = bannerinput
            bannerver = str('3.8 phase 2 (wanderer)')
        elif (bannerinput == 3822):
            fivestarlim = (['Kokomi'])
            fourstarlim = (['Rosaria', 'Yanfei', 'Faruzan'])
            banner_ver = bannerinput
            bannerver = str('3.8 phase 2 (kokomi)')
        elif (bannerinput == 4011):
            fivestarlim = (['Yelan'])
            fourstarlim = (['Barbara', 'Bennett', 'Lynette'])
            banner_ver = bannerinput
            bannerver = str('4.0 phase 1 (yelan)')
        elif (bannerinput == 4012):
            fivestarlim = (['Lyney'])
            fourstarlim = (['Barbara', 'Bennett', 'Lynette'])
            banner_ver = bannerinput
            bannerver = str('4.0 phase 1 (lyney)')
        elif (bannerinput == 4021):
            fivestarlim = (['Tartaglia'])
            fourstarlim = (['Noelle', 'Sayu', 'Freminet'])
            banner_ver = bannerinput
            bannerver = str('4.0 phase 2 (tartaglia)')
        elif (bannerinput == 4022):
            fivestarlim = (['Zhongli'])
            fourstarlim = (['Noelle', 'Sayu', 'Freminet'])
            banner_ver = bannerinput
            bannerver = str('4.0 phase 2 (zhongli)')
        elif (bannerinput == 4111):
            fivestarlim = (['Hutao'])
            fourstarlim = (['Fischl', 'Xingqiu', 'Diona'])
            banner_ver = bannerinput
            bannerver = str('4.1 phase 1 (hutao)')
        elif (bannerinput == 4112):
            fivestarlim = (['Neuvillette'])
            fourstarlim = (['Fischl', 'Xingqiu', 'Diona'])
            banner_ver = bannerinput
            bannerver = str('4.1 phase 1 (neuvillette)')
        elif (bannerinput == 4121):
            fivestarlim = (['Venti'])
            fourstarlim = (['Chongyun', 'Thoma', 'Dori'])
            banner_ver = bannerinput
            bannerver = str('4.1 phase 2 (venti)')
        elif (bannerinput ==4122):
            fivestarlim = (['Wriothesley'])
            fourstarlim = (['Chongyun', 'Thoma', 'Dori'])
            banner_ver = bannerinput
            bannerver = str('4.1 phase 2 (wriothesley)')
        elif (bannerinput == 4211):
            fivestarlim = (['Baizhu'])
            fourstarlim = (['Beidou', 'Collei', 'Charlotte'])
            banner_ver = bannerinput
            bannerver = str('4.2 phase 1 (baizhu)')
        elif (bannerinput == 4212):
            fivestarlim = (['Furina'])
            fourstarlim = (['Beidou', 'Collei', 'Charlotte'])
            banner_ver = bannerinput
            bannerver = str('4.2 phase 1 (furina)')
        elif (bannerinput == 4221):
            fivestarlim = (['Ayato'])
            fourstarlim = (['Xiangling', 'Kuki Shinobu', 'Kirara'])
            banner_ver = bannerinput
            bannerver = str('4.2 phase 2 (ayato)')
        elif (bannerinput == 4222):
            fivestarlim = (['Cyno'])
            fourstarlim = (['Xiangling', 'Kuki Shinobu', 'Kirara'])
            banner_ver = bannerinput
            bannerver = str('4.2 phase 2 (cyno)')
        elif (bannerinput == 4311):
            fivestarlim = (['Ayaka'])
            fourstarlim = (['Surcrose', 'Rosaria', 'Candace'])
            banner_ver = bannerinput
            bannerver = str('4.3 phase 1 (ayaka)')
        elif (bannerinput == 4312):
            fivestarlim = (['Navia'])
            fourstarlim = (['Sucrose', 'Rosaria', 'Candace'])
            banner_ver = bannerinput
            bannerver = str('4.3 phase 1 (navia)')
        elif (bannerinput == 4321):
            fivestarlim = (['Yoimiya'])
            fourstarlim = (['Bennett', 'Kujou Sara', 'Chevreuse'])
            banner_ver = bannerinput
            bannerver = str('4.3 phase 2 (yoimiya)')
        elif (bannerinput == 4322):
            fivestarlim = (['Raiden Shogun'])
            fourstarlim = (['Bennett', 'Kujou Sara', 'Chevreuse'])
            banner_ver = bannerinput
            bannerver = str('4.3 phase 2 (raiden shogun)')
        elif (bannerinput == 4411):
            fivestarlim = (['Nahida'])
            fourstarlim = (['Noelle', 'Faruzan', 'Gaming'])
            banner_ver = bannerinput
            bannerver = str('4.4 phase 1 (nahida)')
        elif (bannerinput == 4412):
            fivestarlim = (['Xianyun'])
            fourstarlim = (['Noelle', 'Faruzan', 'Gaming'])
            banner_ver = bannerinput
            bannerver = str('4.4 phase 1 (xianyun)')
        elif (bannerinput == 4421):
            fivestarlim = (['Yae Miko'])
            fourstarlim = (['Ningguang', 'Xinyan', 'Yaoyao'])
            banner_ver = bannerinput
            bannerver = str('4.4 phase 2 (yae miko)')
        elif (bannerinput == 4422):
            fivestarlim = (['Xiao'])
            fourstarlim = (['Ningguang', 'Xinyan', 'Yaoyao'])
            banner_ver = bannerinput
            bannerver = str('4.4 phase 2 (xiao)')
        elif (bannerinput == 4511):
            fivestarlim = (['Itto'])
            fourstarlim = (['Gorou', 'Yun Jin', 'Dori'])
            banner_ver = bannerinput
            bannerver = str('4.5 phase 1 (itto)')
        elif (bannerinput == 4512):
            fivestarlim = (['Chiori'])
            fourstarlim = (['Gorou', 'Yun Jin', 'Dori'])
            banner_ver = bannerinput
            bannerver = str('4.5 phase 1 (chiori)')
        elif (bannerinput == 4521):
            fivestarlim = (['Kazuha'])
            fourstarlim = (['Barbara', 'Xingqiu', 'Yanfei'])
            banner_ver = bannerinput
            bannerver = str('4.5 phase 2 (kazuha)')
        elif (bannerinput == 4522):
            fivestarlim = (['Neuvillette'])
            fourstarlim = (['Barbara', 'Xingqiu', 'Yanfei'])
            banner_ver = bannerinput
            bannerver = str('4.5 phase 2 (neuvillette)')
        elif (bannerinput == 4611):
            fivestarlim = (['Lyney'])
            fourstarlim = (['Xiangling', 'Lynette', 'Freminet'])
            banner_ver = bannerinput
            bannerver = str('4.6 phase 1 (lyney)')
        elif (bannerinput == 4612):
            fivestarlim = (['Arlecchino'])
            fourstarlim = (['Xiangling', 'Lynette', 'Freminet'])
            banner_ver = bannerinput
            bannerver = str('4.6 phase 1 (arlecchino)')
        elif (bannerinput == 4621):
            fivestarlim = (['Baizhu'])
            fourstarlim = (['Beidou', 'Layla', 'Faruzan'])
            banner_ver = bannerinput
            bannerver = str('4.6 phase 2 (baizhu)')
        elif (bannerinput == 4622):
            fivestarlim = (['Wanderer'])
            fourstarlim = (['Beidou', 'Layla', 'Faruzan'])
            banner_ver = bannerinput 
            bannerver = str('4.6 phase 2 (wanderer)')
        elif (bannerinput == 4711):
            fivestarlim = (['Clorinde'])
            fourstarlim = (['Bennett', 'Thoma', 'Sethos'])
            banner_ver = bannerinput
            bannerver = str('4.7 phase 1 (clorinde)')
        elif (bannerinput == 4712):
            fivestarlim = (['Alhaitham'])
            fourstarlim = (['Bennett', 'Thona', 'Sethos'])
            banner_ver = bannerinput
            bannerver = str('4.7 phase 1 (alhaithaim)')
        elif (bannerinput == 4721):
            fivestarlim = (['Furina'])
            fourstarlim = (['Noelle', 'Rosaria', 'Gaming'])
            banner_ver = bannerinput 
            bannerver = str('4.7 phase 2 (furina)')
        elif (bannerinput == 4722):
            fivestarlim = (['Sigewinne'])
            fourstarlim = (['Noelle', 'Rosaria', 'Gaming'])
            banner_ver = bannerinput
            bannerver = str('4.7 phase 2 (sigewinne)')
        elif (bannerinput == 4811):
            fivestarlim = (['Nilou'])
            fourstarlim = (['Ningguang', 'Kaveh', 'Kirara'])
            banner_ver = bannerinput
            bannerver = str('4.8 phase 1 (nilou)')
        elif (bannerinput == 4812):
            fivestarlim = (['Navia'])
            fourstarlim = (['Ningguang', 'Kaveh', 'Kirara'])
            banner_ver = bannerinput
            bannerver = str('4.8 phase 1 (navia)')
        elif (bannerinput == 4821):
            fivestarlim = (['Yelan'])
            fourstarlim = (['Razor', 'Xianglling', 'Yanfei'])
            banner_ver = bannerinput 
            bannerver = str('4.8 phase 2 (yelan)')
        elif (bannerinput == 4822):
            fivestarlim = (['Emilie'])
            fourstarlim = (['Razor', 'Xiangling', 'Yanfei'])
            banner_ver = bannerinput
            bannerver = str('4.8 phase 2 (emilie)')
        else:
            print (f'please enter a valid version number and banner!')
    except ValueError:
        print (f'please enter a valid version number and banner!1')
        

while True:

    user_input: str = input('command:')

    if (user_input == 'wish10'):
        wish10()
    elif user_input == 'wish1':
        wish1()
    elif user_input == 'inventory':
        print (f'loading inventory...')
        wait (1)
        inventory()
    elif user_input == 'pulls':
        pull()
    elif user_input == 'getmorepulls':
        getmorepulls()
    elif user_input == 'getmorepaidmos':
        getmorepaidmos()
    elif user_input == 'seemywallet':
        print (f'pulls:{pulls}')
        print (f'paidmos:{paidmos}')
    elif user_input == 'changebanner':
        changebanner()
    elif user_input == 'currentbanner':
        print (f'current banner: {bannerver}')
        print (f'current five star limited: {fivestarlim}')
        print (f'current rate up four star: {fourstarlim}')
    elif user_input == 'help':
        print (help)
    elif user_input == 'wt':
        wishforacharacter1new()
    elif user_input == 'exit':
        break
    else:
        print ('invalid command, type "help" for a list of commands')
