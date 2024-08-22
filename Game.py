import time
import random
import tkinter as tk
from tkinter import messagebox



class Player:
    def __init__(self):
        self.x = 1
        self.y = 1
        
    def move(self, direction):
        if direction == "up" and self.y > 0:
            self.y -= 1
        elif direction == "down" and self.y < 4:
            self.y += 1
        elif direction == "left" and self.x > 0:
            self.x -= 1
        elif direction == "right" and self.x < 4:
            self.x += 1
class Character:
    def __init__(self, name, x, y, challenge):
        self.name = name
        self.x = x
        self.y = y
        self.challenge = challenge

    def interact(self):
            print(f"You are interacting with {self.name}.")
            self.challenge()

def challenge_1():
    print("Press ENTER 10 times in 10 seconds!")
    input("Press ENTER to start...")
    start_time = time.time()
    count = 0

    while time.time() - start_time < 10:
        input()
        count += 1
        if count >= 10:
            break
    if count >= 10:
        print("Congrats! You`ve completed the challange")
    else:
        print("You failed the challenge!")
        #begginin of challange 2
def challenge_2():
    root = tk.Tk()
    root.title("Click Challange!")

    clicks = 0
    start_time = time.time()
    target_clicks = 10
    challenge_completed = False

    def button_click():
        nonlocal clicks, challenge_completed
        clicks += 1
        if clicks >= target_clicks and not challenge_completed:
            challenge_completed = True
            end_challenge(success=True)

    def end_challenge(success=False):
        nonlocal challenge_completed
        if not challenge_completed:

            elapsed_time = time.time() - start_time
        if success or elapsed_time <= 5:
            messagebox.showinfo("Challenge Complete ", "Congrats! You clicked the button enough times in 5 seconds!")
        else:
            messagebox.showinfo("Challenge failed", "You failed the challenge! Time`s up!")
        challenge_completed = True
        root.destroy()

    button = tk.Button(root, text="Click me!", command=button_click, height=3, width=20)
    button.pack(pady=20)

    root.after(5000, end_challenge)

    root.mainloop()

def challenge_3():
    print("Welcome to the Alchemist's lab! You must choose the correct combination of ingredients to pass, otherwise, you fail.")
    
    ingredients = [
        "Red Herb",
        "Blue Crystal",
        "Yellow Flower",
        "Dragon Scale",
        "Water",
    ]
    correct_combo = {"Red Herb", "Blue Crystal", "Water"}
    
    print("\nIngredients: ")
    for i, ingredient in enumerate(ingredients, 1):
        print(f"{i}. {ingredient}")
    
    selected_ingredients = set()
    start_time = time.time()
    
    while len(selected_ingredients) < 3 and time.time() - start_time < 15:
        try:
            choice = int(input("\nSelect an ingredient by number (1-5): "))
            if 1 <= choice <= 5:
                selected_ingredients.add(ingredients[choice - 1])
                print(f"Selected: {ingredients[choice - 1]}")
            else:
                print("Invalid choice. Select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if selected_ingredients == correct_combo:
        print("\nSuccess! You mixed the correct ingredients and created the potion!")
    else:
        print("\nYou failed. Maybe next time.")
def challenge_4():
    correct_retype = "T3110, k1o43p"
    correct_message = "Hello, player"
    print("You have received a message from the Hacker. Decode it to see it.")
    print("Message: ̵T̴3̴1̶1̷0̶,̵ ̶k̸1̶o̵4̸3̸p̵  (if you have problems reading it in terminal, copy and paste it.)")
    print("Instructions : First, retype the message without the crazy 'font'")
    retype = input("Retype the message using the normal font: \n")

    if retype == correct_retype:
        print("Retyped correctly! But the letters in the message got swapped. \nUse this letter remap instruction: ")
        print("a = p, b = H, c = l, d = r, e = o, f = y, g = u, h = e, i = l, j = y, k = t, l = a, m = n, n = v, o = p, p = r, q = i, r = s, s = g, t = b, u = f, v = c, w = k, x = j, y = d, z = m")
        decode = input("Decoded message: ")
        if decode == correct_message:
            print("Congrats! You decoded the message! The hacker said: " + correct_message)
        else:
            print("Almost there! Try again.")
    else:
        print("Try again.")
        challenge_4()


def display_lobby(player, characters):
    lobby_size = 5
    for y in range(lobby_size):
        for x in range(lobby_size):
            if player.x == x and player.y == y:
                print("[P]", end="")
            elif any(c.x == x and c.y == y for c in characters):
                print("[C]", end="")
            else:
                print("[ ]", end="")
        print()


# main game loop
def main():
    player = Player()
    characters = [
        Character("Bob", 0, 0, challenge_1),
        Character("Clicker", 3, 2, challenge_2),
        Character("Alchemist", 4, 4, challenge_3),
        Character("Hacker", 2, 4, challenge_4)
        
    ]

    while True:
        display_lobby(player, characters)
        action = input("Move (up, down, left, right) or interact (i): ")

        if action in ["up", "down", "left", "right"]:
            player.move(action)
        elif action == "i":
            for character in characters:
                if abs(player.x - character.x) + abs(player.y - character.y) == 1:
                    character.interact()
                    break
            else:
                print("No one to interact with!")
        elif action == "quit":
            print("Exiting game...")
            break
if __name__ == "__main__":
    main()