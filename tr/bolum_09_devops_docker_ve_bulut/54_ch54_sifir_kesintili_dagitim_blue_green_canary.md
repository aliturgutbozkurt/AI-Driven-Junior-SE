# 54. Sıfır Kesintili Dağıtım (Zero-Downtime Deployment): Blue-Green & Canary

**Cuma Akşamı Bile Korkusuzca Deploy Çıkma Sanatı**  
*Bölüm 9 • Zorluk Derecesi: İleri Seviye • Tahmini Okuma Süresi: 13 dk*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Notları
> **Podcast Tartışma Sorusu:**  
> *"Milyonlarca kullanıcısı olan bir banka veya e-ticaret sitesi yeni versiyon yayınlarken 'Sitemiz bakım nedeniyle kapalıdır' yazısı koyamaz! Sıfır kesinti nasıl sağlanır?"*  
> 
> **Bölümden Çıkarılacak 3 Altın Cümle:**  
> - 📌 Zero-Downtime Deployment, kullanıcılar hiçbir kesinti yaşamadan yeni sürümün yayına alınmasıdır.
- 📌 Blue-Green Dağıtım: Eski sürüm (Blue) ve yeni sürüm (Green) yan yana çalışır; yönlendirici tek bir anahtarla trafiği yeniye aktarır.
- 📌 Canary (Kanarya) Dağıtım: Yeni sürüm önce kullanıcıların sadece %5'ine sunulur; hata yoksa kademeli olarak %100'e çıkarılır.

---

## 📖 1. Giriş Hikayesi & Günlük Hayat Analojisi

Eski zamanlarda kömür madencilerini düşünün.

Madenciler yerin yüzlerce metre altına inerken yanlarında küçük sarı bir kanarya kuşu (Canary) taşırlardı. Kömür madeninde zehirli gaz (karbonmonoksit) sızarsa, kanarya kuşunun bünyesi küçük olduğu için hemen bayılır ve madencileri uyarırdı! Madenciler kuşu görünce hemen maskelerini takar ve canlarını kurtarırdı!

Yazılımda **Canary Deployment** işte o madenci kuşudur!

Yeni bir güncelleme yazdığınızda bunu hemen tüm kullanıcılara açmazsınız. Önce trafiğin sadece %1'ine (kanaryalara) açarsınız. Eğer Sentry'de hata oranı artmazsa güncellemeyi %10, %50 ve %100'e çıkarırsınız. Bir hata olursa sadece o %1 etkilenir ve sistem 3 saniyede eski haline geri döner (Rollback).

---

## 🧠 2. AI Çağında Yeni Zihniyet Modeli

Blue-Green vs Canary Dağıtım Mimarisi:

```
BLUE-GREEN DAĞITIM:
[Yük Dengeleyici (Router)]
         │
         ├──(Trafik: %100)──> [BLUE: Mevcut Sürüm v1.0] (Canlıda)
         │
         └──(Trafik: %0)────> [GREEN: Yeni Sürüm v2.0] (Test Ediliyor)
[Geçiş Anı: Router yönü değiştirir; Green %100 olur, Blue yedekte bekler!]

──────────────────────────────────────────────────────────────────────────
CANARY DAĞITIM:
[Yük Dengeleyici]
         │
         ├──(Trafik: %95)───> [STABLE: Mevcut Sürüm v1.0]
         │
         └──(Trafik: %5)────> [CANARY: Yeni Sürüm v2.0] (Gözlemleniyor)
```

---

## 🤖 3. AI Prompt Laboratuvarı (Kopyala-Yapıştır Hazır Prompt)

Aşağıdaki prompt şablonunu Cursor, Claude Code, ChatGPT veya Copilot ortamınızda doğrudan kullanabilirsiniz:

```markdown
# ROL: SRE ve Sürüm Dağıtım Yöneticisi
Üretim ortamımızda sıfır kesintili (Zero-Downtime) bir Canary dağıtım stratejisi kurgulayacağız.

## GÖREV:
1. Blue-Green ile Canary dağıtım arasındaki mimari ve maliyet farklarını karşılaştır.
2. Otomatik geri alma (Automated Rollback) tetikleyicisi olan bir senaryoyu tasarla (Örn: HTTP 500 oranı %1'i geçerse anında eski sürüme dön).
3. Veritabanı şema güncellemelerinde (Migrations) sıfır kesinti sağlamak için 'Expand and Contract' desenini açıkla.
```

---

## 💻 4. Kod İncelemesi: Acemi / Halüsinasyon vs. Üretim Kalitesi

#### ❌ Acemi / Kontrolsüz AI Çıktısı (Riskli):
```yaml
# Kötü Dağıtım: Rolling update veya anında kapatıp açma (Kesinti yaşanır!)
# Eski sunucu kapanır, yenisi 45 saniyede ayağa kalkarken gelen kullanıcılar 502 Bad Gateway alır!
```

#### ✅ Kıdemli Mühendis Tarafından İyileştirilmiş Sürüm (Güvenli & Temiz):
```yaml
# Kubernetes / Cloud Canary Dağıtım Yapılandırması (Canary Rollout)
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: api-service
spec:
  replicas: 10
  strategy:
    canary:
      # Kademeli Trafik Dağıtımı
      steps:
        - setWeight: 5    # 1. Adım: Sadece %5 trafik yönlendir
        - pause: { duration: 10m } # 10 dakika boyunca Sentry / Prometheus izle!
        - setWeight: 20   # 2. Adım: %20'ye çıkar
        - pause: { duration: 10m }
        - setWeight: 50   # 3. Adım: %50'ye çıkar
        - pause: { duration: 5m }
      
      # Otomatik Geri Alma (Automated Rollback Kuralı)
      analysis:
        templates:
          - templateName: error-rate-check
        args:
          - name: max-error-rate
            value: "0.01" # Hata oranı %1'i geçerse ANINDA ESKİYE DÖN!
```

**💡 Kod Analizi:**
`Argo Rollouts` kullanılarak trafik önce %5'e verilir ve Prometheus metrikleri incelenir. Hata oranı %1'i aşarsa sistem insan müdahalesine gerek kalmadan milisaniyeler içinde eski sürüme geri döner.

---

## ⚠️ 5. Junior Tuzakları & Kıdemli Bakış Açısı

- **Tuzak:** Veritabanında kolon silip eski sürümün çökmesine yol açmak (Breaking Migration).
  - **Çözüm:** Expand-Contract desenini uygulayın: Önce yeni kolonu ekleyin, iki sürümü de destekleyin, eski kolonu en son silin.
- **Tuzak:** Rollback (Geri alma) stratejisini önceden test etmeyip kriz anında paniklemek.
  - **Çözüm:** Her deploy öncesi tek tuşla geri alma planınızın çalıştığından emin olun.
- **Tuzak:** Canary dağıtımda logları ve metrikleri izlemeden trafiği hemen %100'e çekmek.
  - **Çözüm:** Her kademede en az 5-10 dakika metriklerin oturmasını bekleyin.

---

## 🎬 6. Udemy Video Dersi Taslağı & Slayt Maddeleri

### 🎥 Ders Başlığı: *Ders 54: Sıfır Kesintili Dağıtım - Blue-Green ve Canary Stratejileri*
- 🖥️ **Slayt 1:** Neden 'Sitemiz bakımda' dönemi tarihe karıştı?
- 🖥️ **Slayt 2:** Blue-Green Dağıtım: Anında anahtarlama ve yedekleme.
- 🖥️ **Slayt 3:** Canary Dağıtım: Madenci kanaryası gibi hata avlamak.
- 🖥️ **Slayt 4:** Bölüm 9 Özeti: DevOps, Konteynerler ve Bulut Mimarisi.

**Canlı Kodlama / Ekran Kaydı Senaryosu:**  
Yerel Kubernetes (Minikube) veya Docker üzerinde iki versiyon ayağa kaldırın. Bir yük dengeleyici üzerinden gelen 100 isteğin 95'inin v1'e, 5'inin v2'ye gittiğini canlı log akışında kanıtlayın.

---

## 🎯 7. Günün Uygulamalı Görevi & Mini Sınav

### 🛠️ Günün Görevi:
Projenizin deployment sürecini inceleyin. Bir hata olduğunda eski sürüme dönmenin (Rollback) kaç dakika sürdüğünü ve bu sürecin otomatikleştirilip otomatikleştirilemeyeceğini analiz edin.

### 🧠 Bölüm Sonu Kontrol Testi:

**Soru 1:** Canary (Kanarya) Dağıtım stratejisinin birincil amacı nedir?
  - A) Kuş resimleri göstermek
  - B) Yeni yazılım sürümünü tüm kullanıcılara açmadan önce küçük bir kullanıcı grubuna (%1-%5) sunarak, olası hataların tüm sistemi çökertmesini engellemek ve riski minimize etmek
  - C) Sadece gece yarısı güncelleme yapmak
  - D) Sunucu masraflarını iki katına çıkarmak
> **Doğru Yanıt:** B
> **Açıklama:** Canary dağıtım, yeni sürümü küçük bir kullanıcı grubunda test eder; bir hata varsa sadece o küçük grup etkilenir ve sistem anında eski sürüme geri döner.

**Soru 2:** Veritabanı şemasında sıfır kesintili (Zero-Downtime) değişiklik yapmayı sağlayan mimari desene ne ad verilir?
  - A) Kapat-Aç Deseni
  - B) Expand and Contract (Genişlet ve Daralt) Deseni
  - C) SQL Silme Deseni
  - D) Rastgele Güncelleme
> **Doğru Yanıt:** B
> **Açıklama:** Expand and Contract deseni, önce yeni yapıyı ekleyip hem eski hem yeni kodu destekler (Expand), ardından eski kodu ve alanı temizler (Contract); böylece kesinti yaşanmaz.

