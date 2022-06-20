import nonebot
import nonebot.adapters.onebot.v11 as onebot

atri_test = nonebot.on_command("test", permission=nonebot.permission.SUPERUSER, block=False, priority=90)
atri_test_notice = nonebot.on_notice(block=False, priority=1000)

@atri_test.handle()
async def atri_test_session1(event: onebot.Event, matcher: nonebot.matcher.Matcher):
    await matcher.send("event.dict: {}".format(event.dict()))

@atri_test_notice.handle()
async def atri_test_notice_session1(event: onebot.Event, matcher: nonebot.matcher.Matcher):
    await matcher.send("event.dict: {}".format(event.dict()))
