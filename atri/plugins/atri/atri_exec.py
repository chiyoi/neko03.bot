import sys
from io import StringIO

import nonebot
import nonebot.adapters.onebot.v11 as onebot
import numpy
import scipy
from nonebot.matcher import Matcher
from scipy import optimize
from scipy import stats

_ = numpy, scipy, stats, optimize

stdout = sys.stdout

atri_exec = nonebot.on_command("exec", block=True, priority=30)


@atri_exec.handle()
async def atri_exec_session(event: onebot.Event, matcher: Matcher):
    expr = event.get_plaintext()[6:]
    output = StringIO()
    sys.stdout = output
    try:
        exec(expr)
    except Exception as exc:
        print(exc)
    sys.stdout = stdout
    output = output.getvalue()
    if len(output) == 0:
        await matcher.finish("<nil>")
    await matcher.finish(output)


atri_eval = nonebot.on_command("eval", block=True, priority=30)


@atri_eval.handle()
async def atri_eval_session(event: onebot.Event, matcher: Matcher):
    expr = event.get_plaintext()[6:]
    output = ""
    try:
        output = str(eval(expr))
    except Exception as exc:
        await matcher.finish(str(exc))
    if len(output) == 0:
        await matcher.finish("<nil>")
    await matcher.finish(output)


atri_echo = nonebot.on_command("echo", block=True, priority=30)


@atri_echo.handle()
async def atri_echo_session(event: onebot.Event, matcher: Matcher):
    await matcher.finish(event.get_plaintext()[6:])
