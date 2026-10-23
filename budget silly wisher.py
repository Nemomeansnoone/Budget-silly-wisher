from asyncio import wait
import random

user_input: str = ''
pulls: int = 69420
fivestar: list[str] = ['Keqing', 'Dehya', 'Diluc', 'Qiqi', 'Jean', 'Tighnari', 'Mona', 'Yumemizuki Mizuki']
fourstar: list[str] = ['Aino', 'Aloysha', 'Amber', 'Barbara', 'Beidou', 'Bennett', 'Candace', 'Charlotte', 'Chevreuse', 'Chongyun', 'Collei', 'Dahlia', 'Diona', 'Dori', 'Faruzan', 'Fischl', 'Freminet', 'Gaming', 'Gorou', 'Iansan', 'Ifa', 'Illuga', 'Jahoda', 'Kachina', 'Kaeya', 'Kaveh', 'Kirara', 'Kujou Sara', 'Kuki Shinobu', 'Lan Yan', 'Layla', 'Lisa', 'Lynette', 'Mika', 'Ningguang']
crap: list[str] = ['crap']
userinventory: list[str] = ['']
help: str = 'commands: wish10, wish1, inventory, help, pulls, getmorepulls, exit'
fivestarchance: float = (.006)
fourstarchance: float = (.051)
crapchance: float = (.943)
result2: str = ['']
pull1: str = ['']
pull2: str = ['']
pull3: str = ['']
pull4: str = ['']
pull5: str = ['']
pull6: str = ['']
pull7: str = ['']
pull8: str = ['']
pull9: str = ['']
pull10: str = ['']
globalresult: str = ['']

def wishforacharacter():
    global globalresult
    result = random.choices(['fivestar', 'fourstar', 'crap'], weights=[fivestarchance, fourstarchance, crapchance])[0]
    if (result == 'fivestar'):
        result2 =(random.choices(fivestar))
        globalresult.append(result2)
    elif (result == 'fourstar'):
        result2 = (random.choices(fourstar))
        globalresult.append(result2)
    elif (result == 'crap'):
        result2 = (random.choices(crap))
        globalresult.append(result2)

        

##start of silly wisher
print('welcome to budget silly wisher v1.0')
print('information accurate as of genshin version 7.1')
print('this only has the standard banner cuz i have no time to add the others')
print('oh also no weapons cuz i said so')
print('type "help" for a list of commands or "wish10" or "wish1" to start pulling')
print(f'you have {pulls} pulls left')

def clearrglobalresult():
    global globalresult
    globalresult = ['']
    return

def wish10():
    global pulls 
    if (pulls > 10):
        pulls -= 10
        print ('pulling...')
        wishforacharacter()
        pull1.append(globalresult)
        wait (.02)
        clearrglobalresult()
        wishforacharacter()
        pull2.append(globalresult)
        wait (.02)
        clearrglobalresult()
        wishforacharacter()
        pull3.append(globalresult)
        wait (.02)
        clearrglobalresult()
        wishforacharacter()
        pull4.append(globalresult)
        wait (.02)
        clearrglobalresult()
        wishforacharacter()
        pull5.append(globalresult)
        wait (.02)
        clearrglobalresult()
        wishforacharacter()
        pull6.append(globalresult)
        wait (.02)
        clearrglobalresult()
        wishforacharacter()
        pull7.append(globalresult)
        wait (.02)
        clearrglobalresult()
        wishforacharacter()
        pull8.append(globalresult)
        wait (.02)
        clearrglobalresult()
        wishforacharacter()
        pull9.append(globalresult)
        wait (.02)
        clearrglobalresult()
        wishforacharacter()
        pull10.append(globalresult)
        wait (.02)
        clearrglobalresult()
        wait (2)
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
