from os import path
import json
import aiofiles
import aiohttp

import nonebot
from nonebot.matcher import Matcher

from ...utils import time, cvtfile

origin = "https://api.lolicon.app/setu/v2"

headers = {
        "Accept": "image/webp,image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Host": "i.pximg.net",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.pixiv.net/",
        "Connection": "keep-alive",
        }

disp_tmpl = """\
title: {}
pid: {}
author: {}
uid: {}"""

cd = time.second

cd_checker = time.now()

eroira = nonebot.on_keyword({"色图"}, block=True, priority=20)

@eroira.handle()
async def _session_1(matcher: Matcher):
    current = time.now()
    if current - cd_checker < cd:
        await matcher.finish("冷却中...")
    await matcher.send("让我找找...")
    img, disp = await get_img()
    await matcher.send(cvtfile.image(img) + disp)

async def get_img() -> tuple[str, str]:
    """
    get_img() (img: str, disp: str)
    """
    params = {
            'r18': 2,
            'proxy': 0,
            }
    async with aiohttp.ClientSession() as session:
        async with session.get(origin, params=params) as res:
            if not res.ok:
                raise ConnectionError
            img_obj = json.loads(await res.text())['data'][0]
            img_origin = img_obj['urls']['original']
            disp = disp_tmpl.format(img_obj['title'], img_obj['pid'], img_obj['author'], img_obj['uid'])
        async with session.get(img_origin, headers=headers) as res:
            if not res.ok:
                raise ConnectionError
            img = path.join("tmp", path.basename(img_origin))
            async with aiofiles.open(img, 'wb') as f:
                await f.write(await res.read())
    return img, disp
