# Açıklama

Bu proje, bir ürün açıklamasını sınıflandırmak için bir FastAPI uygulamasıdır. Kullanıcı, bir ürün açıklaması girer ve model, bu açıklamanın hangi kategoriye ait olduğunu tahmin eder.

## Gereksinimler

- Python 3.7+
- FastAPI
- joblib
- NLTK
- scikit-learn

## Kurulum

1. Gerekli Python paketlerini yükleyin:

    ```bash
    pip install -r requierements.txt
    ```

## Kullanım

### Lokal Çalıştırma

1. FastAPI uygulamasını çalıştırın:

    ```bash
    uvicorn main:app --reload
    ```

2. Tarayıcınızda `http://127.0.0.1:8000` adresine gidin. Buradan ürün açıklamalarınızı girebilir ve modelin tahmin sonuçlarını görebilirsiniz.

### Docker ile Çalıştırma

1. Docker image oluşturun:

    ```bash
    docker build -t category_predictor_api .
    ```

2. Docker container başlatın:

    ```bash
    docker run -d -p 8000:8000 category_predictor_api
    ```

3. Tarayıcınızda `http://127.0.0.1:8000` adresine gidin. Buradan ürün açıklamalarınızı girebilir ve modelin tahmin sonuçlarını görebilirsiniz.

## Proje Yapısı

- `main.py`: FastAPI uygulamasının ana dosyası.
- `logistic_regression_model.joblib`: Logistic Regression model dosyası.
- `tfidf_vectorizer.joblib`: TF-IDF vectorizer dosyası.

## UI kullanımı için 
Tarayıcınızda `http://127.0.0.1:8000` adresine gidin. Buradan ürün açıklamalarınızı girebilir ve modelin tahmin sonuçlarını görebilirsiniz.

## API kullanımı için
```sh
curl 'http://127.0.0.1:8000/api/predict/' \
  --data-raw $'{
  "description": "Ürün Kodu : 40061255166 Genel Özellikler Panel Tipi : LED Ekran Boyutu : 18.5 inch Tepki Süresi : 5 ms Bağlantı Tipi : Analog Çözünürlük : 1366 x 768 Renk : Siyah Pivot : Yok Yükseklik Ayarı : Yok Vesa Uyumu : Var Garanti Süresi : 24 Ay"
}'

