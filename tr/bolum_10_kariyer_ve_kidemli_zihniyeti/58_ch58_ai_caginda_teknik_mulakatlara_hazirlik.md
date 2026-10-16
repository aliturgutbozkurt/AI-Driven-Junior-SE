# 58. AI Çağında Teknik Mülakatlara Hazırlık: Live Coding & System Design

**Ezber LeetCode Sorularından Zihniyeti ve Akıl Yürütmeyi Kanıtlama Sanatına**  
*Bölüm 10 • Zorluk Derecesi: İleri Seviye • Tahmini Okuma Süresi: 13 dk*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Notları
> **Podcast Tartışma Sorusu:**  
> *"Yapay zeka tüm LeetCode sorularını 2 saniyede çözebiliyorsa, modern teknoloji şirketleri teknik mülakatlarda artık neyi ölçüyor?"*  
> 
> **Bölümden Çıkarılacak 3 Altın Cümle:**  
> - 📌 Mülakat yapanlar ezberlediğiniz cevabı değil; belirsizlik altında nasıl akıl yürüttüğünüzü (Thinking Out Loud) görmek ister.
- 📌 AI çağında mülakatlar 'kod yazma' testinden 'kod denetleme, mimari tasarım ve trade-off tartışma' sınavına dönüşmüştür.
- 📌 Sessiz kalıp kod yazmak elenme sebebidir; düşündüğünüz her hipotezi ve kenar durumu mülakatçıyla sesli paylaşın.

---

## 📖 1. Giriş Hikayesi & Günlük Hayat Analojisi

Bir pilot iş mülakatına girdiğinizi düşünün.

Havayolu şirketi pilot adayına: *"Bana uçağın hidrolik pompasının içindeki vidanın diş sayısını ezbere söyle"* der mi? Hayır!
Onu uçuş simülatörüne (Flight Simulator) oturturlar. Motorlardan biri alev aldığında pilotun nasıl sakin kaldığına, kuleyle nasıl iletişim kurduğuna ve acil durum prosedürlerini adım adım nasıl uyguladığına bakarlar!

Teknik mülakatlar da o uçuş simülatörüdür.

Mülakatçı size bir problem verdiğinde: *"Hemen sessizce kod yazayım, doğru cevabı çıkarayım"* derseniz kaybedersiniz. 
Mülakatçının görmek istediği:
- Soruyu netleştirmek için hangi soruları soruyorsunuz?
- Sınır durumları hesaba katıyor musunuz?
- Fikirlerinizi sesli olarak nasıl ifade ediyorsunuz?

---

## 🧠 2. AI Çağında Yeni Zihniyet Modeli

Mülakatta Başarı Formülü: REACTO Metodu

```
1. REPEAT (Tekrar Et & Anla):
   "Problemi doğru anladığımdan emin olmak için tekrar edeyim: Girdi pozitif tamsayılar mı olacak?"

2. EXAMPLES (Örnek Girdiler & Edge Caseler Çıkar):
   "Peki boş dizi veya tek elemanlı dizi gelirse çıktı ne olmalı?"

3. APPROACH (Sözde Kod ve Yaklaşım Tartışması):
   "Burada iki yol var: O(N^2) naive yaklaşım ya da O(N) Hash Map. İkincisini öneriyorum çünkü..."

4. CODE (Temiz ve Okunabilir Kod Yaz):
   Anlamlı değişken isimleri, early return ve modüler yapı.

5. TEST (Kodu Kendi Kendine Adım Adım Koştur):
   "Şimdi örnek bir '5' girdisiyle fonksiyonu satır satır takip edelim..."

6. OPTIMIZE (Karmaşıklığı Açıkla):
   "Zaman karmaşıklığı O(N), alan karmaşıklığı O(N)'dir."
```

---

## 🤖 3. AI Prompt Laboratuvarı (Kopyala-Yapıştır Hazır Prompt)

Aşağıdaki prompt şablonunu Cursor, Claude Code, ChatGPT veya Copilot ortamınızda doğrudan kullanabilirsiniz:

```markdown
# ROL: FAANG / Tier-1 Şirket Kıdemli Mülakatçısı
Ben mülakata giren bir junior yazılım mühendisiyim. Bana 'Canlı Kodlama ve Sistem Tasarımı' mülakatı simülasyonu yapacaksın.

## MÜLAKAT KURALLARI:
1. Bana gerçekçi, orta zorlukta bir problem sor (Örn: URL Kısaltıcı Servis veya Rate Limiter tasarımı).
2. Doğrudan çözümü söyleme; sadece benim sorduğum netleştirme sorularına yanıt ver.
3. Çözümümü REACTO metoduna göre (İletişim, Edge Caseler, Big-O Analizi) puanla ve yapıcı geri bildirim ver.
```

---

## 💻 4. Kod İncelemesi: Acemi / Halüsinasyon vs. Üretim Kalitesi

#### ❌ Acemi / Kontrolsüz AI Çıktısı (Riskli):
```typescript
// Mülakatta Elenme Sebebi: Sessizce oturup kontrolsüz kod yazmak
function solve(a: any, b: any) {
  // Mülakatçı ne yaptığınızı bilmiyor, değişken isimleri anlamsız, edge case yok!
  let x = [];
  for (let i = 0; i < a.length; i++) { x.push(a[i] + b); }
  return x;
}
```

#### ✅ Kıdemli Mühendis Tarafından İyileştirilmiş Sürüm (Güvenli & Temiz):
```typescript
// Mülakat Kazandıran Kod: İletişimli, Tip Güvenli, Sınır Değerleri Kontrollü
export function mergeSortedArrays(
  primaryList: readonly number[],
  secondaryList: readonly number[]
): number[] {
  // 1. Sınır Durum Koruması (Edge Cases)
  if (!primaryList.length) return [...secondaryList];
  if (!secondaryList.length) return [...primaryList];

  const mergedResult: number[] = [];
  let pointerA = 0;
  let pointerB = 0;

  // 2. İki İşaretçi (Two-Pointer) Deseni - O(N + M) Zaman, O(N + M) Alan
  while (pointerA < primaryList.length && pointerB < secondaryList.length) {
    if (primaryList[pointerA] <= secondaryList[pointerB]) {
      mergedResult.push(primaryList[pointerA]);
      pointerA++;
    } else {
      mergedResult.push(secondaryList[pointerB]);
      pointerB++;
    }
  }

  // 3. Kalan elemanları ekle
  while (pointerA < primaryList.length) {
    mergedResult.push(primaryList[pointerA++]);
  }
  while (pointerB < secondaryList.length) {
    mergedResult.push(secondaryList[pointerB++]);
  }

  return mergedResult;
}
```

**💡 Kod Analizi:**
Mülakatçıya iki işaretçi (Two-Pointer) yaklaşımının neden O(N+M) zaman karmaşıklığıyla sıralama fonksiyonlarından (`sort`: O(N log N)) daha üstün olduğu sesli olarak açıklanır.

---

## ⚠️ 5. Junior Tuzakları & Kıdemli Bakış Açısı

- **Tuzak:** Soruyu alır almaz hiç düşünmeden ve soru sormadan klavyeye sarılmak.
  - **Çözüm:** İlk 3-5 dakikayı sorular sorarak, sınır durumları netleştirerek geçirin.
- **Tuzak:** Mülakat esnasında dakikalarca tamamen sessiz kalmak.
  - **Çözüm:** Zihninizden geçenleri sesli düşünün: 'Şu an bir döngü kurmayı düşünüyorum çünkü...'
- **Tuzak:** Kodu bitirir bitirmez 'bitti' demek.
  - **Çözüm:** Kodu mülakatçıya teslim etmeden önce bir örnek girdiyle satır satır kendi kendinize test edin.

---

## 🎬 6. Udemy Video Dersi Taslağı & Slayt Maddeleri

### 🎥 Ders Başlığı: *Ders 58: AI Çağında Teknik Mülakatlar - REACTO Metodu*
- 🖥️ **Slayt 1:** LeetCode ezberciliğinin sonu: Şirketler artık neyi ölçüyor?
- 🖥️ **Slayt 2:** REACTO Metodu: Mülakatta adım adım kazanma stratejisi.
- 🖥️ **Slayt 3:** Sesli Düşünme (Thinking Out Loud) sanatı.
- 🖥️ **Slayt 4:** Canlı Mülakat Simülasyonu: Two-Pointer algoritması üzerinden vaka.

**Canlı Kodlama / Ekran Kaydı Senaryosu:**  
AI'ı mülakatçı rolüne sokun. Bir LeetCode orta seviye soru isteyin. Sesli düşünerek promptlar yazın; AI'ın sınır durum sorularınızı nasıl yanıtladığını ve sizi nasıl puanladığını canlı gösterin.

---

## 🎯 7. Günün Uygulamalı Görevi & Mini Sınav

### 🛠️ Günün Görevi:
Bugün AI asistanınıza: 'Bana orta seviye bir algoritma mülakatı simülasyonu yap' deyin ve REACTO metodunu uygulayarak bir mülakat simülasyonunu tamamlayın.

### 🧠 Bölüm Sonu Kontrol Testi:

**Soru 1:** Teknik bir mülakatta bir soruyu çözmeye başlamadan önce yapılması gereken en doğru ilk adım nedir?
  - A) Hemen hızlıca kod yazmaya başlamak
  - B) Problemi kendi cümlelerinizle tekrar edip, girdi sınırları ve edge caseler hakkında netleştirici sorular sormak
  - C) Mülakatçıdan cevabı istemek
  - D) Bilgisayarı yeniden başlatmak
> **Doğru Yanıt:** B
> **Açıklama:** Mülakatçılar gerçek dünyadaki gibi belirsiz problemler verir; iyi bir mühendis önce sorular sorarak gereksinimleri netleştirir.

**Soru 2:** Mülakatta kod yazmayı bitirdikten hemen sonra yapılması gereken profesyonel hareket nedir?
  - A) 'Bitti' deyip susmak
  - B) Mülakatçının test etmesini beklemeden, belirlediğiniz örnek bir girdiyle kodu satır satır kendi kendinize çalıştırıp (dry run) doğrulamak
  - C) Kodu silmek
  - D) Odayı terk etmek
> **Doğru Yanıt:** B
> **Açıklama:** Kendi kodunu test eden mühendis, yazdığı işe sahip çıktığını ve dikkatli olduğunu kanıtlar; mülakatçının puanını en çok artıran adımdır.

