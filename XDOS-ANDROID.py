from math import sqrt
import random
import time

print("Loading...")
time.sleep(0.25)
print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ops():
    print("Core: +, -, *, /,")
    print("Advanced: **(^), sqrt")
        
def help_menu():
    print("Commands:")
    print("  help   - Show this menu")
    print("  about  - Tells you about the OS")
    print("  time   - Shows the current time in Y-M-D and H:M:S format")
    print("  random - Generates a random number from 1-10")
    print("  sys - Shows your RAM + CPU usage")
    print("  compute  - Just your Ordinary Calculator")
    print("  ops  - Tells you all Calculator Operations")
    print("  dice - Rolls a random number from [1]-[6]")
    print("  kill  - Quit the OS")

def about_menu():
    print("XDOS, Ver: 1.0.2")

def random_menu():
    print("Generated:", random.randint(1, 10))
    
def dice():
    dice = random.randint(1, 6)
    if dice == 1:
        print("[*]")
    elif dice == 2:
        print("[**]")
    elif dice == 3:
        print("[***]")
    elif dice == 4:
        print("[***]")
        print("[*]")
    elif dice == 5:
        print("[***]")
        print("[**]")
    elif dice == 6:
        print("[***]")
        print("[***]")
    
def time_menu():
    unix = time.strftime("%Y-%m-%d %H:%M:%S")
    print(unix)

def calc(expr):
    try:
        print(eval(expr))
    except:
        print("Invalid expression.")
        
def main():
    clear_screen()
    print("Welcome to XDOS Android!")
    print("XDOS 1.0 Type 'help' for all the commands")

    while True:
        command = input("X: > ").strip().split()
        if not command:
            continue
        cmd = command[0]
        args = command[1:]

        if cmd == "help":
            help_menu()            
        elif cmd == "dice":
             dice()
        elif cmd == "about":
            about_menu()
        elif cmd == "random":
            random_menu()
        elif cmd == "ops":
            ops()
        elif cmd == "time":
            time_menu()
        elif cmd == "compute":
            if args:
                calc(" ".join(args))
            else:
                print("Sorry Invalid calculation")
                
        elif cmd == "kill":
            print("Shutting down XDOS...")
            break

        else:
            print("Error 207 - invalid request")

if __name__ == "__main__":
    main()

