import os
import sys
import asyncio
import aiohttp
import json

# Nettoyage de l'écran automatique
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 1. SCANNER DE PSEUDONYME ULTRA-RAPIDE
async def check_site(session, site_name, url_template, username):
    url = url_template.format(username)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        # Configuration propre du timeout et désactivation du SSL strict pour Termux
        timeout = aiohttp.ClientTimeout(total=8)
        async with session.get(url, headers=headers, timeout=timeout, ssl=False) as response:
            if response.status == 200:
                print(f"[\033[92m+\033[0m] {site_name}: {url}")
            elif response.status == 404:
                print(f"[\033[91m-\033[0m] {site_name}: Introuvable (404)")
            else:
                print(f"[\033[93m?\033[0m] {site_name}: Code {response.status}")
    except Exception as e:
        print(f"[\033[91m!\033[0m] {site_name}: Erreur de connexion")

async def scan_username(username):
    platforms = {
        "GitHub": "https://github.com/{}",
        "Instagram": "https://instagram.com{}",
        "TikTok": "https://tiktok.com@{}",
        "Pinterest": "https://pinterest.com{}",
        "Twitter-X": "https://x.com{}",
        "YouTube": "https://youtube.com/@{}"
    }
    
    print(f"\n[\033[94m*\033[0m] Recherche globale pour : {username}...\n")
    async with aiohttp.ClientSession() as session:
        tasks = [check_site(session, name, template, username) for name, template in platforms.items()]
        await asyncio.gather(*tasks)
    input("\nAppuyez sur Entrée pour revenir au menu principal...")

# 2. MENU PRINCIPAL DU SCRIPT
def main_menu():
    while True:
        clear_screen()
        print("""
\033[95m  ________ __                     __     .___        __   
 /  _____//  |__   ____  _______/  |_   |   | _____/  |_  
/   \  __\  |  \ /  _ \/  ___/\   __\  |   |/    \   __\ 
\   \_\  \   Y  (  <_> )___ \  |  |    |   |   |  \  |   
 \______  /__|_  /\____/____  > |__|    |___|___|  /__|   
        \/     \/           \/                   \/      \033[0m
==========================================================
        \033[94m=== GHOST INTEL PRO - MULTI-TOOL v2 ===\033[0m
==========================================================
1. Scanner un pseudonyme (Ultra-Fast OSINT)
2. Tracker une adresse IP (À venir)
3. Analyser un numéro (À venir)
4. Quitter le script
==========================================================
        """)
        choix = input("Choisissez une option (1-4) : ").strip()
        
        if choix == "1":
            pseudo = input("\nEntrez le pseudonyme à rechercher : ").strip()
            if pseudo:
                asyncio.run(scan_username(pseudo))
        elif choix == "2":
            print("\nOption IP en cours de développement...")
            input("\nAppuyez sur Entrée...")
        elif choix == "3":
            print("\nOption Téléphone en cours de développement...")
            input("\nAppuyez sur Entrée...")
        elif choix == "4":
            print("\n\033[93mFermeture de Ghost Intel. Au revoir !\033[0m")
            sys.exit()
        else:
            print("\nOption invalide !")
            input("\nAppuyez sur Entrée...")

if __name__ == "__main__":
    main_menu()

