import sys
import shutil

def main():
    while True:
        #sys.stdout.write("$ ")
        # Wait for user input
        command = input("$ ")
        '''command_and_params = command.split(" ")
        if command_and_params[0] == "exit":
            sys.exit(int(command_and_params[1]))
        elif command_and_params[0] == "echo":
            print(" ".join(command_and_params[1:]))
        elif command_and_params[0] == "type":
            if command_and_params[1] == "exit":    
                print(" ".join(command_and_params[1:]),"is a shell builtin")
            elif command_and_params[1] == "echo":
                print(" ".join(command_and_params[1:]),"is a shell builtin")
            elif command_and_params[1] == "type":
                print(" ".join(command_and_params[1:]),"is a shell builtin")
            elif command_and_params[1] == "invalid":
                print(" ".join(command_and_params[1:]),": not found")
        else:
            print(f"{command}: not found") '''
        
        '''match command:
            case command if command.startswith("echo "):
                sys.stdout.write(f"{command[len("echo "): ]}\n")
            case "exit 0":
                return 0
            case command if command.startswith("type invalid"):
                sys.stdout.write(f"{command[len('type '): ]}: not found\n")
            case command if command.startswith("type "):
                sys.stdout.write(f"{command[len("type "): ]} is a shell builtin\n")
            case _:
                sys.stdout.write(f"{command}: command not found\n")'''
        
        match command.split():
            case ["type", arg] if arg in ["echo","exit","type"]:
                print(f"{arg} is a shell builtin")
            case ["type", arg] if path := shutil.which(command):
                print(f"{command}" is "{path}") 
            case ["type", arg] if arg not in ["echo","exit","type"]:
                print(f"{arg}: not found")
            case ["exit","0"]:
                exit()
            case ["echo", *args]:
                print(*args)
            case _:
                print(f"{command}: command not found")





if __name__ == "__main__":
    main()
