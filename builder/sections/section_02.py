"""
Section 2: Algoritmik Düşünme & Kod Temelleri (Chapters 7 to 12)
"""

def get_section_chapters():
    return [
        # Chapter 7
        {
            "id": 7,
            "section_id": 2,
            "slug_tr": "ch07_sozde_koddan_gercek_koda_algoritma_tasarimi",
            "slug_en": "ch07_from_pseudocode_to_architecture_ai_algorithm",
            "title_tr": "Sözde Koddan (Pseudocode) Gerçek Koda: AI ile Algoritma Tasarlamak",
            "title_en": "From Pseudocode to Architecture: Designing Algorithms with AI",
            "subtitle_tr": "Klavye Başına Geçmeden Önce Düşünceyi Yapılandırma Rehberi",
            "subtitle_en": "Structuring Intent and Algorithmic Logic Before Typing Code",
            "level_tr": "Temel / Orta Seviye",
            "level_en": "Foundational / Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Yapay zekaya doğrudan kod yazdırmak yerine neden önce adım adım sözde kod (pseudocode) tartıştırmalıyız?",
            "podcast_hook_en": "Why does forcing an AI model to draft pseudocode first yield dramatically higher architectural resilience than jumping straight to implementation?",
            "takeaways_tr": [
                "Sözde kod (Pseudocode), insan zihni ile yapay zekanın akıl yürütme motoru arasındaki ortak dildir.",
                "Doğrudan kod istemek modelin aceleci varsayımlar yapmasına; sözde kod ise mantık adımlarını önceden planlamasına yol açar.",
                "İyi bir sözde kod dile bağımsızdır; Python, Go veya Rust'a eşit kolaylıkla derlenebilir."
            ],
            "takeaways_en": [
                "Pseudocode is the universal lingua franca connecting human engineering intent with LLM reasoning.",
                "Direct code generation encourages models to make hasty assumptions; pseudocode forces methodical architectural decomposition.",
                "Robust pseudocode is language-agnostic, effortlessly translatable into Python, Go, or Rust."
            ],
            "story_tr": """Bir inşaat şantiyesine gittiğinizi düşünün. Şef mühendis ustaların yanına gelip: *"Hadi hemen tuğlaları üst üste koymaya başlayın, bina yükselsin!"* der mi? Tabii ki hayır! Önce mavi ozalit planlar (blueprints) incelenir, kolonların taşıma kapasitesi hesaplanır.

Kodlama dünyasında sözde kod (pseudocode), o mavi ozalit plandır. 

Junior yazılımcıların en büyük hatası, problemi tam anlamadan yapay zekaya *"Hemen bana kod yaz"* demektir. Oysa önce mantık akışını sözde kodla kurduğunuzda, yapay zeka hem mantık hatalarını hemen fark eder hem de yazdığı kod ilk seferde çalışır.""",
            "story_en": """Visit a commercial construction site. Does the structural engineer shout: *"Start stacking cinder blocks right now and let's see how high it goes!"* Of course not. They review structural blueprints, verify load-bearing vectors, and plan electrical conduits first.

In software engineering, pseudocode serves as that architectural blueprint.

The most pervasive junior trap is prompting *"Generate the code immediately"* before framing the algorithmic invariants. When you collaborate via pseudocode first, the LLM uncovers logical contradictions and generates production-ready code on the first attempt.""",
            "mental_tr": """Sözde Kod ile Düşünme Döngüsü:

```
[Problem Tanımı] 
      │
      ▼
[Sözde Kod (Pseudocode) Taslağı] ──> "Adım 1: Girdiyi doğrula, Adım 2: Set kullanarak tekilleştir"
      │
      ▼
[AI İle Mantık & Karmaşıklık Denetimi] ──> "Burada O(N^2) var, hash map kullanalım mı?"
      │
      ▼
[Temiz Kod Üretimi & Testler]
```""",
            "mental_en": """The Pseudocode Iteration Loop:

```
[Problem Statement]
      │
      ▼
[Pseudocode Decomposition] ──> "Step 1: Validate payload, Step 2: Deduplicate via Hash Set"
      │
      ▼
[AI Complexity Audit] ──> "This nested lookup is O(N^2); can we use a hash map?"
      │
      ▼
[Code Generation & Unit Tests]
```""",
            "prompt_tr": """# ROL: Algoritma Uzmanı
Bir kullanıcı listesindeki mükerrer (duplicate) e-posta adreslerini temizleyip en son kayıt olanı saklayan bir sistem tasarlayacağız.

Lütfen hemen Python veya JavaScript kodu YAZMA.
Bunun yerine:
1. Problemin adım adım SÖZDE KODUNU (pseudocode) çıkar.
2. Zaman karmaşıklığını (Time Complexity) hesapla.
3. Bellek kullanımını minimize etmek için alternatif bir yaklaşım var mı tartış.""",
            "prompt_en": """# ROLE: Algorithm Design Specialist
We must deduplicate user records sharing the same email, keeping only the most recently registered entry.

Do NOT output implementation code yet.
Instead:
1. Provide step-by-step PSEUDOCODE.
2. Analyze the Big-O Time and Space complexity.
3. Suggest an alternative if memory consumption is constrained.""",
            "code_lang": "python",
            "code_naive": """# Kötü: İç içe döngülerle O(n^2) çalışan kontrolsüz arama
def deduplicate_users(users):
    unique = []
    for u in users:
        # Her eleman için listeyi baştan sona tarar: 100,000 kullanıcıda sistem kilitlenir!
        found = False
        for ex in unique:
            if ex['email'] == u['email']:
                found = True
                break
        if not found:
            unique.append(u)
    return unique""",
            "code_robust": """# Sözde Koddan Üretilmiş O(n) Performanslı Versiyon
from typing import List, Dict, Any

def deduplicate_users_latest(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    \"\"\"
    Kullanıcıları e-posta adresine göre tekilleştirir.
    En güncel 'created_at' damgasına sahip olan kaydı O(N) zaman karmaşıklığında saklar.
    \"\"\"
    latest_by_email: Dict[str, Dict[str, Any]] = {}

    for user in users:
        email = user.get("email", "").strip().lower()
        if not email:
            continue  # Geçersiz e-postaları atla

        existing = latest_by_email.get(email)
        if existing is None or user.get("created_at", 0) > existing.get("created_at", 0):
            latest_by_email[email] = user

    return list(latest_by_email.values())""",
            "code_notes_tr": "Sözde kod aşamasında hash map (sözlük) kullanmaya karar verildiği için arama süresi O(N^2)'den O(N)'e düşürülmüştür. Ayrıca e-posta normalizasyonu (lowercase) ve boş değer koruması eklenmiştir.",
            "code_notes_en": "Formulating pseudocode first guided the architecture toward an O(N) hash map rather than a catastrophic nested loop O(N^2). Email normalization and null handling were systematically accounted for.",
            "pitfalls_tr": [
                {"trap": "AI'a 'bunu çöz' deyip çıkan karmaşık kodu anlamadan kabul etmek.", "solution": "Her zaman önce algoritmanın Türkçe/İngilizce adımlarını yazdırın."},
                {"trap": "Büyük veri setlerinde nested loop (iç içe döngü) tuzaklarına düşmek.", "solution": "Veri yapısı olarak liste yerine Hash Map (Dict/Set) tercih edin."},
                {"trap": "E-posta veya kullanıcı adı karşılaştırmalarında 'case-sensitivity'yi unutmak.", "solution": "String verileri her zaman `.strip().lower()` ile normalize edin."}
            ],
            "pitfalls_en": [
                {"trap": "Accepting convoluted code without understanding the underlying logic.", "solution": "Demand step-by-step plain-English pseudocode before viewing code."},
                {"trap": "Falling into O(N^2) nested loop traps on large datasets.", "solution": "Leverage Hash Sets and Maps for amortized O(1) lookups."},
                {"trap": "Overlooking case sensitivity during string comparisons.", "solution": "Always normalize string keys using lowercase and whitespace trimming."}
            ],
            "udemy_title_tr": "Ders 7: Sözde Kod ile Düşünmek - AI ile Algoritma Tasarımı",
            "udemy_title_en": "Lecture 7: Thinking in Pseudocode - Algorithm Design with AI",
            "udemy_slides_tr": [
                "Neden doğrudan kod yazmak en büyük junior hatasıdır?",
                "Sözde kod (Pseudocode) nedir ve nasıl yapılandırılır?",
                "O(N^2) felaketinden O(N) zarafetine geçiş.",
                "Canlı demo: E-ticaret sepet hesaplama algoritmasını sözde kodla tasarlamak."
            ],
            "udemy_slides_en": [
                "Why writing syntax immediately is the primary junior engineering trap.",
                "What is pseudocode and how does it anchor LLM reasoning?",
                "Refactoring away from O(N^2) nested loops into O(N) hash lookups.",
                "Live demo: Designing a discount pipeline using pseudocode first."
            ],
            "udemy_demo_tr": "Terminal veya chat ekranında bir LeetCode orta seviye problem verin. 'Kod yazma, sadece 4 maddelik sözde kod çıkar' deyin. Çıkan sözde kodu adım adım onaylayıp ardından tek seferde temiz fonksiyonu ürettirin.",
            "udemy_demo_en": "Submit a medium algorithmic problem to an LLM. Constrain it: 'Do not write syntax; provide a 4-step pseudocode blueprint'. Review the logic, approve it, then trigger code generation.",
            "action_task_tr": "Bir sonraki geliştireceğiniz fonksiyonda tek satır kod yazmadan önce defterinize veya not uygulamanıza 5 maddelik sözde kod yazın.",
            "action_task_en": "Draft a 5-bullet pseudocode outline for a pending task before opening your code editor.",
            "quiz_tr": [
                {
                    "question": "Algoritma tasarımında sözde kod (pseudocode) kullanmanın en kritik faydası nedir?",
                    "options": [
                        "A) Kodun derlenme süresini sıfıra indirmesi",
                        "B) Dil söz dizimi karmaşasına girmeden saf iş mantığını ve sınır durumlarını doğrulamaya imkan tanıması",
                        "C) Sadece Python dilinde çalışması",
                        "D) Veritabanı lisans maliyetlerini düşürmesi"
                    ],
                    "answer": "B",
                    "explanation": "Sözde kod, geliştiricinin ve yapay zekanın söz dizimi (syntax) yerine mantık akışına ve karmaşıklığa odaklanmasını sağlar."
                },
                {
                    "question": "100.000 kullanıcılı bir listede tekilleştirme yaparken iç içe iki döngü kullanmanın tehlikesi nedir?",
                    "options": [
                        "A) Hiçbir tehlikesi yoktur, en modern yöntemdir",
                        "B) O(N^2) zaman karmaşıklığı sebebiyle 10 milyar işlem gerektirip sunucuyu kilitlemesi",
                        "C) Sadece CSS hatalarına yol açması",
                        "D) Değişken isimlerinin silinmesi"
                    ],
                    "answer": "B",
                    "explanation": "100.000 eleman için N^2 işlem 10.000.000.000 adıma tekabül eder ve işlemciyi dakikalarca dondurur. O(N) hash map yaklaşımı ise milisaniyeler sürer."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the primary architectural value of formulating pseudocode before implementation?",
                    "options": [
                        "A) Reducing compiler execution overhead to zero",
                        "B) Isolating business logic and algorithmic correctness from language-specific syntax quirks",
                        "C) It only functions in Python",
                        "D) Slashing database cloud licensing costs"
                    ],
                    "answer": "B",
                    "explanation": "Pseudocode frees cognitive bandwidth to analyze algorithmic invariants and edge cases without syntax friction."
                },
                {
                    "question": "What is the operational danger of an O(N^2) nested loop when processing 100,000 records?",
                    "options": [
                        "A) None; modern CPUs process it in nanoseconds",
                        "B) It yields 10 billion operations, starving CPU resources and freezing the service",
                        "C) It exclusively triggers CSS rendering glitches",
                        "D) It resets variable identifiers"
                    ],
                    "answer": "B",
                    "explanation": "An O(N^2) algorithm on 100k items requires ~10 billion operations, creating severe denial-of-service latency spikes."
                }
            ]
        },

        # Chapter 8
        {
            "id": 8,
            "section_id": 2,
            "slug_tr": "ch08_veri_yapilari_neden_hala_hayati",
            "slug_en": "ch08_why_data_structures_matter_in_ai_era",
            "title_tr": "Veri Yapıları AI Çağında Neden Hâlâ Hayati?",
            "title_en": "Data Structures: Why AI Can't Save You from Bad Memory Models",
            "subtitle_tr": "Array, Hash Map, Set ve Tree Arasındaki Seçim Sisteminizi Nasıl Kurtarır?",
            "subtitle_en": "How Array, Hash Map, Set, and Tree Selections Save Production Systems",
            "level_tr": "Temel / Orta Seviye",
            "level_en": "Foundational / Intermediate",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Yapay zeka her şeyi optimize edebiliyorsa, bir yazılımcının Array ile Set arasındaki bellek farkını bilmesine neden hâlâ gerek var?",
            "podcast_hook_en": "If AI models optimize implementations automatically, why does an engineer still need deep mental models of Array vs. Hash Set memory layouts?",
            "takeaways_tr": [
                "Yapay zeka varsayılan olarak en kolayına gelen veri yapısını (çoğunlukla Array) seçme eğilimindedir.",
                "Yanlış veri yapısı seçildiğinde, dünyanın en gelişmiş AI modeli bile o kodu verimli hale getiremez.",
                "Arama için Set/Map, sıralı erişim için Array, hiyerarşik ilişkiler için Tree kullanmak mimari bir karardır."
            ],
            "takeaways_en": [
                "LLMs default to the path of least resistance (often flat arrays and lists) unless instructed otherwise.",
                "No amount of AI optimization can salvage a system crippled by an inappropriate underlying data structure.",
                "Selecting Sets for O(1) membership, Arrays for sequential index access, and Trees for hierarchy is an architectural mandate."
            ],
            "story_tr": """Evinizde 10.000 adet kitap olduğunu düşünün. 

Bu kitapları odanın ortasına rastgele devasa bir dağ gibi yığarsanız ne olur? Belli bir kitabı bulmak için tek tek 10.000 kitabı elden geçirmeniz gerekir. İşte bu **Dizi (Array)** üzerindeki doğrusal aramadır (O(N)).

Peki bu kitapları harf sırasına göre dizilmiş kütüphane raflarına yerleştirirseniz? İstediğiniz kitaba 10 saniyede ulaşırsınız! İşte bu **Hash Map / Ağaç (Tree)** veri yapısıdır.

Yapay zeka size kitapları taşımada yardım eden hızlı bir işçidir. Ama kitapları odaya yığacak mısınız yoksa raflara mı dizeceksiniz? Bu kararı sadece siz verebilirsiniz.""",
            "story_en": """Imagine owning 10,000 physical books.

If you dump them into a mountain in the center of your living room, finding a specific novel forces you to sift through all 10,000 books one by one. That is linear search over an **Array (O(N))**.

Now, place them into labeled alphabetical bookcases. You can retrieve any title within 10 seconds. That is an indexed **Hash Map / Binary Tree** layout.

AI is an indefatigable assistant carrying boxes of books. But whether those books end up in an unorganized pile or a structured index is entirely your architectural decision.""",
            "mental_tr": """Hangi Veri Yapısı Ne Zaman Seçilmeli?

| Veri Yapısı | Arama Hızı | Ekleme/Silme | En İyi Senaryo | Dikkat |
| :--- | :--- | :--- | :--- | :--- |
| **Array / List** | O(N) | Sona ekleme O(1), Araya ekleme O(N) | Sıralı listeleme, indeksle doğrudan erişim | Büyük listelerde `includes()` veya `in` yapmak performansı öldürür |
| **Set** | O(1) | O(1) | Benzersizlik kontrolü, "Bu kullanıcı listede var mı?" | Sıralama garantisi yoktur |
| **Hash Map / Dict**| O(1) | O(1) | Anahtar-değer eşlemeleri, önbellek (cache), indeksleme | Bellek tüketimi diziye göre biraz daha fazladır |
| **Tree / Graph** | O(log N) | O(log N) | Hiyerarşik veri (kategori ağacı, organizasyon şeması) | Düğümleri yönetmek ve dengelemek uzmanlık ister |""",
            "mental_en": """Data Structure Trade-off Matrix:

| Structure | Lookup Speed | Insert / Delete | Ideal Use Case | Operational Risk |
| :--- | :--- | :--- | :--- | :--- |
| **Array / List** | O(N) | Append O(1), Shift O(N) | Sequential display, index access | Running `.includes()` over large arrays cripples throughput |
| **Set** | O(1) | O(1) | Membership checks ("Has user visited?") | No inherent sorting order |
| **Hash Map / Dict**| O(1) | O(1) | Key-value indexing, caching, lookups | Higher memory footprint due to bucket overhead |
| **Tree / Graph** | O(log N) | O(log N) | Hierarchical data (categories, org charts) | Traversal complexity and tree balancing |""",
            "prompt_tr": """# ROL: Kıdemli Veri Yapıları Uzmanı
# GÖREV: 500.000 aktif oturum ID'si (Session Token) içeren bir listede gelen isteklerin geçerli olup olmadığını kontrol edeceğiz.

Lütfen bana bir veri yapısı önerisi ve karşılaştırması sun:
1. Python'da `list` kullanmak ile `set` kullanmak arasındaki bellek ve zaman farkı nedir?
2. 500.000 eleman için sorgu süresi karşılaştırması (Benchmark) senaryosu açıkla.
3. Kodu en optimize veri yapısıyla yaz.""",
            "prompt_en": """# ROLE: Data Structures & Systems Specialist
# OBJECTIVE: Validate incoming session tokens against a collection of 500,000 active tokens.

Provide a data structure trade-off breakdown:
1. Compare memory footprint and lookup latency for Array/List vs. Hash Set.
2. Outline a micro-benchmark scenario for 500,000 elements.
3. Deliver the most performant, memory-conscious implementation.""",
            "code_lang": "typescript",
            "code_naive": """// Kötü Veri Yapısı: Dizi (Array) üzerinde O(n) arama yapmak
export class NaiveSessionManager {
  private activeTokens: string[] = [];

  addToken(token: string) {
    this.activeTokens.push(token);
  }

  // 100.000 aktif kullanıcıda her istekte tüm diziyi gezer: Felaket!
  isValid(token: string): boolean {
    return this.activeTokens.includes(token);
  }
}""",
            "code_robust": """// Doğru Veri Yapısı: O(1) Set ile Anında Üyelik Kontrolü
export class OptimizedSessionManager {
  private activeTokens: Set<string> = new Set();

  addToken(token: string): void {
    this.activeTokens.add(token);
  }

  removeToken(token: string): boolean {
    return this.activeTokens.delete(token);
  }

  // 1.000.000 eleman olsa bile mikrosaniye düzeyinde O(1) yanıt
  isValid(token: string): boolean {
    return this.activeTokens.has(token);
  }

  get count(): number {
    return this.activeTokens.size;
  }
}""",
            "code_notes_tr": "Array üzerindeki `.includes()` araması O(N) iken, Set üzerindeki `.has()` kontrolü O(1) zaman karmaşıklığındadır. 100.000 öğede bu fark 50 milisaniyeden 0.001 milisaniyeye (50.000 kat) hızlanma anlamına gelir.",
            "code_notes_en": "Array `.includes()` requires an O(N) scan across memory blocks, whereas Set `.has()` evaluates hash buckets in O(1) time—delivering up to a 50,000x speedup under load.",
            "pitfalls_tr": [
                {"trap": "Sadece varlık kontrolü (membership check) yaparken Array kullanmak.", "solution": "Elemanın varlığını sorguluyorsanız her zaman Set veya Map tercih edin."},
                {"trap": "Hash Map anahtarlarında çok büyük ve karmaşık objeler kullanıp hash çarpışması yaratmak.", "solution": "Anahtar olarak her zaman benzersiz string veya ID kullanın."},
                {"trap": "AI'a 'bunu hızlı yap' deyip arka plandaki veri yapısını incelememek.", "solution": "AI'ın seçtiği veri tipinin zaman ve alan karmaşıklığını (Big-O) mutlaka sorgulayın."}
            ],
            "pitfalls_en": [
                {"trap": "Using arrays for frequent membership lookups (`arr.includes(id)`).", "solution": "Convert arrays to Sets when membership checks dominate read paths."},
                {"trap": "Using massive complex objects as map keys, inducing hash collisions.", "solution": "Use normalized primitive string IDs as lookup keys."},
                {"trap": "Asking AI to 'make this faster' without interrogating data structure choices.", "solution": "Explicitly query the Big-O trade-offs of proposed collections."}
            ],
            "udemy_title_tr": "Ders 8: Veri Yapıları Ustalığı - Doğru Koleksiyonu Seçmek",
            "udemy_title_en": "Lecture 8: Mastering Data Structures - Choosing the Optimal Collection",
            "udemy_slides_tr": [
                "Neden AI bile kötü bir veri yapısı seçimini kurtaramaz?",
                "Array vs Set vs Map: 50.000 katlık performans farkı.",
                "Bellek tüketimi vs Arama hızı dengesi.",
                "Canlı Benchmark: 100.000 kayıt üzerinde List ve Set hız testi."
            ],
            "udemy_slides_en": [
                "Why no compiler or LLM can rescue an inefficient data model.",
                "Array vs Set vs Map: Benchmarking the 50,000x difference.",
                "Memory overhead vs. lookup speed trade-offs.",
                "Live benchmark: Measuring latency across 100,000 records."
            ],
            "udemy_demo_tr": "Node.js veya Python'da bir micro-benchmark scripti yazın. 100.000 elemanlı bir listede `in` / `.includes()` aramasının kaç ms sürdüğünü, Set ile `.has()` aramasının kaç ms sürdüğünü canlı konsolda gösterin.",
            "udemy_demo_en": "Execute a live micro-benchmark script comparing Array search vs. Set membership on 100,000 items, demonstrating real-time CPU time differences.",
            "action_task_tr": "Mevcut kod tabanınızda bir döngü içinde `.includes()` veya `in` kontrolü yapılan en az bir yer bulun ve bunu `Set` kullanarak O(1)'e refactor edin.",
            "action_task_en": "Locate an instance of `.includes()` inside a loop in your codebase and refactor it into an O(1) Set lookup.",
            "quiz_tr": [
                {
                    "question": "100.000 elemanlı bir koleksiyonda bir elemanın var olup olmadığını en hızlı şekilde kontrol etmek için hangi veri yapısı kullanılmalıdır?",
                    "options": [
                        "A) Dizi (Array / List)",
                        "B) Hash Set",
                        "C) Bağlı Liste (Linked List)",
                        "D) Yığıt (Stack)"
                    ],
                    "answer": "B",
                    "explanation": "Hash Set, verinin hash koduna göre O(1) sabit zamanda doğrudan konumuna erişir; tüm elemanları gezmek zorunda kalmaz."
                },
                {
                    "question": "Array yerine Hash Map kullanmanın potansiyel tek dezavantajı nedir?",
                    "options": [
                        "A) Asla çalışmaması",
                        "B) Hash tablolarının ve kova (bucket) yapısının bellekte biraz daha fazla yer kaplaması",
                        "C) Sadece Python'da geçerli olması",
                        "D) Kodun okunmasını imkansız kılması"
                    ],
                    "answer": "B",
                    "explanation": "Hash Map'ler hızlı erişim sağlamak için bellekten bir miktar ödün verir (Time-Space Tradeoff)."
                }
            ],
            "quiz_en": [
                {
                    "question": "Which data structure provides the fastest membership lookup across 100,000 items?",
                    "options": [
                        "A) Array / List",
                        "B) Hash Set",
                        "C) Linked List",
                        "D) Stack"
                    ],
                    "answer": "B",
                    "explanation": "Hash Sets compute bucket indices via hashing, achieving O(1) lookup time regardless of dataset size."
                },
                {
                    "question": "What is the primary operational trade-off of choosing a Hash Map over a flat contiguous Array?",
                    "options": [
                        "A) Complete lack of execution support",
                        "B) Additional memory overhead consumed by hash tables and pointer metadata",
                        "C) Restriction to dynamic languages",
                        "D) Elimination of type checking"
                    ],
                    "answer": "B",
                    "explanation": "Hash Maps trade spatial overhead (hash tables, buckets) for temporal speed (O(1) lookups)."
                }
            ]
        },

        # Chapter 9
        {
            "id": 9,
            "section_id": 2,
            "slug_tr": "ch09_big_o_karmasikligi_ve_ai_kod_performansi",
            "slug_en": "ch09_big_o_complexity_ai_code_benchmarking",
            "title_tr": "Zaman ve Bellek Karmaşıklığı (Big O): AI Üretti, Ama Verimli mi?",
            "title_en": "Big-O Complexity & AI Code Benchmarking: It Works, But Does It Scale?",
            "subtitle_tr": "5 Elemanla Test Edilen Kodun Canlıda 5 Milyon Elemanda Çökmesini Önlemek",
            "subtitle_en": "Preventing Code Tested on 5 Items from Crashing Under 5 Million Real Users",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "AI modelleri lokal bilgisayarınızda anında çalışan kodlar üretir. Peki o kod canlı ortamda 1 milyon kullanıcıya ulaştığında neden sunucuları eritir?",
            "podcast_hook_en": "Why does AI-generated code run flawlessly on a laptop with 10 dummy records, yet completely melt production clusters under high throughput?",
            "takeaways_tr": [
                "Lokal ortamda çalışan her kod ölçeklenebilir değildir; Big-O analizi olmadan canlıya çıkmak kumardır.",
                "AI modelleri genellikle en az kod satırı gerektiren çözümleri üretir; bu çözümler ise çoğunlukla O(N^2) veya O(2^N) gizli tuzaklar taşır.",
                "İyi bir mühendis, AI çıktısına bakar bakmaz döngü derinliğini ve bellek tahsisini (allocation) zihninde hesaplayabilmelidir."
            ],
            "takeaways_en": [
                "Code that executes locally is not inherently scalable; deploying without Big-O profiling is reckless.",
                "LLMs prioritize concise code, which frequently conceals devastating O(N^2) or recursive complexity.",
                "A seasoned engineer instinctively audits loop nesting depths and memory allocations upon viewing any AI snippet."
            ],
            "story_tr": """Bir kargo dağıtım şirketinde çalıştığınızı düşünün. 

Eğer şehrinizde sadece 3 ev varsa, kargo görevlisi evlerin sırasını rastgele dolaşarak paketleri 15 dakikada dağıtabilir. Ancak şehirde 50.000 ev olduğunda, rotayı akıllıca planlamazsanız kargo görevlisi aynı sokaktan yüzlerce kez geçer ve teslimat aylar sürer!

Big-O notasyonu işte bu kargo rotasının matematiksel ifadesidir:
- Girdi 10 katına çıktığında harcanan süre 10 katına mı çıkıyor (O(N))?
- Yoksa 100 katına mı fırlıyor (O(N^2))?
- Yoksa sabit mi kalıyor (O(1))?

Yapay zeka genellikle 3 evlik senaryolar için kod yazar. 50.000 evi hesaba katmak sizin işinizdir.""",
            "story_en": """Picture running a local courier delivery service.

When your town has only 3 addresses, a driver can visit them in random order and finish within 15 minutes. But when your city grows to 50,000 households, wandering without route optimization requires decades to complete deliveries.

Big-O notation is the formal description of how your system scales:
- If input increases 10x, does execution time increase 10x (O(N))?
- Does it explode by 100x (O(N^2))?
- Or does it remain unchanged (O(1))?

AI naturally writes code suitable for 3 houses. Engineering for 50,000 addresses is your responsibility.""",
            "mental_tr": """Big-O Skalası: Cennetten Cehenneme

```
O(1)      ──> [MÜKEMMEL] Sabit Zaman (Hash Map erişimi)
O(log N)  ──> [HARİKA] İkili Arama (Binary Search)
O(N)      ──> [İYİ / KABUL EDİLEBİLİR] Tekil döngü ile geçiş
O(N log N)──> [ORTALAMA] Hızlı Sıralama (Merge Sort / Timsort)
────────────────────────────────────────────────────────────────
O(N^2)    ──> [TEHLİKELİ] İç içe iki döngü (Nested Loops)
O(2^N)    ──> [FELAKET] Üstel artış, sistemi eritir
```""",
            "mental_en": """The Big-O Scale: From Ideal to Catastrophic

```
O(1)      ──> [EXCELLENT] Constant Time (Hash Map lookup)
O(log N)  ──> [GREAT] Logarithmic Time (Binary Search)
O(N)      ──> [ACCEPTABLE] Linear Scan (Single loop)
O(N log N)──> [FAIR] Efficient Sorting (MergeSort / QuickSort)
────────────────────────────────────────────────────────────────
O(N^2)    ──> [DANGEROUS] Quadratic (Nested loops)
O(2^N)    ──> [DISASTER] Exponential explosion
```""",
            "prompt_tr": """# ROL: Yüksek Performanslı Sistem Mühendisi
Aşağıdaki Python fonksiyonunu analiz et.

## GÖREV:
1. Zaman (Time) ve Alan (Space) Big-O karmaşıklığını tam olarak hesapla.
2. Bu fonksiyon 100.000 elemanlı bir listede çalıştırılırsa ne olur?
3. Fonksiyonu O(N) veya O(N log N) seviyesine çekecek optimize alternatifi üret.

## KOD:
```python
def find_pairs(arr, target_sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
    return pairs
```""",
            "prompt_en": """# ROLE: High-Performance Systems Engineer
Analyze the following function:

## TASK:
1. Formulate the precise Big-O Time and Space complexity.
2. Characterize system behavior when processing 100,000 items.
3. Refactor the algorithm to achieve optimal O(N) time complexity.

## SNIPPET:
```python
def find_pairs(arr, target_sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
    return pairs
```""",
            "code_lang": "python",
            "code_naive": """# AI'ın Ürettiği Naive Kod: O(N^2) Zaman Karmaşıklığı
def find_pairs_quadratic(arr: list[int], target: int) -> list[tuple[int, int]]:
    pairs = []
    # İç içe iki döngü: N=100,000 olduğunda 5 milyar karşılaştırma!
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs""",
            "code_robust": """# Optimize Edilmiş Versiyon: O(N) Zaman ve O(N) Alan Karmaşıklığı
def find_pairs_linear(arr: list[int], target: int) -> list[tuple[int, int]]:
    seen = set()
    pairs = set()

    # Tek geçiş (Single Pass): N=100,000 olduğunda sadece 100,000 işlem
    for num in arr:
        complement = target - num
        if complement in seen:
            # Sıralı tuple ekleyerek tekrarları önleriz
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)

    return list(pairs)""",
            "code_notes_tr": "Hash Set kullanımı sayesinde tamamlayıcı sayı (complement = target - num) O(1) sürede bulunur. İç içe döngü kaldırılarak algoritma O(N^2)'den O(N)'e çekilmiştir. 100.000 elemanda işlem süresi 15 dakikadan 0.05 saniyeye düşer.",
            "code_notes_en": "By leveraging a Hash Set to store previously seen numbers, we check for complements in O(1) time. This collapses execution complexity from O(N^2) to O(N), shrinking latency from minutes to milliseconds.",
            "pitfalls_tr": [
                {"trap": "Küçük mock verilerle (3-5 eleman) test yapıp performansın harika olduğunu sanmak.", "solution": "Test senaryolarınıza en az 50.000 rastgele kayıt üreten yük testleri ekleyin."},
                {"trap": "Döngü içinde farkında olmadan gizli O(N) işlemleri çalıştırmak (Örn: Array.splice veya List.pop(0)).", "solution": "Listenin başından eleman silmenin O(N) olduğunu unutmayın; deque kullanın."},
                {"trap": "Premature Optimization (Erken optimizasyon) yaparak kodu okunaksız hale getirmek.", "solution": "Önce temiz ve doğru çalışan kodu yazın; profil çıkarıp darboğazı ölçtükten sonra optimize edin."}
            ],
            "pitfalls_en": [
                {"trap": "Benchmarking exclusively against small dummy arrays of 5 elements.", "solution": "Generate synthetic payloads of 50,000+ items to profile real degradation curves."},
                {"trap": "Unknowingly executing hidden O(N) methods inside loops (e.g., `list.pop(0)` or `array.shift()`).", "solution": "Recognize that shifting contiguous arrays is O(N); utilize double-ended queues (`deque`)."},
                {"trap": "Engaging in premature optimization at the expense of readability.", "solution": "Establish correctness and clean abstractions first, profile bottlenecks, and optimize empirically."}
            ],
            "udemy_title_tr": "Ders 9: Big-O Analizi - AI Kodunun Performansını Ölçmek",
            "udemy_title_en": "Lecture 9: Big-O Mastery - Benchmarking AI Code at Scale",
            "udemy_slides_tr": [
                "Lokalde çalışan kod neden prod ortamında çöker?",
                "Big-O karmaşıklığını 30 saniyede gözle tespit etme formülü.",
                "O(N^2) vs O(N) Two-Sum algoritması vaka analizi.",
                "Python cProfile ve Node.js console.time ile darboğaz tespiti."
            ],
            "udemy_slides_en": [
                "Why laptop performance is a misleading proxy for cloud production.",
                "Eyeballing Big-O complexity in 30 seconds.",
                "Case study: Refactoring quadratic lookups into linear hash sets.",
                "Profiling bottlenecks using Python cProfile and Node performance APIs."
            ],
            "udemy_demo_tr": "Python'da `time` modülünü kullanarak 100.000 rastgele sayı üretin. `find_pairs_quadratic` fonksiyonunun süresini ölçün (birkaç saniye sonra manuel durdurun). Ardından `find_pairs_linear` fonksiyonunu çalıştırıp 0.04 saniyede bittiğini gösterin.",
            "udemy_demo_en": "Write a timing harness generating 100,000 integers. Run the quadratic version and watch CPU thread peg at 100%. Then run the linear hash version and watch it return in 40 milliseconds.",
            "action_task_tr": "Projenizdeki bir döngüyü inceleyin. İçinde başka bir döngü veya `.find()` / `.indexOf()` var mı kontrol edin. Eğer varsa bunu bir Map veya Set ile O(N)'e dönüştürün.",
            "action_task_en": "Inspect an existing loop in your project. Check if it invokes `.find()` or `.indexOf()`. Refactor the lookup into an O(1) Map or Set.",
            "quiz_tr": [
                {
                    "question": "İç içe iki adet `for` döngüsünün aynı dizi (N elemanlı) üzerinde koştuğu bir algoritmanın zaman karmaşıklığı nedir?",
                    "options": [
                        "A) O(1)",
                        "B) O(N)",
                        "C) O(N^2)",
                        "D) O(log N)"
                    ],
                    "answer": "C",
                    "explanation": "Her eleman için diğer tüm elemanlar taranıyorsa N * N = N^2 işlem yapılır; bu da O(N^2) kuadratik karmaşıklıktır."
                },
                {
                    "question": "Bir Python listesinin en başından eleman silmek (`list.pop(0)`) neden O(N) karmaşıklıktadır?",
                    "options": [
                        "A) Python yavaş bir dil olduğu için",
                        "B) İlk eleman silindiğinde geriye kalan tüm elemanların bellekte bir sola kaydırılması gerektiği için",
                        "C) Sadece sayılarda geçerli olduğu için",
                        "D) Yanlış bilgi, O(1)'dir"
                    ],
                    "answer": "B",
                    "explanation": "Diziler bellekte bitişik bloklar halindedir. Baştan eleman silindiğinde arkadaki tüm elemanlar boşluğu doldurmak için bir adım ötelenir."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the time complexity of two nested loops iterating over the same collection of N items?",
                    "options": [
                        "A) O(1)",
                        "B) O(N)",
                        "C) O(N^2)",
                        "D) O(log N)"
                    ],
                    "answer": "C",
                    "explanation": "Iterating across N elements inside an outer loop of N elements yields N * N operations, resulting in O(N^2) quadratic time."
                },
                {
                    "question": "Why does removing the first element of a dynamic array (`arr.shift()` or `list.pop(0)`) incur O(N) cost?",
                    "options": [
                        "A) Dynamic languages lack optimization",
                        "B) Every subsequent element in contiguous memory must be shifted left by one index",
                        "C) It only applies to floating-point numbers",
                        "D) It is actually O(1)"
                    ],
                    "answer": "B",
                    "explanation": "Contiguous array storage requires shifting all remaining elements to fill the vacant index, touching N items."
                }
            ]
        },

        # Chapter 10
        {
            "id": 10,
            "section_id": 2,
            "slug_tr": "ch10_tip_sistemleri_ve_clean_code",
            "slug_en": "ch10_type_systems_and_clean_code",
            "title_tr": "Tip Sistemleri ve Clean Code: AI Çıktısını Type-Safe Kılmak",
            "title_en": "Type Systems & Clean Code: Making AI Output Bulletproof and Type-Safe",
            "subtitle_tr": "'Any' Kullanımını Yasaklayarak Çalışma Zamanı Hatalarını Derleme Zamanında Yakalamak",
            "subtitle_en": "Banning 'any' and Converting Runtime Panics into Compile-Time Guarantees",
            "level_tr": "Temel / Orta Seviye",
            "level_en": "Foundational / Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Yapay zeka modelleri neden sürekli 'any' veya belirsiz tipler kullanmaya meyillidir ve bu tembellik projeyi nasıl çökertir?",
            "podcast_hook_en": "Why are LLMs notoriously predisposed to sprinkling `any` across codebases, and how does this laziness invite catastrophic production crashes?",
            "takeaways_tr": [
                "TypeScript veya statik tipler lüks değil; yapay zekanın saçmalamasını engelleyen en güçlü gardiyandır.",
                "`any` kullanmak, tip denetleyicisini (type checker) kör etmek ve çalışma zamanı hatalarına davetiye çıkarmaktır.",
                "Zod veya Pydantic gibi doğrulama kütüphaneleri, dış dünyadan gelen verinin AI kodunu patlatmasını engeller."
            ],
            "takeaways_en": [
                "Strict typing is not an aesthetic luxury; it is the most rigid guardrail against LLM hallucinations.",
                "Using `any` blinds the compiler, forfeiting compile-time safety and guaranteeing runtime failures.",
                "Runtime validation schemas (Zod, Pydantic) ensure unverified external payloads never pollute internal business logic."
            ],
            "story_tr": """Havalimanı gümrük kapısını düşünün. 

Gümrük memuru gelen her bavulu açıp kontrol etmek yerine: *"Geç geç, hepiniz geçin, ne olursa olsun kabulüm"* derse ne olur? Ülkeye yasaklı maddeler, kaçak eşyalar dolar. İşte TypeScript'te `any` kullanmak tam olarak budur.

Oysa sıkı bir tip sistemi (Strict Typing), bavulları x-ray cihazından geçiren memurdur:
*"Bu bavulda sadece 'User' tipi kıyafetler olabilir. 'undefined' veya 'null' tespit edildi, içeri giremezsiniz!"*

Yapay zeka modelleri bazen kolaya kaçıp `any` yazar. Bir mühendisin görevi, o gümrük kapısını asla nöbetçisiz bırakmamaktır.""",
            "story_en": """Imagine an international airport customs checkpoint.

If the customs officer waves every arriving passenger through saying: *"Go right ahead, no inspection needed, anything is welcome!"* the terminal descends into chaos. That is what using `any` does to a codebase.

A strict type system acts as the automated biometric scanner:
*"This payload must conform to the `User` contract. We detected `undefined` where a string was required; entry rejected."*

LLMs default to `any` because it satisfies the compiler with zero effort. Your engineering duty is to maintain strict boundary checkpoints.""",
            "mental_tr": """Tip Güvenliği Zinciri:

```
[Dış Dünya: API / Form / DB] 
       │
       ▼
[Çalışma Zamanı Doğrulama (Zod / Pydantic)] ──> "Girdi şemaya uyuyor mu?"
       │
       ▼
[Derleme Zamanı Güvencesi (Strict Types)] ──> "Asla undefined veya any yok"
       │
       ▼
[Saf & Temiz İş Mantığı (Clean Code)]
```""",
            "mental_en": """The Type-Safety Chain of Custody:

```
[External Ingress: API / Form / DB]
       │
       ▼
[Runtime Boundary Validation (Zod / Pydantic)] ──> "Does raw payload match schema?"
       │
       ▼
[Compile-Time Invariants (Strict Types)] ──> "Guaranteed non-null, zero `any`"
       │
       ▼
[Pure Business Logic (Clean Architecture)]
```""",
            "prompt_tr": """# ROL: TypeScript / Clean Code Gurusu
Aşağıdaki gevşek ve güvensiz yazılmış JavaScript/TypeScript fonksiyonunu incele.

## GÖREV:
1. Kodda `any` kullanımını tamamen kaldır.
2. Zod kullanarak gelen JSON verisini doğrulayan (runtime validation) bir şema yaz.
3. 'Early Return' ve Clean Code prensiplerine uygun, tip güvenli hale getir.

## KOD:
```typescript
function processOrder(data: any) {
  if (data) {
    if (data.items) {
      return data.items.map((i: any) => i.price * i.qty);
    }
  }
}
```""",
            "prompt_en": """# ROLE: TypeScript & Clean Code Architect
Refactor this loose, unsafe JavaScript/TypeScript function.

## TASK:
1. Eliminate all instances of `any`.
2. Introduce a Zod validation schema for runtime input validation.
3. Implement clean early returns and export strictly typed result interfaces.

## SNIPPET:
```typescript
function processOrder(data: any) {
  if (data) {
    if (data.items) {
      return data.items.map((i: any) => i.price * i.qty);
    }
  }
}
```""",
            "code_lang": "typescript",
            "code_naive": """// Kötü / Gevşek Tip: 'any' kullanımı ve tanımsız değer çökmesi riski
export function processOrderNaive(data: any): any {
  // Eğer data.items boşsa veya price string geldiyse ('100' * 2 = NaN) patlar!
  return data.items.map((item: any) => {
    return item.price * item.quantity;
  });
}""",
            "code_robust": """import { z } from "zod";

// 1. Çalışma Zamanı Şeması (Runtime Schema)
export const OrderItemSchema = z.object({
  id: z.string().uuid(),
  price: z.number().positive("Fiyat pozitif bir sayı olmalıdır."),
  quantity: z.number().int().positive("Adet pozitif tam sayı olmalıdır.")
});

export const OrderSchema = z.object({
  orderId: z.string().min(1),
  items: z.array(OrderItemSchema).min(1, "En az bir sipariş kalemi bulunmalıdır.")
});

// 2. TypeScript Tipleri Otomatik Türetilir (Inference)
export type Order = z.infer<typeof OrderSchema>;
export type OrderItem = z.infer<typeof OrderItemSchema>;

export interface OrderTotalResult {
  orderId: string;
  total: number;
  itemCount: number;
}

// 3. Tip Güvenli ve Temiz Fonksiyon
export function calculateOrderTotal(rawData: unknown): OrderTotalResult {
  // Veriyi kapıda doğrula: Geçersizse anında açıklayıcı hata fırlatır
  const validated = OrderSchema.parse(rawData);

  const total = validated.items.reduce((sum, item) => {
    return sum + (item.price * item.quantity);
  }, 0);

  return {
    orderId: validated.orderId,
    total: Math.round(total * 100) / 100,
    itemCount: validated.items.length
  };
}""",
            "code_notes_tr": "`unknown` tipi ile dışarıdan gelen verinin belirsizliği açıkça kabul edilmiş, ardından Zod ile kapıda doğrulanmıştır. `z.infer` ile tek bir kaynaktan hem derleme hem çalışma zamanı güvenliği sağlanmıştır.",
            "code_notes_en": "By accepting `unknown` and validating via Zod, the function guarantees runtime integrity. Types are inferred directly from schemas, eliminating duplication between type definitions and validation logic.",
            "pitfalls_tr": [
                {"trap": "Tip hatasını çözemeyince `// @ts-ignore` veya `as any` yazıp geçmek.", "solution": "Sorunu halının altına süpürmeyin; tip daraltma (type narrowing) veya Zod kullanın."},
                {"trap": "Sadece interface yazıp dışarıdan gelen JSON'ın buna uyduğunu varsaymak.", "solution": "TypeScript tipleri derlendikten sonra yok olur (type erasure); runtime'da Zod veya Pydantic şarttır."},
                {"trap": "İç içe 5 kat if-else piramitleri oluşturmak.", "solution": "Guard Clause (Early Return) desenini uygulayarak kodu düzleştirin."}
            ],
            "pitfalls_en": [
                {"trap": "Plastering `// @ts-ignore` or `as any` to silence compiler errors.", "solution": "Use proper type narrowing or runtime schema parsing instead of blinding the compiler."},
                {"trap": "Assuming external API responses match TypeScript interfaces without validation.", "solution": "TypeScript types are erased at runtime; parse untrusted input with Zod or Pydantic."},
                {"trap": "Constructing deeply nested 5-level if-else pyramids.", "solution": "Flatten logic using Guard Clauses and early returns."}
            ],
            "udemy_title_tr": "Ders 10: Tip Sistemleri ve Clean Code - Zod ile Kusursuz Doğrulama",
            "udemy_title_en": "Lecture 10: Type Systems & Clean Code - Bulletproof Validation with Zod",
            "udemy_slides_tr": [
                "Neden 'any' yazılım dünyasının en tehlikeli anahtar kelimesidir?",
                "Type Erasure nedir? Derleme zamanı vs Çalışma zamanı.",
                "Zod ile tek kaynaktan şema ve tip türetme.",
                "Guard Clause deseni ile iç içe if-else piramitlerinden kurtulmak."
            ],
            "udemy_slides_en": [
                "Why `any` is the most dangerous escape hatch in modern software.",
                "Understanding Type Erasure: Compile-time vs Runtime guarantees.",
                "Single source of truth: Inferring types directly from Zod schemas.",
                "Refactoring nested pyramids into clean Guard Clauses."
            ],
            "udemy_demo_tr": "Bir API endpoint simülasyonu yapın. Gelen bozuk JSON verisini (örneğin fiyatı string veya negatif olan bir obje) önce naive fonksiyona yollayın, `NaN` aldığını gösterin. Ardından Zod şemasından geçirin ve hatanın detaylı fırlatıldığını gösterin.",
            "udemy_demo_en": "Simulate an ingress API payload containing a malformed string price. Run it against naive code to produce `NaN`. Then pass it through Zod to illustrate descriptive validation error logs.",
            "action_task_tr": "Projenizde `any` kullanılan en az 2 yeri bulun. `any` yerine katı bir interface veya `unknown` + Zod doğrulaması ekleyin.",
            "action_task_en": "Find 2 instances of `any` in your active codebase. Replace them with explicit types or an `unknown` validation boundary.",
            "quiz_tr": [
                {
                    "question": "TypeScript kodunda `any` yerine `unknown` kullanmanın temel farkı nedir?",
                    "options": [
                        "A) Hiçbir farkı yoktur",
                        "B) `unknown` tipi, üzerinde işlem yapılmadan önce tip kontrolü (typeof, instanceof veya Zod) yapılmasını zorunlu kılar",
                        "C) `unknown` sadece sayılar için kullanılır",
                        "D) `unknown` kodun derlenmesini engeller"
                    ],
                    "answer": "B",
                    "explanation": "`any` tüm kontrolleri devre dışı bırakırken, `unknown` geliştiriciyi veriyi kullanmadan önce tipini daraltmaya zorlar."
                },
                {
                    "question": "Zod veya Pydantic gibi kütüphanelere neden ihtiyaç duyarız?",
                    "options": [
                        "A) CSS yazmak için",
                        "B) TypeScript tipleri derleme sonrasında silindiği için, dışarıdan gelen verileri çalışma zamanında (runtime) doğrulamak için",
                        "C) Sadece SQL sorgularını hızlandırmak için",
                        "D) Bilgisayarın fan hızını ayarlamak için"
                    ],
                    "answer": "B",
                    "explanation": "TypeScript derlendiğinde tüm tip tanımları silinir. Çalışma zamanında gelen verinin güvenliği ancak runtime validator'lar ile sağlanabilir."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the primary safety distinction between `unknown` and `any` in TypeScript?",
                    "options": [
                        "A) They are identical aliases",
                        "B) `unknown` requires explicit type narrowing before properties or methods can be accessed",
                        "C) `unknown` is restricted to primitive numeric types",
                        "D) `unknown` halts project builds"
                    ],
                    "answer": "B",
                    "explanation": "`any` disables all safety checks, whereas `unknown` enforces defensive narrowing before property access."
                },
                {
                    "question": "Why are runtime validation libraries like Zod or Pydantic indispensable in typed languages?",
                    "options": [
                        "A) To format stylesheet margins",
                        "B) Because static types are erased at runtime; runtime validation guards against malformed external inputs",
                        "C) Solely to accelerate SQL query execution",
                        "D) To optimize CPU fan profiles"
                    ],
                    "answer": "B",
                    "explanation": "Type systems undergo type erasure during compilation. Boundary inputs must be validated at runtime."
                }
            ]
        },

        # Chapter 11
        {
            "id": 11,
            "section_id": 2,
            "slug_tr": "ch11_hata_mesajlarini_ve_stack_trace_ai_ile_cozmek",
            "slug_en": "ch11_decoding_stack_traces_error_telemetry_ai",
            "title_tr": "Hata Mesajlarını ve Stack Trace'i AI ile Okuma ve Akıl Yürütme Sanatı",
            "title_en": "Decoding Stack Traces & Error Telemetry with AI: Scientific Triaging",
            "subtitle_tr": "Terminaldeki Kırmızı Yazılardan Korkmayı Bırakıp Dedektif Gibi İz Sürmek",
            "subtitle_en": "Overcoming Terminal Panic and Tracing Root Causes Like a Senior Detective",
            "level_tr": "Temel / Orta Seviye",
            "level_en": "Foundational / Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Junior mühendisler terminaldeki 50 satırlık kırmızı hata mesajını görünce neden panikler ve AI bu panikten nasıl kurtarır?",
            "podcast_hook_en": "Why do junior engineers freeze when confronted with a 50-line terminal stack trace, and how can AI turn that panic into systematic deduction?",
            "takeaways_tr": [
                "Stack Trace düşmanınız değil; hatanın nerede, ne zaman ve hangi çağrı zincirinde gerçekleştiğini söyleyen yol haritasıdır.",
                "AI'a sadece 'Kod çalışmıyor' demek yerine tüm stack trace'i ve ilgili fonksiyon kodunu vermek çözümü 10 saniyeye indirir.",
                "En üstteki kütüphane satırlarına değil, kendi yazdığınız kodun bulunduğu satır numarasına odaklanın."
            ],
            "takeaways_en": [
                "A stack trace is not an indictment of your intelligence; it is an exact GPS map of the failure chain.",
                "Prompting 'My app broke' wastes time; attaching the raw stack trace along with the origin function yields solutions in 10 seconds.",
                "Filter out internal third-party framework frames and zero in on the first line pointing to your project source code."
            ],
            "story_tr": """Bir uçağın kokpitini hayal edin. Aniden kırmızı bir ikaz ışığı yanıp sönüyor ve siren çalıyor.

Acemi bir pilot ne yapar? Panikleyip ellerini havaya kaldırır veya gözünü kapatır. 
Tecrübeli bir kaptan pilot ne yapar? Sakinlikle ikaz panelindeki hata kodunu okur: *"Motor 2 yağ basıncı uyarısı, Sayfa 4B kontrol listesini açın."*

Terminalinizde patlayan o 50 satırlık kırmızı Stack Trace de uçağın ikaz panelidir. O kırmızı yazılar size kızmıyor; sadece: *"Filanca dosyanın 42. satırında tanımsız bir objenin özelliğini okumaya çalıştın"* diyor.

Yapay zekayı yanınıza yardımcı pilot olarak aldığınızda, o karmaşık logları 5 saniyede tercüme edebilirsiniz.""",
            "story_en": """Picture an airplane cockpit at 35,000 feet. A red warning light flashes accompanied by an audio alert.

An inexperienced trainee might panic and freeze.
A veteran pilot calmly reads the fault telemetry: *"Hydraulic pressure drop in Engine 2; initiate Checklist 4B."*

That 50-line crimson stack trace in your terminal is that exact cockpit telemetry. The console isn't judging your worth; it is objectively informing you: *"On line 42 of `checkout.ts`, you attempted to read `.total` from an `undefined` reference."*

With an AI pair alongside you as co-pilot, triaging that telemetry becomes second nature.""",
            "mental_tr": """Stack Trace Okuma Filtresi:

```
[50 Satırlık Kırmızı Terminal Çıktısı]
               │
               ▼
[1. Hata Türü & Mesajı]: TypeError: Cannot read properties of undefined (reading 'email')
               │
               ▼
[2. Kütüphane Gürültüsünü Ele]: /node_modules/express/lib/router/... (ATLA!)
               │
               ▼
[3. Kendi Kodunun İlk Satırı]: at UserService.getUserProfile (src/services/user.ts:42:18)
               │
               ▼
[4. AI'a Beslenecek Odak]: "src/services/user.ts dosyasının 42. satırındaki çağrı bağlamı"
```""",
            "mental_en": """The Stack Trace Triaging Funnel:

```
[Raw 50-Line Terminal Panic Dump]
               │
               ▼
[1. Error Signature]: TypeError: Cannot read properties of undefined (reading 'email')
               │
               ▼
[2. Discard Framework Noise]: /node_modules/express/... (IGNORE)
               │
               ▼
[3. Identify First Application Frame]: at UserService.getUserProfile (src/services/user.ts:42:18)
               │
               ▼
[4. Precision AI Ingestion]: "Provide user.ts lines 35-50 along with the stack trace"
```""",
            "prompt_tr": """# ROL: Debugging ve Kök Neden Analiz Uzmanı
Uygulamamız aşağıdaki hatayı fırlattı.

## HATA MESAJI & STACK TRACE:
```text
TypeError: Cannot read properties of undefined (reading 'name')
    at formatCustomerCard (/app/src/utils/card.ts:34:25)
    at Array.map (<anonymous>)
    at getCustomersDashboard (/app/src/controllers/dashboard.ts:18:32)
```

## İLGİLİ KOD (src/utils/card.ts - Satır 30-40):
```typescript
export function formatCustomerCard(customer: Customer) {
  return {
    id: customer.id,
    displayName: customer.profile.name.toUpperCase(),
  };
}
```

## GÖREV:
1. Bu hatanın gerçek kök nedeni (Root Cause) nedir?
2. `profile` veya `name` alanının eksik geldiği durumları güvenle ele alacak defansif düzeltmeyi yap.
3. Bu durumun gelecekte tekrar etmemesi için TypeScript tipini güncelle.""",
            "prompt_en": """# ROLE: Senior Debugging & Root-Cause Analyst
Our service triggered the following uncaught exception:

## STACK TRACE:
```text
TypeError: Cannot read properties of undefined (reading 'name')
    at formatCustomerCard (/app/src/utils/card.ts:34:25)
    at Array.map (<anonymous>)
    at getCustomersDashboard (/app/src/controllers/dashboard.ts:18:32)
```

## SOURCE CONTEXT (src/utils/card.ts lines 30-40):
```typescript
export function formatCustomerCard(customer: Customer) {
  return {
    id: customer.id,
    displayName: customer.profile.name.toUpperCase(),
  };
}
```

## TASK:
1. Identify the root cause.
2. Provide a defensive refactor using Optional Chaining and Nullish Coalescing.
3. Update the type contract to prevent regression.""",
            "code_lang": "typescript",
            "code_naive": """// Hata Fırlatan Kod: Profil veya Name tanımsız olduğunda patlar
export function formatCustomerCardNaive(customer: any) {
  // Eğer customer.profile null veya undefined ise uygulama çöker!
  return {
    id: customer.id,
    displayName: customer.profile.name.toUpperCase(),
  };
}""",
            "code_robust": """export interface CustomerProfile {
  name?: string;
  avatarUrl?: string;
}

export interface Customer {
  id: string;
  profile?: CustomerProfile | null;
}

export interface FormattedCustomerCard {
  id: string;
  displayName: string;
}

export function formatCustomerCard(customer: Customer): FormattedCustomerCard {
  // Optional Chaining (?.) ve Nullish Coalescing (??) ile tam koruma
  const rawName = customer.profile?.name?.trim();
  const displayName = rawName ? rawName.toUpperCase() : "İSİMSİZ MÜŞTERİ";

  return {
    id: customer.id,
    displayName
  };
}""",
            "code_notes_tr": "Stack trace incelendiğinde `profile` nesnesinin null geldiği hemen anlaşılır. `customer.profile?.name` ile güvenli zincirleme yapılmış ve varsayılan bir geri dönüş değeri (`İSİMSİZ MÜŞTERİ`) atanarak çökme engellenmiştir.",
            "code_notes_en": "The stack trace directly reveals an unchecked dereference of `profile`. Leveraging optional chaining (`?.`) paired with fallbacks guarantees total resilience against incomplete payloads.",
            "pitfalls_tr": [
                {"trap": "Hata çıktısını okumadan tüm dosyayı silip baştan yazdırmak.", "solution": "Hatanın işaret ettiği dosya ve satır numarasını bulun, sadece o bloğu inceleyin."},
                {"trap": "Terminaldeki hatayı kopyalamadan AI'a 'kod hata verdi' demek.", "solution": "Her zaman hem hata türünü hem de ilk 10 satırlık stack trace'i eksiksiz yapıştırın."},
                {"trap": "Hatanın sadece sonucunu gizlemek (Örn: Boş try/catch ile hatayı yutmak).", "solution": "Hataları asla sessizce yutmayın; loglayın ve kök nedeni düzeltin."}
            ],
            "pitfalls_en": [
                {"trap": "Deleting and rewriting entire files rather than reading the stack trace.", "solution": "Target the exact file and line number pinpointed by the stack trace."},
                {"trap": "Prompting 'Code failed' without pasting the terminal trace.", "solution": "Always provide the exact error signature and the originating frame."},
                {"trap": "Swallowing errors silently using empty try/catch blocks.", "solution": "Never suppress exceptions without structured logging and fallback resolution."}
            ],
            "udemy_title_tr": "Ders 11: Stack Trace Okuma Sanatı - Kök Neden Analizi",
            "udemy_title_en": "Lecture 11: The Art of Stack Tracing - Root Cause Deduction with AI",
            "udemy_slides_tr": [
                "Stack Trace anatomisi: Hata türü, mesajı ve çağrı yığını.",
                "node_modules gürültüsünü filtreleyip uygulama kodunu bulmak.",
                "Optional Chaining (?.) ve Nullish Coalescing (??) ile defansif kodlama.",
                "Canlı vaka: Production çökmesini AI ile 60 saniyede teşhis edip çözmek."
            ],
            "udemy_slides_en": [
                "Anatomy of a stack trace: Exception type, payload, call frames.",
                "Filtering out dependency frames to isolate application logic.",
                "Defensive guards: Optional Chaining and Nullish Coalescing.",
                "Live triage: Resolving a production crash in 60 seconds with AI."
            ],
            "udemy_demo_tr": "Kasıtlı olarak `null.toUpperCase()` hatası fırlatan bir API yazın. Terminalde beliren stack trace'i kopyalayın, AI asistanına besleyip kök neden analizini ve çözümünü tek adımda gösterin.",
            "udemy_demo_en": "Trigger a deliberate `TypeError: Cannot read properties of undefined` in an Express route. Copy the raw trace into an AI prompt and demonstrate pinpoint root-cause analysis.",
            "action_task_tr": "Bugün çalıştığınız projede bilerek bir hata fırlatın (`throw new Error('Test Hatası')`). Oluşan stack trace'i satır satır inceleyerek çağrı zincirini takip edin.",
            "action_task_en": "Intentionally throw an exception in a local branch. Trace the execution frames step-by-step from controller to model.",
            "quiz_tr": [
                {
                    "question": "Bir stack trace incelenirken ilk bakılması gereken yer neresidir?",
                    "options": [
                        "A) En alttaki işletim sistemi çekirdek çağrıları",
                        "B) Hata mesajının kendisi (Error Signature) ve kendi proje dizinimize işaret eden ilk satır numarası",
                        "C) Bilgisayarın IP adresi",
                        "D) package.json dosyasının son satırı"
                    ],
                    "answer": "B",
                    "explanation": "Hatanın türü (örn. TypeError) ve kendi kaynak kodumuzun yer aldığı dosya/satır numarası sorunun kaynağını doğrudan gösterir."
                },
                {
                    "question": "JavaScript/TypeScript'te `customer?.profile?.name ?? 'Anonim'` ifadesinin sağladığı fayda nedir?",
                    "options": [
                        "A) Kodu 10 kat hızlandırır",
                        "B) Eğer customer veya profile tanımsız (undefined/null) ise çökmeden güvenle 'Anonim' değerini döndürür",
                        "C) Sadece sayılarda çalışır",
                        "D) Belleği tamamen sıfırlar"
                    ],
                    "answer": "B",
                    "explanation": "Optional Chaining (`?.`) zincirdeki ara eleman null/undefined ise hata fırlatılmasını önler; Nullish Coalescing (`??`) ise varsayılan değer sağlar."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the priority checkpoint when triaging an unfamiliar stack trace?",
                    "options": [
                        "A) Low-level operating system kernel syscalls at the bottom",
                        "B) The error name/message and the first frame referencing application workspace files",
                        "C) The local IP address",
                        "D) The final line of package.json"
                    ],
                    "answer": "B",
                    "explanation": "The error signature and the topmost application frame identify exactly what went wrong and where in your codebase."
                },
                {
                    "question": "What protection is conferred by `user?.profile?.name ?? 'Guest'`?",
                    "options": [
                        "A) Accelerating CPU instruction speeds",
                        "B) Preventing runtime null pointer crashes and supplying a reliable fallback value",
                        "C) Enforcing strictly numeric evaluations",
                        "D) Purging memory caches"
                    ],
                    "answer": "B",
                    "explanation": "Optional chaining aborts traversal gracefully if intermediate properties are nullish, and `??` assigns the fallback value."
                }
            ]
        },

        # Chapter 12
        {
            "id": 12,
            "section_id": 2,
            "slug_tr": "ch12_kod_okuma_super_gucu_yabanci_kod_tabanini_haritalamak",
            "slug_en": "ch12_codebase_onboarding_exploration_superpower",
            "title_tr": "Kod Okuma Süper Gücü: Yabancı Bir Kod Tabanını AI ile 10 Dakikada Haritalamak",
            "title_en": "Rapid Codebase Onboarding: Mapping Legacy Repositories in 10 Minutes with AI",
            "subtitle_tr": "200.000 Satırlık Monolite İlk Kez Bakan Junior'ın Hayatta Kalma Kılavuzu",
            "subtitle_en": "The Junior Survival Guide to Navigating Massive 200,000-Line Codebases",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Bir şirkette ilk iş gününüzde 200.000 satırlık devasa bir kod tabanıyla karşılaştığınızda, günlerce kaybolmak yerine AI ile sistemi nasıl 1 saatte çözebilirsiniz?",
            "podcast_hook_en": "When confronted with a 200,000-line legacy monolith on Day 1, how can an AI-empowered junior map core data flows in 60 minutes instead of drowning for weeks?",
            "takeaways_tr": [
                "Yazılım mühendisleri zamanlarının %70'ini kod yazarak değil, mevcut kodu okuyarak ve anlayarak geçirir.",
                "Bilinmeyen bir projeyi incelerken ilk bakılacak yerler: `package.json`, giriş noktası (`index/main`) ve veritabanı şemalarıdır.",
                "AI'a 'Tüm projeyi oku' demek yerine; 'Giriş isteği (request) geldiğinde hangi katmanlardan geçiyor?' gibi akış soruları sorun."
            ],
            "takeaways_en": [
                "Professional engineers spend upwards of 70% of their working hours reading and synthesizing existing code, not authoring new lines.",
                "Primary orientation coordinates: dependencies manifest (`package.json`), entry point (`index/main`), and data schemas (`schema.prisma`).",
                "Do not dump entire repositories into AI; query execution pipelines: 'Trace the lifecycle of a POST /checkout request from route to database'."
            ],
            "story_tr": """Kendinizi yabancı bir metropolde, örneğin Tokyo'da bir sokak ortasında hayal edin. Elinizde harita yok, tabelalardaki yazıları okuyamıyorsunuz ve binalar gökyüzüne uzanıyor.

Geleneksel bir junior mühendis 500 dosyalık bir şirket projesini açtığında tam olarak bu Tokyo sendromunu yaşar: *"Ben neredeyim? Bu dosya nereye bağlanıyor?"*

Akıllı bir gezgin ne yapar? Önce metro haritasını açar, ana hatları (kırmızı, mavi hatlar) öğrenir.

Kod tabanının metro haritası:
1. Giriş kapısı (Main / Entry Point)
2. Veritabanı modelleri (Data Models)
3. API yönlendiricileri (Router / Controllers)

Yapay zeka ise elinizdeki akıllı navigasyon cihazıdır. Doğru soruları sorduğunuzda sizi 10 dakikada şehrin merkezine ulaştırır.""",
            "story_en": """Imagine landing in central Tokyo for the first time without cellular data or an English map. Skyscrapers tower above you and metro entrances swarm with thousands of commuters.

New junior hires experience this exact sensory overload when opening an enterprise repository: *"Where is the entry point? Why are there 80 nested directories?"*

A seasoned traveler immediately pulls up the primary transit map to understand trunk lines:
1. Application entry points (`main.ts` or `index.ts`)
2. Persistence schemas (`schema.prisma` or migration files)
3. Ingress routes (`routes/` or `controllers/`)

Modern AI IDE tooling serves as your real-time translation GPS, turning incomprehensible labyrinths into clear mental maps in minutes.""",
            "mental_tr": """Kod Tabanı Haritalama Hiyerarşisi (Top-Down Yaklaşım):

```
1. MANİFESTO: package.json / pyproject.toml 
   └── Teknoloji yığını, bağımlılıklar, scriptler

2. VERİ MODELİ: schema.prisma / models/
   └── Bu sistem neyi saklıyor? (Kullanıcı, Ürün, Fatura)

3. GİRİŞ KAPISI: src/main.ts / app.py
   └── Sunucu nasıl ayağa kalkıyor? Hangi middleware'ler devrede?

4. İŞ MANTIĞI: services/ / use-cases/
   └── Gerçek dünya kuralları nerede işleniyor?
```""",
            "mental_en": """The Top-Down Codebase Mapping Hierarchy:

```
1. MANIFEST: package.json / requirements.txt / Cargo.toml
   └── Stack detection, active scripts, major frameworks

2. DATA MODELS: schema.prisma / migrations / models/
   └── What nouns populate this universe? (User, Order, Invoice)

3. ENTRY POINT: src/main.ts / index.js / main.py
   └── How does the server bootstrap? What middleware intercepts traffic?

4. DOMAIN ENGINE: services/ / use-cases/
   └── Where do business rules actually execute?
```""",
            "prompt_tr": """# ROL: Kıdemli Yazılım Mimarı Onboarding Rehberi
Projeye yeni katılan bir mühendisim. Projemizde aşağıdaki 3 ana dosya bulunmaktadır:
1. @package.json
2. @schema.prisma
3. @src/server.ts

## GÖREV:
Bu 3 dosyayı inceleyerek bana şu konularda 1 sayfalık yönetici özeti sun:
1. Bu sistem temel olarak ne işe yarar (iş modeli nedir)?
2. Bir HTTP isteği geldiğinde izlenen tipik akış mimarisi nasıldır?
3. Projeyi yerel makinemde ayağa kaldırmak için çalıştırmam gereken komut sırası nedir?""",
            "prompt_en": """# ROLE: Senior Architectural Onboarding Mentor
I just joined this engineering squad. I am attaching three core orientation files:
1. @package.json
2. @schema.prisma
3. @src/server.ts

## TASK:
Synthesize these inputs into a concise, 1-page architectural briefing:
1. What is the business domain of this application?
2. What is the typical end-to-end request lifecycle (route -> controller -> service -> database)?
3. What is the deterministic sequence of local commands to bootstrap and run the test suite?""",
            "code_lang": "bash",
            "code_naive": """# Kötü Yaklaşım: Nereden başlayacağını bilmeden rastgele dosyaları açıp kaybolmak
# 500 dosya arasında kaybolup 3 gün boyunca hiçbir şey anlayamamak...""",
            "code_robust": """# Akıllı Haritalama İş Akışı:
# 1. Proje bağımlılıklarını ve çalıştırma komutlarını incele
cat package.json | grep -A 10 "scripts"

# 2. Veritabanı modellerini haritala
cat prisma/schema.prisma | grep "model "

# 3. Testleri çalıştırarak canlı doğrulama yap
npm run test:unit

# 4. Cursor / AI aracında @codebase ile sistem mimarisi diyagramı iste:
# "Generate a mermaid diagram illustrating the lifecycle of an order creation request." """,
            "code_notes_tr": "Yeni bir projeye girdiğinizde rastgele dosya okumak yerine `scripts` alanını ve veritabanı modellerini incelemek size 10 kat daha hızlı resmin bütününü verir. AI'a Mermaid formatında mimari diyagram çizdirmek akılda kalıcılığı artırır.",
            "code_notes_en": "Inspecting package scripts and data schemas before reading implementation code accelerates system comprehension tenfold. Prompting an AI model to generate Mermaid.js sequence diagrams makes abstract architecture tangible.",
            "pitfalls_tr": [
                {"trap": "İlk günden tüm kod tabanını baştan sona okumaya çalışıp tükenmek.", "solution": "Sadece üzerinde çalışacağınız ilk biletin (ticket) dokunduğu dosyaları izole edin."},
                {"trap": "Projeyi lokalde çalıştırmadan sadece statik kod okumak.", "solution": "İlk gün hedefiniz projeyi yerel makinenizde hatasız derleyip testleri yeşile döndürmek olsun."},
                {"trap": "Ekip arkadaşlarına sormadan önce AI ile kodun amacını analiz etmemek.", "solution": "Senior'a gitmeden önce AI ile temel akışı çıkarın; soru sorarken 'X dosyasını inceledim, Y akışını teyit etmek istiyorum' deyin."}
            ],
            "pitfalls_en": [
                {"trap": "Attempting to read all 500 repository files sequentially on Day 1.", "solution": "Isolate strictly the vertical slice pertinent to your first assigned ticket."},
                {"trap": "Analyzing code statically without ever spinning up the local test suite.", "solution": "Make passing unit tests locally your number-one Day 1 objective."},
                {"trap": "Interrupting senior teammates with basic structural questions before consulting AI.", "solution": "Map the workflow via AI first, then approach seniors with informed validation questions."}
            ],
            "udemy_title_tr": "Ders 12: Kod Okuma Süper Gücü - Kod Tabanını Haritalamak",
            "udemy_title_en": "Lecture 12: The Code Reading Superpower - Rapid Architecture Mapping",
            "udemy_slides_tr": [
                "Yazılımcılık neden %70 kod okuma, %30 kod yazmadır?",
                "3 Nokta Kılavuzu: Manifestolar, Veri Modelleri, Giriş Noktaları.",
                "Mermaid.js ile AI destekli anlık mimari akış diyagramları üretmek.",
                "Bölüm 2 Özeti: Algoritmik Düşünceden Büyük Resme."
            ],
            "udemy_slides_en": [
                "Why professional engineering is 70% reading and 30% writing.",
                "The 3-point navigation method: Manifests, Schemas, Entry points.",
                "Generating dynamic Mermaid sequence diagrams from repositories with AI.",
                "Module 2 Recap: From Algorithmic Primitives to Big-Picture Systems."
            ],
            "udemy_demo_tr": "Açık kaynaklı popüler bir repoyu (örneğin Redux Toolkit veya tRPC) açın. Cursor'da `@codebase` kullanarak: 'Generate a Mermaid sequence diagram for a basic request' komutunu verin. Çıkan diyagramı Markdown önizlemesinde inceleyerek akışı anlatın.",
            "udemy_demo_en": "Open an open-source repository. In Cursor chat, run `@codebase` to generate a Mermaid diagram of the primary request flow. Render the diagram in markdown preview and walk through the architectural layers.",
            "action_task_tr": "GitHub'da yıldızı yüksek bir açık kaynak projesini klonlayın. AI asistanınızı kullanarak 15 dakika içinde projenin ne işe yaradığını ve veri tabanı modellerini özetleyen bir `ARCHITECTURE.md` dosyası çıkartın.",
            "action_task_en": "Clone a popular open-source repository. Using your AI IDE, spend 15 minutes drafting a concise `ARCHITECTURE.md` summary covering data models and entry points.",
            "quiz_tr": [
                {
                    "question": "Yabancı bir yazılım projesine ilk kez katıldığınızda sistemin ne yaptığını anlamak için en stratejik başlangıç noktası neresidir?",
                    "options": [
                        "A) Rastgele bir CSS dosyası",
                        "B) Proje manifestosu (package.json / pyproject.toml) ve veritabanı şemaları (schema / models)",
                        "C) .gitignore dosyası",
                        "D) README dosyasındaki telif hakları bölümü"
                    ],
                    "answer": "B",
                    "explanation": "Manifesto projenin teknoloji yığınını ve araçlarını gösterirken, veritabanı şemaları sistemin işlediği gerçek dünya nesnelerini (User, Order vb.) ortaya koyar."
                },
                {
                    "question": "AI yardımıyla bir kod tabanının akışını görselleştirmek için en yaygın kullanılan markdown tabanlı diyagram dili hangisidir?",
                    "options": [
                        "A) HTML5",
                        "B) Mermaid.js",
                        "C) SASS",
                        "D) Dockerfile"
                    ],
                    "answer": "B",
                    "explanation": "Mermaid.js, doğrudan markdown dosyaları içinde sequence, flowchart ve class diyagramları oluşturmaya yarayan endüstri standardı bir araçtır."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the most strategic entry point when orienting yourself inside an unfamiliar repository?",
                    "options": [
                        "A) Arbitrary stylesheet files",
                        "B) The project dependency manifest (`package.json`) and database models (`schema.prisma` / `models/`)",
                        "C) The `.gitignore` configuration",
                        "D) Copyright disclaimers"
                    ],
                    "answer": "B",
                    "explanation": "Manifests establish the technology stack, while schemas reveal the core domain entities and business nouns powering the system."
                },
                {
                    "question": "Which markdown-native text-to-diagram specification is the industry standard for modeling software architecture with AI?",
                    "options": [
                        "A) HTML5 Canvas",
                        "B) Mermaid.js",
                        "C) PostCSS",
                        "D) Dockerfile"
                    ],
                    "answer": "B",
                    "explanation": "Mermaid.js allows developers to generate flowcharts, sequence diagrams, and class diagrams directly inside markdown documentation."
                }
            ]
        }
    ]
