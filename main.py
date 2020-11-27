import rotatescreen
import keyboard
import time

screen = rotatescreen.get_primary_display()
start_pos = screen.current_orientation

def rotateByKeyboardKey():
    try:
        keyboard.add_hotkey('ctrl+alt+up', screen.set_landscape, suppress=True)
        keyboard.add_hotkey('ctrl+alt+right', screen.set_portrait_flipped, suppress=True)
        keyboard.add_hotkey('ctrl+alt+down', screen.set_landscape_flipped, suppress=True)
        keyboard.add_hotkey('ctrl+alt+left', screen.set_portrait, suppress=True)

        keyboard.wait()
    except:
        print("Process Terminated")
    

def BarrelRoll(n):
    for i in range(n):
        pos = abs((i*90) % 360)
        screen.rotate_to(pos)
        time.sleep(2)


def main():
    quit = False
    while(quit == False):
        choice = int(input("1] Barrel Roll\n2] Flip the screen\nWhich one u want to try: "))
        if choice == 1:
            BarrelRoll(int(input("Enter the number of times u want to roll: ")))
        elif choice == 2:
            print("Press ctrl + alt + arrow keys to flip your screen accordingly\n")
            print("Press ctrl+C to ternimate the process")
            rotateByKeyboardKey()
        else:
            print("Invalid Input")
        
        if input("Do you want to quit?(y/n): ").lower() == 'y':
            quit = True


if __name__ == "__main__":
    main()
    