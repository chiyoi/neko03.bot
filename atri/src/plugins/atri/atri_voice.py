from os import path
import json
import random
import nonebot
import nonebot.adapters.onebot.v11 as onebot

from ...utils import cvtfile

with open("assets/atri/atri_voice/text/atri.json") as f:
    voice_list = json.load(f)

atri_voice_1 = nonebot.on_notice(block=False, priority=25)
atri_voice_2 = nonebot.on_message(block=False, priority=25)

@atri_voice_1.handle()
async def atri_voice_1_session(event: onebot.Event, matcher: nonebot.matcher.Matcher):
    notice = event.get_event_name()
    if notice != 'notice.notify.poke':
        await matcher.finish()
    matcher.stop_propagation()
    await send_record(matcher)

@atri_voice_2.handle()
async def atri_voice_2_session(event: onebot.Event, matcher: nonebot.matcher.Matcher):
    message = event.get_message().extract_plain_text()
    if not message.startswith('[戳一戳]'):
        await matcher.finish()
    matcher.stop_propagation()
    await send_record(matcher)

async def send_record(matcher: nonebot.matcher.Matcher):
    text, voice = random_voice()
    await matcher.send(text)
    await matcher.send(cvtfile.record(voice))

def random_voice() -> tuple[str, str]:
    voice_obj = random.choice(voice_list)
    text = voice_obj['s']
    voice = path.join("assets/atri/atri_voice/voice", voice_obj['o'])
    return text, voice
