import numpy as np
import tensorflow as tf
import transformers as trf
from transformers import pipeline
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification

import logging
trf.logging.set_verbosity_error()

class SentimentClassifier:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
        self.sentiment_classifier = TFAutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")

    def getSentiment(self, input_sentence: str):
        inputs = self.tokenizer.encode_plus(input_sentence, padding=True, truncation=True, return_tensors="tf")
        outputs = self.sentiment_classifier(inputs["input_ids"])
        output_scores = np.array(outputs.logits)
        confidence_score = round(float(output_scores.max(axis=1)), 4)
        predicted_class = tf.argmax(output_scores, axis=1).numpy()[0]
        sentiment_labels = ["Negative", "Neutral", "Positive"]
        predicted_sentiment = sentiment_labels[predicted_class]
        return predicted_sentiment, confidence_score
    
class EmotionClassifier:
    def __init__(self):
        self.emotion_classifier = pipeline("text-classification",
                                      model='bhadresh-savani/distilbert-base-uncased-emotion',
                                      return_all_scores=True, top_k=1)
        
    def getEmotion(self, input_sentence: str):
        emotions_array = self.emotion_classifier(input_sentence)
        output_scores = max(emotions_array[0], key=lambda x: x['score'])
        predicted_emotion = output_scores['label']
        confidence_score = round(output_scores['score'], 4)
        return predicted_emotion, confidence_score