import os
import subprocess


from locate_ip.locate_main import main
from locate_open_port_and_services import locate_open_port_and_services
from wordlist_generator import cupp


def main():

    while True:
        os.system("clear")

        choice = int(
            input(
                "1. Locate IP\n2. Locate open ports and services\n3. Discover\n4. Wordlist Generator\n5. Main Menu\nEnter your choice: "
            )
        )

        if choice == 1:
            # main()
            pass
        elif choice == 2:
            locate_open_port_and_services.main()
        elif choice == 3:
            pass
        elif choice == 4:
            subprocess.run(["python3", "generator.py", "-i"])
        elif choice == 5:
            break


if __name__ == "__main__":
    main()
