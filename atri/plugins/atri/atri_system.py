import os

import nonebot
import nonebot.adapters.onebot.v11 as onebot
from nonebot.matcher import Matcher

atri_system = nonebot.on_command("system", block=True, priority=30)


@atri_system.handle()
async def atri_system_handler(event: onebot.Event, matcher: Matcher):
    expr = event.get_plaintext()[8:]
    output = os.popen(expr).read()
    if len(output) == 0:
        output = "<nil>"
    await matcher.send(output)
