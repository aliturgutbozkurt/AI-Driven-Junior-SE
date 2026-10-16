"""
Section 6: Test Odaklı Geliştirme (TDD) & Kalite Güvencesi (Chapters 31 to 36)
"""

def get_section_chapters():
    return [
        # Chapter 31
        {
            "id": 31,
            "section_id": 6,
            "slug_tr": "ch31_neden_test_yazariz_test_piramidi",
            "slug_en": "ch31_why_we_test_the_testing_pyramid",
            "title_tr": "Neden Test Yazarız? Test Piramidini Anlamak",
            "title_en": "Why We Test: Demystifying the Testing Pyramid for AI Engineers",
            "subtitle_tr": "'Kodum Zaten Çalışıyor' Tuzağından Kurtulup Gece Rahat Uyuma Sanatı",
            "subtitle_en": "Escaping the 'It Works on My Machine' Delusion to Sleep Peacefully on Deploy Day",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Junior yazılımcılar neden test yazmayı vakit kaybı olarak görür ve test yazmayan bir şirketin iflas etmesi neden sadece bir zaman meselesidir?",
            "podcast_hook_en": "Why do junior engineers frequently dismiss tests as redundant overhead, and why is shipping untested software a mathematical guarantee of catastrophic bugs?",
            "takeaways_tr": [
                "Test yazmak bugünü değil; 6 ay sonra o kodu değiştirecek olan gelecekteki sizi korur (Regresyon Güvencesi).",
                "Test Piramidi: Tabanda çok sayıda hızlı Unit Test, ortada Entegrasyon Testleri, tepede az sayıda E2E Test olmalıdır.",
                "AI kod üretirken test yazımı artık saatler değil saniyeler sürer; test yazmamak için hiçbir mazeret kalmamıştır."
            ],
            "takeaways_en": [
                "Automated testing protects your future self when refactoring logic 6 months from now (Regression Shield).",
                "The Testing Pyramid: Hundreds of lightning-fast Unit Tests at the base, Integration tests in the middle, and selective E2E tests at the apex.",
                "With AI generating test fixtures in seconds, there is zero professional justification for shipping untested modules."
            ],
            "story_tr": """Bir paraşüt imalathanesinde çalıştığınızı düşünün.

Yeni bir paraşüt diktiniz. Patronunuz gelip soruyor: *"Bu paraşüt açılacak mı?"*
Siz de diyorsunuz ki: *"Valla patron kumaşı çok güzel diktim, rengi de harika, kesin açılır!"*
Patron o paraşütle uçaktan atlar mı? Asla! Önce yerde rüzgar tünelinde binlerce kez açılma testine sokulur.

Yazılımda canlıya (production) kod atmak, o paraşütle 10.000 metreden atlamaktır.

Eğer test yazmadıysanız, her cuma akşamı canlıya güncelleme çıktığınızda kabus görürsünüz. Oysa test piramidine sahip bir mühendis, butona basıp kahvesini yudumlayarak hafta sonuna girer.""",
            "story_en": """Imagine working on a parachute manufacturing line.

You just completed sewing a fresh nylon canopy. The plant manager approaches and asks: *"Will this parachute deploy reliably at terminal velocity?"*
You reply: *"I selected durable thread and the fabric looks pristine, so it'll probably open!"*
Would anyone jump out of a plane with that rig? Not a chance. The canopy undergoes thousands of stress cycles inside a wind tunnel first.

Deploying untested software to production is jumping out of an aircraft at 30,000 feet.

Without automated test suites, every production deployment triggers acute anxiety. With an automated testing pyramid, clicking 'Deploy' is routine, predictable, and stress-free.""",
            "mental_tr": """Test Piramidi Anatomisi:

```
            /\\
           /  \\     ──> 1. E2E (Uçtan Uca) Testler (%10)
          / E2E\\    Tarayıcıyı açar, tıklar. Çok yavaş (dakikalar) ve kırılgan.
         /──────\\
        /  INTEG \\  ──> 2. Entegrasyon Testleri (%20)
       /  RATION  \\ Veritabanı ve API bağlantılarını test eder. Orta hız.
      /────────────\\
     /  UNIT TESTS  \\ ──> 3. Birim (Unit) Testler (%70)
    /────────────────\\ Saf fonksiyonları izole test eder. Işık hızında (milisaniyeler).
```""",
            "mental_en": """The Classic Testing Pyramid:

```
            /\\
           /  \\     ──> 1. End-to-End (E2E) Tests (~10%)
          / E2E\\    Automates live browser clicks. High latency (minutes), higher flake rate.
         /──────\\
        /  INTEG \\  ──> 2. Integration Tests (~20%)
       /  RATION  \\ Validates boundaries between database, cache, and HTTP handlers.
      /────────────\\
     /  UNIT TESTS  \\ ──> 3. Unit Tests (~70%)
    /────────────────\\ Tests pure algorithmic logic in isolation. Sub-millisecond execution.
```""",
            "prompt_tr": """# ROL: Test ve Kalite Güvencesi (QA) Mimarı
Bir e-ticaret sepet hesaplama fonksiyonu yazdık.

## GÖREV:
Test Piramidi felsefesine uygun olarak bu fonksiyon için 3 katmanda hangi testlerin yazılması gerektiğini planla:
1. 3 adet kritik Unit Test senaryosu (saf fonksiyon girdileri ve sınır değerler)
2. 1 adet Entegrasyon Testi senaryosu (Veritabanından ürün fiyatı çekip sepeti hesaplama)
3. 1 adet E2E Test senaryosu (Kullanıcının butona tıklayıp sepet toplamını ekranda görmesi)""",
            "prompt_en": """# ROLE: QA & Test Architecture Specialist
We developed an e-commerce checkout calculation engine.

## TASK:
Outline a comprehensive Testing Pyramid strategy across all 3 tiers:
1. Three critical Unit Test scenarios covering boundary values and discount caps.
2. One Integration Test validating database price lookups against the calculation engine.
3. One E2E Test validating a user clicking 'Add to Cart' and asserting the UI total updates.""",
            "code_lang": "typescript",
            "code_naive": """// Test Yazmayan Geliştirici: "Konsolda yazdırdım, çalışıyor!"
function calculateTotal(price: number, quantity: number) {
  return price * quantity;
}
console.log(calculateTotal(10, 2)); // "20 çıktı, tamamdır deploy edelim!"
// Negatif sayı gelirse ne olur? Float yuvarlama ne olur? Bilen yok!""",
            "code_robust": """// Profesyonel Mühendis: Jest ile Kapsamlı Birim Test Paketi (calculator.test.ts)
import { calculateCartTotal } from "./calculator";

describe("calculateCartTotal - Birim Test Paketi", () => {
  it("standart ürünlerde sepet toplamını doğru hesaplamalıdır", () => {
    const items = [{ price: 100, quantity: 2 }, { price: 50, quantity: 1 }];
    expect(calculateCartTotal(items)).toBe(250);
  });

  it("boş sepette 0 döndürmelidir", () => {
    expect(calculateCartTotal([])).toBe(0);
  });

  it("negatif fiyat veya adet girildiğinde RangeError fırlatmalıdır", () => {
    const invalidItems = [{ price: -10, quantity: 1 }];
    expect(() => calculateCartTotal(invalidItems)).toThrow(RangeError);
  });

  it("ondalıklı kuruş tutarlarını 2 haneye doğru yuvarlamalıdır (0.1 + 0.2 hassasiyeti)", () => {
    const items = [{ price: 19.99, quantity: 3 }];
    expect(calculateCartTotal(items)).toBe(59.97);
  });
});""",
            "code_notes_tr": "Birim testler; sınır değerlerini (boş sepet, negatif sayılar, ondalık hassasiyet) saniyenin binde birinde test ederek kod tabanına kırılmaz bir güvenlik kalkanı örer.",
            "code_notes_en": "Unit test suites validate boundary conditions (empty carts, negative values, floating precision) in fractions of a millisecond, establishing an automated regression safety shield.",
            "pitfalls_tr": [
                {"trap": "Sadece mutlu senaryoyu (Happy Path) test edip hata durumlarını atlamak.", "solution": "Testlerinizin en az %60'ı 'kullanıcı yanlış girdiğinde ne olur?' sorusuna odaklanmalıdır."},
                {"trap": "Hiç unit test yazmadan sadece 50 tane aşırı yavaş E2E testi yazmak (Ters Piramit Antipattern).", "solution": "Piramidi dik tutun: %70 Unit, %20 Integration, %10 E2E."},
                {"trap": "Testler hata verdiğinde testi düzeltmek yerine `expect(true).toBe(true)` yazıp geçiştirmek.", "solution": "Testi susturmayın; test sizin can simidinizdir, hatayı kaynakta çözün."}
            ],
            "pitfalls_en": [
                {"trap": "Testing exclusively the happy path while ignoring error states.", "solution": "Devote at least 60% of assertions to edge cases, malformed payloads, and network failures."},
                {"trap": "Skipping unit tests to write 50 fragile, slow E2E tests (Inverted Testing Pyramid).", "solution": "Preserve the pyramid: ~70% Unit, ~20% Integration, ~10% E2E."},
                {"trap": "Silencing broken assertions with `test.skip` or tautologies like `expect(true).toBe(true)`.", "solution": "Treat failing tests as high-signal smoke alarms; diagnose and resolve root causes."}
            ],
            "udemy_title_tr": "Ders 31: Neden Test Yazarız? - Test Piramidinin Gücü",
            "udemy_title_en": "Lecture 31: Why We Test - Mastering the Testing Pyramid",
            "udemy_slides_tr": [
                "'Kodum çalışıyor' yanılgısı ve regresyon riski.",
                "Test Piramidi: Unit vs Integration vs E2E testler.",
                "Happy Path vs Edge Case (Sınır Durum) dengesi.",
                "Canlı Demo: Jest ile 10 milisaniyede 4 test çalıştırmak."
            ],
            "udemy_slides_en": [
                "The 'It works on my machine' fallacy and regression debt.",
                "Deconstructing the Testing Pyramid: Unit, Integration, and E2E.",
                "Happy path vs. Edge case assertion strategies.",
                "Live demo: Executing 4 Jest assertions in under 10 milliseconds."
            ],
            "udemy_demo_tr": "Terminalde Jest'i izleme modunda (`npm test -- --watch`) açın. Test dosyasında bilinçli olarak bir kuralı değiştirip testin anında kırmızıya döndüğünü, kodu düzeltince saniyesinde yeşile döndüğünü gösterin.",
            "udemy_demo_en": "Launch Jest in interactive watch mode (`npm test -- --watch`). Modify business logic to trigger an instant red failure, then correct the implementation to demonstrate sub-second green feedback.",
            "action_task_tr": "Bugün yazdığınız bir fonksiyona en az 3 farklı senaryoyu (başarılı durum, boş girdi, hatalı girdi) kapsayan bir Jest veya PyTest dosyası yazın.",
            "action_task_en": "Write a unit test suite covering at least 3 scenarios (nominal success, empty input, boundary exception) for a function in your active repository.",
            "quiz_tr": [
                {
                    "question": "Yazılım geliştirmede 'Regresyon Hatası' (Regression Bug) ne demektir?",
                    "options": [
                        "A) Yeni bir özellik eklerken veya kodu refactor ederken, daha önce kusursuz çalışan eski bir özelliğin farkında olmadan bozulması",
                        "B) Bilgisayarın klavyesinin bozulması",
                        "C) Sadece Python'da çıkan söz dizimi hatası",
                        "D) İnternet hızının düşmesi"
                    ],
                    "answer": "A",
                    "explanation": "Regresyon hatası, yeni yapılan bir değişikliğin eski çalışan kodları sessizce kırmasıdır. Otomatik testlerin birincil varoluş sebebi regresyonları anında yakalamaktır."
                },
                {
                    "question": "Test Piramidi'ne göre bir projede en çok hangi test türünden bulunmalıdır?",
                    "options": [
                        "A) E2E Testler",
                        "B) Birim (Unit) Testler (%70 civarında, hızlı ve izole)",
                        "C) Manuel Testler",
                        "D) Güvenlik Testleri"
                    ],
                    "answer": "B",
                    "explanation": "Birim testler milisaniyeler içinde çalıştığı ve spesifik mantık hatalarını doğrudan gösterdiği için piramidin en geniş tabanını oluşturur."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the engineering definition of a 'Regression Bug'?",
                    "options": [
                        "A) Introducing a novel feature that inadvertently breaks previously functional capabilities",
                        "B) Hardware keyboard driver failures",
                        "C) Syntax errors unique to Python interpreters",
                        "D) Local Wi-Fi bandwidth degradation"
                    ],
                    "answer": "A",
                    "explanation": "Regressions occur when modifications unintentionally compromise existing system behavior. Automated suites serve as continuous regression catchers."
                },
                {
                    "question": "According to the Testing Pyramid, which tier should dominate total test count?",
                    "options": [
                        "A) End-to-End browser tests",
                        "B) Unit tests (~70% of total assertions, fast and isolated)",
                        "C) Manual smoke tests",
                        "D) Penetration scans"
                    ],
                    "answer": "B",
                    "explanation": "Unit tests run in milliseconds and pinpoint root-cause defects directly, forming the expansive foundation of the pyramid."
                }
            ]
        },

        # Chapter 32
        {
            "id": 32,
            "section_id": 6,
            "slug_tr": "ch32_unit_test_jest_pytest_mocklama",
            "slug_en": "ch32_unit_testing_jest_pytest_mocking",
            "title_tr": "Birim Testlerini AI ile Hızlandırmak: Jest, PyTest ve Mocklama",
            "title_en": "Unit Testing Accelerated by AI: Jest, PyTest & Mocking Masters",
            "subtitle_tr": "Gerçek Veritabanına veya API'ye Bağlanmadan Test Yazma Sanatı",
            "subtitle_en": "Mocking Databases and Network Calls to Run 1,000 Tests in 2 Seconds",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Unit test koşarken gerçek veritabanına bağlanmak veya gerçek kredi kartından para çekmeye çalışmak neden bir felakettir ve 'Mock' kavramı sistemi nasıl kurtarır?",
            "podcast_hook_en": "Why is connecting to real production databases or live payment gateways during unit tests reckless, and how does mock virtualization make test runs lightning fast?",
            "takeaways_tr": [
                "Birim testler tamamen deterministik ve dış dünyadan (ağ, disk, saat) yalıtılmış (izole) olmalıdır.",
                "Mocklama (Mocking), dış bağımlılıkları (Stripe API, PostgreSQL, E-posta servisi) sahte ama kontrollü nesnelerle değiştirmektir.",
                "AI modelleri, karmaşık servislerin mock objelerini ve test tablolarını (fixture) saniyeler içinde üretebilir."
            ],
            "takeaways_en": [
                "Unit assertions must remain strictly deterministic and decoupled from ambient side effects (network, disk, system clocks).",
                "Mocking substitutes real external collaborators (Stripe, PostgreSQL, SES) with predictable, controlled test doubles.",
                "AI tooling excels at generating comprehensive mock fixtures and boundary test suites on demand."
            ],
            "story_tr": """Tıp fakültesinde ameliyat eğitimi alan bir cerrah adayını düşünün.

İlk gün profesör öğrencinin eline neşteri verip: *"Hadi sedyedeki gerçek hastanın kalbini aç ve ameliyat et!"* der mi? Tabii ki hayır! Öğrenci önce silikon mankenler ve simülasyon cihazları üzerinde yüzlerce kez dikiş atar.

Yazılımda **Mock (Sahte Obje)** işte o silikon mankendir!

Eğer unit test yazarken gerçek Stripe API'sine gidip gerçek kredi kartından 100 dolar çekmeye kalkarsanız, test her çalıştığında şirket batar! Mock kullanarak Stripe'ın döndüğü cevabı taklit eder ve kodunuzun mantığını güvenle doğrularsınız.""",
            "story_en": """Consider a surgical resident in their first week of medical residency.

Does the chief surgeon hand them a scalpel and command: *"Proceed to perform open-heart surgery on this living patient in Room 4"?* Never. Residents practice on synthetic silicone mannequins and VR haptic simulators hundreds of times.

In software engineering, a **Mock** is that synthetic silicone mannequin.

If your automated unit test suite charges a live production Stripe card during every run, you will bankrupt the organization. By substituting live APIs with deterministic mock doubles, you verify business execution safely.""",
            "mental_tr": """Mocklama Mimarisi:

```
[Test Ortamı (Jest / PyTest)]
              │
              ▼
[Sipariş Servisi (Test Edilen Kod - SUT)]
              │
      ┌───────┴───────┐
      ▼               ▼
[GERÇEK DÜNYA]   [MOCK DÜNYASI]
❌ Canlı DB      ✅ jest.fn().mockResolvedValue({ id: 1, balance: 1000 })
❌ Canlı Stripe  ✅ jest.spyOn(stripe, 'charge').mockResolvedValue({ success: true })
(Çok yavaş,      (Işık hızında, sıfır maliyet, %100 kontrol)
bağlantı kopar)
```""",
            "mental_en": """The Mock Isolation Boundary:

```
[Automated Test Harness (Jest / PyTest)]
                  │
                  ▼
[OrderProcessor (System Under Test - SUT)]
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
[PRODUCTION I/O]     [TEST DOUBLE / MOCK]
❌ Live PostgreSQL   ✅ `jest.fn().mockResolvedValue({ id: 1, balance: 500 })`
❌ Live Stripe API   ✅ `jest.spyOn(stripe, 'charge').mockResolvedValue({ id: 'ch_test' })`
(Slow, costly,       (Instant execution, zero network overhead, deterministic)
network dependent)
```""",
            "prompt_tr": """# ROL: Test Mühendisi ve Jest Gurusu
Aşağıdaki ödeme servisi fonksiyonu için Jest birim testleri yazacağız.

## SERVİS KODU:
```typescript
export async function payInvoice(invoiceId: string, stripeClient: StripeSDK, db: Database) {
  const invoice = await db.findInvoice(invoiceId);
  if (invoice.isPaid) throw new Error("Fatura zaten ödenmiş.");

  const charge = await stripeClient.charges.create({ amount: invoice.amount });
  await db.markAsPaid(invoiceId, charge.id);
  return { success: true, chargeId: charge.id };
}
```

## GÖREV:
1. `stripeClient` ve `db` nesnelerini `jest.fn()` kullanarak mockla (sahte nesneler üret).
2. Başarılı ödeme durumunu test et (`markAsPaid` fonksiyonunun doğru argümanlarla çağrıldığını doğrula).
3. Fatura zaten ödendiğinde Stripe'a ASLA çağrı yapılmadığını (`expect(stripeClient.charges.create).not.toHaveBeenCalled()`) kanıtla.""",
            "prompt_en": """# ROLE: Lead Test Architect & Jest Specialist
We are authoring isolated unit tests for this invoice payment service:

## SERVICE METHOD:
```typescript
export async function payInvoice(invoiceId: string, stripeClient: StripeSDK, db: Database) {
  const invoice = await db.findInvoice(invoiceId);
  if (invoice.isPaid) throw new Error("Invoice already settled.");

  const charge = await stripeClient.charges.create({ amount: invoice.amount });
  await db.markAsPaid(invoiceId, charge.id);
  return { success: true, chargeId: charge.id };
}
```

## TASK:
1. Mock `stripeClient` and `db` dependencies using `jest.fn()`.
2. Write a test asserting that successful payments invoke `db.markAsPaid` with the correct charge ID.
3. Assert that when an invoice is already marked paid, Stripe's charge API is never invoked (`expect(...).not.toHaveBeenCalled()`).""",
            "code_lang": "typescript",
            "code_naive": """// Kötü Test: Dış bağımlılıkları mocklamadan gerçek veritabanı beklemek
it("faturayı öder", async () => {
  // Eğer PostgreSQL sunucusu açık değilse test patlar!
  const res = await payInvoice("123", new RealStripe(), new RealDB());
  expect(res.success).toBe(true);
});""",
            "code_robust": """import { payInvoice } from "./paymentService";

describe("payInvoice - Birim Test Paketi (Mocklanmış)", () => {
  let mockDb: any;
  let mockStripe: any;

  beforeEach(() => {
    // Her test öncesi temiz mock nesneleri oluşturulur
    mockDb = {
      findInvoice: jest.fn(),
      markAsPaid: jest.fn().mockResolvedValue(true)
    };
    mockStripe = {
      charges: {
        create: jest.fn().mockResolvedValue({ id: "ch_mock_123" })
      }
    };
  });

  it("ödenmemiş faturayı başarıyla tahsil edip veritabanını günceller", async () => {
    mockDb.findInvoice.mockResolvedValue({ id: "inv_1", amount: 1500, isPaid: false });

    const result = await payInvoice("inv_1", mockStripe, mockDb);

    expect(result.success).toBe(true);
    expect(result.chargeId).toBe("ch_mock_123");
    // Yan etkilerin doğrulanması (Assertion of side-effects)
    expect(mockStripe.charges.create).toHaveBeenCalledWith({ amount: 1500 });
    expect(mockDb.markAsPaid).toHaveBeenCalledWith("inv_1", "ch_mock_123");
  });

  it("zaten ödenmiş faturada Stripe çağrısı yapmadan hata fırlatmalıdır", async () => {
    mockDb.findInvoice.mockResolvedValue({ id: "inv_2", amount: 500, isPaid: true });

    await expect(payInvoice("inv_2", mockStripe, mockDb)).rejects.toThrow("Fatura zaten ödenmiş.");

    // GÜVENLİK KONTROLÜ: Stripe asla çağrılmamalıdır!
    expect(mockStripe.charges.create).not.toHaveBeenCalled();
    expect(mockDb.markAsPaid).not.toHaveBeenCalled();
  });
});""",
            "code_notes_tr": "Bu testler ne internet bağlantısına ne de canlı bir veritabanına ihtiyaç duyar. 1000 adet böyle test toplam 1.5 saniyede koşar ve tüm iş kurallarını %100 doğrular.",
            "code_notes_en": "These tests execute with zero external network connectivity or database instances. A suite of 1,000 such tests runs in under 2 seconds, verifying edge-case business invariants deterministically.",
            "pitfalls_tr": [
                {"trap": "Testler arasında mock durumlarını sıfırlamayı unutup testlerin birbirini kirletmesi (Flaky Tests).", "solution": "Her testten önce `beforeEach(() => jest.clearAllMocks())` çalıştırın."},
                {"trap": "Test edilen kodun mantığını değil, mock nesnesinin kendisini test etmek.", "solution": "Mock sadece girdiyi sağlar; test ettiğiniz şey kendi yazdığınız servis fonksiyonudur."},
                {"trap": "Mock kütüphanesinin gerçek API ile uyumsuz hale gelmesi (Stale Mock).", "solution": "TypeScript interface'leri kullanarak mock nesnelerin gerçek tipleri implemente etmesini zorunlu kılın."}
            ],
            "pitfalls_en": [
                {"trap": "Failing to reset mocks between test cases, inducing state leakage and flaky runs.", "solution": "Call `beforeEach(() => jest.clearAllMocks())` to guarantee state hygiene."},
                {"trap": "Testing the mock implementation rather than system-under-test logic.", "solution": "Mocks supply preconditions; assertions must validate domain behavior."},
                {"trap": "Letting mock schemas drift out of sync with evolving external APIs (Stale Mocks).", "solution": "Enforce strict TypeScript interfaces on mock factories."}
            ],
            "udemy_title_tr": "Ders 32: Birim Testleri & Mocklama - Jest ve PyTest Ustalığı",
            "udemy_title_en": "Lecture 32: Accelerated Unit Testing - Mastering Jest, PyTest & Mocks",
            "udemy_slides_tr": [
                "Determinizm kuralı: Unit test neden dış dünyadan izole olmalıdır?",
                "Mock, Stub ve Spy kavramları arasındaki farklar.",
                "Jest ile bağımlılık enjeksiyonunu (DI) mocklamak.",
                "Canlı Demo: 1000 testi 2 saniyede koşan mock altyapısı kurmak."
            ],
            "udemy_slides_en": [
                "The determinism mandate: Isolating unit tests from ambient I/O.",
                "Demystifying test doubles: Mocks, Stubs, and Spies.",
                "Mocking dependency injection boundaries in Jest.",
                "Live demo: Executing 1,000 mock assertions in 2 seconds."
            ],
            "udemy_demo_tr": "Bir hava durumu API'si çağıran fonksiyon yazın. İnterneti kapatın (offline moda geçin). Jest ile API yanıtını mocklayarak testin internet olmadan 5 milisaniyede geçtiğini canlı konsolda gösterin.",
            "udemy_demo_en": "Author a weather lookup function. Disconnect local network connectivity. Execute a mock Jest suite and demonstrate passing assertions in 5ms without live internet.",
            "action_task_tr": "Projenizde harici bir API (hava durumu, ödeme veya e-posta) çağıran bir servisi bulun ve Jest mock (`jest.fn()`) kullanarak izole bir test yazın.",
            "action_task_en": "Author an isolated unit test for an external third-party API integration in your project, replacing network calls with `jest.fn()` mocks.",
            "quiz_tr": [
                {
                    "question": "Birim testlerde 'Mock' kullanmanın birincil teknik gerekçesi nedir?",
                    "options": [
                        "A) Kodun satır sayısını artırmak",
                        "B) Ağ, veritabanı veya üçüncü taraf API gibi yavaş, maliyetli ve güvenilmez dış bağımlılıkları sahte ama kontrollü nesnelerle ikame ederek testleri hızlı ve deterministik kılmak",
                        "C) Sadece Python dilinde geçerli bir zorunluluk olması",
                        "D) CSS hatalarını engellemek"
                    ],
                    "answer": "B",
                    "explanation": "Mock nesneler dış bağımlılıkları yalıtır; testlerin internet veya veritabanı olmadan mikrosaniyeler içinde tutarlı çalışmasını sağlar."
                },
                {
                    "question": "Jest testlerinde `expect(mockFunction).not.toHaveBeenCalled()` assertion'ı neyi doğrular?",
                    "options": [
                        "A) Fonksiyonun çöktüğünü",
                        "B) Belirtilen sahte fonksiyonun test senaryosu boyunca hiçbir koşulda tetiklenmediğini (istenmeyen yan etkinin oluşmadığını)",
                        "C) Bilgisayarın kapandığını",
                        "D) Testin başarısız sayılması gerektiğini"
                    ],
                    "answer": "B",
                    "explanation": "Bu ifade, istenmeyen durumlarda (örn. geçersiz şifre veya ödenmiş fatura) kritik fonksiyonların (örn. para çekme) asla çağrılmadığını garanti altına alır."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the primary technical rationale for utilizing Mocks in unit testing suites?",
                    "options": [
                        "A) Artificially expanding project code volume",
                        "B) Decoupling tests from slow, non-deterministic external I/O (network calls, disks, third-party APIs) to guarantee fast, deterministic runs",
                        "C) Compliance with Python-only standards",
                        "D) Preventing CSS layout glitches"
                    ],
                    "answer": "B",
                    "explanation": "Mocks virtualize external boundaries, ensuring test execution completes in milliseconds without network or database dependencies."
                },
                {
                    "question": "What invariant is validated by `expect(mockFunction).not.toHaveBeenCalled()` in Jest?",
                    "options": [
                        "A) The method suffered a stack overflow",
                        "B) The target mock was never executed during the test, ensuring unintended side-effects were properly averted",
                        "C) The host machine terminated execution",
                        "D) The suite failed"
                    ],
                    "answer": "B",
                    "explanation": "It proves that guarded execution paths prevent dangerous side-effects (like duplicate credit card charges) under negative conditions."
                }
            ]
        },

        # Chapter 33
        {
            "id": 33,
            "section_id": 6,
            "slug_tr": "ch33_entegrasyon_ve_e2e_testleri_playwright",
            "slug_en": "ch33_integration_and_e2e_testing_playwright",
            "title_tr": "Entegrasyon ve E2E Testleri: Playwright ile Uçtan Uca Doğrulama",
            "title_en": "Integration & End-to-End Testing with Playwright: Full-Stack Verification",
            "subtitle_tr": "Tüm Parçaların Bir Araya Geldiğinde Doğru Çalıştığını Kanıtlamak",
            "subtitle_en": "Automating Real Browser Clicks, Form Submissions, and Full-Stack User Flows",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Tüm unit testler yeşil yanarken (başarılıyken) bir web sitesinde 'Giriş Yap' butonu tıklandığında neden hiçbir şey olmaz? Entegrasyon testleri neden bu kör noktayı çözer?",
            "podcast_hook_en": "Why can an application boast 100% passing unit tests yet completely fail when a real user clicks the checkout button? How does Playwright bridge this chasm?",
            "takeaways_tr": [
                "200 adet mükemmel çalışan birim test, iki modülün birbiriyle konuştuğu sınırda (interface) hata olmayacağını garanti etmez.",
                "Playwright, modern web uygulamalarını gerçek Chromium, Firefox ve WebKit tarayıcılarında headless olarak test eden altın standarttır.",
                "E2E testleri sadece en kritik 'kullanıcı yolculuklarına' (User Journey - Kayıt, Ödeme, Giriş) uygulanmalıdır."
            ],
            "takeaways_en": [
                "A suite of 500 passing unit tests provides zero guarantee that two integrated systems agree on HTTP payload schemas.",
                "Playwright represents the industry gold standard for automating real browser interactions across Chromium, Firefox, and WebKit.",
                "Reserve E2E test suites strictly for business-critical user journeys (Sign-up, Authentication, Payment Funnels)."
            ],
            "story_tr": """İki mühendisin harika bir ev inşa ettiğini düşünün:

Biri dünyanın en kaliteli kapı kilidini üretti (Unit Test %100 başarılı).
Diğeri ise dünyanın en sağlam ahşap kapısını yaptı (Unit Test %100 başarılı).

Fakat kapıyı yerine monte ettiklerinde bir baktılar: Kilit solda, kilit deliği sağda! Kapı kilitlenemiyor! İşte bu bir **Entegrasyon Hatasıdır**.

Birim testler parçaların tek başına sağlam olduğunu gösterir. **Entegrasyon ve E2E (Playwright) testleri** ise kapıyı duvara takıp anahtarı çeviren, kolu indiren ve kapının gerçekten kilitlendiğini gören nihai testtir.""",
            "story_en": """Imagine two skilled craftsmen building a house entrance:

One manufactures the world's most intricate mechanical deadbolt (Unit Test: 100% passing).
The other builds a heavy solid oak door (Unit Test: 100% passing).

When assembling the door on-site, they discover the deadbolt is mounted on the left while the doorframe strike plate is on the right! The door cannot lock. That is an **Integration Defect**.

Unit tests prove individual gears spin. **End-to-End tests (via Playwright)** turn the brass key, depress the handle, and verify the door actually latches shut.""",
            "mental_tr": """Test Kapsamının Gerçeklik Seviyesi:

```
[Birim Test (Jest)]          ──> "Fonksiyon matematiksel olarak doğru mu?"
             │
             ▼
[Entegrasyon Testi (Supertest)] ──> "Express rotası veritabanına gerçekten yazıyor mu?"
             │
             ▼
[E2E Testi (Playwright)]       ──> "Kullanıcı tarayıcıda formu doldurup tıkladığında başarı mesajını görüyor mu?"
```""",
            "mental_en": """Hierarchy of Test Realism:

```
[Unit Test (Jest / PyTest)]        ──> "Is the isolated algorithm mathematically correct?"
             │
             ▼
[Integration Test (Supertest)]     ──> "Does the HTTP controller successfully persist to PostgreSQL?"
             │
             ▼
[E2E Test (Playwright Engine)]     ──> "Does a real browser render DOM updates after clicking 'Submit'?"
```""",
            "prompt_tr": """# ROL: E2E Test Otomasyon Mühendisi
Playwright ve TypeScript kullanarak bir e-ticaret sitesinin 'Kullanıcı Girişi (Login Flow)' için E2E testi yazacağız.

## GEREKSİNİMLER:
1. `http://localhost:3000/login` sayfasına git.
2. E-posta ve şifre inputlarını doldur.
3. 'Giriş Yap' butonuna tıkla.
4. Başarılı girişte `/dashboard` sayfasına yönlendirildiğini ve sayfada 'Hoş geldin Ali' yazısının belirdiğini doğrula.
5. Hatalı şifre girildiğinde ekranda beliren kırmızı hata kutusunu test et.""",
            "prompt_en": """# ROLE: E2E Automation Lead & Playwright Specialist
Author an end-to-end authentication test suite in TypeScript using Playwright:

## REQUIREMENTS:
1. Navigate to `http://localhost:3000/login`.
2. Fill the email and password form fields.
3. Click the 'Sign In' submission button.
4. Assert redirection to `/dashboard` and verify greeting text 'Welcome Back'.
5. Implement a negative assertion verifying an alert appears upon invalid password entry.""",
            "code_lang": "typescript",
            "code_naive": """// Kötü E2E Test: Kırılgan CSS seçicileri ve sabit bekleme (sleep) tuzağı
test("login naive", async ({ page }) => {
  await page.goto("http://localhost:3000/login");
  await page.click(".btn-primary-2"); // Kırılgan CSS! Buton stili değişirse test çöker!
  await page.waitForTimeout(5000); // KÖTÜ: 5 saniye boşuna beklemek testi yavaşlatır!
});""",
            "code_robust": """import { test, expect } from "@playwright/test";

test.describe("Kullanıcı Giriş Akışı (Login Flow)", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/login");
  });

  test("geçerli bilgilerle giriş yapıldığında dashboard'a yönlendirmelidir", async ({ page }) => {
    // Erişilebilir (Accessible) Rol ve Label Seçicileri (Sağlam & Kırılmaz)
    await page.getByLabel("E-Posta Adresi").fill("ali@example.com");
    await page.getByLabel("Şifre").fill("GuvenliSifre123!");
    await page.getByRole("button", { name: "Giriş Yap" }).click();

    // Otomatik Bekleme (Auto-waiting): URL ve içerik gelene kadar dinamik bekler
    await expect(page).toHaveURL(/.*dashboard/);
    await expect(page.getByRole("heading", { name: "Hoş Geldin Ali" })).toBeVisible();
  });

  test("hatalı şifrede açıklayıcı hata mesajı göstermelidir", async ({ page }) => {
    await page.getByLabel("E-Posta Adresi").fill("ali@example.com");
    await page.getByLabel("Şifre").fill("YanlisSifre!");
    await page.getByRole("button", { name: "Giriş Yap" }).click();

    const alert = page.getByRole("alert");
    await expect(alert).toBeVisible();
    await expect(alert).toContainText("Geçersiz e-posta veya şifre.");
  });
});""",
            "code_notes_tr": "`getByLabel` ve `getByRole` gibi erişilebilirlik (ARIA) seçicileri kullanılarak UI değişikliklerine karşı dayanıklılık sağlanmış; `page.waitForTimeout` yerine Playwright'ın dahili 'Auto-Waiting' özelliğiyle testler maksimum hızda çalıştırılmıştır.",
            "code_notes_en": "Using semantic locators (`getByRole`, `getByLabel`) immunizes tests against styling shifts. Relying on Playwright's native auto-waiting mechanisms eliminates arbitrary `sleep` timeouts entirely.",
            "pitfalls_tr": [
                {"trap": "Testlerde `page.waitForTimeout(3000)` (sabit uyku) kullanıp test koşu sürelerini uzatmak.", "solution": "Sabit sleep yerine Playwright'ın otomatik bekleyen `expect(locator).toBeVisible()` metodlarını kullanın."},
                {"trap": "Kırılgan CSS seçicileri (`div > div.col-md-4 > button`) kullanmak.", "solution": "Daima kullanıcı odaklı ARIA seçicileri (`getByRole`, `getByText`) veya `data-testid` kullanın."},
                {"trap": "Her küçük buton için E2E testi yazıp CI pipeline süresini 45 dakikaya çıkarmak.", "solution": "E2E testlerini sadece kritik kullanıcı akışları için yazın; detayları Unit testlere bırakın."}
            ],
            "pitfalls_en": [
                {"trap": "Injecting arbitrary delays via `page.waitForTimeout(5000)`.", "solution": "Rely exclusively on Playwright's web-first assertions which poll dynamically until elements appear."},
                {"trap": "Tying locators to fragile structural DOM paths (`div > div:nth-child(2)`).", "solution": "Anchor locators to accessible user semantics (`getByRole('button')`) or explicit `data-testid` attributes."},
                {"trap": "Authoring hundreds of redundant E2E tests, ballooning CI runtimes to 45 minutes.", "solution": "Limit E2E tests strictly to top-level business journeys; defer edge cases to unit tests."}
            ],
            "udemy_title_tr": "Ders 33: Uçtan Uca Testler - Playwright ile Tarayıcı Otomasyonu",
            "udemy_title_en": "Lecture 33: End-to-End Testing - Browser Automation with Playwright",
            "udemy_slides_tr": [
                "Unit testlerin göremediği entegrasyon kör noktaları.",
                "Playwright mimarisi: Çoklu tarayıcı (Chromium, WebKit, Firefox).",
                "Kırılmaz seçiciler: ARIA Rolleri ve data-testid kullanımı.",
                "Canlı Demo: Playwright UI Mode ve Trace Viewer ile hata ayıklama."
            ],
            "udemy_slides_en": [
                "Integration blind spots invisible to unit assertions.",
                "The Playwright architecture: Cross-browser engine execution.",
                "Authoring resilient locators: ARIA roles vs. data-testid attributes.",
                "Live demo: Debugging flaky runs using Playwright UI Mode and Trace Viewer."
            ],
            "udemy_demo_tr": "Terminalde `npx playwright test --ui` komutunu çalıştırın. Playwright UI penceresinde testin tarayıcıyı nasıl açıp formu doldurduğunu, zaman çizelgesinde (timeline) her adımın ekran görüntüsünü nasıl kaydettiğini canlı gösterin.",
            "udemy_demo_en": "Launch Playwright in UI mode (`npx playwright test --ui`). Execute a test step-by-step, showing the real-time DOM inspector, network request waterfall, and time-travel trace viewer.",
            "action_task_tr": "Projenize Playwright ekleyin (`npm init playwright@latest`) ve ana sayfanızın açılıp başlığının doğru göründüğünü doğrulayan ilk E2E testinizi çalıştırın.",
            "action_task_en": "Initialize Playwright in a project (`npm init playwright@latest`) and run a smoke test asserting your home route loads with correct title headers.",
            "quiz_tr": [
                {
                    "question": "E2E testlerinde `page.locator('button.btn-blue-submit')` yerine `page.getByRole('button', { name: 'Giriş Yap' })` tercih edilmesinin sebebi nedir?",
                    "options": [
                        "A) Daha az harf içermesi",
                        "B) CSS sınıfları değişse bile kullanıcının gördüğü metin ve erişilebilirlik (ARIA) rolü değişmediği sürece testin kırılmadan çalışmaya devam etmesi",
                        "C) Sadece Safari'de çalışması",
                        "D) Bilgisayarın sesini açması"
                    ],
                    "answer": "B",
                    "explanation": "Kullanıcı odaklı (User-Facing) seçiciler, frontend tasarım revizyonlarından etkilenmez ve testleri son derece sağlam (resilient) kılar."
                },
                {
                    "question": "Playwright'ın 'Trace Viewer' aracının yazılımcılara sağladığı en büyük süper güç nedir?",
                    "options": [
                        "A) Bedava kahve ısmarlaması",
                        "B) Testin koştuğu her milisaniyenin ekran görüntüsünü, konsol loglarını ve ağ (network) isteklerini zaman makinesi gibi geriye sararak inceleme imkanı vermesi",
                        "C) Kodları otomatik silmesi",
                        "D) Sadece Windows'ta çalışması"
                    ],
                    "answer": "B",
                    "explanation": "Trace Viewer, özellikle CI ortamında çöken E2E testlerinin tam olarak hangi saniyede ve hangi ağ hatasıyla patladığını video gibi incelemeyi sağlar."
                }
            ],
            "quiz_en": [
                {
                    "question": "Why are semantic locators like `page.getByRole('button', { name: 'Submit' })` superior to raw CSS classes?",
                    "options": [
                        "A) They reduce byte length",
                        "B) They mirror real user interactions and remain resilient against styling or markup refactors",
                        "C) Compatibility restricted to Safari",
                        "D) They unmute machine audio"
                    ],
                    "answer": "B",
                    "explanation": "User-facing locators emulate how screen readers and humans navigate, decoupling test stability from CSS class renaming."
                },
                {
                    "question": "What primary forensic capability is provided by Playwright's Trace Viewer?",
                    "options": [
                        "A) Generating automated coffee orders",
                        "B) Providing a time-travel debugging artifact capturing DOM snapshots, console telemetry, and network cascades for every action",
                        "C) Deleting repository files",
                        "D) Enforcing Windows exclusivity"
                    ],
                    "answer": "B",
                    "explanation": "The Trace Viewer gives developers a visual timeline of headless test execution, diagnosing test flakes in CI environments."
                }
            ]
        },

        # Chapter 34
        {
            "id": 34,
            "section_id": 6,
            "slug_tr": "ch34_ai_destekli_tdd_dongusu",
            "slug_en": "ch34_ai_powered_tdd_loop_red_green_refactor",
            "title_tr": "Test Driven Development (TDD) + AI Döngüsü: Red-Green-Refactor",
            "title_en": "The AI-Powered TDD Loop: Red-Green-Refactor Supercharged",
            "subtitle_tr": "Yapay Zekanın Halüsinasyon Görmesini Engelleyen Nihai Geliştirme Ritmi",
            "subtitle_en": "Anchoring AI Code Generation Inside Deterministic Test Gauntlets",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Yapay zeka çağında TDD (Test-Driven Development) öldü mü, yoksa tam aksine AI'ı kontrol altında tutmanın tek bilimsel yolu haline mi geldi?",
            "podcast_hook_en": "Has Test-Driven Development (TDD) become obsolete in the LLM era, or is it now the single most critical engineering discipline to tame AI hallucinations?",
            "takeaways_tr": [
                "TDD öldü söylemi yanlıştır; AI ile kod yazarken önce testi yazdırmak, AI'ın sınırlarını çizen en katı şartnamedir.",
                "Red-Green-Refactor Döngüsü: 1. Başarısız test yaz (Kırmızı), 2. AI'a testi geçecek minimum kodu yazdır (Yeşil), 3. Kodu temizle (Refactor).",
                "Bu döngüde yapay zeka sadece bir uygulayıcıdır; mimari kısıtları ve doğrulama kriterlerini belirleyen mühendistir."
            ],
            "takeaways_en": [
                "The rumor that TDD is dead in the AI era is entirely false; writing assertions first creates an ironclad specification for LLMs.",
                "The Modern TDD Loop: 1. Draft a failing assertion (Red), 2. Have AI generate the minimal passing code (Green), 3. Refactor clean architecture.",
                "Under this discipline, the AI operates as an eager implementer while the engineer remains the authoritative verification anchor."
            ],
            "story_tr": """Bir okçuluk yarışmasını hayal edin.

Geleneksel kötü yöntem: Oku rastgele ormana doğru fırlatırsınız. Okun düştüğü ağacın yanına gidip etrafına kırmızı bir hedef tahtası çizersiniz! *"Bakın tam hedeften vurdum!"* dersiniz. Komik, değil mi? Test yazmadan AI'a kod yazdırmak tam olarak budur.

TDD (Test-Driven Development) ise gerçek okçuluktur:
1. Önce 100 metre ileriye hedef tahtasını dikersiniz: **RED (Kırmızı)**. Henüz ok atılmadı, hedef boş.
2. Ardından oku tam merkeze fırlatırsınız: **GREEN (Yeşil)**. Test başarıyla geçti!
3. Duruşunuzu ve fiyonkları düzeltirsiniz: **REFACTOR (İyileştirme)**.

Yapay zekaya önce hedef tahtasını (testi) göstermezseniz, okun nereye gideceğini asla tahmin edemezsiniz.""",
            "story_en": """Picture an archery tournament.

The unscientific approach: You loose an arrow blindly into the deep forest. You locate the random pine trunk it struck, pull out spray paint, and draw a red bullseye around the arrow: *"Look, a dead-center bullseye!"* Ridiculous, isn't it? Writing code first and testing afterwards is that fake bullseye.

Test-Driven Development (TDD) represents genuine archery:
1. Stake the target board 100 meters away: **RED**. Target stands waiting, untouched.
2. Loose the arrow with precision to strike the center: **GREEN**. Tests verify success.
3. Optimize posture and quiver mechanics: **REFACTOR**. Code is simplified without moving the target.

If you don't present the LLM with the target board (unit assertions) first, you forfeit control over where its generated syntax lands.""",
            "mental_tr": """AI Destekli TDD Döngüsü:

```
    ┌──────────────────────────────────────────────┐
    │ 1. ADIM (RED - Kırmızı):                      │
    │ Testi Yazdır veya Sen Yaz:                    │
    │ "Bu senaryoları kapsayan test dosyasını ver" │
    │ Test koşulur: ❌ BAŞARISIZ OLUR (Beklenen)    │
    └──────────────────────┬───────────────────────┘
                           │
                           ▼
    ┌──────────────────────────────────────────────┐
    │ 2. ADIM (GREEN - Yeşil):                     │
    │ AI'a Yalnızca Bu Testi Geçecek Kodu İste:    │
    │ "Bu testleri geçecek minimum implementasyon" │
    │ Test koşulur: ✅ BAŞARILI OLUR               │
    └──────────────────────┬───────────────────────┘
                           │
                           ▼
    ┌──────────────────────────────────────────────┐
    │ 3. ADIM (REFACTOR - Temizle):                │
    │ Mimariyi İyileştir, Fazlalıkları At:         │
    │ "Testleri bozmadan kodu temizle ve sadeleştir│
    │ Test koşulur: ✅ HÂLÂ YEŞİL KALIR             │
    └──────────────────────────────────────────────┘
```""",
            "mental_en": """The AI-Accelerated TDD Cycle:

```
    ┌──────────────────────────────────────────────┐
    │ STEP 1 (RED):                                │
    │ Author Failing Specification:                │
    │ Define input boundaries and expectations.    │
    │ Test runner execution: ❌ FAILS (As expected) │
    └──────────────────────┬───────────────────────┘
                           │
                           ▼
    ┌──────────────────────────────────────────────┐
    │ STEP 2 (GREEN):                              │
    │ AI Generates Minimal Implementation:         │
    │ "Generate code strictly satisfying tests."   │
    │ Test runner execution: ✅ PASSES             │
    └──────────────────────┬───────────────────────┘
                           │
                           ▼
    ┌──────────────────────────────────────────────┐
    │ STEP 3 (REFACTOR):                           │
    │ Cleanse Architecture, Eliminate Redundancy:  │
    │ Refactor for readability while green.        │
    │ Test runner execution: ✅ REMAINS GREEN      │
    └──────────────────────────────────────────────┘
```""",
            "prompt_tr": """# ROL: TDD ve Temiz Kod Koçu
Bir 'İndirim Kuponu Doğrulama ve Uygulama' motoru geliştireceğiz.

## ADIM 1: RED (ÖNCE TEST)
Lütfen bana fonksiyonun kendisini YAZMA.
Sadece aşağıdaki gereksinimleri test eden Jest test dosyasını oluştur:
1. Kupon tarihi geçmişse `ExpiredCouponError` fırlatmalı.
2. Sepet tutarı minimum sepet limitinin altındaysa `MinimumSpendNotMetError` fırlatmalı.
3. Yüzdelik indirimlerde (%20 indirim) tutarı doğru düşmeli.
4. Maksimum indirim tavanı varsa (örn: max 100 TL) indirimi o tutarla sınırlandırmalı.""",
            "prompt_en": """# ROLE: TDD & Extreme Programming Coach
We are building a Promotional Coupon Engine.

## STEP 1: RED (TESTS FIRST)
Do NOT output implementation code yet.
Author a Jest test suite asserting these exact business invariants:
1. Expired coupons throw `ExpiredCouponError`.
2. Baskets below the qualifying threshold throw `MinimumSpendNotMetError`.
3. Percentage discounts apply correctly.
4. Discounts exceeding the promotional ceiling are strictly clamped to the maximum cap.""",
            "code_lang": "typescript",
            "code_naive": """// Geleneksel Hatalı Akış: Önce karmaşık kod yazıp sonra test yazmaya üşenmek
// Sonuç: Testi olmayan, sınır durumları belirsiz, refactor edilemeyen kod!
export function applyCouponBlind(cart: any, coupon: any) {
  return cart.total - coupon.amount;
}""",
            "code_robust": """// TDD Yeşil Adımı: Testleri geçen temiz ve sağlam implementasyon
export interface Cart {
  total: number;
}

export interface Coupon {
  code: string;
  discountPercent: number;
  maxDiscountAmount: number;
  minSpend: number;
  expiresAt: Date;
}

export function applyPromotionalCoupon(cart: Cart, coupon: Coupon): number {
  if (new Date() > coupon.expiresAt) {
    throw new Error("ExpiredCouponError: Kuponun süresi dolmuş.");
  }

  if (cart.total < coupon.minSpend) {
    throw new Error("MinimumSpendNotMetError: Minimum sepet tutarı karşılanmadı.");
  }

  const calculatedDiscount = (cart.total * coupon.discountPercent) / 100;
  const actualDiscount = Math.min(calculatedDiscount, coupon.maxDiscountAmount);

  return Math.round((cart.total - actualDiscount) * 100) / 100;
}""",
            "code_notes_tr": "TDD yaklaşımında önce test yazıldığı için kupon tavan sınırı (`Math.min`), tarih kontrolü ve minimum tutar kuralı koda daha baştan defansif olarak entegre edilmiş olur.",
            "code_notes_en": "Because test specifications preceded code generation, maximum discount clamping (`Math.min`), date validation, and threshold constraints were embedded defensibly from minute zero.",
            "pitfalls_tr": [
                {"trap": "AI'a hem testi hem kodu aynı anda yazdırıp testin çalıştığını doğrulamamak.", "solution": "Önce testi yazdırın, testin kırmızı yandığını (hata verdiğini) gözlerinizle görün, ardından kodu yazdırın."},
                {"trap": "Refactor aşamasını atlayıp 'nasılsa yeşil yandı' diyerek çirkin kodu öylece bırakmak.", "solution": "Yeşil yandıktan sonra kodu temizleyin; testleriniz yeşil kaldığı sürece korkusuzca düzenleyin."},
                {"trap": "Test senaryolarını çok geniş ve belirsiz tutmak.", "solution": "Her test fonksiyonunda sadece tek bir iş kuralını (`it should...`) test edin."}
            ],
            "pitfalls_en": [
                {"trap": "Prompting AI to generate both tests and implementation in a single turn without observing a failure.", "solution": "Always inspect the test failing in RED before requesting the implementation."},
                {"trap": "Skipping the refactoring stage once tests turn green.", "solution": "Passing tests grant permission to clean architecture fearlessly without risk of breaking behavior."},
                {"trap": "Cramming 10 unrelated assertions into a single test block.", "solution": "Enforce single assertion focus per test block (`it('should clamp discount to max ceiling')`)."}
            ],
            "udemy_title_tr": "Ders 34: AI ile TDD - Red, Green, Refactor Disiplini",
            "udemy_title_en": "Lecture 34: The AI-Powered TDD Loop - Red, Green, Refactor",
            "udemy_slides_tr": [
                "Neden TDD yapay zekayı evcilleştirmenin tek kesin yoludur?",
                "3 Adımlı Ritim: Red (Kırmızı), Green (Yeşil), Refactor (İyileştirme).",
                "AI'a önce test yazdırmanın yarattığı kusursuz şartname etkisi.",
                "Canlı Demo: 5 dakikada TDD ile kupon motoru inşa etmek."
            ],
            "udemy_slides_en": [
                "Why TDD is the ultimate mechanism to discipline AI code generation.",
                "The 3-phase heartbeat: Red, Green, Refactor.",
                "Transforming test assertions into unambiguous system prompts.",
                "Live demo: Crafting a verified discount engine via TDD in 5 minutes."
            ],
            "udemy_demo_tr": "Boş bir dosya açın. AI'a kupon testlerini yazdırın. Terminalde `npm test` çalıştırıp testin kırmızı yandığını (RED) gösterin. Ardından kodu üretip testin yeşile döndüğünü (GREEN) ve refactor sonrası yine yeşil kaldığını gösterin.",
            "udemy_demo_en": "Open an empty directory. Prompt an AI for coupon test specifications. Execute the runner to verify RED. Request minimal code to achieve GREEN. Refactor and verify it stays GREEN.",
            "action_task_tr": "Geliştireceğiniz bir sonraki özellik için önce testi yazın veya AI'a sadece test dosyasını yazdırın. Testin başarısız olduğunu gördükten sonra kodu üretin.",
            "action_task_en": "Practice strict TDD on your next task: draft the test first, observe it fail in your terminal, and only then generate the implementation.",
            "quiz_tr": [
                {
                    "question": "TDD (Test-Driven Development) döngüsünün ilk adımı (RED) neden testin başarısız olduğunu görmeyi zorunlu kılar?",
                    "options": [
                        "A) Geliştiricinin moralini bozmak için",
                        "B) Testin gerçekten çalıştığını, sahte (her zaman geçen) bir test olmadığını ve henüz yazılmamış özelliği doğru denetlediğini kanıtlamak için",
                        "C) Bilgisayarı test etmek için",
                        "D) Sadece C++ dilinde zorunlu olduğu için"
                    ],
                    "answer": "B",
                    "explanation": "Eğer test henüz kod yazılmadan önce yeşil yanıyorsa, o test hatalıdır veya hiçbir şey test etmiyordur. Kırmızı adımını görmek zorunludur."
                },
                {
                    "question": "TDD'nin üçüncü aşaması olan 'Refactor' adımında ne yapılır?",
                    "options": [
                        "A) Proje silinir",
                        "B) Testlerin yeşil kalması güvencesi altında kod temizlenir, optimize edilir ve mimari olarak iyileştirilir",
                        "C) Yeni özellikler eklenir",
                        "D) Testler silinir"
                    ],
                    "answer": "B",
                    "explanation": "Refactor, çalışan sistemin dış davranışını değiştirmeden kod kalitesini, okunabilirliğini ve mimarisini iyileştirme aşamasıdır."
                }
            ],
            "quiz_en": [
                {
                    "question": "Why is observing a failing assertion (RED) the non-negotiable first step in TDD?",
                    "options": [
                        "A) To instill humility in developers",
                        "B) To verify the test harness is genuinely active and that the test does not produce false-positive passes without code",
                        "C) Hardware diagnostic testing",
                        "D) Compliance unique to C++ compilers"
                    ],
                    "answer": "B",
                    "explanation": "If a test passes before implementation exists, the test is defective or tautological. Confirming RED validates test integrity."
                },
                {
                    "question": "What is the primary objective of the 'Refactor' stage in the TDD loop?",
                    "options": [
                        "A) Deleting repository history",
                        "B) Restructuring and optimizing syntax while existing tests guarantee zero behavioral regression",
                        "C) Sneaking in brand-new consumer features",
                        "D) Purging unit test assertions"
                    ],
                    "answer": "B",
                    "explanation": "Refactoring improves maintainability and internal design without altering external behaviors, verified by green test suites."
                }
            ]
        },

        # Chapter 35
        {
            "id": 35,
            "section_id": 6,
            "slug_tr": "ch35_edge_case_avciligi_ve_kaos_testi",
            "slug_en": "ch35_hunting_edge_cases_and_chaos_testing",
            "title_tr": "Edge Case (Uç Durum) Avcılığı: AI ile Olmayacak Senaryoları Bulmak",
            "title_en": "Edge Case Hunting & Chaos Testing: Finding Unthinkable Scenarios with AI",
            "subtitle_tr": "29 Şubat, Artık Saniyeler, Boş Stringler ve Sonsuz Sayılarla Sistemi Kırmak",
            "subtitle_en": "Breaking Systems with Leap Years, Negative Balances, and Malicious Unicode",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Dünyanın en iyi yazılımcılarının yazdığı kodlar bile neden 29 Şubat'ta veya sıfıra bölme (division by zero) durumlarında çöker ve AI bu kör noktaları nasıl yakalar?",
            "podcast_hook_en": "Why do elite software teams still get blindsided by leap year calculations and integer overflows, and how can AI act as an adversarial chaos engineer?",
            "takeaways_tr": [
                "Kullanıcılar asla sizin düşündüğünüz gibi davranmaz; beklenmedik girdiler sistemin gerçek stres testidir.",
                "Edge Case (Uç Durum): Boş stringler, maksimum integer limitleri, farklı zaman dilimleri (Timezones) ve özel karakterlerdir.",
                "AI modellerine 'Bu sistemi patlatacak 10 anormal sınır durum üret' demek, en ucuz ve etkili güvenlik kalkanıdır."
            ],
            "takeaways_en": [
                "Real users will never follow your idealized happy path; adversarial and malformed inputs are reality.",
                "Edge cases encompass: empty strings, boundary numbers (`Number.MAX_SAFE_INTEGER`), timezone shifts, and Unicode payloads.",
                "Prompting an AI model to generate 10 adversarial edge cases is the highest-ROI defensive programming habit."
            ],
            "story_tr": """Bir bankomat (ATM) cihazı düşünün.

Mühendisler ATM'yi test ediyor:
- Kartı sok, şifreyi gir, 100 TL çek -> Başarılı!
- 500 TL çek -> Başarılı!

Peki sarhoş bir müşteri gelip ATM'ye:
- Eksi 100 TL (-100 TL) çekmek isterse ne olur? (Yazılım eksi parayı çıkaramayacağı için kullanıcının hesabına para ekleyebilir!)
- Kart yuvasına bozuk para veya kağıt mendil tıkarsa?
- Aynı anda hem interneti kesip hem para çekme tuşuna basarsa?

İşte buna **Edge Case (Uç Durum)** denir. Acemi geliştirici sadece güneşli havaları düşünür. Kıdemli mühendis ise fırtınada çatının uçup uçmayacağını test eder.""",
            "story_en": """Consider an automated banking ATM.

The developers verify standard operations:
- Insert card, enter PIN, withdraw $100 -> Success!
- Withdraw $500 -> Success!

Now observe an adversarial edge-case scenario:
- What happens if someone requests a withdrawal of -$100? If unvalidated, subtracting a negative number increments their account balance!
- What if someone injects a 4-byte zero-width Unicode string into the PIN keypad?
- What if power drops out the exact millisecond cash leaves the dispenser?

These are **Edge Cases**. Novice developers test only sunny afternoons. Master engineers subject structures to Category 5 hurricanes.""",
            "mental_tr": """En Meşhur 5 Edge Case Kategorisi:

```
1. SAYISAL SINIRLAR (Numeric Limits):
   - Sıfır (0), Negatif Sayılar (-1), Ondalık Yuvarlama (0.1 + 0.2), MAX_SAFE_INTEGER.

2. METİN VE KARAKTERLER (Strings & Unicode):
   - Boş string (""), Sadece boşluk ("   "), Null/Undefined, Emojiler (👨‍👩‍👧‍👦), SQL/HTML etiketleri.

3. ZAMAN VE TARİH (Temporal & Clocks):
   - 29 Şubat (Artık yıl), Gün ışığından yararlanma (Saatlerin 1 saat geri/ileri alınması), UTC vs Yerel Saat.

4. KOLEKSİYONLAR (Collections & Arrays):
   - Boş liste ([]), Tek elemanlı liste ([1]), 1.000.000 elemanlı liste.

5. EŞZAMANLILIK (Concurrency & Race Conditions):
   - Aynı butona 10 milisaniye içinde 2 kez çift tıklama!
```""",
            "mental_en": """The 5 Primary Edge-Case Taxonomies:

```
1. NUMERIC BOUNDARIES:
   - Zero (0), negative values, floating precision (0.1 + 0.2), Integer overflow limits.

2. STRING & UNICODE PAYLOADS:
   - Empty strings (""), whitespace only ("   "), null/undefined, multi-byte emojis (👨‍👩‍👧‍👦), raw script tags.

3. TEMPORAL ANOMALIES:
   - Leap years (Feb 29), Daylight Saving Time hour shifts, leap seconds, divergent UTC offsets.

4. COLLECTION VOLUMES:
   - Empty lists (`[]`), singletons (`[x]`), high-cardinality collections (1,000,000 items).

5. CONCURRENCY & RACE CONDITIONS:
   - Idempotency violations: double-clicking 'Checkout' within 10 milliseconds.
```""",
            "prompt_tr": """# ROL: Kaos Mühendisi ve Uç Durum (Edge Case) Avcısı
Aşağıdaki kullanıcı yaşını ve doğum gününü doğrulayan fonksiyonu incele.

## KOD:
```typescript
function isEligibleToVote(birthDateStr: string): boolean {
  const birthYear = new Date(birthDateStr).getFullYear();
  const currentYear = new Date().getFullYear();
  return (currentYear - birthYear) >= 18;
}
```

## GÖREV:
1. Bu koddaki en az 4 ölümcül sınır durumu (edge case) tespit et (Örn: Ay ve gün hesabı, 29 Şubat, geçersiz tarih formatı, gelecekteki tarihler).
2. Bu sınır durumları patlatacak Jest test senaryolarını yaz.
3. Fonksiyonu tüm bu uç durumlara karşı kurşun geçirmez şekilde refactor et.""",
            "prompt_en": """# ROLE: Chaos & Edge-Case Vulnerability Analyst
Examine this voter eligibility verification method:

## SNIPPET:
```typescript
function isEligibleToVote(birthDateStr: string): boolean {
  const birthYear = new Date(birthDateStr).getFullYear();
  const currentYear = new Date().getFullYear();
  return (currentYear - birthYear) >= 18;
}
```

## TASK:
1. Uncover 4 critical edge cases (month/day boundary off-by-one errors, invalid dates, future birthdates).
2. Author adversarial Jest assertions targeting these exact edge cases.
3. Deliver a hardened, bulletproof refactor handling leap years and temporal boundaries.""",
            "code_lang": "typescript",
            "code_naive": """// Kötü Kod: Sadece yılı çıkarır; ay ve günü hesaba katmaz!
// Örnek: Bugün Ocak 2026 ise ve kullanıcı Aralık 2008 doğumluysa (henüz 17 yaşındayken) 18 kabul eder!
export function isEligibleToVoteNaive(birthDateStr: string): boolean {
  return (new Date().getFullYear() - new Date(birthDateStr).getFullYear()) >= 18;
}""",
            "code_robust": """export function isEligibleToVoteRobust(
  birthDateStr: string,
  now: Date = new Date()
): boolean {
  const birthDate = new Date(birthDateStr);

  // 1. Uç Durum: Geçersiz tarih formatı (NaN)
  if (isNaN(birthDate.getTime())) {
    throw new TypeError("Geçersiz tarih formatı girildi.");
  }

  // 2. Uç Durum: Gelecekte bir doğum tarihi girilemez
  if (birthDate > now) {
    throw new RangeError("Doğum tarihi bugünden ileri bir tarih olamaz.");
  }

  // 3. Kesin Yaş Hesabı (Ay ve Gün Hassasiyeti)
  let age = now.getFullYear() - birthDate.getFullYear();
  const monthDiff = now.getMonth() - birthDate.getMonth();

  if (monthDiff < 0 || (monthDiff === 0 && now.getDate() < birthDate.getDate())) {
    age--; // Doğum günü bu yıl henüz gelmedi!
  }

  // 4. Uç Durum: 130 yaşından büyük mantıksız değerler
  if (age > 130) {
    throw new RangeError("Doğrulanamaz yaş değeri.");
  }

  return age >= 18;
}""",
            "code_notes_tr": "Kıdemli sürüm; geçersiz tarihleri (`NaN`), henüz günü gelmemiş ayları, gelecekteki doğum tarihlerini ve mantıksız sınırları tek tek kontrol ederek çökmeleri engeller.",
            "code_notes_en": "The hardened version validates unparseable date strings (`NaN`), future timestamps, exact month/day boundaries, and upper-bound sanity checks.",
            "pitfalls_tr": [
                {"trap": "Kullanıcının her zaman doğru formatta veri gireceğini varsaymak.", "solution": "Girdileri daima şüpheyle karşılayın; 'Boş gelirse ne olur?', 'Çok büyük gelirse ne olur?' diye sorun."},
                {"trap": "Tarih hesaplamalarında `getFullYear() - getFullYear()` yapıp gün farkını unutmak.", "solution": "Tarih karşılaştırmalarında gün ve saat hassasiyetini veya güvenilir kütüphaneleri (date-fns) kullanın."},
                {"trap": "Sayısal işlemlerde sıfıra bölme (division by zero) kontrolü yapmamak.", "solution": "Her bölme işleminden önce paydanın sıfır olmadığını teyit edin."}
            ],
            "pitfalls_en": [
                {"trap": "Assuming external consumers will always input well-formed data.", "solution": "Treat incoming parameters with suspicion: validate empty payloads, type mismatches, and boundary sizes."},
                {"trap": "Comparing dates via simplistic calendar year subtractions.", "solution": "Account for exact days and months, or rely on established temporal engines like `date-fns`."},
                {"trap": "Neglecting division-by-zero checks in calculation algorithms.", "solution": "Always assert that denominators are non-zero before executing division or modulo arithmetic."}
            ],
            "udemy_title_tr": "Ders 35: Edge Case Avcılığı - AI ile Olmayacak Senaryoları Bulmak",
            "udemy_title_en": "Lecture 35: Edge Case Hunting - Uncovering Impossible Bugs with AI",
            "udemy_slides_tr": [
                "Neden en büyük sistem çöküşleri Edge Case'lerden kaynaklanır?",
                "5 Temel Sınır Durum Kategorisi (Sayılar, Metinler, Tarihler, Listeler, Concurrency).",
                "AI'ı 'Kötü Niyetli Hacker' rolünde sınır testleri için kullanmak.",
                "Canlı Demo: Hatalı yaş hesaplama fonksiyonunu kırmak ve onarmak."
            ],
            "udemy_slides_en": [
                "Why high-profile outages trace back to neglected boundary edge cases.",
                "The 5 core edge case archetypes (Numeric, Text, Temporal, Collections, Concurrency).",
                "Casting AI as an adversarial chaos engineer to expose software cracks.",
                "Live demo: Breaking and repairing an age-calculation function."
            ],
            "udemy_demo_tr": "Basit bir metin kısaltma (truncate) fonksiyonunu AI'a verin. 'Bu fonksiyonu çökertecek 5 sınır durum testi yaz' deyin. AI'ın boş string, 100.000 karakterlik metin ve çoklu bayt emoji testlerini nasıl ürettiğini ve kodun patladığını canlı gösterin.",
            "udemy_demo_en": "Submit a string truncate function to an LLM. Prompt: 'Provide 5 adversarial edge-case assertions designed to crash this function'. Watch it expose crashes on empty strings and multi-byte emojis.",
            "action_task_tr": "Projenizdeki en kritik bir fonksiyonu seçin. AI'a 'Bu fonksiyonu production'da çökertecek 5 çılgın edge case üret' deyin ve çıkan testleri çalıştırın.",
            "action_task_en": "Select a critical core function in your project. Prompt an AI model to generate 5 boundary edge cases, and run them against your code.",
            "quiz_tr": [
                {
                    "question": "JavaScript/TypeScript'te `0.1 + 0.2 === 0.3` ifadesinin sonucu neden `false` döner?",
                    "options": [
                        "A) JavaScript bozuk bir dildir",
                        "B) Sayılar ikili (binary floating-point) tabanda temsil edildiği için 0.3 yerine 0.30000000000000004 hassasiyet kaybı oluşur",
                        "C) Sadece Google Chrome'da öyle olur",
                        "D) Sonuç true döner"
                    ],
                    "answer": "B",
                    "explanation": "IEEE 754 kayan noktalı standartta ikili taban kesirli sayıları tam temsil edemez; bu nedenle parasal işlemlerde kuruş yuvarlama kontrolleri şarttır."
                },
                {
                    "question": "Bir fonksiyonda 'Sıfıra Bölme' (Division by Zero) kontrolü yapılmadığında çoğu dilde ne gerçekleşir?",
                    "options": [
                        "A) Kod daha hızlı çalışır",
                        "B) `Infinity` döner veya `ZeroDivisionError` fırlatılarak program anında çöker",
                        "C) Bilgisayarın ekranı kararır",
                        "D) Sayı otomatik olarak 1 olur"
                    ],
                    "answer": "B",
                    "explanation": "Sıfıra bölme matematiksel olarak tanımsızdır; diller ya çalışma zamanı hatası fırlatır ya da beklenmedik `Infinity` / `NaN` üreterek sistemi bozar."
                }
            ],
            "quiz_en": [
                {
                    "question": "Why does evaluating `0.1 + 0.2 === 0.3` yield `false` in standard programming runtimes?",
                    "options": [
                        "A) JavaScript contains a deliberate compiler bug",
                        "B) Binary floating-point representation (IEEE 754) introduces fractional precision discrepancies (`0.30000000000000004`)",
                        "C) It only manifests on Chrome browsers",
                        "D) It actually evaluates to true"
                    ],
                    "answer": "B",
                    "explanation": "Binary arithmetic cannot precisely store fractional base-10 values like 0.1, resulting in rounding discrepancies."
                },
                {
                    "question": "What operational failure occurs when division by zero is unguarded in software systems?",
                    "options": [
                        "A) Processing speeds double",
                        "B) The runtime emits a fatal `ZeroDivisionError` or injects corrupting `Infinity` / `NaN` payloads into downstream storage",
                        "C) Display monitors disconnect",
                        "D) The dividend automatically normalizes to 1"
                    ],
                    "answer": "B",
                    "explanation": "Division by zero is mathematically undefined, triggering runtime panics or corrupting data pipelines with `NaN` / `Infinity`."
                }
            ]
        },

        # Chapter 36
        {
            "id": 36,
            "section_id": 6,
            "slug_tr": "ch36_statik_analiz_linter_ve_teknik_borc",
            "slug_en": "ch36_static_analysis_linters_technical_debt",
            "title_tr": "Kod Kalite Metrikleri: SonarQube, Linter'lar ve Statik Analiz",
            "title_en": "Static Analysis, Linters & Managing Technical Debt with AI",
            "subtitle_tr": "Teknik Borç Faizini Ödemeden Sistemi Sürdürülebilir Kılmak",
            "subtitle_en": "Automating Code Quality Gates Before Technical Debt Compound Interest Kills Velocity",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Teknik borç (Technical Debt) nedir ve bir startup'ın ilk 6 ayında hızlı olmak için aldığı borçlar 2. yılda şirketi nasıl iflasa sürükler?",
            "podcast_hook_en": "What is technical debt, and how does the reckless code hastily shipped during a startup's first 6 months bring engineering velocity to a dead halt later?",
            "takeaways_tr": [
                "Teknik borç, hızlı teslimat yapmak için kaliteden ödün vermektir; zamanında ödenmezse faizi tüm ekibi felç eder.",
                "Statik analiz (ESLint, Biome, SonarQube), kodu çalıştırmadan potansiyel güvenlik açıklarını ve karmaşıklığı tespit eder.",
                "Siklomotik Karmaşıklık (Cyclomatic Complexity), bir fonksiyondaki karar yollarının sayısıdır; 10'un üzerinde olması tehlike çanıdır."
            ],
            "takeaways_en": [
                "Technical debt is the compounding tax paid when teams choose short-term shortcuts over sustainable architecture.",
                "Static analysis tools (ESLint, Biome, SonarQube) audit source syntax for security vulnerabilities and cognitive bloat without executing code.",
                "Cyclomatic Complexity measures independent linear execution paths; scores exceeding 10 signal unmaintainable code."
            ],
            "story_tr": """Kredi kartıyla alışveriş yaptığınızı düşünün. 

Kredi kartı harika bir kolaylıktır: Paranız yokken bile istediğiniz ayakkabıyı alırsınız (Hızlı kod yazıp teslim etmek). Ancak her ay asgari tutarı bile ödemezseniz ne olur? Faiz biner, faizin faizi biner ve sonunda haciz gelir!

Yazılımda **Teknik Borç (Technical Debt)** işte o kredi kartıdır:
- "Şimdilik test yazmayalım, sonra bakarız."
- "Buradaki if-else'i geçici yazdım, haftaya düzeltirim."
- "Kütüphane deprecated oldu ama şimdilik çalışıyor."

1 yıl sonra bir butonu değiştirmek 3 hafta sürer hale gelir çünkü kimse o borç batağına dokunamaz!

Statik analiz ve linter araçları, her gün borcunuzu ödemenizi hatırlatan akıllı finans danışmanınızdır.""",
            "story_en": """Imagine funding daily lifestyle expenses on a high-interest credit card.

A credit card provides useful leverage: you obtain immediate purchasing power without having cash on hand (shipping shortcuts to hit market deadlines). But if you fail to service the balance, compound interest multiplies until financial ruin strikes.

**Technical Debt** is that credit card:
- "We'll skip writing unit assertions for now; we'll backfill them later."
- "This 400-line if-else block is temporary; I'll refactor it next sprint."
- "The dependency is deprecated and vulnerable, but it compiles."

Twelve months later, modifying a button takes 3 weeks because nobody understands the fragile spaghetti codebase.

Static analyzers and linters serve as the automated financial auditors keeping your technical debt under control.""",
            "mental_tr": """Teknik Borç ve Kod Kalite Piramidi:

```
[KOD YAZILIRKEN]
       │
       ▼
[1. Linter & Formatlayıcı (Biome / ESLint / Prettier)]
   └── Söz dizimi hatalarını, kullanılmayan değişkenleri anında yakalar.
       │
       ▼
[2. Tip Kontrolü (TypeScript / MyPy)]
   └── Tip güvenliğini ve şema uyumunu garanti eder.
       │
       ▼
[3. Karmaşıklık ve Koku Analizi (SonarQube / Code Climate)]
   └── Siklomotik karmaşıklığı, mükerrer kodları (duplicate) ölçer.
       │
       ▼
[TEMİZ & SÜRDÜRÜLEBİLİR ÜRÜN]
```""",
            "mental_en": """The Static Code Quality Funnel:

```
[Source Code Authored]
           │
           ▼
[1. Linter & Formatter (Biome / ESLint / Prettier)]
   └── Traps formatting defects, dead imports, and unused variables.
           │
           ▼
[2. Type Verification (TypeScript Strict / MyPy)]
   └── Guarantees type invariance and structural integrity.
           │
           ▼
[3. Cognitive Complexity & Vulnerability Audit (SonarQube)]
   └── Quantifies cyclomatic complexity, code duplication, and CVEs.
           │
           ▼
[SUSTAINABLE, MAINTAINABLE CODEBASE]
```""",
            "prompt_tr": """# ROL: Kod Kalitesi ve Statik Analiz Uzmanı
Aşağıdaki yüksek karmaşıklığa sahip (Cyclomatic Complexity > 12) JavaScript fonksiyonunu incele.

## KOD:
```typescript
function calculateUserTariff(user: any) {
  let rate = 10;
  if (user.isStudent) {
    if (user.age < 25) {
      rate -= 3;
    } else {
      rate -= 1;
    }
  } else if (user.isSenior) {
    if (user.hasCard) {
      rate -= 4;
    } else {
      rate -= 2;
    }
  } else {
    if (user.isVip) {
      rate -= 5;
    }
  }
  return rate;
}
```

## GÖREV:
1. Bu koddaki Siklomotik Karmaşıklığı (Cyclomatic Complexity) analiz et.
2. 'Lookup Table' veya 'Kural Motoru (Rule Engine)' deseni kullanarak karmaşıklığı 2'nin altına düşüren temiz refactor'ü yap.
3. ESLint için karmaşıklık sınırını zorunlu kılan kural önerisini sun.""",
            "prompt_en": """# ROLE: Code Quality & Static Analysis Lead
Analyze this convoluted function exhibiting excessive Cyclomatic Complexity (> 12):

## SNIPPET:
```typescript
function calculateUserTariff(user: any) {
  let rate = 10;
  if (user.isStudent) {
    if (user.age < 25) {
      rate -= 3;
    } else {
      rate -= 1;
    }
  } else if (user.isSenior) {
    if (user.hasCard) {
      rate -= 4;
    } else {
      rate -= 2;
    }
  } else {
    if (user.isVip) {
      rate -= 5;
    }
  }
  return rate;
}
```

## TASK:
1. Calculate the Cyclomatic Complexity score.
2. Refactor using a declarative Rule Engine or Lookup Table to reduce complexity below 3.
3. Provide the ESLint configuration rule to enforce cyclomatic limits automatically.""",
            "code_lang": "typescript",
            "code_naive": """// Yüksek Siklomotik Karmaşıklık: 6 adet iç içe if-else ve 'any' kullanımı
export function calculateTariffNaive(user: any): number {
  if (user.isStudent && user.age < 25) return 7;
  if (user.isStudent && user.age >= 25) return 9;
  if (user.isSenior && user.hasCard) return 6;
  if (user.isSenior && !user.hasCard) return 8;
  if (user.isVip) return 5;
  return 10;
}""",
            "code_robust": """// Deklaratif ve Sıfır Karmaşıklık: Kural Listesi Deseni
export interface TariffUser {
  isStudent?: boolean;
  age?: number;
  isSenior?: boolean;
  hasCard?: boolean;
  isVip?: boolean;
}

type TariffRule = {
  predicate: (user: TariffUser) => boolean;
  discount: number;
};

const TARIFF_RULES: readonly TariffRule[] = [
  { predicate: (u) => Boolean(u.isVip), discount: 5 },
  { predicate: (u) => Boolean(u.isSenior && u.hasCard), discount: 4 },
  { predicate: (u) => Boolean(u.isStudent && (u.age ?? 0) < 25), discount: 3 },
  { predicate: (u) => Boolean(u.isSenior && !u.hasCard), discount: 2 },
  { predicate: (u) => Boolean(u.isStudent && (u.age ?? 0) >= 25), discount: 1 },
];

const BASE_RATE = 10;

export function calculateUserTariff(user: TariffUser): number {
  const matchedRule = TARIFF_RULES.find((rule) => rule.predicate(user));
  return BASE_RATE - (matchedRule?.discount ?? 0);
}""",
            "code_notes_tr": "İç içe if-else blokları tamamen ortadan kaldırılarak deklaratif bir kural listesine (`TARIFF_RULES`) dönüştürülmüştür. Fonksiyonun karmaşıklığı 1'e düşürülmüş ve yeni bir tarife kuralı eklemek tek bir satır eklemeye indirgenmiştir.",
            "code_notes_en": "Nested branching is eradicated by delegating evaluations to a declarative rules table (`TARIFF_RULES`). Cyclomatic complexity drops to 1, and introducing new discounts requires only appending a rule definition.",
            "pitfalls_tr": [
                {"trap": "Linter uyarılarını (warnings) önemsemeyip yüzlerce uyarının birikmesine izin vermek.", "solution": "CI pipeline'ında uyarıları hata kabul eden kuralı (`--max-warnings 0`) devreye alın."},
                {"trap": "Teknik borcu tamamen görmezden gelip her sprintte sadece yeni özellik yazmaya çalışmak.", "solution": "Her sprint kapasitenizin en az %15-20'sini teknik borç temizliğine ve refactor'e ayırın."},
                {"trap": "Linter kurallarını çok katı yapıp ekibi kod yazamaz hale getirmek.", "solution": "Pragmatik olun; kuralları takım kararıyla belirleyin."}
            ],
            "pitfalls_en": [
                {"trap": "Tolerating hundreds of compiler and linter warnings until they become background noise.", "solution": "Enforce strict CI quality gates: fail builds on warnings (`eslint --max-warnings 0`)."},
                {"trap": "Refusing to allocate sprint capacity to debt retirement.", "solution": "Dedicate 15-20% of every sprint buffer to refactoring technical debt."},
                {"trap": "Imposing draconian stylistic linter rules that paralyze delivery.", "solution": "Automate formatting via Biome or Prettier; focus static analysis on logic errors and security leaks."}
            ],
            "udemy_title_tr": "Ders 36: Kod Kalite Metrikleri - Teknik Borcu Kontrol Altına Almak",
            "udemy_title_en": "Lecture 36: Code Quality Metrics - Taming Technical Debt with Static Analysis",
            "udemy_slides_tr": [
                "Teknik Borç (Technical Debt) nedir ve bileşik faizi nasıl işler?",
                "Siklomotik Karmaşıklık (Cyclomatic Complexity) nasıl ölçülür?",
                "Biome ve ESLint ile otomatik kod hijyeni kurmak.",
                "Bölüm 6 Özeti: Test Odaklı Geliştirme ve Kalite Güvencesi."
            ],
            "udemy_slides_en": [
                "What is Technical Debt and how does its compound interest paralyze teams?",
                "Quantifying Cyclomatic and Cognitive Complexity.",
                "Automating code hygiene via Biome and ESLint.",
                "Module 6 Recap: Test-Driven Development and Bulletproof Quality Assurance."
            ],
            "udemy_demo_tr": "Karmaşık iç içe if-else içeren bir dosyada ESLint karmaşıklık eklentisini çalıştırıp uyarının yandığını gösterin. Kural tablosuna refactor ettikten sonra uyarının söndüğünü canlı gösterin.",
            "udemy_demo_en": "Run ESLint with complexity rules enabled over a heavily nested function. Observe the warning flag. Refactor the implementation into a declarative lookup table and watch the linter clear.",
            "action_task_tr": "Projenizde `eslint` veya `biome` çalıştırın. En karmaşık veya en çok uyarı veren dosyayı tespit edip en az 2 uyarısını temizleyin.",
            "action_task_en": "Execute your project's linter. Identify the file producing the highest warning count and refactor it until zero warnings remain.",
            "quiz_tr": [
                {
                    "question": "Yazılım mühendisliğinde 'Siklomotik Karmaşıklık' (Cyclomatic Complexity) neyi ölçer?",
                    "options": [
                        "A) Kodun kaç megabayt yer kapladığını",
                        "B) Bir fonksiyondaki bağımsız kod yürütme yollarının (if, else, while vb. dallanmaların) sayısını",
                        "C) Bilgisayarın ekran parlaklığını",
                        "D) GitHub'daki yıldız sayısını"
                    ],
                    "answer": "B",
                    "explanation": "Siklomotik karmaşıklık, koddaki mantıksal dallanma sayısını ölçer. Sayı ne kadar yüksekse kodu test etmek ve anlamak o kadar zorlaşır."
                },
                {
                    "question": "Teknik borcun (Technical Debt) zamanında ödenmemesinin ekipler üzerindeki en yıkıcı sonucu nedir?",
                    "options": [
                        "A) Elektrik faturasının artması",
                        "B) Basit bir değişikliğin bile haftalar sürmesi, her güncellemede başka yerlerin kırılması ve geliştirici üretkenliğinin sıfıra yaklaşması",
                        "C) Sadece Python'da hata çıkması",
                        "D) Monitörün kapanması"
                    ],
                    "answer": "B",
                    "explanation": "Ödenmeyen teknik borç, kod tabanını kırıntı haline getirir; yeni özellik ekleme hızı çöker ve şirket teknik iflasa sürüklenir."
                }
            ],
            "quiz_en": [
                {
                    "question": "What specifically is quantified by 'Cyclomatic Complexity' in static analysis?",
                    "options": [
                        "A) Disk file storage footprint in megabytes",
                        "B) The number of linearly independent paths through a program's source code (branching via `if`, `while`, `switch`)",
                        "C) Hardware display brightness",
                        "D) Repository star counts"
                    ],
                    "answer": "B",
                    "explanation": "Cyclomatic complexity counts discrete decision points; higher scores correlate directly with defect density and testing friction."
                },
                {
                    "question": "What is the most devastating long-term consequence of unaddressed technical debt on an engineering team?",
                    "options": [
                        "A) Electrical utility bill increases",
                        "B) Engineering velocity collapses: minor modifications take weeks, regressions proliferate, and developer morale plummets",
                        "C) Defects restricted exclusively to Python",
                        "D) Display hardware failures"
                    ],
                    "answer": "B",
                    "explanation": "Compounding technical debt causes paralysis: system changes become high-risk endeavors, bringing innovation to a standstill."
                }
            ]
        }
    ]
