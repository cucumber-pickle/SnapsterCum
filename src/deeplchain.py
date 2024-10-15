import os
import json
import asyncio
from datetime import datetime
from colorama import *

mrh = Fore.LIGHTRED_EX
pth = Fore.LIGHTWHITE_EX
hju = Fore.LIGHTGREEN_EX
kng = Fore.LIGHTYELLOW_EX
bru = Fore.LIGHTBLUE_EX
reset = Style.RESET_ALL
htm = Fore.LIGHTBLACK_EX

last_log_message = None

def _banner():
    banner = r"""
      _____   _    _    _____   _    _   __  __   ____    ______   _____  
     / ____| | |  | |  / ____| | |  | | |  \/  | |  _ \  |  ____| |  __ \ 
    | |      | |  | | | |      | |  | | | \  / | | |_) | | |__    | |__) |
    | |      | |  | | | |      | |  | | | |\/| | |  _ <  |  __|   |  _  / 
    | |____  | |__| | | |____  | |__| | | |  | | | |_) | | |____  | | \ \ 
     \_____|  \____/   \_____|  \____/  |_|  |_| |____/  |______| |_|  \_\ """
    print(Fore.GREEN + Style.BRIGHT + banner + Style.RESET_ALL)
    print(hju + f" Snapster Auto Bot")
    print(mrh + f" FREE TO USE = Join us on {hju}t.me/cucumber_scripts")
    print(mrh + f" before start please '{hju}git pull{mrh}' to update bot")
    log_line()

def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_config():
    config_path = os.path.join(os.path.dirname(__file__), '../config.json')
    with open(config_path, 'r') as file:
        try:
            config_content = file.read()
            return json.loads(config_content)
        except json.JSONDecodeError as e:
            return {}

def log_error(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("last.log", "a") as log_file:
        log_file.write(f"{now}{message}\n")

def log(message, **kwargs):
    global last_log_message
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    flush = kwargs.pop('flush', False)
    end = kwargs.pop('end', '\n')
    if message != last_log_message:
        print(f"{htm}[{current_time}] {message}", flush=flush, end=end)
        last_log_message = message

def log_line():
    print(pth + "~" * 60)

async def countdown_timer(seconds):
    while seconds:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        h = str(h).zfill(2)
        m = str(m).zfill(2)
        s = str(s).zfill(2)
        print(f"{pth}please wait until {h}:{m}:{s} ", flush=True, end="\r")
        seconds -= 1
        await asyncio.sleep(1)
    print(f"{pth}please wait until {h}:{m}:{s} ", flush=True, end="\r")

def _number(number):
    return "{:,.0f}".format(number)