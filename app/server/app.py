from fastapi import Request, FastAPI

from app.analyzer.textblob import TextBlobAnalyzer
from app.server.models.models import SearchQuery
from app.twitter.twitter_client import TwitterClient

app = FastAPI()
client = TwitterClient()
text_blob = TextBlobAnalyzer()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

@app.post("/search")
async def get_body(search: SearchQuery):
    tweets = client.read_tweeets(search.query)
    analyzed_tweets = {}
    for tweet in tweets:
        sentiment = text_blob.analyze(tweet[0])
        analyzed_tweets[tweet[0]] = sentiment

    return analyzed_tweets
