import os
import os.path as path
import nonebot
from nonebot.adapters.onebot.v11 import Adapter

nonebot.init()
app = nonebot.get_asgi()
driver = nonebot.get_driver()
driver.register_adapter(Adapter)
nonebot.load_plugin("atri")
if not path.exists("tmp"):
    os.mkdir("tmp")
