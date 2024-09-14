import subprocess
import os

from recon.locate_ip import locate_main
from recon.locate_open_port_and_services import locate_open_port_and_services
from recon.wordlist_generator import cupp


def recon():
    while True:
        os.system("clear")

        choice = int(
            input(
                "1. Locate IP\n2. Locate open ports and services\n3. Discover\n4. Wordlist Generator\n5. Main Menu\nEnter your choice: "
            )
        )

        if choice == 1:
            locate_main.main()
            input("Completed!! Press Enter to continue")
        elif choice == 2:
            locate_open_port_and_services.main()
            input("Completed!! Press Enter to continue")
        elif choice == 3:
            pass
        elif choice == 4:
            subprocess.run(["python3", "generator.py", "-i"])
            input("Completed!! Press Enter to continue")
        elif choice == 5:
            break


def main():

    while True:
        print("Choose an option:")
        print("1. Recon")
        print("2. Weaponisation")
        print("3. Exploitation")
        print("4. Quit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            recon()

        elif choice == "4":
            return
    """
    elif choice == '2':
        subprocess.run(['python', '2.py'])
    elif choice == '3':
        subprocess.run(['python', '3.py'])
    
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
    """


if __name__ == "__main__":
    main()
