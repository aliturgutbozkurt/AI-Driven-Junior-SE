"""
Section 9: DevOps, Docker & Bulut Dağıtımı (Chapters 49 to 54)
"""

def get_section_chapters():
    return [
        # Chapter 49
        {
            "id": 49,
            "section_id": 9,
            "slug_tr": "ch49_benim_makinemde_calisiyordu_docker_101",
            "slug_en": "ch49_works_on_my_machine_docker_fundamentals",
            "title_tr": "'Benim Makinemde Çalışıyordu': Docker ve Konteyner Mantığı",
            "title_en": "'Works on My Machine': Docker & Container Fundamentals Decoded",
            "subtitle_tr": "Yazılım Dünyasının En Meşhur Mazeretini Tarihe Gömen Konteyner Devrimi",
            "subtitle_en": "Eradicating the Most Infamous Excuse in Tech via Immutable Linux Containers",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Bir junior mühendisin 'Ama benim bilgisayarımda çalışıyordu!' demesi neden bir senior lider için en sinir bozucu cümledir ve Docker bunu nasıl çözer?",
            "podcast_hook_en": "Why is 'It worked fine on my laptop!' the most infuriating excuse in software engineering, and how does Docker eliminate environmental drift?",
            "takeaways_tr": [
                "Docker, uygulamanızı tüm bağımlılıkları, işletim sistemi kütüphaneleri ve konfigürasyonlarıyla birlikte izole bir kutuya (Container) paketler.",
                "İmaj (Image) mimari plandır (class); Konteyner (Container) ise o planın çalışan canlı örneğidir (instance).",
                "Çok aşamalı derleme (Multi-Stage Build), üretim imajlarını 1 GB'tan 50 MB'a düşürerek hem güvenlik hem hız sağlar."
            ],
            "takeaways_en": [
                "Docker packages application code, runtime dependencies, and operating system packages into an immutable, isolated container.",
                "An Image is the immutable class blueprint; a Container is the running instantiated process.",
                "Multi-stage builds strip compilers and development toolchains, shrinking final production containers from 1GB to 50MB."
            ],
            "story_tr": """1950'li yıllardan önce uluslararası deniz ticaretini hayal edin.

Muzlar ahşap kasalara konur, pamuklar çuvallara basılır, viski şişeleri samanların arasına sarılırdı. Bir limandan diğerine aktarılırken şişeler kırılır, muzlar çürür, her limanın vinci farklı olduğu için yükleme günlerce sürerdi!

Sonra Malcolm McLean adında bir adam çıktı ve **Standart Çelik Taşımacılık Konteynerini** icat etti!
İçinde ne olursa olsun (araba, muz, bilgisayar), dışındaki çelik kutunun boyutları ve kilitleri standarttır. Dünyadaki her vinç, her gemi, her tır bu konteyneri aynı hızla taşır.

Docker işte o çelik konteynerdir! 

Uygulamanızı Docker kutusuna koyduğunuzda; kodunuzun Mac'te mi, Windows'ta mı yoksa AWS Ubuntu sunucusunda mı çalıştığının hiçbir önemi kalmaz. Her yerde aynı milisaniyede çalışır.""",
            "story_en": """Consider global maritime cargo shipping prior to 1956.

Bananas were packed into cedar crates, cotton stuffed into burlap sacks, and whiskey barrels wedged between straw bales. Unloading at foreign ports was chaos: bottles broke, grain spoiled, and every harbor crane required bespoke rigging.

Then Malcolm McLean engineered the standardized intermodal shipping container: a uniform corrugated steel box. Whether hauling textiles, machine parts, or frozen beef, the external dimensions and locking corners are identical. Every crane, railcar, and cargo ship handles it uniformly.

Docker is that standard intermodal shipping container for code.

Once an application is encapsulated inside a container image, whether the underlying host is an M3 MacBook, a Windows workstation, or an AWS Linux cluster becomes irrelevant. It executes identically everywhere.""",
            "mental_tr": """Docker Kavramlar Sözlüğü:

```
1. DOCKERFILE:
   Konteynerin yemek tarifidir. "Hangi Linux sürümü, hangi Node.js, hangi dosyalar kopyalanacak?"

2. DOCKER IMAGE (İmaj):
   Tarife göre fırından çıkmış dondurulmuş kek kalıbıdır. Değiştirilemez (Immutable), taşınabilir.

3. DOCKER CONTAINER (Konteyner):
   İmajın RAM üzerinde çalışan canlı halidir. Başlatılabilir, durdurulabilir, çoğaltılabilir.

4. DOCKER REGISTRY (Docker Hub / AWS ECR):
   İmajların internette saklandığı ve paylaşıldığı kütüphanedir.
```""",
            "mental_en": """The Docker Conceptual Hierarchy:

```
1. DOCKERFILE:
   The declarative build recipe: base OS distribution, dependencies, and entrypoint command.

2. DOCKER IMAGE:
   The compiled, immutable snapshot: a layered filesystem artifact stored in a registry.

3. DOCKER CONTAINER:
   An isolated, instantiated runtime process running an image on a shared host OS kernel.

4. CONTAINER REGISTRY (Docker Hub / AWS ECR):
   The centralized repository hosting versioned container images.
```""",
            "prompt_tr": """# ROL: DevOps ve Konteynerleştirme Uzmanı
Next.js ve Node.js 20 kullanan bir web uygulaması için production-ready `Dockerfile` yazacağız.

## GÖREV:
1. 'Multi-Stage Build' (Çok Aşamalı Derleme) kullanarak derleme araçlarını nihai imajdan temizle.
2. `node_modules` ve kaynak kodları non-root (root olmayan) güvenli bir kullanıcı ile çalıştır.
3. İmaj boyutunu en aza indiren hafif `node:20-alpine` tabanını kullan.""",
            "prompt_en": """# ROLE: Containerization & DevOps Specialist
Author a production-grade `Dockerfile` for a Next.js / TypeScript application.

## TASK:
1. Implement a Multi-Stage Build stripping build tooling, TypeScript compilers, and devDependencies from the final container.
2. Enforce non-root security by executing via an unprivileged `nextjs` user.
3. Target `node:20-alpine` to maintain a sub-100MB production footprint.""",
            "code_lang": "dockerfile",
            "code_naive": """# Kötü / Ağır Dockerfile: 1.2 GB boyut, root kullanıcısı, devDependencies temizlenmemiş!
FROM node:20
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build
CMD ["npm", "start"] # Root olarak çalışır (BÜYÜK GÜVENLİK RİSKİ)""",
            "code_robust": """# Çok Aşamalı (Multi-Stage) Üretim Dockerfile

# AŞAMA 1: Bağımlılıkları Kur
FROM node:20-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

# AŞAMA 2: Uygulamayı Derle
FROM node:20-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

# AŞAMA 3: Hafif & Güvenli Üretim Ortamı (Minimal Runner)
FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production

# Güvenlik Kuralı: Asla 'root' kullanıcısı ile çalıştırma!
RUN addgroup --system --gid 1001 nodejs && \\
    adduser --system --uid 1001 nextjs

# Sadece derlenmiş çıktıları kopyala (İmaj boyutu 1.2 GB yerine 80 MB!)
COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs
EXPOSE 3000
ENV PORT=3000

CMD ["node", "server.js"]""",
            "code_notes_tr": "Multi-stage yapı sayesinde derleyici ve dev paketler `builder` aşamasında çöpe atılmış, sadece saf JavaScript ve asset'ler `runner` aşamasına kopyalanarak imaj boyutu 1.2 GB'tan 80 MB'a düşürülmüş ve `USER nextjs` ile root çalıştırma riski önlenmiştir.",
            "code_notes_en": "Multi-stage compilation discards heavy toolchains in the builder stage, copying only standalone production bundles into the runner. The image drops from 1.2GB to 80MB, executing under an unprivileged `nextjs` UID.",
            "pitfalls_tr": [
                {"trap": "Konteyneri varsayılan `root` kullanıcısı ile çalıştırıp sunucuda güvenlik açığı yaratmak.", "solution": "Her zaman `USER node` veya özel bir non-root kullanıcı tanımlayın."},
                {"trap": "`.dockerignore` dosyası oluşturmayıp `node_modules` ve `.env` dosyalarını imaja kopyalamak.", "solution": "Proje köküne mutlaka kapsamlı bir `.dockerignore` dosyası ekleyin."},
                {"trap": "Konteyner içinde veri saklayıp konteyner silindiğinde tüm veritabanını kaybetmek.", "solution": "Kalıcı veriler için daima Docker Volumes (`-v db_data:/var/lib/postgresql/data`) kullanın."}
            ],
            "pitfalls_en": [
                {"trap": "Executing containers as the default `root` user, expanding host breakout risks.", "solution": "Always declare an unprivileged system user (`USER node`)."},
                {"trap": "Omitting `.dockerignore` and copying local `node_modules` or `.env` into image layers.", "solution": "Add a `.dockerignore` file mirroring your `.gitignore` configuration."},
                {"trap": "Storing database data inside ephemeral container writable layers.", "solution": "Always bind database persistence paths to external Docker Volumes (`-v db_data:/data`)."}
            ],
            "udemy_title_tr": "Ders 49: Docker 101 - 'Benim Makinemde Çalışıyordu' Efsanesine Son",
            "udemy_title_en": "Lecture 49: Docker 101 - Demystifying Containers for Developers",
            "udemy_slides_tr": [
                "Neden 'Benim makinemde çalışıyor' mazereti artık kabul edilemez?",
                "Konteyner vs Sanal Makine (VM): Hafifliğin sırrı.",
                "Multi-Stage Build ile 1.2 GB'lık imajı 80 MB'a düşürmek.",
                "Canlı Demo: Sıfırdan Dockerfile yazıp imaj derlemek."
            ],
            "udemy_slides_en": [
                "Why 'It works on my machine' is unacceptable in modern engineering.",
                "Containers vs. Virtual Machines: Shared kernel isolation.",
                "Multi-stage builds: Shrinking 1.2GB bloat to an 80MB artifact.",
                "Live demo: Authoring and building an immutable container image."
            ],
            "udemy_demo_tr": "Bir Next.js projesinde `docker build -t my-app .` çalıştırın. `docker images` çıktısında imaj boyutunun 80 MB olduğunu gösterin. `docker run -p 3000:3000 my-app` ile tarayıcıda uygulamanın ayağa kalktığını canlı gösterin.",
            "udemy_demo_en": "Execute `docker build -t my-app .` on a sample service. Run `docker images` to demonstrate an 80MB footprint. Launch the container via `docker run -p 3000:3000 my-app` and verify browser accessibility.",
            "action_task_tr": "Kişisel bir projeniz için çok aşamalı (multi-stage) bir `Dockerfile` ve `.dockerignore` dosyası yazarak yerel makinenizde imajı derleyin.",
            "action_task_en": "Author a multi-stage `Dockerfile` and companion `.dockerignore` for a local repository, verifying it compiles and runs locally.",
            "quiz_tr": [
                {
                    "question": "Docker'da 'Multi-Stage Build' (Çok Aşamalı Derleme) kullanmanın en büyük faydası nedir?",
                    "options": [
                        "A) Bilgisayara yeni monitör bağlamak",
                        "B) Derleme aşamasında kullanılan ağır araçları (compiler, TypeScript, npm cache) üretim imajından çöpe atarak nihai imajı hem çok hafif (MB düzeyinde) hem de saldırılara karşı daha güvenli kılmak",
                        "C) Sadece C++ dilinde çalışması",
                        "D) İnternet gerektirmemesi"
                    ],
                    "answer": "B",
                    "explanation": "Multi-stage builds, gereksiz kaynak kodları ve derleme araçlarını nihai imajın dışında bırakarak hafif ve güvenli konteynerler üretir."
                },
                {
                    "question": "Docker konteynerleri ile geleneksel Sanal Makineler (Virtual Machine - VM) arasındaki temel fark nedir?",
                    "options": [
                        "A) Hiçbir farkı yoktur",
                        "B) Sanal makineler her biri için ayrı bir misafir işletim sistemi (Guest OS) kurarken; Docker konteynerleri ana makinenin Linux çekirdeğini (Kernel) ortaklaşa kullanarak saniyeler içinde ayağa kalkar",
                        "C) Docker sadece mobilde çalışır",
                        "D) VM'lerin ücretsiz olması"
                    ],
                    "answer": "B",
                    "explanation": "Docker ana çekirdeği (Host Kernel) paylaştığı için çok daha az RAM harcar ve milisaniyeler içinde başlar."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the primary operational advantage of utilizing Multi-Stage Docker builds?",
                    "options": [
                        "A) Connecting additional hardware monitors",
                        "B) Stripping build toolchains, compilers, and cache files from the final production layer to minimize image size and attack surface",
                        "C) Mandatory compliance with C++ runtimes",
                        "D) Eliminating network requirements"
                    ],
                    "answer": "B",
                    "explanation": "Multi-stage builds leave compilation tools in discarded layers, yielding tiny, security-hardened production artifacts."
                },
                {
                    "question": "What is the architectural distinction between Docker containers and Virtual Machines?",
                    "options": [
                        "A) They are identical architectures",
                        "B) Virtual Machines package an entire guest operating system kernel, whereas containers virtualize at the process level sharing the host OS kernel",
                        "C) Docker is exclusive to mobile architectures",
                        "D) Virtual Machines require zero disk storage"
                    ],
                    "answer": "B",
                    "explanation": "Containers share the host operating system kernel, avoiding guest OS overhead and booting in fractions of a second."
                }
            ]
        },

        # Chapter 50
        {
            "id": 50,
            "section_id": 9,
            "slug_tr": "ch50_docker_compose_coklu_servis_gelistirme",
            "slug_en": "ch50_multi_service_stacks_docker_compose",
            "title_tr": "Docker Compose ile Çok Servisli Yerel Geliştirme Ortamı",
            "title_en": "Multi-Service Stacks with Docker Compose: One-Command Environments",
            "subtitle_tr": "Tek Bir 'docker compose up' Komutuyla Tüm Şirket Altyapısını Ayağa Kaldırmak",
            "subtitle_en": "Spinning Up Full-Stack Apps, PostgreSQL, and Redis in 10 Seconds via Code",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Yeni katıldığınız bir şirkette projeyi çalıştırmak için 3 gün boyunca PostgreSQL, Redis, RabbitMQ kurup boğuşmak mı, yoksa tek bir 'docker compose up' ile 1 dakikada kodlamaya başlamak mı?",
            "podcast_hook_en": "Why spend 3 days wrestling with manual database installations when Docker Compose scaffolds backend, database, and cache stacks in 15 seconds?",
            "takeaways_tr": [
                "Docker Compose, çoklu konteyner uygulamalarını tek bir YAML dosyasında (`compose.yaml`) tanımlayıp yönetme aracıdır.",
                "Konteynerler aynı Docker köprüsünde (bridge network) birbirlerine IP adresi yerine doğrudan servis adlarıyla (örn: `postgres:5432`) erişir.",
                "Named Volume'lar, konteynerler silinse veya yeniden başlatılsa bile veritabanı verilerinin kaybolmasını engeller."
            ],
            "takeaways_en": [
                "Docker Compose coordinates multi-container stacks (App, PostgreSQL, Redis) via a declarative `compose.yaml` specification.",
                "Containers on the shared Compose bridge network address each other using service names (`postgres:5432`) instead of hardcoded IPs.",
                "Named Volumes persist database storage across container teardowns and restarts."
            ],
            "story_tr": """Bir orkestrayı yönettiğinizi düşünün. 

Konser saati geldiğinde kemancıya *"Sen hazırlan"*, 10 dakika sonra piyaniste *"Sen gel"*, sonra davulcuya *"Sen ayarla"* derseniz konser fiyaskoyla sonuçlanır! 

Orkestra şefi sahneye çıkar, bagetini kaldırır: **"1, 2, 3, BAŞLA!"** dediği anda 50 müzisyen aynı anda tek bir armoniyle çalmaya başlar!

Docker Compose işte o orkestra şefidir!
- Backend sunucusu
- PostgreSQL veritabanı
- Redis önbelleği
- MailHog e-posta test sunucusu

`docker compose up` dediğiniz anda hepsi aynı saniyede ayağa kalkar, birbirine bağlanır ve siz anında kod yazmaya başlarsınız.""",
            "story_en": """Picture conducting a symphony orchestra.

If you phone the violinist saying: *"Warm up your strings"*, then 15 minutes later text the cellist: *"Come to the hall"*, and an hour later ask the percussionist to set up drums, you'll never start.

The maestro steps onto the podium, raises the baton, and gives the downbeat: 50 musicians strike the opening chord in unified harmony.

Docker Compose is that conductor:
- Node.js API
- PostgreSQL Database
- Redis In-Memory Cache
- MailHog SMTP sandbox

You run `docker compose up`, and the entire multi-service stack bootstraps, links network bridges, and accepts requests immediately.""",
            "mental_tr": """Docker Compose Ağ ve Veri Mimarisi:

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
```""",
            "mental_en": """The Docker Compose Network Topology:

```
[docker compose up]
         │
         ▼
┌────────────────────────────────────────────────────────┐
│             DOCKER COMPOSE BRIDGE NETWORK              │
│                                                        │
│   [Service: api] ──(postgres:5432)──> [Service: db]    │
│          │                                   │         │
│          │ (redis:6379)                      ▼         │
│          ▼                             [NAMED VOLUME]  │
│   [Service: cache]                     (postgres_data) │
│                                        (Durable Disk)  │
└────────────────────────────────────────────────────────┘
         │
 (Host Mapping: 3000:3000)
         ▼
[Local Browser: http://localhost:3000]
```""",
            "prompt_tr": """# ROL: DevOps ve Geliştirici Deneyimi (DevEx) Mimarı
Yerel geliştirme ortamımız için eksiksiz bir `compose.yaml` (Docker Compose) dosyası hazırlayacağız.

## GEREKSİNİMLER:
1. `app`: Mevcut Dockerfile'ı derlesin, 3000 portunu dışa açsın ve kod değişikliklerini anında yakalasın (volume mount).
2. `postgres`: PostgreSQL 16 Alpine kullansın, verileri `pg_data` named volume'unda saklasın ve sağlık kontrolü (healthcheck) içersin.
3. `redis`: Redis Alpine kullansın.
4. `app` servisi sadece PostgreSQL sağlık kontrolünden (healthy) geçtikten sonra başlasın (`depends_on`).""",
            "prompt_en": """# ROLE: DevEx & Infrastructure Automation Specialist
Author a declarative `compose.yaml` file for local development.

## REQUIREMENTS:
1. `api`: Builds local Dockerfile, maps port 3000, and mounts workspace code for hot-reloading.
2. `postgres`: PostgreSQL 16 Alpine, persists storage via `pg_data` named volume, includes health check.
3. `cache`: Redis Alpine.
4. `api` waits until `postgres` evaluates as healthy via `depends_on: condition: service_healthy`.""",
            "code_lang": "yaml",
            "code_naive": """# Kötü Compose Dosyası: Volume yok (veriler silinir), healthcheck yok, şifreler açık
services:
  db:
    image: postgres
  web:
    image: my-web-app
# db hazır olmadan web başlarsa bağlantı hatasıyla çöker!""",
            "code_robust": """services:
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
  pg_data: # Konteyner silinse bile veritabanı verisi diske kaydedilir!""",
            "code_notes_tr": "`depends_on: condition: service_healthy` sayesinde backend servisi veritabanı gerçekten hazır olana kadar bekleterek başlangıç çöküşlerini engeller; `pg_data` named volume ile veritabanı kalıcılığı garanti edilir.",
            "code_notes_en": "Using `condition: service_healthy` ensures the application never attempts to connect before PostgreSQL accepts sockets. The `pg_data` volume ensures data persists across container lifecycles.",
            "pitfalls_tr": [
                {"trap": "Konteyner içi bağlantılarda `localhost:5432` yazıp bağlanamamak.", "solution": "Konteynerler birbirine `localhost` ile değil, servis adıyla (`postgres:5432`) bağlanır."},
                {"trap": "Named volume kullanmayıp `docker compose down` yapınca tüm veritabanının silinmesi.", "solution": "Veritabanı servislerinde mutlaka kalıcı named volume tanımlayın."},
                {"trap": "Büyük projelerde `docker compose up` yapıp logları okuyamamak.", "solution": "`docker compose up -d` ile arka planda başlatıp sadece ilgilendiğiniz servisin loglarını izleyin (`docker compose logs -f app`)."}
            ],
            "pitfalls_en": [
                {"trap": "Configuring inter-service database hosts as `localhost:5432`.", "solution": "Containers connect across Compose networks via internal service identifiers (`postgres:5432`)."},
                {"trap": "Omitting named volumes, wiping the entire database on `docker compose down`.", "solution": "Mount database state to an explicitly declared named volume (`pg_data`)."},
                {"trap": "Getting overwhelmed by stdout noise from all services simultaneously.", "solution": "Run detached (`docker compose up -d`) and tail logs for specific targets (`docker compose logs -f api`)."}
            ],
            "udemy_title_tr": "Ders 50: Docker Compose - Tek Komutta Tüm Altyapı",
            "udemy_title_en": "Lecture 50: Multi-Service Stacks with Docker Compose",
            "udemy_slides_tr": [
                "Docker Compose nedir ve çoklu servisleri nasıl orkestre eder?",
                "Konteynerler arası iç ağ (Internal Network) ve servis adlandırma.",
                "Service Healthchecks ve depends_on ile sıralı başlatma.",
                "Canlı Demo: Tek komutla Next.js + Postgres + Redis ayağa kaldırmak."
            ],
            "udemy_slides_en": [
                "What is Docker Compose and how does it automate multi-tier stacks?",
                "Inter-container networking and service resolution.",
                "Health checks and deterministic startup ordering with `depends_on`.",
                "Live demo: Bootstrapping Next.js, PostgreSQL, and Redis in 15 seconds."
            ],
            "udemy_demo_tr": "Terminalde `docker compose up` çalıştırın. PostgreSQL'in sağlık kontrolünden geçip yeşil yandığını, ardından backend servisinin ayağa kalktığını gösterin. `docker compose down` ve tekrar `up` yaparak veritabanı kayıtlarının korunduğunu gösterin.",
            "udemy_demo_en": "Run `docker compose up`. Show the healthcheck polling until Postgres is ready, triggering the web app bootstrap. Run `docker compose down`, restart the stack, and demonstrate data persistence.",
            "action_task_tr": "Projeniz için bir `compose.yaml` dosyası oluşturun. İçine bir PostgreSQL ve bir Redis servisi ekleyip `docker compose up -d` ile ayağa kaldırın.",
            "action_task_en": "Author a `compose.yaml` file orchestrating a local database and cache, running the stack in detached mode.",
            "quiz_tr": [
                {
                    "question": "Docker Compose ağında bir backend servisi PostgreSQL veritabanına bağlanırken host adresi olarak ne yazmalıdır?",
                    "options": [
                        "A) localhost",
                        "B) 127.0.0.1",
                        "C) compose.yaml dosyasında PostgreSQL servisine verilen isim (Örn: `postgres` veya `db`)",
                        "D) Bilgisayarın MAC adresi"
                    ],
                    "answer": "C",
                    "explanation": "Docker Compose dahili DNS sunucusuna sahiptir; servisler birbirlerine doğrudan servis isimleriyle (örn: `postgres:5432`) erişir."
                },
                {
                    "question": "Docker Compose'da veritabanı servisinin hazır olmasını beklemek için hangi mekanizma kullanılır?",
                    "options": [
                        "A) setTimeout",
                        "B) `healthcheck` ve `depends_on: condition: service_healthy`",
                        "C) Bilgisayarı kapatıp açmak",
                        "D) Sadece `ports` tanımı"
                    ],
                    "answer": "B",
                    "explanation": "Healthcheck veritabanının soket bağlantılarını kabul ettiğini teyit eder; `depends_on` ise bağımlı servisi o an gelene kadar bekletir."
                }
            ],
            "quiz_en": [
                {
                    "question": "How does an application container resolve a PostgreSQL container on a Docker Compose network?",
                    "options": [
                        "A) `localhost`",
                        "B) `127.0.0.1`",
                        "C) By using the declared service name identifier (e.g., `postgres` or `db`)",
                        "D) Machine MAC addresses"
                    ],
                    "answer": "C",
                    "explanation": "Docker Compose deploys an embedded DNS resolver mapping service names directly to container IP addresses."
                },
                {
                    "question": "What configuration ensures an application container pauses until its database dependency is fully operational?",
                    "options": [
                        "A) Hardcoded `sleep 30` loops",
                        "B) A `healthcheck` definition combined with `depends_on: condition: service_healthy`",
                        "C) Restarting the Docker daemon",
                        "D) Standard port forwarding declarations"
                    ],
                    "answer": "B",
                    "explanation": "`service_healthy` conditions poll database socket readiness before spinning up dependent application processes."
                }
            ]
        },

        # Chapter 51
        {
            "id": 51,
            "section_id": 9,
            "slug_tr": "ch51_bulut_bilisime_giris_aws_gcp_azure",
            "slug_en": "ch51_cloud_essentials_aws_gcp_azure",
            "title_tr": "Bulut Bilişime Giriş: AWS, GCP ve Azure Temel Kavramları",
            "title_en": "Cloud 101: Compute, Storage & Networking Explained Simply",
            "subtitle_tr": "Kendi Sunucunu Yönetme Zahmetinden Bulutun Sınırsız Gücüne Geçiş",
            "subtitle_en": "Demystifying VMs, Object Storage, VPCs, and Load Balancers Without Jargon",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "AWS konsolunda 200'den fazla servis var. Junior bir mühendis bunların hepsini bilmek zorunda mı, yoksa sadece 4 temel yapı taşını bilmek yeterli mi?",
            "podcast_hook_en": "The AWS console catalogs over 200 distinct services. Does a junior engineer need to learn them all, or does mastering 4 core primitives unlock the cloud?",
            "takeaways_tr": [
                "Tüm bulut servisleri 4 ana yapı taşı üzerine kuruludur: Compute (İşlemci), Storage (Depolama), Database (Veritabanı) ve Networking (Ağ).",
                "EC2 kiralık sanal bir bilgisayardır; S3 sınırsız bir dosya deposudur; RDS yönetilen bir veritabanıdır.",
                "Bulut maliyetleri kullandıkça öde (Pay-as-you-go) modelidir; kapatılmayan test sunucuları devasa faturalar çıkarabilir."
            ],
            "takeaways_en": [
                "Every cloud platform converges on 4 primary primitives: Compute, Object Storage, Managed Databases, and Virtual Networks.",
                "EC2 is a virtual server instance; S3 is scalable object storage; RDS is an automated managed relational database.",
                "Cloud billing operates on pay-as-you-go models; orphaned, unmonitored test instances will exhaust engineering budgets."
            ],
            "story_tr": """Evinizde elektrik üretmek istediğinizi düşünün.

Bahçenize jeneratör kurup, her gün benzin alıp, motorun yağını değiştirip, gece sesinden uyuyamaz mıydınız? Tabii ki hayır! Duvardaki prize bir fiş takarsınız. Elektrik idaresi elektriği üretir, siz sadece ay sonunda harcadığınız kilovatsaat kadar fatura ödersiniz.

Bulut Bilişim (Cloud Computing) işte o elektrik prizidir!

Eskiden şirketler ofislerinin bodrum katına devasa sunucu odaları kurar, klima arızalarıyla boğuşur, hard disk değiştirirdi (On-Premise). 
Bugün AWS, Google Cloud veya Azure sayesinde tek tıkla dünyanın en güçlü veri merkezlerinden prizi takıyor ve sadece kullandığımız saniye kadar ödeme yapıyoruz.""",
            "story_en": """Consider how you power your home appliances.

Do you excavate your backyard, install a diesel turbine, source fuel, and service alternators? Of course not. You plug a cord into the wall outlet. The municipal electrical utility manages infrastructure, and you pay exclusively for consumed kilowatt-hours.

Cloud Computing is that electrical utility grid for compute infrastructure.

Historically, enterprises maintained on-premises server racks in basement closets, managing air conditioning and disk replacements.
Today, AWS, GCP, and Azure let you tap into global data centers with a single API call, paying strictly for consumed compute seconds.""",
            "mental_tr": """Bulutun 4 Temel Yapı Taşı Karşılaştırması:

| Yapı Taşı | AWS Karşılığı | GCP Karşılığı | Ne İşe Yarar? |
| :--- | :--- | :--- | :--- |
| **Compute (İşlem)** | EC2 / ECS / Lambda | Compute Engine / Cloud Run | Kodu çalıştıran sanal işlemciler ve RAM |
| **Storage (Depolama)**| S3 (Simple Storage) | Cloud Storage | Resimler, videolar, yedekler (Sınırsız nesne deposu) |
| **Database (Veri)** | RDS / Aurora / DynamoDB | Cloud SQL / Firestore | Otomatik yedeklenen, bakımı yapılan veritabanı |
| **Networking (Ağ)** | VPC / Route 53 / ALB | VPC / Cloud DNS / Load Balancing | Güvenlik duvarları, alan adı ve yük dengeleme |""",
            "mental_en": """The Cloud Primitives Rosetta Stone:

| Primitive | AWS Ecosystem | GCP Ecosystem | Core Mandate |
| :--- | :--- | :--- | :--- |
| **Compute** | EC2 / ECS / Lambda | Compute Engine / Cloud Run | Virtual CPUs and RAM executing application workloads |
| **Object Storage** | S3 | Cloud Storage | Scalable, highly durable storage for static media and backups |
| **Managed DB** | RDS / Aurora | Cloud SQL / AlloyDB | Automated database provisioning, patching, and backups |
| **Networking** | VPC / ALB / Route 53 | Cloud VPC / Load Balancing | Virtual networks, subnets, DNS, and traffic routing |""",
            "prompt_tr": """# ROL: Bulut Çözüm Mimarı (AWS Certified Solutions Architect)
Bir startup'ın ilk web uygulamasını AWS üzerinde ayağa kaldıracağız.

## GEREKSİNİMLER:
- 1 adet Docker konteynerinde çalışan Node.js API
- 1 adet PostgreSQL veritabanı
- Kullanıcı profil fotoğraflarının yükleneceği dosya deposu

## GÖREV:
1. En ucuz ve yönetimi en kolay AWS servis kombinasyonunu öner (Örn: App Runner / ECS Fargate + RDS + S3).
2. S3 bucket'ına dosya yüklerken güvenliği sağlayan 'Presigned URL' mimarisini açıkla.
3. Maliyet alarmı (AWS Budget Alert) kurmanın adımlarını özetle.""",
            "prompt_en": """# ROLE: AWS Solutions Architect
We are deploying an early-stage startup workload onto AWS.

## REQUIREMENTS:
- Containerized Node.js API
- Managed PostgreSQL database
- Storage bucket for user avatar uploads

## TASK:
1. Recommend an operational, cost-effective service blueprint (e.g., AWS App Runner / ECS Fargate + RDS Postgres + S3).
2. Detail the secure file upload pattern using S3 Presigned URLs.
3. Specify AWS Budget alarm thresholds to prevent runaway infrastructure bills.""",
            "code_lang": "typescript",
            "code_naive": """// Kötü Bulut Mimarisi: Kullanıcı resimlerini doğrudan web sunucusunun diskine kaydetmek
// Sunucu yeniden başladığında veya 2. sunucu açıldığında tüm resimler kaybolur!
app.post("/upload", (req, res) => {
  fs.writeFileSync(`/var/www/uploads/${req.body.name}`, req.body.file);
});""",
            "code_robust": """import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";
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
}""",
            "code_notes_tr": "Presigned URL deseni sayesinde kullanıcı dosyayı web sunucunuza değil, doğrudan S3'e yükler. Web sunucunuzun işlemcisi ve belleği dosya yükleme trafiğiyle boğulmaz.",
            "code_notes_en": "The Presigned URL pattern authorizes clients to stream media directly to S3 buckets, bypassing the application server entirely and preserving backend CPU threads.",
            "pitfalls_tr": [
                {"trap": "Kullanıcı dosyalarını sunucunun yerel diskine kaydetmek (Konteyner kapanınca silinir!).", "solution": "Statik medyayı daima S3 veya Google Cloud Storage gibi Nesne Depolarında (Object Storage) saklayın."},
                {"trap": "AWS hesabında bütçe alarmı (Budget Alert) kurmayı unutmak.", "solution": "İlk gün 10$ ve 50$ eşiklerinde e-posta gönderen bir bütçe alarmı kurun."},
                {"trap": "S3 bucket'larını internete tamamen açık (Public Read/Write) bırakıp veri sızdırmak.", "solution": "Bucket'larda 'Block Public Access' ayarını açık tutun; erişimi Presigned URL ile sınırlayın."}
            ],
            "pitfalls_en": [
                {"trap": "Writing uploaded files to the local ephemeral container filesystem.", "solution": "Always route media persistence to decoupled Object Storage (S3 / GCS)."},
                {"trap": "Neglecting to configure AWS Budget alarms upon account creation.", "solution": "Set billing thresholds immediately ($10 and $50 alarms) with SMS/email notifications."},
                {"trap": "Disabling S3 bucket public access blocks, exposing private assets.", "solution": "Keep 'Block Public Access' enabled; expose private assets strictly via short-lived Presigned URLs."}
            ],
            "udemy_title_tr": "Ders 51: Bulut Bilişim 101 - AWS, GCP ve Temel Yapı Taşları",
            "udemy_title_en": "Lecture 51: Cloud 101 - Demystifying AWS, GCP & Core Primitives",
            "udemy_slides_tr": [
                "Neden artık kimse bodrumda sunucu kurmuyor? Bulutun gücü.",
                "4 Temel Taş: Compute, Storage, Database, Networking.",
                "S3 Presigned URL ile sunucuyu yormadan güvenli dosya yükleme.",
                "AWS Bütçe Alarmları ile sürpriz faturalardan korunmak."
            ],
            "udemy_slides_en": [
                "The death of on-premise server closets: The utility model.",
                "The 4 core cloud primitives unpacked.",
                "Presigned URLs: Offloading binary file uploads directly to S3.",
                "Configuring billing alarms to avoid surprise cloud invoices."
            ],
            "udemy_demo_tr": "AWS konsoluna girin (veya LocalStack ile simüle edin). S3 üzerinde bir bucket açın. Node.js SDK ile 15 saniyede bir presigned URL üretip curl ile dosyayı doğrudan S3'e yüklemeyi canlı gösterin.",
            "udemy_demo_en": "Generate an S3 Presigned URL via the AWS SDK. Execute a `curl -X PUT` command pushing an image directly into the S3 bucket, verifying immediate presence in the storage console.",
            "action_task_tr": "AWS veya Google Cloud hesabınızda ilk bütçe alarmınızı (Budget Alert: 10$) kurun ve bildirim e-postanızı ekleyin.",
            "action_task_en": "Configure a $10 billing alert on your personal cloud account with email notifications.",
            "quiz_tr": [
                {
                    "question": "AWS S3 (Simple Storage Service) gibi Nesne Depoları (Object Storage) geleneksel sunucu disklerinden hangi özelliğiyle ayrılır?",
                    "options": [
                        "A) Sadece müzik saklayabilmesi",
                        "B) Sınırsız depolama kapasitesi sunması, yüksek dayanıklılık (%99.999999999) sağlaması ve dosyalara doğrudan HTTP üzerinden erişilebilmesi",
                        "C) Bilgisayara takılan bir USB bellek olması",
                        "D) Sadece Python ile çalışması"
                    ],
                    "answer": "B",
                    "explanation": "S3, sabit disk boyutu kısıtlaması olmadan petabaytlarca veriyi güvenle ve yüksek dayanıklılıkla saklayan dağıtık bir nesne deposudur."
                },
                {
                    "question": "Bir web uygulamasında dosya yüklerken 'Presigned URL' kullanmanın sağladığı en büyük mimari fayda nedir?",
                    "options": [
                        "A) Dosyanın rengini değiştirmesi",
                        "B) İstemcinin dosyayı doğrudan S3'e yüklemesini sağlayarak backend sunucusunun işlemci, bellek ve bant genişliği darboğazına girmesini engellemesi",
                        "C) Sadece Chrome'da çalışması",
                        "D) Veritabanını silmesi"
                    ],
                    "answer": "B",
                    "explanation": "Presigned URL, dosya trafiğini uygulama sunucusundan arındırarak yükü doğrudan S3 altyapısına devreder."
                }
            ],
            "quiz_en": [
                {
                    "question": "What primary capability distinguishes Object Storage (e.g., AWS S3) from traditional block storage volumes?",
                    "options": [
                        "A) Restricting storage strictly to audio files",
                        "B) Providing theoretically limitless capacity, high durability (11 9s), and direct HTTP/HTTPS addressing",
                        "C) Requiring physical USB connections",
                        "D) Operating exclusively with Python"
                    ],
                    "answer": "B",
                    "explanation": "Object storage stores arbitrary binary payloads at massive scale, reachable via signed REST endpoints without filesystem volume limits."
                },
                {
                    "question": "What is the primary architectural payoff of utilizing S3 Presigned URLs for file uploads?",
                    "options": [
                        "A) Enhancing image color profiles",
                        "B) Allowing clients to upload directly to S3 buckets, freeing backend servers from memory, CPU, and bandwidth bottlenecks",
                        "C) Chrome browser exclusivity",
                        "D) Automating table drops"
                    ],
                    "answer": "B",
                    "explanation": "Presigned URLs grant temporary write authorization directly to storage buckets, offloading heavy binary I/O from backend application instances."
                }
            ]
        },

        # Chapter 52
        {
            "id": 52,
            "section_id": 9,
            "slug_tr": "ch52_sunucusuz_serverless_ve_edge_computing",
            "slug_en": "ch52_serverless_functions_and_edge_runtimes",
            "title_tr": "Sunucusuz (Serverless) Mimariler & Edge Computing",
            "title_en": "Serverless Functions & Edge Runtimes: Beyond Traditional Servers",
            "subtitle_tr": "Sıfır Sunucu Yönetimi, Soğuk Başlangıçlar (Cold Start) ve Küresel Dağıtım",
            "subtitle_en": "Conquering Cold Starts, Stateless Compute, and Sub-10ms Edge Responses",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Serverless mimaride gerçekten 'sunucu yok' mu? AWS Lambda ve Vercel Edge Functions kodu dünyanın dört bir yanındaki kullanıcılara 5 milisaniyede nasıl ulaştırır?",
            "podcast_hook_en": "Is 'Serverless' genuinely serverless? How do edge runtimes execute stateless code 5 milliseconds away from global users without spinning up virtual machines?",
            "takeaways_tr": [
                "Serverless 'sunucusuz' demek değildir; sunucuların yönetimini ve ölçeklenmesini bulut sağlayıcısına devretmektir.",
                "Kullanılmadığında 0 maliyet üretir; trafik geldiğinde saniyenin onda birinde otomatik olarak 1'den 10.000 örneğe fırlar.",
                "Soğuk Başlangıç (Cold Start) sorununu aşmak için hafif edge çalışma zamanları (Cloudflare Workers / Vercel Edge) tercih edilmelidir."
            ],
            "takeaways_en": [
                "Serverless does not mean absence of servers; it means abstracting server provisioning and automated scaling to the cloud provider.",
                "Scale-to-zero economics: idle functions incur zero compute cost, bursting to 10,000 parallel instances on traffic spikes.",
                "Mitigate Cold Starts by targeting lightweight V8 isolate edge runtimes (Cloudflare Workers, Vercel Edge)."
            ],
            "story_tr": """Bir taksi durağını ve kiralık bir arabayı düşünün.

Eğer bir araba kiralarsanız (Geleneksel Sunucu / EC2): Arabayı sürseniz de, garajda park halinde dursa da her ay 1000 dolar kira ödersiniz.

Peki ya taksi çağırırsanız (Serverless / Lambda)? Taksi kapınıza gelir, sizi gitmek istediğiniz yere götürür ve sadece gittiğiniz kilometre kadar ücret ödersiniz. Taksi bittikten sonra gider; arabanın vergisiyle, sigortasıyla, bakımıyla siz uğraşmazsınız!

Edge Computing ise durağın hemen her köşe başında olmasıdır: Taksi 30 saniye içinde kapınızdadır!

Günde sadece 50 istek alan bir servis için ayda 50 dolar sunucu parası ödemek yerine, serverless ile ayda 0.01 dolar ödersiniz.""",
            "story_en": """Consider renting a car versus hailing an on-demand ride.

Leasing a vehicle (Traditional Dedicated Server / EC2): Whether driving on the highway or parked in your garage for weeks, you pay a flat monthly lease fee.

Hailing a ride (Serverless / AWS Lambda): The vehicle arrives on demand, transports you across town, and charges you strictly for elapsed trip seconds. When you exit, the car departs. You never service its transmission or pay for garage storage.

Edge Computing is having rides idling at every street corner: the vehicle arrives at your curb in 30 seconds.

For an API receiving 50 requests daily, why pay $40 monthly for an idle virtual machine when Serverless costs $0.001?""",
            "mental_tr": """Geleneksel Sunucu vs Serverless vs Edge:

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
```""",
            "mental_en": """The Compute Paradigm Continuum:

```
┌────────────────────────────────────────────────────────┐
│               COMPUTE PARADIGM SPECTRUM                │
└──────────────────────────┬─────────────────────────────┘
                           │
       ┌───────────────────┼───────────────────┐
       ▼                   ▼                   ▼
[TRADITIONAL VM / EC2] [SERVERLESS LAMBDA]    [EDGE ISOLATES]
- 24/7 billing baseline - Invocations scale-to-zero - Runs at CDN points of presence
- Full Node / OS kernel - Cold start: 200-800ms   - Cold start: < 5ms (V8 isolates)
- Zero cold start       - Regional data center    - Globally distributed (300 cities)
```""",
            "prompt_tr": """# ROL: Serverless ve Edge Mimarı
Vercel Edge Functions veya Cloudflare Workers kullanarak küresel ölçekte çalışan bir 'Geolokasyon Yönlendirme Servisi' yazacağız.

## GÖREV:
1. Kullanıcının hangi ülkeden geldiğini tespit eden bir Edge Function kodu yaz.
2. V8 Isolate mimarisinin neden Node.js sanal makinelerine göre 100 kat daha hızlı ayağa kalktığını açıkla.
3. Serverless fonksiyonlarda veritabanı bağlantı havuzu (Connection Pooling) patlamasını önlemek için Prisma Accelerate / Neon Serverless kullanımını özetle.""",
            "prompt_en": """# ROLE: Serverless & Edge Systems Specialist
We are architecting a latency-critical geolocation redirection service using Edge Runtimes.

## TASK:
1. Implement an Edge Function inspecting geolocation headers and returning localized responses.
2. Explain how V8 isolates boot 100x faster than full Node.js container environments.
3. Detail how to prevent database connection exhaustion in serverless environments via pooling proxies (Prisma Accelerate / PgBouncer).""",
            "code_lang": "typescript",
            "code_naive": """// Kötü Serverless Kullanımı: Her fonksiyon çağrısında yeni DB bağlantısı açmak
// 1000 eşzamanlı istek geldiğinde veritabanının bağlantı havuzu (Max Connections) patlar!
import { Client } from 'pg';

export async function handler() {
  const client = new Client(process.env.DB_URL);
  await client.connect(); // HATA: Her lambdada yeni bağlantı açılırsa PostgreSQL çöker!
  const res = await client.query('SELECT * FROM config');
  await client.end();
  return res.rows;
}""",
            "code_robust": """// Modern Edge Fonksiyonu: Sub-10ms Gecikme ile Küresel Yürütme (api/geo.ts)

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
}""",
            "code_notes_tr": "`runtime: 'edge'` direktifi ile kod standart ağır container yerine Cloudflare/Vercel V8 Isolate motorunda koşar. Dünyanın neresinden istek gelirse gelsin kullanıcıya en yakın veri merkezinde 5 milisaniyede yanıt üretilir.",
            "code_notes_en": "Specifying `runtime: 'edge'` executes this handler within lightweight V8 isolates stationed at global CDN points of presence, delivering personalized responses in under 5 milliseconds.",
            "pitfalls_tr": [
                {"trap": "Serverless fonksiyonlarda veritabanı bağlantı havuzu (Connection Pooler) kullanmamak.", "solution": "Sunucusuz ortamlarda daima PgBouncer, Prisma Accelerate veya Neon gibi HTTP bağlantı havuzlayıcıları kullanın."},
                {"trap": "Büyük ve uzun süren (>15 dakika) işlemleri Serverless fonksiyonlarda çalıştırmaya çalışmak.", "solution": "Uzun süren işler (video işleme, büyük veri) için Lambda yerine arka plan işçileri (ECS/SQS) kullanın."},
                {"trap": "Edge fonksiyonlarında Node.js'e özel modülleri (örn: `fs` veya `child_process`) çağırmak.", "solution": "Edge çalışma zamanları standart Web API'lerini (fetch, Request, Response) destekler; dosya sistemi modüllerini çağırmayın."}
            ],
            "pitfalls_en": [
                {"trap": "Directly connecting serverless functions to relational databases without a connection pooler.", "solution": "Always route serverless queries through connection proxies (PgBouncer, Prisma Accelerate, Neon)."},
                {"trap": "Executing long-running background tasks (>15 minutes) inside ephemeral functions.", "solution": "Serverless functions enforce hard timeouts; dispatch long-running jobs to queues and dedicated worker containers."},
                {"trap": "Importing Node-specific modules (`fs`, `net`, `child_process`) inside Edge runtimes.", "solution": "Edge isolates adhere strictly to Web Standard APIs (`fetch`, `Request`, `Crypto`); avoid Node built-ins."}
            ],
            "udemy_title_tr": "Ders 52: Serverless ve Edge Computing - Sunucusuz Gelecek",
            "udemy_title_en": "Lecture 52: Serverless & Edge Runtimes - Sub-10ms Computing",
            "udemy_slides_tr": [
                "Serverless nedir? Sıfır maliyetten küresel ölçeğe geçiş.",
                "Cold Start problemi ve V8 Isolate mimarisi.",
                "Edge Runtimes: Kullanıcının 5 milisaniye yanında kod çalıştırmak.",
                "Serverless veritabanı bağlantı havuzu yönetimi (Connection Pooling)."
            ],
            "udemy_slides_en": [
                "Demystifying serverless: Scale-to-zero economics.",
                "The Cold Start dilemma and V8 isolate architecture.",
                "Edge runtimes: Executing compute 5 milliseconds from the end user.",
                "Managing database connection pools in ephemeral environments."
            ],
            "udemy_demo_tr": "Vercel üzerinde basit bir Edge Function deploy edin. Farklı ülkelerden VPN ile istek atarak yanıt süresinin her ülkede 10 milisaniye altında kaldığını ve x-vercel-ip-country başlığının doğru çalıştığını canlı gösterin.",
            "udemy_demo_en": "Deploy an Edge function. Query it through global VPN endpoints: demonstrate sub-10ms response latencies worldwide while inspecting edge headers.",
            "action_task_tr": "Next.js veya Cloudflare Workers projenizde basit bir Edge rotası oluşturun ve kullanıcının istek başlıklarını inceleyin.",
            "action_task_en": "Deploy a lightweight Edge Function in Next.js or Cloudflare Workers that outputs the client's country header.",
            "quiz_tr": [
                {
                    "question": "Serverless (Sunucusuz) mimarinin geleneksel sanal makinelere (VM) göre en büyük ekonomik avantajı nedir?",
                    "options": [
                        "A) Elektrik faturası ödememek",
                        "B) 'Scale-to-Zero' (Sıfıra Ölçeklenme) özelliği sayesinde hiç istek gelmediğinde 0 TL maliyet üretmesi; sadece çağrıldığı saniyeler için ödeme yapılması",
                        "C) Sadece C++ dilinde çalışması",
                        "D) Kodların silinmesi"
                    ],
                    "answer": "B",
                    "explanation": "Serverless servisler kullanılmadığı anlarda tamamen kapanır ve sıfır maliyet yaratır; trafik geldiğinde ise milisaniyeler içinde ayağa kalkar."
                },
                {
                    "question": "Serverless fonksiyonlarda 'Cold Start' (Soğuk Başlangıç) ne demektir?",
                    "options": [
                        "A) Sunucunun kışın donması",
                        "B) Uzun süre çağrılmayan bir fonksiyon ilk kez tetiklendiğinde bulut sağlayıcının yeni bir mikro-konteyner ayağa kaldırması sebebiyle ilk istekte yaşanan küçük gecikme",
                        "C) Bilgisayarın fanının çalışması",
                        "D) Kodun derlenememesi"
                    ],
                    "answer": "B",
                    "explanation": "Boştaki fonksiyonlar uyutulur. Yeni bir istek geldiğinde ortamın sıfırdan başlatılması birkaç yüz milisaniyelik soğuk başlangıç gecikmesine yol açar."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the primary economic advantage of Serverless architectures over dedicated virtual machines?",
                    "options": [
                        "A) Bypassing regional sales tax",
                        "B) Scale-to-Zero economics: incurring zero cost during idle periods, billing strictly for consumed compute fractions",
                        "C) Exclusive compatibility with C++ runtimes",
                        "D) Automated repository deletion"
                    ],
                    "answer": "B",
                    "explanation": "Serverless environments decommission idle capacity entirely, eliminating baseline infrastructure costs during periods of zero traffic."
                },
                {
                    "question": "What specifically is a 'Cold Start' in serverless computing?",
                    "options": [
                        "A) Sub-zero data center ambient temperatures",
                        "B) The latency penalty incurred when a provider boots a fresh container instance to serve an invocation following an idle period",
                        "C) Server cooling fan initialization",
                        "D) Compilation syntax failure"
                    ],
                    "answer": "B",
                    "explanation": "When an idle function receives traffic, the cloud provider must spin up an execution context, introducing an initial initialization latency."
                }
            ]
        },

        # Chapter 53
        {
            "id": 53,
            "section_id": 9,
            "slug_tr": "ch53_infrastructure_as_code_terraform",
            "slug_en": "ch53_infrastructure_as_code_with_ai_terraform",
            "title_tr": "Infrastructure as Code (IaC): Terraform ve Pulumi'ye AI Bakışı",
            "title_en": "Infrastructure as Code: Writing Terraform & Pulumi with AI",
            "subtitle_tr": "Bulut Konsolunda Elle Tıklamayı Bırakıp Altyapıyı Kod Olarak Sürümlemek",
            "subtitle_en": "Retiring 'ClickOps' and Managing Cloud Fleets via Version-Controlled Declarative Code",
            "level_tr": "İleri Seviye",
            "level_en": "Advanced",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "AWS konsolunda fareyle tıklayarak sunucu açmak (ClickOps) neden şirketler için saatli bir bombadır ve Terraform altyapıyı nasıl silinip yeniden kurulabilir kılar?",
            "podcast_hook_en": "Why is configuring cloud infrastructure via manual console clicks ('ClickOps') an unmitigated disaster waiting to happen, and how does Terraform make infrastructure repeatable?",
            "takeaways_tr": [
                "ClickOps (Konsolda elle tıklayarak altyapı kurmak) belgelenemez, tekrarlanamaz ve insan hatasına davetiye çıkarır.",
                "Infrastructure as Code (IaC), sunucuları, veritabanlarını ve güvenlik duvarlarını tıpkı uygulama kodu gibi Git'te versiyonlamaktır.",
                "Terraform'un `plan` komutu, gerçek buluta dokunmadan önce hangi kaynakların oluşturulacağını veya silineceğini önizleme imkanı sunar."
            ],
            "takeaways_en": [
                "'ClickOps'—manually clicking cloud console buttons—creates unreplicable infrastructure snowflakes and invites human error.",
                "Infrastructure as Code (IaC) models servers, databases, and networks as declarative code checked into version control.",
                "Terraform's `plan` phase generates an exact execution preview, eliminating guesswork before applying changes to production."
            ],
            "story_tr": """Bir şehir kurduğunuzu hayal edin.

Belediye başkanı sokakları, su borularını ve elektrik hatlarını mühendislerin aklına estikçe elle kazarak yapmasına izin verirse ne olur? 6 ay sonra kimse hangi borunun nereden geçtiğini bilmez! Yeni bir bina yapmak için kazmayı vurduğunuz an ana su borusunu patlatırsınız! İşte konsolda elle tıklayarak sunucu kurmak (**ClickOps**) tam olarak bu kaostur.

**Infrastructure as Code (Terraform)** ise o şehrin 3 boyutlu CAD mimari planıdır.

Tek bir dosyada:
- 1 adet PostgreSQL veritabanı
- 2 adet yük dengeleyici
- 1 adet S3 depolama alanı
kod olarak yazılır. Şehir bir depremde yıkılsa bile tek bir komutla (`terraform apply`) 5 dakikada tüm şehri başka bir kıtada birebir yeniden inşa edebilirsiniz!""",
            "story_en": """Imagine building a metropolis.

If municipal workers bury water mains, high-voltage lines, and fiber cables wherever they feel like on a given morning without blueprints, within 6 months nobody knows what lies beneath the pavement. The next excavator slices the main power grid. That is **ClickOps**.

**Infrastructure as Code (Terraform)** is the master digital blueprint.

Declared in declarative code:
- One PostgreSQL cluster
- Two Application Load Balancers
- One private S3 bucket
If a regional data center suffers a catastrophic power outage, running `terraform apply` reconstructs the entire infrastructure in a secondary region within 10 minutes.""",
            "mental_tr": """Terraform Çalışma Döngüsü:

```
[main.tf Kodunu Yaz]
         │
         ▼
[1. terraform init] ──> Bulut sağlayıcı eklentilerini (AWS Provider) indirir.
         │
         ▼
[2. terraform plan] ──> "Neler değişecek?" (Önizleme yapar, ASLA değişiklik yapmaz!)
         │
         ▼
[3. terraform apply] ──> Gerçek buluta gider ve kaynakları inşa eder!
         │
         ▼
[terraform.tfstate] ──> Bulutun mevcut durumunu hafızasında tutan kilit dosya.
```""",
            "mental_en": """The Terraform Operational Workflow:

```
[Author `main.tf` Declarations]
              │
              ▼
[1. terraform init]  ──> Downloads required provider plugins (AWS / GCP / Azure).
              │
              ▼
[2. terraform plan]  ──> Forensic dry-run preview: asserts mutations without executing.
              │
              ▼
[3. terraform apply] ──> Executes real API calls to provision cloud resources.
              │
              ▼
[terraform.tfstate]  ──> Authoritative state ledger mapping code to live cloud IDs.
```""",
            "prompt_tr": """# ROL: DevSecOps ve Terraform Mimarı
AWS altyapımız için Terraform (HCL) kodu yazacağız.

## GÖREV:
Aşağıdaki altyapıyı oluşturan modüler bir `main.tf` hazırla:
1. Şifrelenmiş (AES-256) ve public erişime kapalı bir AWS S3 bucket'ı.
2. Bu bucket'a dosya yüklendiğinde versiyonlamayı (versioning) aktif et.
3. Altyapıyı test etmek için `terraform plan` çıktısının nasıl okunacağını açıkla.""",
            "prompt_en": """# ROLE: Infrastructure as Code & Terraform Specialist
Author a modular Terraform (HCL) specification for an AWS storage module.

## TASK:
Deliver a production-grade `main.tf`:
1. Provision a private AWS S3 bucket with server-side encryption enabled (AES-256).
2. Enforce strict public access blocks.
3. Enable bucket versioning to protect against accidental deletions.""",
            "code_lang": "hcl",
            "code_naive": """# Kötü Terraform: Güvensiz, şifreleme yok, public erişim açık!
resource "aws_s3_bucket" "insecure_bucket" {
  bucket = "sirket-gizli-veriler"
  # Şifreleme yok, versiyonlama yok!
}""",
            "code_robust": """# Profesyonel ve Güvenli Terraform Mimarisi (main.tf)

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# 1. S3 Depolama Alanı
resource "aws_s3_bucket" "secure_assets" {
  bucket        = "sirket-guvenli-depo-${var.environment}"
  force_destroy = false

  tags = {
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}

# 2. Versiyonlama Koruması (Yanlışlıkla silinmeyi önler)
resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.secure_assets.id
  versioning_configuration {
    status = "Enabled"
  }
}

# 3. Sunucu Taraflı Şifreleme (AES-256)
resource "aws_s3_bucket_server_side_encryption_configuration" "crypto" {
  bucket = aws_s3_bucket.secure_assets.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# 4. İnternete Tamamen Kapat (Block Public Access)
resource "aws_s3_bucket_public_access_block" "public_block" {
  bucket = aws_s3_bucket.secure_assets.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}""",
            "code_notes_tr": "Altyapı kodla tanımlandığı için şifreleme, versiyonlama ve public erişim kilidi gibi güvenlik standartları zorunlu kılınmış; insan dalgınlığıyla açık bir S3 bucket bırakma riski sıfırlanmıştır.",
            "code_notes_en": "Codifying storage via Terraform guarantees encryption, object versioning, and public-access blocks by default, completely eliminating human configuration drift.",
            "pitfalls_tr": [
                {"trap": "`terraform.tfstate` dosyasını GitHub'a commit etmek (Şifreler ve API anahtarları içerebilir!).", "solution": "State dosyasını daima AWS S3 ve DynamoDB kilitli uzak backend'de (Remote Backend) saklayın."},
                {"trap": "`terraform plan` çıktısını okumadan körü körüne `terraform apply` çalıştırmak.", "solution": "Plan çıktısındaki kırmızı silme (`- destroy`) uyarılarını mutlaka tek tek inceleyin."},
                {"trap": "Konsoldan (ClickOps) elle değişiklik yapıp Terraform koduyla uyumsuzluk (Drift) yaratmak.", "solution": "Bir kaynak Terraform ile yönetiliyorsa, konsoldan elle müdahaleyi kesinlikle yasaklayın."}
            ],
            "pitfalls_en": [
                {"trap": "Committing local `terraform.tfstate` files to Git (they contain plaintext cloud secrets).", "solution": "Store state files in remote encrypted backends (S3 with DynamoDB state locking)."},
                {"trap": "Running `terraform apply` without auditing the preceding `terraform plan` output.", "solution": "Always review plan diffs for unexpected resource destructions (`- destroy`)."},
                {"trap": "Manually tweaking settings in the cloud console, inducing Configuration Drift.", "solution": "Once codified in Terraform, strictly prohibit out-of-band ClickOps edits."}
            ],
            "udemy_title_tr": "Ders 53: Infrastructure as Code - Terraform ile Bulutu Kodlamak",
            "udemy_title_en": "Lecture 53: Infrastructure as Code - Cloud Automation via Terraform",
            "udemy_slides_tr": [
                "ClickOps felaketi: Neden konsolda elle tıklamak yasaklanmalıdır?",
                "IaC felsefesi: Altyapıyı Git ile versiyonlamak.",
                "Terraform yaşam döngüsü: init, plan, apply, destroy.",
                "Canlı Demo: 60 saniyede kodla AWS S3 bucket ayağa kaldırmak."
            ],
            "udemy_slides_en": [
                "The ClickOps catastrophe: Why manual console edits destroy reliability.",
                "The Infrastructure as Code paradigm: Versioning topologies in Git.",
                "The Terraform lifecycle: `init`, `plan`, `apply`, `destroy`.",
                "Live demo: Provisioning an encrypted S3 bucket in 60 seconds with Terraform."
            ],
            "udemy_demo_tr": "Bir `main.tf` dosyası oluşturun. `terraform init` ve `terraform plan` çalıştırın. Terminalde yeşil `+ create` satırlarını gösterin. `terraform apply` diyerek AWS'de (veya LocalStack'te) saniyeler içinde kaynağın oluştuğunu gösterin.",
            "udemy_demo_en": "Execute `terraform init` followed by `terraform plan`. Walk through the execution summary showing planned resource additions, then execute `terraform apply` to provision the resource live.",
            "action_task_tr": "Bilgisayarınıza Terraform kurun (`brew install terraform`) ve LocalStack veya AWS kullanarak basit bir depolama alanı oluşturan ilk `.tf` dosyanızı yazıp `terraform plan` alın.",
            "action_task_en": "Install Terraform CLI and execute `terraform plan` against a simple local storage configuration.",
            "quiz_tr": [
                {
                    "question": "Terraform'da `terraform plan` komutunun temel işlevi nedir?",
                    "options": [
                        "A) Buluttaki tüm sunucuları silmek",
                        "B) Yazılan kod ile bulutun mevcut durumunu karşılaştırarak, hangi kaynakların ekleneceğini, değiştirileceğini veya silineceğini buluta DOKUNMADAN güvenle önizlemek",
                        "C) Sadece fatura miktarını hesaplamak",
                        "D) Bilgisayarı kapatmak"
                    ],
                    "answer": "B",
                    "explanation": "`terraform plan`, altyapı üzerinde hiçbir yıkıcı işlem yapmadan önce geliştiriciye tam bir değişiklik önizlemesi (dry-run) sunar."
                },
                {
                    "question": "Terraform'un ürettiği `terraform.tfstate` dosyasını neden public bir Git reposuna commit etmemeliyiz?",
                    "options": [
                        "A) Dosya çok büyük olduğu için",
                        "B) State dosyasının veritabanı şifreleri, API anahtarları gibi hassas bilgileri düz metin olarak içerebilmesi ve güvenlik açığı yaratması",
                        "C) Sadece Linux'ta çalışması",
                        "D) Kodun derlenmesini engellemesi"
                    ],
                    "answer": "B",
                    "explanation": "Terraform state dosyası buluttaki kaynakların tüm detaylarını (şifreler dahil) tutar; bu nedenle daima şifrelenmiş uzak backend'lerde (S3 vb.) saklanmalıdır."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the primary function of the `terraform plan` command?",
                    "options": [
                        "A) Deleting cloud infrastructure",
                        "B) Generating an execution preview comparing code against live state to declare which resources will be added, altered, or destroyed without modifying cloud state",
                        "C) Calculating estimated cloud costs",
                        "D) Powering down runner instances"
                    ],
                    "answer": "B",
                    "explanation": "`terraform plan` serves as a read-only speculative execution preview, ensuring visibility prior to executing mutations."
                },
                {
                    "question": "Why must `terraform.tfstate` files never be committed to public Git repositories?",
                    "options": [
                        "A) They exceed GitHub file size caps",
                        "B) They often store sensitive cloud metadata and database passwords in plaintext",
                        "C) They execute strictly on Linux runtimes",
                        "D) They break TypeScript compilation"
                    ],
                    "answer": "B",
                    "explanation": "State files store live configuration metadata, including sensitive secrets and database connection strings, mandating encrypted remote backends."
                }
            ]
        },

        # Chapter 54
        {
            "id": 54,
            "section_id": 9,
            "slug_tr": "ch54_sifir_kesintili_dagitim_blue_green_canary",
            "slug_en": "ch54_zero_downtime_deployment_blue_green_canary",
            "title_tr": "Sıfır Kesintili Dağıtım (Zero-Downtime Deployment): Blue-Green & Canary",
            "title_en": "Zero-Downtime Deployments: Blue-Green, Canary & Automated Rollbacks",
            "subtitle_tr": "Cuma Akşamı Bile Korkusuzca Deploy Çıkma Sanatı",
            "subtitle_en": "Shipping Software on Friday Afternoons Without Breaking Production Traffic",
            "level_tr": "İleri Seviye",
            "level_en": "Advanced",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Milyonlarca kullanıcısı olan bir banka veya e-ticaret sitesi yeni versiyon yayınlarken 'Sitemiz bakım nedeniyle kapalıdır' yazısı koyamaz! Sıfır kesinti nasıl sağlanır?",
            "podcast_hook_en": "Global payment gateways cannot show a 'Down for Maintenance' banner during deployments. How do Blue-Green and Canary pipelines swap traffic invisibly?",
            "takeaways_tr": [
                "Zero-Downtime Deployment, kullanıcılar hiçbir kesinti yaşamadan yeni sürümün yayına alınmasıdır.",
                "Blue-Green Dağıtım: Eski sürüm (Blue) ve yeni sürüm (Green) yan yana çalışır; yönlendirici tek bir anahtarla trafiği yeniye aktarır.",
                "Canary (Kanarya) Dağıtım: Yeni sürüm önce kullanıcıların sadece %5'ine sunulur; hata yoksa kademeli olarak %100'e çıkarılır."
            ],
            "takeaways_en": [
                "Zero-Downtime Deployment ensures end users never experience dropouts or maintenance windows during releases.",
                "Blue-Green Deployment provisions duplicate identical production clusters; a router shifts 100% of traffic atomically.",
                "Canary Deployments expose novel releases incrementally (1% -> 10% -> 100%), rolling back instantly if error rates spike."
            ],
            "story_tr": """Eski zamanlarda kömür madencilerini düşünün.

Madenciler yerin yüzlerce metre altına inerken yanlarında küçük sarı bir kanarya kuşu (Canary) taşırlardı. Kömür madeninde zehirli gaz (karbonmonoksit) sızarsa, kanarya kuşunun bünyesi küçük olduğu için hemen bayılır ve madencileri uyarırdı! Madenciler kuşu görünce hemen maskelerini takar ve canlarını kurtarırdı!

Yazılımda **Canary Deployment** işte o madenci kuşudur!

Yeni bir güncelleme yazdığınızda bunu hemen tüm kullanıcılara açmazsınız. Önce trafiğin sadece %1'ine (kanaryalara) açarsınız. Eğer Sentry'de hata oranı artmazsa güncellemeyi %10, %50 ve %100'e çıkarırsınız. Bir hata olursa sadece o %1 etkilenir ve sistem 3 saniyede eski haline geri döner (Rollback).""",
            "story_en": """Consider subterranean coal miners in the 19th century.

Miners carried a caged yellow canary into the tunnels. If odorless, lethal methane or carbon monoxide leaked into the shaft, the canary succumbed first due to its rapid metabolism. The bird's distress alerted miners to evacuate immediately.

In modern site reliability engineering, a **Canary Deployment** is that caged sentinel.

When shipping a critical update, you do not route 100% of global traffic to it simultaneously. You route 1% of live traffic to the canary replica pool. Telemetry monitors error rates for 5 minutes. If latency remains flat, traffic increments to 10%, 50%, and 100%. If exceptions spike, traffic rolls back instantly with zero user impact.""",
            "mental_tr": """Blue-Green vs Canary Dağıtım Mimarisi:

```
BLUE-GREEN DAĞITIM:
[Yük Dengeleyici (Router)]
         │
         ├──(Trafik: %100)──> [BLUE: Mevcut Sürüm v1.0] (Canlıda)
         │
         └──(Trafik: %0)────> [GREEN: Yeni Sürüm v2.0] (Test Ediliyor)
[Geçiş Anı: Router yönü değiştirir; Green %100 olur, Blue yedekte bekler!]

──────────────────────────────────────────────────────────────────────────
CANARY DAĞITIM:
[Yük Dengeleyici]
         │
         ├──(Trafik: %95)───> [STABLE: Mevcut Sürüm v1.0]
         │
         └──(Trafik: %5)────> [CANARY: Yeni Sürüm v2.0] (Gözlemleniyor)
```""",
            "mental_en": """Blue-Green vs. Canary Deployment Topologies:

```
BLUE-GREEN TOPOLOGY:
[Application Load Balancer]
             │
             ├──(100% Traffic)──> [BLUE FLEET: v1.0] (Active Live)
             │
             └──(0% Traffic)────> [GREEN FLEET: v2.0] (Staged & Validated)
[Cutover: Router switches traffic pointer atomically; Green becomes active!]

──────────────────────────────────────────────────────────────────────────
CANARY TOPOLOGY:
[Traffic Router / API Gateway]
             │
             ├──(95% Traffic)───> [STABLE CLUSTER: v1.0]
             │
             └──(5% Traffic)────> [CANARY INSTANCES: v2.0] (Audited via Metrics)
```""",
            "prompt_tr": """# ROL: SRE ve Sürüm Dağıtım Yöneticisi
Üretim ortamımızda sıfır kesintili (Zero-Downtime) bir Canary dağıtım stratejisi kurgulayacağız.

## GÖREV:
1. Blue-Green ile Canary dağıtım arasındaki mimari ve maliyet farklarını karşılaştır.
2. Otomatik geri alma (Automated Rollback) tetikleyicisi olan bir senaryoyu tasarla (Örn: HTTP 500 oranı %1'i geçerse anında eski sürüme dön).
3. Veritabanı şema güncellemelerinde (Migrations) sıfır kesinti sağlamak için 'Expand and Contract' desenini açıkla.""",
            "prompt_en": """# ROLE: Release Engineering & SRE Specialist
We are designing zero-downtime deployment pipelines for our enterprise API.

## TASK:
1. Compare Blue-Green vs. Canary architectures analyzing infrastructure overhead and risk.
2. Detail an automated rollback policy triggered by Prometheus error telemetry.
3. Explain the 'Expand and Contract' (Parallel Run) pattern for non-breaking zero-downtime database migrations.""",
            "code_lang": "yaml",
            "code_naive": """# Kötü Dağıtım: Rolling update veya anında kapatıp açma (Kesinti yaşanır!)
# Eski sunucu kapanır, yenisi 45 saniyede ayağa kalkarken gelen kullanıcılar 502 Bad Gateway alır!""",
            "code_robust": """# Kubernetes / Cloud Canary Dağıtım Yapılandırması (Canary Rollout)
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: api-service
spec:
  replicas: 10
  strategy:
    canary:
      # Kademeli Trafik Dağıtımı
      steps:
        - setWeight: 5    # 1. Adım: Sadece %5 trafik yönlendir
        - pause: { duration: 10m } # 10 dakika boyunca Sentry / Prometheus izle!
        - setWeight: 20   # 2. Adım: %20'ye çıkar
        - pause: { duration: 10m }
        - setWeight: 50   # 3. Adım: %50'ye çıkar
        - pause: { duration: 5m }
      
      # Otomatik Geri Alma (Automated Rollback Kuralı)
      analysis:
        templates:
          - templateName: error-rate-check
        args:
          - name: max-error-rate
            value: "0.01" # Hata oranı %1'i geçerse ANINDA ESKİYE DÖN!""",
            "code_notes_tr": "`Argo Rollouts` kullanılarak trafik önce %5'e verilir ve Prometheus metrikleri incelenir. Hata oranı %1'i aşarsa sistem insan müdahalesine gerek kalmadan milisaniyeler içinde eski sürüme geri döner.",
            "code_notes_en": "Argo Rollouts directs 5% of traffic to the canary replica. If Prometheus records error rates exceeding 1%, automated self-healing triggers an instant rollback before users notice an outage.",
            "pitfalls_tr": [
                {"trap": "Veritabanında kolon silip eski sürümün çökmesine yol açmak (Breaking Migration).", "solution": "Expand-Contract desenini uygulayın: Önce yeni kolonu ekleyin, iki sürümü de destekleyin, eski kolonu en son silin."},
                {"trap": "Rollback (Geri alma) stratejisini önceden test etmeyip kriz anında paniklemek.", "solution": "Her deploy öncesi tek tuşla geri alma planınızın çalıştığından emin olun."},
                {"trap": "Canary dağıtımda logları ve metrikleri izlemeden trafiği hemen %100'e çekmek.", "solution": "Her kademede en az 5-10 dakika metriklerin oturmasını bekleyin."}
            ],
            "pitfalls_en": [
                {"trap": "Executing destructive schema migrations (dropping columns) while older application pods are still serving traffic.", "solution": "Apply the Expand-Contract pattern: add new fields in Phase 1, migrate in Phase 2, prune obsolete fields in Phase 3."},
                {"trap": "Lacking a tested, automated rollback plan prior to deploying.", "solution": "Verify single-command rollback triggers before initiating staging cutovers."},
                {"trap": "Rushing traffic increments without waiting for metric convergence.", "solution": "Allow canary cohorts to soak for 10 minutes to observe asynchronous exception rates."}
            ],
            "udemy_title_tr": "Ders 54: Sıfır Kesintili Dağıtım - Blue-Green ve Canary Stratejileri",
            "udemy_title_en": "Lecture 54: Zero-Downtime Deployments - Blue-Green & Canary",
            "udemy_slides_tr": [
                "Neden 'Sitemiz bakımda' dönemi tarihe karıştı?",
                "Blue-Green Dağıtım: Anında anahtarlama ve yedekleme.",
                "Canary Dağıtım: Madenci kanaryası gibi hata avlamak.",
                "Bölüm 9 Özeti: DevOps, Konteynerler ve Bulut Mimarisi."
            ],
            "udemy_slides_en": [
                "Why maintenance downtime windows are unacceptable in modern SaaS.",
                "Blue-Green cutovers: Atomic routing shifts with instant rollback capacity.",
                "Canary releases: Isolating blast radiuses to 1% of user traffic.",
                "Module 9 Recap: DevOps, Containers, Cloud Infrastructure & Resilient Deployments."
            ],
            "udemy_demo_tr": "Yerel Kubernetes (Minikube) veya Docker üzerinde iki versiyon ayağa kaldırın. Bir yük dengeleyici üzerinden gelen 100 isteğin 95'inin v1'e, 5'inin v2'ye gittiğini canlı log akışında kanıtlayın.",
            "udemy_demo_en": "Run two container fleets behind an Nginx or Traefik proxy. Fire 100 requests in a loop, showing 95 hitting v1.0 and 5 hitting the canary v2.0 deployment live.",
            "action_task_tr": "Projenizin deployment sürecini inceleyin. Bir hata olduğunda eski sürüme dönmenin (Rollback) kaç dakika sürdüğünü ve bu sürecin otomatikleştirilip otomatikleştirilemeyeceğini analiz edin.",
            "action_task_en": "Audit your team's deployment runbook: calculate your Mean-Time-To-Rollback (MTTR) and document steps to automate it via CI/CD.",
            "quiz_tr": [
                {
                    "question": "Canary (Kanarya) Dağıtım stratejisinin birincil amacı nedir?",
                    "options": [
                        "A) Kuş resimleri göstermek",
                        "B) Yeni yazılım sürümünü tüm kullanıcılara açmadan önce küçük bir kullanıcı grubuna (%1-%5) sunarak, olası hataların tüm sistemi çökertmesini engellemek ve riski minimize etmek",
                        "C) Sadece gece yarısı güncelleme yapmak",
                        "D) Sunucu masraflarını iki katına çıkarmak"
                    ],
                    "answer": "B",
                    "explanation": "Canary dağıtım, yeni sürümü küçük bir kullanıcı grubunda test eder; bir hata varsa sadece o küçük grup etkilenir ve sistem anında eski sürüme geri döner."
                },
                {
                    "question": "Veritabanı şemasında sıfır kesintili (Zero-Downtime) değişiklik yapmayı sağlayan mimari desene ne ad verilir?",
                    "options": [
                        "A) Kapat-Aç Deseni",
                        "B) Expand and Contract (Genişlet ve Daralt) Deseni",
                        "C) SQL Silme Deseni",
                        "D) Rastgele Güncelleme"
                    ],
                    "answer": "B",
                    "explanation": "Expand and Contract deseni, önce yeni yapıyı ekleyip hem eski hem yeni kodu destekler (Expand), ardından eski kodu ve alanı temizler (Contract); böylece kesinti yaşanmaz."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the primary operational objective of a Canary deployment strategy?",
                    "options": [
                        "A) Displaying avian icons in UI dashboards",
                        "B) Routing a tiny percentage of live traffic (1-5%) to the new release to validate production telemetry before widening blast radius",
                        "C) Mandating midnight deployments",
                        "D) Doubling cloud provider bills"
                    ],
                    "answer": "B",
                    "explanation": "Canary deployments limit blast radiuses by auditing real production telemetry against small cohorts before committing to global rollouts."
                },
                {
                    "question": "Which database migration strategy enables non-breaking zero-downtime schema evolution?",
                    "options": [
                        "A) The Stop-and-Start anti-pattern",
                        "B) The Expand and Contract (Parallel Run) pattern",
                        "C) The Truncate-Cascade technique",
                        "D) Random schema mutation"
                    ],
                    "answer": "B",
                    "explanation": "Expand and Contract introduces additive changes first, accommodates both code versions simultaneously, and purges obsolete schema fields only after all traffic migrates."
                }
            ]
        }
    ]
