# Sahte İndirim Dedektörü

## Problem ve Hedef Kitle
Bu proje; e-ticaret platformlarından alışveriş yapan bilinçli tüketicilerin, kampanya dönemlerinde ürün fiyatlarının önce yapay olarak şişirilip hemen ardından indirim yapılmış gibi gösterilmesiyle aldatılma ve ürünün gerçek tarihsel dip fiyatını takip edememe problemini çözmek amacıyla geliştirilmiştir.

## İş Takip Panosu
Proje görevleri, kabul kriterleri ve geliştirme süreci GitHub Projects panosu üzerinden takip edilebilir:
👉 [Sahte İndirim Dedektörü İş Takip Panosu](https://github.com/users/Beyza-Sual/projects/1)

## Kurulum ve Çalıştırma Adımları
Uygulama yalnızca Python standart kütüphanelerini (`json`, `os`, `datetime`) kullanır; harici bir paket kurulumu gerektirmez.

1. Depoyu bilgisayarınıza klonlayın:
   `git clone https://github.com/Beyza-Sual/sahte-indirim-dedektoru.git`
2. Proje klasörüne gidin:
   `cd sahte-indirim-dedektoru`
3. Uygulamayı çalıştırın (Python 3.x gereklidir):
   `python indirim_dedektoru.py`

## Tamamlanan Özellikler ve Test Adımları

### 1. Yeni Fiyat Kaydı Ekleme ve Sahte İndirim Analizi (Issue #1)
* **Test Adımı:** Uygulama menüsünden `1` seçeneğini girin. Aynı ürün adı (`Kulaklık`) için sırasıyla `1000`, `1500` ve `1100` TL fiyat girişlerini yapın.
* **Beklenen Sonuç:** Sistem ürünün önce 1000 TL'den 1500 TL'ye şişirilip ardından 1100 TL'ye düşürüldüğünü tespit ederek **`SAHTE İNDİRİM UYARISI!`** mesajı verir ve kayıtları `fiyat_verileri.json` dosyasına kaydeder.

### 2. Ürün Fiyat Geçmişi ve Gerçek En Düşük Fiyat Sorgulama (Issue #2)
* **Test Adımı:** En az iki veya üç fiyat kaydı ekledikten sonra uygulama menüsünden `2` seçeneğini girin ve sorgulanacak ürün adı olarak `Kulaklık` yazın.
* **Beklenen Sonuç:** Ürüne ait tüm fiyat hareketleri tarih sırasıyla listelenir ve görülen gerçek en düşük fiyat (`1000.0 TL`) ile en yüksek fiyat (`1500.0 TL`) ekranda gösterilir.
