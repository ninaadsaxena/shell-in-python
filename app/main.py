import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
    
    # Wait for user input
    #command = input()
        user_input = input()
    #print(f"{command}: command not found")
    #main()
        if user_input == "exit 0":
            break
        sys.stdout.write(f"{user_input}: not found\n")


if __name__ == "__main__":
    main()
