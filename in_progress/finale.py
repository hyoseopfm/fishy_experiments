import pygame
import vlc
import time
import threading
from tkinter import *
import tkinter.font as tkFont
from tkinter import simpledialog, messagebox, NORMAL, DISABLED, RAISED
import math
import random
import requests
import opensimplex
import numpy as np
import subprocess
from PIL import ImageTk, Image
import os
#from rabbit import Rabbit

root = Tk()

root.title("ђץ๏'ร ς๏๓קยՇєг")

root.geometry("700x700")
root.config(bg="black")
money = 0

def rob_the_bank():
    global money
    background_color = "#A34C4C"
    dice_window = Toplevel()
    dice_window.geometry("940x720")
    dice_window.configure(bg=background_color)
    dice_window.title("Rob za bank")

    result_label = Label(dice_window, bg=background_color)
    result_label.pack()

    rolling_label = Label(dice_window, font=("Helvetica", 14), bg=background_color, fg="white")
    rolling_label.pack(pady=10)

    status_label = Label(dice_window, font=("Helvetica", 16), bg=background_color, fg="white")
    status_label.pack(pady=10)

    # Load dice images and keep reference on dice_window to avoid garbage collection
    dice_window.dice_images = []
    image_paths = [
        "in_progress/dice_one.png", "in_progress/dice_two.png", "in_progress/dice_three.png",
        "in_progress/dice_four.png", "in_progress/dice_five.png", "in_progress/dice_six.png"
    ]
    for path in image_paths:
        img = Image.open(path)
        photo = ImageTk.PhotoImage(img)
        dice_window.dice_images.append(photo)

    def roll_the_dice():
        global money
        roll_duration = 4000
        interval = 100
        dots_interval = 500
        start_time = time.time()

        def animate_dice():
            global money
            elapsed = (time.time() - start_time) * 1000
            if elapsed < roll_duration:
                face = random.choice(dice_window.dice_images)
                result_label.config(image=face)
                result_label.image = face
                dice_window.after(interval, animate_dice)
            else:
                final_num = random.randint(1, 6)
                final_face = dice_window.dice_images[final_num - 1]
                result_label.config(image=final_face)
                result_label.image = final_face
                rolling_label.config(text="")
                if final_num >= 4:
                    money += 500
                    status_label.config(
                        text=f"💰 You rolled {final_num}! You stole $500 and escaped! Expect police at your door..."
                    )
                else:
                    money -= 500
                    status_label.config(
                        text=f"💥 You rolled {final_num}! You lost $500 and got caught!"
                    )

        def animate_text():
            elapsed = (time.time() - start_time) * 1000
            if elapsed < roll_duration:
                dots = int((elapsed // dots_interval) % 4)
                rolling_label.config(text="Rolling" + "." * dots)
                dice_window.after(dots_interval, animate_text)

        animate_dice()
        animate_text()

    def setup_robbery_ui():
        explanation = Label(
            dice_window,
            text="Get a four, five, or six to successfully rob za bank!!!!",
            bg=background_color,
            fg="white",
            font=("Helvetica", 12)
        )
        explanation.pack()

        rob_roll = Button(
            dice_window,
            text="Roll the dice",
            bg="white",
            activebackground="Blue",
            command=roll_the_dice
        )
        rob_roll.pack(pady=5)

    rob_the_bank_button = Button(
        dice_window,
        text="Rob the bank",
        bg="white",
        activebackground="Red",
        font=("Arial", 14),
        command=setup_robbery_ui
    )
    rob_the_bank_button.pack(pady=20)

    dice_window.mainloop()
def open_top_ten_window_yay():
    url = "https://top-spotify-songs-in-73-countries.p.rapidapi.com/list"

    payload = {
        "page": "1"
    }
    headers = {
        "x-rapidapi-key": "fcfafdf2fdmshb8c71d882f91dbap1f3de0jsn796e151759da",
        "x-rapidapi-host": "top-spotify-songs-in-73-countries.p.rapidapi.com",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)
    top_ten = (response.json())

    myList = top_ten['result']['data']
    element = myList[0]
    element['name']
    top_songs_window=Tk()
    top_songs_window.title("Top Songs Today")
    for i in range(min(10, len(myList))):
        song_element = myList[i]
        if 'name' in song_element and 'artists' in song_element:
            music_name = song_element['name']
            artist_name = song_element['artists']
            #print(f"{i+1}. Song: {music_name}, Artist: {artist_name}")
            top_ten_songs = Label(top_songs_window, text=(f"{i+1}. Song: {music_name}, Artists: {artist_name}"))
            top_ten_songs.pack()
    top_songs_window.mainloop()
def open_bank_window():
    class BankAccount:
        def __init__(self, initial_balance=0):
            if initial_balance < 0:
                raise ValueError("Initial balance cannot be negative.")
            self.balance = initial_balance
            #money += self.balance

        def deposit(self, amount):
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            self.balance += amount
            return self.balance

        def withdraw(self, amount):
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if amount > self.balance:
                raise ValueError("Insufficient funds.")
            self.balance -= amount
            return self.balance

        def get_balance(self):
            return self.balance


    class BankApp:
        def __init__(self, banka):
            self.banka = banka
            self.banka.title("Bank of Hyomo")
            self.banka.geometry("400x350")
            self.banka.resizable(False, False)

            self.account = None

            self.banka.configure(bg="#e0f7fa")

            self.label_balance = Label(
                banka,
                text="Balance: N/A",
                font=("Arial", 16, "bold"),
                fg="#0056b3",
                bg="#e0f7fa",
                pady=10
            )
            self.label_balance.pack()

            self.button_create_account = Button(
                banka,
                text="Create New Account",
                command=self.create_account,
                font=("Arial", 12),
                activebackground="blue", activeforeground="white",
                relief=RAISED, bd=3,
                width=20, height=2
            )
            self.button_create_account.pack(pady=5)

            self.button_deposit = Button(
                banka,
                text="Deposit",
                command=self.deposit,
                state=DISABLED,
                font=("Arial", 12),
                activebackground="green", activeforeground="white",
                relief=RAISED, bd=3,
                width=20, height=2
            )
            self.button_deposit.pack(pady=5)

            self.button_withdraw = Button(
                banka,
                text="Withdraw",
                command=self.withdraw,
                state=DISABLED,
                font=("Arial", 12),
                activebackground="red", activeforeground="white",
                relief=RAISED, bd=3,
                width=20, height=2
            )
            self.button_withdraw.pack(pady=5)

            self.button_check_balance = Button(
                banka,
                text="Check Balance",
                command=self.check_balance,
                state=DISABLED,
                font=("Arial", 12),
                activebackground="purple", activeforeground="white",
                relief=RAISED, bd=3,
                width=20, height=2
            )
            self.button_check_balance.pack(pady=5)

            self.button_rob_the_bank = Button(
                banka,
                text="Rob za bank",
                command=rob_the_bank,
                state=DISABLED,
                font=("Arial", 12),
                activebackground="orange", activeforeground="white",
                relief=RAISED, bd=3,
                width=20, height=2
            )
            self.button_rob_the_bank.pack(pady=5)

            self.label_status = Label(
                banka,
                text="",
                font=("Arial", 10),
                wraplength=350,
                justify=CENTER,
                bg="#e0f7fa",
                pady=10
            )
            self.label_status.pack()

        def create_account(self):
            if self.account:
                messagebox.showinfo("Info", "An account already exists. You can only have one account.")
                self.label_status.config(text="Account already exists.", fg="orange")
                return

            initial_deposit = simpledialog.askfloat(
                "Initial Deposit",
                "Enter initial deposit amount (minimum $0):",
                minvalue=0.0
            )
            if initial_deposit is None:
                self.label_status.config(text="Account creation cancelled.", fg="red")
                return

            try:
                self.account = BankAccount(initial_deposit)
                self.label_status.config(text=f"Account created with initial balance: ${initial_deposit:.2f}", fg="green")
                self.update_balance_label()
                self.button_deposit.config(state=NORMAL)
                self.button_withdraw.config(state=NORMAL)
                self.button_check_balance.config(state=NORMAL)
                self.button_create_account.config(state=DISABLED)
                self.button_rob_the_bank.config(state=NORMAL)
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                self.label_status.config(text=f"Error creating account: {e}", fg="red")
                self.account = None

        def deposit(self):
            if not self.account:
                messagebox.showerror("Error", "No account found. Please create an account first.")
                self.label_status.config(text="Operation failed: No account.", fg="red")
                return

            amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:", minvalue=0.01)
            if amount is None:
                self.label_status.config(text="Deposit cancelled.", fg="red")
                return

            try:
                new_balance = self.account.deposit(amount)
                self.update_balance_label()
                self.label_status.config(text=f"Deposited ${amount:.2f}. New balance: ${new_balance:.2f}", fg="green")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                self.label_status.config(text=f"Deposit failed: {e}", fg="red")

        def withdraw(self):
            if not self.account:
                messagebox.showerror("Error", "No account found. Please create an account first.")
                self.label_status.config(text="Operation failed: No account.", fg="red")
                return

            amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:", minvalue=0.01)
            if amount is None:
                self.label_status.config(text="Withdrawal cancelled.", fg="red")
                return

            try:
                new_balance = self.account.withdraw(amount)
                self.update_balance_label()
                self.label_status.config(text=f"Withdrew ${amount:.2f}. New balance: ${new_balance:.2f}", fg="green")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                self.label_status.config(text=f"Withdrawal failed: {e}", fg="red")

        def check_balance(self):
            if not self.account:
                messagebox.showerror("Error", "No account found. Please create an account first.")
                self.label_status.config(text="Operation failed: No account.", fg="red")
                return

            balance = self.account.get_balance()
            self.update_balance_label()
            self.label_status.config(text=f"Current balance: ${balance:.2f}", fg="blue")

        def update_balance_label(self):
            if self.account:
                balance = self.account.get_balance()
                self.label_balance.config(text=f"Balance: ${balance:.2f}")
            else:
                self.label_balance.config(text="Balance: N/A")

    banka = Tk()
    app = BankApp(banka)
    banka.mainloop()
def open_radio():
    class RadioPlayer:
        def __init__(self, url):
            self.url = url
            self.instance = None
            self.player = None
            self.is_playing_flag = False
            self.playback_thread = None

        def _play_stream(self):
            try:
                self.instance = vlc.Instance()
                self.player = self.instance.media_player_new()
                media = self.instance.media_new(self.url)
                self.player.set_media(media)

                print(f"Attempting to play radio from: {self.url}")
                self.player.play()

                time.sleep(1) 

                if not self.player.is_playing():
                    print("Error: VLC player did not start playing. Check the URL or stream availability.")
                    self.is_playing_flag = False
                    return

                self.is_playing_flag = True
                print("Radio is playing.")

                while self.is_playing_flag and self.player.is_playing():
                    time.sleep(0.1)

            except Exception as e:
                print(f"An unexpected error occurred during playback: {e}")
                self.is_playing_flag = False
            finally:
                self._cleanup_vlc()

        def play(self):
            if not self.is_playing_flag:
                self.playback_thread = threading.Thread(target=self._play_stream)
                self.playback_thread.daemon = True
                self.playback_thread.start()
                print("Starting playback thread...")

        def stop(self):
            if self.is_playing_flag:
                self.is_playing_flag = False
                if self.player:
                    self.player.stop()
                print("Stopping radio playback.")
                if self.playback_thread and self.playback_thread.is_alive():
                    self.playback_thread.join(timeout=1)
                self._cleanup_vlc()

        def _cleanup_vlc(self):
            if self.player:
                self.player.release()
                self.player = None
            if self.instance:
                self.instance.release()
                self.instance = None
            print("VLC resources released.")

        def is_playing(self):
            return self.is_playing_flag and self.player and self.player.is_playing()


    pygame.init()


    WIDTH, HEIGHT = 600, 400
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("rrrradiooooo")


    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 200, 0)
    RED = (200, 0, 0)
    LIGHT_GREEN = (0, 255, 0)
    LIGHT_RED = (255, 0, 0)

    font = pygame.font.Font(None, 50)
    small_font = pygame.font.Font(None, 30)

    RADIO_URL = "http://wumb.streamguys1.com/wumb919fast"
    radio_player = RadioPlayer(RADIO_URL)

    class Button:
        def __init__(self, x, y, width, height, text, color, hover_color, action=None):
            self.rect = pygame.Rect(x, y, width, height)
            self.text = text
            self.color = color
            self.hover_color = hover_color
            self.action = action
            self.current_color = color

        def draw(self, screen):
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.current_color = self.hover_color
            else:
                self.current_color = self.color

            pygame.draw.rect(screen, self.current_color, self.rect)
            text_surf = font.render(self.text, True, BLACK)
            text_rect = text_surf.get_rect(center=self.rect.center)
            screen.blit(text_surf, text_rect)

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    if self.action:
                        self.action()
                    return True
            return False

    start_button = Button(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 70, "Start Radio", GREEN, LIGHT_GREEN, radio_player.play)
    stop_button = Button(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 70, "Stop Radio", RED, LIGHT_RED, radio_player.stop)




    try:
        img = pygame.image.load('radio.png')
        img = pygame.transform.scale(img, (WIDTH, HEIGHT)) 
    except pygame.error as e:
        print(f"Warning: Could not load image 'Final_project/radio.png': {e}")
        img = None 

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            start_button.handle_event(event)
            stop_button.handle_event(event)


        SCREEN.fill(WHITE) 

        if img: 
            SCREEN.blit(img, (0, 0))


        status_text = "Status: "
        if radio_player.is_playing():
            status_text += "Playing :)"
            status_color = GREEN
        else:
            status_text += "stopped. :("
            status_color = RED

        status_surf = small_font.render(status_text, True, status_color)
        status_rect = status_surf.get_rect(center=(WIDTH // 2, 50))
        SCREEN.blit(status_surf, status_rect)


        start_button.draw(SCREEN)
        stop_button.draw(SCREEN)

        pygame.display.flip() 



    radio_player.stop()
    pygame.quit()
    print("Pygame window closed.")
def open_radio_window():
    moosic = Tk()
    moosic.title("moosic stats & more")
    moosic_button = Button(moosic, text="Top 10 music", activebackground="Green",command=open_top_ten_window_yay)
    moosic_button.pack()
    radio_button = Button(moosic, text="Radio", activebackground="Red",command=open_radio)
    radio_button.pack()
    moosic.mainloop()
def open_rabbit_window():
    class Rabbit(pygame.sprite.Sprite):
        def __init__(self, color, width, height):
            super().__init__()

            rabbit_image = pygame.image.load('rabbit.png').convert_alpha()
            self.image = pygame.transform.scale(rabbit_image, (40,40))

            self.rect = self.image.get_rect()

            self.change_x = 0
            self.change_y = 0

        def update(self, world_width, world_height):
            self.rect.x += self.change_x
            self.rect.y += self.change_y

            #This is the boundary for the rabbit player down below. Don't change this.
            self.rect.left = max(0, self.rect.left)
            self.rect.right = min(world_width, self.rect.right)
            self.rect.top = max(0, self.rect.top)
            self.rect.bottom = min(world_height, self.rect.bottom)


            self.change_x = 0
            self.change_y = 0

        def moveLeft(self, pixels):
            self.change_x = -pixels

        def moveRight(self, pixels):
            self.change_x = pixels

        def moveForward(self, pixels):
            self.change_y = -pixels

        def moveBackward(self, pixels):
            self.change_y = pixels

    class Water_Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            original_image = pygame.image.load('water_bunny.png').convert_alpha() # Load with convert_alpha for transparency
            self.image = pygame.transform.scale(original_image, (40,40)) # Resize
            self.rect = self.image.get_rect() # Get the rect from the resized image
            
            self.dx = random.choice([-1, 1]) * random.randint(1, 2)
            self.dy = random.choice([-1, 1]) * random.randint(1, 2)

        def update(self, world_width, world_height):
            self.rect.x += self.dx 
            self.rect.y += self.dy 

            if self.rect.left < 0 or self.rect.right > world_width:
                self.dx *= -1 
            if self.rect.top < 0 or self.rect.bottom > world_height:
                self.dy *= -1 

            self.rect.left = max(0, self.rect.left)
            self.rect.right = min(world_width, self.rect.right)
            self.rect.top = max(0, self.rect.top)
            self.rect.bottom = min(world_height, self.rect.bottom)
            
    class Mountain_Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            original_rock_image = pygame.image.load('rock_bunny-removebg-preview.png').convert_alpha()
            self.image = pygame.transform.scale(original_rock_image, (40,40))
            self.rect = self.image.get_rect()
            
            self.dx = random.choice([-1, 1]) * random.randint(1, 2)
            self.dy = random.choice([-1, 1]) * random.randint(1, 2)

        def update(self, world_width, world_height):
            self.rect.x += self.dx
            self.rect.y += self.dy

            if self.rect.left < 0 or self.rect.right > world_width:
                self.dx *= -1 
            if self.rect.top < 0 or self.rect.bottom > world_height:
                self.dy *= -1 

            self.rect.left = max(0, self.rect.left)
            self.rect.right = min(world_width, self.rect.right)
            self.rect.top = max(0, self.rect.top)
            self.rect.bottom = min(world_height, self.rect.bottom)
    class Sand_Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            original_sand_image = pygame.image.load('sand_bunny.png').convert_alpha()
            self.image = pygame.transform.scale(original_sand_image, (90,90))
            self.rect = self.image.get_rect()
            
            self.dx = random.choice([-1, 1]) * random.randint(1, 2)
            self.dy = random.choice([-1, 1]) * random.randint(1, 2)

        def update(self, world_width, world_height):
            self.rect.x += self.dx
            self.rect.y += self.dy

            if self.rect.left < 0 or self.rect.right > world_width:
                self.dx *= -1 
            if self.rect.top < 0 or self.rect.bottom > world_height:
                self.dy *= -1 

            self.rect.left = max(0, self.rect.left)
            self.rect.right = min(world_width, self.rect.right)
            self.rect.top = max(0, self.rect.top)
            self.rect.bottom = min(world_height, self.rect.bottom)


    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Rabbit Wars")
    
    GREEN = (20, 255, 140)
    GREY = (210, 210, 210)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    PURPLE = (255, 0, 255)
    DARK_GREEN = (0, 101, 24)
    BLACK = (0, 0, 0)

    WORLD_WIDTH = 1200
    WORLD_HEIGHT = 1200

    opensimplex.seed(np.random.randint(0, 100000))

    SCALE = 1000
    OCTAVES = 6
    PERSISTENCE = 0.5
    LACUNARITY = 2.0

    def generate_noise_map_opensimplex(width, height):
        start_time = time.time()
        world_data = np.zeros((width, height))

        for y in range(height):
            for x in range(width):
                amplitude = 1.0
                frequency = 1.0 / SCALE
                total_noise = 0.0
                max_amplitude = 0.0

                for i in range(OCTAVES):
                    total_noise += opensimplex.noise2(x * frequency, y * frequency) * amplitude
                    max_amplitude += amplitude

                    amplitude *= PERSISTENCE
                    frequency *= LACUNARITY

                normalized_value = (total_noise / max_amplitude + 1) / 2.0
                world_data[x, y] = normalized_value
        end_time = time.time()
        print(f"Noise map generation took: {end_time - start_time:.4f} seconds")
        return world_data

    def create_terrain_surface(noise_data, width, height):
        start_time = time.time()
        surface = pygame.Surface((width, height))
        pixel_array = pygame.PixelArray(surface)

        for y in range(height):
            for x in range(width):
                noise_val = noise_data[x, y]

                color = BLACK
                if noise_val < 0.3:
                    color = (0, 0, 150)
                elif 0.3 <= noise_val < 0.4:
                    color = (0, 0, 255)
                elif 0.4 <= noise_val < 0.45:
                    color = (240, 240, 100)
                elif 0.45 <= noise_val < 0.65:
                    color = (0, 150, 0)
                elif 0.65 <= noise_val < 0.8:
                    color = (100, 100, 0)
                elif 0.8 <= noise_val < 0.9:
                    color = (150, 150, 150)
                else:
                    color = (255, 255, 255)

                pixel_array[x, y] = color
        pixel_array.close()

        surface = surface.convert()
        
        end_time = time.time()
        print(f"Terrain surface creation took: {end_time - start_time:.4f} seconds")
        return surface

    print("Starting terrain generation... ... ...")
    time.sleep(3)
    print("This might take a while........ heeeellllp meeeeeeeee")
    generated_noise_map = generate_noise_map_opensimplex(WORLD_WIDTH, WORLD_HEIGHT)
    print("Noise map generation complete.")

    print("Starting terrain surface creation...")
    terrain_surface = create_terrain_surface(generated_noise_map, WORLD_WIDTH, WORLD_HEIGHT)
    print("Terrain surface creation complete.")

    all_sprites_list = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    
    spawn_timer_water_enemies = 0
    spawn_interval_water_enemies = 1000
    spawn_timer_mountain_enemies = 0
    spawn_interval_mountain_enemies = 1500
    spawn_timer_sand_enemies = 0
    spawn_interval_sand_enemies = 20000

    playerRabbit = Rabbit(RED, 20, 30)
    playerRabbit.rect.x = WORLD_WIDTH // 2
    playerRabbit.rect.y = WORLD_HEIGHT // 2
    all_sprites_list.add(playerRabbit)

    carryOn = True
    clock = pygame.time.Clock()

    camera_x = 0
    camera_y = 0

    font = pygame.font.Font(None, 74)

    game_over = False
    water_enemy_death = False
    mountain_enemy_death = False
    sand_enemy_death = False

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    carryOn = False
                if game_over and event.key == pygame.K_r:
                    playerRabbit.rect.x = WORLD_WIDTH // 2
                    playerRabbit.rect.y = WORLD_HEIGHT // 2
                    enemies.empty() 
                    all_sprites_list.empty() 
                    all_sprites_list.add(playerRabbit)
                    spawn_timer_water_enemies = 0 
                    spawn_timer_mountain_enemies = 0
                    spawn_timer_sand_enemies = 0
                    game_over = False
                    water_enemy_death = False 
                    mountain_enemy_death = False
                    sand_enemy_death = False
            elif event.type == pygame.VIDEORESIZE:
                screen_width, screen_height = event.size
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                playerRabbit.moveLeft(5)
            if keys[pygame.K_RIGHT]:
                playerRabbit.moveRight(5)
            if keys[pygame.K_UP]:
                playerRabbit.moveForward(5)
            if keys[pygame.K_DOWN]:
                playerRabbit.moveBackward(5)
            
            spawn_timer_water_enemies += clock.get_time()
            if spawn_timer_water_enemies > spawn_interval_water_enemies:
                spawn_timer_water_enemies = 0
                found_spawn_point = False
                attempts = 0
                max_attempts = 100
                while not found_spawn_point and attempts < max_attempts:
                    world_spawn_x = random.randint(0, WORLD_WIDTH - 30)
                    world_spawn_y = random.randint(0, WORLD_HEIGHT - 30)

                    if 0 <= world_spawn_x < WORLD_WIDTH and 0 <= world_spawn_y < WORLD_HEIGHT:
                        noise_val = generated_noise_map[world_spawn_x, world_spawn_y]

                        if noise_val < 0.4:
                            water_enemy = Water_Enemy()
                            water_enemy.rect.x = world_spawn_x
                            water_enemy.rect.y = world_spawn_y
                            all_sprites_list.add(water_enemy)
                            enemies.add(water_enemy)
                            found_spawn_point = True
                    attempts += 1


            spawn_timer_mountain_enemies += clock.get_time()
            if spawn_timer_mountain_enemies > spawn_interval_mountain_enemies:
                spawn_timer_mountain_enemies = 0

                found_spawn_point_m = False
                attempts_m = 0
                max_attempts_m = 100

                while not found_spawn_point_m and attempts_m < max_attempts_m:
                    world_spawn_x = random.randint(0, WORLD_WIDTH - 30)
                    world_spawn_y = random.randint(0, WORLD_HEIGHT - 30)

                    if 0 <= world_spawn_x < WORLD_WIDTH and 0 <= world_spawn_y < WORLD_HEIGHT:
                        noise_val = generated_noise_map[world_spawn_x, world_spawn_y]

                        if noise_val >= 0.65 and noise_val < 0.9:
                            mountain_enemy = Mountain_Enemy()
                            mountain_enemy.rect.x = world_spawn_x
                            mountain_enemy.rect.y = world_spawn_y
                            all_sprites_list.add(mountain_enemy)
                            enemies.add(mountain_enemy)
                            found_spawn_point_m = True
                    attempts_m += 1  #HELLLLP 
            
            spawn_timer_sand_enemies += clock.get_time()
            if spawn_timer_sand_enemies > spawn_interval_sand_enemies:
                spawn_timer_sand_enemies = 0

                found_spawn_point_s = False
                attempts_s = 0
                max_attempts_s = 100

                while not found_spawn_point_s and attempts_s < max_attempts_s:
                    world_spawn_x = random.randint(0, WORLD_WIDTH - 30)
                    world_spawn_y = random.randint(0, WORLD_HEIGHT - 30)

                    if 0 <= world_spawn_x < WORLD_WIDTH and 0 <= world_spawn_y < WORLD_HEIGHT:
                        noise_val = generated_noise_map[world_spawn_x, world_spawn_y]

                        if noise_val >= 0.4 and noise_val < 0.45:
                            sand_enemy = Sand_Enemy()
                            sand_enemy.rect.x = world_spawn_x
                            sand_enemy.rect.y = world_spawn_y
                            all_sprites_list.add(sand_enemy)
                            enemies.add(sand_enemy)
                            found_spawn_point_s = True
                    attempts_s += 1
                if not found_spawn_point_s:
                    print("Could not find a beach for the sand guy's vacation :((((")

            for sprite in all_sprites_list:
                # All sprites should update using their rect, not image.
                # The Water_Enemy had a mix of using self.image.x/y and self.rect.left/right/top/bottom,
                # which is inconsistent and causes issues.
                sprite.update(WORLD_WIDTH, WORLD_HEIGHT)

            collided_enemies = pygame.sprite.spritecollide(playerRabbit, enemies, False) 
            if collided_enemies:
                game_over = True
                for enemy in collided_enemies:
                    if isinstance(enemy, Water_Enemy):
                        water_enemy_death = True
                        mountain_enemy_death = False
                        sand_enemy_death = False # Ensure other death flags are reset
                        print("Death by water enemy!")
                    elif isinstance(enemy, Mountain_Enemy):
                        mountain_enemy_death = True
                        water_enemy_death = False
                        sand_enemy_death = False # Ensure other death flags are reset
                        print("Death by mountain enemy!")
                    elif isinstance(enemy, Sand_Enemy):
                        sand_enemy_death = True
                        mountain_enemy_death = False
                        water_enemy_death = False
                        print("Bro. The sand guy is massive. How did you get hit????")
                    break 

            camera_x = playerRabbit.rect.centerx - screen_width // 2
            camera_y = playerRabbit.rect.centery - screen_height // 2

            camera_x = max(0, min(camera_x, WORLD_WIDTH - screen_width))
            camera_y = max(0, min(camera_y, WORLD_HEIGHT - screen_height))

        screen.fill(BLACK)

        screen.blit(terrain_surface, (-camera_x, -camera_y))


        pygame.draw.rect(screen, GREY, [40 - camera_x, 0 - camera_y, 200, 300])
        pygame.draw.line(screen, WHITE, [140 - camera_x, 0 - camera_y], [140 - camera_x, 300 - camera_y], 5)

        for sprite in all_sprites_list:
            screen.blit(sprite.image, (sprite.rect.x - camera_x, sprite.rect.y - camera_y))

        if game_over:
            game_over_text = ""
            if water_enemy_death: 
                game_over_text = font.render("Game Over! Death by water enemy :P", True, RED)
            elif mountain_enemy_death:
                game_over_text = font.render("Game Over! Death by mountain enemy :P", True, RED)
            elif sand_enemy_death:
                game_over_text = font.render("GAME OVER. Death by Sand guy.", True, RED)

            restart_text = font.render("Press R to restart.", True, WHITE) 
            game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2 - 30)) 
            restart_rect = restart_text.get_rect(center=(screen_width // 2, screen_height // 2 + 30)) 
            screen.blit(game_over_text, game_over_rect)
            screen.blit(restart_text, restart_rect)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
def open_asteroids_window():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    SPACE_DEEP_BLUE = (10, 10, 30)
    STAR_WHITE = (200, 200, 255)
    ASTEROID_GREY = (100, 100, 100)
    ASTEROID_DARK_GREY = (60, 60, 60)
    PLAYER_SHIP_BLUE = (50, 150, 255)
    PLAYER_THRUSTER_ORANGE = (255, 150, 0)
    PROJECTILE_LASER_RED = (255, 50, 50)
    UI_GREEN = (0, 255, 0)
    GAME_OVER_RED = (255, 0, 0)
    GROUND_FOREST_GREEN = (30, 80, 30)
    GROUND_DARK_GREEN = (15, 40, 15)
    HORIZON_BLUE = (50, 100, 150)

    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT - 70
    player_angle = math.pi / 2
    player_speed = 5
    player_width = 30
    player_height = 40
    player_lives = 3

    projectiles = []
    projectile_speed = 15
    projectile_radius = 4

    last_shot_time = 0
    shot_cooldown = 500 #500 milliseconds

    asteroids = []
    asteroid_min_speed = 1
    asteroid_max_speed = 12
    asteroid_min_radius = 15
    asteroid_max_radius = 60
    asteroid_spawn_rate = 10
    asteroid_spawn_counter = 0

    score = 0
    game_over = False
    font = pygame.font.Font(None, 36)
    large_font = pygame.font.Font(None, 72)
    medium_font = pygame.font.Font(None, 48)

    stars = []
    for _ in range(100):
        stars.append({
            'x': random.randint(0, SCREEN_WIDTH),
            'y': random.randint(0, SCREEN_HEIGHT // 3),
            'radius': random.uniform(1, 2.5),
            'alpha': random.randint(100, 255)
        })

    def draw_ground(surface):
        horizon_y = SCREEN_HEIGHT // 3

        surface.fill(SPACE_DEEP_BLUE)

        for star in stars:
            s = pygame.Surface((star['radius'] * 2, star['radius'] * 2), pygame.SRCALPHA)
            pygame.draw.circle(s, (STAR_WHITE[0], STAR_WHITE[1], STAR_WHITE[2], star['alpha']), (star['radius'], star['radius']), star['radius'])
            surface.blit(s, (star['x'] - star['radius'], star['y'] - star['radius']))
            star['alpha'] = max(100, min(255, star['alpha'] + random.randint(-10, 10)))

        for i in range(50):
            alpha = int(255 * (1 - i / 50))
            color = (HORIZON_BLUE[0], HORIZON_BLUE[1], HORIZON_BLUE[2], alpha)
            pygame.draw.line(surface, color, (0, horizon_y + i), (SCREEN_WIDTH, horizon_y + i), 1)

        pygame.draw.rect(surface, GROUND_FOREST_GREEN, (0, horizon_y, SCREEN_WIDTH, SCREEN_HEIGHT - horizon_y))

        for i in range(1, 20):
            y_pos = horizon_y + (SCREEN_HEIGHT - horizon_y) * (i / 20.0)**2
            color_intensity_factor = i / 20.0
            line_color = (
                int(GROUND_DARK_GREEN[0] * (1 - color_intensity_factor) + GROUND_FOREST_GREEN[0] * color_intensity_factor),
                int(GROUND_DARK_GREEN[1] * (1 - color_intensity_factor) + GROUND_FOREST_GREEN[1] * color_intensity_factor),
                int(GROUND_DARK_GREEN[2] * (1 - color_intensity_factor) + GROUND_FOREST_GREEN[2] * color_intensity_factor)
            )
            pygame.draw.line(surface, line_color, (0, y_pos), (SCREEN_WIDTH, y_pos), 2)

    def draw_player(surface, x, y, width, height):
        points = [
            (x + width // 2, y),
            (x, y + height),
            (x + width, y + height)
        ]
        pygame.draw.polygon(surface, PLAYER_SHIP_BLUE, points)

        thruster_points = [
            (x + width // 2, y + height + 5),
            (x + width // 4, y + height),
            (x + width * 3 // 4, y + height)
        ]
        pygame.draw.polygon(surface, PLAYER_THRUSTER_ORANGE, thruster_points)

    def draw_asteroid(surface, x, y, radius):
        num_points = random.randint(8, 12)
        angle_step = 2 * math.pi / num_points
        points = []
        for i in range(num_points):
            angle = i * angle_step
            r = radius * random.uniform(0.8, 1.1)
            px = x + r * math.cos(angle)
            py = y + r * math.sin(angle)
            points.append((px, py))

        pygame.draw.polygon(surface, ASTEROID_GREY, points)
        pygame.draw.circle(surface, ASTEROID_DARK_GREY, (int(x), int(y)), int(radius * 0.7))

    def shoot_projectile(x, y, angle):
        start_x = x + player_width // 2
        start_y = y - 5
        projectiles.append({
            'x': start_x,
            'y': start_y,
            'vx': 0,
            'vy': -projectile_speed,
            'flash_timer': 5
        })

    def spawn_asteroid():
        radius = random.randint(asteroid_min_radius, asteroid_max_radius)
        x = random.randint(radius, SCREEN_WIDTH - radius)
        y = -radius
        speed = random.uniform(asteroid_min_speed, asteroid_max_speed)
        asteroids.append({
            'x': x,
            'y': y,
            'radius': radius,
            'speed': speed
        })

    def check_collision(obj1_x, obj1_y, obj1_radius, obj2_x, obj2_y, obj2_width, obj2_height):
        closest_x = max(obj2_x, min(obj1_x, obj2_x + obj2_width))
        closest_y = max(obj2_y, min(obj1_y, obj2_y + obj2_height))

        distance_x = obj1_x - closest_x
        distance_y = obj1_y - closest_y
        distance_squared = (distance_x * distance_x) + (distance_y * distance_y)

        return distance_squared < (obj1_radius * obj1_radius)

    running = True
    clock = pygame.time.Clock()

    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if not game_over and event.key == pygame.K_SPACE:
                    if current_time - last_shot_time > shot_cooldown:
                        shoot_projectile(player_x, player_y, player_angle)
                        last_shot_time = current_time
                if game_over and event.key == pygame.K_r:
                    player_x = SCREEN_WIDTH // 2
                    player_y = SCREEN_HEIGHT - 70
                    player_lives = 3
                    projectiles.clear()
                    asteroids.clear()
                    score = 0
                    game_over = False
                    asteroid_spawn_counter = 0
                    last_shot_time = 0

        if not game_over:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player_x -= player_speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player_x += player_speed
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                player_y -= player_speed
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                player_y += player_speed

            player_x = max(0, min(player_x, SCREEN_WIDTH - player_width))
            player_y = max(0, min(player_y, SCREEN_HEIGHT - player_height))

            asteroid_spawn_counter += 1
            if asteroid_spawn_counter >= asteroid_spawn_rate:
                spawn_asteroid()
                asteroid_spawn_counter = 0

            for p in projectiles[:]:
                p['x'] += p['vx']
                p['y'] += p['vy']
                if 'flash_timer' in p and p['flash_timer'] > 0:
                    p['flash_timer'] -= 1

                if p['y'] < 0 or p['y'] > SCREEN_HEIGHT or p['x'] < 0 or p['x'] > SCREEN_WIDTH:
                    projectiles.remove(p)

            for a in asteroids[:]:
                a['y'] += a['speed']

                for p_idx, p in enumerate(projectiles[:]):
                    dist = math.hypot(p['x'] - a['x'], p['y'] - a['y'])
                    if dist < projectile_radius + a['radius']:
                        try:
                            projectiles.remove(p)
                        except ValueError:
                            pass

                        if a in asteroids:
                            asteroids.remove(a)
                        score += 10
                        break

                if a in asteroids and check_collision(a['x'], a['y'], a['radius'], player_x, player_y, player_width, player_height):
                    if a in asteroids:
                        asteroids.remove(a)
                        player_lives -= 1
                        if player_lives <= 0:
                            game_over = True

                if a in asteroids and a['y'] > SCREEN_HEIGHT + a['radius']:
                    if a in asteroids:
                        asteroids.remove(a)

        SCREEN.fill(SPACE_DEEP_BLUE)

        draw_ground(SCREEN)

        if not game_over:
            draw_player(SCREEN, player_x, player_y, player_width, player_height)

        for p in projectiles:
            if 'flash_timer' in p and p['flash_timer'] > 0:
                flash_color = (255, 255, 200)
                pygame.draw.circle(SCREEN, flash_color, (int(p['x']), int(p['y'])), projectile_radius * 1.5)
            pygame.draw.circle(SCREEN, PROJECTILE_LASER_RED, (int(p['x']), int(p['y'])), projectile_radius)

        for a in asteroids:
            draw_asteroid(SCREEN, a['x'], a['y'], a['radius'])

        score_text = font.render(f"Score: {score}", True, UI_GREEN)
        lives_text = font.render(f"Lives: {player_lives}", True, UI_GREEN)
        SCREEN.blit(score_text, (10, 10))
        SCREEN.blit(lives_text, (SCREEN_WIDTH - lives_text.get_width() - 10, 10))

        if game_over:
            game_over_text = large_font.render("GAME OVER", True, GAME_OVER_RED)
            restart_text = medium_font.render("Press 'R' to Restart", True, STAR_WHITE)

            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))

            glow_surface = pygame.Surface(game_over_rect.size, pygame.SRCALPHA)
            pygame.draw.rect(glow_surface, (GAME_OVER_RED[0], GAME_OVER_RED[1], GAME_OVER_RED[2], 50), glow_surface.get_rect(), border_radius=10)
            SCREEN.blit(glow_surface, game_over_rect.topleft)

            SCREEN.blit(game_over_text, game_over_rect)
            SCREEN.blit(restart_text, restart_rect)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
def open_aurora_window():
    import asyncio
    import json
    import logging
    import time

    import aiohttp
    from aiohttp import ClientError

    APIUrl = "https://services.swpc.noaa.gov/json/ovation_aurora_latest.json"

    _LOGGER = logging.getLogger("aurora")
    _LOGGER.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    _LOGGER.addHandler(handler)


    class AuroraForecast:
        forecast_dict = {}
        last_update_time = None
        lock = asyncio.Lock()

        def __init__(self, session: aiohttp.ClientSession = None):
            self.retry = 5

            if session:
                self._session = session
            else:
                self._session = aiohttp.ClientSession()

        async def close(self):
            await self._session.close()

        async def get_forecast_data(self, latitude: float, longitude: float):
            await AuroraForecast.lock.acquire()

            try:
                if longitude < 0:
                    longitude = 360 + longitude

                if AuroraForecast.last_update_time is None or (
                    time.monotonic() - AuroraForecast.last_update_time > 5 * 60
                ) or not AuroraForecast.forecast_dict:
                    AuroraForecast.forecast_dict = {}

                    _LOGGER.debug("Fetching forecast data from NOAA")
                    try:
                        async with self._session.get(APIUrl) as resp:
                            resp.raise_for_status()
                            forecast_data = await resp.json()

                            for forecast_item in forecast_data["coordinates"]:
                                if forecast_item[2] > 0:
                                    AuroraForecast.forecast_dict[
                                        (round(forecast_item[0]), round(forecast_item[1]))
                                    ] = forecast_item[2]

                            AuroraForecast.last_update_time = time.monotonic()
                            _LOGGER.debug("Successfully fetched forecast data from NOAA")

                    except ClientError as error:
                        _LOGGER.error("Error fetching forecast from NOAA: %s", error)
                    except json.JSONDecodeError as error:
                        _LOGGER.error("Error decoding JSON from NOAA response: %s", error)
                    except KeyError:
                        _LOGGER.error("Unexpected data structure from NOAA API. Missing 'coordinates' key.")

                probability = AuroraForecast.forecast_dict.get(
                    (round(longitude), round(latitude)), 0
                )
                _LOGGER.debug(
                    "Forecast probability: %s at (long, lat) = (%s, %s)",
                    probability,
                    round(longitude),
                    round(latitude),
                )
                return probability

            finally:
                AuroraForecast.lock.release()

    async def get_forecast(latitude, longitude):
        aurora_service = AuroraForecast()
        forecast_percentage = await aurora_service.get_forecast_data(latitude=latitude, longitude=longitude)
        await aurora_service.close()
        return forecast_percentage

    def main():
        print("Hello Dudes and Dudettes")
        
        aurora_predicter = Tk()
        aurora_predicter.title("Aurora Forecaster")
        aurora_predicter.geometry('500x300')
        aurora_predicter.resizable(True, True)
        aurora_predicter.config(bg="#F0F0F0")

        main_frame = Frame(aurora_predicter, bg="#F0F0F0", padx=20, pady=20)
        main_frame.pack(expand=True, anchor="center")

        title_label = Label(main_frame, text="Aurora Forecast", font=("Helvetica Neue", 24, "bold"), bg="#F0F0F0", fg="#333")
        title_label.pack(pady=10)

        latitude_entry = Entry(aurora_predicter)
        latitude_entry.pack()

        def get_latitude():
            text = latitude_entry.get()
            print("Latitude: ", text)
            text = latitude_input

        latitude_button = Button(aurora_predicter, text="Get Latitude", command = get_latitude)
        latitude_button.pack()

        longitude_entry = Entry(aurora_predicter)
        longitude_entry.pack()

        def get_longitude():
            text_lo = longitude_entry.get()
            print("Longitude: ", text_lo)
            text_lo = longitude_input

        longitude_button = Button(aurora_predicter, text="Get longitude", command = get_longitude)
        longitude_button.pack()

        latitude_input = 44.2272
        longitude_input = 71.7479

        percent_text = "Forecast Chance: ..."
        percent_label = Label(main_frame, text=percent_text, font=("Helvetica Neue", 18), bg="#F0F0F0", fg="#555")
        percent_label.pack(pady=20)

        status_label = Label(main_frame, text="Fetching data...", font=("Helvetica Neue", 12), bg="#F0F0F0", fg="#888")
        status_label.pack(pady=5)

        status_label.config(text=f"For Lat: {latitude_input:.2f}, Long: {longitude_input:.2f}")

        def update_long_lat():
            nonlocal latitude_input, longitude_input
            longitude_input = float(longitude_entry.get())
            latitude_input = float(latitude_entry.get())
            print("update_long_lat")
            print(f"Longitude: {longitude_input}")
            print(f"Latitude: {latitude_input}")
            print(f"Longitude: {type(longitude_input)}")
            print(f"Latitude: {type(latitude_input)}")
            forecast = asyncio.run(get_forecast(latitude_input, longitude_input))
            print(forecast)
            percent_label.config(text=f"Forecast Chance: {forecast}%")
            status_label.config(text=f"For Lat: {latitude_input:.2f}, Long: {longitude_input:.2f}")

        update_long_lat_button = Button(aurora_predicter, text = "Update Long&Lat", command = update_long_lat)
        update_long_lat_button.pack()

        forecast = asyncio.run(get_forecast(latitude_input, longitude_input))
        percent_label.config(text=f"Forecast Chance: {forecast}%")
        status_label.config(text=f"For Lat: {latitude_input:.2f}, Long: {longitude_input:.2f}")

        print(f"Forecast Chance: {forecast}% for Lat: {latitude_input}, Long: {longitude_input}")

        aurora_predicter.mainloop()

    if __name__ == '__main__':
        #asyncio.run(main())
        main()
def open_flight_sim_window():
    import tkinter as tk
    import subprocess
    import os

    def launch_telnet():
        try:
            subprocess.Popen(["fgfs", "--telnet=5400", "EHAM"])
            #os.system("fgfs --aircraft=A300 --airport=KLAX")
            print("FlightGear launched with telnet on port 5400!")
        except Exception as e:
            print(f"Launch failed: {e}")

    root = tk.Tk()
    root.title("Simple FlightGear Launcher")
    root.geometry("300x150")

    button = tk.Button(root, text="Flight sim", font=("Arial", 14), command=launch_telnet)
    button.pack(expand=True)

    root.mainloop()
def open_rpc_window():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Rock, Paper, Scissors")

    rock = pygame.transform.scale(pygame.image.load('in_progress/rock.png'), (100, 200))
    paper = pygame.transform.scale(pygame.image.load('in_progress/paper.png'), (100, 200))
    scissors = pygame.transform.scale(pygame.image.load('in_progress/scissors.png'), (100, 200))

    rock_o = pygame.transform.scale(pygame.image.load('in_progress/rock.png'), (100, 200))
    paper_o = pygame.transform.scale(pygame.image.load('in_progress/paper.png'), (100, 200))
    scissors_o = pygame.transform.scale(pygame.image.load('in_progress/scissors.png'), (100, 200))


    font = pygame.font.SysFont(None, 32)
    clock = pygame.time.Clock()

    choices = ['rock', 'paper', 'scissors']
    player_choice = None
    opponent_choice = None
    result = ""
    show_result = False

    def draw_text(text, center_x, y):
        label = font.render(text, True, (255, 255, 255))
        rect = label.get_rect(center=(center_x, y))
        screen.blit(label, rect)

    def get_result(player, opponent):
        if player == opponent:
            return "Draw!"
        elif (player == "rock" and opponent == "scissors") or \
             (player == "paper" and opponent == "rock") or \
             (player == "scissors" and opponent == "paper"):
            return "You Win!"
        else:
            return "You Lose!"

    def play_again():
        nonlocal player_choice, opponent_choice, result, show_result
        player_choice = None
        opponent_choice = None
        result = ""
        show_result = False

    running = True
    while running:
        screen.fill((20, 20, 30))
        mx, my = pygame.mouse.get_pos()

        rock_button = pygame.Rect(100, 500, 150, 50)
        paper_button = pygame.Rect(325, 500, 150, 50)
        scissors_button = pygame.Rect(550, 500, 150, 50)
        play_again_button = pygame.Rect(325, 550, 150, 40)

 
        draw_text("Rock", rock_button.centerx, rock_button.top - 25)
        draw_text("Paper", paper_button.centerx, paper_button.top - 25)
        draw_text("Scissors", scissors_button.centerx, scissors_button.top - 25)


        pygame.draw.rect(screen, (70, 70, 200), rock_button)
        pygame.draw.rect(screen, (70, 70, 200), paper_button)
        pygame.draw.rect(screen, (70, 70, 200), scissors_button)

        if show_result:
            pygame.draw.rect(screen, (0, 150, 100), play_again_button)
            draw_text("Play Again", play_again_button.centerx, play_again_button.centery)

 
        if player_choice:
            player_img = {'rock': rock, 'paper': paper, 'scissors': scissors}[player_choice]
            screen.blit(player_img, (100, 150))
            draw_text("You", 175, 130)
        if opponent_choice:
            opp_img = {'rock': rock_o, 'paper': paper_o, 'scissors': scissors_o}[opponent_choice]
            screen.blit(opp_img, (550, 150))
            draw_text("Opponent", 625, 130)

        if result:
            draw_text(result, 400, 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if show_result:
                    if play_again_button.collidepoint(mx, my):
                        play_again()
                elif not show_result:
                    if rock_button.collidepoint(mx, my):
                        player_choice = "rock"
                    elif paper_button.collidepoint(mx, my):
                        player_choice = "paper"
                    elif scissors_button.collidepoint(mx, my):
                        player_choice = "scissors"

                    if player_choice:
                        opponent_choice = random.choice(choices)
                        result = get_result(player_choice, opponent_choice)
                        show_result = True

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
class ClickerGame:
    def __init__(self, master):
        self.master = master
        self.window = Toplevel(self.master)
        self.window.title("Clickerrrrrrr")
        self.window.geometry("400x500")

        pygame.mixer.init()
        self.click_sound = pygame.mixer.Sound("in_progress/click.wav")
        self.upgrade_sound = pygame.mixer.Sound("in_progress/upgrade.wav")

        self.score = 0
        self.points_per_click = 1
        self.upgrade_levels = [0] * 5
        self.upgrade_costs = [10, 50, 200, 1000, 3000]
        self.upgrade_values = [1, 5, 10, 20, 70]
        self.high_score_file = "highscore.txt"
        self.high_score = self.load_high_score()

        # Load images and preserve references
        self.background_images = [
            ImageTk.PhotoImage(Image.open(path).resize((400, 500), Image.LANCZOS))
            for path in [
                "in_progress/space_bg.png",
                "in_progress/mountain_bg.png",
                "in_progress/rage_man.png"
            ]
        ]
        self.click_img = ImageTk.PhotoImage(Image.open("in_progress/crhome_dino.png").resize((100, 100), Image.LANCZOS))
        self.current_bg_index = 0

        self.setup_ui()
        self.window.after(100, self.cycle_background)

    def load_high_score(self):
        if os.path.exists(self.high_score_file):
            try:
                with open(self.high_score_file, "r") as f:
                    return int(f.read())
            except:
                return 0
        return 0

    def setup_ui(self):
        self.bg_label = Label(self.window)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.score_label = Label(self.window, text=f"Score: {self.score}", font=("Arial", 18), bg="#ffffff")
        self.score_label.place(relx=0.5, y=20, anchor="n")

        self.high_score_label = Label(self.window, text=f"High Score: {self.high_score}", font=("Arial", 14), bg="#ffffff")
        self.high_score_label.place(relx=0.5, y=60, anchor="n")

        self.click_button = Button(
            self.window,
            image=self.click_img,
            command=self.click,
            bd=0, highlightthickness=0,
            bg="#ffffff", activebackground="#ffffff"
        )
        self.click_button.image = self.click_img
        self.click_button.place(relx=0.5, rely=0.3, anchor="center")

        self.upgrade_buttons = []
        for i in range(5):
            btn = Button(self.window, text="", font=("Helvetica", 12),
                         command=lambda i=i: self.buy_upgrade(i))
            btn.place(relx=0.5, y=250 + i * 45, anchor="n")
            self.upgrade_buttons.append(btn)

        self.update_ui()

    def cycle_background(self):
        img = self.background_images[self.current_bg_index]
        self.bg_label.config(image=img)
        self.bg_label.image = img
        self.current_bg_index = (self.current_bg_index + 1) % len(self.background_images)
        self.window.after(30000, self.cycle_background)

    def click(self):
        self.score += self.points_per_click
        self.click_sound.play()
        self.update_score()

    def buy_upgrade(self, index):
        cost = self.upgrade_costs[index]
        if self.score >= cost:
            self.score -= cost
            self.upgrade_levels[index] += 1
            self.upgrade_costs[index] = int(self.upgrade_costs[index] * 1.5)
            self.points_per_click += self.upgrade_values[index]
            self.upgrade_sound.play()
            self.update_ui()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")
        if self.score > self.high_score:
            self.high_score = self.score
            with open(self.high_score_file, "w") as f:
                f.write(str(self.high_score))
        self.high_score_label.config(text=f"High Score: {self.high_score}")

    def update_ui(self):
        self.update_score()
        for i in range(5):
            self.upgrade_buttons[i].config(
                text=f"Upgrade {i+1} (+{self.upgrade_values[i]}) - {self.upgrade_costs[i]} pts"
            )

def flight_sim_downloaded():
    flight_sim_button = Button(root, text="Flight_sim", activebackground="yellow", activeforeground="white", bg="Lightgray", disabledforeground="gray",command=open_flight_sim_window)
    flight_sim_button.pack()
def rock_paper_scissors_downloaded():
    rock_paper_scissors_button = Button(root, text="Rock, Paper, Scissors", activebackground="yellow", activeforeground="white", bg="Lightgray", disabledforeground="gray",command=open_rpc_window)
    rock_paper_scissors_button.pack()
def clicker_downloaded():
    clicker_button = Button(root, text="Clicker game", activebackground="yellow", activeforeground="white", bg="Lightgray", disabledforeground="gray",command=lambda: ClickerGame(root))
    clicker_button.pack()
def open_app_store():
    app_store = Tk()
    app_store.title("App store")
    app_flight_install = Button(app_store, text = "Flight simulator (Install)", activebackground="yellow", activeforeground="white", bg="Lightgray", disabledforeground="gray", command=flight_sim_downloaded)
    app_flight_install.pack()
    app_rock_paper_scissors_install = Button(app_store, text = "Rock paper scissors (Install)", activebackground="yellow", activeforeground="white", bg="Lightgray", disabledforeground="gray", command = rock_paper_scissors_downloaded)
    app_rock_paper_scissors_install.pack()
    app_clicker_install = Button(app_store, text = "Clicker (Install)", activebackground="yellow", activeforeground="white", bg="Lightgray", disabledforeground="gray", command = clicker_downloaded)
    app_clicker_install.pack()


w = Label(root, text="๓คเภ ฬเภ๔๏ฬ\n", fg="green", bg = "Black")
w.pack()

bank_of_hyo_button = Button(root, text="Bank of Hyo",activebackground="blue",activeforeground="white",bg="Lightgray",disabledforeground="gray", command=open_bank_window)
bank_of_hyo_button.pack()

radio_button = Button(root, text="Radio",activebackground="cyan",activeforeground="white",bg="Lightgray",disabledforeground="gray", command=open_radio_window)
radio_button.pack()

rabbit_wars_button = Button(root, text="Rabbit Wars",activebackground="green",activeforeground="white",bg="Lightgray",disabledforeground="gray", command=open_rabbit_window)
rabbit_wars_button.pack()

asteroids_button = Button(root, text="Asteroids",activebackground="red",activeforeground="white",bg="Lightgray",disabledforeground="gray", command=open_asteroids_window)
asteroids_button.pack()

aurora_button = Button(root, text="Aurora predicter", activebackground="purple",activeforeground="white", bg="Lightgray", disabledforeground="gray", command=open_aurora_window)
aurora_button.pack()

app_store_button = Button(root, text="App store", activebackground="yellow", activeforeground="white", bg="Lightgray", disabledforeground="gray", command=open_app_store) #ADD command
app_store_button.pack()



root.mainloop()