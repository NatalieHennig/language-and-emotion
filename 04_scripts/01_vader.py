import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

#nltk.download('vader_lexicon')

def add_vader_score(nr, pos=0.02, neg=-0.02):
  df = pd.read_csv("/Users/nataliehennig/Documents/language-and-emotion/05_output/{}_text_tokens.csv".format(nr))
  
  # get polarity scores from VADER
  sentiments = SentimentIntensityAnalyzer()
  df['vader_score'] = [sentiments.polarity_scores(i)["compound"] for i in df["token"]]
  
  # assign categorical values to the polarity scores
  score = df["vader_score"].values
  sentiment = []
  
  for i in score:
      if i >= pos:
          sentiment.append('Positive')
      elif i <= neg:
          sentiment.append('Negative')
      else:
          sentiment.append('Neutral')
          
  df["vader_polarity"] = sentiment
  
  #df.drop(df.columns[[4]], axis=1, inplace=True)
  df.to_csv("/Users/nataliehennig/Documents/language-and-emotion/05_output/{}_vader_scores.csv".format(nr))
