from colorama import Fore, Back, Style, init

init(autoreset=True)

# Print text in red
print(Fore.RED + 'Hello World but Red!' + Style.RESET_ALL)

# Print text with a blue background
print(Back.BLUE + 'Hello World but on Blue!' + Style.RESET_ALL)

# Print text in red with a blue background
print(Fore.RED + Back.BLUE + 'Hello World but Red on Blue!' + Style.RESET_ALL)