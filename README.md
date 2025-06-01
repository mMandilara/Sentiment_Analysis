# Sentiment_Analysis
Sentiment analysis on Rotten Tomatoes movie reviews. This notebook covers data scraping, preprocessing, Word2Vec embeddings, and classification using SVM, Decision Tree, Logistic Regression, CNN, and BiLSTM. Includes code, explanations, and evaluation of model performance.
--------------------------------

There is a folder that uses Scrapy Python framework to collect some critics' reviews from Rotten Tomatoes website.

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

![image](https://github.com/user-attachments/assets/c0cee01b-1085-48d7-90a6-a9ac070c90d0)

{
    "title": "65",
    "url": "https://www.rottentomatoes.com/m/65",
    "review": "65 is a gruesome thing to watch, even for dinosaur lovers\u2014and not much fun, either.",
    "sentiment": "NEGATIVE"
}
```


-------------
The Jupyter Notebook conducts sentiment analysis on Rotten Tomatoes movie reviews collected. The method is as follows:

- Data Collection & Preparation: Reviews are scraped, combined, and balanced both positively and negatively.
- Preprocessing: Cleaning of text, removal of stopwords, filtering of profanity, tokenization, and stemming.
- Feature Engineering: Word embeddings are generated using Word2Vec, and review vectors are created by averaging word vectors.
- Machine Learning Models: Three classifiers (Decision Tree, Logistic Regression, SVM) are tested and trained on the features generated.
- Deep Learning Models: Two neural network models (CNN and BiLSTM) are built and tested with hyperparameter and loss function exploration.
- Evaluation: The models are evaluated based on accuracy, F1-score, confusion matrices, and plots.
The notebook is reproducible and has code, explanation, and result interpretation at each step of the sentiment analysis pipeline.

## Machine Learning results:
The results of the machine learning algorithms have an accuracy of around 60% and generally satisfactory results, with an apparent tendency for all three to incorrectly predict negative emotions.

![Χωρίς τίτλο](https://github.com/user-attachments/assets/53896b59-bdf1-4760-9045-2acdee94fbc5)

![image](https://github.com/user-attachments/assets/0341427a-67f1-4405-8d7e-93910e0b1b1e)

## Neural Networks
And as for neural networks, it seems that CNN has an accuracy of close to 60% and very little loss, i.e. errors, of around 24%. While the BiLSTM method which expected better results has accuracy around 50% and loss similar to CNN.

![Χωρίς τίτλο](https://github.com/user-attachments/assets/e9ec2525-9a72-437d-9fec-b6fabbe5cbe8)


------
And here the results of *all the confusion matrix results* are shown and the SVM seems to predict most of them correctly as second comes the logistic regression and from the neural networks the CNN model has good predictions. We would expect much better results but the domain has difficulties where the algorithm can get confused such as ironic comments, or texts where they contain negative and positive emotions while they end up stating one of the two and we would need many more examples. The average accuracy of all of them was 50-60%.

![image](https://github.com/user-attachments/assets/132aebe2-498b-472a-97a8-51c8b73616c0)


