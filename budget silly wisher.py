from asyncio import wait
import random

user_input: str = ''
pulls: int = 1
fivestar: list[str] = {"Keqing":1, "Dehya":2, "Diluc":3, "Qiqi":4, "Jean":5, "Tighnari":6, "Mona":7, "Yumemizuki Mizuki":8}
fourstar: list[str] = {"Aino":9, "Aloysha":10, "Amber":11, "Barbara":12, "Beidou":13, "Bennett":14, "Candace":15, "Charlotte":16, "Chevreuse":17, "Chongyun":18, "Collei":19, "Dahlia":20, "Diona":21, "Dori":22, "Faruzan":23, "Fischl":24, "Freminet":25, "Gaming":26, "Gorou":27, "Iansan":28, "Ifa":29, "Illuga":30, "Jahoda":31, "Kachina":32, "Kaeya":33, "Kaveh":34, "Kirara":35, "Kujou Sara":36, "Kuki Shinobu":37, "Lan Yan":38, "Layla":39, "Lisa":40, "Lynette":41, "Mika":42, "Ningguang":43}
crap: list[str] = {'crap1':44, 'crap2':45}
userinventory: list[str] = {''}
help: str = 'commands: wish10, wish1, inventory, help, pulls, getmorepulls, exit'
fivestarchance: float = (.006)
fourstarchance: float = (.051)
crapchance: float = (.943)
fourstarpicked: bool = False
crappicked: bool = False
pullresult = []


def wishforacharacter():
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    pullresult.append(result)
    if (pullresult == 'fivestar'):
        print(random.choices(fivestar))
    elif (pullresult == 'fourstar'):
        print(random.choices(fourstar))
    elif (pullresult == 'crap'):
        print(random.choices(crap))
    return

        

##start of silly wisher
print('welcome to budget silly wisher v1.0')
print('information accurate as of genshin version 7.1')
print('this only has the standard banner cuz i have no time to add the others')
print('oh also no weapons cuz i said so')
print('type "help" for a list of commands or "wish10" or "wish1" to start pulling')
print(f'you have {pulls} pulls left')

def wish10():
    global pulls 
    if (pulls > 10):
        pulls -= 10
        print ('pulling...')
        wait (5)
        print (f'you pulled {pull1}, {pull2}, {pull3}, {pull4}, {pull5}, {pull6}, {pull7}, {pull8}, {pull9}, and {pull10}')
        userinventory.append(pull1)
        userinventory.append(pull2)
        userinventory.append(pull3)
        userinventory.append(pull4)
        userinventory.append(pull5)
        userinventory.append(pull6)
        userinventory.append(pull7)
        userinventory.append(pull8)
        userinventory.append(pull9)
        userinventory.append(pull10)
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
        wait (5)
        print (f'you pulled {pull1}')
        userinventory.append(pull1)
        print ('' + str(pulls) + ' pulls left')
        return
    return

def inventory():
    print (f'{userinventory}')
    return

def pull():
    global pulls
    print (f'you have {pulls} pull(s) left')
    return

def wait(seconds: int):
    import time
    time.sleep(seconds)
    return

def getmorepulls():
    global pulls
    print ('how many pulls would you like?')
    try:
        more_pulls: int = int(input())
        pulls += more_pulls
        print (f'deducting $' + str(more_pulls * 2) + ' from your bank account...')
        wait (3)
        print (f'you have been given {more_pulls} more pulls! thanks for the free moneh :)')
    except ValueError:
        print ('please enter a valid number')

while True:
    user_input: str = input('command:')

    if (user_input == 'wish10'):
        wish10()
    elif user_input == 'wish1':
        wish1()
    elif user_input == 'inventory':
        inventory()
    elif user_input == 'help':
        print (help)
    elif user_input == 'pulls':
        pull()
    elif user_input == 'getmorepulls':
        getmorepulls()
    elif user_input == 'wt':
        wishforacharacter()
    elif user_input == 'exit':
        break
    else:
        print ('invalid command, type "help" for a list of commands')
