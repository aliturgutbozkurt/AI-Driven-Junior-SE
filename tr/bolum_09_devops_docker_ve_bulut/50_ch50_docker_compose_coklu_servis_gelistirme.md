# 50. Docker Compose ile Çok Servisli Yerel Geliştirme Ortamı

**Tek Bir 'docker compose up' Komutuyla Tüm Şirket Altyapısını Ayağa Kaldırmak**  
*Bölüm 9 • Zorluk Derecesi: Orta Seviye • Tahmini Okuma Süresi: 12 dk*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Notları
> **Podcast Tartışma Sorusu:**  
> *"Yeni katıldığınız bir şirkette projeyi çalıştırmak için 3 gün boyunca PostgreSQL, Redis, RabbitMQ kurup boğuşmak mı, yoksa tek bir 'docker compose up' ile 1 dakikada kodlamaya başlamak mı?"*  
> 
> **Bölümden Çıkarılacak 3 Altın Cümle:**  
> - 📌 Docker Compose, çoklu konteyner uygulamalarını tek bir YAML dosyasında (`compose.yaml`) tanımlayıp yönetme aracıdır.
- 📌 Konteynerler aynı Docker köprüsünde (bridge network) birbirlerine IP adresi yerine doğrudan servis adlarıyla (örn: `postgres:5432`) erişir.
- 📌 Named Volume'lar, konteynerler silinse veya yeniden başlatılsa bile veritabanı verilerinin kaybolmasını engeller.

---

## 📖 1. Giriş Hikayesi & Günlük Hayat Analojisi

Bir orkestrayı yönettiğinizi düşünün. 

Konser saati geldiğinde kemancıya *"Sen hazırlan"*, 10 dakika sonra piyaniste *"Sen gel"*, sonra davulcuya *"Sen ayarla"* derseniz konser fiyaskoyla sonuçlanır! 

Orkestra şefi sahneye çıkar, bagetini kaldırır: **"1, 2, 3, BAŞLA!"** dediği anda 50 müzisyen aynı anda tek bir armoniyle çalmaya başlar!

Docker Compose işte o orkestra şefidir!
- Backend sunucusu
- PostgreSQL veritabanı
- Redis önbelleği
- MailHog e-posta test sunucusu

`docker compose up` dediğiniz anda hepsi aynı saniyede ayağa kalkar, birbirine bağlanır ve siz anında kod yazmaya başlarsınız.

---

## 🧠 2. AI Çağında Yeni Zihniyet Modeli

Docker Compose Ağ ve Veri Mimarisi:

```
[docker compose up]
         │
         ▼
┌────────────────────────────────────────────────────────┐
│           ÖZEL DOCKER AĞI (Internal Bridge)            │
│                                                        │
│  [Servis: backend] ──(postgres:5432)──> [Servis: db]   │
│         │                                    │         │
│         │ (redis:6379)                       ▼         │
│         ▼                               [NAMED VOLUME] │
│  [Servis: redis]                        (postgres_data)│
│                                          (Veri Kalıcı!)│
└────────────────────────────────────────────────────────┘
         │
  (Port 3000:3000)
         ▼
[Geliştirici Tarayıcısı: localhost:3000]
```

---

## 🤖 3. AI Prompt Laboratuvarı (Kopyala-Yapıştır Hazır Prompt)

Aşağıdaki prompt şablonunu Cursor, Claude Code, ChatGPT veya Copilot ortamınızda doğrudan kullanabilirsiniz:

```markdown
# ROL: DevOps ve Geliştirici Deneyimi (DevEx) Mimarı
Yerel geliştirme ortamımız için eksiksiz bir `compose.yaml` (Docker Compose) dosyası hazırlayacağız.

## GEREKSİNİMLER:
1. `app`: Mevcut Dockerfile'ı derlesin, 3000 portunu dışa açsın ve kod değişikliklerini anında yakalasın (volume mount).
2. `postgres`: PostgreSQL 16 Alpine kullansın, verileri `pg_data` named volume'unda saklasın ve sağlık kontrolü (healthcheck) içersin.
3. `redis`: Redis Alpine kullansın.
4. `app` servisi sadece PostgreSQL sağlık kontrolünden (healthy) geçtikten sonra başlasın (`depends_on`).
```

---

## 💻 4. Kod İncelemesi: Acemi / Halüsinasyon vs. Üretim Kalitesi

#### ❌ Acemi / Kontrolsüz AI Çıktısı (Riskli):
```yaml
# Kötü Compose Dosyası: Volume yok (veriler silinir), healthcheck yok, şifreler açık
services:
  db:
    image: postgres
  web:
    image: my-web-app
# db hazır olmadan web başlarsa bağlantı hatasıyla çöker!
```

#### ✅ Kıdemli Mühendis Tarafından İyileştirilmiş Sürüm (Güvenli & Temiz):
```yaml
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgresql://postgres:gizlisifre123@postgres:5432/uygulamadb
      - REDIS_URL=redis://redis:6379
    volumes:
      - .:/app
      - /app/node_modules # Host makinenin node_modules'ünü ezmeyi engeller
    depends_on:
      postgres:
        condition: service_healthy # Veritabanı TAM hazır olana kadar bekle!

  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: gizlisifre123
      POSTGRES_DB: uygulamadb
    ports:
      - "5432:5432"
    volumes:
      - pg_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres -d uygulamadb"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  pg_data: # Konteyner silinse bile veritabanı verisi diske kaydedilir!
```

**💡 Kod Analizi:**
`depends_on: condition: service_healthy` sayesinde backend servisi veritabanı gerçekten hazır olana kadar bekleterek başlangıç çöküşlerini engeller; `pg_data` named volume ile veritabanı kalıcılığı garanti edilir.

---

## ⚠️ 5. Junior Tuzakları & Kıdemli Bakış Açısı

- **Tuzak:** Konteyner içi bağlantılarda `localhost:5432` yazıp bağlanamamak.
  - **Çözüm:** Konteynerler birbirine `localhost` ile değil, servis adıyla (`postgres:5432`) bağlanır.
- **Tuzak:** Named volume kullanmayıp `docker compose down` yapınca tüm veritabanının silinmesi.
  - **Çözüm:** Veritabanı servislerinde mutlaka kalıcı named volume tanımlayın.
- **Tuzak:** Büyük projelerde `docker compose up` yapıp logları okuyamamak.
  - **Çözüm:** `docker compose up -d` ile arka planda başlatıp sadece ilgilendiğiniz servisin loglarını izleyin (`docker compose logs -f app`).

---

## 🎬 6. Udemy Video Dersi Taslağı & Slayt Maddeleri

### 🎥 Ders Başlığı: *Ders 50: Docker Compose - Tek Komutta Tüm Altyapı*
- 🖥️ **Slayt 1:** Docker Compose nedir ve çoklu servisleri nasıl orkestre eder?
- 🖥️ **Slayt 2:** Konteynerler arası iç ağ (Internal Network) ve servis adlandırma.
- 🖥️ **Slayt 3:** Service Healthchecks ve depends_on ile sıralı başlatma.
- 🖥️ **Slayt 4:** Canlı Demo: Tek komutla Next.js + Postgres + Redis ayağa kaldırmak.

**Canlı Kodlama / Ekran Kaydı Senaryosu:**  
Terminalde `docker compose up` çalıştırın. PostgreSQL'in sağlık kontrolünden geçip yeşil yandığını, ardından backend servisinin ayağa kalktığını gösterin. `docker compose down` ve tekrar `up` yaparak veritabanı kayıtlarının korunduğunu gösterin.

---

## 🎯 7. Günün Uygulamalı Görevi & Mini Sınav

### 🛠️ Günün Görevi:
Projeniz için bir `compose.yaml` dosyası oluşturun. İçine bir PostgreSQL ve bir Redis servisi ekleyip `docker compose up -d` ile ayağa kaldırın.

### 🧠 Bölüm Sonu Kontrol Testi:

**Soru 1:** Docker Compose ağında bir backend servisi PostgreSQL veritabanına bağlanırken host adresi olarak ne yazmalıdır?
  - A) localhost
  - B) 127.0.0.1
  - C) compose.yaml dosyasında PostgreSQL servisine verilen isim (Örn: `postgres` veya `db`)
  - D) Bilgisayarın MAC adresi
> **Doğru Yanıt:** C
> **Açıklama:** Docker Compose dahili DNS sunucusuna sahiptir; servisler birbirlerine doğrudan servis isimleriyle (örn: `postgres:5432`) erişir.

**Soru 2:** Docker Compose'da veritabanı servisinin hazır olmasını beklemek için hangi mekanizma kullanılır?
  - A) setTimeout
  - B) `healthcheck` ve `depends_on: condition: service_healthy`
  - C) Bilgisayarı kapatıp açmak
  - D) Sadece `ports` tanımı
> **Doğru Yanıt:** B
> **Açıklama:** Healthcheck veritabanının soket bağlantılarını kabul ettiğini teyit eder; `depends_on` ise bağımlı servisi o an gelene kadar bekletir.

