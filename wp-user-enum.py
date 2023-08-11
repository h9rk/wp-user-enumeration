# wp-enum.py
import requests
import sys
import os
import json
import colorama
from colorama import Fore, Style

# Code started *_8

def clear():
    if sys.platform.startswith('linux'):
        os.system('clear')
    else:
        os.system('cls')
clear()

# Coloring stuff
class fuk_maar_chacha:
    def __init__(self):
        colorama.init(autoreset=True)

    def color(self, text, color):
        colors = {
            "black": colorama.Fore.BLACK + Style.BRIGHT,
            "red": colorama.Fore.RED + Style.BRIGHT,
            "green": colorama.Fore.GREEN + Style.BRIGHT,
            "yellow": colorama.Fore.YELLOW + Style.BRIGHT,
            "blue": colorama.Fore.BLUE + Style.BRIGHT,
            "magenta": colorama.Fore.MAGENTA + Style.BRIGHT,
            "cyan": colorama.Fore.CYAN + Style.BRIGHT,
            "white": colorama.Fore.WHITE + Style.BRIGHT
        }

        if color.lower() in colors:
            return colors[color.lower()] + text
        else:
            return text

def banner():
    colored_text = fuk_maar_chacha()

    skull = "\U0001F480"

    message = '\t\t\t' + '[+]' + "Tool Information :"
    description = '\t\t\t' + '[+]' + skull + 'Wordpress User EnumeraTion'
    creator = '\t\t\t' + '[+]' + skull + 'Creator : h9rk_1337'
    print(colored_text.color(message, "white"))
    print(colored_text.color(description, "red"))
    print(colored_text.color(creator, "yellow"))

# Coloring ended

def wp_enum():
    header = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; es-GQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 UCBrowser/13.4.0.1306'
    }
    path = "/wp-json/wp/v2/users"

    file_path = input("[+] Enter list path or filename: ")

    with open(file_path, 'r') as file:
        urls = file.readlines()
    urls = [url.strip() for url in urls]

    
    symbol = Fore.CYAN + Style.BRIGHT + '[+]'
    color_ = fuk_maar_chacha()

    for url in urls:
        try:
            final_url = url + path
            response = requests.get("https://" + url + path)
            
            if response.status_code == 200:
                if "description" in response.text:
                    try:
                        loda_json = json.loads(response.text)
                    except Exception as e:
                        print(e)
                        sys.exit("[-] JSON parsing error")
                    try:
                        print(f'{symbol}'+color_.color(f'Enumeration For :{url}','green'))

                        print(f"{symbol} Total Found {len(loda_json)} users")
                        for x in range(0, len(loda_json)):
                            user_id = loda_json[x]['id']
                            full_name = loda_json[x]['name']
                            user_name = loda_json[x]['slug']

                            print(f"[+] User ID: {user_id}\nName: {full_name}\nUsername: {user_name}")
                            save = open('userenum.txt','a')
                            save.write(f"\n[+]Url: {url}\n"+f'[+] User ID: {user_id}\n'+f'Name: {full_name}\n'+f'Username: {user_name}\n')
                    except Exception:
                        print("[-] Enumeration failure")
                else:
                    pass
            else:
                pass

        except Exception as e:
            pass

if __name__ == "__main__":
    banner()
    wp_enum()
