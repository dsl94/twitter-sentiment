from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class VaderAnalyzer:
    def analyze(self, tweet):
        vader = SentimentIntensityAnalyzer()
        sentiment = vader.polarity_scores(tweet)["compound"]
        return sentiment
