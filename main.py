from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from joblib import load
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Ön işleme için gerekli bileşenler
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words('turkish'))
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)


# Modeli ve vectorizer'ı yükleyin
lg_model = load('./models/logistic_regression_model.joblib')
vectorizer = load('./models/tfidf_vectorizer.joblib')

# FastAPI uygulaması oluşturun
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>FastAPI Text Classification</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    background-color: #f4f4f9;
                }
                h1 {
                    color: #333;
                }
                form {
                    background: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }
                textarea {
                    width: 100%;
                    padding: 10px;
                    margin: 10px 0;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }
                input[type="submit"] {
                    background-color: #4CAF50;
                    color: white;
                    padding: 15px 20px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #45a049;
                }
                .result {
                    margin-top: 20px;
                    padding: 10px;
                    background: #fff;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }
            </style>
        </head>
        <body>
            <h1>Product Description Classification</h1>
            <form action="/predict/" method="post">
                <textarea name="description" rows="6" placeholder="Enter your product description here..."></textarea><br>
                <input type="submit" value="Predict">
            </form>
            <div class="result">
                <h2>Prediction Result:</h2>
                <div id="prediction">{}</div>
            </div>
        </body>
    </html>
    """

@app.post("/predict/", response_class=HTMLResponse)
async def predict(description: str = Form(...)):
    processed_text = preprocess_text(description)
    text_tfidf = vectorizer.transform([processed_text])
    prediction = lg_model.predict(text_tfidf)
    return f"""
    <html>
        <head>
            <title>FastAPI Text Classification</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    background-color: #f4f4f9;
                }}
                h1 {{
                    color: #333;
                }}
                form {{
                    background: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }}
                textarea {{
                    width: 100%;
                    padding: 10px;
                    margin: 10px 0;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }}
                input[type="submit"] {{
                    background-color: #4CAF50;
                    color: white;
                    padding: 15px 20px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }}
                input[type="submit"]:hover {{
                    background-color: #45a049;
                }}
                .result {{
                    margin-top: 20px;
                    padding: 10px;
                    background: #fff;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }}
            </style>
        </head>
        <body>
            <h1>Product Description Classification</h1>
            <form action="/predict/" method="post">
                <textarea name="description" rows="6" placeholder="Enter your product description here..."></textarea><br>
                <input type="submit" value="Predict">
            </form>
            <div class="result">
                <h2>Prediction Result:</h2>
                <div id="prediction">{prediction[0]}</div>
            </div>
        </body>
    </html>
    """

class PredictRequest(BaseModel):
    description: str


@app.post("/api/predict/")
async def predict(request: PredictRequest):
    processed_text = preprocess_text(request.description)
    text_tfidf = vectorizer.transform([processed_text])
    prediction = rf_model.predict(text_tfidf)
    return {'prediction': prediction.tolist()}
