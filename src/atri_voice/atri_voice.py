import os
import json
import random
import nonebot
import nonebot.adapters.onebot.v11 as onebot
from nonebot_utils import cvtfile

from .config import assets

atri_voice_on_poke = nonebot.on_notice(priority=25)
atri_voice_on_message_poke = nonebot.on_message(block=False, priority=25)

@atri_voice_on_poke.handle()
async def _atri_voice_on_poke_session_1(event: onebot.Event, matcher: nonebot.matcher.Matcher):
    notice = event.get_event_name()
    if notice != 'notice.notify.poke':
        await matcher.finish()
    matcher.stop_propagation()
    await send_record(matcher)

@atri_voice_on_message_poke.handle()
async def _atri_voice_on_message_poke_session_1(event: onebot.Event, matcher: nonebot.matcher.Matcher):
    message = event.get_message().extract_plain_text()
    if not message.startswith('[戳一戳]'):
        await matcher.finish()
    matcher.stop_propagation()
    await send_record(matcher)

async def send_record(matcher):
    text, voice = random_voice()
    await matcher.send(cvtfile("record:{}".format(voice)))
    await matcher.send(text)

with open(assets.text, encoding='utf8') as f:
    voice_list = json.load(f)

def random_voice():
    voice = random.choice(voice_list)
    return voice['s'], os.path.join(assets.voice_dir, voice['o'])
