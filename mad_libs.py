import re
import random

def read_scripts(filename):
    with open(filename, 'r') as file:
        scripts = file.read()
    return re.split(r'---\s*', scripts)

def play_madlibs(script):
    words = re.findall(r'\[([^\]]+)\]', script)
    for word in words:
        replacement = input(f"Enter a {word}: ")
        script = script.replace(f"[{word}]", replacement, 1)
    return script

if __name__ == "__main__":
    scripts = read_scripts("scripts.txt")
    for index, script in enumerate(scripts, start=random.randint(1,len(scripts))):
        print(f"Madlib {index}:\n")
        completed_madlib = play_madlibs(script)
        print("\nCompleted Madlib:\n")
        print(completed_madlib)
        choice = input("Would you like to save this madlib? (y/n): ")
        if choice.lower() == 'y':
            with open(f"madlib{index}.txt", 'w') as file:
                file.write(completed_madlib)
            print(f"Madlib {index} saved.")
        exit_choice = input("Would you like to exit? (y/n): ")
        if exit_choice.lower() == 'y':
            break
        print()
