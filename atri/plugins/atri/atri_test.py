import nonebot
import nonebot.adapters.onebot.v11 as onebot

atri_test = nonebot.on_command("test", permission=nonebot.permission.SUPERUSER, block=False, priority=90)

@atri_test.handle()
async def atri_test_session1(event: onebot.Event, matcher: nonebot.matcher.Matcher):
    await matcher.send("event.dict: {}".format(event.dict()))
    await matcher.send("user_id: {}".format(event.get_user_id()))
    await matcher.send("session_id: {}".format(event.get_session_id()))
    await matcher.send("type: {}".format(event.get_type()))
    await matcher.send("event_name: {}".format(event.get_event_name()))
    await matcher.send("event_discription: {}".format(event.get_event_description()))
    await matcher.send("message: {}".format(event.get_message()))
    await matcher.send("plaintext: {}".format(event.get_plaintext()))
