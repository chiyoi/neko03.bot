from os import path
import random
import numpy as np
import cv2
import torch
import nonebot

from ...utils import cvtfile
from . import stylegan2

G = stylegan2.models.load("assets/animegenerate/Gs.pth")
G.eval()

animegenerate = nonebot.on_keyword({"随机老婆"}, block=True, priority=40)

@animegenerate.handle()
async def _session_1(matcher: nonebot.matcher.Matcher):
    await matcher.send("画呀画呀...")
    img = await generate_img()
    await matcher.finish(cvtfile.image(img))

async def generate_img():
    latents = torch.from_numpy(np.random.randn(1, G.latent_size)).to(torch.float32)
    y = G(latents)
    img = y[0].detach().numpy()
    img = img.clip(-1, 1)
    img = (img + 1) * 255 / 2
    img = img[[2,1,0]]
    img = img.transpose(1,2,0)
    img = img.astype(np.uint8)
    filepath = path.join("tmp", "img{}.png".format(int(random.random() * 10)))
    cv2.imwrite(filepath, img)
    return filepath
