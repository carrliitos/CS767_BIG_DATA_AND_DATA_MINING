from bs4 import BeautifulSoup
import re
import pandas as pd
import uuid

def main():
    titles = []
    years = []
    ratings = []
    ranks = []
    unique_ids = []

    with open("../data-raw/rottentomatoestop1000.html") as fp:
        soup = BeautifulSoup(fp, "html.parser")

    movie_divs = soup.find_all('div', class_='list-item')

    for movie_div in movie_divs:
        name_with_year = movie_div.find('div', class_='item-name').text.strip()
        rt_score_tag = movie_div.find('div', class_='rt-score')
        rt_score_text = rt_score_tag.find('a').text
        
        unique_id = str(uuid.uuid4())

        movie_title = name_with_year.rsplit(' ', 1)[0]
        movie_year = name_with_year.rsplit(' ', 1)[-1].strip('()')
        movie_rt_score = ''.join(char for char in rt_score_text if char.isdigit())
        movie_rank = movie_div.find('div', class_="item-rank").text

        titles.append(movie_title)
        years.append(movie_year)
        ratings.append(movie_rt_score)
        ranks.append(movie_rank)
        unique_ids.append(unique_id)

    data = {'ID': unique_ids, 'Title': titles, 'Year': years, 'Rating': ratings, 'Rank': ranks}
    df = pd.DataFrame(data)

    with open("../data-raw/rt_movie_data.csv", "wb") as data_file:
        df.to_csv(data_file, index=False)

if __name__ == '__main__':
    main()
