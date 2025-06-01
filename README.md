# Sentiment_Analysis
Sentiment analysis on Rotten Tomatoes movie reviews. This notebook covers data scraping, preprocessing, Word2Vec embeddings, and classification using SVM, Decision Tree, Logistic Regression, CNN, and BiLSTM. Includes code, explanations, and evaluation of model performance.

The Jupyter Notebook conducts sentiment analysis on Rotten Tomatoes movie reviews collected. The method is as follows:

- Data Collection & Preparation: Reviews are scraped, combined, and balanced both positively and negatively.
- Preprocessing: Cleaning of text, removal of stopwords, filtering of profanity, tokenization, and stemming.
- Feature Engineering: Word embeddings are generated using Word2Vec, and review vectors are created by averaging word vectors.
- Machine Learning Models: Three classifiers (Decision Tree, Logistic Regression, SVM) are tested and trained on the features generated.
- Deep Learning Models: Two neural network models (CNN and BiLSTM) are built and tested with hyperparameter and loss function exploration.
- Evaluation: The models are evaluated based on accuracy, F1-score, confusion matrices, and plots.
The notebook is reproducible and has code, explanation, and result interpretation at each step of the sentiment analysis pipeline.


Also, there is a folder that uses Scrapy Python framework to collect some critics' reviews from Rotten Tomatoes website.

Scrapy framework is a web scraper and web crawler that collects a few critics' reviews from Rotten Tomatoes website. The folder has specific files for the main script to run, the most_popular_movies folder has the main Python script named "most_popular_movies.py" in path "most_popular_movies\most_popular_movies\spiders". 
To run this crawler, this command must be run in terminal:


For the most popular movies: `scrapy crawl popular_movies`

This works because, Scrapy runs the class of the spider / main script and since the classe is called 'popular_movies' respectfully, you need to be in the **same folder as the spider and then run the command in terminal**.

So scrpay goes to the main page with the filter most popular, for example
![image](https://github.com/user-attachments/assets/78c5b5b5-a12b-49d2-bd2b-3976da4c3b73)

And then it searches for 300 pages, up to 800 movie titles. When it collects all the titles it keeps their URL as to go to the movies page and collect the first six reviews from critics. Then it saves the the movie title, URL, review as a text and the sentment of the review in a JSON file. This JSON file is named ```popular_reviews.json```.

![image](https://github.com/user-attachments/assets/9d6f3c03-e3c8-4e3d-bfee-08f43f6361f9)

![image](https://github.com/user-attachments/assets/a5c3edfc-986b-4ee1-a922-69ba5532d9f4)

And the results of the JSON files look like this:
```
{
    "title": "Carry-On",
    "url": "https://www.rottentomatoes.com/m/carry_on",
    "review": "Carry-On is never amazing, but it\u2019s an easy watch that contains plenty of thrills and two very reliable performers at its center. And it teaches people to be nicer to TSA agents this holiday season.",
    "sentiment": "POSITIVE"
},
{
    "title": "65",
    "url": "https://www.rottentomatoes.com/m/65",
    "review": "The premise doesn't hold up to close scrutiny and the narrative can be jarringly slow-paced.",
    "sentiment": "NEGATIVE"
},
{
    "title": "65",
    "url": "https://www.rottentomatoes.com/m/65",
    "review": "65 is a gruesome thing to watch, even for dinosaur lovers\u2014and not much fun, either.",
    "sentiment": "NEGATIVE"
}```
