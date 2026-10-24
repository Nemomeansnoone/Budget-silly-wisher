from asyncio import wait
import random

user_input: str = ''
banner_ver: int = 0
bannerver: str = 'standard'
pulls: int = 90
paidmos: int = 0
targetcharacter: dict[str] = ['Yelan']
fivestarlim: dict[str] = ['Yelan', 'Raiden Shogun']
fivestarstan: dict[str] = ['Keqing', 'Dehya', 'Diluc', 'Qiqi', 'Jean', 'Tighnari', 'Mona', 'Yumemizuki Mizuki']
fourstarstan: dict[str] = ['Aino', 'Aloysha', 'Amber', 'Barbara', 'Beidou', 'Bennett', 'Candace', 'Charlotte', 'Chevreuse', 'Chongyun', 'Collei', 'Dahlia', 'Diona', 'Dori', 'Faruzan', 'Fischl', 'Freminet', 'Gaming', 'Gorou', 'Iansan', 'Ifa', 'Illuga', 'Jahoda', 'Kachina', 'Kaeya', 'Kaveh', 'Kirara', 'Kujou Sara', 'Kuki Shinobu', 'Lan Yan', 'Layla', 'Lisa', 'Lynette', 'Mika', 'Ningguang', 'Noelle', 'Ororon', 'Prune', 'Razor', 'Rosaria', 'Sayu', 'Sethos', 'Shikanoin Heizou', 'Sucrose', 'Thoma', 'Xiangling', 'Xingqiu', 'Xinyan', 'Yanfei', 'Yaoyao', 'Yun Jun']
crap: dict[str] = ['crap']
lim: dict[str] = ['fivestarstan', 'fivestarlim']
userinventory = set()
help: str = 'commands: wish10, wish1, inventory, pulls, getmorepulls, getmorepaidmos, seemywallet, settargetcharacter, seetargetcharacter, changebanner, currentbanner, help, exit'
fivestarchance: float = (.006)
fourstarchance: float = (.051)
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
    global lim
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[1, 0, 0])[0]
    if (result == 'fivestar') or (sincelastfivestar >= 89):
        sincelastfivestar = 0
        resultingresult = [random.choice(lim)]
        pull0.update(resultingresult)
        print (resultingresult)
        if (resultingresult == ['fivestarlim']):
            resultingresultingresult = targetcharacter
            print (resultingresultingresult)
        elif (resultingresult == ['fivestarstan']):
            resultingresultingresult = [random.choice(fivestarstan)]
            print (resultingresultingresult)
        return
    elif (result == 'fourstar') or (sincelastfourstar >= 9):
        sincelastfourstar = 0
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

def settargetcharacter():
    global fivestarlim
    global targetcharacter
    print (f'please enter the character you want to set a target for (case sensitive!):')
    try:
        chartarg: str = str(input())
        if (chartarg in fivestarlim):
            targetcharacter = chartarg
            print (f'setting target character...')
            wait (1)
            print (f'set target character to {targetcharacter}')
        else:
            print (f'please enter a valid character!')
    except ValueError:
        print (f'please enter a valid character!')

def seetargetcharacter():
    print (f'your target character is {targetcharacter}')

def changebanner():
    global banner_ver
    global bannerver
    print (f'please enter the banner in the following format: <version (without decimal)><banner phase>')
    print (f'e.g. "711" for version 7.1 phase 1 banner, type 0 for standard banner')
    try:
        bannerinput: int = int(input())
        if (bannerinput == 0):
            banner_ver = bannerinput
            bannerver = str('standard')
        elif (bannerinput == 101):
            banner_ver = bannerinput
            bannerver = str('1.0 phase 1')
        elif (bannerinput == 102):
            banner_ver = bannerinput
            bannerver = str('1.0 phase 2')
        elif (bannerinput == 111):
            banner_ver = bannerinput
            bannerver = str('1.1 phase 1')
        elif (bannerinput == 112):
            banner_ver = bannerinput
            bannerver = str('1.1 phase 2')
        elif (bannerinput == 121):
            banner_ver = bannerinput
            bannerver = str('1.2 phase 1')
        elif (bannerinput == 122):
            banner_ver = bannerinput
            bannerver = str ('1.2 phase 2')
        elif (bannerinput == 131):
            banner_ver = bannerinput
            bannerver = str('1.3 phase 1')
        elif (bannerinput == 132):
            banner_ver = bannerinput
            bannerver = str('1.3 phase 2')
        elif (bannerinput == 141):
            banner_ver = bannerinput
            bannerver = str('1.4 phase 1')
        elif (bannerinput == 142):
            banner_ver = bannerinput
            bannerver = str('1.4 phase 2')
        elif (bannerinput == 151):
            banner_ver = bannerinput
            bannerver = str('1.5 phase 1')
        elif (bannerinput == 152):
            banner_ver = bannerinput
            bannerver = str('1.5 phase 2')
        elif (bannerinput == 161):
            banner_ver = bannerinput
            bannerver = str('1.6 phase 1')
        elif (bannerinput == 162):
            banner_ver = bannerinput
            banner_ver = str('1.6 phase 2')
        elif (bannerinput == 201):
            banner_ver = bannerinput
            bannerver = str('2.0 phase 1')
        elif (bannerinput == 202):
            banner_ver = bannerinput
            bannerver = str('2.0 phase 2')
        elif (bannerinput == 211):
            banner_ver = bannerinput
            bannerver = str('2.1 phase 1')
        elif (bannerinput == 212):
            banner_ver = bannerinput
            bannerver = str('2.1 phase 2')
        elif (bannerinput == 221):
            banner_ver = bannerinput
            bannerver = str('2.2 phase 1')
        elif (bannerinput == 222):
            banner_ver = bannerinput
            bannerver = str('2.2 phase 2')
        elif (bannerinput == 231):
            banner_ver = bannerinput
            bannerver = str('2.3 phase 1')
        elif (bannerinput == 232):
            banner_ver = bannerinput
            bannerver = str('2.3 phase 2')
        elif (bannerinput == 241):
            banner_ver = bannerinput
            bannerver = str('2.4 phase 1')
        elif (bannerinput == 242):
            banner_ver = bannerinput
            bannerver = str('2.4 phase 2')
        elif (bannerinput == 251):
            banner_ver = bannerinput
            bannerver = str('2.5 phase 1')
        elif (bannerinput == 252):
            banner_ver = bannerinput
            bannerver = str('2.5 phase 2')
        elif (bannerinput == 261):
            banner_ver = bannerinput
            bannerver = str('2.6 phase 1')
        elif (bannerinput == 262):
            banner_ver = bannerinput
            bannerver == str('2.6 phase 2')
        elif (bannerinput == 271):
            banner_ver = bannerinput
            bannerver = str('2.7 phase 1')
        elif (bannerinput == 272):
            banner_ver = bannerinput
            bannerver = str('2.7 phase 2')
        elif (bannerinput == 281):
            banner_ver = bannerinput
            bannerver = str('2.8 phase 1')
        elif (bannerinput == 282):
            banner_ver = bannerinput
            bannerver = str('2.8 phase 1')
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
    elif user_input == 'settargetcharacter':
        settargetcharacter()
    elif user_input == 'seetargetcharacter':
        seetargetcharacter()
    elif user_input == 'changebanner':
        changebanner()
    elif user_input == 'currentbanner':
        print (bannerver)
    elif user_input == 'help':
        print (help)
    elif user_input == 'wt':
        wishforacharacter1new()
    elif user_input == 'exit':
        break
    else:
        print ('invalid command, type "help" for a list of commands')
