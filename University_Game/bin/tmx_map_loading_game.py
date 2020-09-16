import cocos
import ctypes
import webbrowser
from cocos import mapcolliders
import pyglet
from pyglet.window import key
from cocos.director import director

import Mini_Games.QuickMath.QuickMath as QM
import Mini_Games.SportHall.sporthall as sh
#import Mini_Games.Buffet.buffet as buffet

img = pyglet.image.load("resources/Guy.png")
img_grid = pyglet.image.ImageGrid(img, 4, 3, 40, 40)
anim = [pyglet.image.Animation.from_image_sequence(img_grid[i * 3:i * 3 + 3], 0.1, True) for i in range(4)]
anim_static = pyglet.image.Animation.from_image_sequence(img_grid[0:3], 0,1)

# ===============================MENU==================================================
class Menu_Scene(cocos.scene.Scene):
    def __init__(self, menus_list):
        super().__init__()
        self.add_menu(menus_list)

    def add_menu(self, menu_list):
        for menu in menu_list:
            self.add(menu)


class Menu_BG(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        menu_bg = cocos.sprite.Sprite("resources/menu_bg.jpg")
        menu_bg.position = menu_bg.width / 2, menu_bg.height / 2
        self.add(menu_bg)


class MainMenu(cocos.menu.Menu):
    def __init__(self):
        super().__init__("Bauman School")

        items = [cocos.menu.MenuItem("New Game", self.on_new_game),
                 cocos.menu.MenuItem("Quit", self.on_quit)]

        self.create_menu(items, cocos.menu.shake(), cocos.menu.shake_back())

    def on_new_game(self):
        director.replace(cocos.scene.Scene(scrollable))

    def on_quit(self):
        director.window.close()


# ===============================END==================================================

# =============================Game-Scene===================================================
class Player(cocos.layer.ScrollableLayer):
    def __init__(self, collision_handler):
        super().__init__()
        img = pyglet.image.load("resources/Guy.png")
        img_grid = pyglet.image.ImageGrid(img, 4, 3, 40, 40)
        anim_static = pyglet.image.Animation.from_image_sequence(img_grid[0:3], 0,1)

        player = cocos.sprite.Sprite(anim_static)
        player.position = (630, 220)
        player.velocity = (0, 0)
        player.state = 'Up'

        player.collide_map = collision_handler

        player.do(Mover())
        player.do(Animation())

        self.add(player)

class Animation(cocos.actions.Action):
    def step(self, dt):
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 200
        vel_y = (keyboard[key.UP] - keyboard[key.DOWN]) * 200

        if vel_x > 0 and self.target.state != "Right":
            self.target.state = 'Right'
            self.target.image = anim[2]


        elif vel_x < 0 and self.target.state != "Left":
            self.target.state = 'Left'
            self.target.image = anim[0]

        elif vel_y > 0 and self.target.state != "Up":
            self.target.state = 'Up'
            self.target.image = anim[1]

        elif vel_y < 0 and self.target.state != "Down":
            self.target.state = 'Down'
            self.target.image = anim[3]

        elif vel_x == 0 and vel_y == 0:
            if self.target.state == 'Down':
                self.target.image = pyglet.image.Animation.from_image_sequence(img_grid[10:11], 0.1, loop=False)
            if self.target.state == 'Left':
                self.target.image = pyglet.image.Animation.from_image_sequence(img_grid[1:2], 0.1, loop=False)
            if self.target.state == 'Up':
                self.target.image = pyglet.image.Animation.from_image_sequence(img_grid[4:5], 0.1, loop=False)
            if self.target.state == 'Right':
                self.target.image = pyglet.image.Animation.from_image_sequence(img_grid[7:8], 0.1, loop=False)


class Mover(cocos.actions.Move):
    def step(self, dt):
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 100
        vel_y = (keyboard[key.UP] - keyboard[key.DOWN]) * 100

        dx = vel_x * dt
        dy = vel_y * dt

        last = self.target.get_rect()

        new = last.copy()
        new.x += dx
        new.y += dy
        #print(new.x, new.y);
        self.target.velocity = self.target.collide_map(last, new, vel_x, vel_y)
        self.target.position = new.center

        scrollable.set_focus(*new.center)
        print(new.x, new.y)
        if (new.x >= 57 and new.x <= 115) and (new.y >= 483 and new.y <= new.y):
            print("IN THE GAME")
            player_choice = ctypes.windll.user32.MessageBoxW(0, "Do you want to proceed", "MATH LESSON", 1)
            if (player_choice == 1):
                print("Yes i want")
                active_scene = QM.Math_Scene()

                director.replace(active_scene)
                print(active_scene)
            else:
                print("No i dont")
                self.target.position = 630, 220
                self.target.state = "Down"
        if (new.x >= 120 and new.x <= 170) and (new.y >= 23 and new.y <= 76):
            print("IN THE GAME")
            player_choice = ctypes.windll.user32.MessageBoxW(0, "Do you want to proceed", "Physics FN4", 1)
            if (player_choice == 1):
                print("Yes i want")
                active_scene = Menu_Scene([Menu_BG(), MainMenu()])
                webbrowser.open('http://fn.bmstu.ru/tm-fs-4')
                director.replace(active_scene)
            else:
                print("No i dont")
                self.target.position = 630, 220
                self.target.state = "Down"
        if (new.x >= 1033 and new.x <= 1087) and (new.y >= 188 and new.y <= 215):
            print("IN THE GAME")
            player_choice = ctypes.windll.user32.MessageBoxW(0, "Do you want to proceed", "MOODLE", 1)
            if (player_choice == 1):
                print("Yes i want")
                active_scene = Menu_Scene([Menu_BG(), MainMenu()])
                webbrowser.open('http://e-learning.bmstu.ru/portal_iu7/')
                director.replace(active_scene)
            else:
                print("No i dont")
                self.target.position = 630, 220
                self.target.state = "Down"
        if (new.x >= 997 and new.x <= 1028) and (new.y >= 516 and new.y <= 547):
            print("IN THE GAME")
            player_choice = ctypes.windll.user32.MessageBoxW(0, "Do you want to proceed", "GITLAB", 1)
            if (player_choice == 1):
                print("Yes i want")
                active_scene = Menu_Scene([Menu_BG(), MainMenu()])
                webbrowser.open('https://git.iu7.bmstu.ru/')
                director.replace(active_scene)
            else:
                print("No i dont")
                self.target.position = 630, 220
                self.target.state = "Down"
        if (new.x >= 577 and new.x <= 633) and (new.y >= 815 and new.y <= 868):
            print("IN THE GAME")
            player_choice = ctypes.windll.user32.MessageBoxW(0, "Do you want to proceed", "Sport Hall", 1)
            if (player_choice == 1):
                print("Yes i want")
                active_scene = sh.Sport_Scene()
                director.replace(active_scene)
            else:
                print("No i dont")
                self.target.position = 630, 220
                self.target.state = "Down"





class BackgroundLayer(cocos.layer.ScrollableLayer):
    def __init__(self):
        super().__init__()

        map = cocos.tiles.load('resources/school.tmx')
        self.school = map['school']
        self.colliders = map['colliders']

if __name__ == "__main__":
    director.init(width=1366, height=768, caption="University", fullscreen=False)
    director.window.pop_handlers()
    global keyboard
    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

    mapcollider = mapcolliders.TmxObjectMapCollider()
    mapcollider.on_bump_handler = mapcollider.on_bump_bounce
    collision_handler = mapcolliders.make_collision_handler(mapcollider, BackgroundLayer().colliders)

    scrollable = cocos.layer.ScrollingManager()
    scrollable.add(BackgroundLayer().school)
    scrollable.add(Player(collision_handler))

    active_scene = Menu_Scene([Menu_BG(), MainMenu()])

    director.run(active_scene)