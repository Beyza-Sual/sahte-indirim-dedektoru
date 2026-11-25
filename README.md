
# Sahte İndirim Dedektörü

E-ticaret platformlarındaki ürünlerin fiyat geçmişini takip eden, kampanya dönemlerinde fiyatı önce yapay olarak şişirip ardından indirim yapılmış gibi gösteren **sahte indirimleri tespit eden** ve gerçek tarihsel en düşük fiyatı hesaplayan Python tabanlı fiyat analiz uygulamasıdır.

## İş Takip Panosu (GitHub Projects)
Proje görevlerinin, kabul kriterlerinin ve geliştirme aşamalarının takip edildiği aktif Kanban panosuna aşağıdaki bağlantıdan ulaşabilirsiniz:
* **Pano Bağlantısı:** https://github.com/users/Beyza-Sual/projects/1

## Tamamlanan Özellikler
* **Yeni Fiyat Kaydı ve Sahte İndirim Analizi (#1):** Girilen ürün fiyatını önceki kayıtlarla karşılaştırır; ani fiyat şişirmesi sonrası yapılan sahte indirimleri, zamları ve gerçek alım fırsatlarını otomatik olarak raporlar.
* **Ürün Fiyat Geçmişi ve En Düşük Fiyat Sorgulama (#2):** Seçilen ürünün tüm fiyat hareketlerini tarih sırasıyla listeler ve bugüne kadar görülen en düşük/en yüksek gerçek fiyatları hesaplar.

## Planlanan Özellikler (Backlog)
* **Hedef Fiyat Alarmı Tanımlama (#3):** Kullanıcının belirlediği hedef fiyatın altına düşüldüğünde otomatik uyarı üretilmesi.
* **Fiyat Geçmişini CSV Olarak Dışa Aktarma (#4):** Analiz raporlarının `.csv` formatında bilgisayara kaydedilmesi.
* **E-Ticaret Bağlantısından Otomatik Fiyat Çekme (#5):** Ürün URL'si üzerinden güncel fiyatın otomatik olarak okunması.

## Kurulum ve Çalıştırma
Uygulama harici bir kütüphane gerektirmez, standart Python 3 ortamında doğrudan çalışır:

```bash
git clone https://github.com/Beyza-Sual/sahte-indirim-dedektoru.git
cd sahte-indirim-dedektoru
python indirim_dedektoru.py
