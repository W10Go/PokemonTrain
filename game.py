from pyboy import PyBoy
from pyboy import WindowEvent
import pyautogui
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand= True)

label = customtkinter.CTkLabel(master=frame, text="LayoutSummary", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

pyboy = PyBoy('./PKR.gb')
botsupport = pyboy.botsupport_manager()
tilemapB = botsupport.tilemap_background()
tilemapW = botsupport.tilemap_window()

auxValues = []
root.update()
while not pyboy.tick():
    MONEY = []
    i = 0xD347
    while i<= 0xD349:
        MONEY.append((pyboy.get_memory_value(i)))
        i = i+1
    
    MENU_DATA = []
    i = 0xCC24
    while i<= 0xCC36:
        MENU_DATA.append((pyboy.get_memory_value(i)))
        i = i+1
    print(MENU_DATA)
    HOOKED_POKEMON = pyboy.get_memory_value(0xD05F) # I don't know how it works
    CURRENT_PLAYER_POS = [pyboy.get_memory_value(0xD35E),pyboy.get_memory_value(0xD361), pyboy.get_memory_value(0xD362)]
    STARTERS_FLAG= pyboy.get_memory_value(0xD5AB)

    #print("Player's ID: ",pyboy.get_memory_value(0xCFD9),"Slot 1: ",pyboy.get_memory_value(0xD16B))
    #print(CURRENT_PLAYER_POS)
    #print(pyboy.get_memory_value(0xD057))
    auxValues = MENU_DATA

    pyboy.tick()
    root.update()
    pass
pyboy.stop()

print(len(auxValues))
pil_image = pyboy.screen_image()
pil_image.save('screenshot.png')

"""
    C103 => Y screen position delta (-1,0 or 1)
    C105 => X screen position delta (-1,0 or 1)
    C109 => Facing direction(0: down, 4: up, 8: left, $c: right)
    D057 => Type of battle(0 is not in battle)

    D05C => music of Gym Leader

    D05E => 1 Critical Hit 2 One-hit KO

    D05F => hooked pokemon // I don't know how it works
    D60D => Have Oak's Parcel

    D356 => Badges

    D35E => Current map ID
    D361 => Y player position
    D362 => X player position

    CFD9 => Player's Pokémon internal ID // not exactly like the pokedex
    CFD8 => Enemy's Pokémon internal ID

    D16B => Pokémon ID Slot 1
    D18C => Pokémon's level of Slot 1
    D197 => Pokémon ID Slot 2
    D1B8 => level Slot 2
    D1C3 => Pokémon ID Slot 3
    D1E4 => level Slot 3
    D1EF => Pokémon ID Slot 4
    D210 => level Slot 4
    D21B => Pokémon ID Slot 5
    D23C => level Slot 5
    D247 => Pokémon ID Slot 6
    D268 => level Slot 6

    D347-D349 => Money
    D5AB => Starters flag // 1 if the profesor moves you to the lab
"""