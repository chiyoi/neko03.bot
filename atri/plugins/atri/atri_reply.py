import random
from glob import glob

import nonebot
from nonebot.matcher import Matcher

from ...utils import cvtfile

replies = [
    '（？）',
    '（？',
    '唔...',
    *["image:{}".format(img) for img in glob("assets/atri/reply_imgs/*")],
]

atri_reply = nonebot.on_message(rule=nonebot.rule.to_me(), block=False, priority=100)


@atri_reply.handle()
async def atri_reply_session(matcher: Matcher):
    await matcher.send(cvtfile.auto(random.choice(replies)))
