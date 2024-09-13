from . import bulkipscanner,singleipscanner

def main():

    while True:
        choice=int(input("1. Single IP Scanning\n2. Multi IP Scanning\n3. Back to main menu\nEnter your choice: "))

        if choice==1:
            bulkipscanner.main()
        elif choice==2:
            singleipscanner.main()
        elif choice==3:
            return
        else:
            print("Error")