# 5. Prompt Mühendisliği Değil 'Context Mühendisliği': LLM'lere Nasıl Brif Verilir?

**Süslü Cümleleri Unutun: Şemalar, Tipler ve Dosya Sınırlarıyla Konuşun**  
*Bölüm 1 • Zorluk Derecesi: Başlangıç Seviyesi • Tahmini Okuma Süresi: 12 dk*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Notları
> **Podcast Tartışma Sorusu:**  
> *"'Sen bir dünya çapında yazılımcısın' gibi süslü prompt şablonları gerçekten işe yarıyor mu, yoksa modele doğru TypeScript interface'ini vermek çok daha mı etkili?"*  
> 
> **Bölümden Çıkarılacak 3 Altın Cümle:**  
> - 📌 Prompt mühendisliği sözcüklerle ilgilidir; Context mühendisliği ise sistemin durumunu ve sınırlarını modele aktarmakla ilgilidir.
- 📌 Çöp bağlam (Garbage Context) verirseniz, en gelişmiş model bile çöp kod üretir.
- 📌 Bir modele verilebilecek en kaliteli bağlam: Tip tanımları, girdi/çıktı örnekleri ve kabul kriterleridir.

---

## 📖 1. Giriş Hikayesi & Günlük Hayat Analojisi

Bir mimarlık ofisine stajyer girdiğini düşünün. Patron stajyere: *"Bana harika, modern, ödül alacak bir bina çiz!"* derse ne olur? Stajyer uzay mekiğine benzeyen ama inşa edilmesi imkansız bir gökdelen çizer.

Peki patron şöyle brif verirse:
- Arsa boyutu: 500 m²
- İmar izni: En fazla 3 kat
- Malzeme: Prefabrik betonarme ve cam
- Hedef: 4 kişilik 6 adet daire

Stajyer tam istenen, hemen inşa edilebilir projeyi getirir!

LLM'ler de tıpkı bu stajyer gibidir. Onlara *"Bana harika bir sepet fonksiyonu yaz"* derseniz halüsinasyon görürler. Ama şemayı, tipleri ve kısıtları verirseniz kusursuz üretim yaparlar.

---

## 🧠 2. AI Çağında Yeni Zihniyet Modeli

Context Mühendisliğinin 4B Formülü (Bağlam Piramidi):

```
       ┌────────────────────────┐
       │   4. Beklenen Çıktı    │ -> Örnek JSON / Dönüş Değeri
       ├────────────────────────┤
       │   3. Sınır & Kısıtlar  │ -> "Harici kütüphane yok, O(n) olacak"
       ├────────────────────────┤
       │   2. Tip ve Şemalar    │ -> TypeScript Interface / DB Schema
       ├────────────────────────┤
       │   1. Görev & Rol       │ -> "Kıdemli Backend Mühendisi"
       └────────────────────────┘
```

---

## 🤖 3. AI Prompt Laboratuvarı (Kopyala-Yapıştır Hazır Prompt)

Aşağıdaki prompt şablonunu Cursor, Claude Code, ChatGPT veya Copilot ortamınızda doğrudan kullanabilirsiniz:

```markdown
# ROL: Senior Backend Engineer
# GÖREV: Verilen kullanıcı listesini yaşa göre filtreleyip departmana göre gruplayan fonksiyon yaz.

## GİRDİ TİP TANIMI (TypeScript):
```typescript
interface Employee {
  id: string;
  name: string;
  age: number;
  department: 'ENGINEERING' | 'SALES' | 'MARKETING';
}
```

## KISITLAR:
- Hiçbir üçüncü taraf (Lodash vb.) kütüphane kullanılmayacak.
- Saf JavaScript/TypeScript `reduce` veya `Map` kullanılacak.
- Yaşı 18'den küçük olanlar elenecek.

## BEKLENEN ÇIKTI TİPİ:
```typescript
type GroupedResult = Record<Employee['department'], Employee[]>;
```
```

---

## 💻 4. Kod İncelemesi: Acemi / Halüsinasyon vs. Üretim Kalitesi

#### ❌ Acemi / Kontrolsüz AI Çıktısı (Riskli):
```typescript
// Zayıf Bağlam Verildiğinde AI Çıktısı: Lodash kütüphanesi şart koşulmuş ve tipler eksik
// Prompt: "Çalışanları departmana göre grupla"
const _ = require('lodash');

function groupStaff(data: any) {
  // Lodash yüklemediyseniz projeniz patlar!
  return _.groupBy(data, 'department');
}
```

#### ✅ Kıdemli Mühendis Tarafından İyileştirilmiş Sürüm (Güvenli & Temiz):
```typescript
// Context Mühendisliği ile Elde Edilen Çıktı: Sıfır bağımlılık, tam tip güvenliği
export interface Employee {
  id: string;
  name: string;
  age: number;
  department: 'ENGINEERING' | 'SALES' | 'MARKETING';
}

export type GroupedEmployees = Partial<Record<Employee['department'], Employee[]>>;

export function groupEmployeesByDepartment(
  employees: readonly Employee[]
): GroupedEmployees {
  return employees.reduce<GroupedEmployees>((acc, emp) => {
    if (emp.age < 18) {
      return acc; // Kısıt: 18 yaş altı elenir
    }

    const dept = emp.department;
    if (!acc[dept]) {
      acc[dept] = [];
    }
    acc[dept]!.push(emp);
    return acc;
  }, {});
}
```

**💡 Kod Analizi:**
Modele tipler ve kısıtlar ('Lodash kullanma') verildiğinde, fazladan 50KB bağımlılık eklemek yerine modern dil standartlarını kullanarak hafif ve güvenli kod üretir.

---

## ⚠️ 5. Junior Tuzakları & Kıdemli Bakış Açısı

- **Tuzak:** Prompt içine 10 paragraflık hikaye yazıp asıl teknik kısıtları unutmak.
  - **Çözüm:** Laf kalabalığını atın; kod şemalarını ve kısıtları maddeler halinde yazın.
- **Tuzak:** Modele veri tabanı şemasını vermeden SQL veya ORM kodu istemek.
  - **Çözüm:** Her zaman ilgili tablo şemasını (schema.prisma veya CREATE TABLE) bağlam olarak ekleyin.
- **Tuzak:** Hata aldığınızda sadece 'Hata verdi düzelt' yazmak.
  - **Çözüm:** Terminal çıktısını ve çağrı yığınını (stack trace) tam olarak bağlama ekleyin.

---

## 🎬 6. Udemy Video Dersi Taslağı & Slayt Maddeleri

### 🎥 Ders Başlığı: *Ders 5: Context Mühendisliği - LLM'lere Yazılımcı Gibi Brif Vermek*
- 🖥️ **Slayt 1:** Neden Prompt Mühendisliği yetersiz kalıyor?
- 🖥️ **Slayt 2:** 4B Formülü: Rol, Şemalar, Kısıtlar, Çıktı Formatı.
- 🖥️ **Slayt 3:** TypeScript Interface'lerini en güçlü prompt aracı olarak kullanmak.
- 🖥️ **Slayt 4:** Canlı uygulama: Kötü prompt vs Bağlamı zengin prompt karşılaştırması.

**Canlı Kodlama / Ekran Kaydı Senaryosu:**  
Aynı işi iki farklı pencerede yaptırın: Birinde 'Bana e-posta doğrulayan fonksiyon yaz' deyin; diğerinde regex kısıtları ve TypeScript tipleri verin. Çıkan iki kodu yan yana inceleyin.

---

## 🎯 7. Günün Uygulamalı Görevi & Mini Sınav

### 🛠️ Günün Görevi:
Yapay zekaya göndereceğiniz bir sonraki görevde hiçbir Türkçe/İngilizce açıklama yapmadan sadece `interface Input` ve `interface Output` vererek kod üretmesini isteyin.

### 🧠 Bölüm Sonu Kontrol Testi:

**Soru 1:** Context mühendisliğinde bir yapay zeka modeline verilebilecek en yüksek sinyalli (en kaliteli) bilgi hangisidir?
  - A) 'Sen dahi bir yazılımcısın' cümlesi
  - B) Tip tanımları, veri tabanı şeması ve girdi/çıktı kısıtları
  - C) 5 sayfalık genel şirket tanıtım metni
  - D) Emojilerle süslenmiş motivasyon mesajı
> **Doğru Yanıt:** B
> **Açıklama:** Modeller matematiksel olarak semantik sınırlara göre çalışır; tip tanımları ve şemalar en kesin kısıtları sağlayarak sapmayı önler.

**Soru 2:** Yapay zekanın gereksiz üçüncü taraf kütüphaneler eklemesini önlemenin en pratik yolu nedir?
  - A) İnterneti kapatmak
  - B) Prompt kısıtlarına 'Sıfır harici kütüphane, sadece yerel dil özellikleri kullanılacaktır' şartı eklemek
  - C) Sadece C dilinde kod yazmak
  - D) Kütüphane eklediğinde ona kızmak
> **Doğru Yanıt:** B
> **Açıklama:** Açıkça belirtilen kısıtlar (constraints), modelin token tahmin alanını sınırlar ve gereksiz bağımlılıkları engeller.

