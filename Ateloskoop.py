import time
import random
import os

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# ASCII Banner
BANNER = f"""
{RED}
 █████╗ ████████╗███████╗██╗      ██████╗  ██████╗ ███████╗ ██████╗ ██╗  ██╗ ██████╗ ██████╗ 
██╔══██╗╚══██╔══╝██╔════╝██║     ██╔═══██╗██╔═══██╗██╔════╝██╔═══██╗██║ ██╔╝██╔═══██╗██╔══██╗
███████║   ██║   ██              ██║   ██║██║   ██║███████╗██║   ██║█████╔╝ ██║   ██║██████╔╝
██╔══██║   ██║   ██╔══╝  ██║     ██║   ██║██║   ██║╚════██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
██║  ██║   ██║   ███████╗███████╗╚██████╔╝╚██████╔╝███████║╚██████╔╝██║  ██╗╚██████╔╝██║     
╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                                                                                            
        {CYAN}Atelophobia Pass Finder v3.0{RESET}
"""

# App list
APPS = ["Roblox", "YouTube", "Netflix", "Discord", "Spotify", "Steam", "Amazon", "TikTok", "Instagram", "Twitter", "Reddit"]

def random_username(target):
    formats = [
        f"{target}_x",
        f"{target}99",
        f"{target.lower()}_official",
        f"{target}2025",
        f"{target}_dev",
        f"{target}_login",
        f"{target}_acc",
        f"{target}_main"
    ]
    return random.choice(formats)

def random_password(length=10):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def log(msg, level="INFO", color=CYAN, delay=0.3):
    ts = time.strftime("%H:%M:%S")
    print(f"{color}[{ts}] [{level}] {msg}{RESET}")
    time.sleep(delay)

def progress(label, steps=30, color=YELLOW):
    print(f"{color}{label}: {RESET}", end="", flush=True)
    for _ in range(steps):
        time.sleep(0.02)
        print(f"{GREEN}█{RESET}", end="", flush=True)
    print(f"{color} done.{RESET}")

def glitch_line():
    chars = "▒▓█░▒▓█▒▓█░▒▓█▒▓█░▒▓█▒▓█░▒▓█▒▓█░▒▓█▒▓█░▒▓█▒▓█░▒▓█▒▓█░▒▓█▒▓█░▒▓█"
    print(f"{RED}{''.join(random.choice(chars) for _ in range(60))}{RESET}")
    time.sleep(0.05)

def pass_finder(target):
    print(BANNER)
    print(f"{CYAN}Searching credentials for target: {target}{RESET}")
    progress("Initializing search modules", 25, CYAN)
    log("Connecting to Atelophobia Core", "INFO", CYAN)
    progress("Scanning darknet archives", 30, MAGENTA)
    log("Fingerprinting user identity...", "INFO", CYAN)
    time.sleep(0.5)
    log(f"Match found: {target}", "SUCCESS", GREEN)
    progress("Decrypting credential cache", 35, YELLOW)
    time.sleep(0.5)

    print(f"\n{RED}⚠️ Breach confirmed — credentials recovered for {target.upper()} ⚠️{RESET}\a")
    for _ in range(5):
        glitch_line()

    # Generate and display credentials
    print(f"\n{CYAN}Captured Credentials:{RESET}")
    print("-" * 60)
    print(f"{'APP':<12} | {'USERNAME':<20} | {'PASSWORD'}")
    print("-" * 60)
    for app in random.sample(APPS, 6):
        uname = random_username(target)
        pwd = random_password()
        print(f"{app:<12} | {uname:<20} | {pwd}")
    print("-" * 60)
    print(f"\n{GREEN}Operation complete.{RESET}")

# ------------------ MAIN ------------------
os.system('cls' if os.name == 'nt' else 'clear')
print(BANNER)
print(f"{YELLOW}Enter target username to begin scan:{RESET}")
target = input(f"{CYAN}>> {RESET}")

pass_finder(target)