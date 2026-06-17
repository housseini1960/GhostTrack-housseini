import os
import requests
import phonenumbers
import asyncio
import aiohttp
import random
from phonenumbers import geocoder, carrier

# Liste de navigateurs aléatoires pour tromper les protections des sites (Anti-Bot)
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def track_ip():
    clear_screen()
    print("=== IP ADDRESS TRACKER ===")
    ip = input("Enter IP address to analyze: ").strip()
    print("\nSearching...")
    try:
        response = requests.get(f"http://ipwho.is{ip}")
        data = response.json()
        if data.get("success"):
            print(f"\n[+] Status: Success")
            print(f"[+] Country: {data.get('country')}")
            print(f"[+] City: {data.get('city')}")
            print(f"[+] ISP: {data.get('connection', {}).get('isp')}")
            print(f"[+] Latitude: {data.get('latitude')}")
            print(f"[+] Longitude: {data.get('longitude')}")
            print(f"[+] Google Maps: https://google.com{data.get('latitude')},{data.get('longitude')}")
        else:
            print("\n[-] Unable to track this IP address.")
    except Exception as e:
        print(f"\n[-] An error occurred: {e}")
    input("\nPress Enter to return to menu...")

def track_phone():
    clear_screen()
    print("=== PHONE NUMBER TRACKER ===")
    number = input("Enter phone number (ex: +33612345678): ").strip()
    try:
        parsed_number = phonenumbers.parse(number)
        if phonenumbers.is_valid_number(parsed_number):
            location = geocoder.description_for_number(parsed_number, "en")
            operator = carrier.name_for_number(parsed_number, "en")
            print(f"\n[+] Valid Number")
            print(f"[+] Location: {location if location else 'Unknown'}")
            print(f"[+] Carrier: {operator if operator else 'Unknown'}")
        else:
            print("\n[-] Invalid phone number.")
    except Exception as e:
        print(f"\n[-] Incorrect format or error: {e}")
    input("\nPress Enter to return to menu...")

# Fonction asynchrone qui vérifie UN site de manière ultra-rapide
async def check_site(session, site_name, url_template, username):
    url = url_template.format(username)
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    try:
        # Requête asynchrone avec un timeout de 4 secondes maximum
        async with session.get(url, headers=headers, timeout=4) as response:
            if response.status == 200:
                print(f"[+] FOUND - {site_name}: {url}")
            else:
                print(f"[-] Not found - {site_name}")
    except:
        print(f"[-] Timeout/Error - {site_name}")

# Gestionnaire asynchrone qui lance TOUTES les requêtes en même temps
async def scan_all_platforms(username):
    platforms = {
        "GitHub": "https://github.com{}",
        "Instagram": "https://instagram.com{}",
        "TikTok": "https://tiktok.com@{}",
        "Pinterest": "https://pinterest.com{}",
        "Twitter/X": "https://x.com{}",
        "YouTube": "https://youtube.com@{}",
        "Reddit": "https://reddit.com{}",
        "Spotify": "https://spotify.com{}"
    }
    
    print(f"\nLaunching simultaneous scan for '{username}'...\n")
    # Création d'une session de requêtes web ultra-rapide
    async with aiohttp.ClientSession() as session:
        tasks = []
        for site_name, url_template in platforms.items():
            # On prépare la tâche pour chaque site sans attendre
            tasks.append(check_site(session, site_name, url_template, username))
        
        # On déclenche TOUTES les tâches en même temps (Simultané)
        await asyncio.gather(*tasks)

def track_username():
    clear_screen()
    print("=== ULTRA-FAST ASYNC USERNAME TRACKER ===")
    username = input("Enter username to search: ").strip()
    
    # Exécution de la boucle asynchrone Python
    asyncio.run(scan_all_platforms(username))
    
    input("\nPress Enter to return to menu...")

def main_menu():
    while True:
        clear_screen()
        print("====================================")
        print("       GHOSTTRACK PRO (ASYNC)       ")
        print("====================================")
        print("1. Track an IP Address")
        print("2. Analyze a Phone Number")
        print("3. Search a Username (Ultra-Fast)")
        print("4. Exit")
        print("====================================")
        choice = input("Select an option (1-4): ").strip()
        if choice == "1":
            track_ip()
        elif choice == "2":
            track_phone()
        elif choice == "3":
            track_username()
        elif choice == "4":
            print("\nThank you for using GhostTrack Pro. Goodbye!")
            break
        else:
            input("\n[-] Invalid option. Press Enter to try again...")

if __name__ == "__main__":
    main_menu()

