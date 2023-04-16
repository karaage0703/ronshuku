# Reference
# https://github.com/ftnext/meetup-host-ops/blob/6581cb86914912633b117a7297e09a83c0f06764/discord.py

import json
from urllib.request import Request, urlopen
import configparser
from ronshuku import get_arxiv, summarize_paper

config = configparser.ConfigParser()
config.read('.config')

webhook_url = config.get('discord_webhook', 'url')


def post_discord(message: str, webhook_url: str):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "DiscordBot (private use) Python-urllib/3.10",
    }
    data = {"content": message}
    request = Request(
        webhook_url,
        data=json.dumps(data).encode(),
        headers=headers,
    )

    with urlopen(request) as res:
        assert res.getcode() == 204

if __name__ == "__main__":
    paper_list = get_arxiv(query='deep learning', paper_all_numb=100, paper_select_numb=3)
    for i, paper in enumerate(paper_list):
        try:
            print(str(i+1) + '本目の論文')
            post_discord(summarize_paper(paper), webhook_url)
        except:
            print('error')
