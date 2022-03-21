#!python3
import nonebot
from nonebot.adapters.onebot.v11 import Adapter

#.text
nonebot.init(_env_file='config.env')
app = nonebot.get_asgi()
driver = nonebot.get_driver()
driver.register_adapter(Adapter)
nonebot.load_plugin("src.atri")
nonebot.load_plugin("src.atri_voice")
nonebot.load_plugin("src.eroira")
nonebot.load_plugin("src.animegenerate")
