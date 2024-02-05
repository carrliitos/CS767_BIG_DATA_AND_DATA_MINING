from bs4 import BeautifulSoup
import re
import pandas as pd

def main():
    titles = []
    years = []
    ratings = []
    ranks = []

    with open("data-raw/top_1000.html") as fp:
        soup = BeautifulSoup(fp, "html.parser")

    movie_divs = soup.find_all('div', class_='lister-item')

    for movie_div in movie_divs:
        title_tag = movie_div.find('h3', class_='lister-item-header').a
        year_tag = movie_div.find('span', class_='lister-item-year')
        rating_tag = movie_div.find('span', class_='ipl-rating-star__rating')
        rank_tag = movie_div.find('span', class_='lister-item-index unbold text-primary')

        movie_title = title_tag.text
        year_text = year_tag.text.strip('()')
        numeric_year = re.search(r'\b\d+\b', year_text).group() if re.search(r'\b\d+\b', year_text) else None
        movie_rating = rating_tag.text
        movie_rank = rank_tag.text.replace(".", "").replace(",", "")        

        titles.append(movie_title)
        years.append(numeric_year)
        ratings.append(movie_rating)
        ranks.append(movie_rank)

    data = {'Title': titles, 'Year': years, 'Rating': ratings, 'Rank': ranks}
    df = pd.DataFrame(data)

    with open("./data-raw/movie_data.csv", "wb") as data_file:
        df.to_csv(data_file, index=False)


if __name__ == '__main__':
    main()

