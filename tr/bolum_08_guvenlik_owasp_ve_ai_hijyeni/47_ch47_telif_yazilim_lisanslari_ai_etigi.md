# 47. Telif Hakları, Lisanslar ve Kodun Hukuki Güvenliği

**GPL, MIT, Apache Lisansları ve Şirketinizi Davalardan Koruma Rehberi**  
*Bölüm 8 • Zorluk Derecesi: Orta Seviye • Tahmini Okuma Süresi: 12 dk*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Notları
> **Podcast Tartışma Sorusu:**  
> *"Bir açık kaynak projesinden kopyalanan 10 satırlık GPL lisanslı bir kod, şirketinizin tüm ticari kod tabanını açık kaynak yapmaya zorlayabilir mi?"*  
> 
> **Bölümden Çıkarılacak 3 Altın Cümle:**  
> - 📌 Açık kaynak 'sahipsiz' demek değildir; her kütüphanenin yasal bir lisansı ve kullanım şartı vardır.
- 📌 MIT ve Apache 2.0 lisansları son derece esnektir ve ticari yazılımlarda serbestçe kullanılabilir.
- 📌 GPL (Copyleft) lisansı 'bulaşıcıdır' (Viral); ticari kapalı kaynak bir projeye GPL kod dahil edilirse tüm projenin açık kaynak yapılması gerekebilir.

---

## 📖 1. Giriş Hikayesi & Günlük Hayat Analojisi

Bir otomobil fabrikası kurduğunuzu ve milyon dolarlık lüks bir araba ürettiğinizi düşünün.

Motor ustası bir cıvata eksik olunca yan sanayiden bedava bir cıvata bulup takıyor. Fakat o cıvatanın üzerinde küçük bir patent yazısı var: *"Bu parçayı kullanan her araba halka ücretsiz dağıtılmalıdır!"* (GPL Lisansı).

Şirketin avukatları bir gün kapınızı çalar ve der ki: *"O küçük parça yüzünden tüm fabrikanın planlarını ve arabalarımızı ücretsiz vermek zorundayız!"*

Yazılım dünyasında bu felaketi yaşayan dev şirketler oldu! 

Yapay zeka modelleri bazen GPL lisanslı kodları eğitim verisinden hatırlayıp sizin projenize kopyalayabilir. Bir mühendisin görevi, projeye giren her kütüphanenin lisans pasaportunu kontrol etmektir.

---

## 🧠 2. AI Çağında Yeni Zihniyet Modeli

Açık Kaynak Lisans Spektrumu:

```
[İTİBARLI & SERBEST (Permissive)]        [KATILIMCI & KISITLAYICI (Copyleft)]
          MIT / Apache 2.0 / BSD                         GPL v3 / AGPL
                    │                                          │
                    ▼                                          ▼
- Ticari projelerde serbestçe kullanılabilir. - Kodunu değiştirip dağıtırsan,
- Kodunu kapalı tutabilirsin.                 KENDİ KODUNU DA açık kaynak
- Sadece telif bildirimini sakla.             yapmak ZORUNDASIN! ("Bulaşıcı")
```

---

## 🤖 3. AI Prompt Laboratuvarı (Kopyala-Yapıştır Hazır Prompt)

Aşağıdaki prompt şablonunu Cursor, Claude Code, ChatGPT veya Copilot ortamınızda doğrudan kullanabilirsiniz:

```markdown
# ROL: Fikri Mülkiyet ve Yazılım Hukuku Danışmanı
Şirketimiz kapalı kaynak (proprietary) bir ticari SaaS ürünü geliştiriyor.

## GÖREV:
1. MIT, Apache 2.0 ve GPL v3 lisansları arasındaki temel hukuki farkları açıkla.
2. Neden şirket projelerinde GPL v3 lisanslı npm veya pip paketlerinin kullanılmasının riskli olduğunu belirt.
3. CI pipeline'ımızda lisans uyumluluğunu otomatik denetleyen bir araç (`license-checker` veya `fossa`) yapılandırma örneği sun.
```

---

## 💻 4. Kod İncelemesi: Acemi / Halüsinasyon vs. Üretim Kalitesi

#### ❌ Acemi / Kontrolsüz AI Çıktısı (Riskli):
```json
// Lisans Denetimi Yapmayan Şirket:
// Geliştirici bilmeden "gpl-calculator" paketini ekler ve tüm şirket kodu tehlikeye girer!
"dependencies": {
  "super-secret-calculator": "gpl-licensed-package"
}
```

#### ✅ Kıdemli Mühendis Tarafından İyileştirilmiş Sürüm (Güvenli & Temiz):
```json
// CI Pipeline Lisans Denetim Yapılandırması (package.json scripti)
{
  "scripts": {
    "audit:licenses": "npx license-checker --onlyAllow 'MIT;Apache-2.0;BSD-2-Clause;BSD-3-Clause;ISC' --summary"
  }
}

// GitHub Actions Adımı:
// - name: 🛡️ Yasal Lisans Denetimi
//   run: npm run audit:licenses
// Eğer birisi GPL veya AGPL lisanslı paket eklerse CI derlemeyi anında iptal eder!
```

**💡 Kod Analizi:**
`license-checker` aracı ile sadece onaylı izinli lisanslar (`MIT`, `Apache-2.0`, `BSD`) kabul edilir; GPL gibi kapalı kaynak projeyi tehlikeye atacak bir lisans tespit edildiğinde derleme bloke edilir.

---

## ⚠️ 5. Junior Tuzakları & Kıdemli Bakış Açısı

- **Tuzak:** GitHub'da bulduğu her açık kaynak kodu lisansına bakmadan ticari projeye kopyalamak.
  - **Çözüm:** Her kütüphanenin `LICENSE` dosyasını kontrol edin; şüphe durumunda MIT veya Apache tercih edin.
- **Tuzak:** Yapay zekanın ürettiği büyük kod bloklarının telifli kaynaklardan birebir ezberlenmiş (memorized) olabileceğini unutmak.
  - **Çözüm:** AI araçlarında 'public code matching' / 'telemetri eşleme' filtresini daima açık tutun.
- **Tuzak:** AGPL lisanslı bir servisi ağ üzerinden çağırıp lisans şartlarına uymamak.
  - **Çözüm:** AGPL ağ üzerinden kullanımda dahi kaynak kodun açılmasını zorunlu kılar; şirketlerde çok dikkatli kullanılmalıdır.

---

## 🎬 6. Udemy Video Dersi Taslağı & Slayt Maddeleri

### 🎥 Ders Başlığı: *Ders 47: Yazılım Lisansları ve AI Etiği - Şirketi Korumak*
- 🖥️ **Slayt 1:** Açık kaynak lisanslarının anatomisi: Permissive vs Copyleft.
- 🖥️ **Slayt 2:** GPL v3 tuzağı: Şirket kodlarını açık kaynak yapmak zorunda kalmak.
- 🖥️ **Slayt 3:** AI modellerinin telifli kod kopyalama riski ve filtreler.
- 🖥️ **Slayt 4:** Canlı Demo: CI pipeline'ında otomatik lisans denetimi kurmak.

**Canlı Kodlama / Ekran Kaydı Senaryosu:**  
Bir Node projesine `license-checker` kurun. `npm run audit:licenses` çalıştırıp projedeki tüm kütüphanelerin lisans dökümünü ekranda listeleyin. Kasıtlı olarak GPL lisanslı bir paket ekleyip denetimin nasıl hata verdiğini gösterin.

---

## 🎯 7. Günün Uygulamalı Görevi & Mini Sınav

### 🛠️ Günün Görevi:
Projenizdeki `package.json` veya `requirements.txt` dosyalarını açın. Projenizde hangi açık kaynak lisanslarının kullanıldığını bir listeleyici araçla kontrol edin.

### 🧠 Bölüm Sonu Kontrol Testi:

**Soru 1:** Aşağıdaki yazılım lisanslarından hangisi ticari ve kapalı kaynaklı bir projede kodu açma zorunluluğu olmadan en serbestçe kullanılabilir?
  - A) GPL v3
  - B) AGPL v3
  - C) MIT Lisansı
  - D) Lisanssız kodlar
> **Doğru Yanıt:** C
> **Açıklama:** MIT Lisansı, telif bildirimi korunduğu sürece kodun ticari kapalı kaynaklı projelerde serbestçe kullanılmasına, değiştirilmesine ve satılmasına izin verir.

**Soru 2:** GPL lisansının 'Bulaşıcı' (Viral / Copyleft) olarak adlandırılmasının sebebi nedir?
  - A) Bilgisayarlara virüs bulaştırması
  - B) GPL lisanslı bir kod parçasını veya kütüphaneyi kullanan bir yazılımın da zorunlu olarak GPL lisansıyla açık kaynak yapılmasını hukuken şart koşması
  - C) Sadece kış aylarında çalışması
  - D) Kodun silinmesine sebep olması
> **Doğru Yanıt:** B
> **Açıklama:** GPL, kendi kodundan türetilen tüm yazılımların da aynı şekilde özgür ve açık kaynak olmasını şart koşar (Reciprocal / Copyleft).

