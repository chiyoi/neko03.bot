import os
root = os.path.dirname(os.path.realpath(__file__))
class assets:
    assets_root = os.path.join(root, 'assets')
    voice_dir = os.path.join(assets_root, 'voice')
    text = os.path.join(assets_root, 'text', 'atri.json')
