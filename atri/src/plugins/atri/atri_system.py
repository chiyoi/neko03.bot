import os

import nonebot
import nonebot.adapters.onebot.v11 as onebot

atri_system = nonebot.on_command("system", permission=nonebot.permission.SUPERUSER, block=True, priority=30)

@atri_system.handle()
async def atri_system_session(event: onebot.Event, matcher: nonebot.matcher.Matcher):
    expr = event.get_plaintext()[8:]
    output = os.popen(expr).read()
    if len(output) == 0:
        output = "<nil>"
    await matcher.send(output)
