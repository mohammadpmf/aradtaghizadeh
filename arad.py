from ascii_pro import *
import pygame
from time import sleep

player = pygame.mixer
player.init()
def load(n):
    player.music.load(n)
    player.music.play()
def myinput(i):
    answer = input(f"{i}: ").lower()
    while answer not in i:
        answer = input(f"{i}").lower()
    return answer

def play(a):
    if a =='exit':
        print('***Thank for playing this game***')
        exit()
    elif a=='salon':
        load('1.mp3')
    elif a=='garden':
        load('1.mp3')
    elif a in fridge_i and a!='kitchen':
        print(p.get(a))
        fridge_i.remove(a)
        sleep(3)
        print(p['fridge'])
        a = myinput(act.get('fridge'))
        play(a)
    elif a in microwave_i and a!='kitchen':
        t = int(input("Enter time in seconds: "))
        print(p['microwave'])
        for i in range(t, 0, -1):
            sleep(1)
            print(i)
        print(p.get(a))
        microwave_i.remove(a)
        sleep(3)
        print(p['kitchen'])
        a = myinput(act.get('kitchen'))
        play(a)
    elif a == 'sleep':
        print(sleepi)
        for i in range(1, 11):
            sleep(1)
            print(f'sleeping for {i} seconds.')
        print(p['room'])
        a = myinput(act.get('room'))
        play(a)

    elif a in transport_i:
        items = act.get(a)
        print(items)
        c = ''
        while c not in items:
            c = input('Where do you go? ')
        print(p.get(a))
        if a=='airplane':
            load('1.mp3')
        if a=='car':
            load('1.mp3')
        if a=='train':
            load('1.mp3')
        for i in range(10, 0, -1):
            sleep(1)
            print(f"wait {i} seconds to arrive that place. ")
        player.music.stop()
        print(p.get(c))
        c = myinput(act.get(c))
        play(c)
        
    print(p.get(a))
    a = myinput(act.get(a))
    play(a)

    

out_i = ['beach', 'jungle', 'garden', 'city', 'mount', 'exit']
transport_i = ['car', 'airplane', 'ship', 'horse', 'train', 'exit']
fridge_i = ['kitchen', 'banana', 'choco', 'milk', 'pineapple', 'icecream', 'drink', 'cheese', 'apple', 'exit']
microwave_i = ['kitchen', 'cake', 'pizza', 'hotdog', 'burger', 'cofee', 'exit']
p = { 
      'home'    : house,
      'house'   : house,
      'kitchen' : kitchen,
      'salon'   : salon,
      'room'    : bedroom,
      'fridge'  : fridge,
      'microwave': microwave,
      'burger'  : burger,
      'banana'  : banana,
      'choco'   : chocolate,
      'milk'    : milk,
      'cake'    : cake,
      'pizza'   : pizza,
      'hotdog'  : hotdog,
      'cheese'  : cheese,
      'apple'   : apple,
      'drink'   : drink,
      'icecream': icecream,
      'coffe'   : coffe,
      'horse'   : horse,
      'car'     : car,
      'airplane': airplane,
      'ship'    : ship,
      'garden'  : bird_garden,
      'mount'   : mount,
      'jungle'  : jungle,
      'city'    : city,
      'beach'   : beach,
      'train'   : train,
      'pineapple':pineapple,
      'tv'      : television,
      'tv1'     : tv1,
      'tv2'     : tv2,
      'tv3'     : tv3,
      'tv4'     : tv4,
      'tv_off'  : tv_off,
      'on'      : l_on,
      'off'     : l_off,
      'lamp'    : l_on,
      'outside' : out
}
act = {
    'home': ['salon', 'outside', 'exit'],
    'house': ['salon', 'outside', 'exit'],
    'room': ['salon', 'sleep', 'lamp', 'exit'],
    'tv': ['salon', 'tv1', 'tv2', 'tv3', 'tv4', 'exit'],
    'tv1': ['salon', 'tv2', 'tv3', 'tv4', 'tv_off', 'exit'],
    'tv2': ['salon', 'tv1', 'tv3', 'tv4', 'tv_off', 'exit'],
    'tv3': ['salon', 'tv1', 'tv2', 'tv4', 'tv_off', 'exit'],
    'tv4': ['salon', 'tv1', 'tv2', 'tv3', 'tv_off', 'exit'],
    'tv_off': ['salon', 'tv1', 'tv2', 'tv3', 'tv4', 'exit'],
    'salon': ['outside', 'room', 'kitchen', 'tv', 'exit'],
    'kitchen': ['salon', 'fridge', 'microwave', 'exit'],
    'lamp': ['room', 'off', 'exit'],
    'on': ['room', 'off', 'exit'],
    'off': ['room', 'on', 'exit'],
    'fridge': fridge_i,
    'microwave': microwave_i,
    'outside'  : transport_i,
    'car':['mount', 'city', 'jungle', 'home','exit'],
    'airplane':['mount', 'jungle', 'beach', 'home', 'exit'],
    'horse':['garden', 'jungle', 'mount', 'home', 'exit'],
    'ship':['beach', 'home', 'exit'],
    'train':['city', 'mount', 'home', 'exit'],
    'mount':['car', 'airplane', 'ship', 'horse', 'train', 'exit'],
    'beach':['car', 'airplane', 'ship', 'horse', 'train', 'exit'],
    'city':['car', 'airplane', 'ship', 'horse', 'train', 'exit'],
    'garden':['car', 'airplane', 'ship', 'horse', 'train', 'exit'],
    'jungle':['car', 'airplane', 'ship', 'horse', 'train', 'exit']
    


}

play('house')