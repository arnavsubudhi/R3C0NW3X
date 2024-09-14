import subprocess

from recon.locate_ip import locate_main
from recon.locate_open_port_and_services import locate_open_port_and_services

from exploitation.ssh_bruteforce import ssh_exploit
from exploitation.sub_domain_bruteforce import subenum


def recon():
    while True:

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


def weapon():
    choice = input("Do you have Searchsploit installed (y/n): ")

    if choice == "n":
        print("You need searchsploit to run this!! PLease install!!")
        return

    query = input(
        "Enter the service-name which you want to exploit (also mention the version number if possible): "
    )

    subprocess.run(["searchsploit", query])

    patch = input("Enter the patch nummber which you want to download: ")

    subprocess.run(["searchsploit", "-m", patch])

    input("Completed!! Press Enter to continue")


def exploit():

    while True:

        choice = int(
            input(
                "1. SSH Brute-force\n2. Sub-domain Brute-force\n3. Directory Brute-force\n4. Back to main menu: "
            )
        )

        if choice == 1:
            ssh_exploit.main()
            input("Completed!! Press Enter to continue")

        elif choice == 2:
            subenum.main()
            input("Completed!! Press Enter to continue")
        elif choice == 3:
            print("This feature is in-progress!!")
        elif choice == 4:
            break
        else:
            print("Wrong Input!! Please try again")


def main():

    while True:
        print("Choose an option:")
        print("1. Recon")
        print("2. Weaponisation")
        print("3. Exploitation")
        print("4. Quit")

        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            recon()

        elif choice == 2:
            weapon()

        elif choice == 3:
            exploit()

        elif choice == 4:
            return


if __name__ == "__main__":
    main()
