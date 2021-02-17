#!/usr/bin/env

# import libraries
import pandas as pd
import tmdbsimple as tmdb
import bs4
import argparse
from utils import verify_api, update_db, data2tag

with open('tmdb-api-key.txt', 'r') as f:
    tmdb.API_KEY = f.read().split('\n')[0]
search = tmdb.Search()


# first test if tmdb API_KEY works, along with internet connectivity
if verify_api(search) is False:
    print("Ensure that tmdb.API_KEY is correct.")
    exit()
else:
    print("API_KEY Verified!")

parser = argparse.ArgumentParser("Train optical Trojan")
parser.add_argument("--movie", action="store_true",
                    help="update only movie database (by default does movie and tv)")
parser.add_argument("--tv", action="store_true",
                    help="update only tv database (by default does movie and tv)")
args = parser.parse_args()

db_types = ['movie', 'tv']
if args.movie is True:
    db_types = ['movie']
elif args.tv is True:
    db_types = ['tv']

for db_type in db_types:
    df = pd.read_csv('db_{}.csv'.format(db_type), encoding='utf-8')
    df = update_db(df, search, db_type=db_type)

    with open("templates/{}.html".format(db_type)) as f:
        txt = f.read()
        soup = bs4.BeautifulSoup(txt, features='lxml')
    template = soup.find("div", class_="row")

    for i, item in enumerate(df.iloc):
        # print(item['Title'])
        tag = data2tag(soup, column_tag=item["Type"], img=item["Poster"],
                       title=item['Title'], info="", year=item["Year"])
        if i == 0:
            # replace if index is 0, i.e., first element
            template.div.replaceWith(tag)
        else:
            # append if index is not 0
            template.append(tag)

    # update html files with new soup tags
    with open('index_{}.html'.format(db_type), 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))
    if db_type == 'movie':
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))

    # update csv with fetched information
    df.to_csv('db_{}.csv'.format(db_type), index=False)
print("Done!")
