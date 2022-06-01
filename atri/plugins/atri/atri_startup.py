import nonebot
from nonebot.log import logger

driver = nonebot.get_driver()

@driver.on_bot_connect
async def welcome():
    logger.success('アトリ、起動！')
