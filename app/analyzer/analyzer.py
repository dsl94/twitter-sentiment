class Analyzer:
    def extract_results_per_library(self, all_results):
        vader = []
        text_blob = []
        pattern = []
        for result in all_results:
            vader.append(result['vader_numeric'])
            text_blob.append(result['text_blob_numeric'])
            pattern.append(result['pattern_numeric'])
        return {
            "vader": vader,
            "text_blob": text_blob,
            "pattern": pattern
        }


    def extract_number_of_different_sentiments_per_library(self, all_results):
        vader_very_positive, vader_positive, vader_neutral, vader_negative, vader_very_negative = 0,0,0,0,0
        pattern_very_positive, pattern_positive, pattern_neutral, pattern_negative, pattern_very_negative = 0,0,0,0,0
        text_blob_very_positive, text_blob_positive, text_blob_neutral, text_blob_negative, text_blob_very_negative = 0,0,0,0,0

        for result in all_results:
            if "Very positive" in result['vader']:
                vader_very_positive = vader_very_positive + 1
            elif "Positive" in result['vader']:
                vader_positive = vader_positive + 1
            elif "Neutral" in result['vader']:
                vader_neutral = vader_neutral + 1
            elif "Very negative" in result['vader']:
                vader_very_negative = vader_very_negative + 1
            else:
                vader_negative = vader_negative + 1

            if "Very positive" in result['pattern']:
                pattern_very_positive = pattern_very_positive + 1
            elif "Positive" in result['pattern']:
                pattern_positive = pattern_positive + 1
            elif "Neutral" in result['pattern']:
                pattern_neutral = pattern_neutral + 1
            elif "Very negative" in result['pattern']:
                pattern_very_negative = pattern_very_negative + 1
            else:
                pattern_negative = pattern_negative + 1

            if "Very positive" in result['text_blob']:
                text_blob_very_positive = text_blob_very_positive + 1
            elif "Positive" in result['text_blob']:
                text_blob_positive = text_blob_positive + 1
            elif "Neutral" in result['text_blob']:
                text_blob_neutral = text_blob_neutral + 1
            elif "Very negative" in result['text_blob']:
                text_blob_very_negative = text_blob_very_negative + 1
            else:
                text_blob_negative = text_blob_negative + 1

        return {
            "vader_very_positive": vader_very_positive,
            "vader_positive": vader_positive,
            "vader_neutral": vader_neutral,
            "vader_negative": vader_negative,
            "vader_very_negative": vader_very_negative,
            "pattern_very_positive": pattern_very_positive,
            "pattern_positive": pattern_positive,
            "pattern_neutral": pattern_neutral,
            "pattern_negative": pattern_negative,
            "pattern_very_negative": pattern_very_negative,
            "text_blob_very_positive": text_blob_very_positive,
            "text_blob_positive": text_blob_positive,
            "text_blob_neutral": text_blob_neutral,
            "text_blob_negative": text_blob_negative,
            "text_blob_very_negative": text_blob_very_negative,
        }