import os
import random
import numpy as np
import cv2
import torch
import nonebot
import nonebot.adapters.onebot.v11 as onebot

from ..nonebot_utils import cvtfile
from . import stylegan2
from .preprosess import keyword_filter
from . import config

#.data
G = stylegan2.models.load(config.ckpt.Gs)
G.eval()


#.text
animegenerate = nonebot.on_message(block=False, priority=40)

@animegenerate.handle()
async def _session_1(event: onebot.Event, matcher: nonebot.matcher.Matcher):
    message = event.get_plaintext()
    if not keyword_filter(message):
        await matcher.finish()
    matcher.stop_propagation()
    await matcher.send("让我看看stylegan放哪了...")
    img = generate_img()
    await matcher.send(cvtfile("image:{}".format(img)))
    await matcher.finish()

def generate_img():
    latents = torch.from_numpy(np.random.randn(1, G.latent_size)).to(torch.float32)
    y = G(latents)
    img = y[0].detach().numpy()
    img = img.clip(-1, 1)
    img = (img + 1) * 255 / 2
    img = img[[2,1,0]]
    img = img.transpose(1,2,0)
    img = img.astype(np.uint8)
    filepath = os.path.join(config.data.cache, 'img{}.png'.format(int(random.random() * 10)))
    cv2.imwrite(filepath, img)
    return filepath
