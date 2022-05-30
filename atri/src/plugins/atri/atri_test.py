import nonebot
import nonebot.adapters.onebot.v11 as onebot

atri_test = nonebot.on_command("atri", permission=nonebot.permission.SUPERUSER, priority=20)

@atri_test.handle()
async def atri_test_session1(event: onebot.Event, matcher: nonebot.matcher.Matcher):
    await matcher.send(event.get_plaintext())
