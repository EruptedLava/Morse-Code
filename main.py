import os
import platform
import colorama
from colorama import Fore
import pyperclip

colorama.init()
morse_code = {
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..", 
    "e":".", 
    "f":"..-.", 
    "g":"--.", 
    "h":"....",
    "i":"..", 
    "j":".---", 
    "k":"-.-", 
    "l":".-..", 
    "m":"--", 
    "n":"-.", 
    "o":"---", 
    "p":".--.", 
    "q":"--.-", 
    "r":".-.", 
    "s":"...", 
    "t":"-", 
    "u":"..-",
    "v":"...-", 
    "w":".--", 
    "x":"-..-", 
    "y":"-.--", 
    "z":"--..",
    ",":"--..--",
    "?":"..--..",
    " ":"/"
}

logo = Fore.GREEN+'''\n\n8888888b.                                 888                      d88P                                              888          
888  "Y88b                                888                     d88P                                               888          
888    888                                888                    d88P                                                888          
888    888  .d88b.   .d8888b .d88b.   .d88888  .d88b.           d88P          .d88b.  88888b.   .d8888b .d88b.   .d88888  .d88b.  
888    888 d8P  Y8b d88P"   d88""88b d88" 888 d8P  Y8b         d88P          d8P  Y8b 888 "88b d88P"   d88""88b d88" 888 d8P  Y8b 
888    888 88888888 888     888  888 888  888 88888888        d88P           88888888 888  888 888     888  888 888  888 88888888 
888  .d88P Y8b.     Y88b.   Y88..88P Y88b 888 Y8b.           d88P            Y8b.     888  888 Y88b.   Y88..88P Y88b 888 Y8b.     
8888888P"   "Y8888   "Y8888P "Y88P"   "Y88888  "Y8888       d88P              "Y8888  888  888  "Y8888P "Y88P"   "Y88888  "Y8888  
                                                                                                                                  
                    Version 2.0
                                                  MADE BY Erupted_Lava                                                                     
                                                                                                                                  

'''+Fore.RESET
reverse_morse_code = {value:key for key,value in morse_code.items()}



def encrypt(text):
    morse = ""
    for i in text:
        if i in morse_code:
            morse+=f"{morse_code[i]} "
        else:
            morse+=f"{i} "

    pyperclip.copy(morse)
    print(f"\n The encoded text is : {Fore.GREEN+morse+Fore.RESET}")


def decrypt(morsed_code):

    morsed_code = morsed_code.split(' ')
    real_text = ""
    for i in morsed_code:
        if i in reverse_morse_code:
            real_text+=f"{reverse_morse_code[i]}"
        else:
            real_text+= f"{i}"

    pyperclip.copy(real_text)
    print(f"\n The decoded text is : {Fore.BLUE+real_text.title()+Fore.RESET}")

if __name__ == '__main__':

    should_continue = True
    while should_continue:
        if platform.system() == "Linux":
            os.system('clear')
        else:
            os.system('cls')
        print(logo)
        direction = input(Fore.LIGHTBLUE_EX+" Type 'e' to encrypt, type 'd' to decrypt:\n "+Fore.RESET)
        text = input(Fore.GREEN+" Type your message:\n "+Fore.RESET).lower()
    

        if direction == 'd':
            decrypt(text)
        elif direction == 'e':
            encrypt(text)

        choice = input("\n\n Type 'y' if you want to go again. Otherwise, type 'n'  >> ")
        if choice =="n":
            print(" GoodByee")
            break
