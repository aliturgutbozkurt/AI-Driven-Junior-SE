# 51. Bulut Bilişime Giriş: AWS, GCP ve Azure Temel Kavramları

**Kendi Sunucunu Yönetme Zahmetinden Bulutun Sınırsız Gücüne Geçiş**  
*Bölüm 9 • Zorluk Derecesi: Orta Seviye • Tahmini Okuma Süresi: 12 dk*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Notları
> **Podcast Tartışma Sorusu:**  
> *"AWS konsolunda 200'den fazla servis var. Junior bir mühendis bunların hepsini bilmek zorunda mı, yoksa sadece 4 temel yapı taşını bilmek yeterli mi?"*  
> 
> **Bölümden Çıkarılacak 3 Altın Cümle:**  
> - 📌 Tüm bulut servisleri 4 ana yapı taşı üzerine kuruludur: Compute (İşlemci), Storage (Depolama), Database (Veritabanı) ve Networking (Ağ).
- 📌 EC2 kiralık sanal bir bilgisayardır; S3 sınırsız bir dosya deposudur; RDS yönetilen bir veritabanıdır.
- 📌 Bulut maliyetleri kullandıkça öde (Pay-as-you-go) modelidir; kapatılmayan test sunucuları devasa faturalar çıkarabilir.

---

## 📖 1. Giriş Hikayesi & Günlük Hayat Analojisi

Evinizde elektrik üretmek istediğinizi düşünün.

Bahçenize jeneratör kurup, her gün benzin alıp, motorun yağını değiştirip, gece sesinden uyuyamaz mıydınız? Tabii ki hayır! Duvardaki prize bir fiş takarsınız. Elektrik idaresi elektriği üretir, siz sadece ay sonunda harcadığınız kilovatsaat kadar fatura ödersiniz.

Bulut Bilişim (Cloud Computing) işte o elektrik prizidir!

Eskiden şirketler ofislerinin bodrum katına devasa sunucu odaları kurar, klima arızalarıyla boğuşur, hard disk değiştirirdi (On-Premise). 
Bugün AWS, Google Cloud veya Azure sayesinde tek tıkla dünyanın en güçlü veri merkezlerinden prizi takıyor ve sadece kullandığımız saniye kadar ödeme yapıyoruz.

---

## 🧠 2. AI Çağında Yeni Zihniyet Modeli

Bulutun 4 Temel Yapı Taşı Karşılaştırması:

| Yapı Taşı | AWS Karşılığı | GCP Karşılığı | Ne İşe Yarar? |
| :--- | :--- | :--- | :--- |
| **Compute (İşlem)** | EC2 / ECS / Lambda | Compute Engine / Cloud Run | Kodu çalıştıran sanal işlemciler ve RAM |
| **Storage (Depolama)**| S3 (Simple Storage) | Cloud Storage | Resimler, videolar, yedekler (Sınırsız nesne deposu) |
| **Database (Veri)** | RDS / Aurora / DynamoDB | Cloud SQL / Firestore | Otomatik yedeklenen, bakımı yapılan veritabanı |
| **Networking (Ağ)** | VPC / Route 53 / ALB | VPC / Cloud DNS / Load Balancing | Güvenlik duvarları, alan adı ve yük dengeleme |

---

## 🤖 3. AI Prompt Laboratuvarı (Kopyala-Yapıştır Hazır Prompt)

Aşağıdaki prompt şablonunu Cursor, Claude Code, ChatGPT veya Copilot ortamınızda doğrudan kullanabilirsiniz:

```markdown
# ROL: Bulut Çözüm Mimarı (AWS Certified Solutions Architect)
Bir startup'ın ilk web uygulamasını AWS üzerinde ayağa kaldıracağız.

## GEREKSİNİMLER:
- 1 adet Docker konteynerinde çalışan Node.js API
- 1 adet PostgreSQL veritabanı
- Kullanıcı profil fotoğraflarının yükleneceği dosya deposu

## GÖREV:
1. En ucuz ve yönetimi en kolay AWS servis kombinasyonunu öner (Örn: App Runner / ECS Fargate + RDS + S3).
2. S3 bucket'ına dosya yüklerken güvenliği sağlayan 'Presigned URL' mimarisini açıkla.
3. Maliyet alarmı (AWS Budget Alert) kurmanın adımlarını özetle.
```

---

## 💻 4. Kod İncelemesi: Acemi / Halüsinasyon vs. Üretim Kalitesi

#### ❌ Acemi / Kontrolsüz AI Çıktısı (Riskli):
```typescript
// Kötü Bulut Mimarisi: Kullanıcı resimlerini doğrudan web sunucusunun diskine kaydetmek
// Sunucu yeniden başladığında veya 2. sunucu açıldığında tüm resimler kaybolur!
app.post("/upload", (req, res) => {
  fs.writeFileSync(`/var/www/uploads/${req.body.name}`, req.body.file);
});
```

#### ✅ Kıdemli Mühendis Tarafından İyileştirilmiş Sürüm (Güvenli & Temiz):
```typescript
import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

const s3 = new S3Client({ region: process.env.AWS_REGION });

// Mükemmel Mimari: S3 Presigned URL ile Doğrudan Güvenli Yükleme
// Sunucu dosya yüküyle yorulmaz; istemci doğrudan S3'e güvenle yükler!
export async function generateAvatarUploadUrl(userId: string): Promise<string> {
  const fileKey = `avatars/${userId}-${Date.now()}.png`;

  const command = new PutObjectCommand({
    Bucket: process.env.S3_BUCKET_NAME,
    Key: fileKey,
    ContentType: "image/png"
  });

  // 15 Dakika geçerli tek kullanımlık imzalı yükleme linki üret
  return await getSignedUrl(s3, command, { expiresIn: 900 });
}
```

**💡 Kod Analizi:**
Presigned URL deseni sayesinde kullanıcı dosyayı web sunucunuza değil, doğrudan S3'e yükler. Web sunucunuzun işlemcisi ve belleği dosya yükleme trafiğiyle boğulmaz.

---

## ⚠️ 5. Junior Tuzakları & Kıdemli Bakış Açısı

- **Tuzak:** Kullanıcı dosyalarını sunucunun yerel diskine kaydetmek (Konteyner kapanınca silinir!).
  - **Çözüm:** Statik medyayı daima S3 veya Google Cloud Storage gibi Nesne Depolarında (Object Storage) saklayın.
- **Tuzak:** AWS hesabında bütçe alarmı (Budget Alert) kurmayı unutmak.
  - **Çözüm:** İlk gün 10$ ve 50$ eşiklerinde e-posta gönderen bir bütçe alarmı kurun.
- **Tuzak:** S3 bucket'larını internete tamamen açık (Public Read/Write) bırakıp veri sızdırmak.
  - **Çözüm:** Bucket'larda 'Block Public Access' ayarını açık tutun; erişimi Presigned URL ile sınırlayın.

---

## 🎬 6. Udemy Video Dersi Taslağı & Slayt Maddeleri

### 🎥 Ders Başlığı: *Ders 51: Bulut Bilişim 101 - AWS, GCP ve Temel Yapı Taşları*
- 🖥️ **Slayt 1:** Neden artık kimse bodrumda sunucu kurmuyor? Bulutun gücü.
- 🖥️ **Slayt 2:** 4 Temel Taş: Compute, Storage, Database, Networking.
- 🖥️ **Slayt 3:** S3 Presigned URL ile sunucuyu yormadan güvenli dosya yükleme.
- 🖥️ **Slayt 4:** AWS Bütçe Alarmları ile sürpriz faturalardan korunmak.

**Canlı Kodlama / Ekran Kaydı Senaryosu:**  
AWS konsoluna girin (veya LocalStack ile simüle edin). S3 üzerinde bir bucket açın. Node.js SDK ile 15 saniyede bir presigned URL üretip curl ile dosyayı doğrudan S3'e yüklemeyi canlı gösterin.

---

## 🎯 7. Günün Uygulamalı Görevi & Mini Sınav

### 🛠️ Günün Görevi:
AWS veya Google Cloud hesabınızda ilk bütçe alarmınızı (Budget Alert: 10$) kurun ve bildirim e-postanızı ekleyin.

### 🧠 Bölüm Sonu Kontrol Testi:

**Soru 1:** AWS S3 (Simple Storage Service) gibi Nesne Depoları (Object Storage) geleneksel sunucu disklerinden hangi özelliğiyle ayrılır?
  - A) Sadece müzik saklayabilmesi
  - B) Sınırsız depolama kapasitesi sunması, yüksek dayanıklılık (%99.999999999) sağlaması ve dosyalara doğrudan HTTP üzerinden erişilebilmesi
  - C) Bilgisayara takılan bir USB bellek olması
  - D) Sadece Python ile çalışması
> **Doğru Yanıt:** B
> **Açıklama:** S3, sabit disk boyutu kısıtlaması olmadan petabaytlarca veriyi güvenle ve yüksek dayanıklılıkla saklayan dağıtık bir nesne deposudur.

**Soru 2:** Bir web uygulamasında dosya yüklerken 'Presigned URL' kullanmanın sağladığı en büyük mimari fayda nedir?
  - A) Dosyanın rengini değiştirmesi
  - B) İstemcinin dosyayı doğrudan S3'e yüklemesini sağlayarak backend sunucusunun işlemci, bellek ve bant genişliği darboğazına girmesini engellemesi
  - C) Sadece Chrome'da çalışması
  - D) Veritabanını silmesi
> **Doğru Yanıt:** B
> **Açıklama:** Presigned URL, dosya trafiğini uygulama sunucusundan arındırarak yükü doğrudan S3 altyapısına devreder.

