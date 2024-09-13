import subprocess
from locate_ip import locate_main

def main():

    while True:
        print("Choose an option:")
        print("1. Recon")
        print("2. Weaponisation")
        print("3. Exploitation")
        print("4. Quit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            locate_main.main()

        elif choice=='4':
            return
    '''
    elif choice == '2':
        subprocess.run(['python', '2.py'])
    elif choice == '3':
        subprocess.run(['python', '3.py'])
    
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
    '''

if __name__ == "__main__":
    main()
