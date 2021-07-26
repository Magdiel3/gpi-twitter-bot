import flair
import re

flair_sentiment = flair.models.TextClassifier.load("en-sentiment")

def predict(sentence):
    # Pre-process sentence
    re.sub(r"@?(\w){1,15}","username",sentence)
    print(sentence)

    # Parse sentence
    s = flair.data.Sentence(sentence)
    
    # Predict rentiment
    flair_sentiment.predict(s)

    # Interprete and return result
    label = s.labels[0]
    
    if label.score > 0.55 and label.value == "NEGATIVE":
        return ("Gpin't", label)

    elif label.score > 0.35 and label.value == 'POSITIVE':
        return ("Gpi", label)

    else:
        return ("Tgp", label)