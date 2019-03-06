import argparse
import sys
import os
import random


pip_youtube_dl = "pip install youtube-dl"
pip_retrying = "pip install retrying"
#os.system(pip_youtube_dl)


fan_ren_xiu_xian_youtube_url_dict = {
    "https://www.youtube.com/playlist?list=PLTJaWZoVPdT0eJmyU007ErWp5nwgFD9gO":"0001-0200[1/8]",
    "https://www.youtube.com/playlist?list=PLTJaWZoVPdT3oYVeSSfh1Yd8LvDcdiOqS":"0201-0400[2/8]",
    "https://www.youtube.com/playlist?list=PLTJaWZoVPdT389mx3RdY1DUwQ6F6P3smD":"0401-0600[3/8]",
    "https://www.youtube.com/playlist?list=PLTJaWZoVPdT0cuaZ6q1RaqFBqxM5vT5aa":"0601-0800[4/8]",
    "https://www.youtube.com/playlist?list=PLTJaWZoVPdT0yL8JJfCsaRE51QypCKNCQ":"0801-1000[5/8]",
    "https://www.youtube.com/playlist?list=PLTJaWZoVPdT0nkqh0xUblhpDQYhgtZiFd":"1001-1200[6/8]",
    "https://www.youtube.com/playlist?list=PLTJaWZoVPdT1ePwvhqHLdDhfsHvsnZmWZ":"1201-1400[7/8]",
    "https://www.youtube.com/playlist?list=PLTJaWZoVPdT2X-cE47-s2k02ZY6y7SYrC":"1401-1631[8/8]",
}
fan_ren_xiu_xian_youtube_url_list = [url for url in fan_ren_xiu_xian_youtube_url_dict]



parser = argparse.ArgumentParser()
parser.add_argument("-p", "--part", type=int, choices=[0, 1, 2, 3, 4, 5, 6, 7, 8],
                    help="you can choices from part: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 0 is all!")
parser.add_argument("-ps",'--playlist_start', type=int)

args = parser.parse_args()

def pruduce_completed_URL(url):
    if args.playlist_start is None:
        youtube_dl_cmd = "youtube-dl --proxy https://127.0.0.1:1080 " + url
    else:
        youtube_dl_cmd = "youtube-dl --proxy https://127.0.0.1:1080 " + \
                         "--playlist-start" + " " + str(args.playlist_start) + \
                         " " + url
    return youtube_dl_cmd


def download_novel(youtube_dl_cmd):
    os.system(youtube_dl_cmd)
    print("下载完成！")


if __name__ == '__main__':
    if args.part is None:
        print("你必须指定小说的章节进行下载！0-8")
        assert args.part > -1
    if args.part==0: # 下载全部章节
        for url in fan_ren_xiu_xian_youtube_url_list:
            youtube_dl_cmd = pruduce_completed_URL(url)
            download_novel(youtube_dl_cmd)
    else: # 下载指定章节
        url = fan_ren_xiu_xian_youtube_url_list[args.part-1]
        youtube_dl_cmd = pruduce_completed_URL(url)
        download_novel(youtube_dl_cmd)








