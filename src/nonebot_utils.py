import nonebot.adapters.onebot.v11 as onebot

#.data
segtypes = ['image', 'record']

class STATE:
    def __new__(cls, *args, **kwargs):
        raise TypeError("class {} cannot be instantiate.".format(cls))
    @classmethod
    def get(cls, key):
        return getattr(cls, key)
    @classmethod
    def set(cls, key, val):
        setattr(cls, key, val)
    @classmethod
    def to_dict(cls):
        d = {}
        for attr in dir(cls):
            if attr.startswith('_'):
                continue
            if attr in {'get', 'set', 'to_dict'}:
                continue
            d.update({attr: getattr(cls, attr)})
        return d

def cvtfile(msg:str) -> onebot.MessageSegment:
    for segtype in segtypes:
        if msg.startswith("{}:".format(segtype)):
            with open(msg.lstrip("{}:".format(segtype)), 'rb') as file:
                msg = getattr(onebot.MessageSegment, segtype)(file.read())
                break
    else:
        msg = onebot.MessageSegment.text(msg)
    return msg
