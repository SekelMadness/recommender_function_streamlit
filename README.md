# WebApp predicting Sentiment140 tweets
This app can recommend the top 5 article_ids from Globo.com user_ids.

# Context
This was a `kaggle competition` held several years ago.
See [News Portal User Interactions](https://www.kaggle.com/datasets/gspmoreira/news-portal-user-interactions-by-globocom#clicks_sample.csv) for much more detailed documentation.

# About the app
It is in fact a python `BayesianPersonalizedRanking	` model using an Azure serverless function.

# Librairies
You need to install first some python librairies:

```
Requests
streamlit
```

# Goal
As you know now, our main objective is to recommend for users the 5 articles that they may be interested to read.

## Target
* Top 5 article_ids

Our function `recommand_article` gives us a list of the top 5 article_ids.

## Recommandations
I strongly recommand you to install packages from the `requirements.txt`.