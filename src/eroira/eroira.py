import json, time, os
import aiofiles
import aiohttp
import nonebot
from nonebot.log import logger
import nonebot.adapters.onebot.v11 as onebot
from nonebot_utils import STATE, cvtfile

from .preprocess import keyword_filter, parse_cmd
from .config import origins, data

#.data
cooldown_time = 1

class state(STATE):
    cd_checker = 0
    chat_history = {}

#.text
eroira = nonebot.on_message(block=False, priority=20)

@eroira.handle()
async def _session_2_1(event: onebot.Event, matcher: nonebot.matcher.Matcher):
    message = event.get_plaintext()
    uid = event.get_user_id()
    current = time.time()
    isAgain = False
    if uid in state.chat_history:
        if current - state.chat_history[uid]['timestamp'] < 120:
            isAgain = True
    if not keyword_filter(message, isAgain):
        await matcher.finish()
    matcher.stop_propagation()
    state.chat_history.update({uid: {'timestamp': current}})
    if not await check_time():
        await matcher.finish("技能冷却中...")
    await matcher.send("让我找找...")
    params = await parse_cmd(message, matcher)
    ok, (img, disp) = await get_some(params)
    if ok:
        await send_img(img, disp, matcher)
    else:
        await send_error(disp, matcher)

async def check_time():
    current = time.time()
    if current - state.get('cd_checker') <= cooldown_time:
        return False
    state.set('cd_checker', current)
    return True

async def send_img(imgs, disps, matcher):
    if len(imgs) == 0:
        await matcher.send("图丢了...")
    for idx, img in enumerate(imgs):
        await matcher.send(cvtfile("image:{}".format(img)) + disps[idx])
    await matcher.finish()
async def send_error(info, matcher):
    await matcher.finish("Something went wrong...\n{}".format(info))

async def get_some(params=None):
    url = origins.origin
    if params is None:
        params = {'r18': 2}
    else:
        params = {key: val for key, val in params.items() if val}
    params.update({'proxy': 0})
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as res:
            if res.ok:
                imgs = json.loads(await res.text())['data']
                img_origins, disps = [], []
                for img in imgs:
                    img_origins.append(img['urls']['original'])
                    disps.append("""\
title[{}]
pid[{}]
author[{}] uid[{}]""".format(
                        img['title'],
                        img['pid'],
                        img['author'],
                        img['uid']
                        ))
                logger.debug(params)
            else:
                raise ConnectionError()
        imgs = []
        headers = {
                'Accept': 'image/webp,image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Host': 'i.pximg.net',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15',
                'Accept-Language': 'en-US,en;q=0.9',
                'Referer': 'https://www.pixiv.net/',
                'Connection': 'keep-alive',
                }
        for img_origin in img_origins:
            async with session.get(img_origin, headers=headers) as res:
                if res.ok:
                    filename = os.path.join(data.save_dir, os.path.basename(img_origin))
                    async with aiofiles.open(filename, 'wb') as f:
                        await f.write(await res.read())
                    imgs.append(filename)
                else:
                    raise ConnectionError()
    return True, (imgs, disps)
