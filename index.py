import random
import time

def print_delay(text, delay=1):
    print(text)
    time.sleep(delay)

def play_game():
    # Game Setup
    mischief_meter = 0
    wake_o_meter = 0
    turns = 3
    
    print("=" * 50)
    print("      CAT'S MIDNIGHT MISCHIEF: THE CODE EDITION")
    print("=" * 50)
    print_delay("The humans are asleep. The house is yours.")
    print_delay("Your goal: Reach 100% Mischief before the sun rises.")
    print_delay("Warning: If the Wake-o-Meter hits 100%, the human wakes up.\n")

    # Turn 1: Option A (The Couch Zoomies)
    print(f"--- TURN 1/3 ---")
    print_delay("Executing Option A: Couch Zoomies!")
    print_delay("You sprint into the living room, launch off the armchair, and tear across the back of the couch...")
    
    # Randomize the outcome
    zoom_luck = random.choice(["stealthy", "chaotic"])
    if zoom_luck == "stealthy":
        print_delay("🔥 SUCCESS! You were fast as lightning and quiet as a ghost.")
        mischief_meter += 40
        wake_o_meter += 10
    else:
        print_delay("💥 THUD! You wiped out into a throw pillow, knocking a remote onto the hardwood floor.")
        mischief_meter += 30
        wake_o_meter += 40

    print(f"Current Stats -> Mischief: {mischief_meter}% | Wake-o-Meter: {wake_o_meter}%\n")

    # Turn 2: Option C (The Pen Slap)
    print(f"--- TURN 2/3 ---")
    print_delay("Executing Option C: The Hallway Pen Slap.")
    print_delay("You trott into the hallway and spot a shiny plastic pen resting on the edge of the table.")
    print_delay("You raise your paw. You look at it. You swat.")
    
    print_delay("...skitter skitter skitter...")
    mischief_meter += 30
    wake_o_meter += 20
    
    print(f"Current Stats -> Mischief: {mischief_meter}% | Wake-o-Meter: {wake_o_meter}%\n")

    # Turn 3: The Climax
    print(f"--- TURN 3/3 ---")
    print_delay("The sky is starting to turn a faint gray. One final move to seal your glory.")
    print("What is your final chaotic act?")
    print("1. Sing the song of your people (Meow loudly at a blank wall)")
    print("2. Puke up a hairball directly onto the bedroom rug")
    
    choice = input("Choose 1 or 2: ")
    print("")

    if choice == "1":
        print_delay("📢 MEOWWWWWW. MREEEEE-OWWWWW!")
        mischief_meter += 35
        wake_o_meter += 30
    elif choice == "2":
        print_delay("🤢 *HACK-HACK-HACK-BLECH.* Perfect placement.")
        mischief_meter += 50
        wake_o_meter += 15
    else:
        print_delay("You hesitated and just stared into space. Classic cat.")
        mischief_meter += 5
        wake_o_meter += 0

    # Final Evaluation
    print("=" * 50)
    print("GAME OVER - THE SUN IS RISING")
    print(f"Final Mischief: {mischief_meter}%")
    print(f"Final Wake-o-Meter: {wake_o_meter}%")
    print("=" * 50)

    if wake_o_meter >= 100:
        print("❌ YOU LOSE: The human woke up, yelled your name, and threw a slipper. You must flee under the bed.")
    elif mischief_meter >= 100:
        print("👑 YOU WIN! Total chaos achieved. You curl up at the foot of the bed, purring innocently as a saint.")
    else:
        print("😐 MEDIOCRE: You didn't cause enough chaos, nor did you get caught. You are left unsatisfied.")

# Run the game
if __name__ == "__main__":
    play_game()
