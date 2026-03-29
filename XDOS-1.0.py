from math import sqrt
import os
import sys
import random
import time
import psutil as ps

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def system_info():
    print("---System---")
    cpu_usage = ps.cpu_percent(interval=1)
    freq = ps.cpu_freq()
    current_freq = freq.current

    print("CPU Usage:", cpu_usage, "%")
    print("Current Frequency:", current_freq, "MHz")
    print("DISCLAMER: CPU May be Innaccurate")
    print("-" * 40)
    
    ram = ps.virtual_memory()
    print(f"RAM Used:  {ram.used // (1024*1024)} MB")
    print(f"RAM Total: {ram.total // (1024*1024)} MB")
    print(f"RAM Usage: {ram.percent}%")

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
    print("XDOS is a basic Line-Based OS. It is Retro-style but has no kernel.")

def random_menu():
    print("Generated:", random.randint(1, 10))
    
def dice():
    dice = random.randint(1, 6)
    print("You Rolled: [",dice,"]")
    
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
    print("Welcome to XDOS!")
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
            random_menuu()
        elif cmd == "ops":
            ops()
        elif cmd == "time":
            time_menu()            
        elif cmd == "sys":
            system_info()
        elif cmd == "compute":
            time.sleep(0.2)
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

