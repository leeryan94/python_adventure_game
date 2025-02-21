import os, time, random, sys

os.system("cls" if os.name == "nt" else "clear")

dev_levelskip = 0

current_level = 0
slow_message_interval = 4
message_interval = 1
fast_message_interval = 0.5

character_name = "Placeholder Peter"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_typewriter(story):
    word_interval = 0.15  
    comma_interval = 0.5  
    sentence_interval = 1.0  

    for paragraph in story:
        words = paragraph.split()  
        for i, word in enumerate(words):
            
            if word.endswith(","):
                print(f"{word}", end=' ', flush=True)
                time.sleep(comma_interval)
            elif word.endswith(".") or word.endswith("!"):
                print(f"{word}", end=' ', flush=True)
                time.sleep(sentence_interval)
            else:
                print(f"{word}", end=' ', flush=True)
                time.sleep(word_interval)
        print()  

def death_screen():
    clear_screen()
    global current_level
    
    RED = '\033[31m'
    RESET = '\033[0m'

    ascii_art = '''
                                ,-.
           ___,---.__          /'|`\          __,---,___
        ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
    ,'        |           ~'\     /`~           |        `.
    /      ___//              `. ,'          ,  , \___      -
    |    ,-'   `-.__   _         |        ,    __,-'   `-.    |
    |   /          /\_  `   .    |    ,      _/\          \   |
    \  |           \ \`-.___ \   |   / ___,-'/ /           |  /
    \  \           | `._   `\\  |  //'   _,' |           /  /
    `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
        ``       /     \    ,='/ \`=.    /     \       ''
                |__   /|\_,--.,-.--,--._/|\   __| 
                /  `./  \\`\ |  |  | /,//' \,'  -
            /   /     ||--+--|--+-/-|     \   -
            |   |     /'\_\_\ | /_/_/`\     |   |
             \  \   \__, \_     `~'     _/ .__/   /
                `-._,-'   `-._______,-'   `-._,-'

    ██╗   ██╗ ██████╗ ██╗   ██╗     █████╗ ██████╗ ███████╗
    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██╔══██╗██╔════╝
    ╚████╔╝ ██║   ██║██║   ██║    ███████║██████╔╝█████╗  
    ╚██╔╝  ██║   ██║██║   ██║    ██╔══██║██╔══██╗██╔══╝  
    ██║   ╚██████╔╝╚██████╔╝    ██║  ██║██║  ██║███████╗
    ╚═╝    ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                                        
    ██████╗ ███████╗ █████╗ ██████╗                        
    ██╔══██╗██╔════╝██╔══██╗██╔══██╗                       
    ██║  ██║█████╗  ███████║██║  ██║                       
    ██║  ██║██╔══╝  ██╔══██║██║  ██║                       
    ██████╔╝███████╗██║  ██║██████╔╝                       
    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝        
    '''

    def print_slow(text, delay=0.005):
        for char in text:
            sys.stdout.write(RED + char + RESET) 
            sys.stdout.flush()  
            time.sleep(delay)  

    print_slow(ascii_art)

    time.sleep(1)

    if current_level == 0:
        print(f"\nYou are returning to the very beginning...")
        time.sleep(slow_message_interval)
        clear_screen()
        level_intro()
    elif current_level == 1:
        print(f"\nYou are returning to Level 1")
        time.sleep(slow_message_interval)
        clear_screen()
        level_one()
    elif current_level == 2:
        print(f"\nYou are returning to Level 2")
        time.sleep(slow_message_interval)
        clear_screen()
        level_two()
    elif current_level == 3:
        print(f"\nYou are returning to Level 3")
        time.sleep(slow_message_interval)
        clear_screen()
        level_three()
    elif current_level == 4:
        print(f"\nYou are returning to Level 4")
        time.sleep(slow_message_interval)
        clear_screen()
        level_four()
    elif current_level == 5:
        print(f"\nYou are returning to Level 5")
        time.sleep(slow_message_interval)
        clear_screen()
        level_five()

def player_victory_epilogue():
    clear_screen()
    def level_ascii():
        print("\033[38;5;160m")
        print("   ▄▄▄▄▄   ████▄   ▄   █                             ")
        print("  █     ▀▄ █   █    █  █                             ")
        print("▄  ▀▀▀▀▄   █   █ █   █ █                             ")
        print(" ▀▄▄▄▄▀    ▀████ █   █ ███▄                          ")
        print("                 █▄ ▄█     ▀                         ")
        print("                  ▀▀▀                                ")
        print("                                                     ")
        print("█▄▄▄▄ ▄███▄   ▄█▄    █    ██   ▄█ █▀▄▀█ ▄███▄   █▄▄▄▄")
        print("█  ▄▀ █▀   ▀  █▀ ▀▄  █    █ █  ██ █ █ █ █▀   ▀  █  ▄▀")
        print("█▀▀▌  ██▄▄    █   ▀  █    █▄▄█ ██ █ ▄ █ ██▄▄    █▀▀▌ ")
        print("█  █  █▄   ▄▀ █▄  ▄▀ ███▄ █  █ ▐█ █   █ █▄   ▄▀ █  █ ")
        print("  █   ▀███▀   ▀███▀      ▀   █  ▐    █  ▀███▀     █  ")
        print(" ▀                          █       ▀            ▀   ")
        print("                           ▀                         ")
        print("\033[0m")
        
        time.sleep(slow_message_interval)
    level_ascii()

    dialogue_1 = [
        "Exhausted and relieved, you collapse onto the floor of the creaking elevator.",
        "The journey back to the mundane world feels like an eternity.",
        "",
        "As the elevator lurches to a halt, the rusted doors groan open.",
        "You step out into the familiar, if slightly eerie, confessional booth.",
        "The curtain slides shut, and the familiar, chilling voice echoes through the darkness.",
        "But this time, the mysterious figure steps forth - into the rays of the stained glass sun; reflecting off it's scythe.",
        "That mysterious voice is none other than the Grim Reaper itself.",
        "",
        "Grim Reaper: A reckless gamble, a fateful throw, A soul's surrender, a mournful woe.",
        "The house's triumph, a chilling sight, Eternal darkness, a haunting night.",
        "So learn your lesson, heed the sign, Or face the reaper, lost in time."
    ]
    print_typewriter(dialogue_1)

    time.sleep(slow_message_interval)
    clear_screen()

    dialogue_2 = [
        "A chill runs down your spine as the voice fades.",
        "You bolt from the confessional, only to find the elevator gone.",
        "The once pristine cathedral is now a crumbling ruin.",
        "With a sense of urgency, you flee the crumbling structure, never looking back."
    ]

    print_typewriter(dialogue_2)
    time.sleep(slow_message_interval)
    clear_screen()
    
    final_message = [
        f"{character_name}: I'm never drinking again."
    ]

    print_typewriter(final_message)
    sys.exit()

def hellhound():
    global current_level
    clear_screen()

    def hound():
        print("\n")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠉⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠜⠀⠈⣷⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠾⠛⠁⠀⠀⠀⣿⠀⠀⠀⠀⣠⡶⢟⠁⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠟⠁⠀⠀⠀⠀⠀⠀⣿⠀⣀⣴⠞⠋⡰⠋⠀⠀⠀⠀⣠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⠋⠀⠀⠀⠀⠀⠀⠀⢀⣴⣷⠾⠋⠁⢀⡞⠁⠀⠀⠀⠀⢠⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⠋⠁⠀⠀⠀⠀⠀⠀⣠⣴⡶⠛⠉⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⢸⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⡤⠴⠖⠒⠚⠛⠉⠉⠙⠛⠒⠲⢤⣄⣤⡶⠛⠉⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⢸⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⣴⠤⠶⠶⠶⠦⠤⣤⣄⣀⣀⣀⣀⣾⠉⣡⠴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⡎⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠈⢉⣡⡤⠟⠛⠳⢤⡀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣄⠀⠀⠀⠀⠀⠀⣰⠇⣠⡴⠀⠀⠀⠀⡸⠃⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⣠⣿⣄⣠⣖⣲⣦⡤⠇⠀⠀⠀⠀⠀⠀⢀⣤⠤⠭⣵⣒⢶⣺⣷⢊⣟⣦⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠶⠶⠶⠾⠛⠻⠿⣮⣁⠀⠀⠰⢁⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⢻⣤⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠤⠤⠤⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⢠⣿⡙⢶⣄⡀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠈⠓⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣶⣵⠾⠋⢳⣶⣄⣀⠀⠀⠀⠀⠀⠀⠀")
        print("⡞⢿⡉⢿⣾⠟⢯⣙⣲⣶⢤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣾⣿⠾⣟⡉⠀⠀⠀⠀⠈⠿⢿⣶⠄⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⡇⡞⠉⢻⣿⢀⠞⣇⢿⣩⣟⢻⡛⣿⢿⢿⣿⣷⣦⣄⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣦⡀⠙⢦⠀⠀⠀⠀⠀⠈⠻⣿⣆⠀⠀⠀⠀⣴⡗⠀⠀")
        print("⢻⡇⠀⠀⢿⣸⠀⠈⠀⠁⠈⠛⠿⠻⣏⢦⠶⢧⣙⢙⣧⡀⢀⠀⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣜⣿⣆⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⣤⣠⠞⣽⢀⣰⠀")
        print("⠀⠁⠀⠀⠘⢿⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⡀⠀⢉⣿⠾⡇⠈⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⡀⠀⠹⡍⠁⠀⣠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠈⢻⣦⡷⠋⡟⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⡾⠋⢀⣠⡇⠀⠈⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⠀⢀⣀⣙⣷⡦⡷⠀⡞⠁⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠀⢀⡾⠋⠀⣾⠁⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⣤⣼⣹⠟⠀⣀⠼⠃⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⣰⠋⠀⠀⠀⠀⠀⢸⠏⠀⠀⠀⠀⠀⣠⡾⠏⠀⢀⡤⠛⢹⠋⠋⢁⣿⠋⠉")
        print("⠀⠀⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⣤⣯⡽⠋⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠚⠁⣠⡜⠁⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⢀⣠⡾⠋⠁⠀⠐⣏⠀⢠⡏⠀⢀⡾⠋⠀⠀")
        print("⠀⠀⠀⠀⣿⡇⢸⣆⠀⠀⣰⣿⣄⢸⢦⡷⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⢀⣠⡾⠋⠀⠀⠀⠀⢸⠋⠉⣿⠛⠋⢀⣴⢟⣁⢤⡤")
        print("⠀⠀⠀⠀⢹⣽⣾⡜⢶⣾⠳⣿⣨⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠤⠤⠖⠁⠀⠠⠤⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⢁⣨⠟⠛⢉⡿⡷⠾⠗")
        print("⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")

    def hound_bone():
        print("""⠀ ⣠⡴⠞⠛⠛⠲⢤⡀⢀⠤⢶⣄⠀⠀⠀⠀ 
        ⠀⠀⠀⠀⢀⡴⠶⣄⢠⠞⠁⠀⠀⠀⠀⠀⠀⠙⠋⢰⠀⠈⠢⢤⡀⠀
        ⠀⠠⡶⠚⠉⠀⣖⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡄⠀⠀⠀⠈⢆
        ⠀⠀⡆⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⣧⠀⠀⠀⠀⡾
        ⠀⠀⣧⠀⠀⠀⠈⣷⠀⣠⣖⢦⠀⠀⠀⠀⢰⠓⡍⢧⢻⣧⠀⣠⠚⠀
        ⠀⠀⠸⣆⠀⠀⠀⢹⠀⣧⣨⡆⡇⠀⠀⠀⠸⣷⡇⡸⠀⡏⠉⠀⠀⠀
        ⠀⠀⠀⠈⠳⣄⢀⣧⡀⢻⣿⡡⠁⠀⠀⠀⠀⠙⠒⠣⣜⣀⢀⡀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠉⡀⠙⣶⡬⠀⠀⢠⣾⡟⠛⢻⠀⠀⢸⠁⠀⠙⠄⠀
        ⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⢳⣄⠀⠈⠿⢿⣒⣋⣀⣴⠇⠀⠀⠼⡀⠀
        ⠀⠀⠀⠀⢀⠤⠴⣧⣀⠀⠀⠉⠉⠉⠉⠉⠁⠈⠉⣁⣀⠀⠀⠀⢸⠀
        ⠀⠀⠀⢠⠃⠀⠀⠈⣇⠀⠀⢀⣤⡶⡶⢶⠛⠋⠉⠉⠉⠷⣤⡤⠂⠀
        ⠸⡄⠀⢸⡆⠀⠀⠀⠹⣷⣾⠟⠃⠀⡇⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠰⡘⢤⣀⣿⡄⠀⠀⢠⡿⠧⣴⠀⠀⣷⡈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠙⠲⠤⠭⣥⣤⣤⢽⣤⣶⣸⣤⣰⣌⣼⠾⠼⠀⠀⠀⠀⠀⠀⠀⠀
        """)
    hellhound_dialogue = [
        "After besting Satan in a heated game of Crucifix, Salt, Holy Water, you navigate through the chaotic backstage of the hellish rock concert.",
        "The endless corridors twist and turn until you stumble upon a door marked 'Fire Exit'.",
        "Curiosity—or perhaps desperation—drives you to push it open.",
        "",
        "Inside, you find yourself in a dimly lit room filled with slumbering hellhounds, their fiery breaths casting flickering shadows on the walls.",
        "Just beyond them, you spot an open passage leading to a decaying elevator.",
        "With no other way forward, you carefully consider your options to get past the hounds.",
        "",
        "You have two choices:"
    ]
    print_typewriter(hellhound_dialogue)
    hellhound_choices = [
        "1. **Stealth Approach** - Crouch and move silently through the room, hoping not to disturb the hounds.",
        "2. **Distraction Tactic** - Look for an item to throw and create a diversion, drawing the hounds' attention elsewhere."
    ]
    for hc in hellhound_choices:
        print(hc)
        time.sleep(message_interval)
    
    choice = input("\nHow do you proceed? Type '1' for Stealth or '2' for Distraction: ").strip()
    
    if choice == '1':
        hc_1 = [
            "You choose the stealth approach. You crouch low and take slow, deliberate steps, avoiding any debris that might make noise.",
            ". . ."
        ]

        print_typewriter(hc_1)
        
        roll = random.randint(1, 6)
        if roll >= 4:
            print_typewriter(["You manage to slip past the hellhounds without a sound! You reach the elevator safely."])
            time.sleep(slow_message_interval)
            current_level = 100
            player_victory_epilogue()
        else:
            hound()
            print_typewriter(["The floor creaks under your weight. One of the hellhounds stirs and spots you!"])
            print_typewriter(["With a growl, the hounds pounce and tear you apart. Game over!"])
            time.sleep(slow_message_interval)
            current_level = 0
            death_screen()
    
    elif choice == '2':
        print("")
        print_typewriter(["You choose to create a distraction. You scan the room and spot four boxes nearby."])
        print_typewriter(["Maybe one of the boxes contains something inside that you can use?"])
        print_typewriter(["However, rustling the wrong box might wake them, and you’ll be ripped to pieces. Choose wisely!"])
        print("")
        
        bone_box = random.randint(1, 4)
        bone_box_2 = random.randint(1, 4)
        while True:
            if bone_box == bone_box_2:
                bone_box_2 = random.randint(1, 4)
            else:
                break
        
        box_choice = int(input("\nWhich box do you check? Choose a number between 1 and 4: ").strip())
        
        if box_choice == bone_box or box_choice == bone_box_2:
            print("")
            hound_bone()
            print_typewriter(["\nYou open the box and find a bone inside! Carefully, you toss it across the room."])
            print_typewriter(["The hounds stir and move towards the sound, giving you a clear path to the staircase."])
            time.sleep(slow_message_interval)
            current_level = 100
            player_victory_epilogue()
        else:
            hound()
            print_typewriter(["\nYou rustle the box, but it’s empty. The noise wakes the hellhounds."])
            print_typewriter(["Their fiery eyes snap open, and within moments, they tear you apart. Game over!"])
            time.sleep(slow_message_interval)
            current_level = 0
            death_screen()
    else:
        print("")
        hound()
        print_typewriter(["\nInvalid choice. The hellhounds wake up from your hesitation, and you become their next snack. Game over!"])
        time.sleep(slow_message_interval)
        current_level = 0
        death_screen()

def alternate_ending():
    clear_screen()

    def level_ascii():
        print("\033[38;5;160m")
        print("██▄   ▄███▄   ██   █     ▄███▄   █▄▄▄▄     ████▄ ▄████ ")
        print("█  █  █▀   ▀  █ █  █     █▀   ▀  █  ▄▀     █   █ █▀   ▀")
        print("█   █ ██▄▄    █▄▄█ █     ██▄▄    █▀▀▌      █   █ █▀▀   ")
        print("█  █  █▄   ▄▀ █  █ ███▄  █▄   ▄▀ █  █      ▀████ █     ")
        print("███▀  ▀███▀      █     ▀ ▀███▀     █              █    ")
        print("                █                 ▀                ▀   ")
        print("               ▀                                        ")
        print("▄███▄     ▄▄▄▄▀ ▄███▄   █▄▄▄▄   ▄   ▄█    ▄▄▄▄▀ ▀▄    ▄")
        print("█▀   ▀ ▀▀▀ █    █▀   ▀  █  ▄▀    █  ██ ▀▀▀ █      █  █ ")
        print("██▄▄       █    ██▄▄    █▀▀▌ ██   █ ██     █       ▀█  ")
        print("█▄   ▄▀   █     █▄   ▄▀ █  █ █ █  █ ▐█    █        █   ")
        print("▀███▀    ▀      ▀███▀     █  █  █ █  ▐   ▀       ▄▀    ")
        print("                         ▀   █   ██                    ")


        print("\033[0m")
        
        time.sleep(slow_message_interval)
    level_ascii()


    intro_text = [
        "After losing to Satan in a fateful game of Crucifix, Salt, Holy Water, you find yourself beginning your first week in the eternal fires of Hell.",
        "",
        "Your new job? Training to become a dice dealer at the Casino of the Damned.",
        "",
        "Dressed in your new, pristine dealer’s suit, you stand at the table, eyes cold yet calculating. The room hums with the low murmur of lost souls.",
        "You call to the unfortunate mortals — in an identical position as you were a week ago, lost and desperate.",
        "They shuffle forward, trembling, to roll the dice and face the whims of fate.",
        "",
        "Here, an eternity is determined with each throw."
    ]

    print_typewriter(intro_text)
    print("")

    dealer_dialogue = [
        f"{character_name}: Step forward, mortals.",
        "This game is simple: beat my hand, and you'll win a chip—redeemable at the cashier’s desk.",
        "But lose... and your soul will be harvested right here, for all eternity!"
    ]

    print_typewriter(dealer_dialogue)

    def roll_dice():
        return random.randint(1, 6)

    def player_roll():
        dice_roll = roll_dice()
        dealer_roll = roll_dice()

        print(f"\nYou rolled: {dealer_roll} | Unfortunate Player: {dice_roll}")

        if dealer_roll >= dice_roll:
            player_vic = [
                "The dice roll across the table and land with a clatter, and you beat the unfortunate playera roll!"
            ]
            print_typewriter(player_vic)
            return False
        else:
            npc_vic = [
                "The dice roll across the table and land with a clatter.",
                "You lost to the unfortunate players roll."
            ]
            print_typewriter(npc_vic)
            return True

    def play_game():
        attempts = 0
        max_attempts = 3
        while attempts < max_attempts:
            print(f"\nAttempt {attempts + 1} of {max_attempts}:")
            if player_roll():
                return True
            attempts += 1
        return False

    def main_game_loop():
        while True:
            time.sleep(message_interval)
            clear_screen()
            print("")
            print_typewriter(["A new player approaches the table..."])
            print("\nWhat will you do?\n")
            print("   1. Roll the dice.")

            choice = input("\nEnter 1: ").strip()

            if choice == "1":
                if play_game():
                    choice_1 = [
                        "The demons around the table groan in disappointment, their hopes dashed.",
                        "You smirk at the lucky player, envious at his win, but happy for him.",
                        "You slide a chip across the table."
                    ]
                    choice_1_b = [
                        "'Well done, now get yourself out of here.' You say to the lucky player.",
                        "",
                        "Right, who's next?"
                    ]
                    print_typewriter(choice_1)
                    print("")
                    print_typewriter(choice_1_b)
                else:
                    choice_else = [
                        "The unfortunate player has used all 3 attempts and failed to beat you.",
                        "The demons laugh cruelly.",
                        "",
                        "The demons feast on the player's soul...",
                        "",
                        "'Another soul claimed,' you mutter, waiting for the next unfortunate soul to roll the dice."
                    ]
                    print_typewriter(choice_else)

                time.sleep(message_interval)

    main_game_loop()

def level_five():
    clear_screen()

    def level_ascii():
        print("\033[38;5;160m")
        print("   ▄▄▄▄▀ ▄  █ ▄███▄       ▄████  ▄█    ▄   ██   █    ")
        print("▀▀▀ █   █   █ █▀   ▀      █▀   ▀ ██     █  █ █  █    ")
        print("    █   ██▀▀█ ██▄▄        █▀▀    ██ ██   █ █▄▄█ █    ")
        print("   █    █   █ █▄   ▄▀     █      ▐█ █ █  █ █  █ ███▄ ")
        print("  ▀        █  ▀███▀        █      ▐ █  █ █    █     ▀")
        print("          ▀                 ▀       █   ██   █       ")
        print("                                            ▀        ")
        print("███   ████▄    ▄▄▄▄▄    ▄▄▄▄▄                        ")
        print("█  █  █   █   █     ▀▄ █     ▀▄                      ")
        print("█ ▀ ▄ █   █ ▄  ▀▀▀▀▄ ▄  ▀▀▀▀▄                        ")
        print("█  ▄▀ ▀████  ▀▄▄▄▄▀   ▀▄▄▄▄▀                         ")
        print("███                                                 ")
        print("\033[0m")

        time.sleep(slow_message_interval)
    level_ascii()

    global current_level
    def l5_create_deck():
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
        random.shuffle(deck) 
        return deck
    
    def l5_calculate_hand_value(hand):
        value = 0
        aces = 0
        for card in hand:
            if card['rank'].isdigit():
                value += int(card['rank'])
            elif card['rank'] in ['Jack', 'Queen', 'King']:
                value += 10
            elif card['rank'] == 'Ace':
                value += 11
                aces += 1
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value
    
    def display_hand(hand, owner):
        print(f"{owner}'s hand:")
        for card in hand:
            print(f"  {card['rank']} of {card['suit']}")
        print(f"Total value: {l5_calculate_hand_value(hand)}\n")

    def blackjack():
        global current_level
        blackjack_intro_dialogue = [
            "The elevator screeches to a halt, its rusted doors groaning open.",
            "Before you stands a sight that chills you to the bone:",
            "Satan himself, lounging at a blackjack table, a smirk playing on his lips.",
            "",
            f"\033[91mSatan: Ahhh, mortal... {character_name}! Come take a seat. So, you've made it to the final stage.\033[0m ",
            "\033[91mYour contract says you were awarded a winning streak in place of a losing streak at a casino.\033[0m",
            "\033[91mLet's see if we can change that.\033[0m",
            "",
            "\033[91mSatan: Win two games out of three, and I'll rip up the contract, setting you free. Lose, and you're mine for eternity.\033[0m"
        ]

        print_typewriter(blackjack_intro_dialogue)

        player_wins = 0
        satan_wins = 0

        for round_number in range(1, 4):  # Max 3 rounds, but ends early if someone wins twice.
            print(f"\nRound {round_number} of 3\n")

            deck = l5_create_deck()
            player_hand = [deck.pop(), deck.pop()]
            dealer_hand = [deck.pop(), deck.pop()]

            l5_card_slide = [
                "Satan slides two cards across the table, their faces hidden. He then deals himself two cards."
            ]
            print_typewriter(l5_card_slide)

            
            while True:
                display_hand(player_hand, character_name)
                player_value = l5_calculate_hand_value(player_hand)
                if player_value > 21:  
                    print(f"\nSatan: \"\033[91mOh, look at that! {character_name}, you bust! This round is mine.\033[0m\"\n")
                    satan_wins += 1
                    break
                move = input("Do you want to (H)it or (S)tand? ").lower()
                if move == 'h':
                    player_hand.append(deck.pop())
                elif move == 's':
                    break

            
            if l5_calculate_hand_value(player_hand) <= 21:
                print("\nSatan takes his turn.")
                while l5_calculate_hand_value(dealer_hand) < 17:
                    dealer_hand.append(deck.pop())

            
            display_hand(player_hand, character_name)
            display_hand(dealer_hand, "Satan")

            
            player_value = l5_calculate_hand_value(player_hand)
            dealer_value = l5_calculate_hand_value(dealer_hand)

            if dealer_value > 21 or (player_value <= 21 and player_value > dealer_value):
                print_typewriter([f"\033[91mSatan: Hmm, well played, {character_name}. A step closer to freedom.\033[0m"])
                player_wins += 1
            elif player_value < dealer_value or player_value > 21:
                print_typewriter([f"\033[91mSatan: Haha! Another loss, {character_name}.\033[0m"])
                satan_wins += 1
            else:
                print_typewriter([f"\033[91mSatan: A tie? How boring, {character_name}. A tie is as good as a loss here!\033[0m"])
                satan_wins += 1

            if player_wins == 2:
                print_typewriter([
                    f"\033[91mSatan: No! Your winning streak continues, {character_name}! The contract is void. You're free to go.\033[0m",
                    "With a sharp motion, he gestures with his clawed hand toward an ancient, creaking elevator—eerily similar to the one that brought you here.", 
                    "His fiery eyes bore into you, his patience wearing thin.", 
                    "The oppressive heat of his glare presses down on you as you step into the rickety elevator. You leave the tormenting flames of Hell behind."
                ])
                time.sleep(slow_message_interval)
                player_victory_epilogue()
                return
            elif satan_wins == 2:
                print_typewriter([
                    f"\033[91mSatan: Haha! I've won, {character_name}. The contract is sealed. You are mine for eternity!\033[0m]",
                    "Satan places your contract at the top of his collection."
                ])
                time.sleep(slow_message_interval)
                current_level = 0
                death_screen()
                return

        if player_wins > satan_wins:
            print_typewriter([
                f"\033[91mSatan: No! You've beaten me, {character_name}! The contract is void. You're free to go.\033[0m"
            ])
            time.sleep(slow_message_interval)
            player_victory_epilogue()
        else:
            print_typewriter([
                f"\033[91mSatan: Haha! I've won, {character_name}. The contract is sealed. You are mine for eternity!\033[0m"
            ])
            current_level = 0
            death_screen()

    if __name__ == "__main__":
        blackjack()

def level_four():
    clear_screen()
    def level_ascii():
        print("\033[38;5;160m")
        print("    ▄▄▄▄▀ ▄  █ ▄███▄     ")
        print(" ▀▀▀ █   █   █ █▀   ▀    ")
        print("     █   ██▀▀█ ██▄▄      ")
        print("    █    █   █ █▄   ▄▀   ")
        print("   ▀        █  ▀███▀     ")

        print(" ▄████  ████▄ █▄▄▄▄ ███   ▄█ ██▄   ██▄   ▄███▄      ▄       ")
        print(" █▀   ▀ █   █ █  ▄▀ █  █  ██ █  █  █  █  █▀   ▀      █      ")
        print(" █▀▀    █   █ █▀▀▌  █ ▀ ▄ ██ █   █ █   █ ██▄▄    ██   █     ")
        print(" █      ▀████ █  █  █  ▄▀ ▐█ █  █  █  █  █▄   ▄▀ █ █  █     ")
        print("  █             █   ███    ▐ ███▀  ███▀  ▀███▀   █  █ █     ")
        print("   ▀           ▀                                 █   ██     ")

        print("█  █▀   ▄   ████▄         █     ▄███▄   ██▄     ▄▀  ▄███▄   ")
        print("█▄█      █  █   █  █   █  █     █▀   ▀  █  █  ▄▀    █▀   ▀  ")
        print("█▀▄  ██   █ █   █ █  ▄  █ █     ██▄▄    █   █ █ ▀▄  ██▄▄    ")
        print("█  █ █ █  █ ▀████ █  █  █ ███▄▀ █▄   ▄▀ █  █  █   █ █▄   ▄▀ ")
        print("  █  █  █ █        █ █ █        ▀███▀   ███▀   ███  ▀███▀   ")
        print(" ▀   █   ██         ▀ ▀                                     ")
        print("\033[0m")

        time.sleep(slow_message_interval)
    level_ascii()

    global current_level

    def l4_ask_question(question, options, correct_answer):
        print(question)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        try:
            answer = int(input("Please select the number of your answer: "))
            if answer == correct_answer:
                print("Correct!\n")
                return True  
            else:
                print("Incorrect. Game Over.\n")
                return False
        except ValueError:
            print("Invalid input. Please enter a number corresponding to your choice.\n")
            return False  


    l4_narr = [
        "You navigate the labyrinthine corridors, the muffled whispers of unseen voices echoing through the darkness.",
        "",
        "As you emerge from the final curtain, a blinding spotlight illuminates the stage.",
        "The cheers of a hidden audience fill the air, their applause echoing in your ears. ",
        "Two elegant chairs face each other in the centre of the stage. ",
        "",
        "A sharply dressed man, a sinister smile playing on his lips, strides onto the stage, his presence commanding attention."
    ]

    print_typewriter(l4_narr)
    print("")
    time.sleep(message_interval)

    l4_dialogue = [
        "Presenter: Welcome, everyone, to another thrilling round of Forbidden Knowledge!",
        "Our contestants will face a series of challenging questions.",
        "",
        "Presenter: Answer correctly, and earn the final key to reclaim their souls.",
        "Fail, and one of you lucky audience members will claim the soul of the unfortunate contestant. Let the games begin!",
        "",
        "[The audience erupts into cheer]",
        "",
        f"Presenter: Now today we have {character_name} taking the seat, please {character_name}, take a seat and let's begin.",
        "",
        "You take your seat, a wave of nervousness washing over you.",
        "The spotlight narrows, focusing on you and the host.",
        "The once-raucous audience falls silent, anticipation hanging heavy in the air.",
        "As the dim light settles, you brace yourself for the first question."
    ]

    print_typewriter(l4_dialogue)

    print("")

    questions = [
        {
            "question": "What is the colour often associated with the Devil?",
            "options": ["White", "Blue", "Red", "Green"],
            "correct_answer": 3
        },
        {
            "question": "What is a common symbol of evil?",
            "options": ["A dove", "A skull", "A heart", "A rainbow"],
            "correct_answer": 2
        },
        {
            "question": "What is the name of the creature that guards the gates of Hell in Dante's Inferno?",
            "options": ["Minotaur", "Cerberus", "Hydra", "Chimera"],
            "correct_answer": 2
        }
    ]

    all_correct = True

    for q in questions:
        if not l4_ask_question(q["question"], q["options"], q["correct_answer"]):
            all_correct = False
            break 
    if all_correct:
        ending_dialogue = [
            "The audience boos, their disappointment palpable.",
            "The presenter, visibly deflated, apologises to the crowd.",
            "",
            "Presenter: Well, that's the end of this round. Perhaps next time, one of you lucky audience members will claim a soul.",
            "Until then, let's hope for a more exciting match.",
            "",
            "Turning to you, the presenter offers a forced smile.",
            "",
            "Congratulations on your win. Now, to your final level. Step into the elevator, and may fortune favour you.",
            "",
            "With a final, ominous glance, he gestures towards the antique elevator, its rusted cage looming in the dim light.",
            "You step inside, the heavy door clanging shut behind you. As the elevator descends into the darkness, a sense of dread washes over you."
        ]

        print_typewriter(ending_dialogue)
        input("\nPress Enter to go to Level 5")
        current_level = 5
        level_five()

    else:
        ending_dialogue = [
            "The audience erupts in cheers, their anticipation palpable.",
            "The presenter, grinning widely, makes an annonucement...",
            "",
            "Presenter: It's time for one of you lucky audience members to claim your prize!",
            "",
            " A spotlight darts around the crowd, finally settling on a small, mischievous demon girl. ",
            "The bowtie cresting her tiny little horns jiggling alongside her excitement.",
            "She bounds onto the stage, her eyes sparkling with excitement.",
            "With a mischievous grin, she clamps a heavy shackle around your neck and drags you off stage, your fate sealed."
        ]

        print_typewriter(ending_dialogue)
        time.sleep(slow_message_interval)
        death_screen()

def level_satan_duel():
    clear_screen()

    def level_ascii():
        print("\033[38;5;160m")
        print("██▄   ▄███▄      ▄   ▄█ █      ▄▄▄▄▄       ██▄     ▄   ▄███▄   █    ")
        print("█  █  █▀   ▀      █  ██ █     █     ▀▄     █  █     █  █▀   ▀  █    ")
        print("█   █ ██▄▄   █     █ ██ █   ▄  ▀▀▀▀▄       █   █ █   █ ██▄▄    █    ")
        print("█  █  █▄   ▄▀ █    █ ▐█ ███▄ ▀▄▄▄▄▀        █  █  █   █ █▄   ▄▀ ███▄ ")
        print("███▀  ▀███▀    █  █   ▐     ▀              ███▀  █▄ ▄█ ▀███▀       ▀")
        print("                █▐                                ▀▀▀               ")
        print("                ▐                                                   ")

        print("\033[0m")
        
        time.sleep(slow_message_interval)
    level_ascii()

    global current_level
    def c_s_hw():
        global current_level
        clear_screen()
        intro_narr = [
            "The room is dead silent for a moment, save for the distant echo of dripping sulphur.",
            "Then Satan throws his head back and lets out a thunderous laugh that shakes the walls.",
            "",
            "\033[91mSatan: You’d play a game against me? *Me*? You’ve got guts, mortal, I’ll give you that.\033[0m",
            "\033[91mBut you’ll need more than guts to leave here intact.\033[0m",
            "",
            "He leans in close, his fiery eyes boring into yours.",
            "",
            "\033[91mSatan: Tell me something. When you lose — and you will —\033[0m ",
            "\033[91mdo you plan to seek help for your *gambling problem* up there?\033[0m",
            "\033[91mOh wait. You won’t, because I’ll be keeping you right here.\033[0m",
            "",
            "The crowd erupts into wicked laughter, some demons clutching their sides, others jeering with malicious glee.",
            "",
            f"{character_name}: Alright, fine! What are the rules to this ga-",
            "",
            "Before you’ve even finished asking, Satan throws his arms out theatrically,",
            "and the crowd roars again, this time louder, the sound nearly deafening.",
            "",
            "\033[91mSatan: Rules? *Rules?!* This is Hell, mortal. Did you think you’d get a fair fight?\033[0m",
            "",
            "Another wave of laughter ripples through the crowd, demons banging their fists on the walls or stomping the floor.",
            "",
            "\033[91mSatan: You don’t get to ask questions. You just *play*. And when you lose, you’ll wish you’d stayed in that elevator.\033[0m",
            "",
            "Satan steps back to his makeshift podium, flames erupting around him.",
            "A glowing table appears between you and him, etched with unholy runes and symbols.",
            "",
            "\033[91mSatan: Prepare yourself for Crucifix, Salt, Holy Water!\033[0m",
            "",
            "He raises his hands, and the crowd falls eerily silent.",
            "",
            "\033[91mSatan: Let’s begin. Choose wisely, mortal... not that it matters.\033[0m"
        ]

        print_typewriter(intro_narr)

        player_wins = 0
        satan_wins = 0
        moves = {1: "Crucifix", 2: "Salt", 3: "Holy Water"}

        def choices():
            print("\nChoose your move: \n")
            cshw_choices = [
                "   1. Crucifix",
                "   2. Salt",
                "   3. Holy Water"
            ]
            for choice in cshw_choices:
                print(choice)
                time.sleep(message_interval)

        def determine_winner(player, satan):
            if player == satan:
                return "satan"  # Satan wins on a draw
            elif (player == 1 and satan == 3) or (player == 2 and satan == 1) or (player == 3 and satan == 2):
                return "player"
            else:
                return "satan"

        while player_wins < 2 and satan_wins < 2:
            choices()
            try:
                player_choice = int(input("\nEnter your move (1, 2, or 3): "))
                if player_choice not in [1, 2, 3]:
                    print("Invalid choice. Choose 1, 2, or 3.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            satan_choice = random.randint(1, 3)
            print(f"\nYou chose {moves[player_choice]}. Satan chose {moves[satan_choice]}.")

            result = determine_winner(player_choice, satan_choice)
            if result == "player":
                player_wins += 1
                print_typewriter(["\033[91mSatan: What?? No! You win this round? How!\033[0m"])
            elif result == "satan":
                satan_wins += 1
                if player_choice == satan_choice:  
                    print_typewriter(["\033[91mSatan: *Draw?* Did you forget where you are? In Hell, *I* win draws.\033[0m"])
                else:
                    print_typewriter(["\033[91mSatan: HAHAHAA! Your eternal fate is one step closer.\033[0m"])
            print(f"Score: {character_name} {player_wins} - {satan_wins} Satan")

        if player_wins == 2:
            player_vic = [
                "The crowd falls silent as you claim victory. Satan scowls, flames flickering from his nostrils.",
                "",
                "\033[91Satan: *Impossible!* No mortal has ever beaten me!\033[0m",
                "",
                "Satan vanishes in a puff of smoke, leaving the crowd of demons silent... and stunned.",
                "Mouths agape, their eyes follow you as you slowly creep your way backstage."
            ]

            print_typewriter(player_vic)
            time.sleep(message_interval)
            current_level = 11
            hellhound()
            
        else:
            satan_vic = [
                "Satan throws his head back in victorious laughter.",
                "",
                "\033[91mSatan: I told you, mortal! You cannot beat the master of Hell at his own game!\033[0m",
                "",
                "The crowd cheers wildly as chains wrap around your wrists, pulling you into the abyss that opened beneath you."
            ]
            
            print_typewriter(satan_vic)
            time.sleep(message_interval)
            current_level = 12
            alternate_ending()

    narration = [
        "After stepping out of the elevator and wandering through an endless labyrinth of hallways, ",
        "you stumble upon a hidden passage. The sound of heavy metal music blares from behind a bright red door.",
        "Curiosity piqued, you push the door open and step inside.",
        "",
        "The scene before you is nothing short of surreal.",
        "Satan himself stands on a massive stage, shredding a guitar as a crowd of demons roars with approval.",
        "As soon as he sees you, he halts the music, his eyes narrowing.",
        "",
        "\033[91mSatan: You! How did you get in here?!\033[0m",
        "",
        "With a flick of his hand, the crowd surges forward and drags you to the stage, lifting you before Satan.",
        "He glares at you, unfazed by your presence.",
        "",
        "\033[91mSatan: Tell me, mortal, how did you find your way here?\033[0m",
        "",
        f"{character_name}: The ghoul at reception said if I roll a double, I could come through and speak to you about...",
        "ripping up the contract I signed.",
        "",
        "The crowd erupts into laughter, followed by boos, as various projectiles are tossed in your direction.",
        "",
        "\033[91mSatan: That ghoul is an imbecile! You think it's as easy as rolling dice to get your soul back?\033[0m",
        "",
        "The laughter of the crowd intensifies.",
        "",
        "\033[91mSatan: Alright, since that stupid ghoul clearly doesn't understand how things work around here,\033[0m",
        "\033[91mI'll tell you what: I'll tear up that contract, return your soul\033[0m",
        "\033[91mbut ONLY if you can beat me in a game of Crucifix, Salt, Holy Water!\033[0m",
        "",
        "The demons cheer wildly, some banging on drums in excitement.",
        "",
        "\033[91mSatan: But, and here's the catch. . .\033[0m",
        "\033[91mIf you lose, I’ve got the perfect job lined up for you down here.\033[0m",
        "",
        f"\033[91mSatan: So, what’s it gonna be, {character_name}?\033[0m"
    ]

    print_typewriter(narration)
    
    choices = [
        "   1. Accept Satan's terms and play Crucifix, Salt, Holy Water",
        "   2. Respectfully decline"
    ]

    for choice in choices:
        print(f"{choice}")
        time.sleep(message_interval)

    while True:
        input_check = ["1", "2"]
        user_input = input("\nPlease choose an option: ")
        if user_input not in input_check:
            print("Please enter a valid option\n")
        else:
            if user_input == "1":
                c_s_hw()
                break
            elif user_input == "2":
                narr = [

                    "\033[91mSatan lets out a booming laugh, the sound echoing through the infernal chamber.",
                    "",
                    "Satan: Declining my challenge? Oh, that’s rich! You’re smarter than you look, mortal, I’ll give you that.\033[0m",
                    "",
                    "The crowd erupts into raucous laughter, demons pointing and jeering at your decision.",
                    "",
                    "\033[91mSatan: But let’s be honest. You didn’t think you’d get out of here unscathed, did you?\033[0m",
                    "",
                    "He leans in close, his voice dropping to a menacing whisper.",
                    "",
                    "\033[91mSatan: I’ve got just the job for you. The perfect role for a... *gambler* like yourself.\033[0m",
                    "",
                    "The demons cheer wildly as chains materialise around your wrists, dragging you towards a dimly lit corner of the room.",
                    "",
                    "As the crowd's laughter fades, the last thing you see is a pair of glowing dice clattering onto a table.",
                    "Your fate is sealed."
                ]
                print_typewriter(narr)
                time.sleep(message_interval)
                current_level = 12
                alternate_ending()

def level_three():
    global character_name, current_level

    clear_screen()

    def level_ascii():
        print("\033[38;5;160m")
        print("   ▄▄▄▄▀ ▄  █ ▄███▄          ▄▄▄▄▄   ████▄   ▄   █               ")
        print("▀▀▀ █   █   █ █▀   ▀        █     ▀▄ █   █    █  █               ")
        print("    █   ██▀▀█ ██▄▄        ▄  ▀▀▀▀▄   █   █ █   █ █               ")
        print("   █    █   █ █▄   ▄▀      ▀▄▄▄▄▀    ▀████ █   █ ███▄            ")
        print("  ▀        █  ▀███▀                        █▄ ▄█     ▀           ")
        print("          ▀                                 ▀▀▀                  ")
        print("                                                                 ")
        print(" ▄  █ ██   █▄▄▄▄    ▄   ▄███▄     ▄▄▄▄▄      ▄▄▄▄▀ ▄███▄   █▄▄▄▄ ")
        print("█   █ █ █  █  ▄▀     █  █▀   ▀   █     ▀▄ ▀▀▀ █    █▀   ▀  █  ▄▀ ")
        print("██▀▀█ █▄▄█ █▀▀▌ █     █ ██▄▄   ▄  ▀▀▀▀▄       █    ██▄▄    █▀▀▌  ")
        print("█   █ █  █ █  █  █    █ █▄   ▄▀ ▀▄▄▄▄▀       █     █▄   ▄▀ █  █  ")
        print("   █     █   █    █  █  ▀███▀               ▀      ▀███▀     █   ")
        print("  ▀     █   ▀      █▐                                       ▀    ")
        print("       ▀           ▐                                             ")
        print("\033[0m")

        time.sleep(slow_message_interval)
    level_ascii()

    def level_three_player_roll():
        l3_dice_roll = random.randint(1, 6)
        l3_dealer_roll = random.randint(1, 6)

        time.sleep(message_interval)
        print(f"\nYou Rolled: {l3_dice_roll} | Dealer Rolled: {l3_dealer_roll}")

        if l3_dice_roll > l3_dealer_roll:
            time.sleep(message_interval)
            l3_roll_success = ["The dice roll across the table and land with a satisfying clatter. You beat the dealer's roll!"]
            print_typewriter(l3_roll_success)
            return True
        elif l3_dice_roll == l3_dealer_roll:
            time.sleep(message_interval)
            l3_roll_draw = ["Sorry champ, draws go to me. It's not higher!"]
            print_typewriter(l3_roll_draw)
            return False
        else:
            time.sleep(message_interval)
            l3_roll_fail = ["The dice roll across the table and land with a dissapointing clatter. The dealer's roll stands victorious"]
            print_typewriter(l3_roll_fail)
            return False
    def level_three_play_game():
        l3_attempts = 0
        l3_max_attempts = 3

        while l3_attempts < l3_max_attempts:
            print(f"Attempt: {l3_attempts + 1} of {l3_max_attempts}:")
            if level_three_player_roll():
                return True
            l3_attempts += 1
        return False

    level_three_intro_message = [
        "You emerge from the labyrinthine maze into a bustling casino, a cacophony of clinking coins and cheering patrons filling the air.",
        "",
        "Demons, goblins, and otherworldly creatures are engrossed in games of chance,",
        "their eyes fixed on spinning roulette wheels, shuffled decks of cards, and flashing slot machines. ",
        "The ghoul, the same eerie figure from the reception desk, spots you and a surprised expression crosses its skeletal face."
    ]

    print_typewriter(level_three_intro_message)

    time.sleep(message_interval)

    print("")

    level_three_dialogue = [
        f"Ghoul: Ooooh, damn! {character_name}, you actually made it. I would say I'm happy for you, but I'm not...",
        f"{character_name}: Jeez, thanks. And what about that kick in the back earlier?",
        "Ghoul: Hey, don't take it personally. It's just we don't like losing souls down here is all, and the kick is just company policy.",
        f"{character_name}: What's next? Let's just get this over with.",
        "Ghoul: Of course! Follow me - you're going to love this one."
    ]

    print_typewriter(level_three_dialogue)

    clear_screen()
    time.sleep(fast_message_interval)
    level_three_narration = [
        "The ghoul leads you to a crowded table, where a group of mortal souls are locked in a high-stakes dice game.",
        "The tension is palpable, each roll of the dice a life-or-death gamble.",
        "As the mortals lose, the demons surrounding the table erupt in cheers, their laughter echoing through the casino.",
        "Desperation paints the faces of the players, their futures hanging in the balance.",
        "",
        "The ghoul, with a cruel grin, grabs you by the scruff of your neck and hurls you towards the front of the table.",
        "The dealer, a grotesque creature with horns and a forked tail, welcomes you to the game.",
        "A set of dice is thrust into your trembling hands, and the demons around the table let out a chorus of jeers and taunts.",
        "",
        "The pressure is immense, the stakes higher than life itself."
    ]

    print_typewriter(level_three_narration)

    time.sleep(slow_message_interval)

    print("")

    clear_screen()

    dealer_dialogue = [
        "Dealer: Ah hellcome, hellcome! This is a super easy game of chance. All you have to do is roll the set of dice and beat my roll. Good luck!",
        "",
        "Dealer: You've got 3 chances to beat my roll. If you beat it, you earn a chip to cash in. If not, well, hellcome to Hell!"
    ]

    print_typewriter(dealer_dialogue)

    print("")

    print("\nWhat will you do?")
    print("   1. Roll the dice")
    print("   2. Back out and leave the casino")

    while True:
        l3_choice = input("\nEnter 1 or 2: ").strip()
        if l3_choice == "1":
            if level_three_play_game():
                l3_play_narration = [
                    "The demons at the table groan in disappointment, their hopes dashed.",
                    "The dealer, with a begrudging sigh, slides a chip across the table.",
                    "",
                    "You make your way to the cashier's desk, a grotesque demon woman with glowing red eyes.",
                    "You slide the chip across the glass counter, and she, with a flick of her wrist, hands you a peculiar key.",
                    "",
                    "“If you make your way up the stairs behind the bar, that key will unlock that door,” she rasps.",
                    "",
                    "You follow her directions, ascending the dimly lit staircase."
                ]
                print_typewriter(l3_play_narration)
                input("\nPress Enter to go to Level 4: ")
                current_level = 4
                level_four()
                break
            else:
                l3_play_fail_narration = ["You have used all 3 attempts and failed to beat the dealer. The demons laugh cruelly."]
                print_typewriter(l3_play_fail_narration)
                time.sleep(slow_message_interval)
                death_screen()
                break
        elif l3_choice == "2":
            clear_screen()
            l3_choice_2_narration = [
                "You decide to back out and leave the casino. As you turn to walk away, a loud growl fills the air.",
                "",
                "From the shadows, massive hellhounds emerge, their eyes glowing red as they snarl at you.",
                "Before you can react, they pounce on you, their claws digging into your flesh.",
                "The hounds drag you back to the table, their jaws snapping dangerously. The ghoul laughs menacingly.",
                "",
                f"Ghoul: What part of the game don't you understand? Hellcome back, {character_name}. You're playing whether you like it or not!",
                "",
                "You struggle but the hounds' grip is too strong.",
                "With no choice left, you sit back down at the table, the dice forced back into your hands.",
                "",
                "The dealer smirks, clearly amused by your predicament"
            ]

            print_typewriter(l3_choice_2_narration)

            print("\nDo you want to try again?")
            print("1. Roll the dice.")
            print("2. Quit and accept your fate.")

            while True:
                next_choice = input("\nEnter 1 or 2: ").strip()

                if next_choice == "1":
                    if level_three_play_game():
                        l3_next_choice_narr = [
                            "The demons at the table groan in disappointment, their hopes dashed.",
                            "The dealer, with a begrudging sigh, slides a chip across the table.",
                            "",
                            "You make your way to the cashier's desk, a grotesque demon woman with glowing red eyes.",
                            "You slide the chip across the glass counter, and she, with a flick of her wrist, hands you a peculiar key.",
                            "",
                            "“If you make your way up the stairs behind the bar, that key will unlock that door,” she rasps.",
                            "",
                            "You follow her directions, ascending the dimly lit staircase."
                        ]

                        print_typewriter(l3_next_choice_narr)
                        input("\nPress Enter to go to Level 4: ")
                        current_level = 4
                        level_four()
                        break
                    else:
                        l3_used_all_attempts_narr = [
                            "You have used all 3 attempts and failed to beat the dealer. The demons laugh cruelly."
                        ]
                        print_typewriter(l3_used_all_attempts_narr)
                        time.sleep(slow_message_interval)
                        death_screen()
                        break
                elif next_choice == "2":
                    l3_give_up_narr = [
                        "You resign to your fate, staying in the casino as demons laugh around you."
                    ]
                    print_typewriter(l3_give_up_narr)
                    time.sleep(slow_message_interval)
                    death_screen()
                    break
                else:
                    print("\nInvalid choice. Please enter 1 or 2.")
            break
        else:
            print("\nInvalid choice. Please enter 1 or 2.")

def level_two():
    global character_name, current_level
    skip = True
    
    clear_screen()

    def level_ascii():
        print("\033[38;5;160m")
        print("   ▄▄▄▄▀ ▄  █ ▄███▄       ██▄   ▄███▄      ▄   ▄█ █      ▄▄▄▄▄   ")
        print("▀▀▀ █   █   █ █▀   ▀      █  █  █▀   ▀      █  ██ █     █     ▀▄ ")
        print("    █   ██▀▀█ ██▄▄        █   █ ██▄▄   █     █ ██ █      ▀▀▀▀▄   ")
        print("   █    █   █ █▄   ▄▀     █  █  █▄   ▄▀ █    █ ▐█ ███▄ ▀▄▄▄▄▀    ")
        print("  ▀        █  ▀███▀       ███▀  ▀███▀    █  █   ▐                ")
        print("          ▀                               █▐                     ")
        print("                                           ▐                     ")
        print("█ ▄▄  █    ██  ▀▄    ▄  ▄▀  █▄▄▄▄ ████▄   ▄      ▄   ██▄        ")
        print("█   █ █    █ █   █  █ ▄▀    █  ▄▀ █   █    █      █  █  █     ")
        print("█▀▀▀  █    █▄▄█   ▀█  █ ▀▄  █▀▀▌  █   █ █   █ ██   █ █   █      ")
        print("█     ███▄ █  █   █   █   █ █  █  ▀████ █   █ █ █  █ █  █      ")
        print("█            █  ▄▀     ███    █         █▄ ▄█ █  █ █ ███▀        ")
        print(" ▀                           ▀           ▀▀▀  █   ██           ")
        print("                                                                ")
        print("\033[0m")

        time.sleep(slow_message_interval)
    level_ascii()

    def level_two_choices(isFirstAppearance):
        l2_choices = [
            "   1. Roll the Dies",
            "   2. Enter the Layers of Hell"
        ]

        if isFirstAppearance:
           l2_choices = [
                "   1. Roll the Dies",
                "   2. Enter the Layers of Hell"
            ]
        else:
            l2_choices = [
                "   1. Enter the Layers of Hell"
            ]

        for choice in l2_choices:
            print(f"{choice}")

        while True:
            if isFirstAppearance:
                input_check = ["1", "2"]

                user_input = input("\nPlease choose an option: ")
                if user_input not in input_check:
                    print("Please enter a valid option\n")
                else:
                    if user_input == "1":
                        level_two_dies_game()
                        return_to_reception()
                        break
                    elif user_input == "2":
                        clear_screen()
                        l2_maze_selection_dialogue = [
                            "The ghoul rises from his chair, a sinister grin spreading across his skeletal face.",
                            "He leads you to a hidden door behind his desk and with a forceful kick, propels you through the portal.",
                            "As you tumble through the darkness, you hear his maniacal laughter echoing in the distance."
                        ] 
                        print_typewriter(l2_maze_selection_dialogue)
                        time.sleep(message_interval)
                        level_two_maze()
                        return_to_reception()
                        break
            else:
                input_check = ["1"]
                user_input = input("\nPlease choose an option: ")
                if user_input not in input_check:
                    print("Please enter a valid option\n")
                else:
                    clear_screen()
                    l2_maze_selection_dialogue = [
                        "The ghoul rises from his chair, a sinister grin spreading across his skeletal face.",
                        "He leads you to a hidden door behind his desk and with a forceful kick, propels you through the portal.",
                        "As you tumble through the darkness, you hear his maniacal laughter echoing in the distance."
                    ] 
                    print_typewriter(l2_maze_selection_dialogue)
                    time.sleep(message_interval)
                    level_two_maze()
                    return_to_reception()
                    break
                

    def level_two_ghoul_convo_pre_input():
        convo_messages = [
            "Ghoul: Can I help you?",
            "",
            "You: Yes. I need to speak to someone about this contract I found in my pocket..?",
            "",
            "Ghoul: Ah, I see. So, on Tuesday evening, November 21st, 2024, at around 10:30 PM,",
            "       you were at the High Roller Casino where you lost a considerable amount of money.",
            "       You were offered a deal to reverse your losing streak in exchange for your soul,",
            "       and you willingly signed the contract. It's a good thing you came here.",
            "       The contract was breached instantly. You did the right thing coming here.",
            "       If you left it any longer, the hellhounds would have been picking you up-",
            "",
            "You: Wait a minute, how have I breached it, it's not even my name on the damn contract?!",
            "",
            "Ghoul: Oh yes, we know that...",
            "       You see... it was because you fraudulently signed it is why the terms and conditions were",
            "       breached almost instantaneously!",
            "       This is why your soul is being retrieved.",
            "",
            "You: Do you have any proof that it was me who signed that contract?",
            "     If not, then I guess it's null and void!",
            "",
            "Ghoul: Don't try to be a smarty pants, it's got your blood on it.",
            "       But if you want to contest it then we can send you to our National Hellth Service for a test",
            "       And believe me, you don't want that, the wait times are a lot worse than they are up there.",
            "",
            "       So if you'd like to give us your real name that would be great!"
        ]

        print_typewriter(convo_messages)

    def level_two_ghoul_convo_post_input():
        convo_messages_cont = [
            f"Ghoul: Ahh Thank you {character_name}, now that we've got a bit of honesty flowing in here,",
            "I can tell you how to get out of that contract...",
            "Yes, I know the contract states it's irreversible with no appeal...",
            "The Law of Hell is different than your mortal law, jeez leave me alone.",
            "",
            f"{character_name}: Right, okay, so how do I get out of it then?",
            "",
            "Ghoul: Well through these doors behind me are a series of levels which have to be completed,",
            "after completing each level you will gain a key which will open up the next level.",
            "If you can get through each one to the end...",
            "... We will tear up your contract, and your soul will be yours once more!",
            "",
            "Ghoul: ... OR you could roll these two dies.",
            "",
            f"{character_name}: Dies? Do you mean dice?",
            "",
            f"Ghoul: No! Dies. You forget where you are, {character_name}.",
            "Roll a double in 3 moves then I'll let you go to the big man's office downstairs",
            "and you can hash it out with him.",
            "",
            f"Judging by your contract, you are a gambler, so what's it gonna be {character_name}?"
        ] 

        print_typewriter(convo_messages_cont)

    def level_two_dies_game():
        global current_level, attempt_count, tries_left  # Player starts with 3 attempts
        attempt_count = 0
        tries_left = 3

        def level_two_dies_game_intro():
            clear_screen()
            dies_game_intro_messages = [
                "The ghoul hands you 2 die, each numbered 1 to 6.",
                "You nervously grasp the dice, your palms clammy.",
                "With a deep breath, you will roll them across the desk.",
                "Roll a double to win!"
            ]
        
            print_typewriter(dies_game_intro_messages)
            # input("\nPress Enter to continue...")  

        def level_two_dies_game_play():
            global current_level, attempt_count, tries_left  # Use the global variables for attempt tracking
            
            while tries_left > 0:  # The game continues as long as the player has tries left
                print(f"\nYou have {tries_left} tries left.")
                input("Press Enter to roll the dice...")  # Wait for user to

                
                your_roll = random.randint(1, 6)
                your_roll2 = random.randint(1, 6)

                print(f"\nYou rolled: {your_roll} and {your_roll2}")
                
                
                if your_roll == your_roll2:
                    print("\nYou win! You rolled a double!")
                    current_level = 10
                    time.sleep(slow_message_interval)
                    level_satan_duel()
                    break  
                else:
                    tries_left -= 1  
                    attempt_count += 1  

                
                    if tries_left == 0:
                        print("You have no tries left. Game over!\n")
                        print_typewriter([". . ."])
                        clear_screen()
                        print_typewriter(["The ghoul laughs as you fail to win."])
                        print("")
                        break  

                    print_typewriter(["You did not roll a double."])
                    

        def level_two_dies_game_main():
            """Runs the main flow of the game."""
            level_two_dies_game_intro()  # Call the intro function to start the game
            level_two_dies_game_play()  # Call the game function to begin the dice-rolling process

        # Start the game
        if __name__ == "__main__":
            level_two_dies_game_main()
    
    def level_two_maze():
        clear_screen()
        riddle_messages = [
            "Darkness envelops you, a void devoid of sight. A haunting echo whispers,",
            "",
            "“Two paths unfold, a choice to make:",
            "A memory-filled road, a familiar wake,",
            "Or plunge into the dark, the unknown sea, ",
            "A risky venture, a chance to be free.”"
        ]

        print_typewriter(riddle_messages)
        time.sleep(message_interval)
        print("")

        scene_message = [
            "A soft, ethereal light begins to illuminate the room",
            "To your left, a pair of rusted, iron gates beckon you into a vast, ancient cemetery.",
            "Rows of weathered gravestones stretch into the distance, each marking a forgotten life.",
            "At the far end, a brilliant light emanates from a grand, open doorway, ",
            "promising both hope and danger.",
            "",
            "To your right, a gaping, inky black hole descends into the earth, promising an eternity of darkness.",
            "Its depths are shrouded in mystery, a terrifying unknown."
        ]

        print_typewriter(scene_message)

        time.sleep(message_interval)

        print("\nWhich path will you choose?\n   1. Go left through the iron gates\n   2. Go right into the black hole")

        while True:
            choice = input("\nEnter 1 or 2: ").strip()
            if choice == "1":
                clear_screen()
                choice_one_messages = [
                    "You have chosen to go left, through the iron gates.",
                    "The ancient cemetery awaits your courage..."
                ]
                print_typewriter(choice_one_messages)

                cemetary_story = [
                    "You cautiously step through the rusted gates...",
                    "",
                    "The eerie quiet of the graveyard is broken only by the distant cawing of crows.",
                    "A sense of foreboding hangs heavy in the air.",
                    "As you venture deeper, a flock of crows descends upon you,",
                    "their dark wings blotting out the sunlight.",
                    "The ground beneath your feet begins to tremble, and the once-still graves erupt,",
                    "spewing forth the undead.",
                    "Surrounded by the reanimated corpses, you struggle to escape their grasp,",
                    "but their relentless pursuit proves too much.",
                    "",
                    "You are consumed by the darkness, your life extinguished by the hungry horde."
                ]

                print_typewriter(cemetary_story)
                
                time.sleep(slow_message_interval)
                death_screen()
                break
            elif choice == "2":
                clear_screen()
                choice_two_message = [
                    "You have chosen to go right, into the black hole. The mysteries of the void beckon..."
                ]
                print_typewriter(choice_two_message)
                print("")
                
                black_hole_story = [
                    "You peer into the inky black abyss, your heart pounding in your chest.",
                    "With a deep breath, you leap into the void.",
                    "As you plummet through the darkness, the world around you transforms.",
                    "You're submerged in the icy depths of the ocean, surrounded by strange, bioluminescent creatures.",
                    "A shiver runs down your spine as a colossal shark, its teeth glinting in the dim light,",
                    "lunges towards you.",
                    "With a desperate grab, you snatch a key from its jaws and push it away.",
                    "",
                    "As you struggle to stay afloat, you notice a large, metal plug embedded in the ocean floor.",
                    "With a surge of adrenaline, you swim towards it and pull it free.",
                    "The water begins to drain away, revealing a desolate beach littered with stranded marine life.",
                    "A weathered wooden door, half-buried in the sand, catches your eye.",
                    "",
                    "Using the key you retrieved from the shark, you unlock the door and step into the unknown."
                ]

                print_typewriter(black_hole_story)

                phase_two_message = [
                    "Darkness consumes you, an impenetrable void.",
                    "",
                    "A chilling voice echoes through the silence, its words searing your soul with an icy dread:"
                ]
                time.sleep(message_interval)
                print_typewriter(phase_two_message)
                time.sleep(slow_message_interval)

                clear_screen()

                riddle_two = [
                    "“Two paths unfold, a choice, a test:",
                    "A jungle's depths, a wild, untamed quest,",
                    "Or cuddly kittens, a purring, gentle sight,",
                    "A choice between danger and soft delight.",
                    "Trust your bigger feline friend, he's the one you cannot see.”"
                ]

                print_typewriter(riddle_two)

                scene_two_message = [
                    "The room slowly brightens, revealing two contrasting paths ahead.",
                    "",
                    "To the left, a dense, impenetrable jungle stretches into the darkness,",
                    "its tangled undergrowth and towering trees promising hidden dangers and unknown secrets.",
                    "",
                    "To the right, a warm, inviting glow emanates from a quaint little café.",
                    "A charming sign above the door reads:",
                    "Cat Café: Come and relax with our feline friends, big and small."
                ]

                print_typewriter(scene_two_message)

                print("\nWhich path will you choose?\n   1. Go through the unknown jungle\n   2. Make some cute feline friends")

                while True:
                    next_choice = input("\nEnter 1 or 2: ").strip()
                    if next_choice == "1":
                        clear_screen()
                        jungle_story = [
                            "Hacking through the dense jungle, you're swarmed by a relentless horde of stinging insects.",
                            "You scramble for cover, stumbling upon the lifeless body of a beekeeper",
                            "his protective suit still pristine.",
                            "Slipping into the suit, you feel the insects' attacks futile as you continue your trek. ",
                            "",
                            "Hours later, a dark, gaping cave entrance appears.",
                            "The faint rumble of a purr draws you in.",
                            "As you venture deeper, a colossal tiger emerges from the shadows, its eyes gleaming. ",
                            "Dangling from its collar, a single key glints in the dim light.",
                            "The tiger lets out a bone-chilling roar and charges. ",
                            "",
                            "Fear cripples you, but then an unexpected twist:",
                            "The tiger playfully tackles you, showering you with playful licks.",
                            "A discarded toy box catches your eye. ",
                            "",
                            "You grab a stringy mouse, waving it enticingly.",
                            "Distracted, the tiger swats at the toy, eventually collapsing in a playful heap.",
                            "Seizing the opportunity, you retrieve the key from its collar and unlock the mysterious door before you,",
                            "escaping the watchful gaze of the jungle's king."
                        ]

                        print_typewriter(jungle_story)

                        print("""
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣄⣕⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⠉⠙⠢⡀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣠⣬⣿⣿⣿⣿⣶⣿⣷⣶⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⠿⠟⠛⣻⣿⣿⣿⣿⣿⣿⣤⣦⣤⣤⡉⠙⢶⣤⡀⠀⠀⠀⣼⣷⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⣫⣵⣶⣾⣿⣿⠟⣿⣿⠻⠿⠿⠿⠿⠛⠿⢿⣷⣄⠙⣿⡖⠀⣰⣿⣿⡄⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀
                        ⠀⠀⠀⣠⠋⠉⠓⣦⣀⠀⠀⠀⠀⢀⣴⠏⢠⣾⡿⠟⠛⠋⠁⠀⣠⣿⣿⣦⣄⣀⣀⣀⠀⠀⠀⠈⠻⣷⡌⢻⣴⣿⣿⣿⡇⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀
                        ⠀⠀⠀⡇⠀⠀⠀⠈⣿⣷⡦⣄⣐⣾⣟⣰⣿⡟⠀⠀⠀⣠⣴⣾⣿⡟⠻⢿⣿⣿⣿⣿⣿⣶⠋⠉⢧⠈⠻⢳⡉⠘⣿⣿⣧⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀
                        ⠀⠀⠀⡇⠀⠀⠀⠀⢹⣿⣿⣾⡿⣿⠋⣿⢋⡤⠄⢤⣾⣿⣿⠛⠁⠀⠀⠀⡀⠉⢁⡭⠛⠃⠀⠀⣨⣇⡀⠀⠁⢠⡌⢻⣿⠀⠀⠀⡰⠁⠀⠀⠀⠀⠀
                        ⠀⠀⠀⢇⠀⠀⠀⠀⠀⢻⣿⣟⣛⠛⠀⠋⢸⠀⠀⠀⠛⠋⢦⢶⣶⣄⠀⣶⣿⣦⠞⠀⠀⢰⣾⡿⠿⠛⠉⠑⢦⣀⢻⣷⣿⣦⣀⡼⠁⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠘⡄⠀⠀⠀⢀⣿⣿⣿⢏⡀⠀⠀⣨⣯⣦⣤⣀⠀⠈⣳⡹⣿⡟⠿⠟⠋⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠊⢈⣿⡟⣿⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠙⣄⠀⠀⣨⡿⣿⣧⣾⠁⡴⠋⠉⠉⠉⠉⠁⠀⠀⢳⠀⠀⠁⠀⠀⠀⠀⢸⠀⠀⣠⣶⣿⢿⣿⣿⣿⠿⠟⢛⣿⠘⣷⠇⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠈⠳⣄⠀⣼⣿⣿⣿⣾⠁⠀⢀⣤⣤⣤⣤⣄⠀⠘⡇⠀⠀⠀⠀⠀⠀⠈⡀⢰⣿⣿⣧⣠⣿⣿⣿⠀⢠⣾⣿⠀⣿⣾⠅⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠈⠙⣾⣿⣿⡿⡿⣿⣿⣿⣿⣿⣿⠟⢻⣷⡀⢹⠀⠀⢀⡠⠤⢤⡀⡇⢸⣏⠿⣿⣿⡿⣿⠟⢠⢿⣿⡏⢰⣿⡟⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣟⣿⣷⣄⠹⠹⣯⢹⣿⣿⣷⣿⡿⣷⡀⡇⠘⠁⠀⠀⠀⠉⢳⠸⣏⠓⠒⠒⣚⠁⠀⣠⣿⣿⠇⣼⠟⡁⠀⢘⣄⡀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠉⢻⣿⣦⠁⠙⠷⣭⣛⣛⣩⠵⢫⣇⡽⠀⠀⠀⠀⠀⠀⠸⣿⣿⣆⣀⡀⣤⣶⣿⡿⢟⡿⠋⣇⢀⣿⠀⢾⣠⣿⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣤⡈⠻⣿⣷⣤⣀⣀⣤⠄⠀⣀⣿⠿⣇⠀⠀⠀⠀⢀⡀⢰⠋⠁⢀⣤⣉⣛⣿⣶⣶⣏⠀⢦⡙⠛⠋⠀⠈⠉⢡⡴⢒⡆
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣤⡀⠈⠛⣿⣿⣿⣧⡴⢏⣁⠀⠀⠈⣇⠈⠉⠉⠀⠀⣠⠇⢀⡀⠀⠤⠀⠀⣘⠛⠻⣶⡿⢣⠞⠉⠉⠙⢦⠘⠿⠿⠃
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⣿⣿⣿⣿⠿⣿⣟⠉⠁⠒⠪⡍⠀⠈⠓⠒⠠⡖⠚⠁⠀⠀⠑⡦⢄⠀⠀⠈⠳⡄⠀⠀⣟⠀⠀⠀⠀⠈⡇⣠⠔⢦
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣄⠀⠐⠀⠀⢀⡀⣄⣈⡀⠀⢀⣠⣾⣿⣶⣤⣤⣤⠴⠋⠀⢱⠀⠀⠀⣿⣶⣄⠈⠉⠓⠒⠶⠞⠁⢧⣶⠞
                        ⠀⣀⡠⣤⣤⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠙⡆⠀⠀⠀⠀⠀⠀⠉⠙⢿⠉⠻⣅⡴⢸⣿⠃⠀⠀⠀⣀⣷⣄⣀⣽⣿⣏⣳⣄⣀⣀⣀⣤⣤⠐⠀⠀
                        ⠀⣿⡄⠘⣿⡄⣼⡿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣷⣼⣆⡀⠀⠀⠀⠀⠈⠻⠧⠙⠡⠿⠋⠀⠀⢀⣴⣿⣿⢛⣿⠁⠙⣿⢿⣿⣾⣷⣶⣾⡏⠀⠀⠀
                        ⣤⣹⡿⠞⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⢠⣾⠀⢿⣿⣮⡍⣻⡷⢶⣤⢤⡀⠀⠀⠀⠀⠀⠀⠠⢾⠿⠟⠛⠁⣾⣿⣧⡀⠀⠀⠉⠉⠛⠉⢻⠁⠀⠀⠀
                        ⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⠀⠀⠈⠻⢿⣶⠿⠀⠀⠀⠉⠛⠒⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠘⢿⣿⣧⣀⡀⠀⠀⢀⣰⡏⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⣿⣿⡀⠀⠀⠀⣠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣆⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⠃⠉⢿⣿⣶⣄⣰⣻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣦⣤⣄⠀⠀⠀⠀⣀⡴⠋⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⣀⣤⠤⣄⣀⢀⣿⡆⠀⠀⠹⠻⢿⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣿⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
                        ⣄⠀⠀⠀⠀⠠⣾⣿⣷⣤⣶⣨⣿⣿⣷⣄⣠⣆⠀⠀⣀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣻⣿⣿⣁⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠏⢳⣄⣀⠀⠉⠙⠉⠙⠛⢻⣿⣿⠏⠙⠻⠟⠿⢿⠿⠿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⢹⣿⡿⢠⡮⣽⠢⣄
                        """)

                        time.sleep(slow_message_interval)
                        current_level = 3
                        level_three()
                        break
                    elif next_choice == "2":
                        clear_screen()
                        cat_story = [
                            "You step into a feline paradise, a cacophony of purrs and meows filling the air.",
                            "Hundreds of cats, from tiny kittens to majestic Persians, swarm around you, seeking affection.",
                            "",
                            "A kind waitress brings you a steaming cup of coffee,",
                            "and you settle into a cozy armchair, lost in the serene chaos.",
                            "After a while, you decide to leave this idyllic haven.",
                            "As you approach the exit, a sudden sharp pain shoots through your neck.",
                            "",
                            "A small, seemingly harmless cat has sunk its teeth into your skin.",
                            "Before you can react, a horde of cats descends upon you,",
                            "their tiny claws raking. You bleed and bleed and bleed.",
                            "Death by a thousand tiny, cute, cuts."
                        ]

                        print_typewriter(cat_story)
                        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢀⣠⣤⣤⣄⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠟⣫⡿⠉⢻⣇⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠟⢁⡴⠋⠀⠀⠈⢿⡆⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠷⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠋⠁⣠⠞⠁⠀⠀⠀⠀⢸⣷⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⠀⠉⠳⢤⡉⠙⠻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠏⠁⠀⣰⠃⠀⠀⠀⠀⠀⠀⠈⣿⡆
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠙⠶⣄⠀⠉⠻⢷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣾⠟⠁⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠉⠛⢿⣶⣀⣤⣶⠶⠿⠟⠛⣿⠉⠉⠉⠉⠉⠙⠛⠳⠶⠦⣤⣞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⣀⡴⠿⠉⠉⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠲⢤⣀⠀⠀⠀⠀⠀⠀⢸⡇
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⢀⣿⠇
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡴⠀⠀⠀⠀⠀⠀⣠⡾⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⢸⡟⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠹⣆⠀⠀⠀⠀⠀⣠⡴⠶⠖⠶⠶⢦⣀⠀⠀⠀⠹⣦⡿⠁⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣧⠀⠀⢠⡟⠀⠀⠀⠀⢀⣀⣠⠤⢤⣀⣀⠀⠀⠀⢀⡟⠀⠀⠀⠙⣦⠀⠀⣴⣟⣁⣀⣀⡀⠀⠀⠀⠈⠳⣆⠀⠀⠸⣷⡀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣧⣄⡿⠀⠀⠀⣠⠶⠋⠁⠀⠀⢀⣀⣉⡳⢦⣀⣾⠀⠀⠀⠀⠀⠘⢷⡾⡿⠚⠻⣿⣿⣿⣶⡄⠀⠀⠀⠸⡆⠀⠀⢹⣇⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣿⠁⠀⠀⣴⠋⠀⠀⠀⣠⣾⣿⣿⠋⠉⠳⣝⢧⡀⠀⠀⠀⠀⠀⡾⢻⣧⣀⣀⣿⣿⣿⣿⣿⡄⠀⠀⠀⡇⠀⠀⠸⣿⡄
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⢰⠇⠀⠀⠀⢰⣿⣿⣿⣿⣄⣀⣴⣿⠈⢷⠀⠀⠀⠀⣸⡃⠸⣿⣿⢿⣿⣿⠟⠉⣿⠁⠀⠀⢠⡇⠀⠀⠀⣿⡇
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠘⣇⠀⠀⠀⢸⣿⠿⢿⣿⣿⠿⠿⣿⠀⠈⡇⠀⠀⠀⠙⣇⠀⠙⢧⣀⣀⣀⣠⠶⠃⠀⠀⣠⠟⠁⠀⠀⠀⣿⡇
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠻⣄⠀⠀⠀⠻⣤⣀⣀⣀⣠⡶⠋⢀⣼⠃⣀⣀⣀⡀⠙⠶⢤⣀⣈⣉⣉⣁⣀⣤⠶⠾⢥⣀⣀⡀⠀⢠⣿⠁
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀⠀⠉⠳⢤⣀⣀⠀⠉⠉⣉⣁⣠⠶⠚⠁⠀⠈⠙⡏⠁⠀⠀⠀⠈⠉⠉⡉⠉⠁⠀⠀⠀⠁⠀⠉⠉⠙⣻⡏⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⢀⣀⠶⠛⠉⠉⠉⠉⠉⢉⡀⠀⠀⠀⠀⠀⣠⢿⣄⠀⠀⠀⠀⢠⡟⠁⠀⠀⠀⠀⠀⡈⠉⠉⠉⢹⡿⠓⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⠴⠞⠋⠁⣀⡀⠀⠀⠀⠀⠀⠈⠳⣄⣀⣀⣠⠞⠁⠀⠈⠙⠲⠶⠖⠋⠀⠀⠀⠀⠀⠀⠈⠓⠶⢤⣰⣿⣃⡀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⡶⠚⠋⠉⢀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢤⣀⣴⡟⠉⠙⠃⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣠⠶⠋⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⡿⠳⣦⣀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠙⠷⣄⣶⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠶⠛⠉⣿⠀⠀⠀⠉⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⢀⡶⠋⠉⢳⠶⠦⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡤⠴⠶⠒⠉⠉⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠐⠋⠀⠀⢀⡿⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠟⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠰⠶⠦⢤⣤⠤⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⣰⠞⠁⠀⠀⠀⠉⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⠿⡿⠀⠀⠀⠀⠀⣀⡤⠶⠋⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⣀⣴⡿⠛⠉⠀⢰⡧⠤⠶⠶⠒⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⣠⣾⠟⠉⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⣰⡿⠃⠀⠀⠀⠀⠀⣀⣘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⣀⡀⠀⠀⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⢸⣿⠁⠀⠀⠀⠀⢰⡟⠉⠉⢹⡄⠀⠀⠀⠀⠀⠀⠀⣀⡴⠚⠋⠉⠉⠉⠙⠶⣄⣷⣠⠶⠚⠉⠉⠉⠉⠙⠶⣤⣧⡴⠞⠋⠉⠉⠉⠙⠲⢦⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⢸⣿⠀⠀⠀⠀⠀⠸⣇⣀⣀⣀⣻⣄⣀⣀⣀⣀⣀⣰⣏⡀⠀⣴⠀⠀⣤⠀⠀⠈⣿⠁⠀⠀⣶⠀⠀⣤⠀⠀⠈⡿⠀⠀⢰⡀⠀⢠⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠸⣿⡆⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢷⣼⠀⠀⣿⠀⠀⠀⣿⡀⠀⠀⢹⠀⠀⣿⠀⠀⠀⣷⠀⠀⢸⡇⠀⢸⠀⠀⠀⣸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠸⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠈⠻⣷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠈⠉⠻⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠿⠋⠀
                        """)
                        time.sleep(slow_message_interval)
                        death_screen()
                        break
                    else:
                        print("\nInvalid choice. Please enter 1 or 2.")
                break
            else:
                print("\nInvalid choice. Please enter 1 or 2.")


    def return_to_reception():
        return_messages = [
            "Ghoul: Ahh, back again are we?",
            "I can see why you needed the contract. Not a great gambler are you?",
            "",
            "Well, it's my deathday today, so I'm gonna be nice...",
            "You can have another shot at winning your soul back.",
            "",
            ". . .",
            "",
            "But you'll have to go the long way round!"
        ]

        print_typewriter(return_messages)
        print("\nPlease choose an option: ")
        level_two_choices(False)

    level_two_intro_messages = [
        "As you descend the stairs, you find yourself in a strangely serene waiting room.",
        "Soft, ethereal music fills the air, contrasting sharply with the hellish heat you'd just escaped.",
        "A large fish tank, filled with menacing piranhas, bubbles quietly in the corner.",
        "",
        "Behind a desk, a gaunt, skeletal figure sits, immersed in paperwork.",
        "Its hollow eyes meet yours, a chilling smile playing on its lips.",
        "",
        "You approach the decrepit figure behind the desk, and wait for it to notice you.",
        "",
        ". . ."
    ]

    if not skip:
        print_typewriter(level_two_intro_messages) 
    time.sleep(message_interval)
    print("")
    level_two_ghoul_convo_pre_input()

    while True:
        character_name = input("\nTell the Ghoul your name: ").strip()
        if not character_name:
            print("You must tell the Ghoul your real name.")
        else:
            break
    print("")

    level_two_ghoul_convo_post_input()

    print("")
    
    level_two_choices(True)
        
def level_one():
    clear_screen()

    def level_ascii():
        print("\033[38;5;160m")
        print("    ▄▄▄▄▀ ▄  █ ▄███▄       █▀▄▀█ ▄█ ██▄      ▄   ▄█   ▄▀   ▄  █    ▄▄▄▄▀        ")
        print(" ▀▀▀ █   █   █ █▀   ▀      █ █ █ ██ █  █      █  ██ ▄▀    █   █ ▀▀▀ █           ")
        print("     █   ██▀▀█ ██▄▄        █ ▄ █ ██ █   █ ██   █ ██ █ ▀▄  ██▀▀█     █           ")
        print("    █    █   █ █▄   ▄▀     █   █ ▐█ █  █  █ █  █ ▐█ █   █ █   █    █            ")
        print("   ▀        █  ▀███▀          █   ▐ ███▀  █  █ █  ▐  ███     █    ▀             ")

        print("█▄▄▄▄ ▄█    ▄▄▄▄▀     ██   █        ")
        print("█  ▄▀ ██ ▀▀▀ █        █ █  █        ")
        print("█▀▀▌  ██     █  █   █ █▄▄█ █        ")
        print("█  █  ▐█    █   █   █ █  █ ███▄     ")
        print("    █  ▐   ▀    █▄ ▄█    █     ▀    ")
        print("   ▀             ▀▀▀    █           ")
        print("\033[0m")
        time.sleep(slow_message_interval)
    level_ascii()
    global current_level

    def level_one_choices():
        level_one_choices = [
            "   1. Check out the large crucifix at the back of the church",
            "   2. Walk into the confession booth",
            "   3. Head to the altar."
        ]

        for choice in level_one_choices:
            print(f"{choice}")

        while True:
            input_check = ["1", "2", "3"]
            user_input = input("\nPlease choose an option: ")
            if user_input not in input_check:
                print("Please enter a valid option\n")
            else:
                if user_input == "1":
                    level_one_crucifix()
                    return_to_church()
                    break
                elif user_input == "2": 
                    level_one_confessional_room()
                    return_to_church()
                    break
                elif user_input == "3":
                    level_one_altar()
                    break

    def return_to_church():
        clear_screen()
        rtc_dialogue = [
            "You have returned to the Cathedral of St. Lucifer.",
            "The eerie silence hangs in the air as you stand in the nave of the church.",
            "",
            "What do you wish to do next?"
        ]
        print_typewriter(rtc_dialogue)

        print("")
        
        level_one_choices()

    def level_one_crucifix():
        clear_screen()
        print("Level One - The Crucifix\n\n")
        
        crucifix_message = [
                "You make your way to the back of the cathedral",
                "",
                "Drawn to the imposing crucifix that dominates the space.", 
                "As you approach, you notice intricate carvings and symbols adorning the wooden structure.",
                "", 
                "The carvings on the crucifix seem to pulsate with an ancient energy.",
                "As you read the words 'By the power of darkness, I summon the ancient forces,' an unshakable sense of authority emanates from the phrase.",
                "It feels like the opening line of a dark symphony, commanding the unseen to awaken.",
                "",
                "A chill runs down your spine as you realise this could be a missing piece of the puzzle.",
        ]

        print_typewriter(crucifix_message)
        
        input("\nPress Enter to Go Back...")

    def level_one_confessional_room():
        clear_screen()
        print("Level One - The Confessional Booth\n\n")

        confessional_booth_message = [
            "You enter the shadowy confessional booth, the silence heavy and oppressive. A moment passes, then a chilling voice echoes from the darkness.",
        ]
        print_typewriter(confessional_booth_message)
        print("")
        confess_ask = [
            "Do you have a confession?"
        ]
        print_typewriter(confess_ask)
        print("")
        choices = [
            " 1. Yes",
            " 2. No"
        ]

        for choice in choices:
              print(f"{choice}")
        
        print("")

        while True:
            input_check = ["1", "2"]
            user_input = input("\nPlease choose an option: ")
            if user_input not in input_check:
                print("Please enter a valid option\n")
            else:
                if user_input == "1":
                    confession = input("Enter your confession: ")
                    confess_yes = [
                        f"{confession}, what? Why you're telling me that? Do I look like a priest?",
                        "Now this is awkward.",
                        "",
                        ". . .",
                        "",
                        "Errh. . . how about a clue?",
                        "",
                        "'Let the veil between worlds be torn asunder. I invoke the night, the void, and all that dwells within.'",
                        "",
                        "The eerie echo reverberates, as if it tears through the walls of this reality into another."
                    ]
                    print_typewriter(confess_yes)
                    break
                elif user_input == "2": 
                    confess_no = [
                        "Well then, I guess it's a clue you want, isn't it?",
                        "I hope you're going to remember this . . .",
                        "",
                        "'Let the veil between worlds be torn asunder. I invoke the night, the void, and all that dwells within.'",
                        "",
                        "The eerie echo reverberates, as if it tears through the walls of this reality into another."
                    ]
                    print_typewriter(confess_no)
                    break
        user_input = input("\nPress Enter to Go Back...")

    def level_one_altar():
        clear_screen()
        time.sleep(message_interval)
        print("\033[1;95mLevel One - The Altar\033[0m\n\n")

        phrases = [
            "By the power of darkness, I summon the ancient forces.",
            "Let the veil between worlds be torn asunder. I invoke the night, the void, and all that dwells within.",
            "Let the ritual begin."
        ]

        altar_success_messages = [
            "A chilling, discordant melody erupted from the cathedral organ, its eerie tune filling the room.",
            "The stone tiles beneath the altar began to rumble, slowly parting to reveal a dark, yawning chasm",
            "",
            "A wave of intense heat radiated from the depths, but you had no choice.",
            "",
            "With a deep breath, you descended the winding cobblestone steps into the unknown..."
        ]

        def level_one_altar_intro():
            l1_altar_intro_messages = [
                "A cluster of candles surround the altar.",
                "A large, leather-bound book lay open on the altar, its front cover emblazoned with the words:",
                "",
                "'Let the Ritual Begin'.",
                "",
                "The pages within were blank, save for a single lighter that had fallen out.",
                "",
                "You light each candle one by one, the soft glow casting an ethereal light over the room.",
                "As the last candle flickers to life, the air thickens.",
                "",
                "It's as if time itself holds its breath, awaiting this final act."
            ]
            print_typewriter(l1_altar_intro_messages)

            input("\nPress Enter to Continue...")

            clear_screen()
            time.sleep(fast_message_interval)

        def level_one_altar_game():
            time.sleep(message_interval)
            clear_screen()
            l1_altar_game_messages = [
                "You stand before the altar, ready to perform the ritual.",
                "You must say the correct phrase in order to proceed. Select the phrases in the correct order:"
            ]
            print_typewriter(l1_altar_game_messages)
            print("")
            shuffled_phrases = phrases.copy()
            random.shuffle(shuffled_phrases)

            correct_order = phrases

            player_choices = []
            
            for i in range(1, 4):
                print(f"Choose phrase {i}:\n")
                
                for idx, option in enumerate(shuffled_phrases, 1):
                    print(f"    {idx}. {option}")
                
                while True:
                    try:
                        choice = int(input("\nEnter the number of your choice: "))
                        if 1 <= choice <= 3:
                            player_choices.append(shuffled_phrases[choice-1])  
                            break
                        else:
                            print("\nInvalid choice, please enter a number between 1 and 3.")
                    except ValueError:
                        print("\nInvalid input. Please enter a number.")
            
            if player_choices == correct_order:
                return True  # Correct order, proceed with the game
            else:
                return False  # Incorrect order, ritual failed

        def level_one_altar_main():
            level_one_altar_intro()  
            
            while True:
                success = level_one_altar_game()  
                if success:
                    clear_screen()
                    print_typewriter(altar_success_messages)
                    input("\nPress Enter to Continue...")
                    level_two()
                    break  
                else:
                    retry = input("Would you like to try again? (yes/no): ").strip().lower()
                    if retry != 'yes' and retry != 'y':
                        print("\nYou have chosen not to retry. You extinguish the candles and head back into the church.")
                        input("\nPress Enter to Continue...")
                        return_to_church()
                        break

        if __name__ == "__main__":
            level_one_altar_main()

    level_one_start_messages = [
        "After what felt like an eternity, you arrive at St. Lucifer's Cathedral.",
        "",
        "The sun had already begun its descent, casting long, eerie shadows across the desolate landscape.",
        "The cathedral loomed before you, a gothic behemoth, its weathered stonework and broken windows hinting at centuries of decay.",
        "",
        "You navigate through the overgrown cemetery, the only sound is the mournful cry of an owl and the occasional rustle of wind through the skeletal trees.",
        "As you approach the massive, wooden doors, gargoyles, grotesque and menacing, seem to watch your every move...",
        "",
        "With a trembling hand, you motion to push open the creaking doors . . ."
    ]

    print_typewriter(level_one_start_messages)

    print("")

    input("Press enter to go inside...")

    clear_screen()

    level_one_interior_messages = [
        "...The interior of the church, in stark contrast to its decaying exterior, was pristine and untouched.",
        "",
        "The stained-glass windows, though dusty, still cast the last vibrant hues of light across the polished floor.",
        "You walked down the aisle, the silence broken only by the echo of your footsteps.",
        "You find a crisp note left on one of the benches. You unfold the note, its message chilling and ominous.",
        "",
        "",
        "\033[91mIf you are reading this note, you have come here to discuss the contract in which you signed. In order to do this you must perform the midnight ritual.\033[0m",
        "\033[91mWhen the church bell rings at midnight, light the candles on the altar and repeat the phrase to open up the passage to Hell.\033[0m",
        "\033[91mIf you don't know the phrase, take a look around the Cathedral.\033[0m"
    ]

    print_typewriter(level_one_interior_messages)
    
    level_one_interior_messages_2 = [
        "",
        "Suddenly, the church bells began to chime, their deep, resonant tones echoing through the silent cathedral."
    ]

    time.sleep(slow_message_interval)
    print_typewriter(level_one_interior_messages_2)
    print("")

    level_one_choices()

def prologue():
    def backstory():
        story = [
            "The night started innocently enough.",
            "A few drinks with friends, a bit of laughter, the usual.",
            "But as the hours wore on, the drinks flowed, and the atmosphere grew more electric.",
            "The allure of the casino, with its flashing lights and the promise of easy money, proved too tempting to resist.",
            "",
            "The roulette wheel spun, the ball danced, and with each spin, hope flickered",
            "only to be extinguished by the cruel hand of fate...",
            "The losses mounted, and with them, a growing desperation.",
            "In the haze of alcohol-induced euphoria and despair, a stranger appeared...",
            "",
            "A shadowy figure, offering a tempting proposition:",
            "A guaranteed win in exchange for a soul.",
            "In a moment of reckless abandon, a drunken bargain was struck.",
            "",
            "The next morning, the hangover was brutal, but it was the memory of the night that truly haunted.",
            "The casino, the roulette wheel, the stranger's offer - all vanished into a fog of uncertainty."
        ]

        print_typewriter(story)  
        time.sleep(2)  

    def title_card():
        print("\033[91m")  
        print("██▄   ▄███▄      ▄   ▄█ █   ▄  ▄▄▄▄▄       ██▄     ▄   ▄███▄  ")
        print("█  █  █▀   ▀      █  ██ █     █     ▀▄     █  █     █  █▀   ▀ ")
        print("█   █ ██▄▄   █     █ ██ █      ▀▀▀▀▄       █   █ █   █ ██▄▄   ")
        print("█  █  █▄   ▄▀ █    █ ▐█ ███▄▀ ▀▄▄▄▄▀       █  █  █   █ █▄   ▄▀")
        print("███▀  ▀███▀    █  █   ▐                    ███▀  █▄ ▄█ ▀███▀  ")
        print("                █▐                               ▀▀▀          ")
        print("                ▐                                             ")
        print("\033[0m") 

    title_card()  
    print("\n--- A DAY IN HELL ---\n")
    time.sleep(2)  
    backstory()  

    input("\n\nPress Enter to Begin Your Journey...")

def level_intro():
    global current_level

    # Handler function to reshow the choices when returning to the bedroom
    def return_to_bedroom():
        # Clears the termimal
        clear_screen()

        rtb_text = [
            "You have returned to the bedroom.",
            "What do you do next?"
        ]

        print_typewriter(rtb_text)
        print("")
        intro_options()

    def intro_options():
        # Choices are put into a function so they can be redisplayed as needed
        intro_choices = [
            "  1. Head to the bathroom to splash some water on your face and try to wake up.",
            "  2. Stumble to the kitchen, hopefully a bowl of cereal will soothe your aching head and kickstart your day.",
            "  3. Search for your trousers, hoping they might offer clues to the night's events.",
        ]
        # print_typewriter(intro_choices)
        for choice in intro_choices:
            print(f"{choice}")
            time.sleep(message_interval)

        print("")
        print_typewriter(["What do you do?"])

        # Handles user input, While loop is used to reask the user if they enter an incorrect input, the loop exits when "break" is read
        while True:
            input_check = ["1", "2", "3"]
            user_input = input("Please choose an option: ").strip()
            if user_input not in input_check:
                print("Please enter a valid option\n")
            else:
                if user_input == "1":
                    intro_bathroom()
                    return_to_bedroom()
                    break
                elif user_input == "2": 
                    intro_kitchen()
                    return_to_bedroom()
                    break
                elif user_input == "3":
                    intro_trouser_check()
                    break
    # The subroom functions are pretty similar, they again just display a load of messages and then tells the user to press enter to return to the bedroom
    def intro_kitchen():
        clear_screen()
        kitchen_messages = [
            "The kitchen is a disaster zone: plates, bowls, and takeout containers litter the countertops.",
            "A stench of stale food fills the air.",
            "",
            "You grab a box of Alpha-Bits and pour the colorful cereal into a bowl.",
            "As you pour the milk, the cereal pieces float to the surface, spelling out a chilling message:"
            "'Time is Ticking'",
            "",
            '   “What the…”',
            '   “I Really need to stop drinking!”'
        ]

        print_typewriter(kitchen_messages)

        input("\nPress Enter to Return to the Bedroom...")


    def intro_bathroom():
        clear_screen()
        bathroom_messages = [
            "The harsh bathroom light assaults your eyes as you stumble in.",
            "",
            "You turn on the cold tap, splashing water on your face.",
            "As you look up at your reflection in the mirror, a chilling sight greets you...",
            "",
            "IT'S MINE!!! etched in blood, staring back at you...",
            "",
            "   “What the heck?!”",
            "   “Who did this?”",
            "",
            "Your gaze drops to your hand, and a gasp escapes your lips.",
            "",
            "A deep gash, still oozing blood, mars your writing finger...",
            "   “Damn, how did I manage that?”",
            "",
            "   “I need to stop drinking!”"
        ]

        print_typewriter(bathroom_messages)

        input("\nPress Enter to Return to the Bedroom...")

    # Trouser check is a bit different, it displays the messages but also gives the user some choices. If they choose the correct one, they advance to level one, if they choose incorrectly, they die.
    def intro_trouser_check():
        clear_screen()
        global current_level
        # The weird \033[1;91 and stuff are just to make it red and bold
        trouser_messages = [
            "You dig through the crumpled mess beneath your bed, finally locating your trousers.",
            "As you empty the pockets, a curious collection spills out...",
            "",
            "You find:"
        ]
        trouser_items =[
            "   1. Your Wallet",
            "   2. A thick wad of cash",
            "   3. A shiny new casino membership card",
            "   4. A blood-stained contract",
        ]    
        trouser_messages_cont = [
            "You unfurled the contract, the words etched in crimson ink:",
            "",
            "\033[91mThis contract, sealed in blood and ink, is a binding agreement between [Michael Mouse], hereafter referred to as the Mortgagor, and [Satan], hereafter referred to as the Mortgagee.",
            "",
            "Terms and Conditions:",
            "\033[1;91m1. Ownership:\033[0m \033[91mThe Mortgagee shall have absolute and unrestricted ownership of the Mortgagor’s soul upon the conclusion of the Mortgagor’s natural life or upon the earlier occurrence of a breach of this contract.\033[0m",
            "\033[1;91m2. Breach of Contract:\033[0m \033[91mAny attempt by the Mortgagor to circumvent or evade the terms of this contract shall result in immediate forfeiture of the Mortgagor’s soul.\033[0m",
            "\033[1;91m3. Divine Intervention:\033[0m \033[91mThe Mortgagee shall not be held liable for any interference or intervention by divine or supernatural forces.\033[0m",
            "\033[1;91m4. Eternal Bondage:\033[0m \033[91mUpon claiming the Mortgagor’s soul, the Mortgagee shall have the right to bind the Mortgagor to eternal servitude in the Mortgagee’s realm.\033[0m\n",
            "",
            "\033[3;91mThis contract is eternal and irrevocable. There shall be no recourse or appeal. For more information regarding said contract, please visit in person: St. Lucifer’s Cathedral The Pit, West Midlands.\033[0m",
            "\033[3;91mWalk in appointments 00:00-00:59 monday-saturday (business hours may vary on bank holidays)\033[0m",
            "",
            "   “Who the hell is Michael Mouse?”",
            "",
            "What do you do?"
        ]
        

        print_typewriter(trouser_messages)
        print("")
        for item in trouser_items:
            print(f"{item}")
            time.sleep(message_interval)
        print("")
        time.sleep(fast_message_interval)
        print_typewriter(trouser_messages_cont)

        choices = [
            "   1. Worried about the contract, get dressed and make your way to St. Lucifer’s Cathedral to investigate ",
            "   2. Tear the contract up and throw it in the bin then get back in bed."
        ]

        for choice in choices:
            print(f"{choice}")
            time.sleep(message_interval)
        # print_typewriter(choices)

        while True:
            input_check = ["1", "2"]
            user_input = input("\nPlease choose an option: ")
            if user_input not in input_check:
                print("Please enter a valid option\n")
            else:
                if user_input == "1":
                    current_level = 1
                    level_one()
                    break
                elif user_input == "2":
                    clear_screen()
                    go_to_bed_text = [
                        "You stare at the contract for a moment, a chill running down your spine.",
                        "The crimson ink seems to pulse faintly, as if alive, but you shake the feeling off.",
                        "",
                        "Deciding it’s not worth the headache, you tear the contract into tiny pieces.",
                        "The fragments flutter to the floor, dark spots of blood staining the carpet beneath.",
                        "",
                        "“Good riddance,” you mutter, tossing the scraps under the bed and climbing back into the warm embrace of your sheets.",
                        "But as you drift off, unease lingers in your mind. You can almost hear faint whispers, too quiet to understand."
                    ]
                    print_typewriter(go_to_bed_text)
                    time.sleep(message_interval)
                    clear_screen()
                    go_to_bed_text_2 = [
                        "Hours later, a cacophony of barking jolts you awake.",
                        "",
                        "The once bright room is plunged into an unnatural darkness.",
                        "The sound of clawing echoes closer, right outside your door.",
                        "",
                        "As the door bursts open, a horde of hellish hounds, their eyes glowing red, rush towards you.",
                        "",
                        "In a terrifying blur, they tear into you, their sharp teeth sinking into your flesh.",
                        "As consciousness fades, you are dragged into the abyss, a victim of the infernal contract."
                    ]

                    print_typewriter(go_to_bed_text_2)
                    def hound():
                        print("\n")
                        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠉⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠜⠀⠈⣷⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠾⠛⠁⠀⠀⠀⣿⠀⠀⠀⠀⣠⡶⢟⠁⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠟⠁⠀⠀⠀⠀⠀⠀⣿⠀⣀⣴⠞⠋⡰⠋⠀⠀⠀⠀⣠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⠋⠀⠀⠀⠀⠀⠀⠀⢀⣴⣷⠾⠋⠁⢀⡞⠁⠀⠀⠀⠀⢠⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⠋⠁⠀⠀⠀⠀⠀⠀⣠⣴⡶⠛⠉⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⢸⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⡤⠴⠖⠒⠚⠛⠉⠉⠙⠛⠒⠲⢤⣄⣤⡶⠛⠉⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⢸⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⣴⠤⠶⠶⠶⠦⠤⣤⣄⣀⣀⣀⣀⣾⠉⣡⠴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⡎⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠈⢉⣡⡤⠟⠛⠳⢤⡀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣄⠀⠀⠀⠀⠀⠀⣰⠇⣠⡴⠀⠀⠀⠀⡸⠃⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⣠⣿⣄⣠⣖⣲⣦⡤⠇⠀⠀⠀⠀⠀⠀⢀⣤⠤⠭⣵⣒⢶⣺⣷⢊⣟⣦⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠶⠶⠶⠾⠛⠻⠿⣮⣁⠀⠀⠰⢁⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⢻⣤⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠤⠤⠤⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⢠⣿⡙⢶⣄⡀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠈⠓⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣶⣵⠾⠋⢳⣶⣄⣀⠀⠀⠀⠀⠀⠀⠀")
                        print("⡞⢿⡉⢿⣾⠟⢯⣙⣲⣶⢤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣾⣿⠾⣟⡉⠀⠀⠀⠀⠈⠿⢿⣶⠄⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⡇⡞⠉⢻⣿⢀⠞⣇⢿⣩⣟⢻⡛⣿⢿⢿⣿⣷⣦⣄⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣦⡀⠙⢦⠀⠀⠀⠀⠀⠈⠻⣿⣆⠀⠀⠀⠀⣴⡗⠀⠀")
                        print("⢻⡇⠀⠀⢿⣸⠀⠈⠀⠁⠈⠛⠿⠻⣏⢦⠶⢧⣙⢙⣧⡀⢀⠀⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣜⣿⣆⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⣤⣠⠞⣽⢀⣰⠀")
                        print("⠀⠁⠀⠀⠘⢿⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⡀⠀⢉⣿⠾⡇⠈⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⡀⠀⠹⡍⠁⠀⣠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠈⢻⣦⡷⠋⡟⠀")
                        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⡾⠋⢀⣠⡇⠀⠈⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⠀⢀⣀⣙⣷⡦⡷⠀⡞⠁⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠀⢀⡾⠋⠀⣾⠁⠀")
                        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⣤⣼⣹⠟⠀⣀⠼⠃⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⣰⠋⠀⠀⠀⠀⠀⢸⠏⠀⠀⠀⠀⠀⣠⡾⠏⠀⢀⡤⠛⢹⠋⠋⢁⣿⠋⠉")
                        print("⠀⠀⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⣤⣯⡽⠋⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠚⠁⣠⡜⠁⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⢀⣠⡾⠋⠁⠀⠐⣏⠀⢠⡏⠀⢀⡾⠋⠀⠀")
                        print("⠀⠀⠀⠀⣿⡇⢸⣆⠀⠀⣰⣿⣄⢸⢦⡷⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⢀⣠⡾⠋⠀⠀⠀⠀⢸⠋⠉⣿⠛⠋⢀⣴⢟⣁⢤⡤")
                        print("⠀⠀⠀⠀⢹⣽⣾⡜⢶⣾⠳⣿⣨⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠤⠤⠖⠁⠀⠠⠤⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⢁⣨⠟⠛⢉⡿⡷⠾⠗")
                        print("⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    hound()


                    
                time.sleep(3)
                    
                death_screen()
                break
                
    # Initial messages which display to the user               
    messages = [
        "You wake with a start, a cold sweat drenching your brow.",
        "A chilling sensation creeps up your spine as you try to piece together the night before.",
        "", 
        "Your mind is a blank slate, a void where memories should be",
        "A throbbing headache and a foggy mind greet you as you force yourself out of bed.",
        "",
        "You need to try and remember what happened the night before."
    ]

    clear_screen()

    print_typewriter(messages)
    print("")
    intro_options()

if dev_levelskip == 0:
    prologue()
    level_intro() 
elif dev_levelskip == 1:
    current_level = 1
    level_one()
elif dev_levelskip == 2:
    current_level = 2
    level_two()
elif dev_levelskip == 3:
    current_level = 3
    level_three()
elif dev_levelskip == 4:
    current_level = 4
    level_four()
elif dev_levelskip == 5:
    current_level = 5
    level_five()
elif dev_levelskip == 10:
    current_level = 10
    level_satan_duel()
elif dev_levelskip == 11:
    current_level = 11
    hellhound()
elif dev_levelskip == 12:
    current_level = 12
    alternate_ending()
elif dev_levelskip == 100:
    current_level = 100
    player_victory_epilogue()