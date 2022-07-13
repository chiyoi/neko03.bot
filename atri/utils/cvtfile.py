import nonebot.adapters.onebot.v11 as onebot

file_types = ['image', 'record']


def auto(msg: str) -> onebot.MessageSegment:
    for file_type in file_types:
        if msg.startswith("{}:".format(file_type)):
            with open(msg[len("{}:".format(file_type)):], 'rb') as file:
                msg = getattr(onebot.MessageSegment, file_type)(file.read())
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
