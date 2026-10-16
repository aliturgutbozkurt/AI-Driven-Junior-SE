# 1. İlk Gün Heyecanı: 'Yazılımcılık Bitti mi?' Mitini Yıkmak

**Kod Yazmanın Değil, Problem Çözmenin Yeni Altın Çağı**  
*Bölüm 1 • Zorluk Derecesi: Başlangıç Seviyesi • Tahmini Okuma Süresi: 11 dk*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Notları
> **Podcast Tartışma Sorusu:**  
> *"Yapay zeka tüm kodları birkaç saniyede yazabiliyorsa, bir şirketin yeni mezun veya junior bir yazılımcıya maaş ödemesi için mantıklı tek bir sebep kaldı mı?"*  
> 
> **Bölümden Çıkarılacak 3 Altın Cümle:**  
> - 📌 Yapay zeka yazılımcılığı öldürmedi; söz dizimi (syntax) ezberciliğini öldürüp mimari düşünceyi öne çıkardı.
- 📌 Junior mühendis artık 'klavye amelesi' değil, yapay zeka stajyerlerini yöneten bir orkestra şefidir.
- 📌 Değeriniz yazdığınız kod satır sayısıyla değil, doğruluğunu garanti ettiğiniz sistemlerle ölçülür.

---

## 📖 1. Giriş Hikayesi & Günlük Hayat Analojisi

Ofise veya uzaktan çalışma masanıza oturduğunuz o ilk günü hayal edin. Ekranda yanıp sönen imleç ve kulağınızda sosyal medyanın uğultusu: *"Yapay zeka varken artık junior'lara gerek yok!"* 

Bir an durup aşçılık tarihine bakalım. Mikserler, akıllı fırınlar ve otomatik hamur yoğurma makineleri icat edildiğinde şefler yok oldu mu? Tam aksine! Önceden saatlerce yumurta çırpmak zorunda kalan çıraklar, artık lezzet dengesine, sunuma ve menü tasarımına odaklanmaya başladı. 

Yazılımda da tam olarak bu devrim yaşanıyor. Eskiden günlerce 'for döngüsü' veya karmaşık CSS hizalamasıyla boğuşan junior, bugün dakikalar içinde prototip çıkarıp işin mantığına, güvenliğine ve kullanıcı deneyimine kafa yorabiliyor. Korku duymak yerine fırının kontrol düğmelerini elinize almanın zamanı geldi.

---

## 🧠 2. AI Çağında Yeni Zihniyet Modeli

Geleneksel yazılımcı zihniyeti **"Nasıl yazarım?"** sorusuyla başlardı. Syntax hatırlamak, StackOverflow'da kaybolmak ve dökümantasyon sayfalarında saatler harcamak bir meziyetti.

AI-Driven mühendis zihniyeti ise **"Ne inşa ediyoruz ve bunu nasıl doğrularım?"** sorusunu merkeze alır:

| Özellik | Geleneksel Junior | AI Destekli (AI-Driven) Junior |
| :--- | :--- | :--- |
| **Odak Noktası** | Dil söz dizimi (Syntax) ve kütüphane API'leri | Problem tanımı, sistem akışı ve doğrulama |
| **Hızlandırıcı** | Google arama + StackOverflow kopyala-yapıştır | LLM ve Agent tabanlı akıllı asistanlar |
| **En Büyük Risk** | Yavaş öğrenme ve motivasyon kaybı | AI halüsinasyonunu fark edemeyip körü körüne güvenme |
| **Katma Değer** | Basit görevleri manuel kodlama | Görevi AI ile hızla çözüp kenar durumları test etme |

---

## 🤖 3. AI Prompt Laboratuvarı (Kopyala-Yapıştır Hazır Prompt)

Aşağıdaki prompt şablonunu Cursor, Claude Code, ChatGPT veya Copilot ortamınızda doğrudan kullanabilirsiniz:

```markdown
# ROL: Kıdemli Yazılım Mühendisi Mentoru
Sen deneyimli, temiz kod (Clean Code) standartlarına bağlı bir kıdemli mühendissin.
Ben yazılım ekibine yeni katılmış bir junior mühendisim.

## GÖREV:
Aşağıdaki kullanıcı hikayesi (User Story) için bana doğrudan kod YAZMA.
Bunun yerine:
1. Çözmem gereken temel iş mantığı maddelerini listele.
2. Karşılaşabileceğim 3 potansiyel uç durumu (edge case) belirt.
3. Kodu yazarken dikkat etmem gereken mimari prensibi açıkla.

## KULLANICI HİKAYESİ:
"Bir e-ticaret sepetinde kullanıcı indirim kuponu uyguladığında sepet toplamını güncelleyen fonksiyon." 
```

---

## 💻 4. Kod İncelemesi: Acemi / Halüsinasyon vs. Üretim Kalitesi

#### ❌ Acemi / Kontrolsüz AI Çıktısı (Riskli):
```python
# Kontrolsüz AI Çıktısı: Sınır değerleri ve tipleri kontrol edilmemiş fonksiyon
def apply_coupon(cart_total, coupon_discount):
    # Eğer indirim sepetten büyükse sepet eksiye düşüyor!
    # Tip kontrolü yok: coupon_discount string gelirse crash olur.
    return cart_total - coupon_discount
```

#### ✅ Kıdemli Mühendis Tarafından İyileştirilmiş Sürüm (Güvenli & Temiz):
```python
from decimal import Decimal
from typing import Union

def apply_discount(
    cart_total: Union[Decimal, float], 
    discount_amount: Union[Decimal, float]
) -> Decimal:
    """
    Sepet toplamına indirim uygular.
    Sepet tutarının sıfırın altına düşmesini engeller ve Decimal hassasiyetinde çalışır.
    """
    total = Decimal(str(cart_total))
    discount = Decimal(str(discount_amount))

    if total < Decimal("0.00"):
        raise ValueError("Sepet tutarı negatif olamaz.")
    if discount < Decimal("0.00"):
        raise ValueError("İndirim tutarı negatif olamaz.")

    new_total = total - discount
    return max(new_total, Decimal("0.00"))
```

**💡 Kod Analizi:**
Acemi yaklaşımda float tipi kullanılarak finansal yuvarlama hataları ve eksi bakiye bug'ı gözden kaçırılmıştır. Kıdemli mühendis denetimindeki sürümde ise `Decimal` tipiyle yuvarlama hassasiyeti sağlanmış, negatif değer kontrolleri ve `max(..., 0)` ile defansif koruma eklenmiştir.

---

## ⚠️ 5. Junior Tuzakları & Kıdemli Bakış Açısı

- **Tuzak:** AI'ın ürettiği ilk kodu çalıştığı an PR olarak açmak.
  - **Çözüm:** Her zaman 'Bu kod neden patlayabilir?' sorusunu sorup en az 3 uç durum testi yazın.
- **Tuzak:** Temel algoritma ve mantığı bilmeden her şeyi yapay zekaya devretmek.
  - **Çözüm:** AI'ı bir 'otopilot' değil, yan koltukta oturan 'yardımcı pilot' olarak görün.
- **Tuzak:** Halüsinasyon riskini unutup kütüphane fonksiyonlarını doğrulamamak.
  - **Çözüm:** AI tarafından önerilen kütüphane metotlarının resmi dokümantasyonunu her zaman hızlıca kontrol edin.

---

## 🎬 6. Udemy Video Dersi Taslağı & Slayt Maddeleri

### 🎥 Ders Başlığı: *Ders 1: AI Çağında Junior Olmak - İlk Adımlar ve Zihniyet Değişimi*
- 🖥️ **Slayt 1:** Neden 'Yazılımcılık Bitti' söylemi gerçeği yansıtmıyor?
- 🖥️ **Slayt 2:** Kod ezberciliğinden Problem Mimarisine geçiş.
- 🖥️ **Slayt 3:** AI-Driven geliştiricinin 3 temel ayağı: Bağlam, Doğrulama, İletişim.
- 🖥️ **Slayt 4:** Günün canlı demo özeti: Hatalı AI çıktısını senior seviyeye dönüştürmek.

**Canlı Kodlama / Ekran Kaydı Senaryosu:**  
Cursor veya VS Code'u açın. Basit bir e-ticaret indirim fonksiyonu isteyin. AI'ın ilk verdiği kontrolsüz çıktıyı inceleyin, eksiklerini tespit edin ve prompt ile defansif kontroller ekleterek test suite oluşturun.

---

## 🎯 7. Günün Uygulamalı Görevi & Mini Sınav

### 🛠️ Günün Görevi:
Bugün bir yapay zeka aracına (Claude, ChatGPT veya Cursor) daha önce yazdığınız bir fonksiyonu verin ve şu soruyu sorun: 'Bu fonksiyonu production ortamında çökertebilecek 3 senaryo nedir?'

### 🧠 Bölüm Sonu Kontrol Testi:

**Soru 1:** AI çağında bir junior yazılım mühendisinin en değerli ayırt edici yeteneği nedir?
  - A) En hızlı kod yazan kişi olmak
  - B) Üretilen kodun mantığını, sınır durumlarını ve doğruluğunu denetleyebilmek
  - C) Dillerin tüm kütüphane fonksiyonlarını ezbere bilmek
  - D) Kodlama yapmadan tüm işi yapay zekaya bırakmak
> **Doğru Yanıt:** B
> **Açıklama:** Yapay zeka hızlı kod üretebilir, ancak üretilen kodun doğruluğunu, sınır durumlarını ve sistemle uyumunu denetlemek mühendisin sorumluluğundadır.

**Soru 2:** Float tipi yerine Decimal kullanılmasının temel finansal sebebi nedir?
  - A) Decimal'ın bellekte daha az yer kaplaması
  - B) Kayan noktalı (float) aritmetiğindeki ikili taban yuvarlama hassasiyet kayıplarını önlemek
  - C) Sadece Python'da geçerli olması
  - D) Kodun derleme hızını artırması
> **Doğru Yanıt:** B
> **Açıklama:** Kayan noktalı sayılar ikili tabanda temsil edilirken kuruş hassasiyetinde yuvarlama hatalarına (örn. 0.1 + 0.2 != 0.3) yol açar. Finansal işlemlerde Decimal zorunludur.

