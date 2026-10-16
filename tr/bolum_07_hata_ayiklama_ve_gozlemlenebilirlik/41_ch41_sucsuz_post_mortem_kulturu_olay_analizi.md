# 41. Post-Mortem Kültürü: 'Kimi Suçlayacağız?' Değil, 'Nasıl Öğreneceğiz?'

**Production Çöktüğünde Mühendisleri Suçlamayan Şirketlerin Yükselişi**  
*Bölüm 7 • Zorluk Derecesi: Orta / İleri Seviye • Tahmini Okuma Süresi: 12 dk*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Notları
> **Podcast Tartışma Sorusu:**  
> *"Bir junior mühendis ilk haftasında yanlışlıkla canlı veritabanını sildiğinde kovulmalı mı, yoksa bir junior'ın canlı veritabanını silebildiği bir sisteme izin veren mimari mi hatalıdır?"*  
> 
> **Bölümden Çıkarılacak 3 Altın Cümle:**  
> - 📌 Suçsuz Post-Mortem (Blameless Post-Mortem), insan hatasını sistemik bir tasarım zaafı olarak ele alma disiplinidir.
- 📌 Eğer bir mühendis bir tuşa basarak tüm sistemi çökertebiliyorsa, hata mühendiste değil; o tuşa korkuluk koymayan süreçtedir.
- 📌 5 Neden (5 Whys) analizi ile yüzeysel bahaneleri aşıp kök mimari zafiyete ulaşılır.

---

## 📖 1. Giriş Hikayesi & Günlük Hayat Analojisi

2017 yılında Amazon AWS'de çalışan bir mühendis, faturalandırma sunucularındaki birkaç test sunucusunu kapatmak için terminale bir komut yazdı. Küçük bir yazım hatası (typo) yaptı ve Kuzey Amerika'daki S3 depolama sunucularının devasa bir kısmını kapattı! Tüm dünya çapında binlerce popüler internet sitesi 4 saat boyunca çöktü.

Amazon o mühendisi kovdu mu? **HAYIR!**

Amazon yönetimi şunu söyledi: *"Mühendisimiz kötü niyetli değildi. Sorun, tek bir insanın yazdığı tek bir komutla bu kadar devasa bir sistemin çökmesine izin veren güvenlik bariyerlerimizin eksikliğidir."*

Komutun etkisini kısıtlayan yeni güvenlik sistemleri kuruldu ve o mühendis şirketin en kıdemli çalışanlarından biri olarak kalmaya devam etti.

İşte olgun bir mühendislik kültürü budur: İnsanları suçlamak hataları gizlemeye iter; sistemleri düzeltmek ise şirketi ölümsüz kılar.

---

## 🧠 2. AI Çağında Yeni Zihniyet Modeli

5 Neden (5 Whys) Kök Neden Analizi Örneği:

```
[OLAY: Canlı veritabanı 45 dakika boyunca çöktü]
  │
  ├─ 1. Neden çöktü? ──> Disk doldu.
  │
  ├─ 2. Disk neden doldu? ──> Debug log dosyaları 500 GB yer kapladı.
  │
  ├─ 3. Loglar neden silinmedi? ──> Log rotasyonu (logrotate) yapılandırılmamıştı.
  │
  ├─ 4. Neden yapılandırılmamıştı? ──> Yeni kurulan sunucu için checklist takip edilmedi.
  │
  └─ 5. KÖK NEDEN: Sunucu kurulumları elle (manual) yapılıyor; Infrastructure as Code (Terraform) otomasyonu yok!
───────────────────────────────────────────────────────────────────────
AKSIYON: "Mühendisi azarla" değil -> "Tüm sunucuları Terraform ile otomatik kur ve log alarmı ekle!"
```

---

## 🤖 3. AI Prompt Laboratuvarı (Kopyala-Yapıştır Hazır Prompt)

Aşağıdaki prompt şablonunu Cursor, Claude Code, ChatGPT veya Copilot ortamınızda doğrudan kullanabilirsiniz:

```markdown
# ROL: Site Reliability Engineering (SRE) ve Olay Analiz Uzmanı
Dün gece yaşanan bir kesinti için 'Suçsuz Post-Mortem (Blameless Post-Mortem)' raporu hazırlayacağız.

## OLAY BİLGİSİ:
- Tarih: 15 Ekim 2026, 22:15 - 23:00 (45 dk kesinti)
- Etki: Kullanıcılar ödeme yapamadı, yaklaşık 40.000 TL ciro kaybı oluştu.
- Tetikleyici: Yeni yayınlanan güncellemedeki hatalı bir `.env` ortam değişkeni.

## GÖREV:
Profesyonel bir Post-Mortem markdown raporu hazırla:
1. Olay Özeti & Zaman Çizelgesi (Timeline)
2. 5 Neden (5 Whys) Kök Neden Analizi
3. 'Neler İyi Gitti?' ve 'Neler Kötü Gitti?'
4. Önleyici Eylem Maddeleri (Action Items - Sahibi ve Bitiş Tarihi olan somut görevler)
```

---

## 💻 4. Kod İncelemesi: Acemi / Halüsinasyon vs. Üretim Kalitesi

#### ❌ Acemi / Kontrolsüz AI Çıktısı (Riskli):
```markdown
# Kötü / Suçlayıcı Rapor:
Dün gece Ahmet yanlış .env dosyasını yüklediği için sistem çöktü.
Ahmet uyarıldı, bir daha yapmayacak.
```

#### ✅ Kıdemli Mühendis Tarafından İyileştirilmiş Sürüm (Güvenli & Temiz):
```markdown
# POST-MORTEM RAPORU: [INC-2026-10-15] Ödeme Servisi Kesintisi

## 📋 Yönetici Özeti
15 Ekim 2026 saat 22:15'te ödeme servisi, eksik bir ortam değişkeni (`STRIPE_WEBHOOK_SECRET`) nedeniyle başlatılamamış ve 45 dakika boyunca ödeme alınamamıştır. Toplam 120 işlem etkilenmiştir.

## ⏱️ Olay Zaman Çizelgesi
- **22:10:** v2.4.0 sürümü üretime dağıtıldı (deploy).
- **22:15:** Sentry üzerinde HTTP 500 alarmları tetiklendi.
- **22:25:** Nöbetçi mühendis (On-call) olaya müdahale etti ve rollback kararı aldı.
- **22:50:** Veritabanı geri alma adımı tamamlandı.
- **23:00:** Sistem tamamen sağlıklı duruma döndü.

## 🔍 5 Neden (5 Whys) Analizi
1. **Ödeme servisi neden çöktü?** -> `STRIPE_WEBHOOK_SECRET` değişkeni `undefined` geldi.
2. **Değişken neden eksikti?** -> Prod ortamına değişken elle eklenmemişti.
3. **Neden elle eklenmesi gerekiyordu?** -> Ortam değişkenlerini yöneten merkezi bir Secrets yöneticisi yoktu.
4. **Deploy öncesi neden fark edilmedi?** -> Uygulama ayağa kalkarken değişkenleri kapıda doğrulayan bir kontrol (Zod env check) yoktu.
5. **KÖK NEDEN:** Uygulama eksik konfigürasyonla çalışmaya başlayabilmektedir; 'Fail-Fast' mekanizması eksiktir.

## 🛠️ Düzeltici Eylem Maddeleri (Action Items)
| Görev | Sorumlu | Termin |
| :--- | :--- | :--- |
| `env.mjs` şeması kurularak eksik değişkende derlemenin durdurulması | Can (Backend) | 18 Ekim |
| Staging ortamında deploy öncesi duman testi (smoke test) eklenmesi | Elif (DevOps) | 20 Ekim |
| Müşteri destek ekibine etkilenen kullanıcılara özür kuponu tanımlanması | Zeynep (Ürün) | 16 Ekim |
```

**💡 Kod Analizi:**
Rapor bireyleri suçlamak yerine; eksik konfigürasyonla sunucunun ayağa kalkmasını engelleyen 'Fail-Fast' doğrulama sistemi kurmayı hedefler. Böylece aynı hata gelecekte hiç kimse tarafından tekrarlanamaz.

---

## ⚠️ 5. Junior Tuzakları & Kıdemli Bakış Açısı

- **Tuzak:** Post-Mortem toplantılarında 'Falanca kişi dikkatsiz davrandı' diyerek insanları hedef almak.
  - **Çözüm:** Soruyu her zaman 'Sistemimiz dikkatsizliği neden engellemedi?' şeklinde sorun.
- **Tuzak:** Post-Mortem raporunu yazıp bir dokümana gömmek ve aksiyon maddelerini yapmamak.
  - **Çözüm:** Aksiyon maddelerini hemen Jira biletlerine dönüştürün ve bir sonraki sprinte dahil edin.
- **Tuzak:** Küçük kesintileri 'nasılsa çabuk çözüldü' diyerek belgelendirmemek.
  - **Çözüm:** Her kesintiyi şirketin kurumsal hafızasını güçlendiren bir eğitim vakası olarak kaydedin.

---

## 🎬 6. Udemy Video Dersi Taslağı & Slayt Maddeleri

### 🎥 Ders Başlığı: *Ders 41: Suçsuz Post-Mortem - Hatalardan Kurumsal Bilgelik Üretmek*
- 🖥️ **Slayt 1:** Neden suçlama kültürü şirketleri teknik iflasa sürükler?
- 🖥️ **Slayt 2:** Blameless Post-Mortem ilkeleri ve psikolojik güvenlik.
- 🖥️ **Slayt 3:** 5 Neden (5 Whys) analizi ile kök nedene inmek.
- 🖥️ **Slayt 4:** Örnek Vaka: 45 dakikalık prod kesintisini aksiyon planına dönüştürmek.

**Canlı Kodlama / Ekran Kaydı Senaryosu:**  
Sentry'de patlayan bir hatanın loglarını açın. Yapay zekaya bu logları verip '5 Whys analizi yap ve suçsuz bir Post-Mortem taslağı oluştur' deyin. Çıkan rapordaki aksiyon maddelerini inceleyin.

---

## 🎯 7. Günün Uygulamalı Görevi & Mini Sınav

### 🛠️ Günün Görevi:
Geçmişte projenizde yaşadığınız küçük bir hatayı düşünün. Kendinize '5 Neden' sorusunu sorarak hatanın arkasındaki asıl sistemsel eksikliği bir kağıda yazın.

### 🧠 Bölüm Sonu Kontrol Testi:

**Soru 1:** 'Suçsuz Post-Mortem' (Blameless Post-Mortem) yaklaşımının en temel felsefesi nedir?
  - A) Hata yapan çalışanlara ceza kesilmemesi
  - B) İnsan hatasını kaçınılmaz kabul edip, hataya izin veren sistemik ve mimari süreçleri iyileştirerek aynı sorunun bir daha ASLA yaşanmamasını sağlamak
  - C) Kesintileri müşterilerden gizlemek
  - D) Sadece haftalık toplantı yapmak
> **Doğru Yanıt:** B
> **Açıklama:** Suçsuz kültür, hatayı bireylere yüklemek yerine sistemik korumalar (linter, test, CI/CD) inşa ederek kurumun güvenilirliğini artırır.

**Soru 2:** Bir Post-Mortem raporunda en değerli ve kalıcı bölüm hangisidir?
  - A) Hatanın olduğu günün hava durumu
  - B) Somut sorumluları ve teslim tarihleri belirlenmiş 'Önleyici Eylem Maddeleri' (Action Items)
  - C) Şirket sahibinin imzası
  - D) Hatanın kaç satır sürdüğü
> **Doğru Yanıt:** B
> **Açıklama:** Aksiyon maddeleri olmadan bir post-mortem sadece bir şikayet metnidir. Kalıcı iyileşmeyi sağlayan somut düzeltici görevlerdir.

