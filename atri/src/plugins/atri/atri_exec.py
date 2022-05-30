import sys
from io import StringIO

import nonebot
import nonebot.adapters.onebot.v11 as onebot

import numpy
import scipy
from scipy import stats
from scipy import optimize
from math import *

stdout = sys.stdout

atri_exec = nonebot.on_command("exec", permission=nonebot.permission.SUPERUSER, block=True, priority=30)

@atri_exec.handle()
async def atri_exec_session(event: onebot.Event, matcher: nonebot.matcher.Matcher):
    expr = event.get_plaintext()[6:]
    output = StringIO()
    sys.stdout = output
    try:
        exec(expr)
    except Exception as e:
        print(e)
    sys.stdout = stdout
    output = output.getvalue()
    if len(output) == 0:
        output = "empty output"
    await matcher.send(output)
