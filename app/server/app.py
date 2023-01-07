from fastapi import Request, FastAPI

from app.analyzer.textblob import TextBlobAnalyzer
from app.analyzer.vader import VaderAnalyzer
from app.analyzer.analyzer import Analyzer
from app.analyzer.pattern import PatternAnalyzer
from app.server.models.models import SearchQuery
from app.twitter.twitter_client import TwitterClient

app = FastAPI()
client = TwitterClient()
text_blob = TextBlobAnalyzer()
vader = VaderAnalyzer()
pattern = PatternAnalyzer()
analyzer = Analyzer()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

@app.post("/search")
async def search(search: SearchQuery):
    tweets = client.read_tweeets(search.query, search.max_results)
    analyzed_tweets = []
    for tweet in tweets:
        text_blob_sentiment = text_blob.analyze(tweet[0])
        vader_sentiment = vader.analyze(tweet[0])
        pattern_sentiment = pattern.analyze(tweet[0])
        analyzed_tweet = {
            "original": tweet[0],
            "text_blob": num_to_text(text_blob_sentiment),
            "text_blob_numeric": text_blob_sentiment,
            "vader": num_to_text(vader_sentiment),
            "vader_numeric": vader_sentiment,
            "pattern": num_to_text(pattern_sentiment),
            "pattern_numeric": pattern_sentiment
        }
        analyzed_tweets.append(analyzed_tweet)

    result = {
        "analyzed_tweets": analyzed_tweets,
        "results_per_library": analyzer.extract_results_per_library(analyzed_tweets),
        "sentiment_per_library": analyzer.extract_number_of_different_sentiments_per_library(analyzed_tweets),
    }

    return result

@app.post("/search-test")
async def searchTest(search: SearchQuery):
    tweets = client.read_tweeets(search.query)

    return tweets

def num_to_text(num):
    if num < -0.6:
        return "Very negative (" + num.__str__() + ")"
    if num < -0.2:
        return "Negative (" + num.__str__() + ")"
    if num < 0.2:
        return "Neutral (" + num.__str__() + ")"
    if num < 0.6:
        return "Positive (" + num.__str__() + ")"
    return "Very positive (" + num.__str__() + ")"
