# 1) cd,
# 2)remove kakoy to directory
# 3)gde ya
# 4)end, finishes the code
import os

while True:
    command = input()

    if command == 'end':
        break
    elif command == 'cd':
        kuda = input()
        if os.path.isdir(kuda) and os.path.exists(kuda):
            os.chdir(kuda)
            print("Done")
        else:
            print("Not a directory")
    elif command == 'gde':
        print(f'The current directory is: [{os.getcwd()}]')
    elif command == 'remove':
        x = input()
        if os.path.exists(x):
            os.rmdir(x)
        else:
            print('Error')
        

    
