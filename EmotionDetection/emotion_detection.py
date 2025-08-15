"""Emotion detection module using Watson NLP API.

This module provides the `emotion_detector` function, which sends text to the
Watson NLP EmotionPredict service and returns the five emotion scores along
with the dominant emotion. Blank input and API errors are handled gracefully.
"""

import json
import requests

def emotion_detector(text_to_analyze):
    """Detect emotions in a given text using the Watson NLP API.

    Args:
        text_to_analyze (str): The text to be analyzed.

    Returns:
        dict: Dictionary containing scores for anger, disgust, fear, joy, sadness,
              and the dominant emotion. All values are None if input is invalid or
              an error occurs.
    """
    url = """https://sn-watson-emotion.labs.skills.network/v1/
    watson.runtime.nlp.v1/NlpService/EmotionPredict"""
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    anger = disgust = fear = joy = sadness = dominant_emotion = None
    none_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    if not text_to_analyze or not str(text_to_analyze).strip():
        return none_result

    response = requests.post(url, headers=headers, json=input_json, timeout=10)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response.get("emotionPredictions", [])[0].get("emotion", {})

        anger = emotions.get("anger", 0)
        disgust = emotions.get("disgust", 0)
        fear = emotions.get("fear", 0)
        joy = emotions.get("joy", 0)
        sadness = emotions.get("sadness", 0)

        scores = {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness
        }
        dominant_emotion = max(scores, key=scores.get)

    elif response.status_code in (400, 500):
        return none_result

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }
