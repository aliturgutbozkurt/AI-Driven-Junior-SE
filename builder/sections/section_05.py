"""
Section 5: Veritabanları, Modelleme & Backend (Chapters 25 to 30)
"""

def get_section_chapters():
    return [
        # Chapter 25
        {
            "id": 25,
            "section_id": 5,
            "slug_tr": "ch25_sql_vs_nosql_ai_karar_matrisi",
            "slug_en": "ch25_sql_vs_nosql_ai_tradeoff_analysis",
            "title_tr": "İlişkisel (SQL) vs. İlişkisel Olmayan (NoSQL): Hangisi Ne Zaman?",
            "title_en": "SQL vs. NoSQL: Picking the Right Persistence Engine with AI",
            "subtitle_tr": "PostgreSQL mi MongoDB mi? Ezbere Seçimlerden Kurtulma Kılavuzu",
            "subtitle_en": "PostgreSQL vs. MongoDB: Escaping Hype and Choosing via Workload Metrics",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Yeni başlayan geliştiriciler neden her projeye hemen MongoDB açmaya çalışır ve finansal işlemlerde NoSQL kullanmak nasıl bir felakettir?",
            "podcast_hook_en": "Why do novice developers default to MongoDB for everything, and why is handling financial ledgers in NoSQL an existential risk?",
            "takeaways_tr": [
                "SQL ilişkisel bütünlüğü (ACID) ve katı şemaları korurken; NoSQL esnek şemalar ve yatay ölçeklenme için tasarlanmıştır.",
                "Eğer verileriniz arasında ilişkiler (Kullanıcı -> Sipariş -> Fatura) varsa, varsayılan tercihiniz her zaman PostgreSQL olmalıdır.",
                "Modern PostgreSQL, JSONB desteği sayesinde NoSQL'in esnekliğini SQL'in güvenilirliğiyle birleştirir."
            ],
            "takeaways_en": [
                "SQL enforces relational integrity and strict ACID transactions; NoSQL prioritizes schema mutability and horizontal partition tolerance.",
                "Whenever entities possess relational joins (User -> Order -> Invoice), PostgreSQL is your resilient default.",
                "Modern PostgreSQL with native JSONB indices absorbs 90% of use cases historically cited to justify NoSQL."
            ],
            "story_tr": """Bir banka kasasını ve bir oyuncak sepetini düşünün.

Banka kasasında (SQL) her kuruşun yeri bellidir. Kim kime ne kadar para gönderdiyse, Ahmet'in hesabından düşüldüğü saniyede Mehmet'in hesabına eklenmelidir. İkisi aynı anda gerçekleşmezse işlem iptal edilir (ACID).

Oyuncak sepetinde (NoSQL) ise kural yoktur! Pelüş ayı, lego parçası, uzaktan kumandalı araba hepsini aynı sepete atabilirsiniz. Hızlıca eşya atmak veya sepeti kucaklayıp başka bir odaya taşımak (yatay ölçeklenme) çok kolaydır.

Eğer banka parasını oyuncak sepetine koyarsanız, paralar kaybolur! Ancak IoT sensörlerinden saniyede 10.000 log topluyorsanız sepet tam aradığınız şeydir.""",
            "story_en": """Consider a bank vault versus a children's toy chest.

Inside the bank vault (SQL), every currency note is serialized and ledgered. When transfering funds from Alice to Bob, Alice's balance must decrement at the exact microsecond Bob's balance increments. If a power cut interrupts the operation midway, the system rolls back to the prior state (ACID).

In a children's toy chest (NoSQL), there are no rigid dividers. You toss in building blocks, stuffed animals, and puzzle pieces together. Ingesting arbitrary items rapidly and dragging the chest across rooms is effortless.

Storing banking transactions inside a toy chest invites accounting fraud. But if you are ingesting high-throughput telemetry logs from 50,000 IoT weather sensors, the toy chest is optimal.""",
            "mental_tr": """SQL vs NoSQL Karşılaştırma Rehberi:

```
[İhtiyaç Analizi]
       │
       ├── Veri ilişkisel mi? (Tablolar arası Foreign Key var mı?)
       │   └──> SQL (PostgreSQL, MySQL)
       │
       ├── Finansal işlem veya katı tutarlılık (ACID) şart mı?
       │   └──> SQL (PostgreSQL)
       │
       ├── Veri şeması sürekli değişen dökümanlar mı? (CMS, Dinamik Formlar)
       │   └──> NoSQL (MongoDB, CouchDB) VEYA Postgres JSONB
       │
       └── Milyonlarca geçici oturum veya cache mi?
           └──> Key-Value NoSQL (Redis)
```""",
            "mental_en": """The Database Selection Heuristic:

```
[Workload Assessment]
       │
       ├── Heavy relational joins? Foreign key integrity mandatory?
       │   └──> Relational SQL (PostgreSQL)
       │
       ├── Financial ledgers requiring strict ACID transactional atomicity?
       │   └──> Relational SQL (PostgreSQL)
       │
       ├── Semi-structured, polymorphic documents with dynamic schemas?
       │   └──> Document Store (MongoDB) OR PostgreSQL JSONB
       │
       └── Sub-millisecond session state or ephemeral caches?
           └──> In-Memory Key-Value NoSQL (Redis)
```""",
            "prompt_tr": """# ROL: Baş Veritabanı Mimarı
Yeni bir SaaS platformu kuruyoruz. Sistemde kullanıcılar, faturalar, abonelik planları ve kullanıcıların yüklediği dinamik anket formları olacak.

## GÖREV:
1. Bu sistem için PostgreSQL mi yoksa MongoDB mi seçmeliyiz? Trade-off (ödünleşim) analizi yap.
2. Neden PostgreSQL + JSONB kombinasyonunun her iki dünyanın en iyi yönlerini birleştirdiğini açıkla.
3. Örnek bir kullanıcı ve anket şemasını SQL ve JSONB ile tasarla.""",
            "prompt_en": """# ROLE: Lead Database Architect
We are launching a B2B SaaS application handling users, recurring subscription invoices, and dynamic user-authored survey forms.

## TASK:
1. Deliver a technical trade-off evaluation comparing PostgreSQL against MongoDB for this hybrid workload.
2. Explain how PostgreSQL with native JSONB columns achieves the best of relational consistency and document flexibility.
3. Draft a hybrid SQL schema modeling relational users and polymorphic survey responses.""",
            "code_lang": "sql",
            "code_naive": """-- Kötü NoSQL Yaklaşımı: İlişkisel veriyi MongoDB'de iç içe gömmek (Denormalization Kabusu)
-- Kullanıcı bir adresini güncellediğinde, 50 farklı sipariş dökümanındaki gömülü adresi elle güncellemek gerekir!
{
  "_id": "order_123",
  "user": { "id": "u1", "name": "Ali", "address": "Eski Adres" },
  "total": 450.00
}""",
            "code_robust": """-- PostgreSQL ile Hibrit Mükemmellik: Katı İlişkiler + Esnek JSONB
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE invoices (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
    amount NUMERIC(10, 2) NOT NULL,
    status VARCHAR(50) DEFAULT 'PENDING',
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Dinamik ve Şemasız Veri İçin JSONB Kolonu
CREATE TABLE survey_responses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    -- Anket soruları ve yanıtları dinamiktir; şema zorunluluğu yok!
    answers JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- JSONB Alanı Üzerinde GIN İndeksi ile Işık Hızında Arama
CREATE INDEX idx_survey_answers ON survey_responses USING GIN (answers);""",
            "code_notes_tr": "PostgreSQL sayesinde hem finansal fatura verisi `REFERENCES users(id)` ile katı ilişkisel güvencede tutulur, hem de dinamik anket yanıtları `JSONB` kolonunda esnekçe saklanıp `GIN` indeksiyle aranabilir.",
            "code_notes_en": "PostgreSQL delivers relational integrity for financial billing tables (`REFERENCES users(id)`) while absorbing dynamic survey documents via `JSONB` with inverted `GIN` indices.",
            "pitfalls_tr": [
                {"trap": "Daha proje başlamadan 'MongoDB daha modern' deyip ilişkisel sistemi NoSQL'e taşımak.", "solution": "Aksi için çok güçlü bir sebep yoksa varsayılan olarak her zaman PostgreSQL ile başlayın."},
                {"trap": "NoSQL'de ilişkisel tabloları simüle etmeye çalışıp elle `populate` veya `lookup` yazmak.", "solution": "Eğer `JOIN` yapmaya ihtiyaç duyuyorsanız yanlış veritabanını seçmişsiniz demektir; SQL'e geçin."},
                {"trap": "SQL veritabanında para tutarlarını FLOAT olarak saklamak.", "solution": "Para tutarları için daima `NUMERIC` veya `DECIMAL` tipi kullanın."}
            ],
            "pitfalls_en": [
                {"trap": "Assuming MongoDB is inherently 'more modern' than relational engines.", "solution": "Default to PostgreSQL for standard business domains unless specific document constraints dictate otherwise."},
                {"trap": "Emulating relational joins in document stores via manual client loops or complex `$lookup` stages.", "solution": "If your domain model is fundamentally relational, migrate to SQL."},
                {"trap": "Storing financial balances as floating point numbers in SQL tables.", "solution": "Always use exact `NUMERIC` or `DECIMAL` columns for currency values."}
            ],
            "udemy_title_tr": "Ders 25: SQL vs NoSQL - Veritabanı Seçim Rehberi",
            "udemy_title_en": "Lecture 25: SQL vs NoSQL - The Pragmatic Persistence Decision",
            "udemy_slides_tr": [
                "SQL ve NoSQL arasındaki felsefe farkı: ACID vs BASE.",
                "İlişkisel Bütünlük (Foreign Key) neden hayat kurtarır?",
                "PostgreSQL JSONB: NoSQL esnekliğini SQL'de kullanmak.",
                "Canlı SQL: GIN indeksi ile JSON içinde sorgu çalıştırmak."
            ],
            "udemy_slides_en": [
                "Philosophical divergence: ACID guarantees vs. BASE eventual consistency.",
                "Why relational foreign keys prevent orphaned records and data corruption.",
                "PostgreSQL JSONB: Marrying document flexibility with relational reliability.",
                "Live demo: Querying indexed JSONB payloads with SQL containment operators."
            ],
            "udemy_demo_tr": "PostgreSQL veritabanında JSONB kolonuna sahip bir tablo açın. `WHERE answers @> '{\"rating\": 5}'` sorgusunu çalıştırarak JSON içindeki bir alanın milisaniye altında nasıl filtrelendiğini gösterin.",
            "udemy_demo_en": "Create a table with a JSONB column in PostgreSQL. Insert sample survey documents and execute `WHERE answers @> '{\"score\": 10}'`, demonstrating fast index scans.",
            "action_task_tr": "Projenizdeki veritabanı şemasını açın. Eğer NoSQL kullanıyorsanız tablolar arası ilişki kurup kurmadığınızı; SQL kullanıyorsanız gereksiz tablolar yerine JSONB kullanılabilecek alanları analiz edin.",
            "action_task_en": "Audit your project's persistence layer: identify if relational joins are awkwardly emulated in NoSQL or if dynamic JSON fields could simplify rigid SQL tables.",
            "quiz_tr": [
                {
                    "question": "Veritabanlarında 'ACID' kısaltmasının 'A' harfi (Atomicity) neyi garanti eder?",
                    "options": [
                        "A) Veritabanının atom bombasına dayanıklı olduğunu",
                        "B) Bir transaction içindeki tüm adımların ya tamamen başarılı olacağını ya da tek bir hata durumunda tüm işlemlerin geri alınacağını (ya hep ya hiç)",
                        "C) Sadece Python ile çalıştığını",
                        "D) Tabloların otomatik silineceğini"
                    ],
                    "answer": "B",
                    "explanation": "Atomicity (Bütünlük), ilişkili işlemlerin bölünemez bir bütün olduğunu; başarısızlık durumunda veritabanının önceki temiz durumuna geri döndürüleceğini garanti eder."
                },
                {
                    "question": "PostgreSQL'in `JSONB` kolon tipi ile standart `JSON` tipi arasındaki temel fark nedir?",
                    "options": [
                        "A) Hiçbir farkı yoktur",
                        "B) JSONB veriyi ikili (binary) formatta saklar ve GIN indeksleri ile alan bazlı hızlı arama yapılmasını sağlar",
                        "C) JSONB sadece sayılar saklayabilir",
                        "D) JSONB daha yavaş çalışır"
                    ],
                    "answer": "B",
                    "explanation": "JSONB, JSON verisini parçalanmış ikili formatta tutar ve indeksleme desteği sayesinde devasa JSON belgeleri içinde anında filtreleme imkanı sunar."
                }
            ],
            "quiz_en": [
                {
                    "question": "What invariant is guaranteed by the 'A' (Atomicity) in relational ACID transactions?",
                    "options": [
                        "A) Hardware immunity to physical shock",
                        "B) An all-or-nothing execution contract: every mutation succeeds, or the entire transaction rolls back completely",
                        "C) Exclusive compilation in Python runtimes",
                        "D) Automated schema pruning"
                    ],
                    "answer": "B",
                    "explanation": "Atomicity guarantees that multi-step transactions execute as an indivisible unit; partial failure triggers a complete rollback."
                },
                {
                    "question": "What is the technical differentiator between PostgreSQL `JSONB` and standard `JSON` types?",
                    "options": [
                        "A) They are identical aliases",
                        "B) `JSONB` parses JSON into a decomposed binary representation enabling fast indexing via GIN",
                        "C) `JSONB` accepts only primitive numbers",
                        "D) `JSONB` is deprecated"
                    ],
                    "answer": "B",
                    "explanation": "`JSONB` stores decomposed binary data, allowing operators to leverage GIN indices for sub-millisecond document lookups."
                }
            ]
        },

        # Chapter 26
        {
            "id": 26,
            "section_id": 5,
            "slug_tr": "ch26_veri_modelleme_ve_er_diyagramlari_ai",
            "slug_en": "ch26_schema_design_entity_relations_via_ai",
            "title_tr": "Veri Modelleme & ER Diyagramlarını AI ile Tasarlamak",
            "title_en": "Schema Design & Entity Relationships via Natural Language",
            "subtitle_tr": "1:1, 1:N ve N:M İlişkilerini Doğru Kurarak Veri Tutarlılığını Sağlamak",
            "subtitle_en": "Structuring 1:1, 1:N, and N:M Cardinalities to Guarantee Data Integrity",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Birçok junior mühendis N:M (Çoka-Çok) ilişkileri kurarken neden ara tabloyu (Junction Table) unutur ve AI ile kusursuz ER diyagramı nasıl çizdirilir?",
            "podcast_hook_en": "Why do junior engineers frequently stumble when modeling Many-to-Many relationships, and how can natural language prompts generate bulletproof ER diagrams?",
            "takeaways_tr": [
                "Veri modelleme, kod yazmadan önce gerçek dünyanın nesnelerini ve kurallarını tablolara aktarma sanatıdır.",
                "1:N (Bire-Çok) ilişkide yabancı anahtar (Foreign Key) daima 'Çok' olan tarafa konur.",
                "N:M (Çoka-Çok) ilişkiler doğrudan kurulamaz; arada iki foreign key tutan bir ara tablo (Junction Table) zorunludur."
            ],
            "takeaways_en": [
                "Data modeling translates real-world business constraints into relational integrity constraints before any code is typed.",
                "In 1:N cardinalities, the foreign key anchor always resides on the 'Many' side of the relationship.",
                "N:M relationships cannot exist directly in relational engines; they mandate an intermediate Junction (Join) table."
            ],
            "story_tr": """Bir okul hayal edin:
- Her öğrencinin tek bir kimlik kartı vardır: **Bire-Bir (1:1)**
- Bir öğretmenin onlarca öğrencisi olabilir: **Bire-Çok (1:N)**
- Peki öğrenciler ve dersler? Bir öğrenci 5 farklı derse girer, bir derste 30 farklı öğrenci vardır! İşte bu **Çoka-Çok (N:M)** ilişkidir!

Eğer öğrenci tablosunun içine dersin adını yazarsanız, öğrenci 5 ders aldığında öğrencinin adını 5 kez tekrar yazmak zorunda kalırsınız! 

Çözüm: Ortaya bir sınıf yoklama defteri koymaktır (Junction Table). Defterde sadece: *"Öğrenci 101, Ders 201'e kayıtlıdır"* yazar.

Veri tabanı tasarımı, bu ilişkileri mantıklı defterlere bölme sanatıdır.""",
            "story_en": """Consider a university campus:
- Each student has exactly one official biometric ID: **One-to-One (1:1)**
- A department head advises multiple undergraduate students: **One-to-Many (1:N)**
- What about students and lecture courses? A single student enrolls in 5 courses, and a single course contains 40 students: **Many-to-Many (N:M)**!

If you attempt to jam course titles directly into the student table, you must duplicate that student record 5 times for every enrolled class, corrupting data integrity.

The relational solution: introduce an enrollment registrar ledger (Junction Table). Each row states simply: *`student_id 101` is enrolled in `course_id 201`*.

Schema design is the disciplined art of organizing business records into normalized ledgers.""",
            "mental_tr": """İlişki Türleri ve Yabancı Anahtar (Foreign Key) Kuralları:

```
1. BİRE-BİR (1:1):
   [Kullanıcı (User)] <───> [Kullanıcı Profili (Profile)]
   * Foreign Key profil tablosuna konur ve UNIQUE yapılır.

2. BİRE-ÇOK (1:N):
   [Müşteri (Customer)] 1 <─── N [Siparişler (Orders)]
   * Foreign Key daima 'Çok' tarafına (Orders tablosuna customer_id) konur.

3. ÇOKA-ÇOK (N:M):
   [Öğrenciler] N <─── [Kayıtlar (Enrollments)] ───> M [Dersler]
   * Ara tablo (Junction Table) her iki tablonun ID'sini tutar.
```""",
            "mental_en": """Relational Cardinalities & Foreign Key Placement:

```
1. ONE-TO-ONE (1:1):
   [User] 1 <───> 1 [UserProfile]
   * Foreign key resides in `profiles` with an enforced `UNIQUE` constraint.

2. ONE-TO-MANY (1:N):
   [Customer] 1 <─── N [Orders]
   * Foreign key always anchors on the 'Many' table (`orders.customer_id`).

3. MANY-TO-MANY (N:M):
   [Student] N <─── [CourseEnrollment] ───> M [Course]
   * Junction table pairs compound foreign keys: `(student_id, course_id)`.
```""",
            "prompt_tr": """# ROL: Veritabanı Mimarı ve ER Uzmanı
Bir 'Online Kurs ve Eğitmen Platformu' (Udemy benzeri) için veritabanı şeması tasarlayacağız.

## GEREKSİNİMLER:
- Bir eğitmenin birden fazla kursu olabilir (1:N).
- Bir kursun birden fazla kategorisi ve bir kategorinin birden fazla kursu olabilir (N:M).
- Kullanıcılar kurslara kaydolabilmelidir (N:M).
- Her kursun video dersleri (Lessons) sırayla listelenmelidir (1:N).

## GÖREV:
1. Bu sistemin Mermaid ERD (Entity Relationship Diagram) şemasını çiz.
2. Prisma ORM formatında `schema.prisma` dosyasını foreign key ve index'leriyle eksiksiz yaz.""",
            "prompt_en": """# ROLE: Lead Database Modeler
We are designing the relational schema for an online learning platform.

## REQUIREMENTS:
- An instructor authors multiple courses (1:N).
- Courses and categories have a Many-to-Many relationship (N:M).
- Students enroll in multiple courses (N:M).
- Courses contain ordered video lessons (1:N).

## TASK:
1. Deliver a Mermaid.js Entity-Relationship diagram.
2. Provide the complete, production-grade `schema.prisma` definition with compound keys and indices.""",
            "code_lang": "prisma",
            "code_naive": """// Kötü Tasarım: Çoka-Çok ilişkiyi string array olarak saklamak
model Course {
  id          String   @id @default(uuid())
  title       String
  categories  String[] // HATA: Arama yapılamaz, kategori adı değişirse tüm kurslar bozulur!
  studentIds  String[] // HATA: 50.000 öğrenci kaydolduğunda döküman patlar!
}""",
            "code_robust": """// Profesyonel Prisma Şeması: İlişkisel Bütünlük ve İndeksleme
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id           String       @id @default(uuid())
  email        String       @unique
  fullName     String
  taughtCourses Course[]    @relation("InstructorCourses")
  enrollments  Enrollment[]
  createdAt    DateTime     @default(now())
}

model Course {
  id           String       @id @default(uuid())
  title        String
  instructorId String
  instructor   User         @relation("InstructorCourses", fields: [instructorId], references: [id])
  lessons      Lesson[]
  enrollments  Enrollment[]
  categories   CourseCategory[]
  createdAt    DateTime     @default(now())

  @@index([instructorId])
}

model Lesson {
  id        String   @id @default(uuid())
  courseId  String
  course    Course   @relation(fields: [courseId], references: [id], onDelete: Cascade)
  title     String
  order     Int
  videoUrl  String

  @@index([courseId, order])
}

// N:M İlişkisi İçin Ara Tablo (Junction Table)
model Enrollment {
  userId     String
  courseId   String
  user       User     @relation(fields: [userId], references: [id], onDelete: Cascade)
  course     Course   @relation(fields: [courseId], references: [id], onDelete: Cascade)
  enrolledAt DateTime @default(now())

  @@id([userId, courseId]) // Bir kullanıcı aynı kursa iki kez kaydolamaz!
}

model Category {
  id      String           @id @default(uuid())
  name    String           @unique
  courses CourseCategory[]
}

model CourseCategory {
  courseId   String
  categoryId String
  course     Course   @relation(fields: [courseId], references: [id], onDelete: Cascade)
  category   Category @relation(fields: [categoryId], references: [id], onDelete: Cascade)

  @@id([courseId, categoryId])
}""",
            "code_notes_tr": "`@@id([userId, courseId])` bileşik anahtarı (compound key) sayesinde bir öğrencinin aynı kursa mükerrer kaydolması veritabanı seviyesinde imkansız kılınmıştır. `onDelete: Cascade` ile kurs silindiğinde derslerinin öksüz (orphaned) kalması engellenir.",
            "code_notes_en": "The compound primary key `@@id([userId, courseId])` prevents duplicate enrollments at the engine level. `onDelete: Cascade` rules prevent orphaned records when a parent entity is purged.",
            "pitfalls_tr": [
                {"trap": "Çoka-çok ilişkilerde ID listesini JSON veya virgülle ayrılmış string olarak tek bir kolona tıkıştırmak.", "solution": "Her zaman iki foreign key içeren standart bir ara tablo (Junction Table) oluşturun."},
                {"trap": "Foreign Key alanlarına indeks koymayı unutmak.", "solution": "Prisma'da `@@index([foreignKey])` veya SQL'de `CREATE INDEX` ile arama hızını garanti edin."},
                {"trap": "Silme (Delete) kurallarını belirlememek ve veritabanında öksüz (orphan) kayıtlar bırakmak.", "solution": "İş mantığına göre `ON DELETE CASCADE` veya `ON DELETE RESTRICT` kurallarını açıkça tanımlayın."}
            ],
            "pitfalls_en": [
                {"trap": "Packing foreign ID arrays into comma-separated strings or loose JSON blobs.", "solution": "Always model Many-to-Many relationships via a normalized Junction table."},
                {"trap": "Failing to index foreign key columns.", "solution": "Always add `@@index([foreignKey])` to prevent full table scans during join operations."},
                {"trap": "Neglecting referential deletion constraints, leaving orphaned records.", "solution": "Declare explicit `ON DELETE CASCADE` or `RESTRICT` rules on all foreign keys."}
            ],
            "udemy_title_tr": "Ders 26: Veri Modelleme - ER Diyagramları ve Prisma Şeması",
            "udemy_title_en": "Lecture 26: Schema Modeling - ER Diagrams & Production Prisma Models",
            "udemy_slides_tr": [
                "Veri modelleme nedir? Gerçek dünyayı tablolara dökmek.",
                "1:1, 1:N ve N:M ilişkilerinin matematiksel kuralları.",
                "Junction Table (Ara Tablo) ve Compound Primary Key kullanımı.",
                "Prisma ORM ile 5 dakikada kurumsal şema oluşturmak."
            ],
            "udemy_slides_en": [
                "What is relational schema design? Mapping business entities to tables.",
                "Cardinality rules: 1:1, 1:N, and N:M unpacked.",
                "Junction tables and composite primary keys in action.",
                "Generating enterprise Prisma schemas in 5 minutes via natural language prompts."
            ],
            "udemy_demo_tr": "Mermaid.js ile bir e-ticaret ER diyagramı çizin. Ardından AI asistanına bu diyagramı verip hatasız bir `schema.prisma` üretmesini sağlayın ve `npx prisma format` ile doğrulayın.",
            "udemy_demo_en": "Author a Mermaid ER diagram representing courses and students. Pipe it to an AI model to generate a valid `schema.prisma` file, then run `npx prisma format` to verify syntax.",
            "action_task_tr": "Kendi projeniz için Mermaid.js formatında en az 4 tablodan oluşan bir ER diyagramı çizin ve markdown önizlemesinde inceleyin.",
            "action_task_en": "Draft a 4-entity Mermaid ER diagram for your current project, including 1:N and N:M cardinalities.",
            "quiz_tr": [
                {
                    "question": "İlişkisel veritabanlarında Çoka-Çok (Many-to-Many) bir ilişkiyi modellemenin standart yolu nedir?",
                    "options": [
                        "A) Tüm ID'leri virgülle ayırıp tek bir hücreye yazmak",
                        "B) Her iki tablonun birincil anahtarlarını (Primary Key) yabancı anahtar (Foreign Key) olarak tutan bir ara tablo (Junction Table) oluşturmak",
                        "C) Veritabanını silip baştan kurmak",
                        "D) Sadece NoSQL kullanmak"
                    ],
                    "answer": "B",
                    "explanation": "N:M ilişkiler, her iki tarafın ilişkisini satır bazında tutan bir ara tablo (Junction Table) ile iki adet 1:N ilişkiye dönüştürülerek modellenir."
                },
                {
                    "question": "Bir tabloda `ON DELETE CASCADE` kuralı tanımlandığında ne gerçekleşir?",
                    "options": [
                        "A) Bilgisayar yeniden başlar",
                        "B) Ana tablodaki kayıt silindiğinde, ona bağlı olan tüm alt tablodaki ilişkili kayıtlar da otomatik olarak güvenle silinir",
                        "C) Tablo şifrelenir",
                        "D) Silme işlemi tamamen yasaklanır"
                    ],
                    "answer": "B",
                    "explanation": "CASCADE silme kuralı, ebeveyn kayıt silindiğinde geride öksüz (orphan) kayıtlar kalmasını önlemek için çocuk kayıtları da siler."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the standard relational mechanism for implementing a Many-to-Many (N:M) relationship?",
                    "options": [
                        "A) Packing IDs into comma-separated text strings",
                        "B) Introducing a Junction table pairing foreign keys pointing to both participating entities",
                        "C) Reinstalling the database daemon",
                        "D) Forcing migration to document stores"
                    ],
                    "answer": "B",
                    "explanation": "Relational engines resolve N:M relationships by creating an intermediate Junction table composed of two 1:N foreign key pairs."
                },
                {
                    "question": "What operational behavior occurs when a foreign key defines `ON DELETE CASCADE`?",
                    "options": [
                        "A) The machine reboots",
                        "B) Deleting a parent row automatically deletes all related child rows in dependent tables",
                        "C) The database encrypts its storage volume",
                        "D) Deletions are strictly prohibited"
                    ],
                    "answer": "B",
                    "explanation": "`CASCADE` deletion guarantees that child records linked to a deleted parent entity are cleaned up automatically."
                }
            ]
        },

        # Chapter 27
        {
            "id": 27,
            "section_id": 5,
            "slug_tr": "ch27_sql_ustaligi_ve_indeks_optimizasyonu",
            "slug_en": "ch27_high_performance_sql_and_query_optimization",
            "title_tr": "SQL Ustalığı: Karmaşık Sorgular, İndeksleme ve AI Query Optimizer",
            "title_en": "High-Performance SQL: Advanced Joins, Indexing & AI Query Optimization",
            "subtitle_tr": "EXPLAIN ANALYZE Okuyarak 10 Saniyelik Sorguları 5 Milisaniyeye Düşürmek",
            "subtitle_en": "Deciphering EXPLAIN ANALYZE to Slash Query Latencies from 10 Seconds to 5ms",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Veritabanına indeks eklemek sorguları 1000 kat hızlandırıyorsa, neden tüm kolonlara indeks eklemiyoruz? Gizli bedel nedir?",
            "podcast_hook_en": "If database indices accelerate query lookups by 1,000x, why don't we index every single column? What is the hidden write cost?",
            "takeaways_tr": [
                "İndeks eklemek okuma (SELECT) hızını katbekat artırırken, her yazma (INSERT/UPDATE) işleminde ek CPU ve disk yükü getirir.",
                "`EXPLAIN ANALYZE` çıktısındaki 'Seq Scan' (Ardışık Tarama) milyonlarca satırda sunucuyu boğan en büyük tehlikedir.",
                "AI modelleri yavaş SQL sorgularını ve EXPLAIN planlarını analiz ederek en ideal B-Tree veya Composite indeksleri önerebilir."
            ],
            "takeaways_en": [
                "Indices multiply SELECT speeds exponentially, but degrade INSERT, UPDATE, and DELETE throughput due to B-Tree balancing costs.",
                "Encountering a 'Seq Scan' (Sequential Table Scan) inside an `EXPLAIN ANALYZE` output on high-cardinality tables indicates missing indices.",
                "Feeding query execution plans into AI models enables precise B-Tree and Composite index recommendations."
            ],
            "story_tr": """1000 sayfalık kalın bir tıp ansiklopedisini düşünün.

Kitabın en arkasında alfabetik bir **Fihrist / Dizin (İndeks)** vardır. "Kalp krizi" kelimesini arıyorsanız, fihristten "K" harfine bakar ve doğrudan sayfa 412'yi açarsınız (İndeks Taraması - Index Scan). 5 saniye sürer!

Eğer o fihrist olmasaydı ne yapardınız? Sayfa 1'den başlayıp sayfa 1000'e kadar tüm sayfaları tek tek okumak zorunda kalırdınız! (Ardışık Tarama - Sequential Scan). 3 saat sürerdi!

Ama dikkat: Ansiklopediye yeni bir sayfa eklendiğinde (INSERT), arkadaki fihristi de baştan sona silip yeniden alfabetik düzenlemek gerekir! 

İşte bu yüzden her kolona indeks konmaz; sadece sık aranan kritik kolonlara konur.""",
            "story_en": """Picture a 1,000-page medical encyclopedia.

At the very back rests an alphabetical **Index**. To find 'Myocardial Infarction', you jump to 'M' in the index and flip directly to page 412 (Index Scan). It takes 4 seconds.

Without that index, you would be forced to read every word starting from page 1 all the way to page 1,000 (Sequential Table Scan). It would take hours.

However, consider the cost: every time a medical researcher updates a paragraph or inserts a new page (INSERT / UPDATE), the entire rear alphabetical index must be recalculated and rewritten.

This is why experienced engineers index judiciously: prioritize frequently queried filters and foreign keys, leaving write-heavy columns unindexed.""",
            "mental_tr": """SQL İndeksleme Mantığı (B-Tree):

```
Sorgu: SELECT * FROM users WHERE email = 'ali@test.com';

SENARYO A: İndeks Yok (Sequential Scan)
[Satır 1] ──> [Satır 2] ──> ... ──> [Satır 5.000.000] (Tüm disk okunur, 8 saniye sürer!)

SENARYO B: B-Tree İndeksi Var (Index Scan)
                   [ Root: L-Z ]
                  /             \\
           [ A-K ]               [ M-Z ]
           /
   [ 'ali@test.com' ──> Satır Adresi: Block 42, Offset 8 ] (Sadece 3 adımda bulunur, 2 milisaniye!)
```""",
            "mental_en": """The B-Tree Index Traversal Model:

```
Query: SELECT * FROM orders WHERE status = 'COMPLETED' AND created_at > '2026-01-01';

SCENARIO A: No Index (Sequential Table Scan)
[Row 1] ──> [Row 2] ──> ... ──> [Row 10,000,000] (Disk I/O saturated; 12.4 seconds)

SCENARIO B: Composite B-Tree Index `(status, created_at)`
                     [ Root Node ]
                    /             \\
         [ PENDING ]               [ COMPLETED ]
                                  /             \\
                       [ 2025 Orders ]       [ >= 2026 Orders ] ──> Direct Pointers (3ms!)
```""",
            "prompt_tr": """# ROL: PostgreSQL Veritabanı Performans Tuning Uzmanı
Aşağıdaki SQL sorgusu 2 milyon satırlık `orders` tablosunda 7.5 saniye sürüyor.

## YAVAŞ SORGU:
```sql
SELECT id, user_id, total, created_at 
FROM orders 
WHERE status = 'PAID' AND created_at >= '2026-01-01'
ORDER BY created_at DESC 
LIMIT 20;
```

## EXPLAIN ANALYZE ÇIKTISI:
`Seq Scan on orders (cost=0.00..45210.00 rows=152000 width=32) (actual time=12.50..7450.21 ms)`

## GÖREV:
1. Bu sorgunun neden bu kadar yavaş olduğunu açıkla.
2. Bu sorguyu 5 milisaniyenin altına indirecek tam Composite Index (Bileşik İndeks) SQL komutunu yaz.
3. İndeks sıralamasının (status, created_at) neden önemli olduğunu açıkla.""",
            "prompt_en": """# ROLE: PostgreSQL Performance Tuning Specialist
This query takes 7.5 seconds on an `orders` table with 2 million rows.

## SLOW QUERY:
```sql
SELECT id, user_id, total, created_at 
FROM orders 
WHERE status = 'PAID' AND created_at >= '2026-01-01'
ORDER BY created_at DESC 
LIMIT 20;
```

## EXPLAIN ANALYZE OUTPUT:
`Seq Scan on orders (cost=0.00..45210.00 rows=152000 width=32) (actual time=12.50..7450.21 ms)`

## TASK:
1. Diagnose the execution bottleneck.
2. Provide the exact composite index statement to reduce execution time below 5ms.
3. Explain why the column order in `(status, created_at DESC)` matters.""",
            "code_lang": "sql",
            "code_naive": """-- Kötü Çözüm: Ayrı ayrı iki bağımsız indeks oluşturmak (Bitmap Index Scan karmaşası)
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_orders_created ON orders(created_at);
-- Veritabanı iki indeksi birleştirmeye çalışırken gereksiz CPU yakar!""",
            "code_robust": """-- Mükemmel Çözüm: Sorgu Filtresine ve Sıralamasına Birebir Uyumlu Composite Index
-- Sıralama: Önce eşitlik (equality: status), sonra aralık ve sıralama (range: created_at)
CREATE INDEX idx_orders_status_created 
ON orders (status, created_at DESC);

-- İsteğe Bağlı: Index-Only Scan için kapsayıcı indeks (Covering Index)
-- Tabloya hiç gitmeden sadece indeksten yanıt döner:
CREATE INDEX idx_orders_optimized 
ON orders (status, created_at DESC) 
INCLUDE (user_id, total);""",
            "code_notes_tr": "`Composite Index` oluşturulurken altın kural: Önce `=` ile aranan eşitlik kolonu (`status`), ardından `>=` veya `ORDER BY` ile kullanılan kolondur (`created_at DESC`). `INCLUDE` eki ise tabloya (heap) gitme ihtiyacını tamamen ortadan kaldırır (Index-Only Scan).",
            "code_notes_en": "The composite indexing golden rule: equality columns first (`status = 'PAID'`), followed by range/order columns (`created_at DESC`). Adding `INCLUDE (user_id, total)` achieves an Index-Only Scan, bypassing heap lookups entirely.",
            "pitfalls_tr": [
                {"trap": "Tablodaki her kolona ezbere indeks koyup INSERT işlemlerini süründürmek.", "solution": "Sadece WHERE, JOIN ve ORDER BY koşullarında sıkça kullanılan kolonları indeksleyin."},
                {"trap": "İndekslenen kolon üzerinde fonksiyon çalıştırmak (Örn: `WHERE LOWER(email) = 'ali'`).", "solution": "Fonksiyonlar standart B-Tree indeksini bozar; ya veriyi küçük harf kaydedin ya da Expression Index (`CREATE INDEX ON users(LOWER(email))`) oluşturun."},
                {"trap": "Production ortamında kilitlenme (lock) yaratan indeks komutları çalıştırmak.", "solution": "Canlı veritabanında indeks eklerken daima `CREATE INDEX CONCURRENTLY` kullanın."}
            ],
            "pitfalls_en": [
                {"trap": "Indexing every single table column indiscriminately, destroying write throughput.", "solution": "Index only columns participating in high-frequency WHERE, JOIN, and ORDER BY clauses."},
                {"trap": "Applying mutations to indexed columns in WHERE clauses (e.g., `WHERE LOWER(email) = '...'`).", "solution": "Function wrappers invalidate standard B-Trees; normalize inputs on write or create an expression index."},
                {"trap": "Running synchronous indexing commands on production tables under high traffic.", "solution": "Always append `CONCURRENTLY` (`CREATE INDEX CONCURRENTLY`) to prevent blocking table writes."}
            ],
            "udemy_title_tr": "Ders 27: SQL Ustalığı - EXPLAIN ANALYZE ve İndeks Optimizasyonu",
            "udemy_title_en": "Lecture 27: SQL Mastery - Deciphering EXPLAIN ANALYZE & Composite Indices",
            "udemy_slides_tr": [
                "Veritabanı fihristi nedir? B-Tree indeks nasıl çalışır?",
                "EXPLAIN ANALYZE okuma rehberi: Seq Scan vs Index Scan.",
                "Bileşik İndekslerde (Composite Index) kolon sırası kuralı.",
                "Production güvenliği: CREATE INDEX CONCURRENTLY."
            ],
            "udemy_slides_en": [
                "Understanding database indexes: How B-Trees navigate pages.",
                "Deciphering EXPLAIN ANALYZE telemetry: Seq Scan vs. Index Scan.",
                "The column ordering hierarchy in composite indices.",
                "Zero-downtime indexing in production via `CONCURRENTLY`."
            ],
            "udemy_demo_tr": "PostgreSQL'de 1.000.000 satırlık mock sipariş tablosu oluşturun. İndeks olmadan sorguyu çalıştırıp 8 saniye sürdüğünü ve 'Seq Scan' verdiğini gösterin. Ardından composite index ekleyip sürenin 3 milisaniyeye düştüğünü canlı kanıtlayın.",
            "udemy_demo_en": "Seed a Postgres table with 1,000,000 records. Run a multi-condition query showing an 8-second Seq Scan. Add a composite index and watch latency plunge to 3ms on live telemetry.",
            "action_task_tr": "Projenizdeki en yavaş çalışan veritabanı sorgusunu tespit edin. Başına `EXPLAIN ANALYZE` ekleyerek 'Seq Scan' olup olmadığını kontrol edin ve gerekiyorsa indeks ekleyin.",
            "action_task_en": "Execute `EXPLAIN ANALYZE` on your heaviest production query. Audit the plan for sequential scans and propose a targeted composite index.",
            "quiz_tr": [
                {
                    "question": "Bir SQL sorgusunun yürütme planında 'Seq Scan' (Sequential Scan) görülmesi ne anlama gelir?",
                    "options": [
                        "A) Sorgunun ışık hızında çalıştığını",
                        "B) Veritabanının uygun bir indeks bulamadığı için tablodaki tüm satırları baştan sona tek tek taramak zorunda kaldığını",
                        "C) Sadece Python'da hata olduğunu",
                        "D) Tablonun tamamen boş olduğunu"
                    ],
                    "answer": "B",
                    "explanation": "Seq Scan, aranan koşula uygun indeks bulunmadığında tablodaki tüm satırların diskten taranmasıdır; büyük tablolarda çok ciddi performans kaybıdır."
                },
                {
                    "question": "Canlı (production) bir PostgreSQL veritabanında tabloyu kilitlemeden ve yazma işlemlerini durdurmadan indeks eklemek için hangi anahtar kelime kullanılır?",
                    "options": [
                        "A) FAST",
                        "B) CONCURRENTLY",
                        "C) ASYNC",
                        "D) NOWAIT"
                    ],
                    "answer": "B",
                    "explanation": "`CREATE INDEX CONCURRENTLY` komutu, tablo üzerinde okuma ve yazma kilitlerini engeller; arka planda güvenle indeks inşa edilmesini sağlar."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is signaled by the presence of a 'Seq Scan' in a database execution plan?",
                    "options": [
                        "A) The query executed in sub-millisecond time",
                        "B) The engine lacked an appropriate index and was forced to scan every single disk block in the table",
                        "C) A fatal syntax error in Python",
                        "D) The table contains zero rows"
                    ],
                    "answer": "B",
                    "explanation": "Sequential scans evaluate every row in the table, saturating I/O and creating severe bottlenecks on high-volume tables."
                },
                {
                    "question": "Which modifier instructs PostgreSQL to build an index in the background without blocking concurrent writes?",
                    "options": [
                        "A) FAST",
                        "B) CONCURRENTLY",
                        "C) ASYNC",
                        "D) NOWAIT"
                    ],
                    "answer": "B",
                    "explanation": "`CREATE INDEX CONCURRENTLY` avoids acquiring exclusive table write locks during index construction."
                }
            ]
        },

        # Chapter 28
        {
            "id": 28,
            "section_id": 5,
            "slug_tr": "ch28_ormler_ve_n_arti_1_problemi",
            "slug_en": "ch28_orms_and_the_n_plus_one_problem",
            "title_tr": "ORM'ler (Prisma, TypeORM, SQLAlchemy) ve Gizli Tehlike: N+1 Problemi",
            "title_en": "ORMs & Conquering the N+1 Query Problem with AI Audits",
            "subtitle_tr": "Tek Bir Sayfa İçin Veritabanına 1000 Sorgu Gönderme Tuzağından Kurtulmak",
            "subtitle_en": "Preventing ORMs from Firing 1,000 Unnecessary Queries for a Single Page Load",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "ORM'ler geliştiricilerin hayatını kolaylaştıran harika araçlar mı, yoksa arka planda sessizce binlerce sorgu atan tehlikeli bir canavar mı?",
            "podcast_hook_en": "Are Object-Relational Mappers (ORMs) an indispensable productivity gift or a stealthy source of crippling database saturation via N+1 queries?",
            "takeaways_tr": [
                "ORM (Object-Relational Mapping), nesne yönelimli kod ile ilişkisel veritabanı arasında köprü kurar; ancak SQL bilme zorunluluğunu ortadan kaldırmaz.",
                "N+1 problemi, bir liste çekildikten sonra her elemanın ilişkili verisini döngü içinde ayrı ayrı sorgulama hatasıdır (1 + N sorgu).",
                "`include` (Eager Loading) veya `JOIN` kullanarak N+1 sorgu felaketini tek bir birleşik sorguya indirebilirsiniz."
            ],
            "takeaways_en": [
                "ORMs bridge object models with relational tables, but never absolve developers of mastering underlying SQL mechanics.",
                "The N+1 problem occurs when an application executes 1 query for a parent dataset followed by N individual queries inside an iteration loop.",
                "Applying Eager Loading (`include`, `joinedload`, or `select_related`) collapses N+1 round-trips into a single optimized query."
            ],
            "story_tr": """Bir süpermarkete gittiğinizi ve 50 farklı ürün alacağınızı düşünün.

Kasaya geldiniz. Sepetteki her ürünü tek tek geçirip ödemek yerine; her bir ürün için ayrı ayrı otoparka gidip arabanıza bir ürün bırakıp, tekrar kasaya dönüp ikinci ürünü alıp, tekrar otoparka gidip gelseydiniz ne olurdu? 50 kez arabaya gidip gelirdiniz ve gününüz biterdi!

İşte **N+1 Sorgu Problemi** tam olarak budur:
Geliştirici 100 kullanıcının siparişlerini listelemek ister. 
1. Önce 100 kullanıcıyı çeker (1 sorgu).
2. Sonra `for` döngüsünün içinde her kullanıcının siparişini tek tek veritabanına sorar (100 ayrı sorgu!).
Toplamda 101 sorgu atılır! Veritabanı sunucusu nefes alamaz hale gelir.

Oysa *"Tüm kullanıcıları ve ilişkili siparişlerini tek seferde getir"* derseniz arabanıza tüm poşetleri tek seferde yüklersiniz.""",
            "story_en": """Imagine grocery shopping for 50 household items.

At checkout, instead of paying for all items together and wheeling your cart to your car, you purchase a carton of eggs, walk out to your vehicle, deposit the eggs, walk back into the store, purchase a carton of milk, walk out to your car... repeating this 50 consecutive times. You would waste your entire afternoon.

That is the notorious **N+1 Query Problem**:
An application requests 100 users and their latest orders.
1. It queries the `users` table once (1 query).
2. Inside an unmonitored code loop, it queries the `orders` table individually for each user (N = 100 queries).
Result: 101 network round-trips for a single HTTP request! The database server collapses under connection pool exhaustion.

Eager Loading allows you to pack the cart once, returning both datasets in a single optimized query.""",
            "mental_tr": """N+1 Probleminin Tespiti ve Çözümü:

```
YAVAŞ (N+1 Sorgu):
1. Sorgu: SELECT * FROM users LIMIT 50;
2. Sorgu: SELECT * FROM orders WHERE user_id = 1;
3. Sorgu: SELECT * FROM orders WHERE user_id = 2;
...
51. Sorgu: SELECT * FROM orders WHERE user_id = 50;
─────────────────────────────────────────────────────────────
HIZLI (Eager Loading - Tek Sorgu):
SELECT users.*, orders.* 
FROM users 
LEFT JOIN orders ON orders.user_id = users.id 
LIMIT 50;
```""",
            "mental_en": """Anatomy of the N+1 Bottleneck & Resolution:

```
NAIVE LAZY FETCH (N+1 Round-trips):
Query 1: SELECT * FROM users LIMIT 100;
Query 2: SELECT * FROM profiles WHERE user_id = 1;
Query 3: SELECT * FROM profiles WHERE user_id = 2;
...
Query 101: SELECT * FROM profiles WHERE user_id = 100;
─────────────────────────────────────────────────────────────
OPTIMIZED EAGER FETCH (Single Round-trip):
SELECT u.*, p.* 
FROM users u 
INNER JOIN profiles p ON p.user_id = u.id 
LIMIT 100;
```""",
            "prompt_tr": """# ROL: ORM ve Veritabanı Optimizasyon Uzmanı
Aşağıdaki Prisma / TypeScript fonksiyonu veritabanına yüzlerce gereksiz sorgu atmaktadır.

## YAVAŞ KOD:
```typescript
export async function getUsersWithPosts() {
  const users = await prisma.user.findMany({ take: 100 });
  const results = [];
  for (const user of users) {
    // N+1 tuzağı! Her kullanıcı için ayrı sorgu atılıyor!
    const posts = await prisma.post.findMany({ where: { authorId: user.id } });
    results.push({ ...user, posts });
  }
  return results;
}
```

## GÖREV:
1. N+1 problemini açıkla ve arka planda neden 101 sorgu çalıştığını göster.
2. Prisma'nın `include` (Eager Loading) özelliğini kullanarak bu işlemi tek bir veritabanı turuna (round-trip) indirecek optimize kodu yaz.""",
            "prompt_en": """# ROLE: Database & ORM Performance Lead
The following Prisma code triggers an N+1 query storm.

## SLOW SNIPPET:
```typescript
export async function getUsersWithPosts() {
  const users = await prisma.user.findMany({ take: 100 });
  const results = [];
  for (const user of users) {
    const posts = await prisma.post.findMany({ where: { authorId: user.id } });
    results.push({ ...user, posts });
  }
  return results;
}
```

## TASK:
1. Explain the N+1 mechanics resulting in 101 queries.
2. Refactor using Prisma's `include` API to collapse this into an optimized eager fetch.""",
            "code_lang": "typescript",
            "code_naive": """// N+1 Tuzağı: Döngü içinde await sorgusu çalıştırmak
export async function getArticlesWithCommentsNaive() {
  const articles = await prisma.article.findMany({ take: 50 });

  // 50 makale için 50 kez veritabanına gidip gelir (Toplam 51 sorgu!)
  return await Promise.all(articles.map(async (article) => {
    const comments = await prisma.comment.findMany({ where: { articleId: article.id } });
    return { ...article, comments };
  }));
}""",
            "code_robust": """// Eager Loading ile Optimize Edilmiş Sürüm: Tek veya 2 birleşik sorgu
export async function getArticlesWithCommentsOptimized() {
  // Prisma arka planda tek bir JOIN veya IN sorgusuyla çözer
  return await prisma.article.findMany({
    take: 50,
    include: {
      comments: {
        select: {
          id: true,
          content: true,
          createdAt: true
        },
        orderBy: { createdAt: 'desc' },
        take: 5 // Sadece en son 5 yorumu alarak payload'ı hafiflet
      }
    }
  });
}""",
            "code_notes_tr": "`include` bloğu sayesinde Prisma tüm makaleleri ve ilişkili yorumları tek bir SQL sorgusunda çeker. 51 veritabanı turu (round-trip) 1 tura iner; sayfa yüklenme süresi 1500 ms'den 20 ms'ye düşer.",
            "code_notes_en": "Leveraging `include` causes Prisma to resolve relational data via an efficient SQL `JOIN` or optimized batch lookup. Latency collapses from 1,500ms down to 20ms.",
            "pitfalls_tr": [
                {"trap": "Döngü (for/map) içinde veritabanı sorgusu (`await db...`) çalıştırmak.", "solution": "Döngü içinde asla sorgu çalıştırmayın; veriyi döngüden önce `include` veya `IN (...)` ile topluca çekin."},
                {"trap": "ORM loglarını (query logging) kapatıp arkada ne kadar sorgu çalıştığını takip etmemek.", "solution": "Geliştirme ortamında ORM SQL loglarını (`log: ['query']`) mutlaka açık tutun."},
                {"trap": "İhtiyaç duyulmayan tüm devasa kolonları (`SELECT *`) çekmek.", "solution": "`select` anahtarı ile sadece sayfada gösterilecek alanları çekerek bellek tasarrufu yapın."}
            ],
            "pitfalls_en": [
                {"trap": "Invoking database queries (`await db...`) inside loops.", "solution": "Never query persistence stores within loops; batch fetch records upfront via `include` or SQL `IN (...)`."},
                {"trap": "Disabling ORM query logging in development environments.", "solution": "Enable verbose SQL logging (`log: ['query']`) to inspect generated queries during local testing."},
                {"trap": "Pulling entire database rows indiscriminately (`SELECT *`).", "solution": "Use projection (`select: { id: true, title: true }`) to minimize memory bloat."}
            ],
            "udemy_title_tr": "Ders 28: ORM Optimizasyonu - N+1 Sorgu Tehlikesini Yok Etmek",
            "udemy_title_en": "Lecture 28: ORM Optimization - Eliminating the N+1 Query Storm",
            "udemy_slides_tr": [
                "ORM nedir ve yazılımcıları nasıl tembelleştirir?",
                "N+1 Probleminin anatomisi: 1 sorgu yerine 101 sorgu atmak.",
                "Eager Loading (include) vs Lazy Loading mantığı.",
                "Canlı SQL Log İncelemesi: 50 sorguyu 1 sorguya indirmek."
            ],
            "udemy_slides_en": [
                "The productivity and abstraction trade-offs of modern ORMs.",
                "Anatomy of the N+1 bottleneck: Why 1 query turns into 101 round-trips.",
                "Eager Loading (`include`) vs. Lazy Loading.",
                "Live demo: Collapsing 50 queries into 1 using Prisma query telemetry."
            ],
            "udemy_demo_tr": "Prisma'da `log: ['query']` aktif edin. Önce döngü içinde Post çeken fonksiyonu çalıştırıp terminali dolduran onlarca SQL sorgusunu gösterin. Ardından `include` ekleyip terminalde tek bir SQL sorgusu aktığını gösterin.",
            "udemy_demo_en": "Initialize Prisma with `log: ['query']`. Execute a loop-based relation lookup and observe the terminal cascade of SQL logs. Refactor to `include` and observe a single clean query.",
            "action_task_tr": "Projenizde ORM sorgu loglarını aktif edin. Bir sayfayı açtığınızda arka planda kaç adet SQL sorgusu tetiklendiğini terminalden sayın.",
            "action_task_en": "Enable debug query logging in your project's ORM configuration. Audit the number of database queries executed during a single page render.",
            "quiz_tr": [
                {
                    "question": "Veritabanı geliştirmede 'N+1 Problemi' tam olarak neyi ifade eder?",
                    "options": [
                        "A) Veritabanına 1 ekleme yapınca N tanesinin silinmesini",
                        "B) Ana kayıtları getirmek için 1 sorgu, ardından döngü içinde her bir kaydın ilişkili verisini getirmek için N adet ayrı sorgu çalıştırılması felaketini",
                        "C) Sadece Python'da geçerli bir matematik teoremini",
                        "D) Tabloların adlarının 1 artırılmasını"
                    ],
                    "answer": "B",
                    "explanation": "N+1 problemi, ilişkili verilerin toplu çekilmek yerine döngü içinde her satır için ayrı ayrı sorgulanarak veritabanının gereksiz yere boğulmasıdır."
                },
                {
                    "question": "Prisma veya TypeORM gibi ORM'lerde N+1 problemini çözmek için kullanılan temel yaklaşım hangisidir?",
                    "options": [
                        "A) Eager Loading (`include` veya `relations` kullanarak ilişkili veriyi tek seferde çekmek)",
                        "B) Veritabanını kapatıp açmak",
                        "C) Tüm verileri frontend'e aktarmak",
                        "D) Sadece string veri kullanmak"
                    ],
                    "answer": "A",
                    "explanation": "Eager Loading, ilişkili kayıtların ana sorguyla birlikte JOIN veya optimize toplu sorgularla tek seferde belleğe alınmasını sağlar."
                }
            ],
            "quiz_en": [
                {
                    "question": "What specifically constitutes the 'N+1 Query Problem' in backend engineering?",
                    "options": [
                        "A) Deleting N records whenever 1 record is created",
                        "B) Executing 1 query for primary records followed by N distinct queries inside a loop for each associated record",
                        "C) A mathematical formula unique to Python compilers",
                        "D) Incrementing primary keys by one"
                    ],
                    "answer": "B",
                    "explanation": "The N+1 problem occurs when child relationships are fetched per-iteration rather than in a batched, joined operation."
                },
                {
                    "question": "What architectural technique resolves the N+1 problem in ORMs like Prisma or TypeORM?",
                    "options": [
                        "A) Eager Loading (using `include` or join configurations to fetch relations upfront)",
                        "B) Restarting the database server",
                        "C) Delegating joins to browser client state",
                        "D) Storing records as raw strings"
                    ],
                    "answer": "A",
                    "explanation": "Eager loading instructs the ORM to resolve child records upfront using joins or grouped `IN` queries."
                }
            ]
        },

        # Chapter 29
        {
            "id": 29,
            "section_id": 5,
            "slug_tr": "ch29_cache_mekanizmalari_ve_redis_mimarisi",
            "slug_en": "ch29_caching_strategies_redis_architecture",
            "title_tr": "Cache Mekanizmaları: Redis ile Yıldırım Hızında Yanıtlar",
            "title_en": "Caching Strategies & Redis Architecture: Sub-Millisecond Speeds",
            "subtitle_tr": "Cache-Aside Deseni ve 'Cache Invalidation' Zorluğunu Aşmak",
            "subtitle_en": "Conquering Cache-Aside Patterns, TTL Strategies, and Invalidation Hazards",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "'Bilgisayar bilimlerinde sadece iki zor şey vardır: Cache Invalidation ve isimlendirme.' Peki Redis ile önbellek yönetirken bayat (stale) veriyi nasıl önleriz?",
            "podcast_hook_en": "Phil Karlton famously said: 'There are only two hard things in Computer Science: cache invalidation and naming things.' How does modern Redis architecture solve this?",
            "takeaways_tr": [
                "En hızlı veritabanı sorgusu, hiç yapılmayan veritabanı sorgusudur; sık okunan veriler RAM'de (Redis) tutulmalıdır.",
                "Cache-Aside deseni: Önce Redis'e bak (Cache Hit), yoksa veritabanından oku ve Redis'e yaz (Cache Miss).",
                "Her önbellek anahtarının mutlaka bir yaşam süresi (TTL - Time to Live) olmalıdır; sonsuz önbellek bellek patlamasına yol açar."
            ],
            "takeaways_en": [
                "The fastest database query is the one you never execute; store read-heavy data in memory (Redis).",
                "The Cache-Aside pattern: Inspect cache first (Hit); on miss, query database, populate cache, and return payload.",
                "Every cached key requires a definitive Time-To-Live (TTL); unbounded caching leads to memory exhaustion and stale reads."
            ],
            "story_tr": """Bir kütüphane görevlisini hayal edin.

Günde 500 öğrenci gelip aynı kitabı soruyor: *"Harry Potter 1. kitap var mı?"*

Eğer kütüphaneci her seferinde 3 kat yukarı çıkıp, tozlu rafların arasında 15 dakika yürüyüp kitabı kontrol edip gelseydi akşamı zor ederdi! (Veritabanı Disk Erişimi).

Akıllı bir kütüphaneci ne yapar? O çok sorulan kitabın bir kopyasını hemen masasının çekmecesine koyar! Biri sorduğunda çekmeceyi açıp 2 saniyede gösterir (Redis RAM Belleği). 

Ancak bir kural vardır: Eğer kitap kütüphaneden atılırsa veya güncellenirse, çekmecedeki kitabı da hemen yenilemek gerekir (Cache Invalidation).""",
            "story_en": """Picture a librarian at an academic reference desk.

500 students arrive daily asking for the exact same reference volume: *"Do you have the 2026 Tax Code Manual?"*

If the librarian walks up 3 flights of stairs, navigates dusty aisles for 10 minutes, and carries the book down for every single student, operations grind to a halt (Disk Database Access).

An experienced librarian keeps a copy directly inside their desk drawer. When asked, they produce it in 2 seconds (In-Memory Redis Cache).

The challenge: if congress updates the tax statute, the librarian must instantly purge the obsolete manual from their drawer (Cache Invalidation).""",
            "mental_tr": """Cache-Aside Deseni Akışı:

```
[İstemci İsteği: GET /products/123]
                  │
                  ▼
        [1. Redis'i Kontrol Et]
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   [CACHE HIT]         [CACHE MISS]
 (Veri Redis'te var)  (Veri Redis'te yok)
        │                   │
  [Anında Yanıt]      [2. PostgreSQL'den Oku]
  (0.8 ms)                  │
                            ▼
                      [3. Redis'e Yaz (TTL: 1 saat)]
                            │
                            ▼
                      [4. İstemciye Dön (45 ms)]
```""",
            "mental_en": """The Cache-Aside Interaction Loop:

```
[Client Request: GET /api/v1/products/42]
                   │
                   ▼
        [1. Query Redis In-Memory]
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
   [CACHE HIT]           [CACHE MISS]
 (Found in Redis RAM)   (Key absent or expired)
        │                     │
 [Return Payload]       [2. Read from PostgreSQL]
    (< 1 ms)                  │
                              ▼
                        [3. Store in Redis with TTL]
                              │
                              ▼
                        [4. Return to Client]
```""",
            "prompt_tr": """# ROL: Dağıtık Sistemler ve Cache Mimarı
Node.js ve Redis (ioredis) kullanarak bir 'Ürün Detay Önbellek Servisi' yazacağız.

## GÖREV:
1. 'Cache-Aside' desenini uygulayan tip güvenli bir fonksiyon yaz.
2. Ürün verisini Redis'te saklarken 1 saatlik TTL (Time to Live) ekle.
3. Ürün güncellendiğinde (`updateProduct`) Redis'teki eski anahtarı anında silen (Invalidation) fonksiyonu hazırla.""",
            "prompt_en": """# ROLE: Distributed Systems & Caching Architect
Implement a Product Caching Service using TypeScript and Redis (ioredis).

## TASK:
1. Implement the Cache-Aside pattern with strict return types.
2. Store JSON payloads with an explicit 1-hour TTL.
3. Provide an invalidation helper (`invalidateProductCache`) to purge stale keys on updates.""",
            "code_lang": "typescript",
            "code_naive": """// Kötü Cache: TTL yok (sonsuza kadar bellekte kalır) ve güncellemede silinmiyor (bayat veri)
export async function getProductNaive(id: string) {
  const cached = await redis.get(`product:${id}`);
  if (cached) return JSON.parse(cached);

  const product = await db.product.findUnique({ where: { id } });
  // TTL YOK! Bellek dolunca Redis çöker; ürün fiyatı değişse de eski fiyat kalır!
  await redis.set(`product:${id}`, JSON.stringify(product));
  return product;
}""",
            "code_robust": """import Redis from "ioredis";

const redis = new Redis(process.env.REDIS_URL || "redis://localhost:6379");
const CACHE_TTL_SECONDS = 3600; // 1 Saat

export class ProductCacheService {
  private static getKey(id: string): string {
    return `cache:product:${id}`;
  }

  // 1. Cache-Aside Okuma
  static async getProduct(id: string): Promise<Product | null> {
    const key = this.getKey(id);

    try {
      const cached = await redis.get(key);
      if (cached) {
        return JSON.parse(cached) as Product; // Cache Hit (1 ms)
      }
    } catch (err) {
      console.warn("Redis okuma hatası, DB'ye yönlendiriliyor:", err);
    }

    // Cache Miss: Veritabanından oku
    const product = await db.product.findUnique({ where: { id } });
    if (!product) return null;

    // Redis'e TTL ile kaydet (Fail-safe)
    try {
      await redis.set(key, JSON.stringify(product), "EX", CACHE_TTL_SECONDS);
    } catch (err) {
      console.error("Redis yazma hatası:", err);
    }

    return product;
  }

  // 2. Cache Invalidation (Güncelleme Anında Temizleme)
  static async invalidate(id: string): Promise<void> {
    try {
      await redis.del(this.getKey(id));
    } catch (err) {
      console.error("Cache invalidation hatası:", err);
    }
  }
}""",
            "code_notes_tr": "Kıdemli yaklaşımda; Redis çöktüğünde uygulamanın durmaması için `try/catch` ile sessiz devralma (fallback to DB) sağlanmış, `EX` parametresi ile 1 saatlik yaşam süresi zorunlu kılınmış ve güncelleme anında `del` ile bayat veri riski önlenmiştir.",
            "code_notes_en": "The production implementation wraps cache operations in fail-safe try/catch blocks so Redis network outages fall back to the database gracefully. `EX` guarantees eviction, and `invalidate` purges stale keys.",
            "pitfalls_tr": [
                {"trap": "Redis'e TTL (Time-To-Live) vermeden anahtar kaydetmek ve sunucu belleğini patlatmak.", "solution": "İstisnasız her cache anahtarına makul bir TTL süresi verin."},
                {"trap": "Redis çöktüğünde tüm backend uygulamasının da çökmesine izin vermek.", "solution": "Redis çağrılarını try/catch ile sarın; Redis yoksa doğrudan veritabanına gidin (Graceful Degradation)."},
                {"trap": "Kullanıcıya özel hassas verileri genel (public) cache anahtarlarında saklamak.", "solution": "Cache anahtarlarına kullanıcı ID'si ekleyin (`user:123:profile`) ve hassas verileri şifreleyin."}
            ],
            "pitfalls_en": [
                {"trap": "Writing cache keys without TTLs, inducing out-of-memory crashes.", "solution": "Always configure an eviction TTL on every cached item."},
                {"trap": "Letting Redis connection errors crash the main web application thread.", "solution": "Implement graceful degradation: catch cache exceptions and fall back to database queries."},
                {"trap": "Caching user-specific private payloads under global shared keys.", "solution": "Namespace keys explicitly with user IDs (`user:42:profile`) to prevent cross-tenant data leakage."}
            ],
            "udemy_title_tr": "Ders 29: Cache Stratejileri - Redis ile Yıldırım Hızı",
            "udemy_title_en": "Lecture 29: Caching Strategies - Sub-Millisecond Speeds with Redis",
            "udemy_slides_tr": [
                "Neden en hızlı sorgu hiç yapılmayan sorgudur?",
                "Cache-Aside Deseni: Hit, Miss ve TTL kavramları.",
                "Cache Invalidation kabusu ve çözüm yöntemleri.",
                "Graceful Degradation: Redis çökerse sistem nasıl ayakta kalır?"
            ],
            "udemy_slides_en": [
                "Why the fastest database call is the one you never execute.",
                "The Cache-Aside anatomy: Hits, Misses, and TTL eviction policies.",
                "Tackling cache invalidation hazards.",
                "Graceful degradation: Ensuring services survive Redis downtime."
            ],
            "udemy_demo_tr": "Docker üzerinde yerel bir Redis ayağa kaldırın. Postman ile API'ye istek atın: İlk istekte sürenin 120 ms olduğunu (DB okuma), ikinci istekte 2 ms'ye düştüğünü (Redis Hit) canlı gösterin. Ardından veriyi güncelleyip cache'in nasıl temizlendiğini kanıtlayın.",
            "udemy_demo_en": "Run a local Redis container. Execute an API endpoint via curl: observe the initial 120ms database fetch, followed by a 2ms Redis cache hit. Mutate the entity and demonstrate cache invalidation.",
            "action_task_tr": "Docker ile yerel makinenizde bir Redis başlatın (`docker run -p 6379:6379 redis:alpine`) ve projenizdeki en sık okunan endpoint'e Cache-Aside deseni ekleyin.",
            "action_task_en": "Deploy a local Redis container and wrap your most frequently queried read endpoint in a Cache-Aside function.",
            "quiz_tr": [
                {
                    "question": "Önbelleğe alınan bir veriye 'TTL' (Time to Live) süresi tanımlamanın temel amacı nedir?",
                    "options": [
                        "A) Veriyi şifrelemek",
                        "B) Belirtilen süre dolduğunda verinin bellekten otomatik silinmesini sağlayarak hem RAM'in dolmasını engellemek hem de bayat veri riskini sınırlamak",
                        "C) Bilgisayarı kapatmak",
                        "D) Sadece Python'da hata vermesini sağlamak"
                    ],
                    "answer": "B",
                    "explanation": "TTL, anahtarın yaşam süresini belirler; süresi biten anahtar silinir ve RAM'in taşması önlenir."
                },
                {
                    "question": "Cache-Aside deseninde 'Cache Miss' ne anlama gelir?",
                    "options": [
                        "A) Sistemin tamamen çöktüğünü",
                        "B) Aranan verinin önbellekte (Redis) bulunamadığını; bu yüzden asıl veritabanından okunup önbelleğe yazılması gerektiğini",
                        "C) CSS dosyasının eksik olduğunu",
                        "D) Kullanıcının şifresini unuttuğunu"
                    ],
                    "answer": "B",
                    "explanation": "Cache Miss, aranan bilginin Redis'te olmaması durumudur; uygulama veritabanından veriyi çeker, Redis'e kaydeder ve kullanıcıya döner."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the primary operational purpose of defining a TTL (Time To Live) on cached keys?",
                    "options": [
                        "A) Cryptographically signing the payload",
                        "B) Automatically evicting expired keys to prevent memory saturation and bound stale data exposure",
                        "C) Triggering server shutdowns",
                        "D) Forcing Python syntax checks"
                    ],
                    "answer": "B",
                    "explanation": "TTL ensures keys expire deterministically, keeping RAM usage bounded and preventing permanently outdated records."
                },
                {
                    "question": "In the Cache-Aside pattern, what constitutes a 'Cache Miss'?",
                    "options": [
                        "A) Fatal database cluster crash",
                        "B) The requested key was absent from cache, requiring an authoritative database read and subsequent cache population",
                        "C) Missing stylesheet assets",
                        "D) User credential expiration"
                    ],
                    "answer": "B",
                    "explanation": "A cache miss occurs when a key is not found in memory, necessitating a fallback read from primary storage."
                }
            ]
        },

        # Chapter 30
        {
            "id": 30,
            "section_id": 5,
            "slug_tr": "ch30_kimlik_dogrulama_ve_yetkilendirme_jwt_rbac",
            "slug_en": "ch30_auth_identity_jwt_oauth2_rbac",
            "title_tr": "Kimlik Doğrulama ve Yetkilendirme: JWT, OAuth2 ve Session Yönetimi",
            "title_en": "Authentication & Authorization: JWT, OAuth2 & Role-Based Access Control",
            "subtitle_tr": "Authentication (Sen Kimsin?) vs. Authorization (Neye İznin Var?) Ayrımı",
            "subtitle_en": "Securing Web APIs: The Clear Divide Between Authentication and Authorization",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "JWT (JSON Web Token) neden 'localStorage' içinde saklanmamalıdır ve bir access token çalındığında sistem nasıl korunur?",
            "podcast_hook_en": "Why is persisting JWTs in `localStorage` an open invitation to XSS attacks, and how do HttpOnly cookies combined with Refresh Tokens safeguard APIs?",
            "takeaways_tr": [
                "Authentication (Kimlik Doğrulama) 'Sen kimsin?' sorusudur; Authorization (Yetkilendirme) ise 'Neye erişebilirsin?' sorusudur.",
                "JWT'ler şifrelenmiş değil, imzalanmış (signed) jetonlardır; içeriği herkes okuyabilir, bu yüzden içine asla şifre veya kredi kartı yazılmaz.",
                "JWT'leri XSS saldırılarından korumak için `localStorage` yerine daima `HttpOnly, Secure` çerezlerde (Cookies) saklayın."
            ],
            "takeaways_en": [
                "Authentication answers 'Who are you?'; Authorization answers 'What permissions do you hold?'.",
                "JWTs are cryptographically signed, NOT encrypted; anyone can decode the payload, so never store secrets inside them.",
                "Guard tokens against Cross-Site Scripting (XSS) by storing them in `HttpOnly, Secure, SameSite=Strict` cookies rather than `localStorage`."
            ],
            "story_tr": """Bir havalimanına girdiğinizi düşünün.

1. **Authentication (Kimlik Doğrulama):** Pasaport kontrolüne gidersiniz. Polis memuru pasaportunuza ve yüzünüze bakar: *"Evet, sen Ali Turgut'sun."* Bu kimlik doğrulamadır.
2. **Authorization (Yetkilendirme):** Uçağa binerken biletinizi gösterirsiniz. Biletiniz 'Ekonomi' ise Business Class bölümüne veya pilot kabinine giremezsiniz! Giriş kartınız (RBAC) sadece koltuk numaranıza izin verir.

Pasaportunuz var diye uçağı uçuramazsınız!

Yazılımda da bir kullanıcının sisteme giriş yapmış olması (AuthN), her veriyi silebileceği (AuthZ) anlamına gelmez. Rolleri ve izinleri (RBAC) sıkı bir kapı nöbetçisi gibi denetlemelisiniz.""",
            "story_en": """Picture navigating an international airport terminal.

1. **Authentication:** You approach border control. The officer checks your passport and facial biometrics: *"You are indeed Jordan."* That is identity verification.
2. **Authorization:** You walk down the jet bridge. Your boarding pass designates Seat 18B. You cannot walk into First Class or unlock the cockpit door. Your role-based pass grants entry strictly to Seat 18B.

Holding a verified passport does not authorize you to fly the plane.

In software engineering, successfully logging in (AuthN) does not confer permission to delete other tenants' invoices (AuthZ). Role-Based Access Control (RBAC) enforces these operational boundaries.""",
            "mental_tr": """Güvenli Auth Mimarisi (HttpOnly Cookie + Refresh Token):

```
[İstemci (Tarayıcı)] ──(POST /login)──> [Auth Sunucusu]
                                               │
                                 ┌─────────────┴─────────────┐
                                 ▼                           ▼
                     [Access Token (15 dk)]      [Refresh Token (7 gün)]
                     (Kısa ömürlü JWT)           (Veritabanında tutulur)
                                 │                           │
                                 └─────────────┬─────────────┘
                                               ▼
                       Set-Cookie: HttpOnly, Secure, SameSite=Strict
```""",
            "mental_en": """Hardened Modern Auth Topology:

```
[Browser Client] ──(POST /api/login)──> [Authentication Server]
                                                │
                                  ┌─────────────┴─────────────┐
                                  ▼                           ▼
                      [Access Token (15 min)]     [Refresh Token (7 days)]
                      (Stateless Signed JWT)      (Opaque, hashed in DB)
                                  │                           │
                                  └─────────────┬─────────────┘
                                                ▼
                         Set-Cookie: HttpOnly, Secure, SameSite=Strict
```""",
            "prompt_tr": """# ROL: Web Güvenliği ve Kimlik Yönetimi Uzmanı
Express ve TypeScript kullanan bir API'ye Role-Based Access Control (RBAC) middleware'i ekleyeceğiz.

## GÖREV:
1. Bir JWT doğrulayan ve kullanıcıyı `req.user` içine koyan `authenticate` middleware'i yaz.
2. Sadece belirli rollere ('ADMIN', 'SUPERVISOR') izin veren `authorize(...roles)` middleware'i tasarla.
3. Yetkisiz girişlerde (401 vs 403) doğru HTTP durum kodlarını fırlat.""",
            "prompt_en": """# ROLE: Application Security & IAM Specialist
We are securing an Express/TypeScript API with Role-Based Access Control (RBAC).

## TASK:
1. Implement an `authenticate` middleware verifying JWT signatures and attaching claims to `req.user`.
2. Implement a higher-order `authorize(...allowedRoles)` middleware enforcing access permissions.
3. Emit semantically correct status codes: 401 Unauthorized vs. 403 Forbidden.""",
            "code_lang": "typescript",
            "code_naive": """// Güvensiz Yaklaşım: Rolü frontend'den gelen parametreye göre kontrol etmek!
app.delete("/users/:id", async (req, res) => {
  // Saldırgan URL'e ?role=ADMIN yazarak herkesi silebilir!
  if (req.query.role === "ADMIN") {
    await db.user.delete({ where: { id: req.params.id } });
    return res.send("Silindi");
  }
  res.status(403).send("Yetkisiz");
});""",
            "code_robust": """import { Request, Response, NextFunction } from "express";
import jwt from "jsonwebtoken";

export interface UserTokenPayload {
  userId: string;
  email: string;
  role: "USER" | "ADMIN" | "SUPERVISOR";
}

// 1. Kimlik Doğrulama (Authentication - 401)
export function authenticate(req: Request, res: Response, next: NextFunction) {
  const token = req.cookies?.accessToken || req.headers.authorization?.split(" ")[1];

  if (!token) {
    return res.status(401).json({ error: "Oturum açılmadı (Token eksik)." });
  }

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET!) as UserTokenPayload;
    (req as any).user = decoded;
    next();
  } catch (err) {
    return res.status(401).json({ error: "Geçersiz veya süresi dolmuş token." });
  }
}

// 2. Yetkilendirme (Authorization / RBAC - 403)
export function authorize(...allowedRoles: Array<UserTokenPayload["role"]>) {
  return (req: Request, res: Response, next: NextFunction) => {
    const user = (req as any).user as UserTokenPayload;

    if (!user || !allowedRoles.includes(user.role)) {
      return res.status(403).json({ error: "Yetersiz yetki: Bu kaynağa erişim izniniz yok." });
    }

    next();
  };
}

// 3. Güvenli Rota Kullanımı:
// app.delete("/users/:id", authenticate, authorize("ADMIN"), deleteUserHandler);""",
            "code_notes_tr": "`401 Unauthorized` (Kimliğinizi doğrulamadınız, giriş yapın) ile `403 Forbidden` (Kimliğinizi biliyorum ama buraya girmeye yetkiniz yok) ayrımı tam olarak uygulanmıştır.",
            "code_notes_en": "Respects the critical distinction: `401 Unauthorized` means authentication failed; `403 Forbidden` means identity is verified, but permissions are insufficient.",
            "pitfalls_tr": [
                {"trap": "JWT içine kullanıcının şifresini veya kredi kartı numarasını koymak.", "solution": "JWT şifrelenmiş değildir (Base64'tür); içine sadece zararsız kullanıcı ID ve rolü koyun."},
                {"trap": "JWT'yi frontend'de `localStorage` içine kaydedip XSS saldırılarına açık kapı bırakmak.", "solution": "Token'ları daima `HttpOnly` çerezlerde saklayarak JavaScript ile okunmasını engelleyin."},
                {"trap": "401 ve 403 durum kodlarını birbirine karıştırmak.", "solution": "Giriş yapılmadıysa 401, giriş yapılmış ama rol yetersizse 403 dönün."}
            ],
            "pitfalls_en": [
                {"trap": "Embedding passwords or sensitive PII inside JWT payloads.", "solution": "JWT payloads are easily decoded Base64 strings; store only public IDs and role claims."},
                {"trap": "Storing authorization tokens in browser `localStorage`, exposing them to XSS exfiltration.", "solution": "Persist tokens in `HttpOnly` cookies inaccessible to JavaScript injection attacks."},
                {"trap": "Conflating 401 Unauthorized with 403 Forbidden.", "solution": "Emit 401 when authentication is absent or expired; emit 403 when authenticated identity lacks role permissions."}
            ],
            "udemy_title_tr": "Ders 30: Güvenli Kimlik Yönetimi - JWT ve RBAC Mimarisi",
            "udemy_title_en": "Lecture 30: Authentication & Authorization - JWTs & RBAC in Action",
            "udemy_slides_tr": [
                "Authentication (Kimlik) vs Authorization (Yetki) farkı.",
                "JWT'nin anatomisi: Header, Payload, Signature.",
                "Neden localStorage değil HttpOnly Cookie?",
                "Bölüm 5 Özeti: Veritabanı, Modelleme ve Backend Ustalığı."
            ],
            "udemy_slides_en": [
                "Authentication vs. Authorization: Understanding the boundary.",
                "Anatomy of a JWT: Header, Claims Payload, Cryptographic Signature.",
                "Mitigating XSS: Why `HttpOnly` cookies trump `localStorage`.",
                "Module 5 Recap: Databases, Relational Modeling & Backend Mastery."
            ],
            "udemy_demo_tr": "jwt.io sitesini açın. Basit bir JWT oluşturup payload'ın şifresiz şekilde herkes tarafından okunabildiğini gösterin. Ardından Express'te `authorize('ADMIN')` middleware'i kurup normal kullanıcıyla istek atınca 403 Forbidden aldığını gösterin.",
            "udemy_demo_en": "Navigate to jwt.io. Paste a sample token to illustrate that payloads are plain Base64 JSON. Test an Express route with an unprivileged token to demonstrate a 403 Forbidden response.",
            "action_task_tr": "Projenizdeki bir rotayı inceleyin. Eğer kullanıcı rolü frontend'den gelen bir parametreye göre kontrol ediliyorsa, bunu JWT içindeki güvenli claims payload'ına göre kontrol edecek şekilde refactor edin.",
            "action_task_en": "Refactor a route in your project to read user roles strictly from verified JWT claims rather than request bodies or query parameters.",
            "quiz_tr": [
                {
                    "question": "Bir web uygulamasında `401 Unauthorized` ile `403 Forbidden` arasındaki fark nedir?",
                    "options": [
                        "A) Hiçbir farkı yoktur",
                        "B) 401 kullanıcının henüz oturum açmadığını (kimlik doğrulanmadığını); 403 ise kullanıcının oturum açtığını fakat o kaynağa erişim yetkisinin olmadığını belirtir",
                        "C) 401 sadece telefonlarda çıkar",
                        "D) 403 sunucunun bozulduğunu belirtir"
                    ],
                    "answer": "B",
                    "explanation": "401 kimlik eksikliğini (AuthN), 403 ise yetki yetersizliğini (AuthZ) ifade eder."
                },
                {
                    "question": "JWT token'larının `localStorage` yerine `HttpOnly` çerezlerde saklanmasının birincil güvenlik sebebi nedir?",
                    "options": [
                        "A) HttpOnly çerezlerin CSS'i daha hızlı render etmesi",
                        "B) Kötü niyetli JavaScript kodlarının (XSS saldırıları) çereze doğrudan erişip token'ı çalamamasını sağlamak",
                        "C) Sadece Chrome tarayıcısında çalışması",
                        "D) Token'ın boyutunu küçültmesi"
                    ],
                    "answer": "B",
                    "explanation": "`HttpOnly` bayrağı, tarayıcıda çalışan JavaScript kodunun (XSS) çerezi okumasını tarayıcı seviyesinde engelleyerek token hırsızlığını önler."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the precise RFC HTTP distinction between 401 Unauthorized and 403 Forbidden?",
                    "options": [
                        "A) They are interchangeable status codes",
                        "B) 401 implies missing or invalid credentials (unauthenticated); 403 implies authenticated identity with insufficient privileges (unauthorized)",
                        "C) 401 is exclusive to mobile clients",
                        "D) 403 indicates database infrastructure failures"
                    ],
                    "answer": "B",
                    "explanation": "401 indicates unauthenticated requests; 403 indicates that credentials were recognized but lack authorization for the target resource."
                },
                {
                    "question": "What is the primary security justification for storing authentication JWTs inside `HttpOnly` cookies rather than `localStorage`?",
                    "options": [
                        "A) Accelerating CSS rendering pipelines",
                        "B) Preventing cross-site scripting (XSS) malicious scripts from accessing and exfiltrating the token payload",
                        "C) Compatibility restricted to Google Chrome",
                        "D) Compressing token string lengths"
                    ],
                    "answer": "B",
                    "explanation": "The browser blocks JavaScript from accessing `HttpOnly` cookies, preventing compromised client scripts from exfiltrating credentials."
                }
            ]
        }
    ]
