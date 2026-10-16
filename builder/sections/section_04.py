"""
Section 4: Modern Yazılım Mimarisi & Tasarım Kalıpları (Chapters 19 to 24)
"""

def get_section_chapters():
    return [
        # Chapter 19
        {
            "id": 19,
            "section_id": 4,
            "slug_tr": "ch19_mimari_101_monolit_vs_mikroservis",
            "slug_en": "ch19_architecture_101_monolith_vs_microservices",
            "title_tr": "Mimari Nedir ve Junior Neden Bilmelidir? Monolit vs. Mikroservis",
            "title_en": "Architecture 101: Monoliths, Microservices & AI Navigation for Juniors",
            "subtitle_tr": "Erken Dönem Mikroservis Çılgınlığına Kapılmadan Doğru Mimarisi Seçmek",
            "subtitle_en": "Avoiding Premature Microservice Madness: Trade-offs Every Junior Must Know",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Bir şirketin 5 kişilik junior/mid ekibi varken neden Netflix gibi 200 mikroservis yapmaya çalışması ölümcül bir hatadır?",
            "podcast_hook_en": "Why is an early-stage team of 5 engineers attempting to replicate Netflix's 200 microservices an almost guaranteed startup death sentence?",
            "takeaways_tr": [
                "Yazılım mimarisi, projenin ilerleyen aşamalarında değiştirilmesi pahalı olan kararlar bütünüdür.",
                "Monolit mimari kötü kod demek değildir; modüler bir monolit başlangıç aşamasındaki ekipler için en hızlı ve güvenli yoldur.",
                "Yapay zeka araçları tek bir monolit kod tabanında (monorepo) çok daha yüksek bağlam (context) başarısı gösterir."
            ],
            "takeaways_en": [
                "Software architecture represents the decisions that are prohibitively expensive to alter later in a system's lifecycle.",
                "A monolith is not inherently legacy; a well-structured modular monolith is the most resilient starting point for velocity.",
                "AI developer tools achieve exponentially higher reasoning accuracy when operating inside a cohesive monorepo rather than fragmented microservices."
            ],
            "story_tr": """Bir kahve dükkanı açtığınızı düşünün. 

İlk gün dükkanda sadece siz ve bir arkadaşınız var. Şöyle bir plan yapar mısınız:
- Kahve çekirdeği öğütme departmanı ayrı bir binada
- Süt ısıtma departmanı arka sokakta
- Kasa ayrı bir binada
- Her departman birbirine telsizle (HTTP/gRPC) sipariş numarası yollasın!

Böyle yaparsanız bir fincan kahveyi 45 dakikada servis edemezsiniz ve batarsınız! İşte erken aşamada mikroservise bölünmek tam olarak budur.

Oysa tek bir tezgahın arkasında (Monolit) yan yana durursanız, birbirinizle konuşarak saniyede 1 kahve çıkarırsınız. Dükkanınız Starbucks gibi 1000 şubeye ulaştığında departmanları ayırmayı düşünürsünüz.""",
            "story_en": """Imagine opening a neighborhood artisan coffee shop with a single partner.

Would you structure operations like this:
- Bean grinding facility in a separate leased warehouse across town
- Milk steaming unit in another zip code
- Cash register hosted on a third street
- Baristas communicating across departments via short-wave radio (HTTP / gRPC payloads)

Serving a single cappuccino would take 45 minutes, bankrupting the business. That is premature microservice decomposition.

Operating behind a single consolidated counter (Monolith) allows you to pull shots and hand drinks to patrons in 30 seconds. Only when scaling to thousands of enterprise franchises does physical compartmentalization make sense.""",
            "mental_tr": """Monolit vs Mikroservis Karşılaştırma Matrisi:

| Kriter | Modüler Monolit (Modular Monolith) | Dağıtık Mikroservisler (Microservices) |
| :--- | :--- | :--- |
| **Geliştirme Hızı** | Çok yüksek (Tek repo, tek derleme) | Düşük (Servisler arası sözleşmeler, RPC) |
| **Dağıtım (Deployment)** | Basit (Tek bir Docker imajı / sunucu) | Karmaşık (Kubernetes, servis ağı, API Gateway) |
| **Hata Ayıklama (Debug)**| Kolay (Tek stack trace, yerel breakpoint) | Zor (Distributed tracing, Jaeger, correlation ID) |
| **Ölçeklenme** | Dikey ölçeklenme (CPU/RAM artırma) | Yatay bağımsız ölçeklenme (servis bazlı) |
| **AI Uyumluluğu** | Mükemmel (Tüm modeller ve tipler aynı bağlamda) | Parçalı (Servis sınırları prompt sınırlarını zorlar) |""",
            "mental_en": """Monolith vs. Microservice Architectural Matrix:

| Dimension | Modular Monolith | Distributed Microservices |
| :--- | :--- | :--- |
| **Initial Velocity** | Maximum (Unified workspace, immediate refactoring) | Sluggish (RPC schema synchronization, network boundaries) |
| **Deployment Simplicity** | High (Single container or binary deployment) | Complex (Kubernetes orchestration, API Gateways) |
| **Debugging / Tracing**| Direct (Single thread stack trace, local breakpoints) | Complex (Distributed tracing, correlation IDs) |
| **Scaling Dynamics** | Vertical scaling, horizontal web replica pools | Independent granular component scaling |
| **AI Tooling Synergy**| Optimal (Complete type universe visible to context) | Fragmented (Context windows split across repos) |""",
            "prompt_tr": """# ROL: Baş Sistem Mimarı (Chief Architect)
Yeni kurulan bir e-ticaret platformunun teknik mimarisini tartışıyoruz. 
Ekip büyüklüğümüz: 4 Junior, 1 Kıdemli Mühendis.

## GÖREV:
Mikroservis mi yoksa Modüler Monolit mi tercih etmeliyiz?
Lütfen şu 4 başlık altında net bir karar raporu hazırla:
1. Geliştirici üretkenliği ve yerel ortam kurulum süresi
2. Operasyonel maliyet (AWS / DevOps altyapısı)
3. Dağıtık veri tutarlılığı ve distributed transaction riskleri
4. Nihai mimari tavsiyen ve geçiş stratejisi""",
            "prompt_en": """# ROLE: Chief Systems Architect
We are architecting a seed-stage B2B SaaS platform.
Engineering headcount: 4 Juniors, 1 Staff Lead.

## TASK:
Provide an architectural recommendation: Modular Monolith vs. Microservices.
Deliver an executive trade-off briefing analyzing:
1. Developer onboarding velocity & local Docker setup complexity
2. Operational cloud budget & infrastructure maintenance overhead
3. Data consistency hazards & distributed transaction pitfalls
4. Final architectural recommendation and progressive migration strategy""",
            "code_lang": "typescript",
            "code_naive": """// Mikroservis Çılgınlığı: Basit bir sipariş için 3 farklı HTTP servisini çağırmak
// Ağ gecikmesi, servis kesintisi ve tutarsızlık riski tavan!
export async function createOrderMicroservices(userId: string, itemId: string) {
  // 1. Kullanıcı servisi
  const user = await fetch(`http://user-service/users/${userId}`).then(r => r.json());
  // 2. Stok servisi (Eğer çökerse ne olacak?)
  const stock = await fetch(`http://inventory-service/items/${itemId}`).then(r => r.json());
  // 3. Ödeme servisi (Para çekilip sipariş servisi çökerse para buharlaşır!)
  const payment = await fetch(`http://payment-service/charge`, { method: 'POST' }).then(r => r.json());

  return { success: true };
}""",
            "code_robust": """// Modüler Monolit: Aynı işlem belleğinde (in-memory) güvenli transaction
export class OrderService {
  constructor(
    private readonly userRepo: UserRepository,
    private readonly inventoryRepo: InventoryRepository,
    private readonly paymentGateway: PaymentGateway,
    private readonly db: DatabaseClient
  ) {}

  async createOrder(userId: string, itemId: string): Promise<OrderResult> {
    // Tüm adımlar tek bir veritabanı transaction'ında atomik yürütülür
    return await this.db.transaction(async (tx) => {
      const user = await this.userRepo.findById(userId, tx);
      if (!user) throw new NotFoundError("Kullanıcı bulunamadı.");

      const item = await this.inventoryRepo.reserveItem(itemId, tx);
      if (!item.inStock) throw new StockError("Ürün stokta kalmadı.");

      const charge = await this.paymentGateway.authorize(user, item.price);
      const order = await tx.orders.create({ data: { userId, itemId, chargeId: charge.id } });

      return { success: true, orderId: order.id };
    });
  }
}""",
            "code_notes_tr": "Modüler monolit sayesinde 3 farklı ağ çağrısı (network round-trip) ve servis çökme riski yerine, tek bir veritabanı işlemiyle atomik başarı garanti altına alınır.",
            "code_notes_en": "The modular monolith eliminates network hops, serialization overhead, and partial failure states by executing business logic atomically within a single database transaction.",
            "pitfalls_tr": [
                {"trap": "Ekipte tek bir DevOps mühendisi bile yokken Kubernetes ve 15 mikroservis kurmaya çalışmak.", "solution": "İlk 1-2 yıl modüler monolit ile ilerleyin; iş modeli kanıtlanınca gerektiğinde servisleri ayırın."},
                {"trap": "Monolit kod yazarken modülleri birbirine çorba yapmak (Spagetti Monolit).", "solution": "Monolit içinde katı modül sınırları (User, Order, Inventory) belirleyin; servisler sadece interface üzerinden konuşsun."},
                {"trap": "Mikroservisler arasında distributed transaction (2PC / Saga) karmaşasını yönetememek.", "solution": "Mümkün olan her yerde tek veritabanı ve ACID transaction gücünü kullanın."}
            ],
            "pitfalls_en": [
                {"trap": "Adopting Kubernetes and 20 microservices without dedicated DevOps infrastructure specialists.", "solution": "Begin with a clean modular monolith on managed compute (Render, Fly.io, ECS)."},
                {"trap": "Letting monolithic code degenerate into an unmaintainable 'Big Ball of Mud'.", "solution": "Enforce strict module boundaries via package workspaces and dependency injection."},
                {"trap": "Underestimating the complexity of distributed data consistency (Saga patterns, event eventual consistency).", "solution": "Leverage unified ACID transactions as long as throughput permits."}
            ],
            "udemy_title_tr": "Ders 19: Mimari Kararlar - Monolit vs Mikroservis Rehberi",
            "udemy_title_en": "Lecture 19: Architectural Trade-offs - Monolith vs Microservices",
            "udemy_slides_tr": [
                "Yazılım mimarisi nedir ve junior mühendis neden bilmelidir?",
                "Mikroservis hipotezi: Ne zaman gereklidir, ne zaman felakettir?",
                "Modüler Monolit anatomisi: Hız ve düzenin birleşimi.",
                "AI araçlarının monolit projelerdeki bağlam üstünlüğü."
            ],
            "udemy_slides_en": [
                "What is software architecture and why does it dictate system longevity?",
                "The microservices hype cycle: When it empowers vs. when it bankrupts.",
                "Anatomy of a Modular Monolith: Combining velocity with clean boundaries.",
                "Why AI development workflows thrive inside unified monorepos."
            ],
            "udemy_demo_tr": "Tek bir monorepo içinde `modules/user` ve `modules/order` yapısını gösterin. Modüllerin birbirinin iç detaylarına doğrudan erişmek yerine dışa açılan servis interface'i üzerinden nasıl konuştuğunu IDE'de gösterin.",
            "udemy_demo_en": "Inspect a modular monolith repository containing `modules/user` and `modules/order`. Demonstrate how TypeScript interfaces decouple module internals, allowing seamless future extraction.",
            "action_task_tr": "Mevcut projenizin mimarisini inceleyin. Kodlar katmanlara ve modüllere ayrılmış mı, yoksa tüm fonksiyonlar tek bir devasa klasörde mi toplanmış? 3 maddelik bir analiz çıkarın.",
            "action_task_en": "Perform an architectural inventory of your project: evaluate directory nesting, module coupling, and whether database models leak directly into view controllers.",
            "quiz_tr": [
                {
                    "question": "Erken aşamadaki (startup) küçük bir yazılım ekibi için 'Modüler Monolit' mimarinin en büyük avantajı nedir?",
                    "options": [
                        "A) Asla kod yazılmaması",
                        "B) Dağıtık ağ karmaşıklığı ve DevOps maliyeti olmadan hızlı geliştirme, kolay hata ayıklama ve atomik transaction imkanı sunması",
                        "C) Sadece C++ dilinde derlenebilmesi",
                        "D) İnternet gerektirmemesi"
                    ],
                    "answer": "B",
                    "explanation": "Modüler monolit, mikroservislerin getirdiği ağ gecikmesi ve operasyonel yük olmadan yüksek geliştirici hızı ve veri bütünlüğü sağlar."
                },
                {
                    "question": "Mikroservis mimarisinde karşılaşılan en karmaşık teknik problem hangisidir?",
                    "options": [
                        "A) CSS yazmak",
                        "B) Servisler arası ağ gecikmeleri, kısmi çöküşler (partial failures) ve dağıtık veri tutarlılığı",
                        "C) Bilgisayar monitörünün çözünürlüğü",
                        "D) Klavye tuşlarının sertliği"
                    ],
                    "answer": "B",
                    "explanation": "Dağıtık sistemlerde ağ güvenilmezdir. Bir servisin çökmesi veya gecikmesi zincirleme hatalara (cascading failure) yol açabilir."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the primary commercial advantage of a Modular Monolith for a small engineering squad?",
                    "options": [
                        "A) Elimination of typing code",
                        "B) High iteration velocity, direct local debugging, and zero distributed network orchestration overhead",
                        "C) Compatibility strictly with C++",
                        "D) Completely offline operation"
                    ],
                    "answer": "B",
                    "explanation": "Modular monoliths avoid distributed systems taxes (network latencies, serializations, cluster management), maximizing feature velocity."
                },
                {
                    "question": "What is the most notorious engineering hazard introduced by microservices?",
                    "options": [
                        "A) Formatting CSS rules",
                        "B) Network latency, distributed partial failures, and cross-service data consistency",
                        "C) Hardware display resolution limits",
                        "D) Keyboard mechanical switch resistance"
                    ],
                    "answer": "B",
                    "explanation": "Network calls introduce latency, network partitions, and eventual consistency dilemmas that require complex patterns like Saga or 2PC."
                }
            ]
        },

        # Chapter 20
        {
            "id": 20,
            "section_id": 4,
            "slug_tr": "ch20_solid_prensiplerini_ai_promptlarina_cevirmek",
            "slug_en": "ch20_translating_solid_principles_to_ai_prompts",
            "title_tr": "SOLID Prensipleri AI Promptlarına Nasıl Çevrilir?",
            "title_en": "Translating SOLID Principles into AI System Prompts",
            "subtitle_tr": "Yapay Zekanın Spagetti Kod Üretmesini Engelleyen 5 Altın Mimari Kural",
            "subtitle_en": "The 5 Architectural Pillars Preventing AI from Generating Spaghetti Disasters",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "SOLID prensipleri 20 yıl önce nesne yönelimli programlama için çıktı. Peki 2026'da LLM'lere kod yazdırırken SOLID neden hâlâ en büyük kurtarıcımız?",
            "podcast_hook_en": "SOLID principles were formulated decades ago for object-oriented systems; why are they the ultimate prompt constraints for AI code generation in 2026?",
            "takeaways_tr": [
                "AI modelleri serbest bırakıldığında her işi tek bir fonksiyona yığma (God Function) eğilimindedir.",
                "SOLID prensiplerini prompt kısıtı olarak vermek (Örn: 'Single Responsibility uygula'), AI'ın modüler kod üretmesini sağlar.",
                "Bağımlılıkların Tersine Çevrilmesi (Dependency Inversion), test edilebilir ve mocklanabilir kodun anahtarıdır."
            ],
            "takeaways_en": [
                "Unconstrained AI models instinctively construct bloated 'God Objects' that handle validation, database queries, and notifications in one method.",
                "Injecting SOLID principles directly into system prompts forces models to produce clean, decoupled classes and modules.",
                "Dependency Inversion (DIP) is the single most crucial pattern for generating easily testable and mockable code with AI."
            ],
            "story_tr": """İsviçre çakısını elinize alın: Üzerinde bıçak, makas, tirbüşon, testere ve tırnak törpüsü var. Küçük bir piknik için harikadır; ancak bir ameliyathaneye girdiğinizde cerrahın elinde İsviçre çakısı görürseniz masadan kaçarsınız! 

Cerrahın elinde sadece tek bir işi mükemmel yapan neşter olmalıdır.

Yapay zekaya *"Kullanıcı kaydı yap"* dediğinizde size tam bir İsviçre çakısı üretir: Aynı fonksiyon hem şifreyi doğrular, hem veritabanına yazar, hem e-posta atar, hem PDF fatura üretir! Kod 300 satır olur ve ilk değişiklikte patlar.

SOLID prensiplerini prompt'a eklediğinizde ise yapay zeka neşterler üretir: Her sınıf ve fonksiyon tek bir işi kusursuz yapar.""",
            "story_en": """Examine a Swiss Army knife: it packs a blade, scissors, can opener, toothpick, and saw. It's handy for camping, but if you walked into an operating theater and saw a neurosurgeon wielding a Swiss Army knife, you'd run for your life.

A surgeon relies on dedicated, single-purpose scalpels.

Prompting an LLM with *"Implement user registration"* yields a bloated Swiss Army knife: one 300-line monster function that hashes passwords, mutates database tables, sends welcome emails, and generates invoice PDFs.

When you inject SOLID constraints into your prompts, the AI produces surgical scalpels: modular, single-responsibility units that never bleed into adjacent domains.""",
            "mental_tr": """SOLID Prensiplerinin Prompt Karşılıkları:

```
S - Single Responsibility: "Bu fonksiyon sadece tek bir iş yapmalı. E-posta gönderimini ayrı bir servise ayır."
O - Open/Closed: "Yeni bir ödeme yöntemi eklendiğinde mevcut koda dokunulmamalı; bir interface implemente edilmeli."
L - Liskov Substitution: "Alt sınıflar üst sınıfın davranışını bozmamalı, beklenmedik hata fırlatmamalı."
I - Interface Segregation: "Müşteriyi kullanmadığı metotları içermeye zorlayan devasa interfaceler yazma; küçük arayüzler kur."
D - Dependency Inversion: "Doğrudan somut sınıfa (Concrete Class) değil, bir Interface/Abstraksiyona bağımlı ol."
```""",
            "mental_en": """The SOLID to AI Prompt Translation Guide:

```
S - Single Responsibility: "Decompose this into discrete classes: separate database writes from mail notifications."
O - Open/Closed: "Design this via a strategy interface so novel payment gateways can be added without editing the core router."
L - Liskov Substitution: "Derived classes must satisfy base contracts without altering behavioral invariants or throwing unanticipated exceptions."
I - Interface Segregation: "Avoid bloated 20-method interfaces; split into composable, granular capabilities."
D - Dependency Inversion: "Inject dependencies via constructor interfaces; do not instantiate concrete database clients internally."
```""",
            "prompt_tr": """# ROL: SOLID ve Temiz Mimari Uzmanı
Aşağıdaki 'God Object' (her işi yapan) JavaScript fonksiyonunu SOLID prensiplerine göre refactor et.

## MEVCUT KOD:
```typescript
class OrderProcessor {
  async process(order: any) {
    // 1. Doğrulama
    if (order.amount <= 0) throw new Error("Hatalı tutar");
    // 2. SQL kaydı
    await db.query(`INSERT INTO orders VALUES (${order.id}, ${order.amount})`);
    // 3. E-posta bildirimi
    await mailer.send(order.email, "Sipariş alındı");
  }
}
```

## GÖREV:
1. Single Responsibility (SRP) uyarınca doğrulama, veritabanı ve bildirim işlerini ayrı servislere böl.
2. Dependency Inversion (DIP) uyarınca `OrderProcessor` sınıfına bağımlılıkları constructor üzerinden interface olarak enjekte et.""",
            "prompt_en": """# ROLE: Clean Architecture Lead
Refactor this monolithic 'God Class' following SOLID principles:

## LEGACY SNIPPET:
```typescript
class OrderProcessor {
  async process(order: any) {
    if (order.amount <= 0) throw new Error("Invalid amount");
    await db.query(`INSERT INTO orders VALUES (${order.id}, ${order.amount})`);
    await mailer.send(order.email, "Order confirmed");
  }
}
```

## TASK:
1. Apply Single Responsibility (SRP): decouple validation, persistence, and messaging into dedicated collaborators.
2. Apply Dependency Inversion (DIP): inject dependencies via constructor interfaces to enable mock unit testing.""",
            "code_lang": "typescript",
            "code_naive": """// SOLID'e Aykırı: Her işi tek sınıfta yapan God Object
export class OrderProcessorNaive {
  async processOrder(order: any) {
    // SRP ihlali: Validasyon, DB erişimi ve Mail tek yerde
    if (!order.id || order.amount <= 0) throw new Error("Geçersiz");
    // SQL Injection açığı da var!
    await db.query(`INSERT INTO orders VALUES ('${order.id}', ${order.amount})`);
    // DIP ihlali: Dış kütüphaneye doğrudan sıkı bağımlılık (tight coupling)
    await fetch("https://api.sendgrid.com/send", { body: JSON.stringify(order) });
  }
}""",
            "code_robust": """// SOLID Uyumlu: Modüler, Test Edilebilir, Tip Güvenli Mimari

// 1. Abstraksiyonlar (DIP)
export interface OrderRepository {
  save(order: ValidatedOrder): Promise<void>;
}

export interface NotificationService {
  notifyOrderPlaced(order: ValidatedOrder): Promise<void>;
}

export interface ValidatedOrder {
  readonly id: string;
  readonly amount: number;
  readonly customerEmail: string;
}

// 2. Orkestrasyon Sınıfı (SRP: Sadece iş akışını yönetir)
export class OrderProcessor {
  constructor(
    private readonly repository: OrderRepository,
    private readonly notifier: NotificationService
  ) {}

  async process(order: ValidatedOrder): Promise<void> {
    // Adım 1: Kaydet
    await this.repository.save(order);

    // Adım 2: Bildir
    await this.notifier.notifyOrderPlaced(order);
  }
}""",
            "code_notes_tr": "Artık `OrderProcessor` veritabanının PostgreSQL mi MongoDB mi olduğunu veya e-postanın SendGrid ile mi AWS SES ile mi gittiğini bilmez. Test yazarken sahte (mock) repository enjekte etmek 2 satırdır.",
            "code_notes_en": "`OrderProcessor` is completely decoupled from database drivers and third-party email SDKs. Unit testing this workflow requires only passing lightweight in-memory test doubles into the constructor.",
            "pitfalls_tr": [
                {"trap": "SOLID prensiplerini aşırıya kaçırıp 3 satırlık kod için 15 farklı interface ve dosya üretmek (Over-engineering).", "solution": "Pragmatik olun; SOLID prensiplerini sistemin büyüyeceği ve değişeceği kritik noktalara uygulayın."},
                {"trap": "AI'a sadece 'SOLID uygula' deyip hangi prensibe odaklanacağını belirtmemek.", "solution": "Özellikle 'SRP ve Dependency Injection uygula' şeklinde spesifik kurallar verin."},
                {"trap": "Interface yazıp constructor yerine sınıf içinde `new ConcreteClass()` çağırmak.", "solution": "Bağımlılıkları daima dışarıdan constructor parametresi olarak geçin (Inversion of Control)."}
            ],
            "pitfalls_en": [
                {"trap": "Over-engineering trivial 5-line scripts into 12 abstract factories.", "solution": "Apply SOLID pragmatically where domain rules shift or multiple implementations exist."},
                {"trap": "Vaguely prompting 'make it SOLID' without specifying architectural intent.", "solution": "Pinpoint exact constraints: 'Apply SRP to separate HTTP adapters from persistence'."},
                {"trap": "Declaring interfaces yet instantiating concrete classes via `new` inside constructors.", "solution": "Always inject dependencies as constructor parameters to maintain Inversion of Control."}
            ],
            "udemy_title_tr": "Ders 20: SOLID Prensipleri - AI Kodunu Mimari Seviyeye Taşımak",
            "udemy_title_en": "Lecture 20: SOLID in Practice - Elevating AI Code to Enterprise Standards",
            "udemy_slides_tr": [
                "Neden yapay zeka varsayılan olarak 'God Object' üretir?",
                "5 SOLID prensibinin sadeleştirilmiş Türkçe açıklaması.",
                "Dependency Inversion ile test edilebilir kod üretmek.",
                "Canlı Refactoring: 150 satırlık dev fonksiyonu SOLID ile parçalamak."
            ],
            "udemy_slides_en": [
                "Why unconstrained LLMs default to bloated God Objects.",
                "The 5 SOLID pillars explained through everyday engineering analogies.",
                "Decoupling systems via Dependency Inversion for testability.",
                "Live refactor: Slicing a 150-line procedural script into SOLID units."
            ],
            "udemy_demo_tr": "Tek bir sınıf içinde hem veritabanına yazan hem e-posta atan fonksiyonu AI'a verin. 'Apply Single Responsibility and Dependency Inversion' promptuyla iki ayrı interface ve sınıf oluşturmasını sağlayın. Ardından mock kullanarak Jest testi yazdırın.",
            "udemy_demo_en": "Take an all-in-one procedural script. Prompt the AI: 'Refactor using SRP and Dependency Injection with TypeScript interfaces'. Show the resulting clean classes and write a mock unit test in 30 seconds.",
            "action_task_tr": "Kod tabanınızda 100 satırdan uzun olan bir fonksiyon bulun. İçindeki işleri listeleyin ve en az bir işi (örn: e-posta veya loglama) ayrı bir servise çıkartın.",
            "action_task_en": "Locate a monolithic function in your codebase (>100 lines). Extract logging or notification side-effects into a distinct injected collaborator.",
            "quiz_tr": [
                {
                    "question": "SOLID'in 'Single Responsibility Principle' (Tek Sorumluluk Prensibi) kuralı neyi ifade eder?",
                    "options": [
                        "A) Şirkette sadece bir yazılımcının çalışmasını",
                        "B) Bir sınıfın veya fonksiyonun değişmesi için yalnızca tek bir nedeninin olması gerektiğini",
                        "C) Sadece tek bir satır kod yazılmasını",
                        "D) Değişkenlerin tek harfle isimlendirilmesini"
                    ],
                    "answer": "B",
                    "explanation": "SRP, bir modülün sadece tek bir aktöre/iş kuralına karşı sorumlu olması gerektiğini; farklı sorumlulukların birbirine karıştırılmamasını savunur."
                },
                {
                    "question": "Dependency Inversion (Bağımlılıkların Tersine Çevrilmesi) prensibinin en büyük pratik avantajı nedir?",
                    "options": [
                        "A) Kodun daha yavaş çalışması",
                        "B) Sınıfların somut veritabanlarına sıkı sıkıya bağlanmasını engelleyerek birim testlerde (Unit Test) kolayca mocklanabilmesini sağlaması",
                        "C) Sadece Java dilinde çalışması",
                        "D) CSS hatalarını düzeltmesi"
                    ],
                    "answer": "B",
                    "explanation": "Interface bağımlılıkları sayesinde test koşarken gerçek veritabanı yerine sahte (mock) objeler verilebilir; testler izole ve yıldırım hızında çalışır."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the formal definition of the Single Responsibility Principle (SRP)?",
                    "options": [
                        "A) An engineering squad must have only one developer",
                        "B) A class or module should have one, and only one, reason to change",
                        "C) Every function must be exactly one line long",
                        "D) All variables must be single letters"
                    ],
                    "answer": "B",
                    "explanation": "SRP dictates that each class or function encapsulates one business capability, insulating it from unrelated requirement shifts."
                },
                {
                    "question": "What is the primary architectural payoff of Dependency Inversion (DIP)?",
                    "options": [
                        "A) Slowing down CPU instruction clocks",
                        "B) Decoupling high-level business rules from low-level I/O details, allowing frictionless unit test mocking",
                        "C) Exclusivity to Java enterprise applications",
                        "D) Automatic CSS flexbox formatting"
                    ],
                    "answer": "B",
                    "explanation": "DIP allows developers to substitute production infrastructure with in-memory test doubles during automated testing."
                }
            ]
        },

        # Chapter 21
        {
            "id": 21,
            "section_id": 4,
            "slug_tr": "ch21_tasarim_kaliplari_factory_strategy_observer",
            "slug_en": "ch21_design_patterns_factory_strategy_observer",
            "title_tr": "Tasarım Kalıpları (Design Patterns): Factory, Strategy, Observer Pratikte",
            "title_en": "Design Patterns in Modern AI Workflows: Factory, Strategy & Observer",
            "subtitle_tr": "Tekerleği Yeniden İcat Etmeden Endüstri Standartlarında Kod Yazmak",
            "subtitle_en": "Writing Industry-Standard Software Without Reinventing the Algorithmic Wheel",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Gang of Four tasarım kalıpları 1994 yılında yazıldı. 2026'da AI çağında Factory, Strategy veya Observer kalıpları hâlâ geçerli mi?",
            "podcast_hook_en": "The Gang of Four catalog was published in 1994; why are patterns like Strategy, Factory, and Observer still indispensable in modern AI-assisted engineering?",
            "takeaways_tr": [
                "Tasarım kalıpları ezberlenecek formüller değil; yazılımcıların ve yapay zekanın ortak kelime dağarcığıdır (Vocabulary).",
                "AI'a 'Burada 10 tane if-else yazmak yerine Strategy Pattern kullan' demek, tek kelimeyle mükemmel mimari kurdurur.",
                "Observer deseni, günümüzün modern olay tabanlı (Event-Driven) sistemlerinin ve bildirim mekanizmalarının temelidir."
            ],
            "takeaways_en": [
                "Design patterns are not academic dogma; they are a high-bandwidth shared vocabulary between humans and AI.",
                "Instructing an AI model: 'Refactor this branching logic using the Strategy Pattern' conveys vast architectural nuance in a single sentence.",
                "The Observer pattern is the architectural bedrock of modern reactive event-driven and streaming systems."
            ],
            "story_tr": """Bir restorana gittiğinizi ve garsona sipariş verdiğinizi hayal edin. 

Garsona her seferinde: *"Önce bir tabağı dolaptan çıkar, sonra içine 200 gram un koy, fırını 180 dereceye ayarla, fırına sür ve piştikten sonra masama getir"* diyor musunuz? Hayır! Sadece menüden: *"Bir pizza Margherita lütfen"* dersiniz. Mutfak bunu nasıl üreteceğini zaten bilir. İşte bu **Factory (Fabrika)** desenidir!

Peki pizzayı nasıl ödeyeceksiniz? Nakit mi, kredi kartı mı, kripto ile mi? Kasiyer ödeme yöntemine göre pos cihazını uzatır veya nakit alır. İşte bu **Strategy (Strateji)** desenidir!

Pizzanız hazır olduğunda masadaki çağrı cihazı titrer ve size haber verir. İşte bu da **Observer (Gözlemci)** desenidir!

Tasarım kalıpları hayatın içindeki standart çözümlerdir. Kodda da aynısı geçerlidir.""",
            "story_en": """Visit a pizzeria and place an order.

Do you tell the server: *"Retrieve a porcelain dish from cupboard 3, measure 200 grams of flour, preheat the oven to 450 degrees, bake for 12 minutes, and carry it to my table"?* Never. You say: *"One Margherita pizza, please."* The kitchen encapsulates the instantiation mechanics. That is the **Factory Pattern**.

How do you settle the bill? Apple Pay, credit card, or cash? The cashier presents the appropriate terminal without altering the bill total. That is the **Strategy Pattern**.

When your pizza is boxed, a buzzer lights up on your table notifying you to pick it up. That is the **Observer Pattern**.

Design patterns are standard operational blueprints for everyday problems. The same rigor applies to scalable software.""",
            "mental_tr": """En Çok Kullanılan 3 Tasarım Kalıbı:

```
1. FACTORY PATTERN (Yaratımsal):
   İstemci nesnenin nasıl üretildiğini bilmez; sadece 'Bana X tipinde bir nesne ver' der.
   Kullanım: Farklı veritabanı sürücüleri, ödeme sağlayıcıları oluşturma.

2. STRATEGY PATTERN (Davranışsal):
   Çalışma zamanında (runtime) algoritmanın veya davranışın değiştirilebilmesini sağlar.
   Kullanım: Farklı kargo hesaplama algoritmaları, indirim kuponu stratejileri.

3. OBSERVER PATTERN (Davranışsal):
   Bir nesnede durum değiştiğinde, ona abone olan tüm diğer nesneleri otomatik haberdar eder.
   Kullanım: Event Emitter'lar, Webhook bildirimleri, WebSocket yayınları.
```""",
            "mental_en": """The Essential Junior Pattern Triumvirate:

```
1. FACTORY PATTERN (Creational):
   Hides instantiation complexity. The caller asks: 'Give me a storage client for AWS S3'.
   Use Cases: Multi-cloud adapters, database connection pooling.

2. STRATEGY PATTERN (Behavioral):
   Allows runtime interchangeability of algorithms without modifying the context host.
   Use Cases: Dynamic discount policies, payment processing adapters.

3. OBSERVER PATTERN (Behavioral):
   Maintains a subscriber registry; state mutations trigger automatic updates to all listeners.
   Use Cases: Event emitters, UI state subscription, webhook fan-out.
```""",
            "prompt_tr": """# ROL: Yazılım Tasarım Kalıpları Mimarı
Projemizde kullanıcılar 3 farklı yöntemle bildirim alabilmektedir:
- SMS (Twilio)
- E-posta (SendGrid)
- Push Notification (Firebase)

## GÖREV:
Bu yapıyı 'Strategy Pattern' kullanarak TypeScript ile kur.
1. Ortak bir `NotificationStrategy` interface'i tanımla (`send(userId, message)`).
2. Her kanal için ayrı bir somut strateji sınıfı yaz.
3. Bir `NotificationContext` sınıfı yazarak çalışma zamanında stratejinin dinamik olarak değiştirilebilmesini sağla.""",
            "prompt_en": """# ROLE: Software Design Patterns Architect
Our platform sends notifications across 3 distinct channels:
- SMS (Twilio)
- Email (SendGrid)
- Push Notifications (Firebase FCM)

## TASK:
Model this system in TypeScript using the Strategy Pattern:
1. Define a shared `NotificationStrategy` interface (`send(userId, message)`).
2. Implement discrete strategy classes for each provider.
3. Implement a `NotificationContext` class allowing dynamic runtime swapping of notification channels.""",
            "code_lang": "typescript",
            "code_naive": """// Kötü: 20 tane if-else ile spagetti kod
export async function sendNotificationSpaghetti(type: string, userId: string, msg: string) {
  if (type === "SMS") {
    // 30 satır Twilio kodu...
  } else if (type === "EMAIL") {
    // 30 satır SendGrid kodu...
  } else if (type === "PUSH") {
    // 30 satır Firebase kodu...
  } else {
    throw new Error("Bilinmeyen bildirim türü");
  }
}""",
            "code_robust": """// Strategy Pattern ile Zarif ve Genişletilebilir Mimari

// 1. Strateji Arayüzü (Contract)
export interface NotificationStrategy {
  send(userId: string, message: string): Promise<boolean>;
}

// 2. Somut Stratejiler (Concrete Strategies)
export class EmailNotificationStrategy implements NotificationStrategy {
  async send(userId: string, message: string): Promise<boolean> {
    console.log(`[SendGrid] ${userId} kullanıcısına e-posta gönderildi: ${message}`);
    return true;
  }
}

export class SmsNotificationStrategy implements NotificationStrategy {
  async send(userId: string, message: string): Promise<boolean> {
    console.log(`[Twilio] ${userId} kullanıcısına SMS atıldı: ${message}`);
    return true;
  }
}

// 3. Bağlam Yöneticisi (Context)
export class NotificationService {
  private strategy: NotificationStrategy;

  constructor(initialStrategy: NotificationStrategy) {
    this.strategy = initialStrategy;
  }

  setStrategy(newStrategy: NotificationStrategy): void {
    this.strategy = newStrategy;
  }

  async dispatch(userId: string, message: string): Promise<boolean> {
    return await this.strategy.send(userId, message);
  }
}""",
            "code_notes_tr": "Artık sisteme 'WhatsApp' veya 'Slack' bildirimi eklemek istediğimizde mevcut koda tek bir satır dahi dokunmayız (Open/Closed Principle). Sadece yeni bir `WhatsAppStrategy` sınıfı ekleriz.",
            "code_notes_en": "Adding WhatsApp or Discord notifications requires zero modifications to existing classes (Open/Closed Principle). We simply implement a new `WhatsAppStrategy` conforming to the interface.",
            "pitfalls_tr": [
                {"trap": "Basit 2 durumlu bir kontrol için devasa Factory veya Strategy sınıfları kurmak.", "solution": "Eğer durum sayısı 2'yi geçmeyecekse basit bir `if/else` yeterlidir; kalıpları karmaşıklık arttığında devreye sokun."},
                {"trap": "Observer deseninde abonelikten çıkmayı (unsubscribe) unutup bellek sızıntısına (memory leak) yol açmak.", "solution": "Bileşenler yok edildiğinde (unmount) event listener'ları mutlaka temizleyin."},
                {"trap": "Kalıpların isimlerini projedeki isimlendirmelere yansıtmamak.", "solution": "Sınıf isimlerine `PaymentStrategy`, `LoggerFactory` gibi açık ekler verin."}
            ],
            "pitfalls_en": [
                {"trap": "Overusing patterns for simple binary conditions (e.g., boolean flags).", "solution": "A simple ternary or if/else is sufficient for binary branches; reserve patterns for extensible domains."},
                {"trap": "Failing to unsubscribe listeners in the Observer pattern, causing memory leaks.", "solution": "Always clean up subscriptions when components unmount or sessions terminate."},
                {"trap": "Concealing pattern intent with ambiguous class names.", "solution": "Explicitly append pattern suffixes: `StripePaymentStrategy`, `LoggerFactory`."}
            ],
            "udemy_title_tr": "Ders 21: Tasarım Kalıpları - Factory, Strategy ve Observer",
            "udemy_title_en": "Lecture 21: Design Patterns in Action - Factory, Strategy & Observer",
            "udemy_slides_tr": [
                "Tasarım kalıpları neden yapay zeka ile geliştiricinin ortak dilidir?",
                "If-Else canavarından Strategy Pattern ile kurtulmak.",
                "Factory Pattern ile nesne yaratımını soyutlamak.",
                "Observer Pattern: Event-Driven mimarinin temeli."
            ],
            "udemy_slides_en": [
                "Design patterns as the common vocabulary uniting engineers and AI models.",
                "Slaying the if-else branching beast with the Strategy Pattern.",
                "Decoupling instantiation complexity using the Factory Pattern.",
                "The Observer Pattern: Foundation of modern reactive and event-driven systems."
            ],
            "udemy_demo_tr": "Bir e-ticaret kargo hesaplayıcısı yazın. 'Aras', 'Yurtiçi' ve 'DHL' için 3 farklı strateji sınıfı kurun. Kullanıcı kargo firmasını seçtiğinde runtime'da stratejinin nasıl değiştiğini ve doğru ücreti hesapladığını konsolda gösterin.",
            "udemy_demo_en": "Implement a shipping cost calculator. Author 3 strategy classes for FedEx, UPS, and DHL. Demonstrate swapping strategies at runtime in response to user selection.",
            "action_task_tr": "Projenizde en az 3 farklı `else if` içeren bir kod bloğu bulun ve bunu Strategy Pattern ile refactor edin.",
            "action_task_en": "Refactor a multi-branch `switch` or `else-if` statement in your project into a polymorphic Strategy map.",
            "quiz_tr": [
                {
                    "question": "Strategy Pattern'in temel amacı nedir?",
                    "options": [
                        "A) Veritabanındaki tüm tabloları silmek",
                        "B) Birbirinin yerine geçebilen algoritmalar ailesi tanımlayarak, algoritmayı onu kullanan istemciden bağımsız şekilde çalışma zamanında değiştirebilmek",
                        "C) Sadece HTML dosyalarını sıkıştırmak",
                        "D) Bilgisayarın pil ömrünü uzatmak"
                    ],
                    "answer": "B",
                    "explanation": "Strategy Pattern, çalışma zamanında farklı algoritmaların (örn: ödeme veya sıralama yöntemleri) dinamik olarak birbirinin yerine kullanılmasını sağlar."
                },
                {
                    "question": "Observer Pattern'de bildirimleri dinleyen taraflara ne ad verilir?",
                    "options": [
                        "A) Subscriber (Abone / Gözlemci)",
                        "B) Compiler",
                        "C) Terminal",
                        "D) Router"
                    ],
                    "answer": "A",
                    "explanation": "Observer deseninde durum yayınlayan nesne Subject (Yayımcı), bu durumu dinleyen nesneler ise Observer / Subscriber (Abone) olarak adlandırılır."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the primary architectural purpose of the Strategy Pattern?",
                    "options": [
                        "A) Wiping database tables cleanly",
                        "B) Encapsulating a family of interchangeable algorithms to swap behaviors dynamically at runtime without modifying the client",
                        "C) Compressing HTML templates",
                        "D) Conserving laptop battery cycles"
                    ],
                    "answer": "B",
                    "explanation": "The Strategy Pattern enables dynamic runtime selection of algorithms by adhering to a shared polymorphic interface."
                },
                {
                    "question": "In the Observer Pattern, what term designates the listening entities registered for notifications?",
                    "options": [
                        "A) Subscribers / Observers",
                        "B) Compilers",
                        "C) Command Shells",
                        "D) Network Routers"
                    ],
                    "answer": "A",
                    "explanation": "The publisher maintains a registry of Observers/Subscribers and invokes their notification callback on state changes."
                }
            ]
        },

        # Chapter 22
        {
            "id": 22,
            "section_id": 4,
            "slug_tr": "ch22_katmanli_mimari_ve_separation_of_concerns",
            "slug_en": "ch22_layered_architecture_separation_of_concerns",
            "title_tr": "Katmanlı Mimari & Separation of Concerns: Sorumlulukları Ayırmak",
            "title_en": "Layered & Clean Architecture: Separation of Concerns in Practice",
            "subtitle_tr": "Controller, Service, Repository Katmanlarını Birbirine Karıştırmama Kılavuzu",
            "subtitle_en": "The Definitive Guide to Decoupling Controllers, Services, and Repositories",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Bir API Controller'ının içine SQL sorgusu yazmak neden yazılım dünyasının en büyük günahlarından biridir ve katmanlı mimari sistemi nasıl korur?",
            "podcast_hook_en": "Why is writing raw database queries inside an HTTP Controller considered a cardinal sin in production engineering, and how does layered architecture shield your codebase?",
            "takeaways_tr": [
                "Separation of Concerns (İlgi Alanlarının Ayrımı), sistemin her katmanının sadece kendi işini bilmesidir.",
                "Controller sadece HTTP protokolünü (istek/yanıt) yönetir; Service saf iş mantığını yürütür; Repository ise veriye erişir.",
                "Yapay zekaya bu katmanları açıkça belirttiğinizde, AI çok daha temiz, modüler ve kurumsal kod üretir."
            ],
            "takeaways_en": [
                "Separation of Concerns mandates that each architectural layer is oblivious to concerns outside its boundary.",
                "Controllers parse HTTP transports; Services enforce domain business rules; Repositories encapsulate data access.",
                "Explicitly directing an AI model to structure code along these three layers prevents logic leakage and guarantees testability."
            ],
            "story_tr": """Lüks bir oteli hayal edin. 

Otelde 3 ana görevli var:
1. **Resepsiyonist (Controller):** Kapıda müşteriyi karşılar, kimliğini kontrol eder ve isteğini alır. Asla mutfağa girip yemek pişirmez!
2. **Şef Aşçı (Service):** Siparişin malzemelerini hazırlar, tarife göre pişirir. Müşterinin kredi kartıyla ilgilenmez!
3. **Kiler Sorumlusu (Repository):** Domatesin, etin hangi rafta olduğunu bilir; şef isteyince raftan çıkarıp verir.

Eğer resepsiyonist masayı bırakıp mutfakta omlet yapmaya, kilerdeki domatesleri saymaya kalkarsa otelde kaos çıkar!

İşte Controller içine veritabanı sorgusu yazmak, o resepsiyonistin mutfakta tencere yıkamasıdır.""",
            "story_en": """Picture a luxury five-star hotel.

Three distinct professionals operate seamlessly:
1. **The Concierge (Controller):** Greets arriving guests, verifies reservations, and accepts requests. They never step into the kitchen to grill steaks.
2. **The Executive Chef (Service):** Prepares exquisite meals adhering to culinary recipes. They never process guest credit card swipes.
3. **The Pantry Inventory Manager (Repository):** Knows the precise shelf location of aged cheeses and cuts of beef; retrieves them upon chef request.

If the concierge abandons the front desk to wash pots and count pantry crates, the hotel descends into chaos.

Writing database queries inside an Express or FastAPI Controller is that concierge washing dishes in the lobby.""",
            "mental_tr": """3 Katmanlı Mimari Akışı:

```
[İstemci (React/Mobil)] ──(HTTP İsteği)──> [1. CONTROLLER KATMANI]
                                                  │
                                            (İş Talebi)
                                                  ▼
                                           [2. SERVICE KATMANI]
                                            (İş Mantığı & Kurallar)
                                                  │
                                            (Veri Talebi)
                                                  ▼
                                           [3. REPOSITORY KATMANI]
                                                  │
                                           (SQL / ORM Sorgusu)
                                                  ▼
                                           [VERİTABANI (Postgres/Mongo)]
```""",
            "mental_en": """The 3-Tier Layered Architecture Flow:

```
[Client (Web / Mobile App)] ──(HTTP JSON)──> [1. CONTROLLER LAYER]
                                                    │ (Sanitized DTO)
                                                    ▼
                                             [2. SERVICE LAYER]
                                              (Core Domain Logic)
                                                    │ (Persistence Request)
                                                    ▼
                                             [3. REPOSITORY LAYER]
                                                    │ (SQL / Prisma Query)
                                                    ▼
                                             [DATABASE (PostgreSQL)]
```""",
            "prompt_tr": """# ROL: Temiz Mimari (Clean Architecture) Uzmanı
Node.js / Express ve Prisma kullanan bir kullanıcı oluşturma özelliğimiz var.

## GÖREV:
Bu özelliği 3 katmanlı mimariye uygun şekilde 3 ayrı dosyada tasarla:
1. `user.controller.ts`: Sadece HTTP req/res, durum kodları ve Zod doğrulaması ile ilgilensin.
2. `user.service.ts`: Şifre hashleme ve iş kuralları ile ilgilensin (asla HTTP nesnesi almasın!).
3. `user.repository.ts`: Sadece Prisma sorgusu ile veritabanına kayıt yapsın.""",
            "prompt_en": """# ROLE: Clean Architecture Lead
We are building a user registration feature using Node.js, Express, and Prisma.

## TASK:
Architect this feature strictly adhering to 3-tier Layered Architecture:
1. `user.controller.ts`: Handles HTTP req/res, status codes, and Zod parsing exclusively.
2. `user.service.ts`: Handles password hashing and business validation (never accepts HTTP req/res!).
3. `user.repository.ts`: Encapsulates pure Prisma database persistence.""",
            "code_lang": "typescript",
            "code_naive": """// Felaket: Controller içinde hem validasyon, hem hashleme, hem SQL!
app.post("/users", async (req, res) => {
  if (!req.body.email) return res.status(400).send("Email gerekli");
  const hashed = await bcrypt.hash(req.body.password, 10);
  const user = await prisma.user.create({ data: { email: req.body.email, password: hashed } });
  await sendEmail(user.email);
  res.json(user); // Şifre hash'i bile frontend'e sızdı!
});""",
            "code_robust": """// 1. REPOSITORY KATMANI (user.repository.ts)
export class UserRepository {
  async create(data: { email: string; passwordHash: string }) {
    return await prisma.user.create({ data });
  }
  async findByEmail(email: string) {
    return await prisma.user.findUnique({ where: { email } });
  }
}

// 2. SERVICE KATMANI (user.service.ts - Saf İş Mantığı)
export class UserService {
  constructor(private readonly userRepo: UserRepository) {}

  async registerUser(dto: RegisterUserDto): Promise<SafeUser> {
    const existing = await this.userRepo.findByEmail(dto.email);
    if (existing) throw new ConflictError("E-posta zaten kayıtlı.");

    const passwordHash = await hashPassword(dto.password);
    const user = await this.userRepo.create({ email: dto.email, passwordHash });

    return { id: user.id, email: user.email }; // Şifre asla dönmez!
  }
}

// 3. CONTROLLER KATMANI (user.controller.ts - Sadece HTTP Protokolü)
export class UserController {
  constructor(private readonly userService: UserService) {}

  async handleRegister(req: Request, res: Response): Promise<void> {
    const validated = RegisterUserSchema.parse(req.body);
    const user = await this.userService.registerUser(validated);
    res.status(201).json({ success: true, data: user });
  }
}""",
            "code_notes_tr": "Katmanlar ayrıldığında; veritabanını Prisma'dan TypeORM'a geçirmek sadece Repository'yi etkiler. Web framework'ünü Express'ten Fastify'a geçirmek ise sadece Controller'ı etkiler. Service katmanındaki iş mantığına asla dokunulmaz!",
            "code_notes_en": "Decoupling layers yields extreme durability: swapping Prisma for raw SQL impacts only the Repository; migrating from Express to Fastify impacts only the Controller. Pure domain logic inside the Service remains untouched.",
            "pitfalls_tr": [
                {"trap": "Service fonksiyonlarına Express `req` ve `res` nesnelerini parametre olarak geçmek.", "solution": "Service katmanı HTTP'den habersiz olmalıdır; sadece saf JavaScript objeleri (DTO) almalıdır."},
                {"trap": "Controller'ı atlayıp doğrudan veritabanı modelini frontend'e döndürerek şifre gibi gizli alanları sızdırmak.", "solution": "Daima Response DTO kullanarak sadece güvenli alanları dönün."},
                {"trap": "Basit CRUD işlemlerinde gereksiz 10 katman oluşturup aşırı karmaşıklık yaratmak.", "solution": "İş mantığı olmayan yerlerde katmanları gereksiz derinleştirmeyin; pragmatik olun."}
            ],
            "pitfalls_en": [
                {"trap": "Passing HTTP `req` and `res` objects into the Service layer.", "solution": "Services must remain transport-agnostic, consuming only plain Data Transfer Objects (DTOs)."},
                {"trap": "Leaking database entity models containing password hashes directly to frontend clients.", "solution": "Always map entities through explicit Response DTOs exposing only safe fields."},
                {"trap": "Over-architecting trivial pass-through CRUD endpoints into 10 layers of abstraction.", "solution": "Remain pragmatic; avoid unnecessary boilerplate when zero business transformation exists."}
            ],
            "udemy_title_tr": "Ders 22: Katmanlı Mimari - Controller, Service ve Repository",
            "udemy_title_en": "Lecture 22: Layered Architecture - Controller, Service & Repository",
            "udemy_slides_tr": [
                "Separation of Concerns (İlgi Alanlarının Ayrımı) nedir?",
                "3 Katmanın Görev Dağılımı: Resepsiyonist, Şef ve Kiler.",
                "Service katmanını HTTP bağımsız (framework-agnostic) tutmanın gücü.",
                "Canlı Demo: Spagetti Express rotasını 3 katmana refactor etmek."
            ],
            "udemy_slides_en": [
                "What is Separation of Concerns and why does it protect sanity?",
                "The 3-tier contract: Concierge, Chef, and Pantry Manager.",
                "Keeping Services transport-agnostic for universal reusability.",
                "Live demo: Refactoring a bloated Express route into 3 distinct layers."
            ],
            "udemy_demo_tr": "Tek dosyalık bir `app.post('/register')` kodunu açın. Adım adım `repository`, `service` ve `controller` dosyalarına bölün. Service katmanı için sahte bir repository ile 1 dakikada unit test yazarak çalıştığını gösterin.",
            "udemy_demo_en": "Open an monolithic Express route. Extract data queries into `UserRepository`, logic into `UserService`, and routing into `UserController`. Demonstrate writing an isolated unit test for `UserService` in 60 seconds.",
            "action_task_tr": "Mevcut projenizde Controller içinde doğrudan veritabanı sorgusu yapılan bir fonksiyonu bulun ve veritabanı kodunu bir Repository fonksiyonuna taşıyın.",
            "action_task_en": "Isolate an inline database query from an API route in your codebase and extract it into a dedicated repository class.",
            "quiz_tr": [
                {
                    "question": "3 Katmanlı Mimaride 'Service' katmanının temel sorumluluğu nedir?",
                    "options": [
                        "A) HTTP durum kodlarını (200, 404) belirlemek",
                        "B) Şirketin saf iş kurallarını (business logic) ve hesaplamalarını yürütmek",
                        "C) Doğrudan SQL sorgusu yazmak",
                        "D) CSS butonlarını renklendirmek"
                    ],
                    "answer": "B",
                    "explanation": "Service katmanı iş kurallarının kalbidir; ne HTTP protokolünden ne de veritabanının türünden etkilenmeden mantığı işletir."
                },
                {
                    "question": "Service fonksiyonuna `(req, res)` nesnelerini parametre olarak geçmek neden kötü bir mimari alışkanlıktır?",
                    "options": [
                        "A) Fonksiyonu yavaşlatması",
                        "B) Service katmanını Express'e ve HTTP protokolüne sıkı sıkıya bağlayarak CLI, kuyruk (queue) veya test ortamlarında yeniden kullanılmasını imkansız kılması",
                        "C) TypeScript'in hata vermesi",
                        "D) Monitörün kapanması"
                    ],
                    "answer": "B",
                    "explanation": "Service saf verilerle (DTO) çalışmalıdır; böylece aynı servis hem bir HTTP isteğinden hem de bir cron job veya kuyruk mesajından çağrılabilir."
                }
            ],
            "quiz_en": [
                {
                    "question": "In a 3-tier Layered Architecture, what is the sole mandate of the 'Service' layer?",
                    "options": [
                        "A) Evaluating HTTP status headers (200, 404)",
                        "B) Enforcing business rules, orchestrating domain workflows, and executing calculations",
                        "C) Assembling raw SQL query statements",
                        "D) Styling CSS UI buttons"
                    ],
                    "answer": "B",
                    "explanation": "The Service layer houses pure business logic, remaining agnostic of delivery protocols and database dialects."
                },
                {
                    "question": "Why is passing `(req, res)` objects directly into Service methods an architectural anti-pattern?",
                    "options": [
                        "A) It impairs compiler speed",
                        "B) It couples domain logic tightly to HTTP transports, preventing reuse in CLI scripts, background workers, or unit tests",
                        "C) TypeScript automatically rejects it",
                        "D) It induces display resolution drops"
                    ],
                    "answer": "B",
                    "explanation": "Services must accept transport-agnostic DTOs so the same business logic can be triggered by background queues or CLI scripts."
                }
            ]
        },

        # Chapter 23
        {
            "id": 23,
            "section_id": 4,
            "slug_tr": "ch23_state_yonetimi_ve_veri_akisi",
            "slug_en": "ch23_state_management_predictable_data_flow",
            "title_tr": "State Yönetimi & Veri Akışı: Kaosu Önlemek",
            "title_en": "State Management & Predictable Data Flow: Taming the Chaos",
            "subtitle_tr": "Prop Drilling, Global State ve Asenkron Durum Yönetimi Rehberi",
            "subtitle_en": "Overcoming Prop Drilling, Race Conditions, and Global State Antipathies",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Modern web uygulamalarında en çok bug nerede çıkar? Neden veritabanı veya sunucu değil, istemcideki 'State (Durum)' yönetimi başımızı ağrıtır?",
            "podcast_hook_en": "Why do over 70% of frontend defects trace back to mutability and chaotic state management rather than server-side errors?",
            "takeaways_tr": [
                "State (Durum), uygulamanın belirli bir andaki hafızasıdır; kontrolsüz mutasyonlar kaosa yol açar.",
                "Sunucu Durumu (Server State - React Query / SWR) ile İstemci Durumu (Client State - Zustand) birbirine karıştırılmamalıdır.",
                "Tek Yönlü Veri Akışı (Unidirectional Data Flow), durum değişikliklerini öngörülebilir ve izlenebilir kılar."
            ],
            "takeaways_en": [
                "State represents the application's memory at a given millisecond; unchecked mutations breed unpredictable bugs.",
                "Segregate Server State (React Query / TanStack Query) from purely local Client UI State (Zustand / Redux).",
                "Unidirectional Data Flow guarantees state mutations remain predictable, deterministic, and easily debugged."
            ],
            "story_tr": """Büyük bir ailenin ortak bir buzdolabı olduğunu düşünün.

Eğer evdeki 5 kişi de buzdolabındaki sütü kafasına göre kafaya dikip içerse, kimse sütün bittiğinden haberdar olmaz. Anne kahve yapacakken süt kutusunun boş olduğunu görünce çığlık atar! İşte bu **kontrolsüz mutable state**'tir.

Peki buzdolabının kapağına bir liste koysanız:
- Sütü alan kişi listeden bir çizgi çeker.
- Son süt bittiğinde otomatik olarak sipariş listesine eklenir.

Artık herkes ne olduğunu bilir ve sürpriz yaşanmaz!

Yazılımda Zustand, Redux veya React Query işte o buzdolabı listesidir. Verinin kim tarafından, ne zaman ve nasıl değiştirildiğini kayıt altına alır.""",
            "story_en": """Imagine a shared refrigerator in a house with 5 roommates.

If everyone drinks milk straight from the carton without telling anyone, somebody inevitably pours coffee only to find an empty carton. That is **uncontrolled mutable state**.

Now place a magnetic chalkboard on the refrigerator door:
- Taking a carton requires decrementing the count on the board.
- When the tally reaches zero, an automated grocery alert fires.

Surprises vanish because mutations are tracked through a single deterministic channel.

Modern state engines (Zustand, TanStack Query) act as that chalkboard, establishing single sources of truth for UI components.""",
            "mental_tr": """Modern State Ayrımı Matrisi:

```
┌────────────────────────────────────────┐
│             UYGULAMA VERİSİ            │
└──────────────────┬─────────────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
[1. SUNUCU DURUMU]     [2. İSTEMCİ DURUMU]
(Server State)         (Client State)
- API'den gelen veriler  - Modal açık mı?
- Önbellek, yenileme     - Tema (Koyu/Açık)
- Yükleniyor/Hata hali   - Form adımı
─────────────────────  ───────────────────
Araç: TanStack Query   Araç: Zustand / Context
```""",
            "mental_en": """The Modern State Segregation Model:

```
┌────────────────────────────────────────┐
│         APPLICATION STATE DOMAIN       │
└──────────────────┬─────────────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
[1. SERVER STATE]      [2. CLIENT UI STATE]
- Asynchronous API data - Is modal visible?
- Caching, revalidation - Dark / Light theme
- Background sync       - Stepper form index
─────────────────────  ───────────────────
Tool: TanStack Query   Tool: Zustand / useState
```""",
            "prompt_tr": """# ROL: Frontend Mimarisi ve React Uzmanı
Uygulamamızda hem sunucudan gelen ürün listesi var hem de kullanıcının sepet durumu var.

## GÖREV:
1. Neden ürün listesini `useEffect` ve `useState` ile yönetmenin kötü bir alışkanlık olduğunu açıkla.
2. Ürün listesini TanStack Query (React Query) kullanarak önbellekli ve otomatik yenilenen şekilde kodla.
3. Sepet durumunu (ekle/çıkar/toplam) hafif bir Zustand store'u olarak tasarla.""",
            "prompt_en": """# ROLE: Frontend Architecture & State Specialist
Our React application handles a catalog fetched from an API alongside a local shopping cart.

## TASK:
1. Explain why fetching data inside raw `useEffect` triggers race conditions and state sync bugs.
2. Implement catalog fetching using TanStack Query with caching and loading states.
3. Implement the shopping cart state using a clean, immutable Zustand store.""",
            "code_lang": "typescript",
            "code_naive": """// Kötü: useEffect ile veri çekmek (Race condition, önbellek yok, boilerplate dolu)
function ProductListNaive() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Bileşen unmount olursa memory leak ve race condition riski!
    fetch("/api/products")
      .then(res => res.json())
      .then(data => {
        setProducts(data);
        setLoading(false);
      });
  }, []); // Bağımlılıklar güncellenmediğinde bayat veri!
}""",
            "code_robust": """// 1. İSTEMCİ DURUMU: Zustand ile Sepet Yönetimi (cartStore.ts)
import { create } from "zustand";

interface CartItem {
  id: string;
  name: string;
  price: number;
}

interface CartStore {
  items: CartItem[];
  addItem: (item: CartItem) => void;
  clearCart: () => void;
  total: () => number;
}

export const useCartStore = create<CartStore>((set, get) => ({
  items: [],
  addItem: (item) => set((state) => ({ items: [...state.items, item] })),
  clearCart: () => set({ items: [] }),
  total: () => get().items.reduce((sum, item) => sum + item.price, 0)
}));

// 2. SUNUCU DURUMU: TanStack Query ile Ürün Çekme (products.hook.ts)
import { useQuery } from "@tanstack/react-query";

export function useProducts() {
  return useQuery({
    queryKey: ["products"],
    queryFn: async () => {
      const res = await fetch("/api/products");
      if (!res.ok) throw new Error("Ürünler yüklenemedi.");
      return (await res.json()) as CartItem[];
    },
    staleTime: 1000 * 60 * 5 // 5 dakika boyunca önbellekten anında sun
  });
}""",
            "code_notes_tr": "TanStack Query; otomatik önbellekleme (caching), arka planda yenileme (revalidation) ve yüklenme durumlarını tek satırda çözerken, Zustand yerel sepet hafızasını prop drilling olmadan yönetir.",
            "code_notes_en": "TanStack Query automatically manages caching, loading/error states, and background synchronization, while Zustand maintains local client state without prop drilling.",
            "pitfalls_tr": [
                {"trap": "Sunucudan gelen her API verisini Redux veya global state'e kopyalayıp senkronizasyon kaybetmek.", "solution": "Sunucu verisi için TanStack Query kullanın; Redux/Zustand'ı sadece gerçek UI durumları için saklayın."},
                {"trap": "React state'ini doğrudan mutasyona uğratmak (Örn: `state.items.push(item)`).", "solution": "State daima immutable (değişmez) güncellenmelidir (`[...state.items, item]`)."},
                {"trap": "Prop drilling yaparak bir veriyi 8 alt bileşene elle aktarmak.", "solution": "Derin hiyerarşilerde Zustand veya React Context kullanın."}
            ],
            "pitfalls_en": [
                {"trap": "Manually syncing server API responses into global Redux stores.", "solution": "Use TanStack Query for server state; reserve client stores strictly for UI state."},
                {"trap": "Mutating React state directly via `state.items.push()`.", "solution": "Always treat state as immutable, returning fresh references (`[...state.items, item]`)."},
                {"trap": "Prop drilling state across 8 nested component layers.", "solution": "Use lightweight stores like Zustand or React Context for cross-cutting state."}
            ],
            "udemy_title_tr": "Ders 23: State Yönetimi - TanStack Query ve Zustand ile Düzen",
            "udemy_title_en": "Lecture 23: State Management Mastery - TanStack Query & Zustand",
            "udemy_slides_tr": [
                "Frontend bug'larının %70'i neden State yönetiminden kaynaklanır?",
                "Server State (Sunucu) vs Client State (İstemci) ayrımı.",
                "useEffect veri çekme tuzağından TanStack Query'ye geçiş.",
                "Zustand ile 10 satırda global sepet yönetimi."
            ],
            "udemy_slides_en": [
                "Why 70% of UI defects trace back to mutability and chaotic state.",
                "Drawing the boundary: Server State vs. Client State.",
                "Retiring `useEffect` data fetching in favor of TanStack Query.",
                "Building a reactive shopping cart in 10 lines with Zustand."
            ],
            "udemy_demo_tr": "React uygulamasında iki bileşen açın. Biri sepete ürün eklesin, diğeri header'da sepet adedini göstersin. Zustand store'u ile prop aktarmadan anında güncellendiğini gösterin.",
            "udemy_demo_en": "Build a React component pair: an 'Add to Cart' button and a navigation badge. Connect both through a Zustand store and demonstrate instant reactive synchronization without prop drilling.",
            "action_task_tr": "Projenizde `useEffect` ile veri çektiğiniz bir yeri bulun ve TanStack Query `useQuery` kullanarak yeniden yazın.",
            "action_task_en": "Refactor a data-fetching `useEffect` hook in your project into a TanStack `useQuery` hook with automatic caching.",
            "quiz_tr": [
                {
                    "question": "React uygulamalarında sunucudan (API) gelen veriyi yönetmek için modern standart hangi araçtır?",
                    "options": [
                        "A) Sadece `useState` ve `useEffect`",
                        "B) TanStack Query (React Query) veya SWR gibi Sunucu Durumu (Server State) kütüphaneleri",
                        "C) jQuery",
                        "D) CSS Animations"
                    ],
                    "answer": "B",
                    "explanation": "TanStack Query önbellekleme, deduplication, retry ve otomatik senkronizasyon özelliklerini otomatik sunar."
                },
                {
                    "question": "React state'inde `state.users.push(newUser)` yazmak neden tehlikelidir?",
                    "options": [
                        "A) Kodun derlenmemesi",
                        "B) Dizinin referansı değişmediği için React'in değişikliği fark edememesi ve arayüzü yeniden render etmemesi (Bailout)",
                        "C) Bilgisayarın kilitlenmesi",
                        "D) Sadece Python'da hata vermesi"
                    ],
                    "answer": "B",
                    "explanation": "React sığ karşılaştırma (shallow equality) yapar. Dizi doğrudan mutasyona uğradığında referans değişmediği için render tetiklenmez."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the industry standard for managing remote API data in modern React applications?",
                    "options": [
                        "A) Handcrafted `useState` + `useEffect` fetching blocks",
                        "B) Server state engines like TanStack Query or SWR",
                        "C) jQuery AJAX calls",
                        "D) Keyframe CSS"
                    ],
                    "answer": "B",
                    "explanation": "Server state libraries provide declarative caching, request deduplication, and automatic background revalidation out of the box."
                },
                {
                    "question": "Why is invoking `state.users.push(newUser)` hazardous in React?",
                    "options": [
                        "A) Compilers refuse to parse arrays",
                        "B) Mutating objects in-place preserves memory references, causing React to miss changes and skip UI re-renders",
                        "C) It halts browser network threads",
                        "D) It only operates in Python runtimes"
                    ],
                    "answer": "B",
                    "explanation": "React relies on shallow reference equality. Mutating existing memory arrays fails to trigger reconciliation cycles."
                }
            ]
        },

        # Chapter 24
        {
            "id": 24,
            "section_id": 4,
            "slug_tr": "ch24_api_mimarisi_rest_graphql_grpc",
            "slug_en": "ch24_api_architecture_rest_graphql_grpc",
            "title_tr": "API Mimarisi: REST, GraphQL ve gRPC Karşılaştırması",
            "title_en": "API Design: REST, GraphQL, gRPC & Contract-First AI Generation",
            "subtitle_tr": "Hangi Protokolü Ne Zaman Seçmelisin? OpenAPI Şemalarıyla Tip Güvenliği",
            "subtitle_en": "Selecting the Right Protocol: Generating End-to-End Type Safety via OpenAPI",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "REST öldü mü? GraphQL her derde deva mı yoksa gRPC mikroservislerin gizli süper gücü mü?",
            "podcast_hook_en": "Is REST genuinely obsolete, is GraphQL a cure-all, or is gRPC the unsung champion of high-throughput distributed systems?",
            "takeaways_tr": [
                "REST basitliği ve HTTP önbelleklemesiyle kamusal API'lerin (Public API) kralıdır.",
                "GraphQL, mobil uygulamalarda aşırı veri çekme (Over-fetching) ve yetersiz veri çekme (Under-fetching) sorununu çözer.",
                "gRPC (Protocol Buffers), mikroservisler arasında ikili (binary) formatta HTTP/2 ile ışık hızında haberleşme sağlar."
            ],
            "takeaways_en": [
                "REST remains the undisputed standard for public APIs due to universal tooling and HTTP caching.",
                "GraphQL solves over-fetching and under-fetching dilemmas for complex mobile client frontends.",
                "gRPC leverages Protocol Buffers over HTTP/2 to deliver high-throughput, low-latency microservice communications."
            ],
            "story_tr": """Farklı ülkelere mektup gönderdiğinizi düşünün.

1. **REST:** Standart bir posta mektubudur. Zarfın üstünde adres yazar (URL), içine standart kağıt konur (JSON). Dünyadaki her postacı bunu anlar.
2. **GraphQL:** Kişiye özel alışveriş sipariş formudur. Forma tam olarak *"Bana sadece kırmızı kazağın bedenini ve fiyatını getir, kumaş bilgisini getirme"* yazarsınız; kurye tam istediklerinizi getirir.
3. **gRPC:** İki askeri üs arasındaki kriptolu fiber optik kablodur. İngilizce veya Türkçe konuşmaz; ikili (binary 0 ve 1) şifreli sinyallerle mikrosaniyede haberleşir.

Bir e-ticaret sitesi yapıyorsanız REST veya GraphQL seçersiniz. Ancak arka planda binlerce finansal işlemi konuşturan sunucularınız varsa gRPC seçersiniz.""",
            "story_en": """Consider three international communication channels:

1. **REST:** Standard postal airmail. The envelope has a clear address (URL), contains standard paper (JSON), and is understood by every postal system globally.
2. **GraphQL:** A customized procurement checklist. You instruct the courier: *"Retrieve only the size and price of the blue sweater; omit fabric composition."* You receive exactly what you requested.
3. **gRPC:** A dedicated fiber-optic link between two financial data centers. It bypasses human-readable text, streaming raw binary Protocol Buffers over HTTP/2 at sub-millisecond latencies.

For public web APIs, choose REST or GraphQL. For internal microservice pipelines handling millions of requests per second, choose gRPC.""",
            "mental_tr": """Protokol Karar Ağacı:

```
[Yeni Bir API Geliştirilecek]
             │
             ├── Kamuya açık genel API veya standart CRUD mu?
             │   └──> REST API (OpenAPI / Swagger ile)
             │
             ├── Karmaşık mobil ekranlar ve ilişkili veriler mi var?
             │   └──> GraphQL (Apollo / Yoga)
             │
             └── İç mikroservisler arası yüksek hızlı veri transferi mi?
                 └──> gRPC (Protocol Buffers)
```""",
            "mental_en": """API Architectural Decision Protocol:

```
[Architecting an Ingress/Egress Interface]
             │
             ├── Public consumer API or straightforward CRUD?
             │   └──> RESTful HTTP API (Documented via OpenAPI)
             │
             ├── Complex mobile frontends with nested relational payloads?
             │   └──> GraphQL (Single endpoint, client-defined schemas)
             │
             └── High-throughput internal microservice-to-microservice traffic?
                 └──> gRPC (Binary serialization over HTTP/2)
```""",
            "prompt_tr": """# ROL: API Mimarisi ve Entegrasyon Uzmanı
Bir ödeme platformu için 'Müşteri İşlemleri API'si tasarlıyoruz.

## GÖREV:
1. REST, GraphQL ve gRPC arasındaki farkları; gecikme (latency), ağ yükü (payload size) ve önbellekleme (caching) açısından karşılaştır.
2. Bu sistem için OpenAPI 3.0 (Swagger) uyumlu bir `POST /v1/payments` endpoint şeması (YAML) hazırla.
3. Bu şemadan TypeScript client tiplerinin nasıl otomatik türetileceğini (Contract-First) göster.""",
            "prompt_en": """# ROLE: API Systems Architect
We are architecting a Core Payments API.

## TASK:
1. Deliver a comparative breakdown of REST, GraphQL, and gRPC analyzing serialization latency, payload footprint, and caching.
2. Author an OpenAPI 3.0 YAML specification for `POST /v1/payments`.
3. Demonstrate a contract-first workflow auto-generating TypeScript client SDKs from this schema.""",
            "code_lang": "yaml",
            "code_naive": """# Kötü / Dokümante Edilmemiş REST: Tip yok, hata şeması belirsiz
/api/pay:
  post:
    description: Para ode
    responses:
      200:
        description: Basarili""",
            "code_robust": """openapi: 3.0.3
info:
  title: Core Payments API
  version: 1.0.0
paths:
  /v1/payments:
    post:
      summary: Yeni bir ödeme işlemi başlatır
      operationId: processPayment
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PaymentRequest'
      responses:
        '201':
          description: Ödeme başarıyla onaylandı
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaymentResponse'
        '400':
          description: Geçersiz parametreler veya yetersiz bakiye
components:
  schemas:
    PaymentRequest:
      type: object
      required: [amount, currency, sourceToken]
      properties:
        amount:
          type: number
          format: float
          minimum: 0.01
        currency:
          type: string
          enum: [USD, EUR, TRY]
        sourceToken:
          type: string
          example: "tok_visa_1234"
    PaymentResponse:
      type: object
      properties:
        paymentId:
          type: string
          format: uuid
        status:
          type: string
          enum: [SUCCEEDED, PENDING, FAILED]""",
            "code_notes_tr": "Contract-First yaklaşımında bu YAML dosyası yazıldıktan sonra `openapi-typescript` aracıyla hem frontend hem backend için tek tuşla sıfır hatayla TypeScript tipleri ve SDK üretilir.",
            "code_notes_en": "Under a contract-first paradigm, running `openapi-typescript` on this specification auto-generates client and server types, guaranteeing end-to-end synchronization without manual coordination.",
            "pitfalls_tr": [
                {"trap": "Basit bir blog sitesi için GraphQL kurup gereksiz N+1 sorgu karmaşasıyla boğuşmak.", "solution": "İhtiyaç yoksa REST ile başlayın; karmaşık veri grafikleri oluştuğunda GraphQL'e geçin."},
                {"trap": "REST API'de HTTP durum kodlarını (200, 400, 404, 500) görmezden gelip her hatada 200 OK içinde `{ error: true }` dönmek.", "solution": "HTTP standartlarına uyun; hataları doğru durum kodlarıyla iletin."},
                {"trap": "API sözleşmesini (OpenAPI) elle yazıp koddan koparmak.", "solution": "Şemayı ya koddan otomatik türetin ya da şemayı tek gerçeklik kaynağı kabul edip kodu şemadan üretin."}
            ],
            "pitfalls_en": [
                {"trap": "Adopting GraphQL for trivial CRUD apps and inheriting N+1 DataLoader complexity.", "solution": "Default to RESTful patterns unless nested heterogeneous queries genuinely justify GraphQL."},
                {"trap": "Returning HTTP 200 OK for application crashes accompanied by `{ error: true }`.", "solution": "Respect HTTP transport semantics: return 4xx for client faults and 5xx for server panics."},
                {"trap": "Manually authoring OpenAPI files disconnected from live application routes.", "solution": "Enforce automated contract generation from Zod/code or generate route skeletons from the schema."}
            ],
            "udemy_title_tr": "Ders 24: Modern API Mimarisi - REST, GraphQL ve gRPC",
            "udemy_title_en": "Lecture 24: Modern API Protocols - REST, GraphQL & gRPC",
            "udemy_slides_tr": [
                "API Protokolleri Karşılaştırması: REST vs GraphQL vs gRPC.",
                "Over-fetching ve Under-fetching problemlerini anlamak.",
                "Contract-First Yaklaşımı: OpenAPI ile Tip Güvenliği.",
                "Bölüm 4 Özeti: Yazılım Mimarisi ve Tasarım Kalıpları."
            ],
            "udemy_slides_en": [
                "Comparative analysis of API protocols: REST vs GraphQL vs gRPC.",
                "Demystifying over-fetching, under-fetching, and waterfall requests.",
                "The Contract-First philosophy: Type safety via OpenAPI schemas.",
                "Module 4 Recap: Software Architecture and Enterprise Design Patterns."
            ],
            "udemy_demo_tr": "Bir OpenAPI YAML dosyasından `openapi-typescript` CLI aracıyla 5 saniyede TypeScript tipleri üretin. Bu tipleri hem Express rotasında hem de fetch çağrısında kullanarak tam tip güvenliğini gösterin.",
            "udemy_demo_en": "Run `npx openapi-typescript schema.yaml -o api.d.ts`. Demonstrate importing generated types into both a client fetch wrapper and a backend controller, highlighting auto-complete fidelity.",
            "action_task_tr": "Projenizdeki en önemli 1 REST endpoint'i için Swagger / OpenAPI 3.0 uyumlu şema tanımı yazın veya Zod kullanarak şema türetin.",
            "action_task_en": "Draft an OpenAPI 3.0 JSON/YAML specification for one primary API endpoint in your current workspace.",
            "quiz_tr": [
                {
                    "question": "GraphQL'in geleneksel REST API'ye göre en belirgin avantajı nedir?",
                    "options": [
                        "A) Asla hata vermemesi",
                        "B) İstemcinin (Frontend/Mobil) tam olarak ihtiyaç duyduğu alanları talep edebilmesi (Over-fetching ve Under-fetching'i önlemesi)",
                        "C) Sadece Python'da çalışması",
                        "D) CSS yüklemesini hızlandırması"
                    ],
                    "answer": "B",
                    "explanation": "GraphQL istemcinin tek bir sorguyla sadece istediği alanları ve iç içe ilişkili nesneleri tek istekte alabilmesini sağlar."
                },
                {
                    "question": "İç mikroservisler arasında yüksek hız ve düşük gecikme gerektiğinde gRPC'nin tercih edilmesinin temel teknik sebebi nedir?",
                    "options": [
                        "A) Metin tabanlı JSON yerine Protocol Buffers (ikili veri) kullanması ve HTTP/2 üzerinden çalışması",
                        "B) Şifre gerektirmemesi",
                        "C) Sadece Google tarafından kullanılması",
                        "D) Veritabanı istememesi"
                    ],
                    "answer": "A",
                    "explanation": "gRPC, binary serialization (Protocol Buffers) ve HTTP/2 multiplexing sayesinde JSON'a kıyasla çok daha küçük paket boyutu ve yüksek hız sunar."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the defining capability of GraphQL over standard REST endpoints?",
                    "options": [
                        "A) Immune to application errors",
                        "B) Enabling client applications to request precisely the fields required, eliminating over-fetching and under-fetching",
                        "C) Exclusivity to Python environments",
                        "D) Speeding up CSS bundle delivery"
                    ],
                    "answer": "B",
                    "explanation": "GraphQL lets clients declare response shapes dynamically, fetching nested relational data in a single network round-trip."
                },
                {
                    "question": "Why is gRPC favored for internal inter-service communication over JSON-REST?",
                    "options": [
                        "A) It utilizes binary Protocol Buffers serialization over HTTP/2 instead of text-based JSON",
                        "B) It bypasses authentication credentials",
                        "C) It is usable exclusively within Google",
                        "D) It eliminates backend databases"
                    ],
                    "answer": "A",
                    "explanation": "Protocol Buffers serialize into compact binary representations transported over multiplexed HTTP/2 streams, minimizing CPU overhead and wire latency."
                }
            ]
        }
    ]
