# 6. Geliştirme Ortamını (IDE) Turbo Şarj Etmek: Cursor Rules ve Kısayollar

**Her Seferinde Aynı Şeyleri Tekrarlamaktan Kurtulun**  
*Bölüm 1 • Zorluk Derecesi: Başlangıç Seviyesi • Tahmini Okuma Süresi: 13 dk*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Notları
> **Podcast Tartışma Sorusu:**  
> *"Bir projede `.cursorrules` dosyası kullanmak ile kullanmamak arasındaki fark, junior bir mühendisin günlük üretkenliğini 2 kat artırabilir mi?"*  
> 
> **Bölümden Çıkarılacak 3 Altın Cümle:**  
> - 📌 Cursor Rules (.cursorrules), takım standartlarınızı ve mimari kurallarınızı yapay zekanın kalıcı hafızasına kazır.
- 📌 Her prompta 'Türkçe yaz, Tailwind kullan, test ekle' demek yerine bu kuralları otomatikleştirin.
- 📌 Klavye kısayolları (Cmd+K, Cmd+L, Cmd+I) refleks haline geldiğinde kod yazma hızınız düşünme hızınıza yaklaşır.

---

## 📖 1. Giriş Hikayesi & Günlük Hayat Analojisi

Her sabah kahve almaya gittiğiniz kafeyi hayal edin. Her gün baristaya: *"Benim adım Ali, laktozsuz sütlü, tek shot espressolu, kağıt bardakta bir latte istiyorum"* demek mi daha verimli; yoksa baristanın sizi gördüğü an: *"Ali Bey, her zamankinden mi?"* deyip 30 saniyede kahvenizi vermesi mi?

`.cursorrules` veya IDE kural dosyaları işte o baristadır! 

Projenizin kök dizinine koyacağınız küçük bir metin dosyası, yapay zekaya sizin kim olduğunuzu, projenin hangi dille yazıldığını, hangi mimari kalıpları kullandığınızı ve nelere ASLA izin vermediğinizi her saniye fısıldar.

---

## 🧠 2. AI Çağında Yeni Zihniyet Modeli

İdeal Bir `.cursorrules` Dosyası Anatomisi:

```markdown
# 1. Proje Kimliği ve Teknoloji Yığını (Stack)
- Next.js 14 (App Router), TypeScript Strict Mode, TailwindCSS.

# 2. Mimari Kurallar
- Asla 'any' kullanma; daima tam tip tanımla.
- React Server Component (RSC) varsayılandır; 'use client' sadece gerekli yerlerde.

# 3. Test ve Doğrulama
- Her yeni servis fonksiyonu için aynı isimde `.test.ts` dosyası üret.

# 4. Stil ve Format
- Erken dönüş (Early Return) desenini uygula.
- İç içe geçmiş if-else bloklarından kaçın.
```

---

## 🤖 3. AI Prompt Laboratuvarı (Kopyala-Yapıştır Hazır Prompt)

Aşağıdaki prompt şablonunu Cursor, Claude Code, ChatGPT veya Copilot ortamınızda doğrudan kullanabilirsiniz:

```markdown
# GÖREV: Projemiz İçin Özel .cursorrules Dosyası Oluştur
Yeni bir Full-Stack projeye başlıyoruz.
Teknoloji Yığını:
- FastAPI (Python 3.12)
- Pydantic V2
- SQLAlchemy 2.0 (Async)
- PostgreSQL
- PyTest

Lütfen bu proje için AI'ın her zaman uyması gereken 5 maddelik katı bir `.cursorrules` içeriği hazırla.
Özellikle tip güvenliğine, async/await standartlarına ve test yazımına odaklansın.
```

---

## 💻 4. Kod İncelemesi: Acemi / Halüsinasyon vs. Üretim Kalitesi

#### ❌ Acemi / Kontrolsüz AI Çıktısı (Riskli):
```markdown
# Kötü .cursorrules: Çok uzun, laf kalabalığı dolu ve kural içermeyen metin
Sen harika bir yardımcısın. Benim için en iyi python kodlarını yaz.
Lütfen hata yapma ve her zaman nazik ol. Kodların çok temiz olsun.
```

#### ✅ Kıdemli Mühendis Tarafından İyileştirilmiş Sürüm (Güvenli & Temiz):
```markdown
# PROJE KURALLARI (.cursorrules)
## TEKNOLOJİ YIĞINI:
- Python 3.12, FastAPI, Pydantic v2, SQLAlchemy 2.0 (Async).

## KODLAMA STANDARTLARI:
1. TIP GÜVENLİĞİ: Tüm fonksiyonlarda type hints zorunludur. 'Any' yasaktır.
2. VERİTABANI: Asla senkron sorgu yazma; daima `await session.execute(...)` kullan.
3. MODELLER: Giriş/Çıkış için daima Pydantic şemalarını SQLAlchemy modellerinden ayır.
4. HATA YÖNETİMİ: HTTPException fırlatırken daima standart JSON hata yapısı kullan.
5. TESTLER: Her endpoint için en az 1 başarı ve 2 hata durumunu kapsayan pytest fonksiyonu yaz.
```

**💡 Kod Analizi:**
Etkili kural dosyaları doğrudan emir kipleriyle, net yasaklarla ve teknoloji sürümleriyle yazılır. Model bu kuralları her işlemde 'Sistem Mesajı' olarak okur.

---

## ⚠️ 5. Junior Tuzakları & Kıdemli Bakış Açısı

- **Tuzak:** Kural dosyasına 50 sayfa dokümantasyon yapıştırıp context penceresini şişirmek.
  - **Çözüm:** Kuralları 30-50 satır arasında, madde madde ve öz tutun.
- **Tuzak:** Kural dosyasını yazıp git'e eklememek.
  - **Çözüm:** `.cursorrules` dosyasını depoya commit edin, böylece tüm ekip arkadaşlarınız aynı AI davranışından faydalansın.
- **Tuzak:** Kısayolları öğrenmeyip her şeyi fareyle tıklayarak yapmak.
  - **Çözüm:** Günde en az 30 dakika farenizi bir kenara bırakıp IDE kısayollarını zorlayın.

---

## 🎬 6. Udemy Video Dersi Taslağı & Slayt Maddeleri

### 🎥 Ders Başlığı: *Ders 6: IDE'nizi Kişiselleştirmek - .cursorrules ile Takım Standartları*
- 🖥️ **Slayt 1:** .cursorrules dosyası nedir ve nasıl çalışır?
- 🖥️ **Slayt 2:** Kalıcı bağlam oluşturmanın faydaları.
- 🖥️ **Slayt 3:** En kritik IDE kısayolları ve geliştirici iş akışı.
- 🖥️ **Slayt 4:** Bölüm 1 Özeti: AI Çağında Yeni Nesil Yazılımcının Zihniyet Dönüşümü.

**Canlı Kodlama / Ekran Kaydı Senaryosu:**  
Proje kökünde `.cursorrules` oluşturun. 'Tüm fonksiyonlar Türkçe açıklama içermelidir ve TypeScript strict olmalıdır' kuralını yazın. Ardından basit bir fonksiyon isteyerek kuralın anında uygulandığını gösterin.

---

## 🎯 7. Günün Uygulamalı Görevi & Mini Sınav

### 🛠️ Günün Görevi:
Bugün çalıştığınız projenin kök dizininde bir `.cursorrules` dosyası oluşturun ve projenizde uyulması gereken en önemli 3 mimari kuralı içine yazın.

### 🧠 Bölüm Sonu Kontrol Testi:

**Soru 1:** Proje kök dizinindeki `.cursorrules` dosyasının temel işlevi nedir?
  - A) Bilgisayara yeni RAM taktırmak
  - B) Projedeki her AI etkileşimine otomatik olarak mimari kuralları ve kodlama standartlarını sistem bağlamı olarak eklemek
  - C) Sadece git commitlerini silmek
  - D) CSS dosyalarını sıkıştırmak
> **Doğru Yanıt:** B
> **Açıklama:** Kural dosyaları, geliştiricinin her promptta aynı kuralları tekrarlamasına gerek kalmadan yapay zekayı proje standartlarına bağlı tutar.

**Soru 2:** Cursor IDE'sinde dosya içinde doğrudan kod düzenleme penceresini açan temel kısayol hangisidir?
  - A) Ctrl + Alt + Del
  - B) Cmd + K (Windows'ta Ctrl + K)
  - C) F5
  - D) Shift + Escape
> **Doğru Yanıt:** B
> **Açıklama:** Cmd+K (veya Ctrl+K) editörde seçili kod üzerinde doğrudan satır içi düzenleme yapmayı sağlayan en yaygın AI kısayoludur.

