import os
import requests
import phonenumbers
from phonenumbers import geocoder, carrier

def clear_screen():
    # Clears the console based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def track_ip():
    clear_screen()
    print("=== IP ADDRESS TRACKER ===")
    ip = input("Enter IP address to analyze: ").strip()
    print("\nSearching...")
    
    try:
        # Querying a free geolocation API
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
        # Parsing the phone number format
        parsed_number = phonenumbers.parse(number)
        
        if phonenumbers.is_valid_number(parsed_number):
            # Extracting indicative location
            location = geocoder.description_for_number(parsed_number, "en")
            # Extracting original carrier network
            operator = carrier.name_for_number(parsed_number, "en")
            
            print(f"\n[+] Valid Number")
            print(f"[+] Location: {location if location else 'Unknown'}")
            print(f"[+] Carrier: {operator if operator else 'Unknown'}")
        else:
            print("\n[-] Invalid phone number.")
    except Exception as e:
        print(f"\n[-] Incorrect format or error: {e}")
        
    input("\nPress Enter to return to menu...")

def track_username():
    clear_screen()
    print("=== USERNAME TRACKER ===")
    username = input("Enter username to search: ").strip()
    print(f"\nSearching for '{username}' across platforms...\n")
    
    # List of sites to test
    platforms = {
        "GitHub": "https://github.com{}",
        "Instagram": "https://instagram.com{}",
        "TikTok": "https://tiktok.com@{}",
        "Pinterest": "https://pinterest.com{}"
    }
    
    for site_name, url_template in platforms.items():
        target_url = url_template.format(username)
        try:
            # Sending a light request to check profile existence
            response = requests.get(target_url, timeout=5)
            if response.status_code == 200:
                print(f"[+] FOUND - {site_name}: {target_url}")
            else:
                print(f"[-] Not found - {site_name}")
        except:
            print(f"[-] Connection error for {site_name}")
            
    input("\nPress Enter to return to menu...")

def main_menu():
    while True:
        clear_screen()
        print("====================================")
        print("          MY OSINT TOOL             ")
        print("====================================")
        print("1. Track an IP Address")
        print("2. Analyze a Phone Number")
        print("3. Search a Username")
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
            print("\nThank you for using the tool. Goodbye!")
            break
        else:
            input("\n[-] Invalid option. Press Enter to try again...")

if __name__ == "__main__":
    main_menu()
