# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import time
from datetime import datetime

from speedtest import Speedtest

from userbot import ALIVE_NAME, CMD_HELP, StartTime
from userbot.events import register


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**𝓚𝓮𝓬𝓮𝓹𝓪𝓽𝓪𝓷 𝓘𝓷𝓽𝓮𝓻𝓷𝓮𝓽 𝓚𝓪𝓶𝓾!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**💉 𝓚𝓮𝓬𝓮𝓹𝓪𝓽𝓪𝓷 𝓘𝓷𝓽𝓮𝓻𝓷𝓮𝓽 𝓚𝓪𝓶𝓾!** "
        f"\n  ➥ `%sms` \n"
        f"**🐣 𝙳𝙴𝙰𝚃𝙷𝙽𝙾𝚃𝙴-𝚅𝙰𝚁𝚂!** "
        f"\n  ➥ `{ALIVE_NAME}` \n" % (duration)
    )


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """For .speed command, use SpeedTest to check server speeds."""
    await spd.edit("`Kecepatan Internetmu Sedang Dihitung!.....🚀`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit(
        "**Hasil Speed-Test! :\n**"
        "💉 **Dimulai Pada :** "
        f"`{result['timestamp']}` \n"
        "🌷 **Downloads :** "
        f"`{speed_convert(result['download'])}` \n"
        "🐧 **Uploads :** "
        f"`{speed_convert(result['upload'])}` \n"
        "🍂 **Pings :** "
        f"`{result['ping']}` \n"
        "🌙 **ISP :** "
        f"`{result['client']['isp']}` \n"
        "🌱 **Bot :** `𝓓𝓔𝓐𝓣𝓗𝓝𝓞𝓣𝓔-𝓥𝓐𝓡𝓢! Userbot`"
    )


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2 ** 10
    zero = 0
    units = {0: "", 1: "Kb/s", 2: "Mb/s", 3: "Gb/s", 4: "Tb/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


CMD_HELP.update(
    {
        "ping": "`.ping`\
    \nUsage: Untuk menunjukkan ping bot.\
    \n\n`.speed`\
    \nUsage: Untuk menunjukkan kecepatan.\
    \n\n`.pong`\
    \nUsage: sama kaya perintah ping."
    }
)
