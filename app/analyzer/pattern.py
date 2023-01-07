from pattern.text.en import sentiment

class PatternAnalyzer:
    def analyze(self, tweet):
        return sentiment(tweet)[0]
