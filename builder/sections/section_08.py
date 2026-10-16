"""
Section 8: Güvenlik, OWASP & AI Kod Hijyeni (Chapters 43 to 48)
"""

def get_section_chapters():
    return [
        # Chapter 43
        {
            "id": 43,
            "section_id": 8,
            "slug_tr": "ch43_ai_kodunun_gizli_guvenlik_aciklari",
            "slug_en": "ch43_hidden_vulnerabilities_in_ai_generated_code",
            "title_tr": "AI'nın Ürettiği Kod Güvenli mi? Gizli Güvenlik Açıkları",
            "title_en": "Is AI Code Secure? Unveiling Common LLM Vulnerabilities",
            "subtitle_tr": "Yapay Zekanın Koda Gizlice Enjekte Ettiği Güvenlik Açıklarını Avlamak",
            "subtitle_en": "Auditing Blind Spots: Detecting Silent Cryptographic, Injection & Auth Flaws",
            "level_tr": "İleri Seviye",
            "level_en": "Advanced",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Stanford Üniversitesi araştırmasına göre yapay zeka kullanan yazılımcıların daha çok güvenlik açığı ürettiği ve kendi kodlarının 'güvenli' olduğuna daha çok inandığı doğru mu?",
            "podcast_hook_en": "Does Stanford research truly prove developers using AI code assistants write significantly more vulnerable software while feeling far more confident in their security?",
            "takeaways_tr": [
                "Yapay zeka modelleri 'çalışan' kod üretmeye odaklıdır; 'güvenli' kod üretmek sizin şartnamelerinize bağlıdır.",
                "En yaygın AI güvenlik kusurları: Hardcoded secret'lar, zayıf şifreleme algoritmaları ve girdi doğrulaması yapılmamış parametrelerdir.",
                "Güvenlik bir eklenti değil; AI'a verilen promptların ve CI pipeline'ındaki SAST (Statik Güvenlik Analizi) araçlarının ayrılmaz parçası olmalıdır."
            ],
            "takeaways_en": [
                "LLMs prioritize syntax that completes tasks functionally; security guarantees depend on your architectural constraints.",
                "Common LLM security blind spots: hardcoded credentials, deprecated crypto algorithms (MD5/DES), and missing input sanitization.",
                "Security is not a post-launch patch; it must be mandated in system prompts and gated via automated SAST tooling in CI."
            ],
            "story_tr": """Bir çilingir çağırdığınızı ve kapınıza kilit taktırmak istediğinizi düşünün.

Çilingir kapıya harika görünen, parlak pirinçten bir kilit takıyor. Anahtarı çeviriyorsunuz: *"Tık!"* diye dönüyor, kapı kapanıyor. Çilingir gülümsüyor: *"Harika çalışıyor!"*

Fakat çilingir gittikten sonra fark ediyorsunuz ki kilit dilini duvardaki yuvaya bağlamamış! Dışarıdan parmağınızla hafifçe dokunduğunuzda kapı ardına kadar açılıyor!

Yapay zekanın ürettiği kontrolsüz kod tam olarak o parlak pirinç kilittir:
Kod hatasız derlenir, ekranda çalışır görünür. Ancak arkasında SQL Injection, yetkilendirme açığı (IDOR) veya zayıf şifreleme gibi devasa delikler bırakabilir.

Bir mühendis olarak göreviniz, anahtarın dönmesine değil, kilidin hırsızı durdurup durdurmadığına bakmaktır.""",
            "story_en": """Imagine hiring a locksmith to secure your front door.

The technician installs an ornate polished brass lock. You turn the key: the cylinder clicks, and the door shuts. The locksmith beams: *"Flawless execution!"*

After they leave, you lean lightly against the door. It swings wide open! The locksmith forgot to chisel the deadbolt strike plate into the wall stud.

Unverified AI code is that exact decorative brass lock:
It compiles without warnings and passes happy-path UI tests. But behind the facade lurks broken access controls (IDOR), SQL injection vectors, or deprecated hash functions.

Your professional responsibility is verifying the deadbolt actually resists intrusion.""",
            "mental_tr": """AI Kod Denetimi Kontrol Listesi (Security Checklist):

```
┌────────────────────────────────────────────────────────┐
│             AI KODU GÜVENLİK SÜZGECİ                   │
└──────────────────────────┬─────────────────────────────┘
                           │
  1. GİRDİ DOĞRULAMA: Dışarıdan gelen veri sanitize edildi mi?
  2. YETKİLENDİRME (AuthZ): Kullanıcı sadece kendi verisine mi erişiyor?
  3. KRİPTOĞRAFİ: MD5, SHA1, DES gibi kırılmış algoritmalar var mı?
  4. SIZINTI KONTROLÜ: API anahtarı veya şifre koda gömülmüş mü?
  5. HATA YÖNETİMİ: Stack trace veya DB şeması istemciye sızıyor mu?
```""",
            "mental_en": """The AI Code Forensic Security Gauntlet:

```
┌────────────────────────────────────────────────────────┐
│             AI CODE FORENSIC CHECKLIST                 │
└──────────────────────────┬─────────────────────────────┘
                           │
  1. INPUT SANITIZATION: Are ingress payloads bounded and type-coerced?
  2. OBJECT AUTHORIZATION (IDOR): Does the query verify tenant ownership?
  3. CRYPTOGRAPHIC INTEGRITY: Are MD5, SHA1, or legacy ciphers banned?
  4. SECRETS HYGIENE: Are private tokens or database credentials committed?
  5. ERROR DISCLOSURE: Are raw stack traces masked from external clients?
```""",
            "prompt_tr": """# ROL: Kıdemli Siber Güvenlik ve Kod Güvenliği Müfettişi
Aşağıdaki Python fonksiyonu bir yapay zeka tarafından üretildi ve production'a gönderilmek üzere.

## KOD:
```python
import hashlib
import sqlite3

def register_user(username, password):
    # AI önerisi:
    hashed_pwd = hashlib.md5(password.encode()).hexdigest()
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users VALUES ('{username}', '{hashed_pwd}')")
    conn.commit()
```

## GÖREV:
1. Bu koddaki 3 ölümcül güvenlik açığını açıkla (SQLi, zayıf hash, salt eksikliği).
2. Bu açıkları istismar eden (exploit) senaryoları göster.
3. Kodu Argon2id / bcrypt ve parametrik SQL kullanarak kurşun geçirmez şekilde yeniden yaz.""",
            "prompt_en": """# ROLE: Senior Application Security Engineer & Penetration Tester
An AI assistant authored this authentication routine:

## SNIPPET:
```python
import hashlib
import sqlite3

def register_user(username, password):
    hashed_pwd = hashlib.md5(password.encode()).hexdigest()
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users VALUES ('{username}', '{hashed_pwd}')")
    conn.commit()
```

## TASK:
1. Pinpoint the 3 critical vulnerabilities (SQL Injection, broken MD5 hashing, missing unique salt).
2. Demonstrate how an attacker exploits the inline SQL string formatting.
3. Provide a hardened refactor utilizing parameterized queries and modern `bcrypt` / `Argon2id` hashing.""",
            "code_lang": "python",
            "code_naive": """# Kötü / AI Üretimi Güvensiz Kod: MD5 kırılmıştır ve SQL Injection açığı vardır!
import hashlib, sqlite3

def register_user_naive(user, pwd):
    # MD5 1 saniyede kırılır; Rainbow tablosu saldırısına açıktır!
    h = hashlib.md5(pwd.encode()).hexdigest()
    # String formatlama ile SQL Injection: user = "admin', '123'); DROP TABLE users; --"
    sqlite3.connect('app.db').cursor().execute(f"INSERT INTO users VALUES ('{user}', '{h}')")""",
            "code_robust": """# Güvenli ve Kurumsal Standart: bcrypt + Parametrik SQL Sorgusu
import bcrypt
import sqlite3

def register_user_secure(username: str, password_plain: str) -> bool:
    # 1. Girdi Uzunluk Sınırı (DoS koruması)
    if len(password_plain) < 12 or len(password_plain) > 128:
        raise ValueError("Şifre 12 ile 128 karakter arasında olmalıdır.")

    # 2. Modern Hashleme: Rastgele Salt + Yavaşlatılmış İşlem Maliyeti (Cost factor 12)
    salt = bcrypt.gensalt(rounds=12)
    password_hash = bcrypt.hashpw(password_plain.encode("utf-8"), salt).decode("utf-8")

    # 3. Parametrik SQL: Değişkenler asla doğrudan SQL içine gömülmez!
    with sqlite3.connect("app.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username.strip().lower(), password_hash)
        )
        conn.commit()

    return True""",
            "code_notes_tr": "MD5 yerine yavaş ve rastgele salt üreten `bcrypt` kullanılarak Rainbow Table saldırıları imkansız kılınmış; f-string yerine `(?, ?)` parametrik sorgusu kullanılarak SQL Injection tamamen bertaraf edilmiştir.",
            "code_notes_en": "Substituting broken MD5 with salted `bcrypt` thwarts pre-computed rainbow table attacks. Replacing string interpolation with parameterized `(?, ?)` placeholders eradicates SQL injection completely.",
            "pitfalls_tr": [
                {"trap": "Şifre hashlemek için MD5 veya SHA-256 gibi hızlı algoritmaları kullanmak.", "solution": "Şifreler için daima yavaş ve bellek zorlayan algoritmalar (bcrypt, Argon2id, PBKDF2) kullanın."},
                {"trap": "SQL sorgularına değişkenleri `f'{var}'` veya `+ var` şeklinde yapıştırmak.", "solution": "İstisnasız her SQL sorgusunda parametrik sorgu (Parameterized Queries / Prepared Statements) kullanın."},
                {"trap": "AI'a 'bunu güvenli yap' demeden doğrudan kod yazmasını istemek.", "solution": "Promptlarınızda 'OWASP standartlarına uy, parametrik sorgu kullan' şartını açıkça belirtin."}
            ],
            "pitfalls_en": [
                {"trap": "Hashing user passwords using fast digest algorithms like MD5 or plain SHA-256.", "solution": "Always employ computationally expensive, memory-hard hashing algorithms (bcrypt, Argon2id)."},
                {"trap": "Concatenating user inputs into SQL strings via templates or string additions.", "solution": "Enforce parameterized queries or prepared statements across all database interactions."},
                {"trap": "Assuming the AI model instinctively applies defensive security practices without prompts.", "solution": "Explicitly mandate OWASP constraints and secure defaults in system rules."}
            ],
            "udemy_title_tr": "Ders 43: AI ve Kod Güvenliği - Gizli Açıkları Yakalamak",
            "udemy_title_en": "Lecture 43: Auditing AI Code - Catching Silent Security Vulnerabilities",
            "udemy_slides_tr": [
                "Stanford Araştırması: AI kullanan geliştiriciler neden daha çok açık üretiyor?",
                "En tehlikeli 3 kör nokta: Parametresiz SQL, MD5 şifreleme, IDOR açıkları.",
                "bcrypt vs Argon2id: Şifre güvenliğinin matematiksel temeli.",
                "Canlı Hack Demosu: AI'ın yazdığı giriş fonksiyonuna SQL Injection saldırısı."
            ],
            "udemy_slides_en": [
                "The Stanford finding: Why AI-assisted engineers introduce more security flaws.",
                "Top 3 LLM blind spots: Unparameterized SQL, legacy hashing, and IDOR.",
                "bcrypt vs. Argon2id: The cryptographic science of password salting.",
                "Live exploit: Executing an injection attack against unverified AI code."
            ],
            "udemy_demo_tr": "String birleştirme ile yazılmış bir giriş fonksiyonu açın. Kullanıcı adı yerine `' OR '1'='1` yazarak şifre bilmeden sisteme giriş yapıldığını (SQL Injection) gösterin. Ardından parametrik sorguya dönüştürüp saldırıyı engelleyin.",
            "udemy_demo_en": "Run a script featuring raw SQL string interpolation. Pass `' OR '1'='1` to demonstrate an authentication bypass. Refactor to a parameterized statement and prove the exploit fails.",
            "action_task_tr": "Projenizdeki tüm SQL sorgularını tarayın. Herhangi bir yerde `+` veya f-string ile sorguya değişken eklenmiş mi kontrol edin ve parametrik hale getirin.",
            "action_task_en": "Grep your project for raw SQL concatenations (`f'SELECT` or `\" + var`). Refactor any discoveries into parameterized queries.",
            "quiz_tr": [
                {
                    "question": "Kullanıcı şifrelerini veritabanında saklarken SHA-256 veya MD5 yerine neden `bcrypt` veya `Argon2id` tercih edilmelidir?",
                    "options": [
                        "A) bcrypt'in daha az yer kaplaması",
                        "B) SHA-256 ve MD5'in çok hızlı olması sebebiyle saniyede milyarlarca parola deneyen kaba kuvvet (Brute-Force) saldırılarına dayanamaması; bcrypt'in ise bilinçli olarak yavaşlatılmış ve 'tuzlanmış' (salted) olması",
                        "C) Sadece Python'da çalışması",
                        "D) Bilgisayarı koruması"
                    ],
                    "answer": "B",
                    "explanation": "Şifre hash algoritmaları saldırganların deneme hızını düşürmek için bilinçli olarak yavaş çalışacak şekilde tasarlanır; hızlı algoritmalar şifre için güvensizdir."
                },
                {
                    "question": "SQL Injection saldırılarını tamamen engellemenin endüstri standardı kesin çözümü nedir?",
                    "options": [
                        "A) Kullanıcılardan tırnak işareti yazmamalarını rica etmek",
                        "B) Parametrik Sorgular (Parameterized Queries / Prepared Statements) kullanmak",
                        "C) Veritabanı şifresini değiştirmek",
                        "D) Sayfayı her gün yeniden başlatmak"
                    ],
                    "answer": "B",
                    "explanation": "Parametrik sorgularda veritabanı motoru kullanıcı girdisini asla çalıştırılabilir SQL kodu olarak yorumlamaz; sadece saf veri (literal string) olarak işler."
                }
            ],
            "quiz_en": [
                {
                    "question": "Why are algorithms like `bcrypt` and `Argon2id` mandated for password hashing over SHA-256 or MD5?",
                    "options": [
                        "A) bcrypt uses fewer disk bytes",
                        "B) SHA-256 and MD5 execute too quickly, permitting billions of brute-force attempts per second; bcrypt enforces tunable work factors and salts",
                        "C) Exclusive compatibility with Python",
                        "D) Motherboard protection"
                    ],
                    "answer": "B",
                    "explanation": "Password storage mandates computationally expensive, salted hashing algorithms to neutralize GPU-accelerated brute-force attacks."
                },
                {
                    "question": "What is the industry-standard defense that eradicates SQL Injection across all databases?",
                    "options": [
                        "A) Prompting users to avoid quotation marks",
                        "B) Using Parameterized Queries / Prepared Statements",
                        "C) Rotating the database password daily",
                        "D) Restarting server processes"
                    ],
                    "answer": "B",
                    "explanation": "Parameterized queries separate SQL instructions from literal data parameters, preventing arbitrary command execution."
                }
            ]
        },

        # Chapter 44
        {
            "id": 44,
            "section_id": 8,
            "slug_tr": "ch44_owasp_top_10_pratik_kilavuz",
            "slug_en": "ch44_owasp_top_10_in_practice_exploits_and_fixes",
            "title_tr": "OWASP Top 10 Pratik Kılavuzu: SQL Injection, XSS, CSRF",
            "title_en": "OWASP Top 10 in Practice: Exploits, Defenses & Hardened Code",
            "subtitle_tr": "Web Güvenliğinin En Tehlikeli 10 Açığını Kod Seviyesinde Kapatmak",
            "subtitle_en": "Immunizing Full-Stack Web Applications Against the Top 10 Security Exploits",
            "level_tr": "İleri Seviye",
            "level_en": "Advanced",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Bir hacker sadece bir yorum kutusuna `<script>` yazarak şirketinizin binlerce kullanıcısının oturumunu nasıl çalabilir? XSS ve CSRF'i nasıl tarihe gömeriz?",
            "podcast_hook_en": "How can an attacker hijack thousands of active corporate sessions simply by typing `<script>` into a blog comment box? How do we neutralize XSS and CSRF?",
            "takeaways_tr": [
                "OWASP Top 10, dünyada web uygulamalarına yönelik en yaygın ve yıkıcı 10 güvenlik riskini listeler.",
                "XSS (Cross-Site Scripting), saldırganın web sayfasına zararlı JavaScript enjekte etmesidir; `dangerouslySetInnerHTML` kullanımından kaçının.",
                "IDOR (Insecure Direct Object Reference), URL'deki ID'yi değiştirerek başkasının faturasına erişmektir; yetkilendirme kontrolü şarttır."
            ],
            "takeaways_en": [
                "The OWASP Top 10 catalogues the most prevalent, critical web application security risks in production software.",
                "Cross-Site Scripting (XSS) occurs when applications render unescaped user inputs directly into the DOM; ban `dangerouslySetInnerHTML`.",
                "Insecure Direct Object References (IDOR) happen when APIs trust client IDs without verifying tenant ownership (`WHERE id = ? AND userId = ?`)."
            ],
            "story_tr": """Bir apartmanda oturduğunuzu düşünün.

1. **XSS:** Kapıdaki zil kutusuna bir saldırgan görünmez zehirli bir iğne yerleştiriyor. Komşunuz zile bastığında zehirleniyor ve anahtarlarını düşürüyor (Kötü niyetli JavaScript'in oturum çerezlerini çalması).
2. **CSRF:** Posta kutunuza sahte bir mektup geliyor: *"Bu zarfı açarsan 1000 TL kazanacaksın!"* Zarfı açtığınız anda arka kapıdaki kurye sizin adınıza bankaya talimat veriyor!
3. **IDOR:** Faturanıza bakmak için web sitesine giriyorsunuz. URL şöyle: `site.com/fatura/101`. Yukarıdaki 101 sayısını silip 102 yazıyorsunuz ve komşunuzun tüm kredi kartı ve harcama dökümü önünüze açılıyor!

OWASP Top 10 işte bu apartmandaki güvenlik açıklarının listesidir. Güvenli bir sistem, kapı numarasını değiştiren birine *"Dur bakalım, bu ev senin mi?"* diye soran sistemdir.""",
            "story_en": """Imagine living in a residential apartment complex.

1. **XSS:** An adversary coats the doorbell with contact neurotoxin. When your neighbor rings the bell, they collapse and drop their keys (Malicious JavaScript executes in the browser, stealing session cookies).
2. **CSRF:** A fraudulent courier delivers a sweepstakes flyer. Reading the card triggers an automated mechanism that transfers rent funds out of your mailbox!
3. **IDOR:** You inspect your utility bill online at `/invoices/101`. You change the URL parameter to `/invoices/102`, and suddenly your neighbor's private bank details and home address load on your screen!

The OWASP Top 10 is the blueprint of these exact vulnerabilities. Hardened engineering asks: *"Does this authenticated user actually own invoice #102?"* before returning a single byte of data.""",
            "mental_tr": """En Kritik 3 OWASP Açığının Çözüm Haritası:

```
1. IDOR (Insecure Direct Object Reference):
   ❌ YANLIŞ: SELECT * FROM invoices WHERE id = req.params.id;
   ✅ DOĞRU: SELECT * FROM invoices WHERE id = req.params.id AND user_id = req.user.id;

2. XSS (Cross-Site Scripting):
   ❌ YANLIŞ: <div dangerouslySetInnerHTML={{ __html: userComment }} />
   ✅ DOĞRU: <div>{userComment}</div> (React varsayılan olarak HTML'i sanitize eder)

3. CSRF (Cross-Site Request Forgery):
   ❌ YANLIŞ: Basit çerezler (SameSite ayarı yok)
   ✅ DOĞRU: SameSite=Strict ve CSRF Token doğrulaması
```""",
            "mental_en": """The Triage Matrix for Top OWASP Flaws:

```
1. IDOR (Broken Object-Level Authorization):
   ❌ VULNERABLE: SELECT * FROM documents WHERE id = :docId;
   ✅ HARDENED: SELECT * FROM documents WHERE id = :docId AND tenant_id = :currentTenantId;

2. XSS (Cross-Site Scripting):
   ❌ VULNERABLE: <div dangerouslySetInnerHTML={{ __html: userPayload }} />
   ✅ HARDENED: <div>{userPayload}</div> (Framework-native HTML entity escaping)

3. CSRF (Cross-Site Request Forgery):
   ❌ VULNERABLE: Default cookies without cross-origin constraints
   ✅ HARDENED: `SameSite=Strict` cookies paired with Anti-CSRF verification tokens
```""",
            "prompt_tr": """# ROL: Web Uygulama Güvenliği Uzmanı (AppSec)
Aşağıdaki Express API endpoint'i tipik bir IDOR (Yetkisiz Nesne Erişimi) açığı içermektedir.

## AÇIKLI KOD:
```typescript
app.get("/api/invoices/:id", authenticate, async (req, res) => {
  const invoice = await db.invoice.findUnique({
    where: { id: req.params.id }
  });
  res.json(invoice);
});
```

## GÖREV:
1. Bu IDOR açığının bir saldırgan tarafından nasıl istismar edileceğini açıkla.
2. Kodda hem sahiplik kontrolünü (Ownership Check) hem de 404/403 durumlarını doğru yöneten güvenli sürümü yaz.
3. Bu açığı otomatik yakalayacak bir güvenlik test senaryosu (Jest/Supertest) tasarla.""",
            "prompt_en": """# ROLE: Application Security Lead & Penetration Specialist
Audit this endpoint suffering from an Insecure Direct Object Reference (IDOR):

## VULNERABLE ROUTE:
```typescript
app.get("/api/invoices/:id", authenticate, async (req, res) => {
  const invoice = await db.invoice.findUnique({
    where: { id: req.params.id }
  });
  res.json(invoice);
});
```

## TASK:
1. Explain how an authenticated malicious user exploits this route.
2. Refactor to enforce strict tenant isolation, preventing enumeration attacks.
3. Author a Supertest assertion proving User A cannot read User B's invoice.""",
            "code_lang": "typescript",
            "code_naive": """// IDOR Açığı: Kullanıcı giriş yapmış ama faturanın KENDİSİNE ait olduğu kontrol edilmiyor!
app.get("/api/orders/:id", authenticate, async (req, res) => {
  // Saldırgan :id yerine rastgele sayılar deneyerek herkesin siparişini çalar!
  const order = await db.order.findUnique({ where: { id: req.params.id } });
  res.json(order);
});""",
            "code_robust": """// IDOR Güvenliği: Çift Koşullu Sorgu ve İzolasyon
app.get("/api/orders/:id", authenticate, async (req: Request, res: Response) => {
  const currentUserId = req.user.id;
  const orderId = req.params.id;

  // 1. Veritabanı sorgusunda hem sipariş ID'si hem de oturumdaki kullanıcı ID'si aranır!
  const order = await db.order.findFirst({
    where: {
      id: orderId,
      userId: currentUserId // SAHİPLİK KONTROLÜ (Ownership Verification)
    }
  });

  // Bilgi sızdırmamak için 403 yerine 404 döneriz (Saldırgan siparişin var olup olmadığını bilemez)
  if (!order) {
    return res.status(404).json({ error: "Sipariş bulunamadı." });
  }

  return res.json({ success: true, data: order });
});""",
            "code_notes_tr": "Sorguya `userId: currentUserId` koşulu eklenerek IDOR açığı kökten kapatılmıştır. Ayrıca bulunamadığında 403 yerine `404 Not Found` dönülerek saldırganın sistemdeki diğer sipariş ID'lerini taraması (Enumeration Attack) engellenmiştir.",
            "code_notes_en": "Adding `userId: currentUserId` guarantees tenant isolation directly inside the SQL query. Returning `404 Not Found` rather than 403 thwarts enumeration probes by obscuring whether the foreign ID exists.",
            "pitfalls_tr": [
                {"trap": "URL'deki ID'nin kullanıcının kendi verisi olduğunu varsaymak (IDOR).", "solution": "Her veritabanı sorgusunda `WHERE id = ? AND userId = ?` sahiplik kontrolü yapın."},
                {"trap": "React'te `dangerouslySetInnerHTML` kullanarak kullanıcı girdisini doğrudan ekrana basmak (XSS).", "solution": "Zorunlu olmadıkça asla ham HTML render etmeyin; DOMPurify ile temizleyin."},
                {"trap": "Güvenlik açıklarını sadece frontend tarafında gizlemeye çalışmak.", "solution": "Frontend güvenlik sağlamaz; tüm kontroller backend tarafında yapılmalıdır."}
            ],
            "pitfalls_en": [
                {"trap": "Assuming an authenticated caller owns the resource ID passed in route parameters (IDOR).", "solution": "Always anchor lookups with tenant constraints (`WHERE id = ? AND userId = ?`)."},
                {"trap": "Bypassing React's built-in escaping via `dangerouslySetInnerHTML` without DOMPurify sanitization.", "solution": "Never render unsanitized HTML directly from user-supplied inputs."},
                {"trap": "Relying on frontend validations or hidden form fields for access control.", "solution": "Client-side checks provide user experience only; absolute security enforcement happens on backend servers."}
            ],
            "udemy_title_tr": "Ders 44: OWASP Top 10 - Web Açıklarını Kapatmak",
            "udemy_title_en": "Lecture 44: OWASP Top 10 - Bulletproof Full-Stack Defense",
            "udemy_slides_tr": [
                "OWASP Top 10 nedir ve neden endüstri standardıdır?",
                "IDOR (Yetkisiz Nesne Erişimi) açığının anatomisi ve çözümü.",
                "XSS (Cross-Site Scripting) ve React'te güvenli render alma.",
                "SameSite Çerezler ve CSRF saldırılarını engellemek."
            ],
            "udemy_slides_en": [
                "What is the OWASP Top 10 and why does every enterprise audit against it?",
                "The anatomy of IDOR (Broken Object-Level Authorization).",
                "Cross-Site Scripting (XSS) and safe DOM rendering conventions.",
                "Hardening against CSRF attacks using `SameSite=Strict` cookies."
            ],
            "udemy_demo_tr": "Postman ile iki farklı kullanıcı token'ı oluşturun. Kullanıcı A'nın oluşturduğu siparişi, Kullanıcı B'nin token'ı ile çekmeye çalışın. Naive kodda siparişin sızdığını, sahiplik kontrolü eklenince 404 döndüğünü canlı gösterin.",
            "udemy_demo_en": "Simulate two distinct user sessions in Postman. Attempt to query User A's order using User B's auth token. Show the naive route leak, then apply the ownership check to demonstrate an immediate 404 response.",
            "action_task_tr": "Projenizdeki tüm `GET /resource/:id` ve `DELETE /resource/:id` endpoint'lerini inceleyin. Her birinde oturum açan kullanıcının sahiplik kontrolünün (ownership check) yapıldığını doğrulayın.",
            "action_task_en": "Audit every parametric resource route (`/api/items/:id`) in your codebase to verify that mutations and reads are strictly scoped to the requesting tenant ID.",
            "quiz_tr": [
                {
                    "question": "IDOR (Insecure Direct Object Reference) güvenlik açığı tam olarak nasıl meydana gelir?",
                    "options": [
                        "A) Bilgisayarın klavyesinin bozulmasıyla",
                        "B) Uygulamanın, URL veya istek parametresindeki ID üzerinden veriyi çekerken, oturum açmış kullanıcının o veriye erişim hakkı olup olmadığını (sahiplik) denetlememesiyle",
                        "C) Sadece CSS dosyalarında",
                        "D) İnternet kablosu çekildiğinde"
                    ],
                    "answer": "B",
                    "explanation": "IDOR, bir kullanıcının sadece URL'deki ID numarasını (örn: 101 yerine 102 yazarak) değiştirip başkalarının verilerine erişebilmesidir."
                },
                {
                    "question": "React uygulamalarında kullanıcı girdilerini ekrana basarken XSS açığı oluşmasını varsayılan olarak engelleyen mekanizma nedir?",
                    "options": [
                        "A) Otomatik HTML Entity Escaping (React süslü parantezler `{value}` içindeki tüm tehlikeli HTML karakterlerini otomatik olarak zararsız metne dönüştürür)",
                        "B) Bilgisayarın antivirüsü",
                        "C) Sadece Google Chrome kullanılması",
                        "D) TypeScript derleyicisi"
                    ],
                    "answer": "A",
                    "explanation": "React, JSX içindeki değişkenleri ekrana basarken `<script>` gibi tehlikeli etiketleri otomatik olarak escape eder (`&lt;script&gt;`); bu sayede kod çalışamaz."
                }
            ],
            "quiz_en": [
                {
                    "question": "How does an Insecure Direct Object Reference (IDOR) vulnerability manifest?",
                    "options": [
                        "A) Physical hardware driver corruptions",
                        "B) The application retrieves records based on a client-supplied identifier without verifying that the authenticated user owns that specific resource",
                        "C) Exclusively within CSS stylesheets",
                        "D) Network disconnects"
                    ],
                    "answer": "B",
                    "explanation": "IDOR occurs when an application exposes a reference to an internal object (e.g., database ID) without verifying access authorization."
                },
                {
                    "question": "What native framework mechanism protects React applications from Cross-Site Scripting (XSS) by default?",
                    "options": [
                        "A) Automated HTML entity escaping inside JSX interpolation braces (`{content}`)",
                        "B) Operating system antivirus software",
                        "C) Chrome browser exclusivity",
                        "D) Static typing in TypeScript"
                    ],
                    "answer": "A",
                    "explanation": "React automatically escapes raw string values bound inside JSX expressions, rendering malicious script tags as harmless text nodes."
                }
            ]
        },

        # Chapter 45
        {
            "id": 45,
            "section_id": 8,
            "slug_tr": "ch45_api_guvenligi_ve_rate_limiting",
            "slug_en": "ch45_api_hardening_rate_limiting_input_sanitization",
            "title_tr": "API Güvenliği & Rate Limiting: Sistemini Korumak",
            "title_en": "API Hardening: Rate Limiting, CORS & Input Sanitization",
            "subtitle_tr": "Brute-Force ve DoS Saldırılarına Karşı Hız Sınırları ve Güvenlik Başlıkları",
            "subtitle_en": "Thwarting Brute-Force and DoS Outages via Sliding-Window Rate Limiters and CORS",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Bir saldırgan `/api/login` endpoint'ine saniyede 10.000 şifre denemesi gönderdiğinde sunucunuz neden 20 saniyede çöker ve Rate Limiting sistemi nasıl kurtarır?",
            "podcast_hook_en": "When a botnet hammers your `/api/login` endpoint with 10,000 credential guesses per second, why does your server freeze, and how does token-bucket rate limiting shield APIs?",
            "takeaways_tr": [
                "Rate Limiting (Hız Sınırlaması), bir IP veya kullanıcının belirli bir zaman diliminde yapabileceği istek sayısını sınırlayan emniyet sübabıdır.",
                "Helmet.js, tarayıcıları koruyan kritik HTTP güvenlik başlıklarını (Content-Security-Policy, HSTS) tek satırda enjekte eder.",
                "CORS (Cross-Origin Resource Sharing), rastgele yabancı web sitelerinin kullanıcılarınız adına API istekleri atmasını engeller."
            ],
            "takeaways_en": [
                "Rate limiting bounds incoming request volume per IP or token, providing a critical circuit-breaker against brute-force attacks.",
                "Helmet.js automatically injects security headers (CSP, HSTS, X-Content-Type-Options) to harden client browsers.",
                "CORS prevents arbitrary third-party web domains from issuing unauthorized credentialed requests against your API."
            ],
            "story_tr": """Bir gece kulübünün kapısını düşünün.

Kapıda bir güvenlik görevlisi (Bouncer) var. Eğer güvenlik olmasaydı ne olurdu? 5.000 kişilik bir holigan grubu aynı anda kapıya yüklenir, kapıyı kırar ve kulübü yerle bir ederdi! (DDoS Saldırısı).

Güvenlik görevlisi ne yapar?
- Kapıda sıra oluşturur: *"Her dakikada sadece 5 kişi içeri girebilir!"* (Rate Limiting).
- Girenlerin üzerini arar, kesici aletleri toplar (Input Sanitization).
- Davetiyesi olmayanları kapıdan çevirir (CORS).

Yazılımda bir API geliştirdiğinizde internetteki tüm botlar ve kötü niyetli tarayıcılar o kapıya koşar. Kapıya bir nöbetçi koymazsanız sunucunuz 1 dakikada çöker.""",
            "story_en": """Consider the entrance of a high-capacity concert hall.

A team of door security guards manages admission. If the doors were left completely unmonitored, an unruly mob of 10,000 would charge the foyer simultaneously, trampling patrons and shattering doors (DoS attack).

Door security enforces structural safety:
- Admission throttling: *"Only 5 patrons through the turnstiles every 60 seconds"* (Rate Limiting).
- Bag inspections: Metal detectors confiscate weapons (Input Sanitization).
- Ticket verification: Rejecting visitors without authorized passes (CORS).

Exposing an API to the public internet invites automated scanners and credential-stuffing botnets. Deploying without admission rate limiters guarantees operational collapse.""",
            "mental_tr": """API Güvenlik Duvarı Mimarisi:

```
[Gelen İstek: POST /api/login]
               │
               ▼
[1. HELMET: Güvenlik Başlıkları] (HSTS, No-Sniff, CSP)
               │
               ▼
[2. CORS KONTROLÜ] ──> "İstek izinli domainden (app.sirket.com) mi geliyor?"
               │
               ▼
[3. RATE LIMITER (Redis)] ──> "Bu IP son 1 dakikada 5'ten fazla denedi mi?"
               │
       ┌───────┴───────┐
       ▼               ▼
[LİMİT AŞILDI (429)] [ONAYLANDI (Geçebilir)]
(Too Many Requests)    │
                       ▼
             [4. ZOD DOĞRULAMASI]
             (Zararlı karakterleri filtrele)
```""",
            "mental_en": """The Hardened API Gateway Pipeline:

```
[Inbound Traffic: POST /api/v1/auth/login]
                   │
                   ▼
[1. HELMET HEADERS] (Enforces HSTS, CSP, X-Frame-Options)
                   │
                   ▼
[2. CORS ENFORCEMENT] ──> "Does origin header match allowed whitelist?"
                   │
                   ▼
[3. RATE LIMITER (Redis Token Bucket)] ──> "Has this IP exceeded 5 attempts/min?"
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
[LIMIT TRIPPED: 429]   [ADMITTED: PASS]
(Too Many Requests)           │
                              ▼
                    [4. SCHEMA PARSER (Zod)]
                    (Strip unexpected properties)
```""",
            "prompt_tr": """# ROL: API Güvenliği ve Altyapı Uzmanı
Express.js projemize kapsamlı bir güvenlik zırhı ekleyeceğiz.

## GÖREV:
1. `express-rate-limit` kullanarak `/api/auth/*` rotalarına dakikada en fazla 5 deneme sınırı koyan ve 429 Too Many Requests dönen middleware'i yaz.
2. `helmet` ve katı `cors` yapılandırmasını güvenli şekilde kur.
3. Redis tabanlı bir rate limiter'ın (Sliding Window) neden çoklu sunucularda (Cluster) zorunlu olduğunu açıkla.""",
            "prompt_en": """# ROLE: Infrastructure Security Specialist
We are hardening an Express.js API cluster.

## TASK:
1. Implement a rate-limiting middleware restricting `/api/auth/*` routes to 5 requests per minute, returning HTTP 429.
2. Configure `helmet` and strict `cors` origins for production.
3. Explain why distributed Redis Sliding-Window rate limiters are mandatory over in-memory limiters across container clusters.""",
            "code_lang": "typescript",
            "code_naive": """// Kötü / Güvensiz Express Kurulumu: CORS her yere açık, hız sınırı yok, güvenlik başlığı yok!
import express from 'express';
const app = express();

app.use(cors()); // Tehlikeli: Tüm siteler (saldırganlar dahil) API'ye erişebilir!
// Rate limit yok: Saldırgan saniyede 100.000 şifre deneyebilir!
app.post('/login', (req, res) => { /* ... */ });""",
            "code_robust": """import express from "express";
import helmet from "helmet";
import cors from "cors";
import rateLimit from "express-rate-limit";

const app = express();

// 1. Güvenlik Başlıkları (Helmet)
app.use(helmet());

// 2. Katı CORS Yapılandırması
const allowedOrigins = ["https://app.sirketimiz.com"];
app.use(cors({
  origin: (origin, callback) => {
    if (!origin || allowedOrigins.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error("CORS İlkesi İhlali: Bu domaine erişim izni yok."));
    }
  },
  credentials: true, // HttpOnly çerezlere izin ver
  methods: ["GET", "POST", "PUT", "DELETE"]
}));

// 3. Hassas Giriş Rotaları İçin Hız Sınırı (Rate Limiting)
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 Dakika
  max: 5, // IP başına maksimum 5 başarısız deneme
  standardHeaders: true, // RateLimit-* standart başlıklarını dön
  legacyHeaders: false,
  message: {
    status: 429,
    error: "Çok fazla başarısız giriş denemesi. Lütfen 15 dakika sonra tekrar deneyin."
  }
});

// Giriş rotasına limitleyiciyi bağla
app.use("/api/auth/login", authLimiter);""",
            "code_notes_tr": "`helmet` ile kritik HTTP güvenlik başlıkları eklenmiş, `cors` ile sadece resmi şirket domainine izin verilmiş ve `authLimiter` ile şifre kaba kuvvet (Brute-Force) saldırıları 5 denemede durdurulmuştur.",
            "code_notes_en": "`helmet` injects defensive HTTP response headers, `cors` restricts browser requests strictly to authorized company domains, and `authLimiter` locks down brute-force attacks after 5 attempts per window.",
            "pitfalls_tr": [
                {"trap": "Çoklu sunucu (cluster / Docker) ortamında yerel bellek (in-memory) rate limiter kullanmak.", "solution": "Sunucu sayısı birden fazlaysa rate limiting durumunu merkezi bir Redis kümesinde tutun."},
                {"trap": "CORS ayarında `origin: '*'` bırakıp kimlik doğrulamalı istekleri savunmasız bırakmak.", "solution": "Origin olarak daima açıkça onaylanmış güvenilir frontend alan adlarını belirtin."},
                {"trap": "DDoS saldırılarını sadece uygulama katmanında çözmeye çalışmak.", "solution": "Büyük hacimli volumetrik saldırılar için Cloudflare veya AWS Shield gibi CDN katmanlarını kullanın."}
            ],
            "pitfalls_en": [
                {"trap": "Deploying in-memory rate limiters across multi-container Kubernetes pods.", "solution": "In distributed topologies, back rate-limiting state via shared Redis clusters so limits apply globally."},
                {"trap": "Permitting wildcard origins (`origin: '*'`) alongside credentialed cookies.", "solution": "Enforce explicit domain whitelists for cross-origin API exchanges."},
                {"trap": "Attempting to absorb volumetric multi-gigabit DDoS attacks at the Node.js application layer.", "solution": "Deflect volumetric flood attacks upstream via Cloudflare or AWS CloudFront/WAF edge shields."}
            ],
            "udemy_title_tr": "Ders 45: API Güvenliği - Rate Limiting ve Helmet ile Korunma",
            "udemy_title_en": "Lecture 45: API Hardening - Thwarting Attacks via Rate Limiting & CORS",
            "udemy_slides_tr": [
                "Brute-Force ve DoS saldırılarının maliyeti.",
                "Rate Limiting mantığı: Sliding Window vs Token Bucket.",
                "Helmet.js ile tek satırda 11 güvenlik başlığı enjekte etmek.",
                "CORS (Cross-Origin Resource Sharing) nedir ve nasıl yapılandırılır?"
            ],
            "udemy_slides_en": [
                "Quantifying the operational risk of credential stuffing and DoS attacks.",
                "Rate limiting algorithms: Sliding Windows vs. Token Buckets.",
                "Injecting 11 hardened security headers instantly with Helmet.js.",
                "Demystifying CORS (Cross-Origin Resource Sharing) policies."
            ],
            "udemy_demo_tr": "Express API'de login rotasına rate limit koyun. Bir for döngüsüyle arka arkaya 6 kez istek atın. İlk 5 isteğin 200 aldığını, 6. isteğin anında `429 Too Many Requests` ile engellendiğini canlı terminalde gösterin.",
            "udemy_demo_en": "Attach a rate limiter to an Express route. Fire 6 rapid curl requests in a bash loop. Observe the first 5 return HTTP 200, while the 6th immediately trips an HTTP 429 Too Many Requests response.",
            "action_task_tr": "Projenizdeki API'ye `helmet` paketini ekleyin ve `/login` rotasına IP başına 15 dakikada en fazla 10 istek sınırı koyan bir rate limiter bağlayın.",
            "action_task_en": "Integrate Helmet and an Express rate-limiter into your project, capping authentication attempts to 10 per 15-minute window per IP.",
            "quiz_tr": [
                {
                    "question": "Bir API endpoint'ine belirlenen limitin üzerinde istek yapıldığında dönülmesi gereken standart HTTP durum kodu hangisidir?",
                    "options": [
                        "A) 200 OK",
                        "B) 404 Not Found",
                        "C) 429 Too Many Requests",
                        "D) 500 Internal Server Error"
                    ],
                    "answer": "C",
                    "explanation": "`429 Too Many Requests` durum kodu, istemcinin hız limitini aştığını ve belirli bir süre beklemesi gerektiğini bildiren RFC standardıdır."
                },
                {
                    "question": "CORS (Cross-Origin Resource Sharing) politikasının temel görevi nedir?",
                    "options": [
                        "A) İnterneti hızlandırmak",
                        "B) Bir web sitesinde çalışan zararlı JavaScript kodunun, kullanıcının bilgisi olmadan başka bir domaindeki API'ye yetkisiz istekler göndermesini tarayıcı seviyesinde engellemek",
                        "C) Veritabanını yedeklemek",
                        "D) CSS kodlarını küçültmek"
                    ],
                    "answer": "B",
                    "explanation": "CORS, tarayıcıların aynı köken politikasını (Same-Origin Policy) esnetirken hangi yabancı domainlerin API'ye erişebileceğini denetleyen güvenlik kalkanıdır."
                }
            ],
            "quiz_en": [
                {
                    "question": "Which RFC HTTP status code must be returned when a client breaches an active rate limit threshold?",
                    "options": [
                        "A) 200 OK",
                        "B) 404 Not Found",
                        "C) 429 Too Many Requests",
                        "D) 500 Internal Server Error"
                    ],
                    "answer": "C",
                    "explanation": "HTTP 429 explicitly communicates rate exhaustion, conventionally paired with a `Retry-After` header."
                },
                {
                    "question": "What is the primary security mandate of Cross-Origin Resource Sharing (CORS)?",
                    "options": [
                        "A) Increasing global network bandwidth",
                        "B) Governing which foreign web origins browsers permit to initiate cross-domain network requests to an API",
                        "C) Automating database dumps",
                        "D) Minifying stylesheet bundles"
                    ],
                    "answer": "B",
                    "explanation": "CORS enforces browser-level restrictions, preventing malicious websites from issuing unauthorized requests to authenticated backend services."
                }
            ]
        },

        # Chapter 46
        {
            "id": 46,
            "section_id": 8,
            "slug_tr": "ch46_gizli_bilgi_secrets_yonetimi_env",
            "slug_en": "ch46_secrets_management_never_commit_api_keys",
            "title_tr": "Gizli Bilgi (Secret) Yönetimi: API Anahtarlarını GitHub'a Yüklememek!",
            "title_en": "Secrets Management: Never Commit API Keys, Passwords or Tokens",
            "subtitle_tr": "GitHub'a Yanlışlıkla AWS Anahtarı Yükleyip 1 Saatte 50.000 Dolar Fatura Yeme Kabusu",
            "subtitle_en": "Avoiding the $50,000 Cloud Bill Nightmare via .env, GitGuardian and Vaults",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "GitHub'da açık (public) bir depoya AWS veya OpenAI API anahtarı yüklendiğinde, saldırgan botların o anahtarı bulup kripto para madenciliği başlatması kaç saniye sürer?",
            "podcast_hook_en": "When an AWS or OpenAI secret is committed to a public GitHub repo, how many seconds does it take for automated scraper botnets to weaponize it for crypto mining?",
            "takeaways_tr": [
                "Botlar GitHub'ın commit akışını gerçek zamanlı tarar; açık bir depoya düşen API anahtarı ortalama 60 saniye içinde istismar edilir.",
                "`.env` dosyası asla Git deposuna commit edilmemelidir; `.gitignore` dosyası ilk günden ayarlanmalıdır.",
                "Pre-commit hook'ları (TruffleHog, GitGuardian) hassas bilgilerin terminalden çıkmasını daha commit anında engeller."
            ],
            "takeaways_en": [
                "Adversarial botnets scrape public GitHub commit streams in real time; leaked cloud keys are weaponized within 60 seconds.",
                "`.env` files must NEVER be tracked in Git; establish rigid `.gitignore` entries from day zero.",
                "Pre-commit secret scanners (TruffleHog, Gitleaks, GitGuardian) block credential commits directly at the terminal boundary."
            ],
            "story_tr": """Genç bir yazılımcının gerçek hikayesini dinleyin:

Bir cumartesi gecesi OpenAI API'si ile harika bir yapay zeka botu kodluyor. Kod çalışıyor, heyecanla terminale koşuyor:
```bash
git add .
git commit -m "ilk versiyon bitti"
git push origin main
```
Yatağa gidip uyuyor. Sabah uyandığında telefonunda 42 adet acil durum e-postası var! AWS faturası: **64.000 Dolar!**

Ne oldu? Koddaki AWS API anahtarını GitHub'a yüklemişti. Kötü niyetli tarayıcı botlar 40 saniye içinde o anahtarı kaptı ve dünya çapında 150 adet devasa sunucu açarak kripto para madenciliği başlattı!

Gizli bilgiler (Secrets) kod tabanına asla yazılmaz. Kod bir arabanın şasisidir; API anahtarı ise sürücünün cebindeki kontak anahtarıdır. Anahtarı torpido gözüne bantlayıp arabayı sokakta bırakmazsınız!""",
            "story_en": """Consider this true incident from a junior developer's first hackathon:

On a Friday night, an engineer builds an AI agent. Excited that it works, they run:
```bash
git add .
git commit -m "it works!"
git push origin main
```
They go to sleep. They wake up Saturday morning to 38 urgent security alerts and an AWS cloud invoice for **$64,000!**

What happened? Their `AWS_SECRET_ACCESS_KEY` was committed inside an unignored `.env` file. Automated botnets scraped the commit within 45 seconds, launched 150 GPU compute clusters, and began mining cryptocurrency.

Secrets must NEVER live inside source repositories. Code is the vehicle's chassis; your API key is the ignition key in your pocket. You don't tape the ignition key to the exterior windshield!""",
            "mental_tr": """Güvenli Secrets Mimarisi:

```
[GELİŞTİRİCİ MAKİNESİ]
├── src/code.ts ──> (Git'e Gönderilir)
├── .env.example ──> (Git'e Gönderilir: Boş şablon)
└── .env ──────────> (ASLA GİT'E GİTMEZ! .gitignore ile Kilitli)
       │
       ▼
[PRODUCTION / CI ORTAMI]
└── Ortam Değişkenleri (Environment Variables):
    - AWS Secrets Manager / Doppler / Infisical / Vercel Env
```""",
            "mental_en": """The Enterprise Secrets Separation Model:

```
[LOCAL WORKSPACE]
├── src/index.ts   ──> (Committed to Git)
├── .env.example   ──> (Committed to Git: Empty template dummy keys)
└── .env           ──> (STRICTLY BANNED FROM GIT via `.gitignore`)
       │
       ▼
[PRODUCTION HOST]
└── Injected Environment Runtime:
    - AWS Secrets Manager / HashiCorp Vault / Doppler / Vercel Environment Variables
```""",
            "prompt_tr": """# ROL: DevSecOps ve Secrets Güvenliği Mühendisi
Projemizde API anahtarlarının yanlışlıkla Git'e yüklenmesini %100 engelleyecek bir güvenlik sistemi kuracağız.

## GÖREV:
1. Kapsamlı bir `.gitignore` dosyası hazırla (`.env`, `.env.local`, pem dosyaları vb.).
2. Takım arkadaşları için güvenli bir `.env.example` şablonu oluştur.
3. Husky ve `gitleaks` kullanarak geliştirici commit atmadan önce gizli bilgi taraması yapan 'Pre-commit Hook' kurulumunu göster.""",
            "prompt_en": """# ROLE: DevSecOps & Secrets Security Engineer
We must establish an unbreachable secrets defense pipeline.

## TASK:
1. Draft a comprehensive `.gitignore` entry guarding all sensitive configuration vectors.
2. Provide a sanitized `.env.example` template for team onboarding.
3. Configure a pre-commit hook using Husky and `gitleaks` to abort commits containing accidental secrets.""",
            "code_lang": "bash",
            "code_naive": """# Kötü .gitignore: .env dosyası unutulmuş!
node_modules/
dist/
# .env unutulduğu için tüm şifreler GitHub'a sızar!""",
            "code_robust": """# 1. Kapsamlı .gitignore Dosyası (.gitignore)
# Ortam değişkenleri ve gizli anahtarlar
.env
.env.*
!.env.example
*.pem
*.key
*.cert
credentials.json
id_rsa

# 2. Örnek Güvenli Şablon (.env.example - Git'e commit edilir)
DATABASE_URL="postgresql://user:password@localhost:5432/mydb"
JWT_SECRET="buraya_en_az_32_karakterlik_gizli_anahtar_yazin"
STRIPE_SECRET_KEY="sk_test_ornek_anahtar"

# 3. Gitleaks Pre-commit Hook Kurulumu (Husky ile)
# Terminalde çalıştırın:
# npx husky init
# echo "npx gitleaks protect --staged --verbose" > .husky/pre-commit
# Artık commit atarken gizli anahtar varsa Git işlemi anında durdurur!""",
            "code_notes_tr": "`.env.example` dosyası şifre içermez, sadece geliştiricilere hangi değişkenlerin tanımlanması gerektiğini gösterir. Husky pre-commit hook'u ise insan dalgınlığını ortadan kaldırarak şifre içeren commit'leri terminalde engeller.",
            "code_notes_en": "`.env.example` supplies the configuration schema with dummy placeholders. The Husky pre-commit hook automates verification, refusing to create commits if Gitleaks detects cryptographic keys.",
            "pitfalls_tr": [
                {"trap": "GitHub'a şifre yükledikten sonra 'Hemen bir commit atıp sildim' diyerek rahatlamak.", "solution": "Git geçmişi silinen her şeyi saklar! Şifre bir kez commit edildiyse o anahtar ÖLMÜŞTÜR; anında revoke (iptal) edin."},
                {"trap": "Frontend kodunun (React/Next.js) içine gizli API anahtarı yazmak.", "solution": "Frontend koduna yazılan her şey tarayıcıda herkes tarafından okunabilir; gizli anahtarları sadece backend'de tutun."},
                {"trap": ".env dosyasını Slack veya e-posta üzerinden takım arkadaşına göndermek.", "solution": "Gizli bilgileri paylaşmak için 1Password, Bitwarden veya Doppler gibi güvenli şifre yöneticileri kullanın."}
            ],
            "pitfalls_en": [
                {"trap": "Believing that committing a deletion commit ('removed keys') fixes a leak.", "solution": "Git retains complete historical commits. Once committed, consider that secret fully compromised: rotate it immediately."},
                {"trap": "Embedding server-side API secrets inside client-side frontend code (`NEXT_PUBLIC_SECRET`).", "solution": "Anything delivered to client bundles is public to anyone inspecting DevTools. Keep private secrets strictly in backend runtimes."},
                {"trap": "Sharing `.env` files via Slack, WhatsApp, or email attachments.", "solution": "Exchange environment secrets via dedicated credential managers (1Password, Doppler, Infisical)."}
            ],
            "udemy_title_tr": "Ders 46: Secrets Yönetimi - API Anahtarlarını Korumak",
            "udemy_title_en": "Lecture 46: Secrets Management - Preventing Disaster Leaks",
            "udemy_slides_tr": [
                "64.000 Dolarlık Bulut Faturası: Bir sızıntının gerçek anatomisi.",
                ".env vs .env.example felsefesi.",
                "Gitleaks ve TruffleHog ile commit öncesi otomatik güvenlik kapıları.",
                "Eğer anahtar sızarsa ne yapılmalı? Anında İptal (Revocation) protokolü."
            ],
            "udemy_slides_en": [
                "The $64,000 Cloud Bill: Anatomical breakdown of a credential leak.",
                "The `.env` vs. `.env.example` paradigm.",
                "Automated pre-commit gating via Gitleaks and TruffleHog.",
                "Emergency response: Key revocation and rotation protocol."
            ],
            "udemy_demo_tr": "Kasıtlı olarak sahte bir Stripe anahtarı içeren dosya oluşturup commit etmeye çalışın. Gitleaks pre-commit hook'unun devreye girip commit'i kırmızı alarm ile engellediğini canlı terminalde gösterin.",
            "udemy_demo_en": "Stage a file containing a mock private key string. Attempt to run `git commit`. Watch the Gitleaks pre-commit hook intercept the command and abort the commit with an alert.",
            "action_task_tr": "Projenizdeki `.gitignore` dosyasını açın. `.env` ve türevlerinin (`.env*.local`) kilitli olduğundan emin olun ve bir `.env.example` şablonu hazırlayın.",
            "action_task_en": "Audit your repository's `.gitignore` to ensure all `.env` variants are excluded, and verify a clean `.env.example` template exists.",
            "quiz_tr": [
                {
                    "question": "Bir API anahtarını yanlışlıkla public (açık) bir GitHub reposuna push ettiğinizde yapılması gereken İLK ve ACİL işlem nedir?",
                    "options": [
                        "A) GitHub'dan hemen yeni bir commit ile anahtarı silmek",
                        "B) İlgili servisin (AWS, OpenAI, Stripe) yönetim paneline girip o API anahtarını ANINDA İPTAL ETMEK (Revoke / Deactivate) ve yenisini üretmek",
                        "C) Bilgisayarı kapatıp beklemek",
                        "D) Depoyu private yapmak"
                    ],
                    "answer": "B",
                    "explanation": "GitHub'daki botlar saniyeler içinde anahtarı kaydeder; depoyu silseniz bile anahtar saldırganın elindedir. Tek kurtuluş anahtarı derhal iptal etmektir."
                },
                {
                    "question": "Bir projede `.env.example` dosyasının varoluş amacı nedir?",
                    "options": [
                        "A) Gerçek şifreleri saklamak",
                        "B) Gerçek değerler içermeden, projeyi çalıştıracak diğer geliştiricilere hangi ortam değişkenlerinin gerekli olduğunu gösteren temiz bir şablon sunmak",
                        "C) CSS dosyalarını derlemek",
                        "D) Testleri hızlandırmak"
                    ],
                    "answer": "B",
                    "explanation": "`.env.example`, şifreleri ifşa etmeden yeni katılan geliştiricilerin hangi anahtarlara ihtiyaç duyduğunu gösteren güvenli dokümantasyon şablonudur."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the mandatory FIRST emergency action upon accidentally pushing a private cloud credential to a public Git repository?",
                    "options": [
                        "A) Pushing a new commit that deletes the text line",
                        "B) Immediately revoking (deactivating) the compromised key in the provider console (AWS, Stripe, OpenAI) and rotating credentials",
                        "C) Shutting down your local laptop",
                        "D) Toggling the repository from public to private"
                    ],
                    "answer": "B",
                    "explanation": "Scraper bots snapshot commits within seconds. Even if you delete the commit, the key is already compromised; immediate provider-level revocation is mandatory."
                },
                {
                    "question": "What is the primary architectural purpose of maintaining a `.env.example` file in version control?",
                    "options": [
                        "A) Storing live production credentials",
                        "B) Providing a clean, dummy-populated configuration blueprint showing onboarding engineers which variables must be provisioned",
                        "C) Compiling CSS modules",
                        "D) Accelerating unit tests"
                    ],
                    "answer": "B",
                    "explanation": "`.env.example` serves as self-documenting configuration specification without exposing sensitive secrets."
                }
            ]
        },

        # Chapter 47
        {
            "id": 47,
            "section_id": 8,
            "slug_tr": "ch47_telif_yazilim_lisanslari_ai_etigi",
            "slug_en": "ch47_software_licenses_ip_and_ai_ethics",
            "title_tr": "Telif Hakları, Lisanslar ve Kodun Hukuki Güvenliği",
            "title_en": "Code Licensing, Intellectual Property & AI Training Ethics",
            "subtitle_tr": "GPL, MIT, Apache Lisansları ve Şirketinizi Davalardan Koruma Rehberi",
            "subtitle_en": "MIT vs. GPL Copyleft Hazards: Shielding Your Enterprise from Licensing Lawsuits",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Bir açık kaynak projesinden kopyalanan 10 satırlık GPL lisanslı bir kod, şirketinizin tüm ticari kod tabanını açık kaynak yapmaya zorlayabilir mi?",
            "podcast_hook_en": "Can 10 lines of GPL-licensed copyleft code inadvertently copied by an AI model legally compel your enterprise to open-source its proprietary codebase?",
            "takeaways_tr": [
                "Açık kaynak 'sahipsiz' demek değildir; her kütüphanenin yasal bir lisansı ve kullanım şartı vardır.",
                "MIT ve Apache 2.0 lisansları son derece esnektir ve ticari yazılımlarda serbestçe kullanılabilir.",
                "GPL (Copyleft) lisansı 'bulaşıcıdır' (Viral); ticari kapalı kaynak bir projeye GPL kod dahil edilirse tüm projenin açık kaynak yapılması gerekebilir."
            ],
            "takeaways_en": [
                "Open source does not equal public domain; every package carries legally enforceable intellectual property licenses.",
                "Permissive licenses (MIT, Apache 2.0, BSD) permit commercial proprietary closed-source redistribution.",
                "GPL (Copyleft) is viral: incorporating GPL-licensed logic into a proprietary system can legally compel you to open-source your entire proprietary codebase."
            ],
            "story_tr": """Bir otomobil fabrikası kurduğunuzu ve milyon dolarlık lüks bir araba ürettiğinizi düşünün.

Motor ustası bir cıvata eksik olunca yan sanayiden bedava bir cıvata bulup takıyor. Fakat o cıvatanın üzerinde küçük bir patent yazısı var: *"Bu parçayı kullanan her araba halka ücretsiz dağıtılmalıdır!"* (GPL Lisansı).

Şirketin avukatları bir gün kapınızı çalar ve der ki: *"O küçük parça yüzünden tüm fabrikanın planlarını ve arabalarımızı ücretsiz vermek zorundayız!"*

Yazılım dünyasında bu felaketi yaşayan dev şirketler oldu! 

Yapay zeka modelleri bazen GPL lisanslı kodları eğitim verisinden hatırlayıp sizin projenize kopyalayabilir. Bir mühendisin görevi, projeye giren her kütüphanenin lisans pasaportunu kontrol etmektir.""",
            "story_en": """Imagine manufacturing a multi-million-dollar luxury hypercar.

An assembly apprentice running low on fasteners finds a free steering column in an open salvage yard. Bolted to the column is an enforceable legal patent: *"Any vehicle incorporating this component must be published with full engineering blueprints for free public distribution."* (GPL Copyleft).

Corporate litigators arrive at your factory: *"Because of that single assembly part, you are legally compelled to open-source your entire proprietary drivetrain!"*

Multi-billion dollar enterprises have faced this exact legal crisis.

AI models occasionally regurgitate verbatim snippets learned from GPL repositories. An engineer must audit the legal passport of every dependency entering the codebase.""",
            "mental_tr": """Açık Kaynak Lisans Spektrumu:

```
[İTİBARLI & SERBEST (Permissive)]        [KATILIMCI & KISITLAYICI (Copyleft)]
          MIT / Apache 2.0 / BSD                         GPL v3 / AGPL
                    │                                          │
                    ▼                                          ▼
- Ticari projelerde serbestçe kullanılabilir. - Kodunu değiştirip dağıtırsan,
- Kodunu kapalı tutabilirsin.                 KENDİ KODUNU DA açık kaynak
- Sadece telif bildirimini sakla.             yapmak ZORUNDASIN! ("Bulaşıcı")
```""",
            "mental_en": """The Open Source Licensing Spectrum:

```
[PERMISSIVE (Commercial-Friendly)]         [COPYLEFT (Viral Reciprocal)]
       MIT / Apache 2.0 / BSD                         GPL v3 / AGPL
                 │                                          │
                 ▼                                          ▼
- Fully permissible in proprietary apps.    - Incorporating into private code
- Zero requirement to publish source.       forces your entire application
- Retain copyright attribution line.        to be open-sourced under GPL!
```""",
            "prompt_tr": """# ROL: Fikri Mülkiyet ve Yazılım Hukuku Danışmanı
Şirketimiz kapalı kaynak (proprietary) bir ticari SaaS ürünü geliştiriyor.

## GÖREV:
1. MIT, Apache 2.0 ve GPL v3 lisansları arasındaki temel hukuki farkları açıkla.
2. Neden şirket projelerinde GPL v3 lisanslı npm veya pip paketlerinin kullanılmasının riskli olduğunu belirt.
3. CI pipeline'ımızda lisans uyumluluğunu otomatik denetleyen bir araç (`license-checker` veya `fossa`) yapılandırma örneği sun.""",
            "prompt_en": """# ROLE: Intellectual Property & Open Source Compliance Specialist
Our organization develops proprietary, closed-source B2B SaaS software.

## TASK:
1. Contrast the legal obligations of MIT, Apache 2.0, and GPL v3 licenses.
2. Detail why introducing GPL/AGPL dependencies into closed-source repositories triggers catastrophic intellectual property risks.
3. Provide an automated CI license auditing workflow using `license-checker` to block non-compliant dependencies.""",
            "code_lang": "json",
            "code_naive": """// Lisans Denetimi Yapmayan Şirket:
// Geliştirici bilmeden "gpl-calculator" paketini ekler ve tüm şirket kodu tehlikeye girer!
"dependencies": {
  "super-secret-calculator": "gpl-licensed-package"
}""",
            "code_robust": """// CI Pipeline Lisans Denetim Yapılandırması (package.json scripti)
{
  "scripts": {
    "audit:licenses": "npx license-checker --onlyAllow 'MIT;Apache-2.0;BSD-2-Clause;BSD-3-Clause;ISC' --summary"
  }
}

// GitHub Actions Adımı:
// - name: 🛡️ Yasal Lisans Denetimi
//   run: npm run audit:licenses
// Eğer birisi GPL veya AGPL lisanslı paket eklerse CI derlemeyi anında iptal eder!""",
            "code_notes_tr": "`license-checker` aracı ile sadece onaylı izinli lisanslar (`MIT`, `Apache-2.0`, `BSD`) kabul edilir; GPL gibi kapalı kaynak projeyi tehlikeye atacak bir lisans tespit edildiğinde derleme bloke edilir.",
            "code_notes_en": "`license-checker` enforces an automated whitelist (MIT, Apache-2.0, BSD). If a dependency introduces a copyleft GPL/AGPL license, the CI pipeline halts immediately, protecting proprietary IP.",
            "pitfalls_tr": [
                {"trap": "GitHub'da bulduğu her açık kaynak kodu lisansına bakmadan ticari projeye kopyalamak.", "solution": "Her kütüphanenin `LICENSE` dosyasını kontrol edin; şüphe durumunda MIT veya Apache tercih edin."},
                {"trap": "Yapay zekanın ürettiği büyük kod bloklarının telifli kaynaklardan birebir ezberlenmiş (memorized) olabileceğini unutmak.", "solution": "AI araçlarında 'public code matching' / 'telemetri eşleme' filtresini daima açık tutun."},
                {"trap": "AGPL lisanslı bir servisi ağ üzerinden çağırıp lisans şartlarına uymamak.", "solution": "AGPL ağ üzerinden kullanımda dahi kaynak kodun açılmasını zorunlu kılar; şirketlerde çok dikkatli kullanılmalıdır."}
            ],
            "pitfalls_en": [
                {"trap": "Copying code snippets from public forums without auditing licensing headers.", "solution": "Verify the license provenance of external modules; default to permissive MIT or Apache 2.0."},
                {"trap": "Disabling public code matching filters inside AI IDE copilots.", "solution": "Keep AI copyright and public code match filters enabled to block regurgitated copyrighted blocks."},
                {"trap": "Underestimating the reach of AGPL (Affero GPL) microservices.", "solution": "AGPL triggers copyleft obligations over network execution; require explicit architectural sign-off before adopting AGPL tools."}
            ],
            "udemy_title_tr": "Ders 47: Yazılım Lisansları ve AI Etiği - Şirketi Korumak",
            "udemy_title_en": "Lecture 47: Software Licensing & AI Ethics - Legal Safeguards",
            "udemy_slides_tr": [
                "Açık kaynak lisanslarının anatomisi: Permissive vs Copyleft.",
                "GPL v3 tuzağı: Şirket kodlarını açık kaynak yapmak zorunda kalmak.",
                "AI modellerinin telifli kod kopyalama riski ve filtreler.",
                "Canlı Demo: CI pipeline'ında otomatik lisans denetimi kurmak."
            ],
            "udemy_slides_en": [
                "Anatomy of open source licenses: Permissive vs. Copyleft.",
                "The viral GPL dilemma: How copyleft can compel source disclosure.",
                "Mitigating regurgitation risks using AI public-code filters.",
                "Live demo: Automating license audits in GitHub Actions."
            ],
            "udemy_demo_tr": "Bir Node projesine `license-checker` kurun. `npm run audit:licenses` çalıştırıp projedeki tüm kütüphanelerin lisans dökümünü ekranda listeleyin. Kasıtlı olarak GPL lisanslı bir paket ekleyip denetimin nasıl hata verdiğini gösterin.",
            "udemy_demo_en": "Run `npx license-checker --summary` on a repository. Add a dummy GPL-licensed module and observe the automated compliance check abort the build.",
            "action_task_tr": "Projenizdeki `package.json` veya `requirements.txt` dosyalarını açın. Projenizde hangi açık kaynak lisanslarının kullanıldığını bir listeleyici araçla kontrol edin.",
            "action_task_en": "Run a license audit across your active repository's dependencies, verifying zero unapproved copyleft licenses exist in production bundles.",
            "quiz_tr": [
                {
                    "question": "Aşağıdaki yazılım lisanslarından hangisi ticari ve kapalı kaynaklı bir projede kodu açma zorunluluğu olmadan en serbestçe kullanılabilir?",
                    "options": [
                        "A) GPL v3",
                        "B) AGPL v3",
                        "C) MIT Lisansı",
                        "D) Lisanssız kodlar"
                    ],
                    "answer": "C",
                    "explanation": "MIT Lisansı, telif bildirimi korunduğu sürece kodun ticari kapalı kaynaklı projelerde serbestçe kullanılmasına, değiştirilmesine ve satılmasına izin verir."
                },
                {
                    "question": "GPL lisansının 'Bulaşıcı' (Viral / Copyleft) olarak adlandırılmasının sebebi nedir?",
                    "options": [
                        "A) Bilgisayarlara virüs bulaştırması",
                        "B) GPL lisanslı bir kod parçasını veya kütüphaneyi kullanan bir yazılımın da zorunlu olarak GPL lisansıyla açık kaynak yapılmasını hukuken şart koşması",
                        "C) Sadece kış aylarında çalışması",
                        "D) Kodun silinmesine sebep olması"
                    ],
                    "answer": "B",
                    "explanation": "GPL, kendi kodundan türetilen tüm yazılımların da aynı şekilde özgür ve açık kaynak olmasını şart koşar (Reciprocal / Copyleft)."
                }
            ],
            "quiz_en": [
                {
                    "question": "Which software license offers maximum permissiveness for commercial proprietary software without requiring source disclosure?",
                    "options": [
                        "A) GPL v3",
                        "B) AGPL v3",
                        "C) MIT License",
                        "D) Unlicensed public code"
                    ],
                    "answer": "C",
                    "explanation": "The MIT license grants unrestricted rights to use, modify, merge, and sell software in proprietary products, requiring only copyright attribution."
                },
                {
                    "question": "Why is the GNU General Public License (GPL) characterized as 'viral' or copyleft?",
                    "options": [
                        "A) It distributes malware across networks",
                        "B) It legally requires any downstream derivative software incorporating GPL code to be open-sourced under the GPL license",
                        "C) It executes exclusively in winter months",
                        "D) It deletes source files upon compilation"
                    ],
                    "answer": "B",
                    "explanation": "GPL's copyleft clause mandates that any derivative system must be distributed under identical open-source GPL terms."
                }
            ]
        },

        # Chapter 48
        {
            "id": 48,
            "section_id": 8,
            "slug_tr": "ch48_savunmaci_programlama_sanati",
            "slug_en": "ch48_the_art_of_defensive_programming",
            "title_tr": "Savunmacı Programlama (Defensive Programming) Sanatı",
            "title_en": "The Art of Defensive Programming & Fail-Safe Design",
            "subtitle_tr": "'Murphy Kanunları'na Göre Kod Yazmak: Yanlış Gidebilecek Her Şey Yanlış Gidecektir",
            "subtitle_en": "Engineering for Murphy's Law: Designing Systems that Fail Safely and Recover",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Savunmacı programlama paranoyakça bir korku mudur, yoksa NASA'nın Mars araçlarını milyonlarca kilometre ötede hayatta tutan nihai mühendislik zihniyeti midir?",
            "podcast_hook_en": "Is defensive programming mere paranoia, or is it the exact fail-safe engineering discipline that keeps interplanetary Mars rovers operational?",
            "takeaways_tr": [
                "Savunmacı programlama: Girdilerin bozuk geleceğini, ağın kopacağını ve üçüncü taraf servislerin çökeceğini varsayarak kod yazmaktır.",
                "Fail-Safe (Güvenli Başarısızlık): Sistem çöktüğünde veriyi bozmadan veya güvenlik kapısını açık bırakmadan zararsız bir duruma geçmelidir.",
                "Circuit Breaker (Devre Kesici) deseni, çöken bir servise sürekli istek atıp sunucuyu kilitlemek yerine sistemi korumaya alır."
            ],
            "takeaways_en": [
                "Defensive programming assumes inputs will be corrupted, networks will disconnect, and external APIs will fail unexpectedly.",
                "Fail-Safe Design: When failure strikes, the system must transition into a safe fallback state without corrupting storage or exposing access.",
                "The Circuit Breaker pattern halts outbound network calls to failing external dependencies, preventing cascading system thread exhaustion."
            ],
            "story_tr": """Elektrik panolarındaki sigortaları (Fuses) düşünün.

Evinize aniden 10.000 voltluk bir yıldırım düştüğünde ne olur? Sigorta anında **"ÇAT!"** diye atar ve evin elektriğini keser. Buzdolabınız veya televizyonunuz yanmaz; sadece ev karanlıkta kalır. Sigorta kendini feda ederek tüm evi korumuştur!

İşte **Savunmacı Programlama (Defensive Programming)** ve **Circuit Breaker** o elektrik sigortasıdır:
Eğer ödeme yaptığınız bankanın sunucusu çöktüyse, uygulamanız kullanıcıya sonsuz yükleniyor (spinner) gösterip arkada binlerce istekle kendi sunucusunu boğmaz!

Sigortayı attırır: *"Şu an banka servislerinde geçici bir bakım var, lütfen 5 dakika sonra tekrar deneyin"* der ve sistemi güvenle ayakta tutar.""",
            "story_en": """Consider the mechanical circuit breakers in an electrical panel.

When a sudden 10,000-volt power surge hits a residence, what happens? The breaker snaps open immediately, cutting circuit power. The refrigerator and television remain unharmed; the lights simply go dark. The fuse sacrifices current to preserve the home.

**Defensive Programming** and the **Circuit Breaker Pattern** serve as that electrical fuse:
If an external payment API experiences an outage, your application should not hang in an infinite spinner loop while spawning thousands of doomed background retries that exhaust your web server's thread pool.

The circuit breaker trips: *"Payment gateway currently degraded; your order has been saved for automated settlement"*—failing safely while keeping the primary application operational.""",
            "mental_tr": """Circuit Breaker (Devre Kesici) Durum Makinesi:

```
         ┌──────────────────────────────────────┐
         ▼                                      │
    [KAPALI (CLOSED)]                           │ (Başarılı Deneme)
    - Sistem normal çalışıyor.                  │
    - İstekler servise iletiliyor.               │
         │                                      │
         │ (Peş peşe 5 hata oluştu!)            │
         ▼                                      │
    [AÇIK (OPEN)] ──────────────────────┐       │
    - İstekler servise GİTMEZ!          │       │
    - Anında fallback hata dönülür.     │       │
    - Servis dinlendirilir (30 saniye)   │       │
                                        │       │
                                        ▼       │
                              [YARI-AÇIK (HALF-OPEN)]
                              - Tek bir deneme isteği gönderilir.
                              - Başarısız olursa -> Tekrar AÇIK'a döner!
```""",
            "mental_en": """The Circuit Breaker State Transition Engine:

```
        ┌──────────────────────────────────────┐
        ▼                                      │
   [CLOSED STATE]                              │ (Canary Test Succeeds)
   - Normal operation.                         │
   - Requests flow to downstream service.      │
        │                                      │
        │ (5 consecutive timeouts trip breaker)│
        ▼                                      │
   [OPEN STATE] ───────────────────────┐       │
   - Downstream calls BLOCKED immediately.     │
   - Immediate fallback returned (<1ms).       │
   - Cooldown window active (30 seconds).      │
                                       │       │
                                       ▼       │
                             [HALF-OPEN STATE]
                             - Dispatches a single canary probe request.
                             - If canary fails -> Trips back to OPEN!
```""",
            "prompt_tr": """# ROL: Yüksek Güvenilirlikli Sistemler Mimarı
Üçüncü taraf bir döviz kuru API'sine bağımlı bir finansal servis yazıyoruz.

## GÖREV:
1. Savunmacı programlama ilkelerine uygun olarak bir Circuit Breaker deseni tasarla.
2. Servis çöktüğünde veya 2 saniye içinde yanıt vermediğinde (timeout), anında son bilinen önbellekteki kuru dönen (Fallback) mekanizmasını kur.
3. Arka arkaya 3 hata olduğunda devreyi AÇIK (OPEN) duruma getiren tip güvenli TypeScript kodunu yaz.""",
            "prompt_en": """# ROLE: Resilient Systems Architect
We depend on an external currency exchange rate API.

## TASK:
1. Implement a Circuit Breaker complying with defensive programming principles.
2. If the API fails or times out beyond 2,000ms, immediately fall back to the last known cached rate.
3. Automatically trip the circuit to OPEN after 3 consecutive failures to protect system threads.""",
            "code_lang": "typescript",
            "code_naive": """// Savunmasız Kod: Timeout yok, hata kontrolü yok, sonsuz bekleme riski!
export async function getExchangeRateNaive() {
  // Dış servis çökerse bu fonksiyon dakikalarca asılı kalır ve tüm sunucuyu kilitler!
  const res = await fetch("https://api.currency.com/rates");
  const data = await res.json();
  return data.rates.USD;
}""",
            "code_robust": """// Savunmacı Mimari: Timeout + Circuit Breaker + Fallback Kalkanı

export class ResilientCurrencyService {
  private failureCount = 0;
  private circuitOpenUntil = 0;
  private lastKnownRate = 34.50; // Fallback varsayılanı

  async getUsdRate(): Promise<{ rate: number; isFallback: boolean }> {
    const now = Date.now();

    // 1. Sigorta Kontrolü (Circuit Breaker Açık mı?)
    if (now < this.circuitOpenUntil) {
      console.warn("[Circuit Breaker] Servis açık durumda, doğrudan fallback dönülüyor.");
      return { rate: this.lastKnownRate, isFallback: true };
    }

    try {
      // 2. Zaman Aşımı Koruması (2 Saniye Sınırı)
      const res = await fetch("https://api.currency.com/rates", {
        signal: AbortSignal.timeout(2000)
      });

      if (!res.ok) throw new Error(`HTTP Hata: ${res.status}`);

      const data = await res.json();
      this.lastKnownRate = data.rates.USD;
      this.failureCount = 0; // Başarı durumunda sayacı sıfırla

      return { rate: this.lastKnownRate, isFallback: false };
    } catch (error) {
      this.failureCount++;
      console.error(`Döviz servisi hatası (${this.failureCount}/3):`, error);

      // 3. Eşik Aşımı: 3 hata üst üste gelirse sigortayı 1 dakika attır!
      if (this.failureCount >= 3) {
        this.circuitOpenUntil = now + 60 * 1000;
        console.error("[Circuit Breaker] Sigorta attı! 1 dakika boyunca dış çağrı yapılmayacak.");
      }

      // 4. Fail-Safe: Sistem çökmez, son bilinen güvenli kuru döner
      return { rate: this.lastKnownRate, isFallback: true };
    }
  }
}""",
            "code_notes_tr": "`AbortSignal.timeout(2000)` ile isteklerin sonsuza kadar asılı kalması engellenmiş, 3 ardışık hatada devre açılarak çöken servise boşuna istek atılması durdurulmuş ve son bilinen kur ile kesintisiz hizmet (graceful degradation) sağlanmıştır.",
            "code_notes_en": "`AbortSignal.timeout(2000)` eliminates hanging threads, 3 failures trip the circuit breaker to prevent hammering the degraded dependency, and the cached fallback guarantees graceful degradation without downtime.",
            "pitfalls_tr": [
                {"trap": "Dış API isteklerine asla zaman aşımı (timeout) koymamak.", "solution": "Her dış ağ çağrısına mutlaka 2-5 saniyelik bir `timeout` sınırı koyun."},
                {"trap": "Hata anında uygulamanın beyaz ekran verip çökmesine izin vermek.", "solution": "Kullanıcıya daima dostça bir hata ekranı ve alternatif bir yol (fallback) sunun."},
                {"trap": "Savunmacı programlamayı abartıp her satıra gereksiz 10 kat kontrol eklemek.", "solution": "Savunmayı sistem sınırlarına (API girişleri, dış servis çağrıları) yerleştirin; iç fonksiyonlarda tip güvenliğine güvenin."}
            ],
            "pitfalls_en": [
                {"trap": "Executing network calls without explicit timeouts, leaving sockets hanging indefinitely.", "solution": "Always wrap external network calls in an `AbortSignal.timeout()`."},
                {"trap": "Allowing unexpected errors to manifest as unhandled white-screen crashes.", "solution": "Provide friendly error boundary fallbacks and retry buttons."},
                {"trap": "Over-defensive clutter: validating inputs inside every private internal helper.", "solution": "Enforce strict validation at architectural perimeter boundaries; trust internal typed contracts."}
            ],
            "udemy_title_tr": "Ders 48: Savunmacı Programlama - Circuit Breaker ve Fallback Tasarımı",
            "udemy_title_en": "Lecture 48: Defensive Programming - Circuit Breakers & Fail-Safe Design",
            "udemy_slides_tr": [
                "Murphy Kanunu: Yanlış gidebilecek her şey yanlış gidecektir.",
                "Fail-Safe Tasarım: Çöküş anında güvenli duruma geçmek.",
                "Circuit Breaker (Devre Kesici) durum makinesi: Closed, Open, Half-Open.",
                "Bölüm 8 Özeti: Güvenlik, OWASP ve Savunmacı Kod Hijyeni."
            ],
            "udemy_slides_en": [
                "Murphy's Law in production engineering: Everything will fail eventually.",
                "Fail-safe architecture: Graceful degradation under cascading failures.",
                "The Circuit Breaker pattern: Closed, Open, and Half-Open states.",
                "Module 8 Recap: Security, OWASP Protections & Defensive Code Hygiene."
            ],
            "udemy_demo_tr": "Bir döviz servisi simülasyonu yapın. Dış servisi kasıtlı olarak kapatın. İlk 3 istekte timeout olduğunu, 4. istekte devrenin açılıp 0 milisaniyede fallback değer döndüğünü canlı konsolda gösterin.",
            "udemy_demo_en": "Simulate an external dependency outage. Trigger requests: show the first 3 timeout at 2,000ms. On the 4th request, watch the circuit breaker trip, immediately returning cached fallbacks in 0.5ms.",
            "action_task_tr": "Projenizde harici bir API çağıran fonksiyona 3 saniyelik bir `AbortSignal.timeout` ve servis çöktüğünde çalışacak bir `fallback` değeri ekleyin.",
            "action_task_en": "Wrap an external network call in your project with an explicit 3,000ms `AbortSignal.timeout` and provide a graceful fallback return value.",
            "quiz_tr": [
                {
                    "question": "Yazılım mimarisinde 'Circuit Breaker' (Devre Kesici) deseninin temel amacı nedir?",
                    "options": [
                        "A) Bilgisayara yeni donanım bağlamak",
                        "B) Sürekli hata veren veya çökmüş olan bir dış servise ısrarla istek atıp sistem kaynaklarını tüketmeyi durdurmak ve sistemi güvenli bir bekleme durumuna almak",
                        "C) Sadece CSS dosyalarını birleştirmek",
                        "D) Kullanıcı şifrelerini değiştirmek"
                    ],
                    "answer": "B",
                    "explanation": "Circuit Breaker, çöken bir servise yapılan çağrıları geçici olarak keserek hem o servisin toparlanmasına fırsat tanır hem de ana sistemin kilitlenmesini önler."
                },
                {
                    "question": "Savunmacı Programlama (Defensive Programming) felsefesine göre bir yazılımcının varsayımı ne olmalıdır?",
                    "options": [
                        "A) Kullanıcıların her zaman doğru veri gireceği ve internetin asla kopmayacağı",
                        "B) Dış girdilerin bozuk olabileceği, ağın her an kopabileceği ve bağımlılıkların çökebileceği; sistemin bu durumlara hazırlıklı olması gerektiği",
                        "C) Kodun sadece cuma günleri test edilmesi gerektiği",
                        "D) Sadece tek bir tarayıcıyı desteklemek gerektiği"
                    ],
                    "answer": "B",
                    "explanation": "Savunmacı programlama 'İyimser Kodlama'nın zıddıdır; her türlü felaket senaryosunu baştan hesaba katarak sistemi dayanıklı (resilient) kılar."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the primary operational objective of the Circuit Breaker architectural pattern?",
                    "options": [
                        "A) Attaching external USB peripheral hardware",
                        "B) Halting calls to failing external services to prevent cascading resource exhaustion and allow degraded systems time to recover",
                        "C) Concatenating CSS style bundles",
                        "D) Forcing user credential rotations"
                    ],
                    "answer": "B",
                    "explanation": "Circuit breakers short-circuit outbound calls to failing systems, returning fallbacks instantly while preventing thread starvation."
                },
                {
                    "question": "Under the philosophy of Defensive Programming, what baseline assumption must guide architecture?",
                    "options": [
                        "A) Client inputs are well-formed and network connections are infallible",
                        "B) Ingress data will be malformed, networks will fail, and external APIs will crash; systems must be engineered with safe fallbacks",
                        "C) Systems require testing only on Fridays",
                        "D) Applications should support exactly one browser"
                    ],
                    "answer": "B",
                    "explanation": "Defensive programming abandons sunny-day optimism, designing systems to fail safely, contain damage, and degrade gracefully."
                }
            ]
        }
    ]
