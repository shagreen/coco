import cocos
import pyglet

from cocos.director import director
from cocos.layer import MultiplexLayer
from cocos.scene import Scene

_font_ = 'Orbitron Light'


class MainMenu(cocos.menu.Menu):

    def __init__(self, scene):
        super().__init__('')

        self.font_title['font_name'] = _font_
        self.font_title['font_size'] = 72

        self.font_item['font_name'] = _font_
        self.font_item['font_size'] = 35

        self.font_item_selected['font_name'] = _font_
        self.font_item_selected['font_size'] = 41

        self.menu_anchor_x = cocos.menu.CENTER
        self.menu_anchor_y = cocos.menu.CENTER

        self.scene = scene
        self.w, self.h = director.get_window_size()
        director.interpreter_locals["pyfense_main"] = self

        items = []
        items.append(cocos.menu.MenuItem('Start Game', self.on_start_game))
        items.append(cocos.menu.MenuItem('Exit', self.on_quit))
        self.create_menu(items)

    def on_start_game(self):
        pass

    def on_quit(self):
        pyglet.app.exit()


if __name__ == "__main__":
    director.init()
    scene = Scene()
    scene.add(MultiplexLayer(
        MainMenu(scene),
    ),
        z=1)
    w, h = director.get_window_size()
    director.run(scene)
