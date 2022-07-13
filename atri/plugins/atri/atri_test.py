import nonebot
import nonebot.adapters.onebot.v11 as onebot
from nonebot import permission
from nonebot.matcher import Matcher

atri_test = nonebot.on_command("test", permission=permission.SUPERUSER, block=False, priority=90)


@atri_test.handle()
async def atri_test_session1(event: onebot.Event, matcher: Matcher):
    print(matcher.__dict__)
    await matcher.send("event.dict: {}".format(event.dict()))
    await matcher.send("event.get_event_name: {}".format(event.get_event_name()))
    await matcher.send("event.get_event_description: {}".format(event.get_event_description()))
