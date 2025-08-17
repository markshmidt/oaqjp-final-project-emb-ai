# Emotion Detection with Watson NLP

This project is a simple Flask web application that uses **IBM Watson NLP's EmotionPredict API** to analyze text and detect emotions such as **anger, disgust, fear, joy, and sadness**.  
It returns both the emotion scores and identifies the **dominant emotion**.

---

## Features
- REST API endpoint `/emotionDetector`
- Returns emotion scores for:
  - Anger
  - Disgust
  - Fear
  - Joy
  - Sadness
- Identifies the **dominant emotion**
- Error handling for blank/invalid input
- Unit tests included (`unittest`)
- PyLint-compliant (10/10 score)

