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

    def prec_rec_fscore(self, all_tweets, lib):
        key = lib + '_numeric'
        true_positives = 0
        false_positives = 1e-8  # Can't be 0 because of presence in denominator
        true_negatives = 0
        false_negatives = 1e-8
        for tweet in all_tweets:
            score = tweet[key]
            true = tweet["vader_numeric"]
            if score > 0.2 and true > 0.2:
                true_positives += 1
            elif score > 0.2 and true < 0.2:
                false_positives += 1
            elif score < 0.2 and true < 0.2:
                true_negatives += 1
            elif score < 0.2 and true > 0.2:
                false_negatives += 1
            precision = true_positives / (true_positives + false_positives)
            recall = true_positives / (true_positives + false_negatives)

            if precision + recall == 0:
                f_score = 0
            else:
                f_score = 2 * (precision * recall) / (precision + recall)

        return {
            "library": lib,
            "TP": true_positives,
            "FP": false_positives,
            "TN": true_negatives,
            "FN": false_negatives,
            "F-SCORE": f_score
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