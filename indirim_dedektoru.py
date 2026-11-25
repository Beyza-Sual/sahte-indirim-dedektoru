import json
import os
from datetime import datetime

VERI_DOSYASI = "fiyat_verileri.json"


def verileri_yukle():
    if not os.path.exists(VERI_DOSYASI):
        return {}
    with open(VERI_DOSYASI, "r", encoding="utf-8") as dosya:
        return json.load(dosya)


def verileri_kaydet(veriler):
    with open(VERI_DOSYASI, "w", encoding="utf-8") as dosya:
        json.dump(veriler, dosya, ensure_ascii=False, indent=4)


def fiyat_ekle_ve_analiz_et(urun_adi: str, yeni_fiyat: float):
    veriler = verileri_yukle()
    urun_anahtari = urun_adi.strip().lower()

    if urun_anahtari not in veriler:
        veriler[urun_anahtari] = {
            "gorunen_ad": urun_adi.strip(),
            "gecmis": []
        }

    gecmis = veriler[urun_anahtari]["gecmis"]
    tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    durum_mesaji = "İLK KAYIT: Ürün fiyat takibi başlatıldı."

    if len(gecmis) >= 1:
        son_fiyat = gecmis[-1]["fiyat"]
        en_dusuk_fiyat = min(kayit["fiyat"] for kayit in gecmis)

        if yeni_fiyat > son_fiyat:
            durum_mesaji = f"ZAM TESPİT EDİLDİ: Fiyat {son_fiyat} TL -> {yeni_fiyat} TL seviyesine yükseldi."
        elif yeni_fiyat < son_fiyat:
            if len(gecmis) >= 2 and son_fiyat > gecmis[-2]["fiyat"] and yeni_fiyat >= gecmis[-2]["fiyat"]:
                durum_mesaji = (
                    f"SAHTE İNDİRİM UYARISI! Fiyat önce {gecmis[-2]['fiyat']} TL'den "
                    f"{son_fiyat} TL'ye şişirilip şimdi {yeni_fiyat} TL'ye düşürülmüş!"
                )
            elif yeni_fiyat <= en_dusuk_fiyat:
                durum_mesaji = f"GERÇEK İNDİRİM (ALIM FIRSATI)! Ürün en düşük fiyatına ({yeni_fiyat} TL) indi."
            else:
                durum_mesaji = f"NORMAL İNDİRİM: Fiyat {son_fiyat} TL'den {yeni_fiyat} TL'ye düştü (En düşük: {en_dusuk_fiyat} TL)."
        else:
            durum_mesaji = "DEĞİŞİKLİK YOK: Fiyat sabit kaldı."

    gecmis.append({
        "tarih": tarih,
        "fiyat": yeni_fiyat,
        "analiz": durum_mesaji
    })
    verileri_kaydet(veriler)
    print(f"\n[{veriler[urun_anahtari]['gorunen_ad']}] -> {durum_mesaji}\n")


def urun_gecmisini_sorgula(urun_adi: str):
    veriler = verileri_yukle()
    urun_anahtari = urun_adi.strip().lower()

    if urun_anahtari not in veriler:
        print("\n[!] Bu ürün için kayıtlı fiyat geçmişi bulunamadı.\n")
        return

    urun = veriler[urun_anahtari]
    gecmis = urun["gecmis"]
    en_dusuk_fiyat = min(kayit["fiyat"] for kayit in gecmis)
    en_yuksek_fiyat = max(kayit["fiyat"] for kayit in gecmis)

    print(f"\n--- {urun['gorunen_ad']} Fiyat Geçmişi ---")
    for sira, kayit in enumerate(gecmis, 1):
        print(f"{sira}. [{kayit['tarih']}] {kayit['fiyat']} TL -> {kayit['analiz']}")
    print("-------------------------------------------")
    print(f"Görülen En Düşük Fiyat : {en_dusuk_fiyat} TL")
    print(f"Görülen En Yüksek Fiyat: {en_yuksek_fiyat} TL\n")


def ana_menu():
    while True:
        print("=== Sahte İndirim Dedektörü ===")
        print("1. Yeni Fiyat Ekle ve İndirim Analizi Yap")
        print("2. Ürün Fiyat Geçmişini ve En Düşük Fiyatı Sorgula")
        print("3. Çıkış")
        secim = input("Seçiminiz (1-3): ").strip()

        if secim == "1":
            ad = input("Ürün adı: ")
            try:
                fiyat = float(input("Güncel fiyat (TL): "))
                fiyat_ekle_ve_analiz_et(ad, fiyat)
            except ValueError:
                print("\n[!] Lütfen geçerli bir sayısal fiyat girin.\n")
        elif secim == "2":
            ad = input("Sorgulanacak ürün adı: ")
            urun_gecmisini_sorgula(ad)
        elif secim == "3":
            print("Uygulamadan çıkılıyor...")
            break
        else:
            print("\n[!] Geçersiz seçim, lütfen 1-3 arası bir değer girin.\n")


if __name__ == "__main__":
    ana_menu()
