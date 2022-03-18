import os

root = os.path.dirname(os.path.realpath(__file__))
class data:
    data_root = os.path.join(root, 'data')
    save_dir = data_root
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
class origins:
    origin = "https://api.lolicon.app/setu/v2"
