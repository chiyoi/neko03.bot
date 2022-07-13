import nonebot
import nonebot.adapters.onebot.v11 as onebot

atri_test = nonebot.on_command("test", permission=nonebot.permission.SUPERUSER, block=False, priority=90)


@atri_test.handle()
async def atri_test_session1(event: onebot.Event, matcher: nonebot.matcher.Matcher):
    await matcher.send("event.dict: {}".format(event.dict()))
    await matcher.send("event.get_event_name: {}".format(event.get_event_name()))
    await matcher.send("event.get_event_description: {}".format(event.get_event_description()))
