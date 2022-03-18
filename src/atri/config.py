import os
from glob import glob

root = os.path.basename(os.path.realpath(__file__))
class assets:
    assets_root = os.path.join(root, 'assets')
    casual_reply_imgs = glob(os.path.join(assets_root, "casual_reply_imgs", '*'))
    waiting_imgs = glob(os.path.join(assets_root, "waiting_imgs", '*'))
