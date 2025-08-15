"""Flask server for Watson NLP emotion detection with defensive handling."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Create Flask application instance
app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """Render the index page"""
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze the emotion for the provided text.

    The text is read from the `textToAnalyze` or `text` query parameter. If the
    upstream emotion detector reports an invalid input (dominant emotion is None),
    respond with an HTTP 400. Otherwise, return the required, human-readable
    sentence listing the five emotion scores and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze') or request.args.get("text")
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    response_sentence = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_sentence

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    