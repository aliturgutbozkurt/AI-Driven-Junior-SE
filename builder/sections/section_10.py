"""
Section 10: Kariyer, Yumuşak Beceriler & Kıdemli Mühendislik (Chapters 55 to 60)
"""

def get_section_chapters():
    return [
        # Chapter 55
        {
            "id": 55,
            "section_id": 10,
            "slug_tr": "ch55_juniordan_midlevela_terfi_haritasi",
            "slug_en": "ch55_the_roadmap_from_junior_to_midlevel",
            "title_tr": "Junior'dan Mid-Level'a Geçişin Haritası: Hangi Metriklerle Ölçülürsün?",
            "title_en": "The Roadmap from Junior to Mid-Level: Key Performance Signals",
            "subtitle_tr": "Sürekli Yardım İsteyen Geliştiriciden Bağımsız Çözüm Üreten Mühendise Dönüşmek",
            "subtitle_en": "Transitioning from Constant Supervision to High-Autonomy Engineering Execution",
            "level_tr": "İleri Seviye",
            "level_en": "Advanced",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Bir yazılımcının unvanını 'Junior'dan 'Mid-Level'a taşıyan şey yazdığı kod satırı sayısı mıdır, yoksa aldığı sorumluluğun ve özerkliğin (autonomy) seviyesi midir?",
            "podcast_hook_en": "What truly transitions an engineer from Junior to Mid-Level? Is it raw years of experience, or the degree of autonomy and ambiguity they can untangle?",
            "takeaways_tr": [
                "Junior adım adım yönlendirme (hand-holding) bekler; Mid-Level belirsiz bir problemi alıp bağımsız çözer.",
                "Terfi etmenin en hızlı yolu, sadece kodu değil; testini, dokümantasyonunu ve deployment'ını sahiplenmektir (End-to-End Ownership).",
                "Senior mühendisin vaktini koruyan junior, ekipteki en değerli junior'dır."
            ],
            "takeaways_en": [
                "Juniors require prescriptive step-by-step guidance; Mid-levels take ambiguous problem statements and deliver autonomous solutions.",
                "The fastest accelerator to promotion is end-to-end ownership: owning tests, deployment, monitoring, and edge-case follow-through.",
                "The junior who protects senior engineer focus time by doing thorough pre-flight homework is the most valuable asset on the squad."
            ],
            "story_tr": """İki marangoz çırağını hayal edin:

**Çırak Can:** Ustanın yanına her 5 dakikada bir gelir:
- *"Usta bu tahtayı hangi testereyle keseyim?"*
- *"Usta bu vidayı nereye sıkayım?"*
- *"Usta cetveli bulamadım, ne yapayım?"*
Usta iş yapamaz hale gelir, akşama kadar Can'ı yönetir!

**Çırak Elif:** Usta sabah gelir ve der ki: *"Bize bu odaya sığacak bir kitaplık lazım."*
Elif odayı ölçer, taslağı çizer, tahtaları keser, monte eder ve akşam ustaya bitmiş kitaplığı sunar: *"Usta kitaplığı yaptım, sağlamlığını test ettim, verniğini attım. İncelemek ister misin?"*

Usta Elif'e bakar ve der ki: *"Sen artık çırak değilsin, sen artık bir kalfasın (Mid-Level)!"*

Yazılımda da terfi formülü budur: Soru sormak ayıp değildir; ama ödevini yapıp çözümlerle gelen mühendis ışık hızında yükselir.""",
            "story_en": """Consider two carpentry apprentices:

**Apprentice Jack:** Interrupts the master carpenter every 7 minutes:
- *"Which saw blade should I use for this pine plank?"*
- *"Where is the wood glue stored?"*
- *"I mismeasured by 2 inches, what should I do?"*
The master craftsman spends their entire day micro-managing Jack.

**Apprentice Sarah:** The master says: *"We need a sturdy 4-shelf oak bookcase for Room B."*
Sarah measures the alcove, calculates load-bearing joints, cuts the timber, sands the edges, and presents the completed piece at 4 PM: *"Bookcase is built, leveled, and stress-tested with 100 lbs. Ready for final inspection."*

The master smiles: *"You are no longer an apprentice. You are a journeyman engineer."*

Autonomy is the sole currency of promotion. It is not about never asking questions; it is about bringing validated options rather than open-ended problems.""",
            "mental_tr": """Mühendislik Seviyeleri ve Sorumluluk Matrisi:

| Seviye | Problem Tanımı | Çözüm Yolu | Beklenen Çıktı |
| :--- | :--- | :--- | :--- |
| **Junior** | Çok net, küçük bilet (Örn: "Butonun rengini mavi yap") | Senior yönlendirmesiyle adım adım | Çalışan temiz kod |
| **Mid-Level** | Orta belirsizlik (Örn: "Kupon doğrulama servisini yaz") | Bağımsız mimari araştırma + AI ile çözüm | Test edilmiş, deploy edilmiş servis |
| **Senior** | Yüksek belirsizlik (Örn: "Ödeme altyapısını ölçeklendir") | Stratejik mimari karar, risk yönetimi | Takımın yönü ve sistem dayanıklılığı |""",
            "mental_en": """The Engineering Maturity Spectrum:

| Level | Problem Ambiguity | Execution Autonomy | Core Deliverable |
| :--- | :--- | :--- | :--- |
| **Junior** | Low (Prescriptive task: 'Add email regex to form') | Requires mentoring on design & conventions | Clean, verified code syntax |
| **Mid-Level** | Moderate ('Implement coupon verification engine') | Autonomous decomposition via AI & docs | Production-tested, monitored feature |
| **Senior** | High ('Scale checkout subsystem to 50k RPS') | Strategic architectural decisions & mentoring | System reliability, team velocity, architecture |""",
            "prompt_tr": """# ROL: Mühendislik Direktörü ve Kariyer Mentoru
Ben bir teknoloji şirketinde 1 yıldır çalışan ve Mid-Level seviyesine terfi etmek isteyen bir Junior mühendisim.

## GÖREV:
1. Bir sonraki 6 ay içinde Mid-Level seviyesine çıkmamı sağlayacak 4 temel somut yetkinliği listele (Bağımsızlık, Test Kalitesi, İletişim, Hata Çözme).
2. Senior mühendislere soru sorarken 'Senior Vaktini Koruyan Soru Sorma Şablonu'nu hazırla.
3. Yönetici ile yapacağım 1-on-1 toplantısında terfi beklentimi profesyonelce konuşma senaryosu sun.""",
            "prompt_en": """# ROLE: Director of Engineering & Career Coach
I am a junior software engineer aiming for promotion to Mid-Level within 6 months.

## TASK:
1. Define 4 concrete behavioral signals that demonstrate mid-level readiness (Autonomy, Quality, Communication, Triage).
2. Author a 'Senior Focus-Shielding Question Template' to use when blocked.
3. Provide a script for my next 1-on-1 performance review aligning expectations with my engineering manager.""",
            "code_lang": "markdown",
            "code_naive": """# Kötü Soru Sorma Şekli (Senior'ı Tüketen):
"Selam abi, benim kod hata veriyor baksana bi." """,
            "code_robust": """# Profesyonel ve Senior Vaktini Koruyan Soru Sorma Şablonu:

"Selam Can, [Jira-405] biletinde ödeme webhook'unu test ederken bir sorunla karşılaştım.

1. **GÖZLEM:** Stripe'tan gelen webhook'ta imza doğrulaması başarısız oluyor (`SignatureVerificationError`).
2. **DENEDİKLERİM:**
   - Ham body'nin (`rawBody`) bozulup bozulmadığını kontrol ettim.
   - Webhook secret anahtarının doğruluğunu test ettim.
   - Sentry loglarında gelen header'ı inceledim.
3. **HİPOTEZİM:** Express'teki `bodyParser.json()` middleware'i raw body buffer'ını parse ettiği için imza eşleşmiyor olabilir.
4. **SORUM:** Daha önce bu projede webhook rotası için `bodyParser.raw()` muafiyeti uygulanmış bir örnek var mı, nereden bakmamı önerirsin?" """,
            "code_notes_tr": "Bu şablon sayesinde senior mühendis sorunu 30 saniyede anlar; junior'ın çaba gösterdiğini ve hipotez kurduğunu görerek büyük saygı duyar.",
            "code_notes_en": "This template demonstrates deep preparation, respect for senior focus time, and scientific deduction. Senior leads gladly mentor developers who present structured context and tested hypotheses.",
            "pitfalls_tr": [
                {"trap": "Takıldığı an hiçbir araştırma yapmadan anında senior'ın masasına koşmak.", "solution": "Soruyu sormadan önce en az 20 dakika AI ve dökümantasyon ile araştırma yapıp hipotezlerinizi listeleyin."},
                {"trap": "Haftalarca sessizce takılıp kalıp (stuck) kimseye hiçbir şey söylememek.", "solution": "Eğer bir problemde 45 dakika boyunca hiçbir ilerleme kaydedemediyseniz profesyonelce yardım isteyin."},
                {"trap": "Sadece kendisine verilen görevi yapıp sistemin bütünüyle ilgilenmemek.", "solution": "Deploy süreçlerini, logları ve müşteri geri bildirimlerini merak edip takip edin."}
            ],
            "pitfalls_en": [
                {"trap": "Interrupting seniors the instant an error occurs without doing baseline research.", "solution": "Invest 20 minutes isolating variables, querying AI, and documenting hypotheses before asking."},
                {"trap": "Suffering in total silence for 3 days without reporting blockers.", "solution": "If completely blocked for >45 minutes with zero forward momentum, escalate using the structured template."},
                {"trap": "Treating software as mere ticket completion rather than business impact.", "solution": "Take ownership of telemetry, deployments, and customer feedback beyond the pull request."}
            ],
            "udemy_title_tr": "Ders 55: Junior'dan Mid-Level'a Terfi - Özerklik ve Sahiplik",
            "udemy_title_en": "Lecture 55: The Road to Mid-Level - Autonomy, Ownership & Impact",
            "udemy_slides_tr": [
                "Junior vs Mid-Level: Kod yazma hızından bağımsızlık seviyesine.",
                "Senior vaktini koruyan soru sorma sanatı.",
                "Uçtan uca sahiplik (End-to-End Ownership) felsefesi.",
                "1-on-1 toplantılarında terfi beklentisini yönetmek."
            ],
            "udemy_slides_en": [
                "Junior vs. Mid-Level: Shifting focus from syntax to autonomous execution.",
                "The art of asking high-signal engineering questions.",
                "End-to-end ownership: From specification to production monitoring.",
                "Navigating performance reviews and salary conversations constructively."
            ],
            "udemy_demo_tr": "Bir slack mesajı simülasyonu yapın. Kötü ve tembel bir soru ile profesyonel '4 Adımlı Soru Şablonu'nu yan yana koyarak senior mühendislerin verdiği tepkiyi ve kazanılan saygıyı tartışın.",
            "udemy_demo_en": "Contrast two real Slack messages: a vague 'It broke' ping vs. a structured 4-step context briefing. Show how the structured approach accelerates resolution and builds team trust.",
            "action_task_tr": "Takıldığınız bir sonraki teknik problemde 'Senior Vaktini Koruyan Soru Şablonu'nu kullanarak mesajınızı hazırlayın ve öyle yardım isteyin.",
            "action_task_en": "The next time you encounter a technical blocker, draft your help request strictly using the 4-part template (Observation, Attempts, Hypothesis, Specific Ask).",
            "quiz_tr": [
                {
                    "question": "Bir yazılım mühendisinin 'Mid-Level' seviyesine ulaştığını gösteren en belirgin performans sinyali nedir?",
                    "options": [
                        "A) Günde 2000 satır kod yazması",
                        "B) Kendisine verilen orta karmaşıklıktaki bir görevi, sürekli yönlendirmeye ihtiyaç duymadan mimari araştırmasını yaparak, testlerini yazarak ve uçtan uca sahiplenerek bağımsız (autonomous) çözebilmesi",
                        "C) Şirketin en eski çalışanı olması",
                        "D) Klavyeye bakmadan yazabilmesi"
                    ],
                    "answer": "B",
                    "explanation": "Mid-level seviyesinin temel tanımı 'Özerklik'tir (Autonomy). Sürekli yönlendirme gerektirmeden işi teslim edebilen mühendis artık junior değildir."
                },
                {
                    "question": "Kıdemli bir mühendise soru sorarken yapılması gereken en profesyonel davranış nedir?",
                    "options": [
                        "A) Sadece 'kod çalışmıyor' yazıp beklemek",
                        "B) Sorunu özetlemek, neleri denediğini belirtmek, kendi hipotezini sunmak ve spesifik bir konuda görüş istemek",
                        "C) Soru sormaktan tamamen vazgeçip işi bırakmak",
                        "D) Gece yarısı aramak"
                    ],
                    "answer": "B",
                    "explanation": "Ödevini yapmış, denediği yolları ve hipotezini sunan geliştirici hem senior'ın vaktini korur hem de profesyonel olgunluğunu kanıtlar."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the primary operational signal that an engineer has attained Mid-Level competence?",
                    "options": [
                        "A) Typing 2,000 lines of code daily",
                        "B) Independently driving moderately ambiguous features from specification through testing and deployment without hand-holding",
                        "C) Longevity at the company",
                        "D) Touch typing speed"
                    ],
                    "answer": "B",
                    "explanation": "Autonomy is the defining metric of mid-level engineering: solving problems reliably with minimal supervision."
                },
                {
                    "question": "What constitutes the most professional protocol when requesting senior debugging guidance?",
                    "options": [
                        "A) Sending a raw screenshot with 'doesn't work'",
                        "B) Stating the observation, enumerating attempted experiments, proposing a hypothesis, and asking a scoped question",
                        "C) Remaining silent indefinitely",
                        "D) Pinging seniors outside working hours"
                    ],
                    "answer": "B",
                    "explanation": "Documenting your attempts and hypotheses respects senior focus time and accelerates diagnosis."
                }
            ]
        },

        # Chapter 56
        {
            "id": 56,
            "section_id": 10,
            "slug_tr": "ch56_teknik_iletisim_urun_yoneticileriyle_konusma",
            "slug_en": "ch56_technical_communication_bridging_tech_and_business",
            "title_tr": "Teknik İletişim: Ürün Yöneticileri ve Tasarımcılarla Konuşma Sanatı",
            "title_en": "Technical Communication: Bridging Tech & Business Stakeholders",
            "subtitle_tr": "'Jargon' Duvarını Yıkıp İş Değeriyle Konuşan Mühendis Olmak",
            "subtitle_en": "Translating Tech Debt, Latency, and Architecture into Revenue and Business Value",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Yazılımcılar neden 'Bu kod çok çirkin, refactor etmemiz lazım' dediğinde patron bütçe vermez de, 'Bu refactor ödeme dönüşüm oranını %12 artıracak' dediğinde anında onaylar?",
            "podcast_hook_en": "Why do executives reject requests to 'clean up tech debt' but instantly fund proposals that 'accelerate checkout page load to boost conversion by 8%'?",
            "takeaways_tr": [
                "Şirketler kod için değil; müşterilere değer üretmek ve ciro kazanmak için vardır.",
                "Ürün Yöneticisi (PM) ve Tasarımcılarla konuşurken teknik jargonu (ORM, Big-O, Pod) bırakıp iş etkisine (Hız, Maliyet, Kullanıcı Kaybı) odaklanın.",
                "Bir şeye 'Olmaz' demek yerine her zaman 'Şu maliyetle ve şu takasla (trade-off) yapılabilir' alternatifini sunun."
            ],
            "takeaways_en": [
                "Software companies exist to deliver customer value and business revenue, not to produce aesthetic code.",
                "When communicating with Product Managers and Designers, translate technical jargon into business metrics: user retention, conversion, and cloud spend.",
                "Never say a blunt 'That's technically impossible'; counter with: 'We can achieve that objective via this trade-off in half the time.'"
            ],
            "story_tr": """Bir oto tamircisine gittiğinizi düşünün.

Tamirci kaputu açıyor ve size şöyle diyor: *"Efendim krank milinin eksantrik segmanındaki mikrometre toleransı 0.04 bar sürtünme oluşturuyor, subapları rektifiye etmemiz lazım!"*
Ne anlarsınız? Hiçbir şey! Korkarsınız ve tamirciye güvenmezsiniz.

Peki tamirci şöyle derse: *"Aracınızın motorundaki şu parça aşınmış. Eğer şimdi 500 TL'ye değiştirmezsek, haftaya uzun yolda motor yanar ve 50.000 TL masraf çıkar."*
Anında onaylarsınız!

Yazılımda Ürün Yöneticileri (Product Manager) ve CEO'lar tam olarak o araba sahibidir. Onlara: *"PostgreSQL connection pool tükendi"* derseniz anlamazlar. 
*"Sunucu yoğunlukta siparişleri kaçırıyor ve günde 10.000 TL kaybediyoruz"* derseniz bütçeyi hemen alırsınız.""",
            "story_en": """Visit an automotive mechanic with engine trouble.

The mechanic lifts the hood and says: *"Your crankshaft eccentric journal exhibits 0.04 bar hydraulic cavitation, requiring immediate line boring!"*
You understand nothing. You feel alienated and skeptical.

Now imagine the mechanic says: *"This $40 rubber timing belt is frayed. If we replace it today, it takes an hour. If it snaps on the highway next week, the pistons smash the valves, destroying the entire engine for $6,000."*
You approve the repair immediately.

Product Managers and executive stakeholders are that vehicle owner. Explaining that *"Our Redis connection pool is hitting maxclients"* induces blank stares. Explaining that *"Customers are seeing checkout failures, losing $15,000 in daily orders"* earns instant alignment.""",
            "mental_tr": """Jargondan İş Değerine Tercüme Sözlüğü:

```
TEKNİK JARGON (Yazılımcı Dili)          ──> İŞ DEĞERİ (Yönetici Dili)
─────────────────────────────────────────────────────────────────────────────
"Teknik borcumuz çok birikti."         ──> "Geliştirme hızımız yarıya düştü; 
                                            yeni özellikleri 2 kat yavaş çıkarıyoruz."

"Database index'i eklememiz lazım."    ──> "Arama sayfası 6 saniyeden 0.5 saniyeye 
                                            inecek ve sepeti terk edenler azalacak."

"Test yazmamız gerekiyor."             ──> "Canlıya güncelleme çıkarken sistemin 
                                            çökmesini ve müşteri kaybını önleyeceğiz."

"AWS sunucu boyutunu büyütelim."       ──> "Aylık 20$ maliyetle cuma yoğunluğundaki 
                                            kesintileri sıfıra indireceğiz."
```""",
            "mental_en": """The Engineering-to-Business Translation Matrix:

```
TECHNICAL JARGON (Engineering)          ──> BUSINESS OUTCOME (Stakeholder)
─────────────────────────────────────────────────────────────────────────────
"We have catastrophic technical debt."   ──> "Feature delivery velocity has halved; 
                                             every new release takes twice as long."

"We must add composite database indexes."──> "Page latency drops from 4s to 300ms, 
                                             reducing checkout cart abandonment."

"We need comprehensive unit test suites."──> "We eliminate production outages on deploy 
                                             days, safeguarding customer trust."

"We should upgrade our Redis instances." ──> "A $30 monthly cloud bump eliminates 
                                             checkout timeouts during Black Friday."
```""",
            "prompt_tr": """# ROL: Teknik Ürün Yöneticisi ve İletişim Koçu
Ben bir backend mühendisiyim. Ürün Yöneticimize (Product Manager) 2 haftalık bir 'Teknik Borç ve Performans İyileştirme' sprinti için bütçe/zaman vermesi gerektiğini anlatmak istiyorum.

## GÖREV:
1. Mühendislerin yaptığı en yaygın 3 iletişim hatasını listele.
2. Teknik borcu 'Para, Hız ve Müşteri Memnuniyeti' metrikleriyle anlatan ikna edici 1 sayfalık bir toplantı brifi hazırla.
3. PM'in 'Şu an yeni özellik çıkarmamız lazım, bunu erteleyelim' itirazına verilecek profesyonel ve yapıcı karşı argümanı yaz.""",
            "prompt_en": """# ROLE: VP of Product & Engineering Communication Coach
I am a software engineer pitching a 2-week technical debt and refactoring sprint to our Product Manager.

## TASK:
1. Identify the 3 most common communication failures engineers commit during roadmap planning.
2. Author an executive briefing framing technical debt through revenue, velocity, and customer retention metrics.
3. Formulate a constructive response to the PM's pushback: 'We must ship Features X and Y first; let's defer refactoring.'""",
            "code_lang": "markdown",
            "code_naive": """# Kötü Mühendis İletişimi:
"Kodlar spagetti oldu, kimse anlamıyor. Bu sprint yeni özellik yazamam, refactor yapmam lazım." """,
            "code_robust": """# İş Odaklı Mühendislik Teklifi:

## 🎯 Konu: Ödeme Altyapısı Hızlandırma ve Çökme Önleme Yatırımı

Sayın Ürün Ekibi,

Son 3 sprint verilerimizi incelediğimizde:
- Ödeme sayfamız ortalama **4.2 saniyede** yükleniyor (Sektör ideali: < 1.5 saniye).
- Yavaşlık sebebiyle sepetten dönen kullanıcı oranımız yaklaşık **%8**.
- Ayrıca ödeme kodunun karmaşıklığı nedeniyle yeni bir ödeme yöntemi eklemek 2 hafta sürüyor.

### 💡 2 Haftalık Odaklanmış İyileştirme Planımız:
1. Veritabanı sorgularını optimize ederek sayfa yüklenme süresini **1.2 saniyeye** indireceğiz.
2. Ödeme kodunu modüler hale getirerek bir sonraki çeyrekte planlanan 'Apple Pay' entegrasyon süresini **2 haftadan 3 güne** düşüreceğiz.

### 📈 Beklenen İş Getirisi:
- Sepet tamamlama oranında tahmini **%5-%7 ciro artışı**.
- Gelecek sprintlerde yeni özellik teslim hızında **%40 ivmelenme**.""",
            "code_notes_tr": "Bu dille konuşan bir mühendis, şirketin büyümesini dert edinen bir iş ortağıdır. PM bu teklifi reddetmez; tam aksine heyecanla destekler.",
            "code_notes_en": "Framing technical investment around conversion gains and feature delivery velocity positions the engineer as an indispensable business partner rather than a cost center.",
            "pitfalls_tr": [
                {"trap": "Toplantılarda teknik jargona boğulup PM'in veya tasarımcının gözünü korkutmak.", "solution": "Metaforlar, basit analojiler ve kullanıcı deneyimi metrikleriyle konuşun."},
                {"trap": "Tasarımcının çizdiği zor bir UI için 'Bu imkansız, yapılmaz' demek.", "solution": "'Bunu birebir yapmak 3 hafta sürer; ancak şu küçük değişiklikle 2 günde %90 benzerini yapabiliriz' deyin."},
                {"trap": "Şirketin para kazanma modelini (Business Model) hiç merak etmemek.", "solution": "Şirketinizin nereden para kazandığını ve hangi özelliğin ciro getirdiğini mutlaka öğrenin."}
            ],
            "pitfalls_en": [
                {"trap": "Overwhelming non-technical stakeholders with architectural jargon during roadmap planning.", "solution": "Speak in terms of user experience latency, operational budgets, and delivery velocity."},
                {"trap": "Dismissing complex designer mockups with an abrasive 'That is impossible'.", "solution": "Propose compromises: 'Building that exact micro-interaction takes 3 weeks; this alternative delivers 90% of the feel in 2 days.'"},
                {"trap": "Remaining indifferent to company business models and unit economics.", "solution": "Learn how your software generates revenue and which user funnels drive cash flow."}
            ],
            "udemy_title_tr": "Ders 56: Teknik İletişim - Mühendislikten İş Değerine Köprü",
            "udemy_title_en": "Lecture 56: Technical Communication - Translating Code to Business Value",
            "udemy_slides_tr": [
                "Neden şirketler kod için değil, değer için yaşar?",
                "Jargon duvarını yıkmak: Teknik dilden iş diline tercüme.",
                "Tasarımcılar ve PM'lerle 'Yapıcı Takas (Trade-off)' müzakeresi.",
                "Teknik borcu yönetime satma ve onay alma stratejisi."
            ],
            "udemy_slides_en": [
                "Why technology companies optimize for business impact over syntax perfection.",
                "Dismantling the jargon barrier: Translating technical debt into velocity metrics.",
                "Constructive trade-off negotiations with designers and product managers.",
                "Pitching and securing executive approval for technical refactoring sprints."
            ],
            "udemy_demo_tr": "Bir sprint planlama toplantısı canlandırın. 'Kodu yeniden yazmalıyız' diyen mühendis ile 'Bu optimizasyon müşteri dönüşümünü %8 artıracak' diyen mühendisin toplantıdaki etkisini karşılaştırın.",
            "udemy_demo_en": "Role-play a sprint prioritization meeting. Contrast the dismissal of 'we need to rewrite the backend' with the enthusiastic approval of 'this optimization recovers $10k in abandoned carts'.",
            "action_task_tr": "Şirketinizdeki veya projenizdeki bir teknik ihtiyacı alın. Bunu tek bir teknik terim kullanmadan, bir işletme sahibine anlatır gibi 3 cümlelik bir iş teklifine dönüştürün.",
            "action_task_en": "Draft a 3-sentence justification for a technical refactor without using any technical jargon, framing it entirely around risk, velocity, or user satisfaction.",
            "quiz_tr": [
                {
                    "question": "Bir yazılım mühendisi ürün yöneticisine (PM) teknik bir borcu açıklarken hangi yaklaşımı seçmelidir?",
                    "options": [
                        "A) 'Kodlar çok kötü, sen anlamazsın' demek",
                        "B) Teknik borcun geliştirme hızını nasıl yavaşlattığını, yeni özelliklerin çıkış süresini ne kadar geciktirdiğini ve çözüldüğünde şirkete sağlayacağı hız/ciro getirisini anlatmak",
                        "C) Sadece kızgın emojiler atmak",
                        "D) Hiçbir şey söylemeden gizlice kodu değiştirmek"
                    ],
                    "answer": "B",
                    "explanation": "Yöneticiler iş sonuçlarıyla ilgilenir. Teknik borcu geliştirme hızı, hata riski ve finansal getiri üzerinden açıklamak anında onay almanızı sağlar."
                },
                {
                    "question": "Bir tasarımcının sunduğu arayüzü kodlamak çok zorsa profesyonel bir mühendis nasıl yanıt vermelidir?",
                    "options": [
                        "A) 'Bu imkansız, çizimi çöpe at' demek",
                        "B) Tasarımın neden zor olduğunu açıklayıp, aynı kullanıcı hedefine hizmet eden ve çok daha kısa sürede yapılabilecek pratik bir alternatif önermek",
                        "C) Tasarımcıyla küsmek",
                        "D) Çizimi görmezden gelip kafasına göre yapmak"
                    ],
                    "answer": "B",
                    "explanation": "Mühendislik takasları (trade-off) yönetme sanatıdır. 'Olmaz' demek yerine alternatif çözüm sunmak saygı uyandırır."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the most effective approach when pitching technical debt remediation to a Product Manager?",
                    "options": [
                        "A) Stating 'The architecture is ugly, you wouldn't understand'",
                        "B) Framing the debt around velocity drag: demonstrating how it slows future feature delivery and quantifying risk to user retention",
                        "C) Sending angry Slack emojis",
                        "D) Refactoring covertly on nights and weekends"
                    ],
                    "answer": "B",
                    "explanation": "Product managers prioritize business outcomes. Tying technical debt to delivery velocity and revenue risk earns alignment."
                },
                {
                    "question": "How should an engineer respond when a designer presents an unusually complex UI interaction?",
                    "options": [
                        "A) Reject the mockup outright as 'technically impossible'",
                        "B) Explain the implementation cost and propose a lightweight alternative achieving 90% of the UX goal in a fraction of the time",
                        "C) Discontinue communication",
                        "D) Ignore mockups and build an arbitrary layout"
                    ],
                    "answer": "B",
                    "explanation": "Constructive engineering focuses on trade-offs, partnering with designers to find optimal effort-to-impact ratios."
                }
            ]
        },

        # Chapter 57
        {
            "id": 57,
            "section_id": 10,
            "slug_tr": "ch57_ai_ile_portfoy_ve_acik_kaynak_insa_etmek",
            "slug_en": "ch57_building_standout_portfolio_open_source_ai",
            "title_tr": "AI Araçlarıyla Portföy ve Açık Kaynak Projesi İnşa Etmek",
            "title_en": "Building a Standout AI-Enhanced Portfolio & Open Source Contributions",
            "subtitle_tr": "Sıradan 'To-Do App' Projelerini Çöpe Atıp Fark Yaratan İşler Üretmek",
            "subtitle_en": "Retiring Generic Todo Apps and Building Production-Grade Open Source Impact",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "İşe alım yöneticileri neden adayın GitHub'ında 10 tane yarım kalmış tutorial projesi görmekten bıktı ve tek bir gerçek açık kaynak katkısı nasıl iş teklifi getirir?",
            "podcast_hook_en": "Why do tech hiring leads discard resumes showing 10 generic tutorial clones, and how does a single impactful open-source contribution land interview offers?",
            "takeaways_tr": [
                "Tutorial çöplüğü (Tutorial Hell) projeleri (To-Do list, basit klonlar) artık hiçbir şirketi etkilemiyor.",
                "İyi bir portföy projesi: Gerçek bir problemi çözen, canlıda çalışan (deployed), testleri olan ve temiz dokümante edilmiş tek bir projedir.",
                "AI araçları, popüler açık kaynak kütüphanelerindeki (open source) bekleyen hata biletlerini (Issues) analiz edip ilk PR'ınızı açmanızı 10 kat kolaylaştırır."
            ],
            "takeaways_en": [
                "Tutorial clones (generic todo apps, basic calculator apps) convey zero engineering credibility to hiring managers.",
                "A standout portfolio showcases: one deployed, production-grade application solving a real domain problem with automated tests and CI/CD.",
                "AI tooling accelerates open-source impact: digest unfamiliar repositories, reproduce community issues, and author upstream Pull Requests."
            ],
            "story_tr": """Bir resim sergisine gittiğinizi düşünün.

Duvarda 50 tane boyama kitabı sayfası asılı. Çocuklar numaralara göre boyamış: 1 mavi, 2 sarı... O ressamı Louvre Müzesi'ne davet eder misiniz? Asla! Çünkü o sadece başkasının çizgilerini doldurmuştur (Tutorial Hell).

Oysa köşede duran, orijinal, fırça darbeleri kendine has, çerçevesi özenle yapılmış tek bir tablo tüm sergiyi büyüler!

Yazılımda da GitHub profiliniz sizin resim serginizdir. 
YouTube'dan kopyalanmış 20 tane yarım 'Netflix Klonu' yerine; gerçek bir problemi çözen, Docker ile paketlenmiş, testleri yeşil yanan ve canlıda çalışan tek bir açık kaynak araç sizi yüzlerce adayın önüne geçirir.""",
            "story_en": """Visit an art gallery.

Hanging on the wall are 50 generic paint-by-numbers coloring book pages: color 1 blue, color 2 green. Would you invite that painter to exhibit at the Louvre? Never. They merely filled in someone else's contours (Tutorial Hell).

Yet in the corner hangs a single original canvas with textured brushwork, authentic perspective, and meticulous framing. It commands the entire room.

Your GitHub profile is that gallery.
Twenty abandoned YouTube tutorial clones signal mediocrity. A single deployed, well-documented open-source utility solving an authentic developer friction point commands immediate respect from tech leads.""",
            "mental_tr": """İşe Alım Yöneticisini Etkileyen Portföy Formülü:

```
┌────────────────────────────────────────────────────────┐
│               10x PORTFÖY PROJESİ FORMU                │
└──────────────────────────┬─────────────────────────────┘
                           │
  1. GERÇEK PROBLEM: "Geliştiricilerin .env dosyalarındaki eksikleri bulan CLI aracı"
  2. CANLI ÇALIŞMA: Tek tıkla çalışan demo veya npm/pip paketi.
  3. TEST KAPSAMI: Jest testleri ve yeşil yanan GitHub Actions CI rozeti.
  4. MÜKEMMEL README: Mimari şema (Mermaid), kurulum kılavuzu, GIF animasyonu.
  5. TEMİZ GİT GEÇMİŞİ: Conventional Commits standardında 30+ düzenli commit.
```""",
            "mental_en": """The Standout Portfolio Anatomy:

```
┌────────────────────────────────────────────────────────┐
│           ANATOMY OF A COMPELLING PORTFOLIO            │
└──────────────────────────┬─────────────────────────────┘
                           │
  1. REAL-WORLD UTILITY: Solves authentic friction (e.g., automated schema linting).
  2. LIVE PRODUCTION ARTIFACT: Deployed URL or published npm/pip package.
  3. REGRESSION RIGOR: Robust test suite accompanied by a passing CI build badge.
  4. STELLAR DOCUMENTATION: Architectural Mermaid diagram, quickstart, demo GIF.
  5. DISCIPLINED GIT TRAIL: Conventional commits demonstrating iterative maturity.
```""",
            "prompt_tr": """# ROL: Açık Kaynak Topluluk Lideri ve Portföy Danışmanı
GitHub'da açık kaynak bir CLI aracı yayınlayacağız. Proje: 'Git commit mesajlarını analiz edip Conventional Commits standartlarına uygunluğunu denetleyen linter'.

## GÖREV:
1. Bu proje için dünya standartlarında, rozetler (Badges) ve Mermaid diyagramı içeren bir `README.md` şablonu hazırla.
2. Açık kaynak projelere ilk katkıyı (First Contribution) yapmak için 'Good First Issue' etiketli biletleri AI ile nasıl çözeceğimi planla.
3. Bir iş görüşmesinde bu projeyi anlatırken öne çıkarılacak 3 mimari noktayı belirle.""",
            "prompt_en": """# ROLE: Open Source Maintainer & Career Strategist
We are launching an open-source CLI utility: a linter validating Git commit messages against the Conventional Commits specification.

## TASK:
1. Author a world-class `README.md` featuring build badges, quickstart docs, and a Mermaid flow diagram.
2. Provide a tactical workflow for triaging and resolving 'Good First Issue' tickets across major open-source repositories via AI.
3. Formulate the technical narrative highlighting architectural decisions for interviews.""",
            "code_lang": "markdown",
            "code_naive": """# commit-linter
Bu proje commitleri kontrol eder.
Kurmak icin npm install yazin.""",
            "code_robust": """# 🛡️ CommitShield: Intelligent Conventional Commit Linter

[![CI Quality Gate](https://github.com/username/commit-shield/actions/workflows/ci.yml/badge.svg)](https://github.com)
[![npm version](https://badge.fury.io/js/commit-shield.svg)](https://badge.fury.io/js/commit-shield)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

**CommitShield**, Git commit mesajlarınızı Conventional Commits standartlarına göre AST seviyesinde denetleyen, hafif ve sıfır bağımlılıklı bir CLI aracıdır.

---

## ⚡ Hızlı Kurulum

```bash
# Global Kurulum
npm install -g commit-shield

# Git Pre-commit Hook Olarak Ekleme
commit-shield install-hook
```

---

## 🏗️ Mimari Akış Şeması

```mermaid
flowchart LR
    A[git commit] --> B[CommitShield CLI]
    B --> C{Geçerli Format mı?}
    C -->|Evet| D[✅ Commit Kabul Edildi]
    C -->|Hayır| E[❌ Hata: Conventional Commit Kuralı İhlali]
```

---

## 🧪 Testler ve Doğrulama
```bash
npm test -- --coverage # %98 Birim Test Kapsamı
```""",
            "code_notes_tr": "Böyle bir README, CI rozetleri ve Mermaid şeması gören bir işe alım lideri adayın kodlama kalitesinden ve profesyonelliğinden anında emin olur.",
            "code_notes_en": "A repository presenting automated CI badges, interactive Mermaid architecture diagrams, and comprehensive quickstart instructions stands out in the top 1% of applicant pools.",
            "pitfalls_tr": [
                {"trap": "GitHub'da sadece ödev veya YouTube klon projeleri barındırmak.", "solution": "Profilinizi temizleyin; sadece gurur duyduğunuz en iyi 2-3 projeyi 'Pinned' (Sabitlenmiş) yapın."},
                {"trap": "README dosyası olmayan veya sadece 'Proje Başlığı' yazan boş repolar bırakmak.", "solution": "README projenizin vitrinidir; ekran görüntüleri, kurulum adımları ve test rozetleri ekleyin."},
                {"trap": "Açık kaynak projelere sadece dokümantasyondaki bir harf hatasını düzelterek katkı yapmaya çalışmak.", "solution": "'Good First Issue' etiketli gerçek bir bug'ı testleriyle birlikte çözerek değer üretin."}
            ],
            "pitfalls_en": [
                {"trap": "Pinning unfinished, unmaintained tutorial repositories on your public GitHub profile.", "solution": "Curate your profile: showcase 2 or 3 polished, deployed, and tested flagships."},
                {"trap": "Neglecting repository README documentation.", "solution": "The README is your resume's landing page: include visual demos, architecture diagrams, and test badges."},
                {"trap": "Limiting open-source contributions to trivial typo fixes in markdown files.", "solution": "Tackle 'Good First Issue' defects containing test assertions to demonstrate real engineering capability."}
            ],
            "udemy_title_tr": "Ders 57: Portföy ve Açık Kaynak - Fark Yaratan Mühendis Olmak",
            "udemy_title_en": "Lecture 57: Standout Portfolios & Open Source Contributions",
            "udemy_slides_tr": [
                "Neden 'To-Do App' projeleri artık kimseyi etkilemiyor?",
                "Mükemmel bir GitHub portföyünün 5 bileşeni.",
                "AI kullanarak açık kaynak projelere ilk PR'ı açma kılavuzu.",
                "Vitrin oluşturma: Mükemmel README ve mimari diyagramlar."
            ],
            "udemy_slides_en": [
                "Why generic tutorial clones destroy applicant credibility.",
                "The 5 structural pillars of a high-impact GitHub portfolio.",
                "Leveraging AI to parse issues and author your first upstream open-source PR.",
                "Curating your engineering storefront: Stellar READMEs and diagrams."
            ],
            "udemy_demo_tr": "GitHub'da açık kaynaklı bir depodaki (örn: Express veya Fastify) bir 'Good First Issue' biletini açın. AI asistanına bu hatayı analiz ettirip test senaryosunu nasıl hazırlayacağınızı canlı gösterin.",
            "udemy_demo_en": "Navigate to a well-known open-source repository issue tracker. Filter by 'good-first-issue'. Use AI to dissect the issue description, replicate the bug locally, and scaffold a proposed fix.",
            "action_task_tr": "GitHub profilinizdeki en iyi projenizi seçin. Ona profesyonel bir `README.md`, rozetler (badges) ve bir Mermaid akış şeması ekleyin.",
            "action_task_en": "Select your strongest personal project and overhaul its `README.md` with an architectural diagram, CI status badge, and clear local quickstart steps.",
            "quiz_tr": [
                {
                    "question": "İşe alım yapan bir teknoloji liderinin bir adayın GitHub profilinde en çok görmek istediği şey nedir?",
                    "options": [
                        "A) 100 farklı yarım bırakılmış tutorial klonu",
                        "B) Gerçek bir problemi çözen, testleri olan, CI/CD boru hattı yeşil yanan ve canlıda çalışan 1-2 adet yüksek kaliteli proje",
                        "C) Profil resminin yapay zeka olması",
                        "D) Sadece yeşil commit kutuları"
                    ],
                    "answer": "B",
                    "explanation": "Kıdemli mühendisler niceliğe değil niteliğe bakar; canlıda çalışan ve testleri olan tek bir proje, 50 yarım klondan katbekat değerlidir."
                },
                {
                    "question": "Açık kaynak (Open Source) projelere yeni başlayan geliştiricilerin araması önerilen standart etiket hangisidir?",
                    "options": [
                        "A) critical-emergency",
                        "B) good first issue (veya beginner-friendly)",
                        "C) do-not-touch",
                        "D) linux-kernel-only"
                    ],
                    "answer": "B",
                    "explanation": "`good first issue`, proje yöneticilerinin topluluğa yeni katılan geliştiricilerin kolayca çözebileceği şekilde etiketlediği başlangıç seviyesi biletlerdir."
                }
            ],
            "quiz_en": [
                {
                    "question": "What portfolio signal most impresses an engineering hiring manager?",
                    "options": [
                        "A) 100 half-finished tutorial forks",
                        "B) 1 or 2 polished, tested, and deployed applications solving authentic problems with passing CI checks and disciplined git commits",
                        "C) AI-generated avatar pictures",
                        "D) Raw green commit contribution counts"
                    ],
                    "answer": "B",
                    "explanation": "Engineering managers evaluate quality over quantity: a single tested, deployed application proves production readiness far beyond fifty cloned projects."
                },
                {
                    "question": "Which standard GitHub label denotes issues optimized for new open-source contributors?",
                    "options": [
                        "A) `critical-emergency`",
                        "B) `good first issue` (or `help wanted`)",
                        "C) `wontfix`",
                        "D) `core-architecture-only`"
                    ],
                    "answer": "B",
                    "explanation": "`good first issue` flags isolated, well-specified problems curated by maintainers to onboard new community contributors."
                }
            ]
        },

        # Chapter 58
        {
            "id": 58,
            "section_id": 10,
            "slug_tr": "ch58_ai_caginda_teknik_mulakatlara_hazirlik",
            "slug_en": "ch58_acing_technical_and_system_design_interviews",
            "title_tr": "AI Çağında Teknik Mülakatlara Hazırlık: Live Coding & System Design",
            "title_en": "Navigating Technical Interviews in the AI Era: Live Coding & System Design",
            "subtitle_tr": "Ezber LeetCode Sorularından Zihniyeti ve Akıl Yürütmeyi Kanıtlama Sanatına",
            "subtitle_en": "Moving Beyond Rote LeetCode: Demonstrating Thought Process and Architecture Under Pressure",
            "level_tr": "İleri Seviye",
            "level_en": "Advanced",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Yapay zeka tüm LeetCode sorularını 2 saniyede çözebiliyorsa, modern teknoloji şirketleri teknik mülakatlarda artık neyi ölçüyor?",
            "podcast_hook_en": "If modern LLMs solve LeetCode algorithms in 3 seconds, what are top-tier engineering companies actually evaluating in modern technical interviews?",
            "takeaways_tr": [
                "Mülakat yapanlar ezberlediğiniz cevabı değil; belirsizlik altında nasıl akıl yürüttüğünüzü (Thinking Out Loud) görmek ister.",
                "AI çağında mülakatlar 'kod yazma' testinden 'kod denetleme, mimari tasarım ve trade-off tartışma' sınavına dönüşmüştür.",
                "Sessiz kalıp kod yazmak elenme sebebidir; düşündüğünüz her hipotezi ve kenar durumu mülakatçıyla sesli paylaşın."
            ],
            "takeaways_en": [
                "Interviewers are not evaluating syntax recall; they are measuring how you reason through ambiguity under pressure (Thinking Out Loud).",
                "In the AI era, interviews have shifted from mechanical coding to architectural trade-off debates and adversarial code audits.",
                "Working in total silence is an immediate red flag; communicate trade-offs, constraints, and edge cases collaboratively."
            ],
            "story_tr": """Bir pilot iş mülakatına girdiğinizi düşünün.

Havayolu şirketi pilot adayına: *"Bana uçağın hidrolik pompasının içindeki vidanın diş sayısını ezbere söyle"* der mi? Hayır!
Onu uçuş simülatörüne (Flight Simulator) oturturlar. Motorlardan biri alev aldığında pilotun nasıl sakin kaldığına, kuleyle nasıl iletişim kurduğuna ve acil durum prosedürlerini adım adım nasıl uyguladığına bakarlar!

Teknik mülakatlar da o uçuş simülatörüdür.

Mülakatçı size bir problem verdiğinde: *"Hemen sessizce kod yazayım, doğru cevabı çıkarayım"* derseniz kaybedersiniz. 
Mülakatçının görmek istediği:
- Soruyu netleştirmek için hangi soruları soruyorsunuz?
- Sınır durumları hesaba katıyor musunuz?
- Fikirlerinizi sesli olarak nasıl ifade ediyorsunuz?""",
            "story_en": """Consider an airline interview for a commercial pilot position.

Does the flight panel ask the candidate: *"Recite from memory the serial number of the hydraulic bolt in the rudder"?* Never.
They place the candidate inside a full-motion Flight Simulator. They kill Engine 2 in heavy turbulence and observe how the pilot manages panic, communicates with air traffic control, and works through emergency checklists.

Technical interviews are that exact flight simulator.

Rushing into silent syntax typing is the fastest path to rejection.
The hiring committee evaluates:
- Do you ask clarifying questions to expose hidden constraints?
- Do you articulate trade-offs between space and time?
- Do you treat the interviewer as a collaborative engineering teammate?""",
            "mental_tr": """Mülakatta Başarı Formülü: REACTO Metodu

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
```""",
            "mental_en": """The REACTO Technical Interview Framework:

```
1. REPEAT: Restate the problem statement to confirm alignment on requirements.
2. EXAMPLES: Formulate 3 test inputs (nominal case, empty input, boundary case).
3. APPROACH: Verbally contrast multiple approaches: "We can solve this via O(N^2) brute force or O(N) hash map; I recommend the latter because..."
4. CODE: Write clean, idiomatic, typed code with descriptive identifiers.
5. TEST: Walk through your code line-by-line using your example inputs before declaring completion.
6. OPTIMIZE: Conclude with definitive Big-O time and space complexity evaluations.
```""",
            "prompt_tr": """# ROL: FAANG / Tier-1 Şirket Kıdemli Mülakatçısı
Ben mülakata giren bir junior yazılım mühendisiyim. Bana 'Canlı Kodlama ve Sistem Tasarımı' mülakatı simülasyonu yapacaksın.

## MÜLAKAT KURALLARI:
1. Bana gerçekçi, orta zorlukta bir problem sor (Örn: URL Kısaltıcı Servis veya Rate Limiter tasarımı).
2. Doğrudan çözümü söyleme; sadece benim sorduğum netleştirme sorularına yanıt ver.
3. Çözümümü REACTO metoduna göre (İletişim, Edge Caseler, Big-O Analizi) puanla ve yapıcı geri bildirim ver.""",
            "prompt_en": """# ROLE: Staff Software Engineer & Interview Bar Raiser
You are conducting a live System Design and Coding interview with me.

## INTERVIEW PROTOCOL:
1. Present a realistic, medium-difficulty challenge (e.g., designing an in-memory distributed Rate Limiter).
2. Do not reveal solutions; respond strictly to my clarifying constraint inquiries.
3. Score my performance using the REACTO rubric (Communication, Edge Case Rigor, Clean Architecture, Big-O Analysis).""",
            "code_lang": "typescript",
            "code_naive": """// Mülakatta Elenme Sebebi: Sessizce oturup kontrolsüz kod yazmak
function solve(a: any, b: any) {
  // Mülakatçı ne yaptığınızı bilmiyor, değişken isimleri anlamsız, edge case yok!
  let x = [];
  for (let i = 0; i < a.length; i++) { x.push(a[i] + b); }
  return x;
}""",
            "code_robust": """// Mülakat Kazandıran Kod: İletişimli, Tip Güvenli, Sınır Değerleri Kontrollü
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
}""",
            "code_notes_tr": "Mülakatçıya iki işaretçi (Two-Pointer) yaklaşımının neden O(N+M) zaman karmaşıklığıyla sıralama fonksiyonlarından (`sort`: O(N log N)) daha üstün olduğu sesli olarak açıklanır.",
            "code_notes_en": "Articulating why the Two-Pointer pattern achieves linear O(N+M) complexity over standard sorting (`sort()`: O(N log N)) proves foundational algorithmic mastery under pressure.",
            "pitfalls_tr": [
                {"trap": "Soruyu alır almaz hiç düşünmeden ve soru sormadan klavyeye sarılmak.", "solution": "İlk 3-5 dakikayı sorular sorarak, sınır durumları netleştirerek geçirin."},
                {"trap": "Mülakat esnasında dakikalarca tamamen sessiz kalmak.", "solution": "Zihninizden geçenleri sesli düşünün: 'Şu an bir döngü kurmayı düşünüyorum çünkü...'"},
                {"trap": "Kodu bitirir bitirmez 'bitti' demek.", "solution": "Kodu mülakatçıya teslim etmeden önce bir örnek girdiyle satır satır kendi kendinize test edin."}
            ],
            "pitfalls_en": [
                {"trap": "Jumping into code without asking clarifying boundary questions.", "solution": "Spend the first 3-5 minutes clarifying constraints, data volume, and null expectations."},
                {"trap": "Falling into extended periods of silence while problem-solving.", "solution": "Think out loud: 'I am weighing a hash set against a binary search because memory is constrained...'"},
                {"trap": "Declaring 'I am done' without manually tracing code execution.", "solution": "Step through your implementation with sample inputs before handing control back to the interviewer."}
            ],
            "udemy_title_tr": "Ders 58: AI Çağında Teknik Mülakatlar - REACTO Metodu",
            "udemy_title_en": "Lecture 58: Technical Interviews in the AI Era - The REACTO Method",
            "udemy_slides_tr": [
                "LeetCode ezberciliğinin sonu: Şirketler artık neyi ölçüyor?",
                "REACTO Metodu: Mülakatta adım adım kazanma stratejisi.",
                "Sesli Düşünme (Thinking Out Loud) sanatı.",
                "Canlı Mülakat Simülasyonu: Two-Pointer algoritması üzerinden vaka."
            ],
            "udemy_slides_en": [
                "The demise of rote algorithm trivia: What companies evaluate today.",
                "The REACTO framework: Step-by-step interview execution.",
                "Mastering the 'Thinking Out Loud' discipline.",
                "Live mock interview: Navigating an algorithmic challenge collaboratively."
            ],
            "udemy_demo_tr": "AI'ı mülakatçı rolüne sokun. Bir LeetCode orta seviye soru isteyin. Sesli düşünerek promptlar yazın; AI'ın sınır durum sorularınızı nasıl yanıtladığını ve sizi nasıl puanladığını canlı gösterin.",
            "udemy_demo_en": "Prompt an AI model into Interviewer Mode. Work through an algorithm step-by-step using the REACTO protocol, demonstrating how asking clarifying questions shifts the interview evaluation.",
            "action_task_tr": "Bugün AI asistanınıza: 'Bana orta seviye bir algoritma mülakatı simülasyonu yap' deyin ve REACTO metodunu uygulayarak bir mülakat simülasyonunu tamamlayın.",
            "action_task_en": "Run a 30-minute mock technical interview with an AI model using the REACTO methodology, practicing thinking out loud throughout.",
            "quiz_tr": [
                {
                    "question": "Teknik bir mülakatta bir soruyu çözmeye başlamadan önce yapılması gereken en doğru ilk adım nedir?",
                    "options": [
                        "A) Hemen hızlıca kod yazmaya başlamak",
                        "B) Problemi kendi cümlelerinizle tekrar edip, girdi sınırları ve edge caseler hakkında netleştirici sorular sormak",
                        "C) Mülakatçıdan cevabı istemek",
                        "D) Bilgisayarı yeniden başlatmak"
                    ],
                    "answer": "B",
                    "explanation": "Mülakatçılar gerçek dünyadaki gibi belirsiz problemler verir; iyi bir mühendis önce sorular sorarak gereksinimleri netleştirir."
                },
                {
                    "question": "Mülakatta kod yazmayı bitirdikten hemen sonra yapılması gereken profesyonel hareket nedir?",
                    "options": [
                        "A) 'Bitti' deyip susmak",
                        "B) Mülakatçının test etmesini beklemeden, belirlediğiniz örnek bir girdiyle kodu satır satır kendi kendinize çalıştırıp (dry run) doğrulamak",
                        "C) Kodu silmek",
                        "D) Odayı terk etmek"
                    ],
                    "answer": "B",
                    "explanation": "Kendi kodunu test eden mühendis, yazdığı işe sahip çıktığını ve dikkatli olduğunu kanıtlar; mülakatçının puanını en çok artıran adımdır."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the mandatory first step when presented with an algorithmic problem in a technical interview?",
                    "options": [
                        "A) Typing code immediately at high speed",
                        "B) Restating the problem and asking clarifying questions regarding data volume, constraints, and edge cases",
                        "C) Asking the interviewer for the solution",
                        "D) Rebooting your laptop"
                    ],
                    "answer": "B",
                    "explanation": "Senior engineers clarify specifications and constraints before building; jumping straight to syntax signals inexperience."
                },
                {
                    "question": "Upon completing an implementation during a live coding interview, what should you do immediately?",
                    "options": [
                        "A) Announce 'Done' and wait in silence",
                        "B) Manually trace through the implementation step-by-step using sample inputs and boundary cases to audit correctness",
                        "C) Erase the whiteboard or buffer",
                        "D) Exit the room"
                    ],
                    "answer": "B",
                    "explanation": "Self-testing your code demonstrates disciplined verification rigor, catching subtle off-by-one errors before the interviewer flags them."
                }
            ]
        },

        # Chapter 59
        {
            "id": 59,
            "section_id": 10,
            "slug_tr": "ch59_surekli_ogrenme_ve_teknoloji_yorgunlugunu_asmak",
            "slug_en": "ch59_the_lifelong_learning_engine_beating_burnout",
            "title_tr": "Sürekli Öğrenme Sistemi: Değişen Teknolojide Geri Kalmama Formülü",
            "title_en": "The Lifelong Learning Engine: Beating Tech Churn & Burnout with AI",
            "subtitle_tr": "Her Hafta Yeni Bir Framework Çıkarken Akıl Sağlığını Korumak",
            "subtitle_en": "Focusing on Timeless Fundamentals While Every Framework Churns Around You",
            "level_tr": "İleri Seviye",
            "level_en": "Advanced",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Her ay yeni bir JavaScript framework'ü veya yeni bir AI modeli çıkıyor. Bir mühendis tükenmişlik (burnout) yaşamadan nasıl her zaman güncel kalabilir?",
            "podcast_hook_en": "With novel frameworks launching every Tuesday, how does an engineer cultivate a lifelong learning system without descending into chronic tech fatigue and burnout?",
            "takeaways_tr": [
                "Teknolojiler değişir, prensipler kalıcıdır. React veya Vue gelip geçicidir; veri yapıları, HTTP ve temiz mimari ebedidir.",
                "T-Shaped Mühendislik: Bir alanda çok derin uzmanlık (T'nin dikey çizgisi), diğer alanlarda genel vizyon (T'nin yatay çizgisi).",
                "Haftalık 'Öğrenme Radarı' kurarak yapay zekayı haftalık teknoloji özetleyiciniz haline getirin."
            ],
            "takeaways_en": [
                "Technologies churn; foundational principles endure. Libraries come and go; data structures, networking protocols, and architecture remain eternal.",
                "The T-Shaped Engineer: Deep, specialized mastery in one vertical discipline, paired with broad working literacy across adjacent domains.",
                "Deploy AI as your personal research synthesizer to curate weekly technical whitepapers and eliminate information overload."
            ],
            "story_tr": """Okyanustaki dalgaları düşünün.

Her gün binlerce dalga gelir, köpürür, kıyıya vurur ve yok olur. Bir sörfçü her gelen küçük dalgaya atlamaya çalışırsa 1 saatte yorulur, nefesi tükenir ve boğulur! (Teknoloji Yorgunluğu / Hype Chasing).

Usta bir sörfçü ne yapar? Okyanusun derinliklerindeki ana akıntıları (Currents) okur. Küçük köpüklere aldırmaz; arkadan gelen devasa ve güçlü dalgayı bekler ve üzerinde ustalıkla kayar.

Yazılımda o küçük dalgalar her hafta çıkan yeni kütüphanelerdir. 
Okyanusun derin dip akıntıları ise:
- Veri Yapıları ve Algoritmalar
- Dağıtık Sistemler Mimarisi
- Ağ Protokolleri (TCP, HTTP)
- İş Problemlerini Çözme Becerisi

Temellere odaklanan bir mühendis, teknoloji ne kadar değişirse değişsin asla boğulmaz.""",
            "story_en": """Consider ocean breakers crashing on a reef.

Thousands of frothing waves churn, break, and dissipate hourly. If a surfer paddles furiously after every tiny ripple, they exhaust their physical stamina within 45 minutes and drown (Hype-Chasing Burnout).

A master surfer monitors deep tidal currents. They disregard surface froth, positioning themselves calmly to ride the massive swell forming underneath.

In software engineering, surface froth is the endless churn of trendy frontend micro-libraries.
The deep oceanic currents are:
- Data structures and algorithms
- Operating systems and memory models
- Networking protocols (TCP/IP, HTTP)
- Architectural problem-solving

An engineer anchored in timeless primitives never drowns in the shifting tides of tech hype.""",
            "mental_tr": """T-Shaped Mühendis Modeli:

```
        ┌────────────────────────────────────────────────────────┐
        │       GENEL VİZYON (Geniş Bilgi - T'nin Yatayı)        │
        │ Docker, AWS, SQL, Güvenlik, CI/CD, Frontend, LLM Temel │
        └──────────────────────────┬─────────────────────────────┘
                                   │
                                   │  DERİN UZMANLIK
                                   │  (T'nin Dikeyi)
                                   ▼
                        [TypeScript / Backend Mimarisi]
                        - Performans Tuning
                        - Karmaşık İş Mantığı
                        - Derin Kütüphane Bilgisi
```""",
            "mental_en": """The T-Shaped Engineering Archetype:

```
        ┌────────────────────────────────────────────────────────┐
        │       BROAD WORKING LITERACY (Horizontal Bar)          │
        │ Docker, AWS, SQL, Security, CI/CD, CSS, Cloud, LLMs    │
        └──────────────────────────┬─────────────────────────────┘
                                   │
                                   │  DEEP SPECIALIZATION
                                   │  (Vertical Pillar)
                                   ▼
                         [High-Throughput Systems]
                         - Advanced concurrency models
                         - Performance profiling & indexing
                         - Distributed data pipelines
```""",
            "prompt_tr": """# ROL: Baş Teknoloji Yöneticisi (CTO) ve Yaşam Boyu Öğrenme Koçu
Yazılım dünyasındaki hızlı değişim karşısında tükenmişlik (burnout) hissetmeden sürdürülebilir bir 'Kişisel Gelişim Sistemi' kurmak istiyorum.

## GÖREV:
1. 'FOMA (Fear of Missing Out - Geri Kalma Korkusu)' tuzağından kurtulmak için hangi teknolojileri derinlemesine, hangilerini sadece genel kültür olarak öğrenmem gerektiğini filtreleyen karar matrisini kur.
2. Haftada sadece 3 saat ayırarak güncel kalmayı sağlayan 'Haftalık Öğrenme Rutini' tasarla.
3. Bir makale veya yeni teknolojiyi yapay zekaya 5 dakikada 'İlk İlkeler (First Principles)' seviyesinde özetletme promptu oluştur.""",
            "prompt_en": """# ROLE: VP of Engineering & Lifelong Learning Mentor
I want to establish a sustainable, burnout-proof professional learning system.

## TASK:
1. Provide a decision heuristic filtering which technologies merit deep mastery vs. which warrant passive awareness.
2. Design a structured 3-hour weekly learning ritual preserving mental health while staying competitive.
3. Author a First-Principles prompt template that extracts the timeless architectural essence of any new technology in 5 minutes.""",
            "code_lang": "markdown",
            "code_naive": """# Kötü / Yoran Öğrenme Yaklaşımı:
Twitter'da gördüğüm her yeni kütüphaneyi hemen indirip gece 3'e kadar tutorial izlemek!
(2 hafta sonra yorgunluktan kod yazamaz hale gelmek...)""",
            "code_robust": """# Sürdürülebilir Öğrenme Sistemi: 3 Saatlik Haftalık Blok

## 📅 Haftalık Öğrenme Rutini (Haftada 3 Saat):
- **Cuma 16:00 - 17:00 (1 Saat - Radar Taraması):**
  - AI ile sektör bültenlerini özetlet (Changelog, Hacker News, InfoQ).
  - Sadece "Bu teknoloji bizim hangi problemimizi çözer?" sorusuna yanıt ara.

- **Cumartesi 10:00 - 12:00 (2 Saat - Derin Prototip):**
  - Seçilen tek bir kavramı (Örn: Redis Pub/Sub veya WebAssembly) izole bir repoda kodla dene.
  - Notlarını kendi dijital bahçene (Obsidian / GitHub) markdown olarak kaydet.

## 🤖 AI 'İlk İlkeler (First Principles)' Promptu:
"Aşağıdaki yeni duyurulan teknolojiyi açıkla:
1. Hangi temel fiziksel/mimari darboğazı çözmek için icat edildi?
2. 20 yıl önceki hangi klasik bilgisayar bilimi kavramının modern bir uygulamasıdır?
3. Bu teknolojinin arkasındaki temel ödünleşim (Trade-off: Neyi feda ediyor?) nedir?" """,
            "code_notes_tr": "Yeni çıkan her aracı değil, arkasındaki bilgisayar bilimi prensiplerini anlamak; 10 yıl sonra da dimdik ayakta kalan bir mühendis olmanın sırrıdır.",
            "code_notes_en": "Decoupling timeless computer science principles from ephemeral tooling names guarantees intellectual durability. Master the fundamentals, and every new framework feels familiar in an afternoon.",
            "pitfalls_tr": [
                {"trap": "Hype peşinde koşup her yeni aracı hemen şirket projelerine entegre etmeye çalışmak.", "solution": "Yeni araçları önce kişisel projelerinizde (sandbox) deneyin; olgunlaşmadan prod'a sokmayın."},
                {"trap": "Sürekli tutorial izleyip tek satır bağımsız kod yazmamak (Tutorial Hell).", "solution": "İzlediğiniz her 30 dakikalık içerik için mutlaka 1 saat kendi başınıza kod yazın."},
                {"trap": "Dinlenmeyi ve uyku düzenini ihmal ederek tükenmişlik (burnout) yaşamak.", "solution": "Yazılımcılık bir maratondur, 100 metre koşusu değil; düzenli dinlenme en büyük üretkenlik aracıdır."}
            ],
            "pitfalls_en": [
                {"trap": "Chasing tech hype and pushing unvetted, experimental libraries directly into production repos.", "solution": "Experiment in local scratch sandboxes; mandate ecosystem maturity before production adoption."},
                {"trap": "Passive consumption without active synthesis (Tutorial Hell).", "solution": "Pair every 30 minutes of video consumption with 60 minutes of unassisted coding."},
                {"trap": "Sacrificing sleep, exercise, and mental recovery in an unsustainable sprint toward burnout.", "solution": "Software engineering is a 40-year endurance marathon; recovery is a prerequisite for sharp reasoning."}
            ],
            "udemy_title_tr": "Ders 59: Sürekli Öğrenme ve Teknoloji Yorgunluğunu Aşmak",
            "udemy_title_en": "Lecture 59: Lifelong Learning - Conquering Tech Churn & Burnout",
            "udemy_slides_tr": [
                "Neden teknolojiler değişir ama prensipler kalıcıdır?",
                "T-Shaped Mühendislik: Derinlik ve genişlik dengesi.",
                "Haftada 3 saat ile tükenmeden güncel kalma rutini.",
                "Yapay zekayı kişisel araştırma ve özetleme asistanı yapmak."
            ],
            "udemy_slides_en": [
                "Why frameworks churn while fundamental principles endure.",
                "The T-Shaped engineering model: Striking breadth and depth balance.",
                "The 3-hour weekly sustainable learning cadence.",
                "Leveraging AI as a personal research synthesizer to distill whitepapers."
            ],
            "udemy_demo_tr": "Karmaşık 40 sayfalık teknik bir dökümanı (örneğin Raft Consensus algoritması) AI'a verin. 'İlk İlkeler (First Principles) promptu' ile konunun özünü 2 dakikada çıkardığını ve nasıl kalıcı öğrenileceğini canlı gösterin.",
            "udemy_demo_en": "Feed a dense whitepaper into an AI model using the First-Principles prompt template. Demonstrate distilling decades of distributed systems concepts into three foundational invariants in 2 minutes.",
            "action_task_tr": "Bu hafta takviminizde sadece 2 saatlik kesintisiz bir 'Öğrenme Bloğu' ayırın ve uzun zamandır merak ettiğiniz bir temel konuyu (örn: veritabanı indeksleri nasıl çalışır) kodla deneyin.",
            "action_task_en": "Block 2 hours on your calendar this week for uninterrupted exploration: prototype one fundamental concept (e.g., building a toy B-Tree or mini HTTP server) in isolation.",
            "quiz_tr": [
                {
                    "question": "'T-Shaped Mühendis' kavramı neyi ifade eder?",
                    "options": [
                        "A) Sadece T harfiyle başlayan dilleri bilen kişiyi",
                        "B) Bir alanda çok derin uzmanlığa (T'nin dikey bacağı) sahipken, diğer ilgili mühendislik disiplinlerinde de genel vizyon ve iletişim yeteneğine (T'nin yatay çizgisi) sahip olan mühendisi",
                        "C) Sadece tişört giyen yazılımcıyı",
                        "D) Monitörü dikey kullanan kişiyi"
                    ],
                    "answer": "B",
                    "explanation": "T-Shaped mühendisler hem kendi ana uzmanlıklarında yüksek katma değer üretir hem de DevOps, frontend, backend gibi komşu ekiplerle kusursuz işbirliği yapar."
                },
                {
                    "question": "Hızla değişen yazılım teknolojileri karşısında tükenmişlik (burnout) yaşamamanın en sağlam kalkanı nedir?",
                    "options": [
                        "A) Tüm yeni çıkan teknolojileri aynı anda öğrenmeye çalışmak",
                        "B) Geçici kütüphaneler yerine değişmeyen temel prensiplere (Veri yapıları, Algoritmalar, Ağ, Mimari) odaklanmak",
                        "C) Yazılımcılığı bırakmak",
                        "D) Sadece gece çalışmak"
                    ],
                    "answer": "B",
                    "explanation": "Temel bilgisayar bilimi prensiplerini sağlam öğrenen bir mühendis için yeni çıkan diller veya framework'ler sadece birkaç günlük söz dizimi (syntax) adaptasyonundan ibarettir."
                }
            ],
            "quiz_en": [
                {
                    "question": "What defines the 'T-Shaped Engineer' industry archetype?",
                    "options": [
                        "A) Developers working exclusively in languages starting with T",
                        "B) Deep vertical expertise in one primary discipline, complemented by broad working literacy across adjacent engineering systems",
                        "C) Engineers who wear corporate apparel",
                        "D) Using vertical monitors exclusively"
                    ],
                    "answer": "B",
                    "explanation": "T-shaped professionals deliver outsized impact in their vertical specialty while collaborating frictionlessly across full-stack domains."
                },
                {
                    "question": "What is the most effective operational defense against technology churn and engineering burnout?",
                    "options": [
                        "A) Attempting to master every trending framework simultaneously",
                        "B) Anchoring your learning in timeless computer science primitives (data structures, protocols, architecture) rather than chasing ephemeral syntax",
                        "C) Quitting software engineering",
                        "D) Working exclusively at night"
                    ],
                    "answer": "B",
                    "explanation": "Mastering enduring principles makes learning new libraries trivial: novel tools become predictable variations of familiar foundational concepts."
                }
            ]
        },

        # Chapter 60
        {
            "id": 60,
            "section_id": 10,
            "slug_tr": "ch60_mezuniyet_ve_manifesto_orkestra_sefi",
            "slug_en": "ch60_graduation_manifesto_the_conductor_of_ai",
            "title_tr": "Mezuniyet ve Manifesto: AI'ın Efendisi Olan Yeni Nesil Mühendis",
            "title_en": "Graduation Manifesto: Becoming the Conductor of the AI Symphony",
            "subtitle_tr": "Yapay Zekanın Değiştiremediği Tek Şey: İnsan Merakı, Vizyonu ve Yargı Yeteneği",
            "subtitle_en": "The Irreplaceable Human Core: Curiosity, Architectural Judgment, and Vision",
            "level_tr": "Uzmanlık Seviyesi",
            "level_en": "Expert Mastery",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "60 bölümlük bu yolculuğun sonunda: Yapay zeka yazılımcıların yerini mi alacak, yoksa yapay zekayı bir orkestra gibi yöneten mühendisler diğer herkesin yerini mi alacak?",
            "podcast_hook_en": "At the conclusion of our 60-chapter odyssey: Will AI replace software engineers, or will engineers who master AI orchestration replace everyone who refused to adapt?",
            "takeaways_tr": [
                "Geleceğin kazananı yapay zekadan korkanlar değil; yapay zekayı bir enstrüman gibi çalan 'Orkestra Şefi Mühendisler'dir.",
                "Kodlama araçları ne kadar gelişirse gelişsin; empati kurma, problem tanımlama ve etik karar alma yeteneği daima insana aittir.",
                "Bu kitap bir son değil; ömür boyu sürecek merak, üretim ve ustalık yolculuğunuzun ilk adımıdır."
            ],
            "takeaways_en": [
                "The future belongs neither to Luddites who reject AI nor to passive bystanders, but to proactive Conductors orchestrating AI agents.",
                "No matter how capable models become, empathy, problem formulation, ethical responsibility, and taste remain uniquely human.",
                "This book is not a finish line; it is the launchpad for a lifetime of curiosity, creation, and engineering craftsmanship."
            ],
            "story_tr": """Kitabımızın 1. bölümündeki o ilk günü hatırlıyor musunuz? 
Ekranda yanıp sönen o yalnız imleç ve kulağınızdaki fısıltı: *"Yazılımcılık bitti mi?"*

Şimdi arkanıza yaslanın ve geçtiğiniz 60 bölümlük yolu izleyin:
- Algoritmaları sözde kodla tasarladınız.
- Big-O ile darboğazları ezdiniz.
- Git ile çatışmaları çözüp CI/CD boru hatları kurdunuz.
- Modüler monolitler ve tasarım kalıplarıyla sistemleri ölçeklendirdiniz.
- Veritabanlarında indekslerle sorguları 5 milisaniyeye indirdiniz.
- Test Piramidi ile kurşun geçirmez kalkanlar ördünüz.
- Post-Mortem ile hatalardan bilgelik ürettiniz.
- Ve güvenlik duvarlarıyla sistemleri siber saldırılara karşı kilitlediniz.

Gördünüz mü? Yazılımcılık ölmedi.
Yazılımcılık kabuk değiştirdi! Klavye hamallığından, milyarlarca parametreli yapay zeka modellerini yöneten bir **Orkestra Şefliğine** yükseldi.

Baget artık sizin elinizde. Sahneye çıkın ve dünyanın en güzel yazılım senfonisini besteleyin!""",
            "story_en": """Remember Day One from Chapter 1?
The blinking cursor on your screen and the anxious whisper: *"Is coding dead?"*

Now lean back and survey the 60-chapter landscape you conquered:
- You decomposed algorithmic logic via pseudocode.
- You crushed performance bottlenecks with Big-O profiling.
- You demystified merge conflicts and engineered automated CI/CD quality gates.
- You structured clean layered architectures and design patterns.
- You tuned composite database indexes to slash query latency to 3ms.
- You erected automated regression shields via the Testing Pyramid.
- You transformed production outages into institutional wisdom through blameless post-mortems.
- You hardened APIs against the OWASP Top 10 with defensive engineering.

Software engineering did not die.
It metamorphosed. It ascended from manual syntax typing into the art of the **Conductor**, orchestrating intelligent autonomous agents across complex systems.

The baton is in your hand. Step onto the podium and compose your masterpiece!""",
            "mental_tr": """Yeni Nesil AI-Driven Mühendisin 10 Maddelik Manifestosu:

```
1. Ben bir klavye amelesi değilim; ben sistem kuran bir Problem Çözücüyüm.
2. Yapay zeka benim yerimi alamaz; çünkü doğruluğu denetleyen akıl benim.
3. Körü körüne güvenmem; her çıktıyı testlerle ve bilimsel şüpheyle doğrularım.
4. Mazeret üretmem; 'Makinemde çalışıyordu' demek yerine konteynerle garanti ederim.
5. Hatalardan korkmam; suçsuz post-mortem kültürüyle her çöküşü bilgeliğe dönüştürürüm.
6. Kodun bekçisiyim; güvenlik ve veri mahremiyetini asla sonraya bırakmam.
7. Basitliği severim; erken optimizasyon ve gereksiz mikroservis çılgınlığından kaçınırım.
8. Takımıma değer katarım; jargondan uzak, iş değerini ve empatiyi önceleyen bir dille konuşurum.
9. Sürekli öğrenirim; geçici trendlere değil, zamansız bilgisayar bilimi temellerine odaklanırım.
10. Ben yapay zekanın çırağı değil; onu yöneten Orkestra Şefiyim!
```""",
            "mental_en": """The AI-Driven Software Engineer's 10-Point Manifesto:

```
1. I am not a syntax typist; I am a systems architect and disciplined problem solver.
2. AI cannot replace me; human judgment, taste, and verification are indispensable.
3. I never trust blindly; I verify all generated logic via executable assertions.
4. I reject excuses; I replace 'works on my machine' with immutable container artifacts.
5. I embrace failure; through blameless post-mortems, every incident breeds institutional wisdom.
6. I am a guardian of security; privacy, sanitization, and defense are non-negotiable defaults.
7. I champion simplicity; I avoid premature optimization and microservice sprawl.
8. I communicate with empathy; I bridge engineering realities with business outcomes.
9. I learn perpetually; I anchor my craft in timeless foundations rather than fleeting hype.
10. I am not an AI passenger; I am the Conductor of the symphony.
```""",
            "prompt_tr": """# ROL: Geleceğin Yazılım Mimarı ve Mentor
Tebrikler! 'AI Çağında Junior Yazılım Mühendisliği' kitabının tüm 60 bölümünü tamamladın.

## MEZUNİYET GÖREVİ:
1. Bu kitaptan öğrendiğin en kritik 3 zihniyet değişimini özetle.
2. Kendine ait 1 yıllık 'Kariyer ve Uzmanlaşma Hedef Kartı'nı hazırla.
3. Bir sonraki projenin ilk commit mesajına şu sözü yaz:
   `feat(core): initialize project with AI orchestration and human craftsmanship`""",
            "prompt_en": """# ROLE: Chief Technology Officer & Lifelong Mentor
Congratulations! You have completed all 60 chapters of AI-Driven Junior Software Engineering.

## GRADUATION DIRECTIVE:
1. Synthesize the 3 most profound mental shifts you internalized across this curriculum.
2. Author your personalized 12-Month Engineering Mastery Roadmap.
3. Stage and push your next repository with this inaugural commit message:
   `feat(core): initialize project with AI orchestration and human craftsmanship`""",
            "code_lang": "typescript",
            "code_naive": """// Dün: Yapay zekadan korkan, ne yaptığını bilmeden kopyala-yapıştır yapan acemi
// const code = ai.magic(); // "İnşallah çalışır..." """,
            "code_robust": """/**
 * Bugün: Ne istediğini bilen, bağlamı yöneten, test eden ve sistemi orkestre eden mühendis.
 *
 * @manifesto
 * "Teknoloji değişir, ilkeler ebedidir.
 *  Yapay zeka hızlandırır, insan aklı yönetir."
 */

export interface FutureEngineer {
  readonly mindset: "Conductor";
  readonly verification: "Deterministic Tests";
  readonly empathy: "Business & User Focused";
  readonly velocity: "10x Accelerated by AI";
}

export const graduate: FutureEngineer = {
  mindset: "Conductor",
  verification: "Deterministic Tests",
  empathy: "Business & User Focused",
  velocity: "10x Accelerated by AI"
};

console.log("🎓 Tebrikler! AI Çağının Yeni Nesil Yazılım Mühendisi Olarak Mezun Oldunuz!");""",
            "code_notes_tr": "60 bölüm boyunca edindiğiniz bilgi birikimi; sizi sadece kod yazan biri değil, geleceğin teknoloji dünyasında söz sahibi olan bir sistem kurucu yaptı.",
            "code_notes_en": "The holistic foundation built across these 60 chapters transforms you from an anxious code consumer into a resilient, high-autonomy systems engineer ready to lead.",
            "pitfalls_tr": [
                {"trap": "Kitabı bitirip 'artık her şeyi öğrendim' diyerek öğrenmeyi bırakmak.", "solution": "Öğrenme asla bitmez; her yeni proje yeni bir öğrenme sahasıdır."},
                {"trap": "Yapay zekanın hızına kapılıp temelleri (algoritmalar, testler) tekrar unutmak.", "solution": "Her zaman 'Bu kodu AI olmadan da anlayabiliyor muyum?' sorusunu canlı tutun."},
                {"trap": "Yalnız çalışıp topluluklardan ve açık kaynaktan kopmak.", "solution": "Bilginizi başkalarıyla paylaşın, topluluklara katılın ve yeni gelen junior'lara mentorluk yapın."}
            ],
            "pitfalls_en": [
                {"trap": "Assuming graduation means learning is complete.", "solution": "The master remains an eternal student; treat every production incident as a masterclass."},
                {"trap": "Getting seduced by raw generation velocity and neglecting deterministic verification.", "solution": "Always demand proof: maintain passing test suites and strict code hygiene."},
                {"trap": "Coding in isolation disconnected from the global engineering community.", "solution": "Contribute to open source, write technical blogs, and mentor the next cohort of junior engineers."}
            ],
            "udemy_title_tr": "Ders 60: Mezuniyet & Manifesto - AI Senfonisinin Orkestra Şefi",
            "udemy_title_en": "Lecture 60: Graduation & Manifesto - Conducting the AI Symphony",
            "udemy_slides_tr": [
                "60 Bölümlük Yolculuğun Büyük Resmi: Nereden Nereye Geldik?",
                "Yeni Nesil Mühendisin 10 Maddelik Manifestosu.",
                "Yapay zekanın asla değiştiremeyeceği insani süper güçler.",
                "Kapanış ve Geleceğe Adım: Baget Artık Sizin Elinizde!"
            ],
            "udemy_slides_en": [
                "The 60-chapter landscape: From day-one anxiety to architectural leadership.",
                "The 10-point AI-Driven Engineering Manifesto.",
                "The uniquely human superpowers: Taste, judgment, empathy, and vision.",
                "Valedictory address: Stepping onto the podium to conduct the symphony."
            ],
            "udemy_demo_tr": "Terminalinizi açın. Sıfırdan bir depo oluşturun, ilk commit'i manifesto mesajıyla atın ve bu 60 bölümlük eğitimin tamamlanışını kutlayın!",
            "udemy_demo_en": "Open your terminal. Initialize a brand-new repository. Stage your first commit with the manifesto signature, and celebrate completing the 60-chapter curriculum!",
            "action_task_tr": "10 Maddelik Mühendislik Manifestosu'nu bir çıktısını alıp veya not uygulamanıza sabitleyip masanızın görebileceğiniz bir yerine asın.",
            "action_task_en": "Pin the 10-Point Engineering Manifesto to your workstation workspace as your permanent north star.",
            "quiz_tr": [
                {
                    "question": "AI çağında bir yazılım mühendisinin yapay zekaya karşı en büyük ve yeri doldurulamaz üstünlüğü nedir?",
                    "options": [
                        "A) Daha hızlı klavye kullanması",
                        "B) İnsan empati yeteneği, gerçek hayat problemlerini anlama vizyonu, etik yargı ve sistemik doğrulama kabiliyeti",
                        "C) Asla uyumaması",
                        "D) Bilgisayardan daha az elektrik harcaması"
                    ],
                    "answer": "B",
                    "explanation": "Yapay zeka ne kadar gelişirse gelişsin; neyin inşa edileceğine karar verme, kullanıcıyla empati kurma ve etik doğruluk daima insanın alanıdır."
                },
                {
                    "question": "Bu 60 bölümlük eğitimin ana felsefesi olan 'Orkestra Şefi Mühendis' kavramı neyi özetler?",
                    "options": [
                        "A) Sadece müzik yazılımları geliştirmeyi",
                        "B) Yapay zeka araçlarını birer enstrüman ve yardımcı stajyer olarak görüp; mimariyi, testleri ve sistemin yönünü tam hakimiyetle yöneten bilinçli mühendisi",
                        "C) Hiç kodlama bilmeyen yöneticileri",
                        "D) Sadece konserde çalışan yazılımcıları"
                    ],
                    "answer": "B",
                    "explanation": "Orkestra şefi mühendis, AI'ın gücünü arkasına alarak mimariyi, kaliteyi ve iş değerini yüksek vizyonla yöneten yeni nesil lider geliştiricidir."
                }
            ],
            "quiz_en": [
                {
                    "question": "What constitutes a software engineer's most irreplaceable advantage over artificial intelligence models?",
                    "options": [
                        "A) Higher keystroke typing speed",
                        "B) Human empathy, real-world problem formulation, ethical discretion, and holistic verification judgment",
                        "C) Functioning without sleep",
                        "D) Consuming less electrical wattage than GPU clusters"
                    ],
                    "answer": "B",
                    "explanation": "LLMs execute token predictions; human engineers provide domain context, taste, ethical responsibility, and strategic judgment."
                },
                {
                    "question": "What is the core philosophical tenet of 'The Conductor of the AI Symphony'?",
                    "options": [
                        "A) Building software exclusively for musical applications",
                        "B) Orchestrating AI models as talented apprentices while maintaining absolute human authority over architecture, verification, and outcomes",
                        "C) Non-technical executive management",
                        "D) Developing software exclusively at concert venues"
                    ],
                    "answer": "B",
                    "explanation": "The Conductor leverages AI velocity without abdicating architectural rigor, steering complex systems toward resilient outcomes."
                }
            ]
        }
    ]
