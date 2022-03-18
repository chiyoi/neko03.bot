import re

#.data
mandatory_kws = {
        'first': {},
        'again': {},
        }
omitting_kws = {'不', '别', '没', '是',}
optional_kws = {
        'first': [{'色图',},],
        'again': [{'再', '还',},],
        }

cn2an = {
        '零': 0,
        '一': 1,
        '二': 2,
        '两': 2,
        '三': 3,
        '四': 4,
        '五': 5,
        '六': 6,
        '七': 7,
        '八': 8,
        '九': 9,
        '十': 10,
        '百': 100,
        '千': 1000,
        '万': 10000,
        '亿': 100000000,
        }

#.text
def keyword_filter(message, isAgain=False):
    if len(message) > 10:
        return False
    for kw in omitting_kws:
        if kw in message:
            return False
    if isAgain:
        if check_again(message):
            return True
    for kw in mandatory_kws['first']:
        if kw not in message:
            return False
    for kws in optional_kws['first']:
        for kw in kws:
            if kw in message:
                break
        else:
            return False
    return True
def check_again(message):
    for kw in mandatory_kws['again']:
        if kw not in message:
            return False
    for kws in optional_kws['again']:
        for kw in kws:
            if kw in message:
                break
        else:
            return False
    return True

async def parse_cmd(message, matcher):
    return {
            'r18': 0,
            'num': await get_num(message, matcher),
            'tag': get_tag(message),
            'keyward': get_kw(message),
            'uid': get_uid(message),
            }

async def get_num(message, matcher):
    match = re.compile('[张份个]').search(message)
    num_end = match and match.span()[0]
    if num_end:
        pattern = re.compile("[0-9{}]".format(''.join(cn2an.keys())))
        nums = pattern.findall(message[:num_end])
        if len(nums) > 0:
            num = cn2an.get(nums[0]) or int(nums[0])
            if len(nums) > 1 or num > 5:
                await matcher.finish("太多啦！不给！")
            else:
                if num == 0:
                    await matcher.finish("不要算了。。")
                else:
                    return cn2an.get(num) or num
    return None
def get_tag(message):
    tag_end = message.find('色图')
    match = re.compile("[张份点个看]").search(message, endpos=tag_end)
    tag_start = match and match.span()[0] + 1
    if tag_end != -1 and tag_start is not None:
        if 1 < tag_end - tag_start < 4:
            return message[tag_start:tag_end].strip('看')
    return None
def get_kw(message):
    keyward_start = message.find('keyward')
    if keyward_start != -1:
        keyward_start += 7
    if keyward_start == -1:
        keyward_start = message.find('关键字')
        if keyward_start != -1:
            keyward_start += 3
        else:
            keyward_start = message.find('关键词')
            if keyward_start != -1:
                keyward_start += 3
    match = re.compile('[,，; ]').search(message, keyward_start)
    keyward_end = match and match.span()[0]
    if keyward_start != -1:
        return message[keyward_start:keyward_end].strip(': []的')
    return None
def get_uid(message):
    uid_start = message.find('uid')
    if uid_start != -1:
        uid_start += 3
    match = re.compile('[,，; ]').search(message, uid_start)
    uid_end = match and match.span()[0]
    if uid_start != -1:
        return message[uid_start:uid_end].strip(': []的')
    return None
