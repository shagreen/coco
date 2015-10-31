import os
import pyglet

root = os.path.dirname(os.path.abspath(__file__))


def pathjoin(relative_path):
    return os.path.join(root, relative_path)

pyglet.resource.path.append(pathjoin('resources'))
pyglet.resource.reindex()


def load_image(filename):
    try:
        img = pyglet.resource.image(filename)
    except:
        # TODO: FileNotFoundError
        print(filename + " not found in load_image," + " please check files")
        raise None
    return img

background = {
    'map_main': load_image(),
    'background': load_image('background.png'),
}
