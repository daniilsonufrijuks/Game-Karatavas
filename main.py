# Izveidoja: Daniils Onufrijuks DP 1-1
from random import choice
from time import sleep
import pygame # lai izvadit skāņu
from import_words import word_store # importejam mūsu funkciju
#import time
import os

def main(): # funkcija
    # ja fail eksiste tad funkcija delete_file() nodzesisiet failu, citādak nē
    try:
        delet_file()
    except:
        pass

    #word_list = ["toy", "cat", "dog", "pencil", "game", "python", "mouse", "logs", "durvis", "lamp", "cave"] # dators var izveleties no šiem vardiem
    #rword = choice(word_list) # dators izvelas vienu vardu no saraksta

    rword = word_store("Words.txt") # tagad funkcija lasa failu un no faila ņem vardus
    guesses = "" # visi lietotaju ievades simboli
    trueguesses = 0 #pareizas atbildes counter
    sk = 6 #lietotajam ir tikai sešas iespejas uz kļūdu

    #print(logo)
    #animacija
    print('\n| |/ /           ___| |                        ')
    sleep(1)
    print("| ' / __ _ _ __ __ _| |_ __ ___   ____ _ ___ ")
    sleep(1)
    print("|  < / _` | '__/ _` | __/ _` \ \ / / _` / __|")
    sleep(1)
    print("| . \ (_| | | | (_| | || (_| |\ V / (_| \__`\`")
    sleep(1)
    print('|_|\_\__,_|_|  \__,_|\__\__,_| \_/ \__,_|___/\n')
    #animacija

    print()
    print()
    print()
    print()
    #print("Laipni lūdzam manā spēlē! Veiksmi!")
    intro = '''
     _           _             _   _           _                                                                   _      _  __      __  _ _                  _ _ 
    | |         (_)           (_) | |         | |                                                                 | |    | | \ \    / / (_) |                (_) |
    | |     __ _ _ _ __  _ __  _  | |_   _  __| |______ _ _ __ ___    _ __ ___   __ _ _ __   __ _   ___ _ __   ___| | ___| |  \ \  / /__ _| | _____ _ __ ___  _| |
    | |    / _` | | '_ \| '_ \| | | | | | |/ _` |_  / _` | '_ ` _ \  | '_ ` _ \ / _` | '_ \ / _` | / __| '_ \ / _ \ |/ _ \ |   \ \/ / _ \ | |/ / __| '_ ` _ \| | |
    | |___| (_| | | |_) | | | | | | | |_| | (_| |/ / (_| | | | | | | | | | | | | (_| | | | | (_| | \__ \ |_) |  __/ |  __/_|    \  /  __/ |   <\__ \ | | | | | |_|
    |______\__,_|_| .__/|_| |_|_| |_|\__,_|\__,_/___\__,_|_| |_| |_| |_| |_| |_|\__,_|_| |_|\__,_| |___/ .__/ \___|_|\___(_)     \/ \___|_|_|\_\___/_| |_| |_|_(_)
                | |                                                                                  | |                                                        
                |_|                                                                                  |_|                                                    
    '''
    print(intro)

    print("Dators izvelas vardu, Jūms ir jāmeģina noteikt to")
    user_name = input('Ievadiet Jūsu vardu: ')
    while sk > 0: # cikls
        for i in rword:
            if i in guesses:
                print(i, end=' ')
            else:
                print("_", end=' ')
        

        if trueguesses == len(rword): #parbaudam vai lietotajis uzvarēja vai nē
            win_game()
            sleep(1)
            play_win()
            write_into_file(user_name, sk)
            sleep(3) # guļam 5 sekundas
            break

        user_input = str(input("\nIevadiet vienu burtu: ")) # lietotaja ievade
        guesses += user_input

        if user_input in rword: #parbaudam vai lietotaja ievade bija pareiza
            trueguesses += 1
        if user_input not in rword: # ja lietotaja ievdits simbols nav datora izveletāja vardā, tad samazinam iespejas uz kļūdu un talak izvādam zīmejumus
            sk = sk - 1
        if sk < 6:
            print("|---|   ")
        if sk < 5:
            print("|   o   ")
        if sk < 4:
            print("|  /|\  ")
        if sk < 3:
            print("|  / \  ")
            print("|       ")
        if sk < 2:
            print("| ----- ")
        if sk < 1:
            print("| ----- ")
        if sk == 0:
            play_dead() # izvadam skaņu no funkcijas nevis ar komandam
            sleep(5) # guļam 5 sekundas
            stop_game(rword)
            write_into_file(user_name, sk)
            user_input2 = str(input("\nVai Jūs gribāt spelēt velreiz? [y - jā/ n - nē]: ")) # ievadam lai paturpināt speli pa jaunām vai pabeigt
            if user_input2 == "y":
                clear()
                main() # programma saksies pa jaunai 
            else:
                break # citadak beidzam

def play_win():
    pygame.mixer.init()
    pygame.mixer.music.load('win sound.mp3') #mūzikas izvade
    pygame.mixer.music.play(0)

def play_dead():
    pygame.mixer.init()
    pygame.mixer.music.load('dead.mp3') #mūzikas izvade
    pygame.mixer.music.play(0)

def write_into_file(user_name, sk: str): # rezultatu ierakstišāna failā
    file = open('rezultāti.txt', "a+")
    file.write(user_name)
    file.write(" ")
    file.write(str(sk))
    file.close()

#def word_store(): # vardu lasišāna un izvele
#    words = []
#    file = open("Words.txt", "r")
#    for word in file:
#        words.append(word[:-1])
#    rword = choice(words)
#    return rword

def delet_file(): # failu dzešana
    os.remove("rezultāti.txt")

def stop_game(rword: str): # izvade kād lietotajs neuzvareja
    print()
    print('ヾ(-_- )ゞ')
    print("\n\nUzvareja dators")
    print("Atbilde ir", rword)

def win_game(): # izvade kad uzvareja
    print()
    print("~(^-^)~")
    print("\nJūs uzvarejāt!")

def clear():
    os.system('cls')

main() # funkcijas calling
