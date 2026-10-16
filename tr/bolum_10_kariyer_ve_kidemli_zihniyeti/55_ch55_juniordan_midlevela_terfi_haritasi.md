# 55. Junior'dan Mid-Level'a Geçişin Haritası: Hangi Metriklerle Ölçülürsün?

**Sürekli Yardım İsteyen Geliştiriciden Bağımsız Çözüm Üreten Mühendise Dönüşmek**  
*Bölüm 10 • Zorluk Derecesi: İleri Seviye • Tahmini Okuma Süresi: 12 dk*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Notları
> **Podcast Tartışma Sorusu:**  
> *"Bir yazılımcının unvanını 'Junior'dan 'Mid-Level'a taşıyan şey yazdığı kod satırı sayısı mıdır, yoksa aldığı sorumluluğun ve özerkliğin (autonomy) seviyesi midir?"*  
> 
> **Bölümden Çıkarılacak 3 Altın Cümle:**  
> - 📌 Junior adım adım yönlendirme (hand-holding) bekler; Mid-Level belirsiz bir problemi alıp bağımsız çözer.
- 📌 Terfi etmenin en hızlı yolu, sadece kodu değil; testini, dokümantasyonunu ve deployment'ını sahiplenmektir (End-to-End Ownership).
- 📌 Senior mühendisin vaktini koruyan junior, ekipteki en değerli junior'dır.

---

## 📖 1. Giriş Hikayesi & Günlük Hayat Analojisi

İki marangoz çırağını hayal edin:

**Çırak Can:** Ustanın yanına her 5 dakikada bir gelir:
- *"Usta bu tahtayı hangi testereyle keseyim?"*
- *"Usta bu vidayı nereye sıkayım?"*
- *"Usta cetveli bulamadım, ne yapayım?"*
Usta iş yapamaz hale gelir, akşama kadar Can'ı yönetir!

**Çırak Elif:** Usta sabah gelir ve der ki: *"Bize bu odaya sığacak bir kitaplık lazım."*
Elif odayı ölçer, taslağı çizer, tahtaları keser, monte eder ve akşam ustaya bitmiş kitaplığı sunar: *"Usta kitaplığı yaptım, sağlamlığını test ettim, verniğini attım. İncelemek ister misin?"*

Usta Elif'e bakar ve der ki: *"Sen artık çırak değilsin, sen artık bir kalfasın (Mid-Level)!"*

Yazılımda da terfi formülü budur: Soru sormak ayıp değildir; ama ödevini yapıp çözümlerle gelen mühendis ışık hızında yükselir.

---

## 🧠 2. AI Çağında Yeni Zihniyet Modeli

Mühendislik Seviyeleri ve Sorumluluk Matrisi:

| Seviye | Problem Tanımı | Çözüm Yolu | Beklenen Çıktı |
| :--- | :--- | :--- | :--- |
| **Junior** | Çok net, küçük bilet (Örn: "Butonun rengini mavi yap") | Senior yönlendirmesiyle adım adım | Çalışan temiz kod |
| **Mid-Level** | Orta belirsizlik (Örn: "Kupon doğrulama servisini yaz") | Bağımsız mimari araştırma + AI ile çözüm | Test edilmiş, deploy edilmiş servis |
| **Senior** | Yüksek belirsizlik (Örn: "Ödeme altyapısını ölçeklendir") | Stratejik mimari karar, risk yönetimi | Takımın yönü ve sistem dayanıklılığı |

---

## 🤖 3. AI Prompt Laboratuvarı (Kopyala-Yapıştır Hazır Prompt)

Aşağıdaki prompt şablonunu Cursor, Claude Code, ChatGPT veya Copilot ortamınızda doğrudan kullanabilirsiniz:

```markdown
# ROL: Mühendislik Direktörü ve Kariyer Mentoru
Ben bir teknoloji şirketinde 1 yıldır çalışan ve Mid-Level seviyesine terfi etmek isteyen bir Junior mühendisim.

## GÖREV:
1. Bir sonraki 6 ay içinde Mid-Level seviyesine çıkmamı sağlayacak 4 temel somut yetkinliği listele (Bağımsızlık, Test Kalitesi, İletişim, Hata Çözme).
2. Senior mühendislere soru sorarken 'Senior Vaktini Koruyan Soru Sorma Şablonu'nu hazırla.
3. Yönetici ile yapacağım 1-on-1 toplantısında terfi beklentimi profesyonelce konuşma senaryosu sun.
```

---

## 💻 4. Kod İncelemesi: Acemi / Halüsinasyon vs. Üretim Kalitesi

#### ❌ Acemi / Kontrolsüz AI Çıktısı (Riskli):
```markdown
# Kötü Soru Sorma Şekli (Senior'ı Tüketen):
"Selam abi, benim kod hata veriyor baksana bi." 
```

#### ✅ Kıdemli Mühendis Tarafından İyileştirilmiş Sürüm (Güvenli & Temiz):
```markdown
# Profesyonel ve Senior Vaktini Koruyan Soru Sorma Şablonu:

"Selam Can, [Jira-405] biletinde ödeme webhook'unu test ederken bir sorunla karşılaştım.

1. **GÖZLEM:** Stripe'tan gelen webhook'ta imza doğrulaması başarısız oluyor (`SignatureVerificationError`).
2. **DENEDİKLERİM:**
   - Ham body'nin (`rawBody`) bozulup bozulmadığını kontrol ettim.
   - Webhook secret anahtarının doğruluğunu test ettim.
   - Sentry loglarında gelen header'ı inceledim.
3. **HİPOTEZİM:** Express'teki `bodyParser.json()` middleware'i raw body buffer'ını parse ettiği için imza eşleşmiyor olabilir.
4. **SORUM:** Daha önce bu projede webhook rotası için `bodyParser.raw()` muafiyeti uygulanmış bir örnek var mı, nereden bakmamı önerirsin?" 
```

**💡 Kod Analizi:**
Bu şablon sayesinde senior mühendis sorunu 30 saniyede anlar; junior'ın çaba gösterdiğini ve hipotez kurduğunu görerek büyük saygı duyar.

---

## ⚠️ 5. Junior Tuzakları & Kıdemli Bakış Açısı

- **Tuzak:** Takıldığı an hiçbir araştırma yapmadan anında senior'ın masasına koşmak.
  - **Çözüm:** Soruyu sormadan önce en az 20 dakika AI ve dökümantasyon ile araştırma yapıp hipotezlerinizi listeleyin.
- **Tuzak:** Haftalarca sessizce takılıp kalıp (stuck) kimseye hiçbir şey söylememek.
  - **Çözüm:** Eğer bir problemde 45 dakika boyunca hiçbir ilerleme kaydedemediyseniz profesyonelce yardım isteyin.
- **Tuzak:** Sadece kendisine verilen görevi yapıp sistemin bütünüyle ilgilenmemek.
  - **Çözüm:** Deploy süreçlerini, logları ve müşteri geri bildirimlerini merak edip takip edin.

---

## 🎬 6. Udemy Video Dersi Taslağı & Slayt Maddeleri

### 🎥 Ders Başlığı: *Ders 55: Junior'dan Mid-Level'a Terfi - Özerklik ve Sahiplik*
- 🖥️ **Slayt 1:** Junior vs Mid-Level: Kod yazma hızından bağımsızlık seviyesine.
- 🖥️ **Slayt 2:** Senior vaktini koruyan soru sorma sanatı.
- 🖥️ **Slayt 3:** Uçtan uca sahiplik (End-to-End Ownership) felsefesi.
- 🖥️ **Slayt 4:** 1-on-1 toplantılarında terfi beklentisini yönetmek.

**Canlı Kodlama / Ekran Kaydı Senaryosu:**  
Bir slack mesajı simülasyonu yapın. Kötü ve tembel bir soru ile profesyonel '4 Adımlı Soru Şablonu'nu yan yana koyarak senior mühendislerin verdiği tepkiyi ve kazanılan saygıyı tartışın.

---

## 🎯 7. Günün Uygulamalı Görevi & Mini Sınav

### 🛠️ Günün Görevi:
Takıldığınız bir sonraki teknik problemde 'Senior Vaktini Koruyan Soru Şablonu'nu kullanarak mesajınızı hazırlayın ve öyle yardım isteyin.

### 🧠 Bölüm Sonu Kontrol Testi:

**Soru 1:** Bir yazılım mühendisinin 'Mid-Level' seviyesine ulaştığını gösteren en belirgin performans sinyali nedir?
  - A) Günde 2000 satır kod yazması
  - B) Kendisine verilen orta karmaşıklıktaki bir görevi, sürekli yönlendirmeye ihtiyaç duymadan mimari araştırmasını yaparak, testlerini yazarak ve uçtan uca sahiplenerek bağımsız (autonomous) çözebilmesi
  - C) Şirketin en eski çalışanı olması
  - D) Klavyeye bakmadan yazabilmesi
> **Doğru Yanıt:** B
> **Açıklama:** Mid-level seviyesinin temel tanımı 'Özerklik'tir (Autonomy). Sürekli yönlendirme gerektirmeden işi teslim edebilen mühendis artık junior değildir.

**Soru 2:** Kıdemli bir mühendise soru sorarken yapılması gereken en profesyonel davranış nedir?
  - A) Sadece 'kod çalışmıyor' yazıp beklemek
  - B) Sorunu özetlemek, neleri denediğini belirtmek, kendi hipotezini sunmak ve spesifik bir konuda görüş istemek
  - C) Soru sormaktan tamamen vazgeçip işi bırakmak
  - D) Gece yarısı aramak
> **Doğru Yanıt:** B
> **Açıklama:** Ödevini yapmış, denediği yolları ve hipotezini sunan geliştirici hem senior'ın vaktini korur hem de profesyonel olgunluğunu kanıtlar.

