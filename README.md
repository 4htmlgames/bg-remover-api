# bg-remover-api

Flask tabanlı arka plan silme API servisi.

## Özellikler

- Görsellerin arka planını otomatik olarak kaldırır
- REST API desteği
- Render.com üzerinde kolay deployment

## Kurulum

```bash
pip install -r requirements.txt
```

## Kullanım

```bash
python app.py
```

API varsayılan olarak `http://localhost:5000` adresinde çalışır.

## API Endpoints

### GET /
API'nin çalışıp çalışmadığını kontrol eder.

### POST /remove-bg
Gönderilen görselin arka planını kaldırır.

**Parametreler:**
- `image`: Arka planı kaldırılacak görsel dosyası

**Örnek Kullanım:**
```bash
curl -X POST -F "image=@your-image.jpg" http://localhost:5000/remove-bg --output result.png
```

## Deployment

Bu proje Render.com üzerinde deploy edilebilir. `render.yaml` dosyası yapılandırmayı içerir.
