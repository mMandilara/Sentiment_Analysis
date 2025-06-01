import scrapy
from scrapy.crawler import CrawlerProcess
from ..items import MostPopularMoviesItem
import os
import json

# !To run this script go to path - where most_popular_movies folser is - and run in command window 'scrapy crawl popular_movies'!
class MoviesSpider(scrapy.Spider):
  name = 'popular_movies'
  allowed_domains = ['rottentomatoes.com']

  def __init__(self, *args, **kwargs):
    super(MoviesSpider, self).__init__(*args, **kwargs)
    self.item_count = 1
    self.max_item_total = 800
    self.output_file = 'popular_reviews.json'

    # Dynamically create start_urls for pages 1-300
    self.start_urls = [f'https://www.rottentomatoes.com/browse/movies_at_home/sort:popular?page={page}' for page in range(1, 301)]

    # Check if the file exists and is not empty
    if os.path.exists(self.output_file) and os.path.getsize(self.output_file) > 0:
      os.remove(self.output_file)

  def parse(self, response):
    all_div = response.css('div.discovery-tiles__wrap')[:self.max_item_total]

    for movie in all_div:
      titles = movie.css('span.p--small::text').getall()
      hrefs = movie.css('a::attr(href)').getall()

      if len(titles) != len(hrefs):
        continue  # Skip if there's a mismatch

      for title, href in zip(titles, hrefs):
        full_url = f"https://www.rottentomatoes.com{href}"

        movie_data = {
          'title': title.strip(),
          'url': full_url,
          'review': [],
          'sentiment': []
        }

        yield scrapy.Request(full_url, callback=self.parse_movie_page, cb_kwargs={'movie_data': movie_data})

  def parse_movie_page(self, response, movie_data):
      critics_reviews = response.css('div.modules-layout section.critics-reviews media-review-card-critic drawer-more rt-text::text').extract()
      critics_sentiments = response.css('div.modules-layout section.critics-reviews media-review-card-critic score-icon-critics::attr(sentiment)').extract()

      for i in range(len(critics_reviews)):
          individual_review = critics_reviews[i].strip()
          sentiment = critics_sentiments[i]

          review_data = {
              'title': movie_data['title'],
              'url': movie_data['url'],
              'review': individual_review,
              'sentiment': sentiment
          }

          self.extract(review_data)

  def extract(self, movie_data):
      with open(self.output_file, 'a') as f:
          if f.tell() == 0:
              f.write('[\n')
          else:
              f.write(',\n')
          json.dump(movie_data, f, indent=4)

  def closed(self, reason):
      with open(self.output_file, 'a') as f:
          f.seek(0, 2)  # move to the end of the file
          if f.tell() > 2:  # is file empty?
              f.seek(f.tell())
              f.truncate()
              f.write('\n]\n')


if __name__ == '__main__':
  process = CrawlerProcess()
  process.crawl(MoviesSpider)
  process.start()
