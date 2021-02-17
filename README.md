## Image Gallery

Live demo: [https://ajboloor.github.io/image-gallery](https://ajboloor.github.io/image-gallery)

## Requirements

Install requirements:
```
pip3 install -r requirements.txt
```

- BeautifulSoup [[link](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)]
- pandas [[link](https://pandas.pydata.org/)]
- tmdbsimple [[link](https://github.com/celiao/tmdbsimple)]

## Usage
1. Install requirements stated above.
2. Create an account on [The Movie Database](https://www.themoviedb.org/account/signup), and generate an API key.
3. Copy and paste the API key into a new file called `tmdb-api-key.txt`
4. Use the provided `.csv` files like `db_movie.csv` as a template and add (or remove rows), you only have to fill in the title column and the type column.
5. Run `python3 update-database.py` to update the `.csv` and `.html` files.
6. Open `index.html` in a browser.

## References
- [HTML Portfolio Gallery with Filtering](https://www.w3schools.com/howto/howto_js_portfolio_filter.asp)
- [Hoverable Dropdown](https://www.w3schools.com/howto/howto_css_dropdown.asp)
- [The Movie Database (TMDb)](https://www.themoviedb.org/)
