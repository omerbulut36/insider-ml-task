FROM python:3.11-slim

# Gereksinimlerinizi belirten requirements.txt dosyasını container'a kopyalıyoruz
COPY requirements.txt .

# Gereksinimleri yükleyip gerekli Python paketlerini kuruyoruz
RUN pip install -r requirements.txt

# NLTK dosyalarını önden indiriyoruz.
RUN python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"

# Uygulama kodlarını container'a kopyalıyoruz
COPY ./api .

COPY ./models ./models

# FastAPI uygulamanızı çalıştırmak için gerekli komutu belirliyoruz
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
