# Project 3. Reddit Classification with NLP (Dogs vs. Dogfree)


## Problem Statement

The main goal for this project collecting data by scraping Reddit website and then building a binary classifier to identify where a given post came from. <br>
For the project I chose highly correlated subreddits:
- Dog lovers subreddit - Dogs https://www.reddit.com/r/dogs/
- Dog haters subreddit - Dogfree https://www.reddit.com/r/Dogfree

This model could be used for identifying dog lovers and dog haters based on their posts in different social networks and websites and offer them target ads.

## Dataset
 - Data was gathered from Reddit's API, using the Python requests library. Reddit's API returns a JSON file with the page’s content. Collection was automated using AWS and Cron.
 - The final dataset contains 2245 rows and 3 columns

 ### Data dictionary
 | Column        | Type | Description                                              |
|---------------|-----------|----------------------------------------------------------|
| subreddit     | string   | which subreddit a post belongs to (dogs/dogfree)      |
| title    | string    | title of a subreddit post                   |
| selftext | string    | text of a  subreddit post if post contains it |

## Repo Structure
 - Code folder - Contains all Jupyter notebooks:
      1. 01_Data_collection.ipynb
      2. 02_Preprocessing_and_Modeling.ipynb
 - Datasets folder - Contains .csv files  - collected data from Reddit's API
 - Images folder - Contains images  
 - AWS folder - Contains script running on EC2 AWS and stats file
 - Presentation folder - Contains the presentation.



## Executive Summary
The project will do the following parts:
1. Data gathering from Reddit's API
2. Cleaning data
2. Doing an EDA
3. Text preprocessing
4. Modeling with Gridsearching Hyperparameters
5. Evaluating models


## Conclusions and findings
In spite of the fact that I chose highly correlated subreddits all three models (Logistic Regression, Naive Bayes and Random Forest) showed at least 1.7x better accuracy score than the baseline.
The best model is Logistic Regression, we can predict with an accuracy of about 95.4% where a given post came from, 19 out of 20 posts.


## Next steps
Further improvements for the model includes:
- better work with hyperparameters to reduce overfitting for Random Forest Classifier
