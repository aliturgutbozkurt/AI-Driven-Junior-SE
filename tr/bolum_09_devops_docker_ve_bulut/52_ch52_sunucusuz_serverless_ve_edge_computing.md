# 52. Sunucusuz (Serverless) Mimariler & Edge Computing

**Sıfır Sunucu Yönetimi, Soğuk Başlangıçlar (Cold Start) ve Küresel Dağıtım**  
*Bölüm 9 • Zorluk Derecesi: Orta / İleri Seviye • Tahmini Okuma Süresi: 12 dk*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Notları
> **Podcast Tartışma Sorusu:**  
> *"Serverless mimaride gerçekten 'sunucu yok' mu? AWS Lambda ve Vercel Edge Functions kodu dünyanın dört bir yanındaki kullanıcılara 5 milisaniyede nasıl ulaştırır?"*  
> 
> **Bölümden Çıkarılacak 3 Altın Cümle:**  
> - 📌 Serverless 'sunucusuz' demek değildir; sunucuların yönetimini ve ölçeklenmesini bulut sağlayıcısına devretmektir.
- 📌 Kullanılmadığında 0 maliyet üretir; trafik geldiğinde saniyenin onda birinde otomatik olarak 1'den 10.000 örneğe fırlar.
- 📌 Soğuk Başlangıç (Cold Start) sorununu aşmak için hafif edge çalışma zamanları (Cloudflare Workers / Vercel Edge) tercih edilmelidir.

---

## 📖 1. Giriş Hikayesi & Günlük Hayat Analojisi

Bir taksi durağını ve kiralık bir arabayı düşünün.

Eğer bir araba kiralarsanız (Geleneksel Sunucu / EC2): Arabayı sürseniz de, garajda park halinde dursa da her ay 1000 dolar kira ödersiniz.

Peki ya taksi çağırırsanız (Serverless / Lambda)? Taksi kapınıza gelir, sizi gitmek istediğiniz yere götürür ve sadece gittiğiniz kilometre kadar ücret ödersiniz. Taksi bittikten sonra gider; arabanın vergisiyle, sigortasıyla, bakımıyla siz uğraşmazsınız!

Edge Computing ise durağın hemen her köşe başında olmasıdır: Taksi 30 saniye içinde kapınızdadır!

Günde sadece 50 istek alan bir servis için ayda 50 dolar sunucu parası ödemek yerine, serverless ile ayda 0.01 dolar ödersiniz.

---

## 🧠 2. AI Çağında Yeni Zihniyet Modeli

Geleneksel Sunucu vs Serverless vs Edge:

```
┌────────────────────────────────────────────────────────┐
│                   MİMARİ KARŞILAŞTIRMASI               │
└──────────────────────────┬─────────────────────────────┘
                           │
       ┌───────────────────┼───────────────────┐
       ▼                   ▼                   ▼
[1. GELENEKSEL SUNUCU] [2. SERVERLESS (Lambda)] [3. EDGE COMPUTING]
- 7/24 çalışır, ödersin- İstek gelince uyanır   - Kullanıcıya en yakın
- Node.js tam ortamı   - Boştayken 0$ fatura     veri merkezinde koşar
- Cold Start yok       - Cold Start: 200-500 ms - Cold Start: < 5 ms
- Konum: Tek bir bölge - Konum: Bölgesel        - Konum: 300+ Şehir
```

---

## 🤖 3. AI Prompt Laboratuvarı (Kopyala-Yapıştır Hazır Prompt)

Aşağıdaki prompt şablonunu Cursor, Claude Code, ChatGPT veya Copilot ortamınızda doğrudan kullanabilirsiniz:

```markdown
# ROL: Serverless ve Edge Mimarı
Vercel Edge Functions veya Cloudflare Workers kullanarak küresel ölçekte çalışan bir 'Geolokasyon Yönlendirme Servisi' yazacağız.

## GÖREV:
1. Kullanıcının hangi ülkeden geldiğini tespit eden bir Edge Function kodu yaz.
2. V8 Isolate mimarisinin neden Node.js sanal makinelerine göre 100 kat daha hızlı ayağa kalktığını açıkla.
3. Serverless fonksiyonlarda veritabanı bağlantı havuzu (Connection Pooling) patlamasını önlemek için Prisma Accelerate / Neon Serverless kullanımını özetle.
```

---

## 💻 4. Kod İncelemesi: Acemi / Halüsinasyon vs. Üretim Kalitesi

#### ❌ Acemi / Kontrolsüz AI Çıktısı (Riskli):
```typescript
// Kötü Serverless Kullanımı: Her fonksiyon çağrısında yeni DB bağlantısı açmak
// 1000 eşzamanlı istek geldiğinde veritabanının bağlantı havuzu (Max Connections) patlar!
import { Client } from 'pg';

export async function handler() {
  const client = new Client(process.env.DB_URL);
  await client.connect(); // HATA: Her lambdada yeni bağlantı açılırsa PostgreSQL çöker!
  const res = await client.query('SELECT * FROM config');
  await client.end();
  return res.rows;
}
```

#### ✅ Kıdemli Mühendis Tarafından İyileştirilmiş Sürüm (Güvenli & Temiz):
```typescript
// Modern Edge Fonksiyonu: Sub-10ms Gecikme ile Küresel Yürütme (api/geo.ts)

export const config = {
  runtime: "edge" // V8 Isolate üzerinde çalışır (Cold Start < 5ms)
};

export default async function handler(request: Request) {
  // Edge runtime otomatik olarak kullanıcının coğrafi konumunu başlıkta sunar
  const country = request.headers.get("x-vercel-ip-country") || "TR";
  const city = request.headers.get("x-vercel-ip-city") || "Istanbul";

  const localizedGreeting = country === "TR" 
    ? "Hoş geldiniz!" 
    : "Welcome to our global platform!";

  return new Response(
    JSON.stringify({
      message: localizedGreeting,
      location: { country, city },
      servedAt: new Date().toISOString()
    }),
    {
      status: 200,
      headers: {
        "content-type": "application/json",
        "cache-control": "public, s-maxage=60, stale-while-revalidate=30"
      }
    }
  );
}
```

**💡 Kod Analizi:**
`runtime: 'edge'` direktifi ile kod standart ağır container yerine Cloudflare/Vercel V8 Isolate motorunda koşar. Dünyanın neresinden istek gelirse gelsin kullanıcıya en yakın veri merkezinde 5 milisaniyede yanıt üretilir.

---

## ⚠️ 5. Junior Tuzakları & Kıdemli Bakış Açısı

- **Tuzak:** Serverless fonksiyonlarda veritabanı bağlantı havuzu (Connection Pooler) kullanmamak.
  - **Çözüm:** Sunucusuz ortamlarda daima PgBouncer, Prisma Accelerate veya Neon gibi HTTP bağlantı havuzlayıcıları kullanın.
- **Tuzak:** Büyük ve uzun süren (>15 dakika) işlemleri Serverless fonksiyonlarda çalıştırmaya çalışmak.
  - **Çözüm:** Uzun süren işler (video işleme, büyük veri) için Lambda yerine arka plan işçileri (ECS/SQS) kullanın.
- **Tuzak:** Edge fonksiyonlarında Node.js'e özel modülleri (örn: `fs` veya `child_process`) çağırmak.
  - **Çözüm:** Edge çalışma zamanları standart Web API'lerini (fetch, Request, Response) destekler; dosya sistemi modüllerini çağırmayın.

---

## 🎬 6. Udemy Video Dersi Taslağı & Slayt Maddeleri

### 🎥 Ders Başlığı: *Ders 52: Serverless ve Edge Computing - Sunucusuz Gelecek*
- 🖥️ **Slayt 1:** Serverless nedir? Sıfır maliyetten küresel ölçeğe geçiş.
- 🖥️ **Slayt 2:** Cold Start problemi ve V8 Isolate mimarisi.
- 🖥️ **Slayt 3:** Edge Runtimes: Kullanıcının 5 milisaniye yanında kod çalıştırmak.
- 🖥️ **Slayt 4:** Serverless veritabanı bağlantı havuzu yönetimi (Connection Pooling).

**Canlı Kodlama / Ekran Kaydı Senaryosu:**  
Vercel üzerinde basit bir Edge Function deploy edin. Farklı ülkelerden VPN ile istek atarak yanıt süresinin her ülkede 10 milisaniye altında kaldığını ve x-vercel-ip-country başlığının doğru çalıştığını canlı gösterin.

---

## 🎯 7. Günün Uygulamalı Görevi & Mini Sınav

### 🛠️ Günün Görevi:
Next.js veya Cloudflare Workers projenizde basit bir Edge rotası oluşturun ve kullanıcının istek başlıklarını inceleyin.

### 🧠 Bölüm Sonu Kontrol Testi:

**Soru 1:** Serverless (Sunucusuz) mimarinin geleneksel sanal makinelere (VM) göre en büyük ekonomik avantajı nedir?
  - A) Elektrik faturası ödememek
  - B) 'Scale-to-Zero' (Sıfıra Ölçeklenme) özelliği sayesinde hiç istek gelmediğinde 0 TL maliyet üretmesi; sadece çağrıldığı saniyeler için ödeme yapılması
  - C) Sadece C++ dilinde çalışması
  - D) Kodların silinmesi
> **Doğru Yanıt:** B
> **Açıklama:** Serverless servisler kullanılmadığı anlarda tamamen kapanır ve sıfır maliyet yaratır; trafik geldiğinde ise milisaniyeler içinde ayağa kalkar.

**Soru 2:** Serverless fonksiyonlarda 'Cold Start' (Soğuk Başlangıç) ne demektir?
  - A) Sunucunun kışın donması
  - B) Uzun süre çağrılmayan bir fonksiyon ilk kez tetiklendiğinde bulut sağlayıcının yeni bir mikro-konteyner ayağa kaldırması sebebiyle ilk istekte yaşanan küçük gecikme
  - C) Bilgisayarın fanının çalışması
  - D) Kodun derlenememesi
> **Doğru Yanıt:** B
> **Açıklama:** Boştaki fonksiyonlar uyutulur. Yeni bir istek geldiğinde ortamın sıfırdan başlatılması birkaç yüz milisaniyelik soğuk başlangıç gecikmesine yol açar.

