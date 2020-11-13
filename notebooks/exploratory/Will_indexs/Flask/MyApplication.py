{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "from random import gauss as gs, uniform as uni, seed\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "from pyspark.sql import SparkSession\n",
    "from flask import Flask\n",
    "import math\n",
    "import sys\n",
    "import sys\n",
    "import time\n",
    "import argparse\n",
    "sys.path.insert(0, 'scripts/')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--2020-11-12 17:20:13--  http://files.grouplens.org/datasets/movielens/ml-latest-small.zip\n",
      "Resolving files.grouplens.org (files.grouplens.org)... 128.101.65.152\n",
      "Connecting to files.grouplens.org (files.grouplens.org)|128.101.65.152|:80... connected.\n",
      "HTTP request sent, awaiting response... 200 OK\n",
      "Length: 978202 (955K) [application/zip]\n",
      "Saving to: ‘../../data/ml-latest-small.zip.1’\n",
      "\n",
      "ml-latest-small.zip 100%[===================>] 955.28K  --.-KB/s    in 0.004s  \n",
      "\n",
      "2020-11-12 17:20:13 (214 MB/s) - ‘../../data/ml-latest-small.zip.1’ saved [978202/978202]\n",
      "\n"
     ]
    }
   ],
   "source": [
    "! wget -P ../../data http://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "import zipfile\n",
    "with zipfile.ZipFile('../../data/ml-latest-small.zip', 'r') as zip_ref:\n",
    "    zip_ref.extractall('../../../data')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "links_df = pd.read_csv('../../../data/ml-latest-small/links.csv')\n",
    "movies_df = pd.read_csv('../../../data/ml-latest-small/movies.csv')\n",
    "ratings_df = pd.read_csv('../../../data/ml-latest-small/ratings.csv')\n",
    "tags_df = pd.read_csv('../../../data/ml-latest-small/tags.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "movie_ratings = links_df.merge(movies_df, on=[\"movieId\"])\n",
    "movie_ratings = ratings_df.merge(movie_ratings, on=[\"movieId\"])\n",
    "movie_ratings = movie_ratings.merge(tags_df, on=[\"movieId\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "movie_ratings[\"liked\"] = movie_ratings['rating'].apply(lambda x: 1 if x >= 4.0 else 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_title_from_index(movie_id):\n",
    "    return movie_ratings[movie_ratings.movieId == movie_id][\"title\"].values[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/')\n",
    "def bayes_ucb1_policy(df, ucb_scale=2.0):\n",
    "    '''\n",
    "    Applies Bayesian UCB policy to generate movie recommendations\n",
    "    Args:\n",
    "        df: dataframe. Dataset to apply Bayesian UCB policy to.\n",
    "        ucb_scale: float. Most implementations use 2.0.\n",
    "    '''\n",
    "    scores = df[['movieId', 'liked']].groupby('movieId').agg({'liked': ['mean', 'count', 'std']})\n",
    "    scores.columns = ['mean', 'count', 'std']\n",
    "    scores['ucb'] = scores['mean'] + (ucb_scale * scores['std'] / np.sqrt(scores['count']))\n",
    "    scores['movieId'] = scores.index\n",
    "    scores = scores.sort_values('ucb', ascending=False)\n",
    "    recs = scores.loc[scores.index[0:6], 'movieId'].values\n",
    "    movie_name = []\n",
    "    for movieid in recs:\n",
    "        movie_name.append(get_title_from_index(movieid))\n",
    "    return movie_name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Horse Feathers (1932)',\n",
       " 'Mean Creek (2004)',\n",
       " 'Gross Anatomy (a.k.a. A Cut Above) (1989)',\n",
       " 'Salaam Bombay! (1988)',\n",
       " 'Danny Deckchair (2003)',\n",
       " 'One, Two, Three (1961)']"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bayes_ucb1_policy(movie_ratings, ucb_scale=2.0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (oy-env)",
   "language": "python",
   "name": "oy-env"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
