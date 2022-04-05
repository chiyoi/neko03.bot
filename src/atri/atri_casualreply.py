import random
import nonebot

from ..nonebot_utils import cvtfile
from .config import assets

#.data

casual_replies = [
        '（？）',
        '（？',
        '唔...',
        *["image:{}".format(img) for img in assets.casual_reply_imgs],
        ]
        
#.text
atri_tome = nonebot.on_message(rule=nonebot.rule.to_me(), block=False, priority=100)

@atri_tome.handle()
async def _tome_session_1(matcher: nonebot.matcher.Matcher):
    await matcher.send(cvtfile(random.choice(casual_replies)))
