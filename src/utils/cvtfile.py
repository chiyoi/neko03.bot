import nonebot.adapters.onebot.v11 as onebot

segtypes = ['image', 'record']
def auto(msg: str) -> onebot.MessageSegment:
    for segtype in segtypes:
        if msg.startswith("{}:".format(segtype)):
            with open(msg[len("{}:".format(segtype)):], 'rb') as file:
                msg = getattr(onebot.MessageSegment, segtype)(file.read())
                break
    else:
        msg = onebot.MessageSegment.text(msg)
    return msg

def image(filepath: str) -> onebot.MessageSegment:
    with open(filepath, 'rb') as f:
        msg = onebot.MessageSegment.image(f.read())
    return msg
def record(filepath: str) -> onebot.MessageSegment:
    with open(filepath, 'rb') as f:
        msg = onebot.MessageSegment.record(f.read())
    return msg
