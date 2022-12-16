from textblob import TextBlob


class TextBlobAnalyzer():
    def analyze(self, tweet):
        return TextBlob(tweet).sentiment.polarity