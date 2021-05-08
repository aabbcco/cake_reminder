# import nonebot
from nonebot import get_driver, require
from nonebot import get_bots
from nonebot.adapters.cqhttp import MessageSegment, message
import sys
import os

sys.path.append(os.path.dirname(__file__))


from .config import Config

global_config = get_driver().config
config = Config(**global_config.dict())

schedular = require("nonebot_plugin_apscheduler").scheduler


@schedular.scheduled_job("cron", hour="9", id="cake")
async def SendCake():
    bots = get_bots()
    msg = [{"type": "image", "data": {"file": "file:////home/aabbcco/cakie.jpg"}}]
    for bot in bots.values():
        await bot.send_msg(group_id="323404924", message=msg)


# Export something for other plugin
# export = nonebot.export()
# export.foo = "bar"

# @export.xxx
# def some_function():
#     pass
