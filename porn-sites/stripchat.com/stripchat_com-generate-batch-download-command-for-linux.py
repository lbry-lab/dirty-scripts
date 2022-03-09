import requests
import re
from datetime import datetime
import os

headers = {'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36', 
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
            }

linux_cmd = ""

while True:
    url = input(">>> ")
    #print(url)
    try:
        r = requests.get(url, headers=headers).text
        room_id = re.search("(\d+)_webp", r)[1]
        star_id = re.search("zh\.stripchat\.com/([\w\-_]+)", r)[1]
    except:
        pass
    format_time = datetime.now().strftime("%Y-%m-%d %H_%M_%S")
    cmd = '(streamlink https://b-hls-19.strpst.com/hls/{room_id}/master/{room_id}_auto.m3u8 best --output "{star_id} {format_time}-{star_id}.mp4"> /dev/null 2>&1 )&\nsleep 1'
    #tammarra_ 2022-02-08 19_19-_tammarra_.mp4
    #print(cmd.format(room_id = room_id, star_id = star_id, format_time = format_time))
    excute_cmd = cmd.format(room_id = room_id, star_id = star_id, format_time = format_time)
    #os.system(excute_cmd)
    linux_cmd += excute_cmd + "\n"
    #print(excute_cmd)
    #print("excute_time: ", format_time, "\n")
    if url == "exit":
        break

print(linux_cmd)
