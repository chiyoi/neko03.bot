from os import path
import json
import random

import nonebot
from nonebot.adapters.onebot.v11 import Event
from nonebot.matcher import Matcher

from ...utils import cvtfile

with open("assets/atri/atri_voice/text/atri.json") as f:
    voice_list = json.load(f)

atri_voice_1 = nonebot.on_notice(block=False, priority=25)
atri_voice_2 = nonebot.on_message(block=False, priority=25)


@atri_voice_1.handle()
async def atri_voice_1_session(event: Event, matcher: Matcher):
    if event.get_event_name() != 'notice.notify.poke' or event.dict()["target_id"] not in (event.self_id, 0):
        await matcher.finish()
    matcher.stop_propagation()
    await send_record(matcher)


@atri_voice_2.handle()
async def atri_voice_2_session(event: Event, matcher: Matcher):
    message = event.get_message().extract_plain_text()
    if not message.startswith('[戳一戳]') or event.dict()["target_id"] not in (event.self_id, 0):
        await matcher.finish()
    matcher.stop_propagation()
    await send_record(matcher)


async def send_record(matcher: Matcher):
    text, voice = random_voice()
    await matcher.send(text)
    await matcher.send(cvtfile.record(voice))


def random_voice() -> tuple[str, str]:
    voice_obj = random.choice(voice_list)
    text = voice_obj['s']
    voice = path.join("assets/atri/atri_voice/voice", voice_obj['o'])
    return text, voice
