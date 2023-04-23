# ronshuku
Summarize paper by using ChatGPT API

## Dependency
- Python 3.8

## Setup
Execute following commands:
```sh
$ git clone https://github.com/karaage0703/ronshuku
$ cd ronshuku
$ pip install -r requirements.txt
```

Write your open api secret key to `.config` file
```
[open_api_key]
key = your_secret_open_api_key
```

Optional(only posting discord): Write your discord webhook url to `.config` file
```
[discord_webhook]
url = your_discord_webhook_url
```

## Usage
### Summarize paper
Get random papers from AI field:
```sh
$ python3 ronshuku.py
```

Specific paper with arXiv ID:
```sh
$ python3 ronshuku.py --paper_id="<paper id>"
```

### Post Discord

```sh
$ python3 post_discord.py
```


## References
- https://zenn.dev/karaage0703/articles/926f18ba04e093
- https://zenn.dev/ozushi/articles/ebe3f47bf50a86
- https://github.com/ftnext/meetup-host-ops
