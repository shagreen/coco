# klasa od ładowania map

import cocos
from resources import resources


class GameMap(cocos.layer.Layer):

    def __init__(self, level_map):
        super().__init__()
        self.level_map = level_map
        self.map_background_spr = self.load_map_background()
        self.draw_map_background()

    def _load_map_background(self):
        return cocos.sprite.Sprite(resources.map_background(self.level_map))

    def _draw_map_background(self):
        w, h = cocos.director.director.get_window_size()
        self.map_background_spr.position = w/2, h/2
        self.add(self.map_background_spr)
        self._scale_background_to_window()

    def _scale_background_to_window(self):
        bcg_w = self.map_background_spr.width
        bcg_h = self.map_bakcground_spr.height
        bcg_ratio = bcg_w / bcg_h
        sc_w, sc_h = cocos.director.director.get_window_size()
        sc_ratio = sc_w / sc_h
        scale = sc_h / bcg_h if bcg_ratio < sc_ratio else sc_w / bcg_w
        self.map_background_spr.scale = scale
