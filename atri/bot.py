#!python3
import os
import nonebot
from nonebot.adapters.onebot.v11 import Adapter

nonebot.init(_env_file='config.env')
app = nonebot.get_asgi()
driver = nonebot.get_driver()
driver.register_adapter(Adapter)
nonebot.load_plugin("src.plugins.atri")
nonebot.load_plugin("src.plugins.eroira")
os.mkdir("tmp")
