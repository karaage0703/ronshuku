#!/usr/bin/env python3
import openai
import configparser
import arxiv
import random

config = configparser.ConfigParser()
config.read('.config')

openai.api_key = config.get('open_api_key', 'key')


def summarize_paper(paper):
    system = """
    論文を以下の制約に従って要約して出力してください。

    [制約]
    タイトルは日本語で書く
    要点は3つにまとめる


    [出力]
    タイトルの日本語訳

    ・要点1
    ・要点2
    ・要点3
    """

    text = f"title: {paper.title}\nbody: {paper.summary}"
    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {'role': 'system', 'content': system},
                    {'role': 'user', 'content': text}
                ],
                temperature=0.2,
            )

    summary = response['choices'][0]['message']['content']
    date_str = paper.published.strftime("%Y-%m-%d %H:%M:%S")
    message = f"発行日: {date_str}\n{paper.entry_id}\n{paper.title}\n{summary}\n"
    return message

def get_arxiv(query: str, paper_all_numb: int = 5, paper_select_numb: int = 3):
    # search arxiv paper
    result = arxiv.Search(
        query=query,
        max_results=paper_all_numb,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    ).results()

    return random.sample(list(result), k=paper_select_numb)


if __name__ == "__main__":
    paper_list = get_arxiv(query='deep learning', paper_all_numb=10, paper_select_numb=3)
    for i, paper in enumerate(paper_list):
        try:
            print(str(i+1) + '本目の論文')
            print(summarize_paper(paper))
        except:
            print('error')
