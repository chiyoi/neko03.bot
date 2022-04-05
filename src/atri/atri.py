import random
import asyncio
import nonebot
from nonebot.log import logger
import nonebot.adapters.onebot.v11 as onebot

from ..nonebot_utils import STATE, cvtfile
from .config import assets

#.data
class state(STATE):
    message = ''

waiting_replies = [
        "何事？",
        "私を呼んでる？",
        "どうしたの",
        "私に用？",
        *["image:{}".format(img) for img in assets.waiting_imgs],
        ]

#.text
driver = nonebot.get_driver()

@driver.on_bot_connect
async def _on_bot_connect():
    nonebot.logger.success('アトリ、起動！')

atri_on_command = nonebot.on_command('atri', permission=nonebot.permission.SUPERUSER, block=False, priority=5)

@atri_on_command.handle()
async def _session_1(matcher: nonebot.matcher.Matcher):
    matcher.stop_propagation()
    nonebot.logger.debug("config: {}".format(driver.config))
    nonebot.logger.debug("driver.config.dict(): {}".format(driver.config.dict()))
    nonebot.logger.debug("config type: {}".format(type(driver.config)))
    await matcher.send("はい！")
    await asyncio.sleep(0.5)
    await matcher.pause(cvtfile(random.choice(waiting_replies)))

@atri_on_command.handle()
async def _session_2(event: onebot.Event, matcher: nonebot.matcher.Matcher):
    logger.debug("user_id: {}".format(event.get_user_id()))
    logger.debug("plaintext: {}".format(event.get_plaintext()))
    logger.debug("message: {}".format(event.get_message()))
    state.set('message', event.get_plaintext())
    for segment in event.get_message():
        if segment.type == 'image':
            url = segment.data['url']
            logger.debug("image_url: {}".format(url))
    logger.debug("data: {}".format(next(iter(event.get_message())).data))
    logger.debug("event_name: {}".format(event.get_event_name()))
    logger.debug("state: {}".format(state.to_dict()))
    await nyan(matcher)

async def nyan(matcher: nonebot.matcher.Matcher):
    await matcher.send("にゃん...（？）")
    await matcher.finish()
