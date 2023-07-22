import tkinter as tk
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
EGG_WIDTH = 50
EGG_HEIGHT = 50
CATCHER_WIDTH = 100
CATCHER_HEIGHT = 20

class EggCatcherGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Egg Catcher Game")

        self.canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg="light green")
        self.canvas.pack()

        self.catcher_x = SCREEN_WIDTH // 2 - CATCHER_WIDTH // 2
        self.catcher_y = SCREEN_HEIGHT - CATCHER_HEIGHT - 10

        self.egg_x = random.randint(0, SCREEN_WIDTH - EGG_WIDTH)
        self.egg_y = 0
        self.egg_speed = 5

        self.score = 0

        self.is_running = True
        self.root.bind('<Left>', self.move_left)
        self.root.bind('<Right>', self.move_right)

        self.update_game()

    def draw_egg(self):
        self.canvas.create_oval(self.egg_x, self.egg_y, self.egg_x + EGG_WIDTH, self.egg_y + EGG_HEIGHT, fill="white")

    def draw_catcher(self):
        self.canvas.create_oval(self.catcher_x, self.catcher_y, self.catcher_x + CATCHER_WIDTH, self.catcher_y + CATCHER_HEIGHT, fill="brown")

    def move_left(self, event):
        if self.catcher_x > 0:
            self.catcher_x -= 10

    def move_right(self, event):
        if self.catcher_x < SCREEN_WIDTH - CATCHER_WIDTH:
            self.catcher_x += 10

    def update_game(self):
        if self.is_running:
            self.egg_y += self.egg_speed

            # Check if the egg is caught
            if self.catcher_x < self.egg_x + EGG_WIDTH < self.catcher_x + CATCHER_WIDTH and self.catcher_y < self.egg_y + EGG_HEIGHT < self.catcher_y + CATCHER_HEIGHT:
                self.egg_x = random.randint(0, SCREEN_WIDTH - EGG_WIDTH)
                self.egg_y = 0
                self.score += 1

            # Check if the egg fell down
            if self.egg_y > SCREEN_HEIGHT:
                self.egg_x = random.randint(0, SCREEN_WIDTH - EGG_WIDTH)
                self.egg_y = 0

            # Clear the canvas
            self.canvas.delete("all")

            # Draw the game elements
            self.draw_egg()
            self.draw_catcher()

            # Display the score
            self.canvas.create_text(10, 10, text=f"Score: {self.score}", fill="white", anchor="nw")

            # Update the display
            self.root.update()

            # Set the frame rate
            self.root.after(30, self.update_game)

    def stop_game(self):
        self.is_running = False

if __name__ == "__main__":
    root = tk.Tk()
    game = EggCatcherGame(root)
    root.mainloop()
    game.stop_game()
