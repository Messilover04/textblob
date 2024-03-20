from textblob import TextBlob

def analisis_sentimientos_ok(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = "positivo"
    elif polarity < 0:
        sentiment = "negativo"
    else:
        sentiment = "neutro"
    print("Texto:", text)
    print("Polaridad:", polarity)
    print("Sentimiento:", sentiment)


text_ejemplo = "I love Kendrick Lamar music"
analisis_sentimientos_ok(text_ejemplo)