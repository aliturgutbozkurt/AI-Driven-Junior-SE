"""
Section 1: Yeni Dünyaya Giriş & AI Zihniyeti (Chapters 1 to 6)
"""

def get_section_chapters():
    return [
        # Chapter 1
        {
            "id": 1,
            "section_id": 1,
            "slug_tr": "ch01_ilk_gun_heyecani_yazilimcilik_bitti_mi",
            "slug_en": "ch01_day_one_excitement_software_dead_myth",
            "title_tr": "İlk Gün Heyecanı: 'Yazılımcılık Bitti mi?' Mitini Yıkmak",
            "title_en": "Day One Excitement: Debunking the 'Software Engineering is Dead' Myth",
            "subtitle_tr": "Kod Yazmanın Değil, Problem Çözmenin Yeni Altın Çağı",
            "subtitle_en": "The Golden Age of Problem Solving Over Syntax Memorization",
            "level_tr": "Başlangıç Seviyesi",
            "level_en": "Beginner Level",
            "read_time_tr": "11 dk",
            "read_time_en": "11 min",
            "podcast_hook_tr": "Yapay zeka tüm kodları birkaç saniyede yazabiliyorsa, bir şirketin yeni mezun veya junior bir yazılımcıya maaş ödemesi için mantıklı tek bir sebep kaldı mı?",
            "podcast_hook_en": "If AI models generate code in seconds, is there still any viable reason for tech companies to hire and mentor junior software engineers?",
            "takeaways_tr": [
                "Yapay zeka yazılımcılığı öldürmedi; söz dizimi (syntax) ezberciliğini öldürüp mimari düşünceyi öne çıkardı.",
                "Junior mühendis artık 'klavye amelesi' değil, yapay zeka stajyerlerini yöneten bir orkestra şefidir.",
                "Değeriniz yazdığınız kod satır sayısıyla değil, doğruluğunu garanti ettiğiniz sistemlerle ölçülür."
            ],
            "takeaways_en": [
                "AI did not kill software engineering; it eliminated syntax memorization and elevated architectural reasoning.",
                "The modern junior is no longer a typing drone, but a conductor supervising junior AI agents.",
                "Your value is measured not by lines of code generated, but by the correctness and reliability of the systems you deliver."
            ],
            "story_tr": """Ofise veya uzaktan çalışma masanıza oturduğunuz o ilk günü hayal edin. Ekranda yanıp sönen imleç ve kulağınızda sosyal medyanın uğultusu: *"Yapay zeka varken artık junior'lara gerek yok!"* 

Bir an durup aşçılık tarihine bakalım. Mikserler, akıllı fırınlar ve otomatik hamur yoğurma makineleri icat edildiğinde şefler yok oldu mu? Tam aksine! Önceden saatlerce yumurta çırpmak zorunda kalan çıraklar, artık lezzet dengesine, sunuma ve menü tasarımına odaklanmaya başladı. 

Yazılımda da tam olarak bu devrim yaşanıyor. Eskiden günlerce 'for döngüsü' veya karmaşık CSS hizalamasıyla boğuşan junior, bugün dakikalar içinde prototip çıkarıp işin mantığına, güvenliğine ve kullanıcı deneyimine kafa yorabiliyor. Korku duymak yerine fırının kontrol düğmelerini elinize almanın zamanı geldi.""",
            "story_en": """Picture your first morning at the engineering desk. The cursor blinks on your screen while social media echoes: *"Why hire junior developers when AI writes code in seconds?"*

Consider the culinary world. When food processors, convection ovens, and automated dough mixers arrived, did master chefs disappear? Exactly the opposite. Apprentices who once spent hours manually whisking eggs could now focus on flavor pairing, plating artistry, and culinary orchestration.

Software engineering is experiencing this exact metamorphosis. Instead of getting stuck for days on syntax edge cases or CSS flexbox alignments, today's junior engineer prototypes solutions in minutes and directs attention toward domain logic, system security, and user experience. Step into the kitchen as the chef, not the appliance.""",
            "mental_tr": """Geleneksel yazılımcı zihniyeti **"Nasıl yazarım?"** sorusuyla başlardı. Syntax hatırlamak, StackOverflow'da kaybolmak ve dökümantasyon sayfalarında saatler harcamak bir meziyetti.

AI-Driven mühendis zihniyeti ise **"Ne inşa ediyoruz ve bunu nasıl doğrularım?"** sorusunu merkeze alır:

| Özellik | Geleneksel Junior | AI Destekli (AI-Driven) Junior |
| :--- | :--- | :--- |
| **Odak Noktası** | Dil söz dizimi (Syntax) ve kütüphane API'leri | Problem tanımı, sistem akışı ve doğrulama |
| **Hızlandırıcı** | Google arama + StackOverflow kopyala-yapıştır | LLM ve Agent tabanlı akıllı asistanlar |
| **En Büyük Risk** | Yavaş öğrenme ve motivasyon kaybı | AI halüsinasyonunu fark edemeyip körü körüne güvenme |
| **Katma Değer** | Basit görevleri manuel kodlama | Görevi AI ile hızla çözüp kenar durumları test etme |""",
            "mental_en": """The traditional mindset focused on **"How do I write the syntax?"** Memorizing API signatures and searching StackOverflow threads defined competence.

The AI-driven mindset centers on **"What are we building, and how do I verify correctness?"**:

| Dimension | Traditional Junior | AI-Driven Junior |
| :--- | :--- | :--- |
| **Primary Focus** | Syntax memorization and API signatures | Problem framing, system flow, verification |
| **Acceleration** | Manual Google search & copy-pasting | Context-aware LLM agents and pair copilots |
| **Greatest Risk** | Slow onboarding and burnout | Blind trust in AI hallucinations |
| **Value Add** | Manually typing boilerplate | Orchestrating AI generation and rigorously testing edge cases |""",
            "prompt_tr": """# ROL: Kıdemli Yazılım Mühendisi Mentoru
Sen deneyimli, temiz kod (Clean Code) standartlarına bağlı bir kıdemli mühendissin.
Ben yazılım ekibine yeni katılmış bir junior mühendisim.

## GÖREV:
Aşağıdaki kullanıcı hikayesi (User Story) için bana doğrudan kod YAZMA.
Bunun yerine:
1. Çözmem gereken temel iş mantığı maddelerini listele.
2. Karşılaşabileceğim 3 potansiyel uç durumu (edge case) belirt.
3. Kodu yazarken dikkat etmem gereken mimari prensibi açıkla.

## KULLANICI HİKAYESİ:
"Bir e-ticaret sepetinde kullanıcı indirim kuponu uyguladığında sepet toplamını güncelleyen fonksiyon." """,
            "prompt_en": """# ROLE: Senior Software Engineer Mentor
You are an experienced mentor committed to clean architecture and robust testing.
I am a newly hired junior engineer on your team.

## TASK:
Do NOT write code immediately for the following user story.
Instead:
1. Break down the core business logic requirements into bullet points.
2. Identify 3 critical edge cases I must account for.
3. Explain the architectural principle I should adhere to before implementing.

## USER STORY:
"A function that recalculates shopping cart totals when a user applies a promotional discount coupon." """,
            "code_lang": "python",
            "code_naive": """# Kontrolsüz AI Çıktısı: Sınır değerleri ve tipleri kontrol edilmemiş fonksiyon
def apply_coupon(cart_total, coupon_discount):
    # Eğer indirim sepetten büyükse sepet eksiye düşüyor!
    # Tip kontrolü yok: coupon_discount string gelirse crash olur.
    return cart_total - coupon_discount""",
            "code_robust": """from decimal import Decimal
from typing import Union

def apply_discount(
    cart_total: Union[Decimal, float], 
    discount_amount: Union[Decimal, float]
) -> Decimal:
    \"\"\"
    Sepet toplamına indirim uygular.
    Sepet tutarının sıfırın altına düşmesini engeller ve Decimal hassasiyetinde çalışır.
    \"\"\"
    total = Decimal(str(cart_total))
    discount = Decimal(str(discount_amount))

    if total < Decimal("0.00"):
        raise ValueError("Sepet tutarı negatif olamaz.")
    if discount < Decimal("0.00"):
        raise ValueError("İndirim tutarı negatif olamaz.")

    new_total = total - discount
    return max(new_total, Decimal("0.00"))""",
            "code_notes_tr": "Acemi yaklaşımda float tipi kullanılarak finansal yuvarlama hataları ve eksi bakiye bug'ı gözden kaçırılmıştır. Kıdemli mühendis denetimindeki sürümde ise `Decimal` tipiyle yuvarlama hassasiyeti sağlanmış, negatif değer kontrolleri ve `max(..., 0)` ile defansif koruma eklenmiştir.",
            "code_notes_en": "The naive implementation blindly uses floating point arithmetic, causing rounding bugs and allowing negative balances. The senior-reviewed version enforces `Decimal` precision, validates input boundaries, and uses defensive clamping.",
            "pitfalls_tr": [
                {"trap": "AI'ın ürettiği ilk kodu çalıştığı an PR olarak açmak.", "solution": "Her zaman 'Bu kod neden patlayabilir?' sorusunu sorup en az 3 uç durum testi yazın."},
                {"trap": "Temel algoritma ve mantığı bilmeden her şeyi yapay zekaya devretmek.", "solution": "AI'ı bir 'otopilot' değil, yan koltukta oturan 'yardımcı pilot' olarak görün."},
                {"trap": "Halüsinasyon riskini unutup kütüphane fonksiyonlarını doğrulamamak.", "solution": "AI tarafından önerilen kütüphane metotlarının resmi dokümantasyonunu her zaman hızlıca kontrol edin."}
            ],
            "pitfalls_en": [
                {"trap": "Submitting the first code generated by AI as a Pull Request without inspection.", "solution": "Always ask 'How could this break in production?' and write 3 edge-case tests."},
                {"trap": "Delegating all critical thinking to the model without understanding fundamentals.", "solution": "Treat AI as an eager co-pilot, never as an unmonitored autopilot."},
                {"trap": "Trusting hallucinated library methods without checking docs.", "solution": "Quickly verify any unfamiliar API method against official library documentation."}
            ],
            "udemy_title_tr": "Ders 1: AI Çağında Junior Olmak - İlk Adımlar ve Zihniyet Değişimi",
            "udemy_title_en": "Lecture 1: Being a Junior in the AI Era - First Steps & Mindset Shift",
            "udemy_slides_tr": [
                "Neden 'Yazılımcılık Bitti' söylemi gerçeği yansıtmıyor?",
                "Kod ezberciliğinden Problem Mimarisine geçiş.",
                "AI-Driven geliştiricinin 3 temel ayağı: Bağlam, Doğrulama, İletişim.",
                "Günün canlı demo özeti: Hatalı AI çıktısını senior seviyeye dönüştürmek."
            ],
            "udemy_slides_en": [
                "Why the 'Coding is Dead' rhetoric misses the real point.",
                "Shifting from syntax memorization to problem architecture.",
                "The 3 pillars of an AI-Driven engineer: Context, Verification, Communication.",
                "Live demo recap: Refactoring risky AI code into bulletproof production code."
            ],
            "udemy_demo_tr": "Cursor veya VS Code'u açın. Basit bir e-ticaret indirim fonksiyonu isteyin. AI'ın ilk verdiği kontrolsüz çıktıyı inceleyin, eksiklerini tespit edin ve prompt ile defansif kontroller ekleterek test suite oluşturun.",
            "udemy_demo_en": "Open Cursor or VS Code. Prompt the AI for a simple cart discount function. Inspect the naive output, pinpoint missing boundary checks, and guide the AI to generate a defensive, typed version with tests.",
            "action_task_tr": "Bugün bir yapay zeka aracına (Claude, ChatGPT veya Cursor) daha önce yazdığınız bir fonksiyonu verin ve şu soruyu sorun: 'Bu fonksiyonu production ortamında çökertebilecek 3 senaryo nedir?'",
            "action_task_en": "Today, feed an existing function you wrote into an AI tool and ask: 'What are 3 realistic production scenarios that would break this code?'",
            "quiz_tr": [
                {
                    "question": "AI çağında bir junior yazılım mühendisinin en değerli ayırt edici yeteneği nedir?",
                    "options": [
                        "A) En hızlı kod yazan kişi olmak",
                        "B) Üretilen kodun mantığını, sınır durumlarını ve doğruluğunu denetleyebilmek",
                        "C) Dillerin tüm kütüphane fonksiyonlarını ezbere bilmek",
                        "D) Kodlama yapmadan tüm işi yapay zekaya bırakmak"
                    ],
                    "answer": "B",
                    "explanation": "Yapay zeka hızlı kod üretebilir, ancak üretilen kodun doğruluğunu, sınır durumlarını ve sistemle uyumunu denetlemek mühendisin sorumluluğundadır."
                },
                {
                    "question": "Float tipi yerine Decimal kullanılmasının temel finansal sebebi nedir?",
                    "options": [
                        "A) Decimal'ın bellekte daha az yer kaplaması",
                        "B) Kayan noktalı (float) aritmetiğindeki ikili taban yuvarlama hassasiyet kayıplarını önlemek",
                        "C) Sadece Python'da geçerli olması",
                        "D) Kodun derleme hızını artırması"
                    ],
                    "answer": "B",
                    "explanation": "Kayan noktalı sayılar ikili tabanda temsil edilirken kuruş hassasiyetinde yuvarlama hatalarına (örn. 0.1 + 0.2 != 0.3) yol açar. Finansal işlemlerde Decimal zorunludur."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the most valuable differentiator for a junior engineer in the AI era?",
                    "options": [
                        "A) Typing code at the highest speed",
                        "B) Verifying logic, boundary conditions, and systemic correctness of generated code",
                        "C) Memorizing every standard library function",
                        "D) Fully delegating all critical thinking to autonomous agents"
                    ],
                    "answer": "B",
                    "explanation": "While AI can generate syntax rapidly, verifying correctness, guarding against edge cases, and aligning with business rules is the engineer's responsibility."
                },
                {
                    "question": "Why is Decimal preferred over standard float in monetary calculations?",
                    "options": [
                        "A) Decimal uses less system RAM",
                        "B) To eliminate binary floating-point representation rounding inaccuracies",
                        "C) Decimal is only supported in Python",
                        "D) It increases CPU compiler optimization"
                    ],
                    "answer": "B",
                    "explanation": "Binary floating-point math cannot precisely represent fractional decimal values (like 0.1 + 0.2), causing compounding balance discrepancies in financial software."
                }
            ]
        },

        # Chapter 2
        {
            "id": 2,
            "section_id": 1,
            "slug_tr": "ch02_geleneksel_junior_vs_ai_augmented_junior",
            "slug_en": "ch02_traditional_vs_ai_augmented_junior",
            "title_tr": "Geleneksel Junior vs. AI-Augmented Junior: 10x Zihniyet",
            "title_en": "Traditional Junior vs. AI-Augmented Junior: The 10x Mindset",
            "subtitle_tr": "Kod Yazma Hamallığından Değer Üretme Hızına Geçiş",
            "subtitle_en": "Moving from Manual Boilerplate Grunt Work to Velocity and Value",
            "level_tr": "Başlangıç Seviyesi",
            "level_en": "Beginner Level",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Bir junior mühendis yapay zekayı etkin kullandığında gerçekten bir mid-level veya senior gibi çıktı üretebilir mi, yoksa bu sadece bir illüzyon mu?",
            "podcast_hook_en": "Can an AI-augmented junior truly deliver output on par with a mid-level engineer, or is that velocity gain merely an illusion hiding technical debt?",
            "takeaways_tr": [
                "10x yazılımcı miti bireysel deha ile değil, doğru araç ve geri bildirim döngüsüyle gerçeğe dönüşür.",
                "Geleneksel junior saatlerce dokümantasyon ararken, AI-augmented junior bağlamı besleyip doğrudan prototipe geçer.",
                "Hız tek başına başarı değildir; test edilmemiş hızlı kod, şirketi batıracak teknik borç demektir."
            ],
            "takeaways_en": [
                "The 10x developer is not a myth of innate genius, but a product of optimal tooling and tight feedback loops.",
                "While traditional juniors get stuck hunting documentation, AI-augmented juniors provide context and iterate rapidly.",
                "Speed alone is dangerous; unverified rapid code is merely fast technical debt."
            ],
            "story_tr": """İki yeni mezun mühendis hayal edin: Can ve Elif. İkisi de aynı fintech şirketinde aynı gün işe başladı.

İlk görevleri: *"Kullanıcıların adres bilgilerini doğrulayan ve posta koduna göre şehri getiren bir servis yazmak."*

Can geleneksel yöntemi seçti. 3 saat boyunca regex (düzenli ifade) yazmaya çalıştı, posta kodu API dokümantasyonunda kayboldu ve günün sonunda sadece birkaç satır kod yazıp yorgun düştü.

Elif ise AI-augmented yaklaşımla ilerledi. Önce iş gereksinimlerini listeledi. AI asistanına Türkiye ve Avrupa posta kodu formatlarını doğrulayan test senaryolarını yazdırdı. Ardından bu testleri geçecek temiz, tip korumalı servisi ürettirdi. 45 dakika içinde çalışan, test edilmiş ve dokümante edilmiş bir Pull Request sundu. Senior mühendis Elif'in PR'ını gördüğünde gözlerine inanamadı.""",
            "story_en": """Consider two newly hired engineers, Jack and Sarah, starting on the same team.

Their first ticket: *"Build a service that validates user postal codes and returns the correct municipality."*

Jack followed the traditional approach. He spent 3 hours struggling with regular expressions, scouring outdated API docs, and writing manual boilerplate. By 5 PM, he was exhausted with an untested draft.

Sarah leveraged an AI-augmented workflow. She defined the business rules first, had an AI pair generate unit test fixtures for international postal formats, and then instructed the model to scaffold a type-safe service that made those tests pass. In 45 minutes, she opened a clean, tested, documented Pull Request. Her tech lead was blown away.""",
            "mental_tr": """AI-Augmented mühendis olmanın 3 temel ayağı vardır:
1. **İterasyon Hızı:** 0'dan 1'e gitmek dakikalar sürer.
2. **Aktif Doğrulama:** Yazılan her kodun hemen unit testi olmalıdır.
3. **Kritik Sorgulama:** "AI bu kütüphaneyi neden önerdi? Daha modern bir alternatif var mı?"

```
[İş Gereksinimi] ──> [AI ile Test Senaryosu] ──> [AI ile Kod Üretimi] ──> [İnsan Doğrulaması & Refactor]
```""",
            "mental_en": """The AI-Augmented mindset rests on 3 core pillars:
1. **Velocity to First Draft:** Going from blank page to prototype in minutes.
2. **Active Verification:** Every generated piece of logic must have instant test verification.
3. **Critical Inquiry:** "Why did the model choose this pattern? Is there a lighter dependency?"

```
[Business Spec] ──> [AI-Driven Test Scaffold] ──> [Code Generation] ──> [Human Review & Refactoring]
```""",
            "prompt_tr": """# GÖREV: Test-Driven Development (TDD) İle Servis Tasarımı
Bir TypeScript projesinde çalışıyoruz. Kullanıcı posta kodu doğrulama servisi yazacağız.

Lütfen bana doğrudan implementasyon KODUNU VERME.
Öncelikle aşağıdaki senaryoları kapsayan Jest test dosyasını hazırla:
1. Geçerli formatlar (Örn: '34340', '06100')
2. Hatalı uzunluk veya harf içeren durumlar
3. Boş veya tanımsız (null/undefined) girdiler
4. API zaman aşımı (timeout) durumu""",
            "prompt_en": """# TASK: Test-Driven Development (TDD) Service Scaffolding
We are building a TypeScript service for postal code validation.

Do NOT provide the implementation code yet.
First, generate comprehensive Jest test suites covering:
1. Valid postal codes (e.g., '10001', 'SW1A 1AA')
2. Malformed inputs containing special characters or invalid lengths
3. Null/undefined edge cases
4. Third-party postal lookup API timeout handling""",
            "code_lang": "typescript",
            "code_naive": """// Geleneksel/Aceleci Junior: Hata fırlatmayan, belirsiz tip
export async function getCityByZip(zip: any) {
  const res = await fetch("https://api.zippopotam.us/tr/" + zip);
  const data = await res.json();
  return data.places[0]["place name"]; // Eğer API hata dönerse patlar!
}""",
            "code_robust": """// AI-Augmented Junior: Tip güvenli, Result Pattern ile hata yönetimi
export interface CityResult {
  city: string;
  region: string;
}

export type PostalLookupResponse = 
  | { success: true; data: CityResult }
  | { success: false; error: string };

export async function getCityByPostalCode(
  postalCode: string,
  fetcher: typeof fetch = fetch
): Promise<PostalLookupResponse> {
  const cleaned = postalCode.trim();
  if (!/^\\d{5}$/.test(cleaned)) {
    return { success: false, error: "Geçersiz posta kodu formatı (5 haneli rakam beklenir)." };
  }

  try {
    const res = await fetcher(`https://api.zippopotam.us/tr/${cleaned}`, { signal: AbortSignal.timeout(3000) });
    if (!res.ok) {
      return { success: false, error: `Sunucu hatası: ${res.statusText}` };
    }
    const data = await res.json();
    return {
      success: true,
      data: {
        city: data.places[0]["place name"],
        region: data.places[0]["state"]
      }
    };
  } catch (err: unknown) {
    return { success: false, error: "Servise erişilemedi veya zaman aşımı oluştu." };
  }
}""",
            "code_notes_tr": "Kıdemli AI yaklaşımında; `any` tipi ortadan kaldırılmış, Result Pattern ile hata durumları açıkça modellenmiş, AbortSignal ile timeout eklenmiş ve bağımlılık enjeksiyonu (fetcher) sayesinde test edilebilirlik sağlanmıştır.",
            "code_notes_en": "The robust version eliminates `any`, implements the Result Pattern for predictable error flows, injects the fetcher for unit test mocking, and adds a 3-second timeout signal.",
            "pitfalls_tr": [
                {"trap": "AI tarafından üretilen kodu okumadan commit etmek.", "solution": "Her satırı sesli okuyabilecek kadar anlamadan kod tabanına dahil etmeyin."},
                {"trap": "Dış API çağrılarında zaman aşımı (timeout) belirlememek.", "solution": "Tüm HTTP isteklerine AbortSignal.timeout() veya benzeri sınırlar ekleyin."},
                {"trap": "Gevşek tip kullanımı (any veya Object).", "solution": "TypeScript'te strictly typed arayüzler ve Union tipleri kullanın."}
            ],
            "pitfalls_en": [
                {"trap": "Committing generated code without line-by-line comprehension.", "solution": "If you cannot explain why a line exists, do not push it to production."},
                {"trap": "Omitting network request timeouts.", "solution": "Always guard network calls with AbortSignal or equivalent timeouts."},
                {"trap": "Falling back to 'any' typing in TypeScript.", "solution": "Enforce strict interfaces and discriminant unions for all API payloads."}
            ],
            "udemy_title_tr": "Ders 2: 10x Junior Mühendisin Anatomisi - Hız ve Kalite Dengesi",
            "udemy_title_en": "Lecture 2: Anatomy of a 10x Junior - Balancing Velocity & Quality",
            "udemy_slides_tr": [
                "Geleneksel geliştirici vs AI-Augmented geliştirici iş akışı.",
                "Result Pattern ile güvenli hata yönetimi.",
                "TDD yaklaşımını AI ile birleştirmek: Önce test, sonra kod.",
                "Pull Request hazırlarken senior mühendisleri etkileyen detaylar."
            ],
            "udemy_slides_en": [
                "Traditional developer vs. AI-Augmented workflow breakdown.",
                "Safe error handling using the Result Pattern.",
                "Marrying TDD with AI: Tests first, implementation second.",
                "Creating PRs that earn senior engineer approval on the first pass."
            ],
            "udemy_demo_tr": "Boş bir TypeScript dosyası açın. Posta kodu doğrulama servisini önce test dosyasıyla birlikte AI'a prompt edin. Mock fetch kullanarak testleri çalıştırın ve 0 hata ile yeşil ışık alın.",
            "udemy_demo_en": "Scaffold a TypeScript project. Prompt the AI for tests first, run Jest with mock data, observe failing tests (Red), generate the service, and verify passing tests (Green).",
            "action_task_tr": "Mevcut projenizdeki bir fonksiyona `try/catch` ve Result Pattern ekleyerek olası bir HTTP 500 hatasında çökmesini engelleyin.",
            "action_task_en": "Refactor a network-calling function in your current project to return a discriminated union result instead of throwing raw exceptions.",
            "quiz_tr": [
                {
                    "question": "Result Pattern kullanmanın geleneksel try/catch fırlatmaya göre en büyük avantajı nedir?",
                    "options": [
                        "A) Kodun daha hızlı çalışması",
                        "B) Fonksiyonu çağıran tarafın olası başarı ve hata durumlarını tip düzeyinde zorunlu olarak ele almasını sağlaması",
                        "C) Sadece JavaScript'e özel olması",
                        "D) Bellek kullanımını yarı yarıya düşürmesi"
                    ],
                    "answer": "B",
                    "explanation": "Result Pattern (success: true | success: false) sayesinde TypeScript derleyicisi çağrıyı yapan mühendisi hata durumunu kontrol etmeye zorlar; beklenmedik çalışma zamanı çökmelerini önler."
                },
                {
                    "question": "AI-Augmented bir junior mühendis ile geleneksel junior arasındaki en belirgin fark nedir?",
                    "options": [
                        "A) AI-Augmented junior hiç kod yazmaz",
                        "B) AI-Augmented junior iş mantığını planlayıp doğrulamaya odaklanırken mekanik işleri AI ile hızlandırır",
                        "C) Geleneksel junior daha güvenli kod yazar",
                        "D) AI-Augmented junior test yazmayı gereksiz bulur"
                    ],
                    "answer": "B",
                    "explanation": "AI-Augmented mühendis zamanını mekanik boilerplate yazmak yerine sistem mimarisine, testlere ve sınır durumlarına harcar."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the primary benefit of the Result Pattern over throwing unhandled exceptions?",
                    "options": [
                        "A) It makes execution twice as fast",
                        "B) It forces the caller to explicitly handle both success and error branches at the type level",
                        "C) It is exclusively available in JavaScript",
                        "D) It cuts memory consumption in half"
                    ],
                    "answer": "B",
                    "explanation": "Discriminated unions ensure compile-time guarantees, requiring the consumer to check for error states before accessing payload data."
                },
                {
                    "question": "What is the key hallmark of an AI-augmented junior engineer?",
                    "options": [
                        "A) They never type any code manually",
                        "B) They focus on problem formulation and verification while delegating mechanical chores to AI",
                        "C) Traditional juniors inherently write safer code",
                        "D) AI-augmented engineers bypass writing tests"
                    ],
                    "answer": "B",
                    "explanation": "AI-augmented developers invest their energy in verification, architecture, and edge cases rather than repetitive syntax typing."
                }
            ]
        },

        # Chapter 3
        {
            "id": 3,
            "section_id": 1,
            "slug_tr": "ch03_modern_ai_arac_seti_copilot_cursor_claude",
            "slug_en": "ch03_modern_ai_toolkit_copilot_cursor_claude",
            "title_tr": "Modern AI Araç Setimiz: Copilot, Cursor, Claude Code ve Ötesi",
            "title_en": "The Modern AI Toolkit: Copilot, Cursor, Claude Code & Beyond",
            "subtitle_tr": "Hangi Görev İçin Hangi AI Aracını Seçmelisin?",
            "subtitle_en": "Choosing the Exact AI Weapon for Each Engineering Battle",
            "level_tr": "Başlangıç Seviyesi",
            "level_en": "Beginner Level",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Cursor varken Copilot gereksiz mi? Ya da Claude Code terminal asistanları geliştiricinin yerini mi alıyor?",
            "podcast_hook_en": "Is GitHub Copilot obsolete now that Cursor and terminal agents like Claude Code exist?",
            "takeaways_tr": [
                "Her yapay zeka aracının bir 'tatlı noktası' (sweet spot) vardır; tek bir araca bağımlı kalmayın.",
                "Satır içi tamamlama (Ghost Text) için Copilot, tüm kod tabanı indeksleme için Cursor, otonom refactoring için CLI agent'lar idealdir.",
                "En pahalı araç değil, bağlamı (context) en iyi yönettiğiniz araç en iyi sonucu verir."
            ],
            "takeaways_en": [
                "Every AI developer tool has a dedicated sweet spot; avoid tool dogmatism.",
                "Use inline completions for microscopic flow, workspace indexing IDEs for file relationships, and CLI agents for autonomous multi-file edits.",
                "The best tool is not the most expensive one, but the one you feed with the clearest project context."
            ],
            "story_tr": """Marangoz atölyesine girdiğinizi düşünün. Duvarda testere, rende, zımpara ve çekiç asılı. Bir marangoz vida sıkmak için çekiç kullanırsa ne olur? Tahta çatlar ve vida bozulur.

Yazılım dünyasında da bugün benzer bir hata yapılıyor: 
Bir junior, 50 dosyalık bir mimari refactoring'i GitHub Copilot'un satır içi otomatik tamamlamasına yaptırmaya çalışıyor. Veya basit bir `console.log` eklemek için 5 dakika otonom CLI agent çalıştırıp jeton (token) yakıyor.

Doğru aleti doğru işte kullanmak, profesyonel bir mühendisi amatörden ayıran ilk beceridir.""",
            "story_en": """Walk into a master carpenter's workshop. Hanging on the pegboard are chisels, saws, orbital sanders, and planers. What happens if you try to drive a drywall screw using a framing hammer? You split the timber.

Junior developers make this exact mistake with AI tooling:
They attempt a 50-file architectural refactor using single-line autocomplete, or they spin up an autonomous terminal agent and burn 200,000 tokens just to fix an indentation typo.

Selecting the exact tool for the job is the signature mark of an engineering professional.""",
            "mental_tr": """AI Araçlarının Katmanlı Mimarisi:

| Katman | Araç Örnekleri | En İyi Kullanım Alanı | Dikkat Edilmesi Gereken |
| :--- | :--- | :--- | :--- |
| **Micro (Satır İçi)** | GitHub Copilot, Supermaven | Boilerplate tamamlama, döngüler, DTO tanımları | Körü körüne Tab'a basıp yanlış mantığı onaylamak |
| **Meso (Editör İçi)** | Cursor (Composer), Windsurf | Dosyalar arası ilişki, `@files`, `@docs` bağlamı | Çok fazla gereksiz dosya ekleyip token limitini aşmak |
| **Macro (CLI / Agent)** | Claude Code, Aider, Antigravity | Terminal komutları, testleri çalıştırıp otomatik düzeltme | Yanlış komut çalıştırma veya git geçmişini bozma riski |""",
            "mental_en": """The 3 Tiers of Developer AI Tooling:

| Tier | Examples | Optimal Sweet Spot | Key Risk |
| :--- | :--- | :--- | :--- |
| **Micro (Inline)** | GitHub Copilot, Supermaven | Fast line completion, DTOs, boilerplate | Blindly tab-accepting incorrect logic |
| **Meso (IDE Native)** | Cursor (Composer), Windsurf | Cross-file references, `@codebase`, documentation | Polluting context with irrelevant files |
| **Macro (Autonomous Agent)**| Claude Code, Aider, Antigravity | Git workflows, test-driven self-healing loops | Unmonitored disk/terminal mutations |""",
            "prompt_tr": """# ROL: Senior Full-Stack Mimar
Projemizde PostgreSQL, Prisma ORM, Next.js ve TailwindCSS kullanıyoruz.

## BAĞLAM (@schema.prisma ve @auth.ts):
Aşağıdaki yeni gereksinimi karşılamak için hangi dosyaları değiştirmem gerektiğini listele:
"Kullanıcıların profil sayfasına iki faktörlü kimlik doğrulama (2FA) açma/kapama butonu ekleme."

Lütfen hemen kod yazma; sadece:
1. Değişecek veritabanı alanları
2. Backend API endpoint'i
3. Frontend bileşeni
adım adım bir mimari plan sun.""",
            "prompt_en": """# ROLE: Senior Full-Stack Architect
Our stack: PostgreSQL, Prisma ORM, Next.js App Router, TailwindCSS.

## CONTEXT (@schema.prisma & @auth.ts):
Identify the precise files requiring modification for this ticket:
"Allow users to toggle Two-Factor Authentication (2FA) from their security settings page."

Do NOT generate complete code yet. Outline:
1. Database schema additions
2. Server action / API endpoint contracts
3. Client-side UI state handling""",
            "code_lang": "bash",
            "code_naive": """# Kötü Yaklaşım: AI'ın çalıştırdığı terminal komutunu kontrol etmeden çalıştırmak
# Yapay zekaya "Projeyi sıfırla ve yeniden kur" dediniz ve şunu önerdi:
rm -rf node_modules package-lock.json && git clean -fdx && npm install
# DİKKAT: Henüz commit etmediğiniz tüm yerel dosyalarınız sonsuza dek silindi!""",
            "code_robust": """# Güvenli Yaklaşım: Önce durumu doğrula, dry-run yap ve korumalı çalış
# 1. Değişiklikleri güvene al
git status
git stash save "proje-temizlik-oncesi"

# 2. Sadece hedeflenen paketleri temizle
rm -rf node_modules
npm cache verify
npm install

# 3. Testleri çalıştırarak ortamı doğrula
npm test""",
            "code_notes_tr": "Terminal üzerinde çalışan otonom AI agent'ları kullanırken `git clean -fdx` veya `rm -rf` gibi yıkıcı komutları asla gözünüz kapalı onaylamayın. Her zaman önce `git stash` veya branch yedeği alın.",
            "code_notes_en": "When using autonomous CLI agents, never accept destructive commands like `git clean -fdx` blindly. Always verify uncommitted work via `git status` or stash changes beforehand.",
            "pitfalls_tr": [
                {"trap": "Aynı anda 3 farklı AI eklentisini açıp birbirleriyle çakıştırmak.", "solution": "Birincil editörünüzü ve tek bir tamamlama aracını belirleyip odaklanın."},
                {"trap": "Büyük projelerde tüm kod tabanını prompta yapıştırmak.", "solution": "Sadece ilgili servis ve interface dosyalarını bağlam (@file) olarak ekleyin."},
                {"trap": "AI CLI araçlarına sudo veya sınırsız terminal izni vermek.", "solution": "Hassas terminal komutları için her zaman manuel onay modunu açık tutun."}
            ],
            "pitfalls_en": [
                {"trap": "Running multiple competing AI extensions simultaneously, causing IDE lag and overlapping ghost text.", "solution": "Standardize on one primary workflow engine."},
                {"trap": "Stuffing entire 100,000-line repositories into prompt context.", "solution": "Selectively target relevant modules and interfaces using `@file` syntax."},
                {"trap": "Granting sudo or auto-accept permissions to terminal agents.", "solution": "Always require interactive confirmation for terminal side-effects."}
            ],
            "udemy_title_tr": "Ders 3: AI Araç Kutunuzu Kurmak - Copilot, Cursor ve CLI Entegrasyonu",
            "udemy_title_en": "Lecture 3: Building Your AI Arsenal - Copilot, Cursor & CLI Agents",
            "udemy_slides_tr": [
                "3 Katmanlı AI Mimarisi: Micro, Meso, Macro araçlar.",
                "Cursor'da @sembolleri (@files, @docs, @codebase) ile bağlam yönetimi.",
                "Terminal asistanlarını güvenli kullanma kılavuzu.",
                "Canlı karşılaştırma: Hangi araç nerede kazandırır?"
            ],
            "udemy_slides_en": [
                "The 3-tier AI developer architecture: Micro, Meso, Macro.",
                "Precision context targeting in Cursor with `@files` and `@codebase`.",
                "Safety guardrails for CLI and terminal agents.",
                "Head-to-head comparison: Choosing the optimal tool for each task."
            ],
            "udemy_demo_tr": "Cursor IDE'de `@codebase` kullanarak projedeki bir veritabanı modelinin nerede kullanıldığını sorgulatın. Ardından `@file` ile sadece iki dosyayı seçerek hedefli bir refactor gerçekleştirin.",
            "udemy_demo_en": "Demonstrate Cursor's context references: run a codebase query to find all occurrences of a database model, then target a specific file pair using `@file` for a surgical refactor.",
            "action_task_tr": "Bugün IDE'nizde en sık kullandığınız 3 dosyayı `@` kısayoluyla bağlama ekleyerek küçük bir fonksiyon geliştirin ve token kullanımını gözlemleyin.",
            "action_task_en": "Configure your IDE with dedicated context references (`@file`) and execute a single-task prompt, noting the difference in response accuracy.",
            "quiz_tr": [
                {
                    "question": "Cursor veya benzeri modern AI IDE'lerinde '@' sembolünün temel amacı nedir?",
                    "options": [
                        "A) E-posta göndermek",
                        "B) Modele yalnızca belirli dosyaları, dokümanları veya kod tabanını bağlam olarak iletmek",
                        "C) Kodu otomatik olarak derlemek",
                        "D) GitHub şifresini kaydetmek"
                    ],
                    "answer": "B",
                    "explanation": "@ sembolü sayesinde LLM'e projenin sadece ilgili parçaları bağlam olarak gönderilir; böylece hem maliyet düşer hem de doğruluk artar."
                },
                {
                    "question": "Otonom terminal agent'ları (CLI) kullanırken en kritik güvenlik kuralı nedir?",
                    "options": [
                        "A) İnternet bağlantısını kesmek",
                        "B) Dosya silen ve git geçmişini etkileyen komutları manuel olarak denetlemek",
                        "C) Sadece Python kullanmak",
                        "D) Bilgisayarı yeniden başlatmak"
                    ],
                    "answer": "B",
                    "explanation": "Terminal agent'ları geri dönülemez dosya silme veya branch ezme komutları önerebilir. Kritik komutlar mutlaka insan onayından geçmelidir."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the primary function of the '@' reference in modern AI IDEs like Cursor?",
                    "options": [
                        "A) Sending automated email updates to the team",
                        "B) Precisely scoping the context window with selected files, docs, or symbols",
                        "C) Triggering background project builds",
                        "D) Storing credentials securely"
                    ],
                    "answer": "B",
                    "explanation": "Scoped context feeds only relevant tokens to the model, preventing token bloat and significantly boosting reasoning accuracy."
                },
                {
                    "question": "What is the most critical safety rule when operating autonomous terminal AI agents?",
                    "options": [
                        "A) Disconnecting from Wi-Fi",
                        "B) Interactively auditing all file-deletion and destructive Git commands before execution",
                        "C) Restricting usage strictly to Python scripts",
                        "D) Rebooting the operating system"
                    ],
                    "answer": "B",
                    "explanation": "Terminal commands like `rm` or `git reset --hard` are irreversible; human verification prevents accidental loss of uncommitted work."
                }
            ]
        },

        # Chapter 4
        {
            "id": 4,
            "section_id": 1,
            "slug_tr": "ch04_halusinasyon_ve_guven_tuzagi",
            "slug_en": "ch04_trust_trap_and_hallucinations",
            "title_tr": "AI Halüsinasyonu ve Güven Tuzağı: Kod Denetçisi Olmak",
            "title_en": "The Trust Trap & Hallucination Defense: Becoming a Code Auditor",
            "subtitle_tr": "Var Olmayan Kütüphaneleri ve Sahte Metotları Yakalama Sanatı",
            "subtitle_en": "Catching Phantom Libraries, Fake Methods, and Silent Security Flaws",
            "level_tr": "Başlangıç Seviyesi",
            "level_en": "Beginner Level",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Bir yapay zeka modeli son derece mantıklı görünen ancak gerçekte hiç var olmayan bir npm paketi önerdiğinde ne olur? Bu halüsinasyon bir siber güvenlik saldırısına dönüşebilir mi?",
            "podcast_hook_en": "What happens when an LLM enthusiastically invents a non-existent package name? Could this hallucination pave the way for a supply chain attack?",
            "takeaways_tr": [
                "Yapay zeka gerçeği bilmez; olasılıksal olarak en mantıklı gelen bir sonraki kelimeyi tahmin eder.",
                "Slopsquatting (paket halüsinasyonu), saldırganların sahte kütüphaneler yükleyip şirketleri hacklediği gerçek bir tehdittir.",
                "Mühendisin en büyük görevi kod yazmak değil, AI çıktısına karşı 'Şüpheci Müfettiş' rolü üstlenmektir."
            ],
            "takeaways_en": [
                "LLMs do not understand ground truth; they generate mathematically probable token sequences.",
                "Package hallucination ('slopsquatting') is an active supply chain attack vector where malicious actors publish invented package names.",
                "Your role as an engineer is transitioning from code author to skeptical forensic inspector."
            ],
            "story_tr": """2023 yılında bir junior geliştirici, Python ile AWS S3 dosyalarını sıkıştırmak için ChatGPT'ye danıştı. Model kendinden çok emin bir dille şu cevabı verdi:

`pip install aws-s3-fast-compressor`

Geliştirici kodu projeye ekledi. Ancak bir gariplik vardı: Böyle bir kütüphane Python Package Index'te (PyPI) henüz yoktu! Bir siber güvenlik araştırmacısı bu durumu fark etti ve yapay zekaların sıkça uydurduğu bu sahte kütüphane ismini tescilleyerek içine bir test kodu koydu. Birkaç gün içinde dünyanın önde gelen teknoloji şirketlerinden yüzlerce sunucunun bu sahte paketi indirmeye çalıştığı görüldü!

İşte buna **AI Halüsinasyon Tuzağı** denir. Yapay zeka yalan söylemez; ama var olmayan şeyleri gerçekmiş gibi hayal eder.""",
            "story_en": """In 2023, an engineer queried an LLM on how to accelerate AWS S3 file compression. The model confidently replied:

`pip install aws-s3-fast-compressor`

The engineer added it to `requirements.txt`. But here was the catch: that package didn't exist. Security researchers tracking LLM hallucinations noticed models repeatedly hallucinating this exact name, registered the namespace on PyPI, and logged inbound downloads. Within days, hundreds of corporate build servers were pulling the dummy package.

This is the **Hallucination Slopsquatting Trap**. Large language models don't lie maliciously—they extrapolate plausible fiction with absolute confidence.""",
            "mental_tr": """Halüsinasyon Tespiti İçin 4 Aşamalı Doğrulama Protokolü:

```
[AI Yanıtı] 
   │
   ├── 1. Paket Doğrulaması: NPM / PyPI üzerinde gerçekten var mı? İndirme sayısı kaç?
   │
   ├── 2. Dokümantasyon Kontrolü: Fonksiyon parametreleri resmi sitede yazıyor mu?
   │
   ├── 3. Tip Kontrolü (Compiler): TypeScript / MyPy hatasız derleniyor mu?
   │
   └── 4. Çalışma Zamanı Testi (Runtime): Unit test uç durumları geçiyor mu?
```""",
            "mental_en": """The 4-Step Hallucination Defense Protocol:

```
[Model Output]
   │
   ├── 1. Package Verification: Does the package exist on npm/PyPI? What is its download count?
   │
   ├── 2. API Signature Audit: Do parameters match official documentation?
   │
   ├── 3. Compiler / Static Analysis: Does TypeScript or MyPy pass with zero errors?
   │
   └── 4. Runtime Test Execution: Do boundary unit tests pass?
```""",
            "prompt_tr": """# ROL: Şüpheci Güvenlik ve Kod Denetçisi
Aşağıda bir yapay zekanın önerdiği kod parçası bulunmaktadır.

## GÖREV:
Bu koda asla hemen güvenme. Aşağıdaki analizleri gerçekleştir:
1. Bu kodda kullanılan fonksiyon ve kütüphaneler güncel mi yoksa 'uydurulmuş' (halüsinasyon) olabilir mi?
2. Hangi satırda sessiz bir mantık hatası (silent bug) veya güvenlik açığı bulunmaktadır?
3. Bu kodun doğruluğunu kanıtlayacak bağımsız bir test fonksiyonu yaz.

## KOD PARÇASI:
```javascript
const crypto = require('crypto');
function createToken(userId) {
  // AI önerisi:
  return crypto.createCipher('des', userId).final('hex');
}
```""",
            "prompt_en": """# ROLE: Skeptical Security & Code Auditor
Below is an AI-suggested code block.

## TASK:
Do not trust this code blindly. Conduct a rigorous audit:
1. Are the APIs and methods current, deprecated, or potential hallucinations?
2. Are there any silent security vulnerabilities or cryptographic flaws?
3. Provide a corrected, hardened version accompanied by a verification unit test.

## SNIPPET:
```javascript
const crypto = require('crypto');
function createToken(userId) {
  return crypto.createCipher('des', userId).final('hex');
}
```""",
            "code_lang": "javascript",
            "code_naive": """// Halüsinasyon / Eski API Tuzağı: createCipher güvensizdir ve Node.js'te deprecated edilmiştir!
const crypto = require('crypto');

function generateSecureToken(userId) {
  // 'des' algoritması kırılmıştır ve createCipher IV (başlatma vektörü) kullanmaz!
  const cipher = crypto.createCipher('des', 'gizli_anahtar');
  let token = cipher.update(userId, 'utf8', 'hex');
  token += cipher.final('hex');
  return token;
}""",
            "code_robust": """// Güncel & Güvenli Standart: AES-256-GCM ve rastgele IV kullanımı
const crypto = require('crypto');

function generateSecureToken(userId, secretKeyBuffer) {
  if (!secretKeyBuffer || secretKeyBuffer.length !== 32) {
    throw new Error("Geçersiz anahtar uzunluğu: 32 baytlık buffer zorunludur.");
  }

  // 12 baytlık benzersiz IV (Initialization Vector)
  const iv = crypto.randomBytes(12);
  const cipher = crypto.createCipheriv('aes-256-gcm', secretKeyBuffer, iv);
  
  let encrypted = cipher.update(String(userId), 'utf8', 'hex');
  encrypted += cipher.final('hex');
  const authTag = cipher.getAuthTag().toString('hex');

  // IV + AuthTag + Şifreli metin bir arada paketlenir
  return `${iv.toString('hex')}:${authTag}:${encrypted}`;
}""",
            "code_notes_tr": "Eski AI modelleri eğitim verilerindeki 10 yıllık eski kodları hatırlayarak güvensiz `crypto.createCipher` metodunu önerebilir. Modern denetim; güvenli `createCipheriv`, AES-256-GCM algoritması ve kimlik doğrulama etiketi (Auth Tag) kullanımını zorunlu kılar.",
            "code_notes_en": "Legacy training corpora cause LLMs to suggest deprecated APIs like `createCipher` with broken DES encryption. Production-grade code mandates `createCipheriv`, authenticated AES-256-GCM, and random initialization vectors.",
            "pitfalls_tr": [
                {"trap": "AI'ın önerdiği her yeni paketi sorgulamadan package.json'a eklemek.", "solution": "npm trends veya Snyk üzerinden paketin yaşını, yapımcısını ve indirilme sayısını kontrol edin."},
                {"trap": "Derleme hatası vermeyen kodun doğru çalıştığını varsaymak.", "solution": "Tip doğrulaması yalnızca şekli kontrol eder; iş mantığını doğrulamak için runtime testi yazın."},
                {"trap": "AI'a 'Bu kod kesin çalışıyor mu?' diye sorup 'Evet efendim' yanıtına inanmak.", "solution": "AI kendi hatasını savunma eğilimindedir; doğrulama için bağımsız test çalıştırın."}
            ],
            "pitfalls_en": [
                {"trap": "Installing newly suggested packages without checking registry metadata.", "solution": "Inspect npm trends, GitHub stars, and maintainer identity before running `npm install`."},
                {"trap": "Assuming compilation success equals functional correctness.", "solution": "Types only validate structure; unit tests validate business behavior."},
                {"trap": "Asking the model 'Are you 100% sure this works?' and accepting its apologetic confirmation.", "solution": "Models exhibit sycophancy; rely on executable test runners instead."}
            ],
            "udemy_title_tr": "Ders 4: Yapay Zekayı Yakalamak - Halüsinasyon ve Güvenlik Denetimi",
            "udemy_title_en": "Lecture 4: Catching the AI - Hallucination Audits & Security Traps",
            "udemy_slides_tr": [
                "Halüsinasyon nedir? Olasılıksal dil modelleri nasıl çalışır?",
                "Paket halüsinasyonu (Slopsquatting) tehdidi ve tedbirler.",
                "Eski (deprecated) API'leri tespit etme teknikleri.",
                "Adım adım kod denetimi: AI çıktısını teste tabi tutmak."
            ],
            "udemy_slides_en": [
                "What is an LLM hallucination? Understanding probabilistic token selection.",
                "The slopsquatting threat and supply chain defenses.",
                "Detecting deprecated API signatures before deployment.",
                "Forensic auditing: Putting AI output through test gauntlets."
            ],
            "udemy_demo_tr": "Modelden bilerek var olmayan bir özellik için kütüphane isteyin. Modelin uydurduğu ismi npm'de aratarak sahte olduğunu gösterin. Ardından aynı işi standart kütüphanelerle güvenli şekilde kodlatın.",
            "udemy_demo_en": "Prompt an LLM for an obscure feature and observe it invent a package name. Cross-reference npm to show it does not exist, then solve the challenge using verified standard libraries.",
            "action_task_tr": "Projenizdeki `package.json` dosyasını açın. En az 1 kütüphanenin npm sayfasını ziyaret edin; son güncelleme tarihini ve haftalık indirme sayısını inceleyin.",
            "action_task_en": "Inspect your project's dependency manifest (`package.json` or `requirements.txt`). Verify release dates and weekly download statistics for at least one critical dependency.",
            "quiz_tr": [
                {
                    "question": "Paket halüsinasyonu (Slopsquatting) saldırısı nasıl gerçekleşir?",
                    "options": [
                        "A) Hackerların kullanıcının bilgisayarına fiziksel olarak girmesiyle",
                        "B) Saldırganların, yapay zekaların sıkça uydurduğu sahte paket isimlerini tescilleyip içine zararlı kod yerleştirmesiyle",
                        "C) Sadece C++ dilinde derleyicinin çökmesiyle",
                        "D) Bilgisayar ekranının donmasıyla"
                    ],
                    "answer": "B",
                    "explanation": "Saldırganlar LLM'lerin uydurmaya meyilli olduğu paket isimlerini takip eder ve bu isimlerle zararlı paketler yayınlayarak dikkatsiz geliştiricilerin indirmesini bekler."
                },
                {
                    "question": "Bir yapay zeka çıktısının güvenilir olduğunu anlamanın en sağlam yolu nedir?",
                    "options": [
                        "A) AI'a 'Bu doğru mu?' diye sormak",
                        "B) Çıktıyı otomatik unit testler, linter'lar ve resmi dokümantasyon ile bağımsızca doğrulamak",
                        "C) Kodun çok uzun ve karmaşık görünmesi",
                        "D) Kodun StackOverflow'da bir yanıta benzemesi"
                    ],
                    "answer": "B",
                    "explanation": "Teknik doğruluk ancak derleyiciler, bağımsız test koşucuları ve resmi dokümantasyon ile garanti altına alınabilir."
                }
            ],
            "quiz_en": [
                {
                    "question": "How does an AI package hallucination (slopsquatting) exploit work?",
                    "options": [
                        "A) Attackers break into local hardware physically",
                        "B) Attackers register hallucinated package names on public registries with malicious code payloads",
                        "C) Compilers crash exclusively in C++",
                        "D) Monitors lose display output"
                    ],
                    "answer": "B",
                    "explanation": "Attackers harvest frequently hallucinated library names and publish malicious code, waiting for unsuspecting developers to run `npm install`."
                },
                {
                    "question": "What is the most robust method to verify AI code correctness?",
                    "options": [
                        "A) Re-asking the AI 'Are you certain?'",
                        "B) Verifying logic against official docs, static analyzers, and automated test suites",
                        "C) Assessing whether the code looks intricate",
                        "D) Finding a similar post on a forum"
                    ],
                    "answer": "B",
                    "explanation": "Deterministic verification via automated test suites and official API references is the only foolproof quality safeguard."
                }
            ]
        },

        # Chapter 5
        {
            "id": 5,
            "section_id": 1,
            "slug_tr": "ch05_prompt_degil_context_muhendisligi",
            "slug_en": "ch05_context_engineering_over_prompt_engineering",
            "title_tr": "Prompt Mühendisliği Değil 'Context Mühendisliği': LLM'lere Nasıl Brif Verilir?",
            "title_en": "Context Engineering Over Prompt Engineering: Briefing LLMs for Precision",
            "subtitle_tr": "Süslü Cümleleri Unutun: Şemalar, Tipler ve Dosya Sınırlarıyla Konuşun",
            "subtitle_en": "Forget Fluff: Speak Through Schemas, Interfaces, and Scope Boundaries",
            "level_tr": "Başlangıç Seviyesi",
            "level_en": "Beginner Level",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "'Sen bir dünya çapında yazılımcısın' gibi süslü prompt şablonları gerçekten işe yarıyor mu, yoksa modele doğru TypeScript interface'ini vermek çok daha mı etkili?",
            "podcast_hook_en": "Does magical prompt phrasing like 'Act as an elite software wizard' actually work, or does feeding the precise TypeScript interface yield vastly superior code?",
            "takeaways_tr": [
                "Prompt mühendisliği sözcüklerle ilgilidir; Context mühendisliği ise sistemin durumunu ve sınırlarını modele aktarmakla ilgilidir.",
                "Çöp bağlam (Garbage Context) verirseniz, en gelişmiş model bile çöp kod üretir.",
                "Bir modele verilebilecek en kaliteli bağlam: Tip tanımları, girdi/çıktı örnekleri ve kabul kriterleridir."
            ],
            "takeaways_en": [
                "Prompt engineering tweaks words; Context engineering curates data, schemas, and system boundaries.",
                "Garbage context into the frontier model yields state-of-the-art garbage output.",
                "The highest signal context consists of: type contracts, input/output assertions, and explicit constraints."
            ],
            "story_tr": """Bir mimarlık ofisine stajyer girdiğini düşünün. Patron stajyere: *"Bana harika, modern, ödül alacak bir bina çiz!"* derse ne olur? Stajyer uzay mekiğine benzeyen ama inşa edilmesi imkansız bir gökdelen çizer.

Peki patron şöyle brif verirse:
- Arsa boyutu: 500 m²
- İmar izni: En fazla 3 kat
- Malzeme: Prefabrik betonarme ve cam
- Hedef: 4 kişilik 6 adet daire

Stajyer tam istenen, hemen inşa edilebilir projeyi getirir!

LLM'ler de tıpkı bu stajyer gibidir. Onlara *"Bana harika bir sepet fonksiyonu yaz"* derseniz halüsinasyon görürler. Ama şemayı, tipleri ve kısıtları verirseniz kusursuz üretim yaparlar.""",
            "story_en": """Imagine an intern joining an architecture studio. If the lead architect says: *"Draw me a breathtaking, futuristic building!"* the intern produces a floating glass spaceship that collapses under gravity.

Contrast that with an engineering brief:
- Lot dimensions: 500 sq meters
- Zoning limit: Maximum 3 stories
- Material constraints: Precast concrete and double-glazed glass
- Objective: 6 two-bedroom rental units

The intern delivers an actionable blueprint.

LLMs are identical to this intern. Demanding 'great code' yields generic hallucinations. Providing interface contracts, database schemas, and constraints yields production-grade solutions.""",
            "mental_tr": """Context Mühendisliğinin 4B Formülü (Bağlam Piramidi):

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
```""",
            "mental_en": """The 4-Layer Context Engineering Pyramid:

```
       ┌────────────────────────┐
       │   4. Output Shape      │ -> Expected JSON schema / return signature
       ├────────────────────────┤
       │   3. Constraints       │ -> "No external npm libs, maximum O(N) time"
       ├────────────────────────┤
       │   2. Schemas & Types   │ -> TypeScript interfaces / Prisma schema
       ├────────────────────────┤
       │   1. Role & Objective  │ -> "Senior Backend Systems Engineer"
       └────────────────────────┘
```""",
            "prompt_tr": """# ROL: Senior Backend Engineer
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
```""",
            "prompt_en": """# ROLE: Senior Backend Engineer
# OBJECTIVE: Filter employees by age and group them by department.

## INPUT TYPE SPECIFICATION:
```typescript
interface Employee {
  id: string;
  name: string;
  age: number;
  department: 'ENGINEERING' | 'SALES' | 'MARKETING';
}
```

## CONSTRAINTS:
- Zero external libraries (no Lodash, no Ramda).
- Pure TypeScript using modern `Map` or `Object.groupBy`.
- Filter out employees under 18 years old.

## EXPECTED OUTPUT CONTRACT:
```typescript
type GroupedResult = Record<Employee['department'], Employee[]>;
```""",
            "code_lang": "typescript",
            "code_naive": """// Zayıf Bağlam Verildiğinde AI Çıktısı: Lodash kütüphanesi şart koşulmuş ve tipler eksik
// Prompt: "Çalışanları departmana göre grupla"
const _ = require('lodash');

function groupStaff(data: any) {
  // Lodash yüklemediyseniz projeniz patlar!
  return _.groupBy(data, 'department');
}""",
            "code_robust": """// Context Mühendisliği ile Elde Edilen Çıktı: Sıfır bağımlılık, tam tip güvenliği
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
}""",
            "code_notes_tr": "Modele tipler ve kısıtlar ('Lodash kullanma') verildiğinde, fazladan 50KB bağımlılık eklemek yerine modern dil standartlarını kullanarak hafif ve güvenli kod üretir.",
            "code_notes_en": "By passing explicit boundary constraints, the model produces a zero-dependency, type-safe implementation instead of unnecessarily pulling in external packages.",
            "pitfalls_tr": [
                {"trap": "Prompt içine 10 paragraflık hikaye yazıp asıl teknik kısıtları unutmak.", "solution": "Laf kalabalığını atın; kod şemalarını ve kısıtları maddeler halinde yazın."},
                {"trap": "Modele veri tabanı şemasını vermeden SQL veya ORM kodu istemek.", "solution": "Her zaman ilgili tablo şemasını (schema.prisma veya CREATE TABLE) bağlam olarak ekleyin."},
                {"trap": "Hata aldığınızda sadece 'Hata verdi düzelt' yazmak.", "solution": "Terminal çıktısını ve çağrı yığınını (stack trace) tam olarak bağlama ekleyin."}
            ],
            "pitfalls_en": [
                {"trap": "Writing lengthy conversational prose while omitting technical constraints.", "solution": "Strip fluff; provide concise types, interfaces, and bulleted rules."},
                {"trap": "Requesting SQL queries without providing table schemas.", "solution": "Always include schema definitions in the prompt context."},
                {"trap": "Prompting 'It broke, fix it' upon encountering an error.", "solution": "Always attach the exact terminal stack trace and input arguments."}
            ],
            "udemy_title_tr": "Ders 5: Context Mühendisliği - LLM'lere Yazılımcı Gibi Brif Vermek",
            "udemy_title_en": "Lecture 5: Context Engineering - Briefing LLMs with Engineering Rigor",
            "udemy_slides_tr": [
                "Neden Prompt Mühendisliği yetersiz kalıyor?",
                "4B Formülü: Rol, Şemalar, Kısıtlar, Çıktı Formatı.",
                "TypeScript Interface'lerini en güçlü prompt aracı olarak kullanmak.",
                "Canlı uygulama: Kötü prompt vs Bağlamı zengin prompt karşılaştırması."
            ],
            "udemy_slides_en": [
                "Why prompt phrasing falls short of context engineering.",
                "The 4-layer pyramid: Role, Schemas, Constraints, Output Spec.",
                "Using TypeScript interfaces as high-precision prompt templates.",
                "Live demonstration: Vague prompt vs Context-engineered prompt."
            ],
            "udemy_demo_tr": "Aynı işi iki farklı pencerede yaptırın: Birinde 'Bana e-posta doğrulayan fonksiyon yaz' deyin; diğerinde regex kısıtları ve TypeScript tipleri verin. Çıkan iki kodu yan yana inceleyin.",
            "udemy_demo_en": "Open two side-by-side chats. Submit 'Write an email validator' to one, and supply explicit domain constraints and interface types to the other. Compare code quality differences.",
            "action_task_tr": "Yapay zekaya göndereceğiniz bir sonraki görevde hiçbir Türkçe/İngilizce açıklama yapmadan sadece `interface Input` ve `interface Output` vererek kod üretmesini isteyin.",
            "action_task_en": "Submit your next AI prompt using only TypeScript `interface Input` and `interface Output` without conversational prose, and observe the output precision.",
            "quiz_tr": [
                {
                    "question": "Context mühendisliğinde bir yapay zeka modeline verilebilecek en yüksek sinyalli (en kaliteli) bilgi hangisidir?",
                    "options": [
                        "A) 'Sen dahi bir yazılımcısın' cümlesi",
                        "B) Tip tanımları, veri tabanı şeması ve girdi/çıktı kısıtları",
                        "C) 5 sayfalık genel şirket tanıtım metni",
                        "D) Emojilerle süslenmiş motivasyon mesajı"
                    ],
                    "answer": "B",
                    "explanation": "Modeller matematiksel olarak semantik sınırlara göre çalışır; tip tanımları ve şemalar en kesin kısıtları sağlayarak sapmayı önler."
                },
                {
                    "question": "Yapay zekanın gereksiz üçüncü taraf kütüphaneler eklemesini önlemenin en pratik yolu nedir?",
                    "options": [
                        "A) İnterneti kapatmak",
                        "B) Prompt kısıtlarına 'Sıfır harici kütüphane, sadece yerel dil özellikleri kullanılacaktır' şartı eklemek",
                        "C) Sadece C dilinde kod yazmak",
                        "D) Kütüphane eklediğinde ona kızmak"
                    ],
                    "answer": "B",
                    "explanation": "Açıkça belirtilen kısıtlar (constraints), modelin token tahmin alanını sınırlar ve gereksiz bağımlılıkları engeller."
                }
            ],
            "quiz_en": [
                {
                    "question": "What constitutes the highest-signal context for an engineering LLM prompt?",
                    "options": [
                        "A) Phrasing like 'You are an infallible software genius'",
                        "B) Strict type interfaces, database schemas, and explicit boundary constraints",
                        "C) Multi-page executive company mission statements",
                        "D) Encouraging emojis"
                    ],
                    "answer": "B",
                    "explanation": "Language models operate on formal constraints; strict type signatures and schemas anchor probabilistic token generation to system boundaries."
                },
                {
                    "question": "How do you systematically prevent an AI model from importing unnecessary third-party packages?",
                    "options": [
                        "A) Disconnecting network adapters",
                        "B) Declaring explicit negative constraints: 'Zero external dependencies; use native runtime APIs only'",
                        "C) Writing all systems in pure Assembly",
                        "D) Reprimanding the model after generation"
                    ],
                    "answer": "B",
                    "explanation": "Explicit negative constraints restrict token generation pathways, steering the model toward native language features."
                }
            ]
        },

        # Chapter 6
        {
            "id": 6,
            "section_id": 1,
            "slug_tr": "ch06_ide_turbo_sarj_cursor_rules",
            "slug_en": "ch06_turbocharging_ide_cursor_rules",
            "title_tr": "Geliştirme Ortamını (IDE) Turbo Şarj Etmek: Cursor Rules ve Kısayollar",
            "title_en": "Turbocharging Your IDE: Cursor Rules, Shortcuts & Workflows",
            "subtitle_tr": "Her Seferinde Aynı Şeyleri Tekrarlamaktan Kurtulun",
            "subtitle_en": "Stop Repeating Yourself: Systematize Your Workflow with Custom Rules",
            "level_tr": "Başlangıç Seviyesi",
            "level_en": "Beginner Level",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Bir projede `.cursorrules` dosyası kullanmak ile kullanmamak arasındaki fark, junior bir mühendisin günlük üretkenliğini 2 kat artırabilir mi?",
            "podcast_hook_en": "Does introducing a repository `.cursorrules` or context config truly double daily engineering velocity, or is it just setup overhead?",
            "takeaways_tr": [
                "Cursor Rules (.cursorrules), takım standartlarınızı ve mimari kurallarınızı yapay zekanın kalıcı hafızasına kazır.",
                "Her prompta 'Türkçe yaz, Tailwind kullan, test ekle' demek yerine bu kuralları otomatikleştirin.",
                "Klavye kısayolları (Cmd+K, Cmd+L, Cmd+I) refleks haline geldiğinde kod yazma hızınız düşünme hızınıza yaklaşır."
            ],
            "takeaways_en": [
                "Repository rules (`.cursorrules`) permanently anchor architectural standards into the AI's system prompt.",
                "Stop manually typing 'Use TypeScript, write tests, follow functional style' into every prompt; codify it.",
                "Mastering shortcuts (Cmd+K for inline edits, Cmd+L for chat, Cmd+I for multi-file composer) aligns coding speed with thinking speed."
            ],
            "story_tr": """Her sabah kahve almaya gittiğiniz kafeyi hayal edin. Her gün baristaya: *"Benim adım Ali, laktozsuz sütlü, tek shot espressolu, kağıt bardakta bir latte istiyorum"* demek mi daha verimli; yoksa baristanın sizi gördüğü an: *"Ali Bey, her zamankinden mi?"* deyip 30 saniyede kahvenizi vermesi mi?

`.cursorrules` veya IDE kural dosyaları işte o baristadır! 

Projenizin kök dizinine koyacağınız küçük bir metin dosyası, yapay zekaya sizin kim olduğunuzu, projenin hangi dille yazıldığını, hangi mimari kalıpları kullandığınızı ve nelere ASLA izin vermediğinizi her saniye fısıldar.""",
            "story_en": """Consider visiting your local coffee shop every morning. Is it productive to repeat: *"Hello, I would like an oat milk cortado with a single shot in a ceramic cup"* every single day? Or is it superior when the barista nods and hands you your cortado in 20 seconds?

System rule files (like `.cursorrules` or `.agents/rules`) serve as that barista.

Placing a concise rules file in your repository root constantly reminds the AI model about your conventions, linting rules, test frameworks, and architectural red lines without you typing a single extra character.""",
            "mental_tr": """İdeal Bir `.cursorrules` Dosyası Anatomisi:

```markdown
# 1. Proje Kimliği ve Teknoloji Yığını (Stack)
- Next.js 14 (App Router), TypeScript Strict Mode, TailwindCSS.

# 2. Mimari Kurallar
- Asla 'any' kullanma; daima tam tip tanımla.
- React Server Component (RSC) varsayılandır; 'use client' sadece gerekli yerlerde.

# 3. Test ve Doğrulama
- Her yeni servis fonksiyonu için aynı isimde `.test.ts` dosyası üret.

# 4. Stil ve Format
- Erken dönüş (Early Return) desenini uygula.
- İç içe geçmiş if-else bloklarından kaçın.
```""",
            "mental_en": """Anatomy of an Effective `.cursorrules` File:

```markdown
# 1. Stack & Runtime
- Next.js App Router, TypeScript (Strict Mode), TailwindCSS.

# 2. Architectural Red Lines
- Never use `any`; define explicit interfaces for all payloads.
- React Server Components by default; add 'use client' only when hooks are required.

# 3. Verification & Testing
- Every new service must have a companion `.test.ts` file with unit tests.

# 4. Coding Conventions
- Prefer early returns over nested if-else pyramids.
- Prefer functional immutable helpers over mutable loops.
```""",
            "prompt_tr": """# GÖREV: Projemiz İçin Özel .cursorrules Dosyası Oluştur
Yeni bir Full-Stack projeye başlıyoruz.
Teknoloji Yığını:
- FastAPI (Python 3.12)
- Pydantic V2
- SQLAlchemy 2.0 (Async)
- PostgreSQL
- PyTest

Lütfen bu proje için AI'ın her zaman uyması gereken 5 maddelik katı bir `.cursorrules` içeriği hazırla.
Özellikle tip güvenliğine, async/await standartlarına ve test yazımına odaklansın.""",
            "prompt_en": """# TASK: Generate a Production-Grade .cursorrules Configuration
We are launching a modern backend service with:
- FastAPI (Python 3.12)
- Pydantic v2
- SQLAlchemy 2.0 (Async engine)
- PostgreSQL
- PyTest

Generate a concise, 5-pillar `.cursorrules` markdown file.
Focus on type safety, async/await correctness, and automated test generation.""",
            "code_lang": "markdown",
            "code_naive": """# Kötü .cursorrules: Çok uzun, laf kalabalığı dolu ve kural içermeyen metin
Sen harika bir yardımcısın. Benim için en iyi python kodlarını yaz.
Lütfen hata yapma ve her zaman nazik ol. Kodların çok temiz olsun.""",
            "code_robust": """# PROJE KURALLARI (.cursorrules)
## TEKNOLOJİ YIĞINI:
- Python 3.12, FastAPI, Pydantic v2, SQLAlchemy 2.0 (Async).

## KODLAMA STANDARTLARI:
1. TIP GÜVENLİĞİ: Tüm fonksiyonlarda type hints zorunludur. 'Any' yasaktır.
2. VERİTABANI: Asla senkron sorgu yazma; daima `await session.execute(...)` kullan.
3. MODELLER: Giriş/Çıkış için daima Pydantic şemalarını SQLAlchemy modellerinden ayır.
4. HATA YÖNETİMİ: HTTPException fırlatırken daima standart JSON hata yapısı kullan.
5. TESTLER: Her endpoint için en az 1 başarı ve 2 hata durumunu kapsayan pytest fonksiyonu yaz.""",
            "code_notes_tr": "Etkili kural dosyaları doğrudan emir kipleriyle, net yasaklarla ve teknoloji sürümleriyle yazılır. Model bu kuralları her işlemde 'Sistem Mesajı' olarak okur.",
            "code_notes_en": "High-impact rule files use imperative instructions, strict constraints, and explicit version designations. The model digests these as system instructions on every interaction.",
            "pitfalls_tr": [
                {"trap": "Kural dosyasına 50 sayfa dokümantasyon yapıştırıp context penceresini şişirmek.", "solution": "Kuralları 30-50 satır arasında, madde madde ve öz tutun."},
                {"trap": "Kural dosyasını yazıp git'e eklememek.", "solution": "`.cursorrules` dosyasını depoya commit edin, böylece tüm ekip arkadaşlarınız aynı AI davranışından faydalansın."},
                {"trap": "Kısayolları öğrenmeyip her şeyi fareyle tıklayarak yapmak.", "solution": "Günde en az 30 dakika farenizi bir kenara bırakıp IDE kısayollarını zorlayın."}
            ],
            "pitfalls_en": [
                {"trap": "Dumping 500 lines of prose into rules, exhausting system tokens.", "solution": "Keep rules concise, actionable, and under 50 lines."},
                {"trap": "Keeping rules local without committing to Git.", "solution": "Commit `.cursorrules` so the entire engineering team shares uniform AI output quality."},
                {"trap": "Navigating entirely with mouse clicks rather than keyboard shortcuts.", "solution": "Practice modal shortcuts (Cmd+K, Cmd+L, Cmd+I) until they become muscle memory."}
            ],
            "udemy_title_tr": "Ders 6: IDE'nizi Kişiselleştirmek - .cursorrules ile Takım Standartları",
            "udemy_title_en": "Lecture 6: Supercharging Your IDE - Standardizing Output via .cursorrules",
            "udemy_slides_tr": [
                ".cursorrules dosyası nedir ve nasıl çalışır?",
                "Kalıcı bağlam oluşturmanın faydaları.",
                "En kritik IDE kısayolları ve geliştirici iş akışı.",
                "Bölüm 1 Özeti: AI Çağında Yeni Nesil Yazılımcının Zihniyet Dönüşümü."
            ],
            "udemy_slides_en": [
                "What is a rules file and how do IDEs inject it?",
                "Eliminating repetitive prompt boilerplate forever.",
                "Essential keyboard shortcuts for high-velocity coding.",
                "Module 1 Recap: The Mental Shift of the AI-Driven Engineer."
            ],
            "udemy_demo_tr": "Proje kökünde `.cursorrules` oluşturun. 'Tüm fonksiyonlar Türkçe açıklama içermelidir ve TypeScript strict olmalıdır' kuralını yazın. Ardından basit bir fonksiyon isteyerek kuralın anında uygulandığını gösterin.",
            "udemy_demo_en": "Create a `.cursorrules` file in the repo root. Add a directive: 'Always generate JSDoc comments and strict TypeScript return types'. Prompt for a function and observe the rules take effect automatically.",
            "action_task_tr": "Bugün çalıştığınız projenin kök dizininde bir `.cursorrules` dosyası oluşturun ve projenizde uyulması gereken en önemli 3 mimari kuralı içine yazın.",
            "action_task_en": "Author a 20-line rules file in your active workspace specifying your runtime version, lint conventions, and testing library.",
            "quiz_tr": [
                {
                    "question": "Proje kök dizinindeki `.cursorrules` dosyasının temel işlevi nedir?",
                    "options": [
                        "A) Bilgisayara yeni RAM taktırmak",
                        "B) Projedeki her AI etkileşimine otomatik olarak mimari kuralları ve kodlama standartlarını sistem bağlamı olarak eklemek",
                        "C) Sadece git commitlerini silmek",
                        "D) CSS dosyalarını sıkıştırmak"
                    ],
                    "answer": "B",
                    "explanation": "Kural dosyaları, geliştiricinin her promptta aynı kuralları tekrarlamasına gerek kalmadan yapay zekayı proje standartlarına bağlı tutar."
                },
                {
                    "question": "Cursor IDE'sinde dosya içinde doğrudan kod düzenleme penceresini açan temel kısayol hangisidir?",
                    "options": [
                        "A) Ctrl + Alt + Del",
                        "B) Cmd + K (Windows'ta Ctrl + K)",
                        "C) F5",
                        "D) Shift + Escape"
                    ],
                    "answer": "B",
                    "explanation": "Cmd+K (veya Ctrl+K) editörde seçili kod üzerinde doğrudan satır içi düzenleme yapmayı sağlayan en yaygın AI kısayoludur."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the primary architectural purpose of a `.cursorrules` file?",
                    "options": [
                        "A) Increasing hardware clock speeds",
                        "B) Automatically injecting repository standards and constraints into the model's system context",
                        "C) Purging Git commit history",
                        "D) Compressing CSS bundles"
                    ],
                    "answer": "B",
                    "explanation": "Rules files automate context delivery, eliminating the need to repeatedly paste guidelines into every prompt."
                },
                {
                    "question": "Which keyboard shortcut opens the inline AI editing prompt in Cursor?",
                    "options": [
                        "A) Ctrl + Alt + Delete",
                        "B) Cmd + K (or Ctrl + K on Windows/Linux)",
                        "C) F5",
                        "D) Shift + Escape"
                    ],
                    "answer": "B",
                    "explanation": "Cmd+K activates the inline edit interface directly in the editor buffer."
                }
            ]
        }
    ]
