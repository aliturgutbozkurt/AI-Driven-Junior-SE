# 15. Kusursuz Pull Request (PR) Yazma Sanatı: AI ile PR Açıklamaları

**Senior Mühendislerin İlk Bakışta Onaylayacağı (LGTM) PR'lar Hazırlamak**  
*Bölüm 3 • Zorluk Derecesi: Orta Seviye • Tahmini Okuma Süresi: 12 dk*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Notları
> **Podcast Tartışma Sorusu:**  
> *"Senior mühendisler neden boş veya 'değişiklikler yapıldı' yazan PR'ları görmekten nefret eder ve AI ile nasıl kusursuz bir PR şablonu doldurulur?"*  
> 
> **Bölümden Çıkarılacak 3 Altın Cümle:**  
> - 📌 Bir Pull Request sadece kod değişikliği değil; takım arkadaşlarınıza yaptığınız bir satış sunumudur.
- 📌 İyi bir PR: 'Neyi değiştirdim?', 'Neden değiştirdim?' ve 'Nasıl test ettim?' sorularına eksiksiz yanıt verir.
- 📌 AI CLI araçları veya GitHub Actions, git diff'ini okuyarak ekran görüntüleri hariç PR açıklamasını saniyeler içinde taslaklaştırabilir.

---

## 📖 1. Giriş Hikayesi & Günlük Hayat Analojisi

Bir restorana gittiğinizi ve garsonun masanıza kapağı kapalı, dumanlar tüten bir tabak bırakıp tek kelime etmeden gittiğini düşünün. İçinde ne olduğunu, alerjen içerip içermediğini, et mi sebze mi olduğunu bilmiyorsunuz. O yemeği hemen yer misiniz? Asla!

Açıklaması boş bırakılmış veya *"bug fix"* yazılmış bir Pull Request de o kapalı tabaktır. Kıdemli mühendis o PR'ı incelemek için saatlerce kodun içine dalıp *"Bu çocuk burada ne yapmaya çalışmış?"* diye dedektiflik yapmak zorunda kalır.

Oysa tabağı açıp: *"Şefimizin özel mantarlı risotto yemeği, glütensizdir ve fırında 20 dakika pişti"* diyen bir garson güven verir.

Kusursuz bir PR açıklaması, kıdemli mühendise *"Gözüm kapalı onaylayabilirim (LGTM)"* dedirten en büyük profesyonellik göstergesidir.

---

## 🧠 2. AI Çağında Yeni Zihniyet Modeli

Altın Standart PR Şablonu:

```markdown
## 🎯 Amaç & Çözülen Problem
- [Jira-123]: Kullanıcı şifre sıfırlama akışında yaşanan zaman aşımı hatası giderildi.

## 🛠️ Yapılan Değişiklikler
- `authService.ts`: Token geçerlilik süresi 15 dakikadan 30 dakikaya çıkarıldı.
- `mailer.ts`: Şifre sıfırlama e-postasına yeni şablon entegre edildi.

## 🧪 Nasıl Test Edildi?
- [x] Unit testler çalıştırıldı (`npm run test:auth`).
- [x] Yerel ortamda MailHog ile sahte e-posta gönderimi doğrulandı.

## 📸 Ekran Görüntüleri / Kanıt (UI Değişiklikleri İçin)
[Ekran Görüntüsü / GIF]
```

---

## 🤖 3. AI Prompt Laboratuvarı (Kopyala-Yapıştır Hazır Prompt)

Aşağıdaki prompt şablonunu Cursor, Claude Code, ChatGPT veya Copilot ortamınızda doğrudan kullanabilirsiniz:

```markdown
# ROL: Kıdemli Yazılım Ekip Lideri
Aşağıdaki `git diff --stat` ve kod değişikliklerimi incele.

## DEĞİŞİKLİK ÖZETİ:
- `src/controllers/payment.ts`: İki adımlı ödeme doğrulama eklendi.
- `src/services/stripe.ts`: Webhook imza kontrolü eklendi.
- `tests/payment.test.ts`: 4 yeni unit test eklendi.

## GÖREV:
GitHub için profesyonel, markdown formatında eksiksiz bir Pull Request (PR) açıklaması hazırla.
İçinde:
1. Problem tanımı
2. Teknik çözüm özeti
3. Test adımları kontrol listesi (checkbox)
4. Güvenlik notu
bulunsun.
```

---

## 💻 4. Kod İncelemesi: Acemi / Halüsinasyon vs. Üretim Kalitesi

#### ❌ Acemi / Kontrolsüz AI Çıktısı (Riskli):
```markdown
# Kötü PR Açıklaması:
odeme duzeltildi testler geciyor
```

#### ✅ Kıdemli Mühendis Tarafından İyileştirilmiş Sürüm (Güvenli & Temiz):
```markdown
## 🎯 Problem & Çözüm Özeti
Stripe üzerinden gelen mükerrer webhook bildirimleri nedeniyle bazı kullanıcıların kartından iki kez para çekilme riski bulunuyordu. 

Bu PR ile **Idempotency Key (Tekillik Anahtarı)** deseni uygulanmış ve webhook istekleri için HMAC imza doğrulaması zorunlu kılınmıştır.

## 🛠️ Değişiklik Maddeleri
- `payment.ts`: İşlem öncesinde Redis üzerinden `idempotencyKey` varlığı sorgulanır.
- `stripe.ts`: `stripe.webhooks.constructEvent` kullanılarak sahte bildirimler engellenir.
- `payment.test.ts`: Aynı payload iki kez gönderildiğinde ikincisinin engellendiği test edildi.

## 🧪 Test Kontrol Listesi
- [x] Tüm unit testler başarıyla geçti (`npm test`).
- [x] Stripe CLI ile yerel ortamda webhook tetiklendi (`stripe trigger payment_intent.succeeded`).
- [x] Kötü niyetli (imzasız) isteklerin 400 Bad Request aldığı doğrulandı.

## 🔒 Güvenlik Notu
Yeni bir kütüphane eklenmemiştir; Stripe SDK'nın yerel doğrulama metodu kullanılmıştır.
```

**💡 Kod Analizi:**
Bu derece ayrıntılı bir PR açıklaması gören bir tech lead, kod tabanına güven duyar ve gereksiz soru-cevap turlarına girmeden onay verir.

---

## ⚠️ 5. Junior Tuzakları & Kıdemli Bakış Açısı

- **Tuzak:** 1000'den fazla satır içeren devasa ('canavar') PR'lar açmak.
  - **Çözüm:** Bir PR'ın maksimum 200-400 satır arasında kalmasına özen gösterin; büyük işleri küçük parçalara bölün.
- **Tuzak:** Test sonuçlarını veya ekran görüntülerini PR'a eklememek.
  - **Çözüm:** Özellikle frontend değişikliklerinde öncesi/sonrası ekran görüntüsü ekleyin.
- **Tuzak:** PR açtıktan sonra CI/CD boru hattının (GitHub Actions) kırmızı yandığını fark etmemek.
  - **Çözüm:** PR açtıktan sonra en az 3 dakika testlerin yeşile dönmesini ekrandan takip edin.

---

## 🎬 6. Udemy Video Dersi Taslağı & Slayt Maddeleri

### 🎥 Ders Başlığı: *Ders 15: Kusursuz Pull Request - Senior'ların Güvenini Kazanmak*
- 🖥️ **Slayt 1:** PR nedir? Bir kod değişikliğinden öte bir iletişim aracı.
- 🖥️ **Slayt 2:** Altın Standart PR şablonunun bileşenleri.
- 🖥️ **Slayt 3:** AI ile git diff'inden otomatik PR açıklaması üretmek.
- 🖥️ **Slayt 4:** Büyük PR'ları küçük parçalara bölme stratejisi.

**Canlı Kodlama / Ekran Kaydı Senaryosu:**  
GitHub üzerinde yeni bir PR açma ekranını gösterin. Terminaldeki diff'i AI'a kopyalayıp 15 saniyede markdown PR metni ürettirin. PR açıklamasına yapıştırıp önizlemesini gösterin.

---

## 🎯 7. Günün Uygulamalı Görevi & Mini Sınav

### 🛠️ Günün Görevi:
Açacağınız bir sonraki PR'da 'Altın Standart PR Şablonu'nu kullanın ve en az bir test ekran görüntüsü veya terminal test çıktısı ekleyin.

### 🧠 Bölüm Sonu Kontrol Testi:

**Soru 1:** Bir Pull Request açılırken kıdemli bir mühendisin en çok görmek istediği bilgi hangisidir?
  - A) Geliştiricinin en sevdiği müzik
  - B) Değişikliğin neden yapıldığı (problem tanımı) ve nasıl test edildiğinin kanıtı
  - C) PR'ın kaç dakikada yazıldığı
  - D) Bilgisayarın işlemci markası
> **Doğru Yanıt:** B
> **Açıklama:** Kıdemli mühendis kodun ne olduğunu diff'te görür; ancak 'neden' yapıldığını ve güvenilirliğini ancak PR açıklamasından ve test kanıtlarından anlar.

**Soru 2:** Bir Pull Request'in ideal büyüklüğü (satır sayısı) ne kadar olmalıdır?
  - A) En az 5.000 satır
  - B) 10.000 satır
  - C) 200 - 400 satır arası odaklanmış küçük parçalar
  - D) Sadece 1 karakter
> **Doğru Yanıt:** C
> **Açıklama:** Araştırmalar, 400 satırdan büyük PR'larda inceleme kalitesinin dramatik şekilde düştüğünü ve hataların gözden kaçtığını göstermektedir.

