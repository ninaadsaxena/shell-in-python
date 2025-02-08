import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input()
        command_and_params = command.split(" ")
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
            else:
                print(f"{command}: not found")
        else:
            print(f"{command}: not found")


if __name__ == "__main__":
    main()
