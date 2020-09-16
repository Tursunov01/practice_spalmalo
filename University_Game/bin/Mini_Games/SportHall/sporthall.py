import cocos
import time
import tmx_map_loading_game
from cocos.director import director
from cocos.layer import ColorLayer
from cocos.sprite import Sprite
from cocos.scenes import *
from cocos.text import Label
from cocos import mapcolliders
import pyglet
from pyglet.window import key

class Sport_Scene(cocos.scene.Scene):
    def __init__(self):
        super().__init__()
        global scroller
        scroller = cocos.layer.ScrollingManager()
        scroller.add(BackgroundLayer().layer_ground)
        scroller.add(BackgroundLayer().layer_box)
        scroller.add(Player(collision_handler_sh))

        self.add(scroller)


class WinningScene(cocos.scene.Scene):
    def __init__(self):
        super().__init__()
        self.back = cocos.sprite.Sprite("Mini_Games/SportHall/res/cong.png", anchor=(0, 0))
        self.back.position = (580, 400)
        self.add(self.back)

        self.add(cocos.layer.ColorLayer(50, 50, 50, 180))

        self.add(cocos.text.Label("Сongratulations! Well done", font_name="Times New Roman", font_size=26,
                                      anchor_x="center", anchor_y="center", position=(580,350)))
        time.sleep(5)
        tmx_map_loading_game.active_scene = tmx_map_loading_game.Menu_Scene([tmx_map_loading_game.Menu_BG(), tmx_map_loading_game.MainMenu()])


class Player(cocos.layer.ScrollableLayer):
    def __init__(self, collision_handler_sh):
        super().__init__()

        img = pyglet.image.load("Mini_Games/SportHall/res/Guy.png")
        img_grid = pyglet.image.ImageGrid(img, 4, 3, item_width = 40, item_height= 40)
        anim = pyglet.image.Animation.from_image_sequence(img_grid[6:9], 0.1, loop=True)

        player = cocos.sprite.Sprite(anim)
        player.position = 630, 360
        player.velocity = (0, 0)

        player.collide_map = collision_handler_sh
        
        player.do(Mover())
        
        self.add(player)

class Mover(cocos.actions.Move):
    def step(self, dt):

        vel_x = 200
        vel_y = (tmx_map_loading_game.keyboard[key.UP] - tmx_map_loading_game.keyboard[key.DOWN]) * 100
        dx = vel_x * dt
        dy = vel_y * dt

        last = self.target.get_rect()

        new = last.copy()
        new.x += dx
        new.y += dy

        if (new.x >= 3100):
            active_scene = WinningScene()
            director.replace(active_scene)
            
    
        self.target.velocity = self.target.collide_map(last, new, vel_x, vel_y)

        self.target.position = new.center
        scroller.set_focus(*new.center)
        
class BackgroundLayer():
    def __init__(self):

        bg = cocos.tiles.load("Mini_Games/SportHall/res/road_box.tmx")
        self.layer_ground = bg["ground"]
        self.layer_box = bg["boxes"]
        self.finish = bg["finish"]
        self.colliders = bg["colliders"]

        mapcollider = mapcolliders.TmxObjectMapCollider()
        mapcollider.on_bump_handler = mapcollider.on_bump_bounce
        #finish_handler = mapcolliders.make_collision_handler(mapcollider, BackgroundLayer().finish)
        global collision_handler_sh
        collision_handler_sh = mapcolliders.make_collision_handler(mapcollider, self.colliders)
