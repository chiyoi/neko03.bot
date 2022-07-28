import nonebot
from nonebot.adapters.onebot.v11 import Event
from nonebot.matcher import Matcher

from ...utils import cvtfile

voice_path = "./assets/aira/aira.mp3"
voice_text = "大切な人と、いつかまた巡り合えますように。"

aira_voice = nonebot.on_message(block=False, priority=25)


@aira_voice.handle()
async def aira_voice_handler(event: Event, matcher: Matcher):
    message = event.get_message().extract_plain_text()
    if not message == "aira":
        await matcher.finish()
    matcher.stop_propagation()
    await matcher.send(voice_text)
    await matcher.send(cvtfile.record(voice_path))
