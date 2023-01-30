import datetime


def verify_api(search):
    """
    Run a search via tmdb for the query "Avengers: Endgame".
    If response title is also "Avengers: Endgame", it means 
    tmdb API has been set up correctly. Returns True.
    """
    response = search.movie(query='Avengers: Endgame')
    title = response['results'][0]['title']
    if title == 'Avengers: Endgame':
        return True
    return False


def update_db(df, search, db_type='movie'):
    """
    For each line in the csv file, first check if data has been 
    manually verified by checking the 'Verified' column.
    Otherwise, use tmdb to query the movie/show and fetch info 
    such as release year, imdb score, and poster .png url.
    """
    for idx, title in enumerate(df['Title']):
        if df.loc[idx, 'Verified'] == 'y':
            # skip already verified data
            continue
        if db_type == 'movie':
            response = search.movie(query=title)['results'][0]
        elif db_type == 'tv':
            response = search.tv(query=title)['results'][0]
        try:
            if db_type == 'movie':
                df.loc[idx, 'Title'] = str(response['title'])
                df.loc[idx, 'Year'] = int(datetime.datetime.strptime(
                    response['release_date'], '%Y-%m-%d').year)
            elif db_type == 'tv':
                df.loc[idx, 'Title'] = response['name']
                df.loc[idx, 'Year'] = int(datetime.datetime.strptime(
                    response['first_air_date'], '%Y-%m-%d').year)
            df.loc[idx, 'Poster'] = 'https://image.tmdb.org/t/p/w342' + \
                response['poster_path']
            df.loc[idx, 'Rating'] = response['vote_average']
        except Exception as e:
            print(title)
            print("\t", e)
    df['Year'] = df['Year'].astype(int)
    return df


def data2tag(soup=None, column_tag="nature", img="something.jpg", title="Mountain", info="Lorem ipsum dolor..", year='1990'):
    """
    Convert data including movie title, type, poster image, etc. 
    to a soup tag for an image grid like in:
    https://www.w3schools.com/howto/howto_js_portfolio_filter.asp
    """
    attributes = {'class': 'column ' + column_tag}
    new_div_tag = soup.new_tag("div", **attributes)
    attributes = {'class': 'content'}
    new_div_tag.insert(0, soup.new_tag("div", **attributes))
    new_div_tag.div.insert(0, soup.new_tag(
        "img", alt="content", src=img, style="width:100%"))
    new_div_tag.div.insert(1, soup.new_tag("h4"))
    new_div_tag.div.h4.string = '{} ({})'.format(title, year)
    new_div_tag.div.insert(2, soup.new_tag("p"))
    new_div_tag.div.p.string = info
    return new_div_tag
