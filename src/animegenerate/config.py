import os

root = os.path.dirname(os.path.realpath(__file__))

class data:
    cache = os.path.join(root, 'cache')
    if not os.path.exists(cache):
        os.mkdir(cache)

class ckpt:
    Gs = os.path.join(root, 'Gs.pth')
