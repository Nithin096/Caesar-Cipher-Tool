import os
import platform
import datetime
import time
import random
import sys

# Color codes for terminal
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
CYAN = "\033[36m"
WHITE = "\033[97m"

def bold_text(text):
    return f"{BOLD}{text}{RESET}"

def color_text(text, color):
    return f"{color}{text}{RESET}"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    system_info = platform.uname()
    banner = f"""
{color_text(bold_text('███████╗ █████╗ ███████╗ █████╗ ███████╗ ██████╗'), GREEN)} {color_text(f'({current_time})', WHITE)}
{color_text(bold_text('██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔═══██╗'), GREEN)} {color_text(f'{system_info.system} {system_info.release}', WHITE)}
{color_text(bold_text('█████╗  ███████║███████╗███████║███████╗██║   ██║'), GREEN)} {color_text(f'{system_info.machine} {system_info.version}', WHITE)}
{color_text(bold_text('██╔══╝  ██╔══██║╚════██║██╔══██║╚════██║██║   ██║'), GREEN)} {color_text(f'{system_info.processor}', WHITE)}
{color_text(bold_text('██║     ██║  ██║███████║██║  ██║███████║╚██████╔╝'), GREEN)}
{color_text(bold_text('╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ '), GREEN)}
{color_text(bold_text('Created by Nithin96'), YELLOW)}
    """
    print(banner)

def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = []
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result.append(encrypted_char)
        else:
            result.append(char)
    return ''.join(result)

def loading_animation(message, length):
    for _ in range(length):
        sys.stdout.write(random.choice(['\\', '|', '/', '-']))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

def display_result_animation(result):
    for _ in range(len(result)):
        time.sleep(0.1)
        sys.stdout.write(random.choice(['\\', '|', '/', '-']))
        sys.stdout.flush()
        time.sleep(0.05)
        sys.stdout.write('\b')
    print(f"{color_text(bold_text(result), CYAN)}")

def hacker_animation():
    """Simulates a hacker-like processing animation."""
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+'
    for _ in range(30):
        sys.stdout.write(f"\r{color_text('Hacking', GREEN)} {random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}")
        sys.stdout.flush()
        time.sleep(0.1)

def menu():
    while True:
        clear_screen()
        display_banner()
        print(f"\n{bold_text('Menu:')}")
        print(f"1. Encrypt")
        print(f"2. Decrypt")
        print(f"3. View Saved Results")
        print(f"4. Clear Screen")
        print(f"5. Exit")
        
        choice = input(f"Enter your choice ({bold_text('1/2/3/4/5')}): ").strip()
        
        if choice == '1':
            text = input("Enter the text: ").strip()
            shift = int(input("Enter the shift value (0-25): ").strip())
            print(f"{bold_text('Processing...')}")
            loading_animation("Processing...", len(text))
            hacker_animation()
            result = caesar_cipher(text, shift)
            print("\nResult: ", end="")
            display_result_animation(result)
            save_result(result)
        
        elif choice == '2':
            text = input("Enter the text: ").strip()
            shift = int(input("Enter the shift value (0-25): ").strip())
            print(f"{bold_text('Processing...')}")
            loading_animation("Processing...", len(text))
            hacker_animation()
            result = caesar_cipher(text, shift, decrypt=True)
            print("\nResult: ", end="")
            display_result_animation(result)
            save_result(result)
        
        elif choice == '3':
            view_results()
        
        elif choice == '4':
            clear_screen()
        
        elif choice == '5':
            print(color_text(bold_text("Exiting the program. Stay safe, hacker!"), RED))
            print(color_text(f"Program created by {bold_text('Nithin96')}", CYAN))
            break
        
        else:
            print(color_text(bold_text("Invalid choice! Please try again."), RED))
            time.sleep(1)

def save_result(result):
    save = input(f"Would you like to save the result to a file? ({bold_text('y/n')}): ").strip().lower()
    if save == 'y':
        with open("caesar_cipher_results.txt", "a") as file:
            file.write(f"{result}\n")
        print(color_text(bold_text("Result saved to caesar_cipher_results.txt"), GREEN))
    else:
        print(color_text(bold_text("Result not saved."), YELLOW))

def view_results():
    clear_screen()
    if os.path.exists("caesar_cipher_results.txt"):
        with open("caesar_cipher_results.txt", "r") as file:
            results = file.read().strip()
            if results:
                print(bold_text("Saved Results:"))
                print(color_text(results, CYAN))
            else:
                print(color_text(bold_text("No results found."), YELLOW))
    else:
        print(color_text(bold_text("No saved results file found."), YELLOW))
    input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    menu()

