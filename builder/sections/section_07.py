"""
Section 7: Hata Ayıklama (Debugging), Profiling & Gözlemlenebilirlik (Chapters 37 to 42)
"""

def get_section_chapters():
    return [
        # Chapter 37
        {
            "id": 37,
            "section_id": 7,
            "slug_tr": "ch37_dedektif_gibi_dusunmek_bilimsel_debugging",
            "slug_en": "ch37_the_detective_mindset_scientific_debugging",
            "title_tr": "Dedektif Gibi Düşünmek: Debugging'in Psikolojisi ve Bilimsel Metodu",
            "title_en": "The Detective Mindset: Scientific Debugging with AI Partners",
            "subtitle_tr": "Rastgele Kod Değiştirme Çaresizliğinden Hipotez Testine Geçiş",
            "subtitle_en": "Escaping the 'Change Random Lines and Pray' Trap Through Scientific Deduction",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Junior mühendisler bir bug çıktığında neden rastgele satırları değiştirip dua etmeye başlar? Sherlock Holmes gibi hipotez kurarak hata çözmek nasıl bir his?",
            "podcast_hook_en": "Why do novice engineers resort to 'shotgun debugging'—randomly tweaking lines and praying—and how does the scientific method cut diagnosis time by 90%?",
            "takeaways_tr": [
                "Debugging bir şans oyunu değil; bilimsel hipotez kurma ve eleme (Elimination) sürecidir.",
                "İlk kural: Hatayı deterministik olarak yerel makinenizde yeniden üretebilir (reproduce) hale getirin.",
                "AI modelleri çok iyi bir 'Sanal Dedektif Ortağıdır' (Watson); gözlemlediğiniz belirtileri verip olası şüphelileri listelemesini isteyin."
            ],
            "takeaways_en": [
                "Debugging is not a guessing game; it is the rigorous application of the scientific method: Observation, Hypothesis, Test, Conclusion.",
                "Golden Rule 1: You cannot fix what you cannot reliably reproduce locally.",
                "AI serves as your forensic partner (Watson): feed it raw symptoms, eliminate impossible hypotheses, and isolate the culprit."
            ],
            "story_tr": """Sherlock Holmes'un bir cinayet mahalline girdiğini düşünün. 

Holmes odaya girip: *"Hadi rastgele sokaktan bir adamı tutuklayalım, belki katil odur. Olmadı başka birini tutuklarız!"* der mi? Tabii ki demez! Çamur izine bakar, kırık vazoyu inceler, saati kontrol eder. İmkansız olan tüm olasılıkları eledikten sonra geriye kalan tek gerçek ne kadar inanılmaz olursa olsun doğru olandır!

Junior yazılımcıların en büyük hatası **"Pompalı Tüfek Debugging" (Shotgun Debugging)** yapmaktır:
Oradan bir `+1` sil, şuraya bir `await` ekle, orayı `null` yap... Belki çalışır! Kod daha da batar.

Oysa bilimsel debugging şudur:
1. Gözlem: *"Sadece Salı günleri fatura toplamı 0 çıkıyor."*
2. Hipotez: *"Haftanın günü index'i 0'dan mı başlıyor?"*
3. Test: İzole bir test yaz ve hipotezi doğrula!""",
            "story_en": """Picture Sherlock Holmes arriving at a locked-room mystery.

Does he proclaim: *"Let us arrest an arbitrary bystander outside, see if the murder rate drops, and if not, arrest someone else"?* Never. He inspects the mud on the rug, the shattered mantle clock, the cigar ash. Once you eliminate the impossible, whatever remains, however improbable, must be the truth.

The classic junior failure mode is **Shotgun Debugging**:
Add a random `+1`, toss in an unneeded `await`, flip a boolean, refresh the browser, and cross your fingers. The bug metastasizes.

The Scientific Debugging Protocol:
1. Observation: *"User balances drop to zero only on the first day of the month."*
2. Hypothesis: *"Is the monthly cron schedule clearing caches before the settlement ledger writes?"*
3. Experiment: Author an isolated test reproducing the hypothesis deterministically.""",
            "mental_tr": """Bilimsel Hata Ayıklama Döngüsü:

```
[1. GÖZLEM (Symptom)] ──> "Kullanıcı sepete 2. ürünü ekleyince fiyat ikiye katlanıyor."
           │
           ▼
[2. TEKRAR ÜRET (Reproduce)] ──> "Adım 1: Giriş yap, Adım 2: X ekle, Adım 3: Y ekle -> Bug çıktı!"
           │
           ▼
[3. HİPOTEZ KUR (Hypothesis)] ──> "Sepet state'i güncellenirken dizi mutasyona uğruyor olabilir mi?"
           │
           ▼
[4. TEST ET (Experiment)] ──> "Breakpoint veya izole test ile değişkeni izle."
           │
     ┌─────┴─────┐
     ▼           ▼
[DOĞRULANDI]  [ÇÜRÜTÜLDÜ]
(Kök nedeni   (Başka bir hipoteze geç:
 düzelt)       "API yanıtı mı bozuk?")
```""",
            "mental_en": """The Scientific Debugging Lifecycle:

```
[1. OBSERVATION] ──> "User profile displays 'NaN' when currency is set to JPY."
          │
          ▼
[2. DETERMINISTIC REPRODUCTION] ──> Minimal test script replicating the bug 100% of the time.
          │
          ▼
[3. HYPOTHESIS FORMULATION] ──> "Does JPY formatting fail because Japanese Yen has zero decimals?"
          │
          ▼
[4. EXPERIMENTATION] ──> Step through currency helper via debugger breakpoints.
          │
    ┌─────┴─────┐
    ▼           ▼
[CONFIRMED]  [DISPROVEN]
(Ship fix &   (Pivot hypothesis:
 regression    "Is the exchange API
 test)         returning null?")
```""",
            "prompt_tr": """# ROL: Bilimsel Hata Ayıklama ve Dedektiflik Mentoru
Uygulamamızda açıklanamayan bir hata ile karşılaştık.

## BELİRTİLER (Gözlem):
- Kullanıcılar sepete kupon uyguladığında bazen indirim uygulanıyor, bazen de sepet tutarı 0 TL'ye düşüyor.
- Sorun sadece birden fazla sekme açıkken veya hızlı tıklandığında yaşanıyor.

## GÖREV:
Rastgele kod yazma. Bunun yerine:
1. Bu hatayı açıklayabilecek en mantıklı 3 olası HİPOTEZİ listele (Örn: Race condition, state mutasyonu, session çakışması).
2. Bu hipotezleri doğrulamak veya çürütmek için hangi adımları izlemem gerektiğini planla.
3. Hatayı yerel makinemde %100 tekrarlayacak (reproduce) test senaryosunu tarif et.""",
            "prompt_en": """# ROLE: Scientific Debugging Specialist
Our engineering team encountered an intermittent defect.

## OBSERVED SYMPTOMS:
- Applying a discount coupon intermittently zeros out the entire cart total to $0.00.
- Manifests primarily when users open multiple browser tabs or click the button repeatedly.

## TASK:
Do NOT output speculative code fixes yet. Instead:
1. Formulate 3 distinct scientific hypotheses explaining this telemetry (e.g., race condition in database writes, shared mutable session state, optimistic UI desync).
2. Outline specific diagnostic steps to test and eliminate each hypothesis.
3. Provide a deterministic reproduction harness script.""",
            "code_lang": "typescript",
            "code_naive": """// Pompalı Tüfek Debugging: Sorunu anlamadan rastgele yamalar yapıştırmak!
export function applyDiscountShotgun(cart: any) {
  // "Bazen 0 oluyormuş, o zaman 0 ise eski haline getirelim bari!" (KÖK NEDENİ ÇÖZMEZ!)
  if (cart.total === 0) {
    cart.total = cart.previousTotal || 100;
  }
  return cart;
}""",
            "code_robust": """// Kök Neden Analizi Sonucu: Asenkron Race Condition Tespit Edildi ve Çözüldü
export class CartManager {
  private activeDiscountPromise: Promise<number> | null = null;

  async applyDiscountWithLock(cartId: string, couponCode: string): Promise<CartResult> {
    // 1. Kök Neden: Kullanıcı art arda tıkladığında iki istek birbirinin üstüne yazıyordu (Race Condition)
    // Çözüm: Promise Memoization / Mutex Kilidi ile mükerrer istekleri engelle
    if (this.activeDiscountPromise) {
      const pendingTotal = await this.activeDiscountPromise;
      return { cartId, total: pendingTotal };
    }

    try {
      this.activeDiscountPromise = (async () => {
        const cart = await db.cart.findById(cartId);
        const discount = await couponService.calculate(cart, couponCode);
        const newTotal = Math.max(0, cart.subtotal - discount);
        await db.cart.updateTotal(cartId, newTotal);
        return newTotal;
      })();

      const finalTotal = await this.activeDiscountPromise;
      return { cartId, total: finalTotal };
    } finally {
      this.activeDiscountPromise = null; // Kilidi serbest bırak
    }
  }
}""",
            "code_notes_tr": "Belirtiyi gizleyen yamalar yapmak yerine kök neden (race condition) bilimsel olarak tespit edilmiş; promise kilitleme mekanizmasıyla sorun kalıcı olarak çözülmüştür.",
            "code_notes_en": "Rather than masking symptoms with defensive duct tape (`if total === 0`), scientific deduction isolated an asynchronous race condition. Introducing a mutex lock resolved the defect permanently.",
            "pitfalls_tr": [
                {"trap": "Hatayı yerel makinede yeniden üretemeden körü körüne koda müdahale etmek.", "solution": "Bir hatayı düzeltmeye başlamadan önce onu lokalde %100 tekrarlayan bir test yazın."},
                {"trap": "Aynı anda 5 farklı dosyayı değiştirip hangisinin işe yaradığını bilememek.", "solution": "Her seferinde sadece tek bir değişkeni veya hipotezi değiştirip test edin."},
                {"trap": "Bug çözülünce regresyon testi yazmadan PR açmak.", "solution": "Çözdüğünüz her bug için gelecekte tekrar etmesini engelleyen bir unit test ekleyin."}
            ],
            "pitfalls_en": [
                {"trap": "Attempting to fix a bug before reproducing it deterministically on a local machine.", "solution": "Never write fix code until you can trigger the defect on demand with a test case."},
                {"trap": "Mutating multiple variables simultaneously across 5 files.", "solution": "Isolate variables: adjust one parameter per experiment to validate or disprove a single hypothesis."},
                {"trap": "Closing an incident without adding a permanent regression test.", "solution": "Every fixed defect must be accompanied by an automated regression test confirming the failure state no longer recurs."}
            ],
            "udemy_title_tr": "Ders 37: Dedektif Gibi Debugging - Bilimsel Hata Ayıklama",
            "udemy_title_en": "Lecture 37: The Detective Mindset - Scientific Debugging with AI",
            "udemy_slides_tr": [
                "Pompalı Tüfek (Shotgun) Debugging neden kariyerinizi bitirir?",
                "Bilimsel Metot: Gözlem, Hipotez, Deney ve Doğrulama.",
                "Hatayı %100 yeniden üretilebilir (Reproduce) kılmanın sırrı.",
                "Canlı Vaka: Açıklanamayan bir sepet hatasını adım adım çözmek."
            ],
            "udemy_slides_en": [
                "Why 'shotgun debugging' wastes hours and erodes senior confidence.",
                "The scientific method applied to software: Observation, Hypothesis, Experiment, Proof.",
                "The discipline of deterministic reproduction.",
                "Live triage: Methodically diagnosing an intermittent shopping cart failure."
            ],
            "udemy_demo_tr": "İçinde gizli bir race condition olan kodu açın. AI'a 'Bu kodda 3 potansiyel hipotez kur' deyin. Hipotezlerden birini test eden küçük bir script yazıp hatayı tetikleyin ve ardından çözümü gösterin.",
            "udemy_demo_en": "Walk through code harboring an asynchronous race condition. Ask the AI to formulate 3 diagnostic hypotheses. Write a minimal script validating hypothesis #2, trigger the crash, and apply the surgical fix.",
            "action_task_tr": "Karşılaştığınız bir sonraki bug'da hemen kod değiştirmeyin. Bir kağıda: 'Gözlemim', 'Hipotezim' ve 'Doğrulama Adımım' başlıklarını yazıp adımları takip edin.",
            "action_task_en": "On your next bug ticket, write down your hypothesis and proposed experiment before modifying a single line of source code.",
            "quiz_tr": [
                {
                    "question": "Yazılım geliştirmede 'Shotgun Debugging' (Pompalı Tüfek Hata Ayıklama) antipattern'i ne anlama gelir?",
                    "options": [
                        "A) Bilgisayara ateş etmek",
                        "B) Kök nedeni anlamadan ve hipotez kurmadan koddaki satırları rastgele değiştirip şans eseri çalışmasını ummak",
                        "C) Sadece Python'da çalışan bir kütüphane",
                        "D) Testlerin çok hızlı koşması"
                    ],
                    "answer": "B",
                    "explanation": "Shotgun debugging, rastgele deneme-yanılma yöntemidir; sorunun kök nedenini çözmediği gibi kodda yeni ve daha gizli bug'lar yaratır."
                },
                {
                    "question": "Bir hatayı çözmeye başlamadan önce yapılması gereken ilk ve en kritik kural nedir?",
                    "options": [
                        "A) Hemen sunucuyu yeniden başlatmak",
                        "B) Hatayı yerel (local) ortamda deterministik olarak %100 yeniden üretilebilir (reproduce) hale getirmek",
                        "C) Şirket yöneticisine e-posta atmak",
                        "D) Tüm projeyi baştan yazmak"
                    ],
                    "answer": "B",
                    "explanation": "Tekrarlanamayan (reproduce edilemeyen) bir hatanın çözülüp çözülmediğini bilmek imkansızdır. Önce hatanın oluşma şartları izole edilmelidir."
                }
            ],
            "quiz_en": [
                {
                    "question": "What behavior defines the 'Shotgun Debugging' engineering anti-pattern?",
                    "options": [
                        "A) Firing projectiles at physical hardware",
                        "B) Randomly modifying lines across multiple files hoping syntax tweaks will accidentally fix symptoms without understanding the root cause",
                        "C) An official Python debugging utility",
                        "D) Rapid test runner execution"
                    ],
                    "answer": "B",
                    "explanation": "Shotgun debugging relies on random trial-and-error, introducing collateral regressions without addressing underlying architectural causes."
                },
                {
                    "question": "What is the non-negotiable prerequisite before writing a line of bugfix code?",
                    "options": [
                        "A) Rebooting production servers",
                        "B) Establishing a deterministic local reproduction harness that triggers the defect on demand",
                        "C) Escalating an incident ticket to executive leadership",
                        "D) Rewriting the entire application from scratch"
                    ],
                    "answer": "B",
                    "explanation": "If a bug cannot be reproduced deterministically, verifying whether a prospective fix works is impossible."
                }
            ]
        },

        # Chapter 38
        {
            "id": 38,
            "section_id": 7,
            "slug_tr": "ch38_breakpointler_ve_interaktif_debugger_kullanimi",
            "slug_en": "ch38_mastering_breakpoints_and_interactive_debuggers",
            "title_tr": "Breakpoint'ler, Loglar ve Debugger Araçlarını Efektif Kullanmak",
            "title_en": "Mastering Breakpoints, Profilers & Interactive Debuggers",
            "subtitle_tr": "'console.log' Kirliliğinden Kurtulup Zamanı Durdurma Sanatı",
            "subtitle_en": "Eradicating 'console.log' Litter and Freezing Time with Modern Debuggers",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Yazılımcılar neden koda 50 tane `console.log('buraya geldi 1')` yazmayı alışkanlık haline getirir ve interaktif debugger kullanmak bu süreyi nasıl 10 kat kısaltır?",
            "podcast_hook_en": "Why do developers clutter code with 50 `console.log('HERE 1')` statements, and how does mastering interactive breakpoints slash debugging time tenfold?",
            "takeaways_tr": [
                "`console.log` ile hata aramak karanlık bir odada el feneriyle küçük bir noktaya bakmaktır; Debugger ise odanın ana ışığını yakmaktır.",
                "Koşullu Breakpoint (Conditional Breakpoint): Sadece belirli bir koşul sağlandığında (örn: `i === 5000` veya `user.id === 'target'`) durur.",
                "Call Stack (Çağrı Yığını) penceresi, o fonksiyonun hangi fonksiyonlar tarafından çağrıldığını zamanda geriye giderek görmenizi sağlar."
            ],
            "takeaways_en": [
                "`console.log` debugging is scanning a dark room with a penlight; an interactive debugger flips on the master ceiling lights.",
                "Conditional Breakpoints freeze execution only when specific predicates evaluate to true (e.g., `iterationCount === 5000` or `balance < 0`).",
                "The Call Stack panel enables time-travel analysis, allowing you to walk backwards through the callers that led to the crash."
            ],
            "story_tr": """Bir futbol maçını televizyonda izlediğinizi düşünün. Hakem ofsayt kararı verdi.

Eğer elinizde video durdurma teknolojisi olmasaydı ne yapardınız? Maçı baştan sona tekrar oynatıp, top ayağa değdiği anda gözünüzü kırpmadan ekrana bakmaya çalışırdınız! (İşte bu `console.log` ile kod çalıştırmaktır).

Peki VAR (Video Hakem) sistemi ne yapar? Tam topa vurulduğu milisaniyede görüntüyü **DURDURUR (Breakpoint)**. İleriye sarar (Step Over), geriye sarar, oyuncunun milimetrik pozisyonunu inceler (Scope Variables).

Modern IDE'lerin Debugger araçları sizin yazılımdaki VAR sisteminizdir. Zamanı dondurabilir, değişkenlerin içine girebilir ve hatayı nokta atışı yakalayabilirsiniz.""",
            "story_en": """Watch a high-stakes football match where the referee signals offside.

Without video review, your only recourse would be replaying the entire match at full speed, squinting at the screen at the exact second the ball left the passer's boot. That is `console.log` debugging.

What does the Video Assistant Referee (VAR) do? It **FREEZES TIME (Breakpoint)** at the exact microsecond the boot strikes the leather. The referee steps forward frame-by-frame (Step Over), rotates camera angles, and inspects millimeter coordinates (Scope Variables).

Interactive IDE debuggers provide that exact VAR capability for your code. You freeze execution, inspect memory frames, and diagnose the defect with surgical certainty.""",
            "mental_tr": """Debugger Kontrol Tuşları Sözlüğü:

```
⏸️ PAUSE / RESUME (F5):
   Kodu bir sonraki breakpoint'e kadar normal hızında çalıştırır.

⏭️ STEP OVER (F10):
   Mevcut satırı çalıştırır ve alt satıra geçer (Fonksiyonun içine girmeden).

⬇️ STEP INTO (F11):
   Mevcut satırdaki fonksiyonun İÇİNE girer (İç mantığı satır satır görmek için).

⬆️ STEP OUT (Shift+F11):
   Bulunduğunuz fonksiyondan çıkar ve onu çağıran üst fonksiyona geri döner.

🔴 CONDITIONAL BREAKPOINT:
   Kodu sadece `user.age < 0` olduğunda durdurur (10.000 döngüyü tek tek gezmez!).
```""",
            "mental_en": """The Interactive Debugger Command Palette:

```
⏸️ RESUME (F5):
   Continues execution until the next breakpoint encountered.

⏭️ STEP OVER (F10):
   Executes the current line and advances to the next instruction without entering subroutines.

⬇️ STEP INTO (F11):
   Steps into the function call on the current line to inspect internal lines.

⬆️ STEP OUT (Shift+F11):
   Runs the remainder of the current function and returns to the caller frame.

🔴 CONDITIONAL BREAKPOINT:
   Halts execution only when an expression evaluates to true (`index === 999`).
```""",
            "prompt_tr": """# ROL: Debugger ve Geliştirme Araçları Mentoru
VS Code veya Cursor üzerinde Node.js uygulamamızı debug edeceğiz.

## GÖREV:
1. `.vscode/launch.json` dosyasını TypeScript ve `tsx` (veya ts-node) ile anında breakpoint yakalayacak şekilde hazırla.
2. 10.000 elemanlı bir döngüde sadece belirli bir hata anında duracak 'Conditional Breakpoint' kullanımını anlat.
3. Call Stack penceresini kullanarak hatanın hangi ara katmandan tetiklendiğini nasıl tespit edeceğimi göster.""",
            "prompt_en": """# ROLE: IDE Tooling & Debugger Architect
We need to configure an interactive debugging environment for our Node.js/TypeScript stack.

## TASK:
1. Author a `.vscode/launch.json` configuration configured to attach to TypeScript via `tsx`.
2. Demonstrate setting a Conditional Breakpoint inside a loop of 10,000 iterations to catch isolated errors without stepping manually.
3. Explain how to leverage the Call Stack panel to trace caller origins across asynchronous boundaries.""",
            "code_lang": "json",
            "code_naive": """// Kötü / İlkel Yöntem: launch.json yok, kodun her yerine console.log saçmak
// console.log("Burada 1");
// console.log("User:", user);
// console.log("Burada 2");""",
            "code_robust": """// Profesyonel VS Code / Cursor Debug Yapılandırması (.vscode/launch.json)
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "🐛 Debug Mevcut TypeScript Dosyası",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": ["tsx", "${file}"],
      "cwd": "${workspaceFolder}",
      "console": "integratedTerminal",
      "internalConsoleOptions": "neverOpen",
      "skipFiles": [
        "<node_internals>/**",
        "**/node_modules/**"
      ]
    },
    {
      "name": "🌐 Attach to Running Node Process",
      "type": "node",
      "request": "attach",
      "port": 9229,
      "restart": true,
      "skipFiles": ["<node_internals>/**"]
    }
  ]
}""",
            "code_notes_tr": "`skipFiles` ayarı sayesinde debug esnasında yanlışlıkla `node_modules` veya Node.js dahili kütüphanelerine düşmezsiniz; debugger sadece sizin kaynak kodunuz üzerinde adım adım ilerler.",
            "code_notes_en": "The `skipFiles` glob filters prevent the debugger from stepping into third-party `node_modules` or runtime internals, keeping focus entirely on application source files.",
            "pitfalls_tr": [
                {"trap": "Koda geçici `console.log` yazıp production'a commit etmek ve logları kirletmek.", "solution": "Her zaman interaktif breakpoint kullanın; commit öncesi `git diff` ile log kalmadığını teyit edin."},
                {"trap": "Büyük döngülerde normal breakpoint koyup 10.000 kez F5'e basmaya çalışmak.", "solution": "Koşullu Breakpoint (Conditional Breakpoint) koyarak sadece `id === 'hatali-kayit'` anında durmasını sağlayın."},
                {"trap": "Asenkron fonksiyonlarda `await` satırında Step Over yaparken thread'in atlamasını anlayamamak.", "solution": "Event Loop mantığını hatırlayın; asenkron çağrılarda Step Into yerine bir sonraki satıra breakpoint koyun."}
            ],
            "pitfalls_en": [
                {"trap": "Littering production branches with temporary `console.log` statements.", "solution": "Rely on interactive IDE breakpoints; run linters that disallow `no-console` in CI."},
                {"trap": "Placing standard breakpoints inside massive loops, forcing thousands of manual clicks.", "solution": "Set Conditional Breakpoints (`user.id === 'corrupted'`) or Logpoints."},
                {"trap": "Stepping blindly into asynchronous callbacks without inspecting the Call Stack.", "solution": "Leverage the Call Stack window to navigate upward through caller execution contexts."}
            ],
            "udemy_title_tr": "Ders 38: Debugger Ustalığı - console.log'a Veda Etmek",
            "udemy_title_en": "Lecture 38: Interactive Debugger Mastery - Retiring console.log",
            "udemy_slides_tr": [
                "Neden console.log ile hata aramak zaman kaybıdır?",
                "VS Code ve Cursor Debugger anatomisi: F5, F10, F11.",
                "Koşullu Breakpoint (Conditional Breakpoints) ve Logpoints.",
                "Canlı Demo: launch.json ile çalışan backend'e bağlanıp zamanı durdurmak."
            ],
            "udemy_slides_en": [
                "The velocity cost of hunting defects via console logging.",
                "Anatomy of modern debuggers: Breakpoints, Call Stacks, and Scopes.",
                "Supercharging workflows with Conditional Breakpoints and Logpoints.",
                "Live demo: Attaching a debugger to a live Node process and freezing execution."
            ],
            "udemy_demo_tr": "VS Code'da bir fonksiyona kırmızı breakpoint koyun. F5 ile debug modunu başlatın. Kod durduğunda sol paneldeki 'Variables' alanını açın; fonksiyonun içindeki tüm değişkenlerin canlı değerlerini, scope'unu ve Call Stack'i gösterin.",
            "udemy_demo_en": "Set a red breakpoint on an active TypeScript function. Press F5 to trigger the debugger. Inspect live variable values in the Scope pane, evaluate expressions in the Debug Console, and demonstrate Step Over (F10).",
            "action_task_tr": "Projenizde `.vscode/launch.json` dosyasını oluşturun ve bir sonraki hatada `console.log` yazmak yerine kırmızı bir breakpoint koyarak değişkenleri inceleyin.",
            "action_task_en": "Create `.vscode/launch.json` in your repository. Diagnose your next local defect entirely via interactive breakpoints without writing `console.log`.",
            "quiz_tr": [
                {
                    "question": "Bir döngü içinde 5.000 eleman varken, sadece `i === 4250` olduğunda kodun durmasını sağlamak için hangi breakpoint türü kullanılmalıdır?",
                    "options": [
                        "A) Standart Breakpoint",
                        "B) Koşullu Breakpoint (Conditional Breakpoint)",
                        "C) Logpoint",
                        "D) CSS Breakpoint"
                    ],
                    "answer": "B",
                    "explanation": "Koşullu breakpoint, içine yazılan mantıksal ifade true olana kadar kodu durdurmaz; böylece binlerce gereksiz adımı atlar."
                },
                {
                    "question": "Debugger panelinde 'Call Stack' (Çağrı Yığını) penceresinin geliştiriciye sunduğu en önemli bilgi nedir?",
                    "options": [
                        "A) Bilgisayarın pil yüzdesi",
                        "B) O an durulan fonksiyonun hangi fonksiyonlar zinciri tarafından çağrıldığını (kimin kimi tetiklediğini) zamanda geriye dönük göstermesi",
                        "C) Kodun satır sayısı",
                        "D) GitHub şifresi"
                    ],
                    "answer": "B",
                    "explanation": "Call Stack, o anki yürütme noktasına ulaşana kadar hangi fonksiyonların sırayla çağrıldığını gösteren geçmiş izidir."
                }
            ],
            "quiz_en": [
                {
                    "question": "To halt execution inside a loop of 10,000 items strictly when `item.id === 'target'`, which breakpoint type is optimal?",
                    "options": [
                        "A) Standard Unconditional Breakpoint",
                        "B) Conditional Breakpoint",
                        "C) Responsive CSS Breakpoint",
                        "D) Inline Print Statement"
                    ],
                    "answer": "B",
                    "explanation": "Conditional breakpoints evaluate predicates on each iteration, freezing threads only when the condition matches."
                },
                {
                    "question": "What primary forensic context is revealed by the 'Call Stack' panel during active debugging?",
                    "options": [
                        "A) Battery charge status",
                        "B) The active call chain demonstrating which functions invoked the current routine, enabling upward frame navigation",
                        "C) Total codebase line count",
                        "D) Git user credentials"
                    ],
                    "answer": "B",
                    "explanation": "The Call Stack illustrates the execution hierarchy, showing the exact cascade of function calls leading to the current instruction."
                }
            ]
        },

        # Chapter 39
        {
            "id": 39,
            "section_id": 7,
            "slug_tr": "ch39_heisenbuglar_ve_race_condition_asenkron",
            "slug_en": "ch39_heisenbugs_and_concurrency_race_conditions",
            "title_tr": "Heisenbug'lar ve Race Condition: Asenkron Hataları Yakalamak",
            "title_en": "Heisenbugs & Concurrency Pitfalls: Mastering Asynchronous Debugging",
            "subtitle_tr": "İncelemeye Çalıştığınızda Ortadan Kaybolan Hayalet Hatalarla Mücadele",
            "subtitle_en": "Taming Phantom Bugs That Vanish Under Inspection via Asynchronous Discipline",
            "level_tr": "İleri Seviye",
            "level_en": "Advanced",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Koda `console.log` eklediğinizde veya breakpoint koyduğunuzda sihirli bir şekilde düzelen, ama canlıda patlayan 'Heisenbug' nedir ve nasıl çözülür?",
            "podcast_hook_en": "What is a 'Heisenbug'—a defect that magically disappears the moment you add logging or attach a debugger—and how do you trap asynchronous race conditions?",
            "takeaways_tr": [
                "Heisenbug, gözlemlendiğinde (log veya debugger eklendiğinde gecikme değiştiği için) davranışını değiştiren veya kaybolan hatalardır.",
                "Asenkron sistemlerde en büyük tehlike Race Condition'dır (Yarış Durumu); verinin hangi sırayla geleceği garanti edilemez.",
                "`Promise.all` yerine sıralı bağımlılıkları `for..of` ile çözmek veya dağıtık kilitler (Redis Redlock / DB Locks) kullanmak yarış durumunu önler."
            ],
            "takeaways_en": [
                "A Heisenbug alters its behavior or disappears entirely when probed because debugging instrumentation shifts thread timing.",
                "Asynchronous race conditions occur when program correctness depends on uncontrolled ordering of non-deterministic network I/O.",
                "Mitigate race hazards using atomic database operations, deterministic state machines, or distributed mutex locks (Redis Redlock)."
            ],
            "story_tr": """Kuantum fiziğindeki Heisenberg Belirsizlik İlkesini duymuşsunuzdur: Bir elektronun hızını ölçmeye çalıştığınız an, ölçüm aletinin ışığı elektronun yerini değiştirir!

Yazılımda da **Heisenbug** tam olarak budur:
Canlı ortamda iki asenkron işlem yarışıyor. Aralarında 2 milisaniyelik bir fark var ve sistem çöküyor. 
Geliştirici hatayı yakalamak için araya `console.log` veya breakpoint koyuyor. Fakat o `console.log` diske yazarken sistemi 5 milisaniye yavaşlatıyor! Zamanlama değiştiği için hata birdenbire yok oluyor! Geliştirici çıldırır: *"Az önce hata veriyordu, şimdi çalışıyor!"*

Bu hayalet hatalarla baş etmenin tek yolu, şansa bırakılmış zamanlamalara değil, deterministik kilitlere ve sıralama kurallarına güvenmektir.""",
            "story_en": """Quantum physics features Heisenberg's Uncertainty Principle: the act of measuring an electron's position shifts its momentum.

In distributed software engineering, a **Heisenbug** embodies this exact paradox:
Two asynchronous threads race against each other with a 3-millisecond delta in production, corrupting memory.
The engineer inserts a `console.log` to inspect the payload. But flushing that log to disk adds a 5-millisecond delay to Thread A. The timing shift reverses the race order, and the defect magically disappears! The engineer screams: *"It was failing 20 seconds ago, now it passes!"*

Taming these phantom bugs requires abandoning timing assumptions in favor of deterministic synchronization primitives and atomic locks.""",
            "mental_tr": """Race Condition (Yarış Durumu) Anatomisi:

```
BAŞLANGIÇ: Kullanıcı Bakiyesi: 100 TL
İki İstek Aynı Anda Gelir (Çift Tıklama):

İSTEK 1: (50 TL Çek)                 İSTEK 2: (80 TL Çek)
    │                                     │
    ├─ Bakiyeyi Oku: 100 TL                ├─ Bakiyeyi Oku: 100 TL
    ├─ Kontrol: 100 >= 50? (EVET)          ├─ Kontrol: 100 >= 80? (EVET)
    ├─ Yeni Bakiye: 50 TL                  ├─ Yeni Bakiye: 20 TL
    └─ DB'ye Yaz: 50 TL                   └─ DB'ye Yaz: 20 TL
─────────────────────────────────────────────────────────────────
SONUÇ FELAKETİ: 
Kullanıcı 130 TL para çekti, ama hesapta 20 TL kaldı! Banka soyuldu!
ÇÖZÜM: Atomic SQL Update: UPDATE accounts SET balance = balance - 50 WHERE balance >= 50;
```""",
            "mental_en": """The Anatomy of a Concurrent Race Hazard:

```
INITIAL STATE: Account Balance = $100
Concurrent Requests Arrive Within 2 Milliseconds:

REQUEST 1: Withdraw $60               REQUEST 2: Withdraw $70
    │                                     │
    ├─ Read Balance: $100                  ├─ Read Balance: $100
    ├─ Assert: $100 >= $60? (PASS)         ├─ Assert: $100 >= $70? (PASS)
    ├─ Calculate: $100 - $60 = $40         ├─ Calculate: $100 - $70 = $30
    └─ Overwrite DB: $40                   └─ Overwrite DB: $30
─────────────────────────────────────────────────────────────────
DISASTER:
User withdrew $130 from a $100 balance!
SOLUTION: Atomic Database Mutation:
UPDATE accounts SET balance = balance - 60 WHERE balance >= 60;
```""",
            "prompt_tr": """# ROL: Eşzamanlılık (Concurrency) ve Asenkron Sistemler Mimarı
Bir e-ticaret sitesinde bilet satışı yapıyoruz. Son 1 bilet kaldı ve iki kullanıcı aynı anda 'Satın Al' butonuna bastı.

## GÖREV:
1. Bu durumdaki Race Condition tehlikesini ve 'Double-Spending' riskini açıkla.
2. PostgreSQL kullanarak 'Optimistic Locking' veya 'Atomic Update' ile bu sorunu kökten çözen SQL / Prisma kodunu yaz.
3. Node.js tarafında `Promise.all` kullanılırken düşülen asenkron sıralama tuzaklarını listele.""",
            "prompt_en": """# ROLE: Concurrency & Distributed Systems Specialist
We manage inventory for concert tickets with 1 remaining seat. Two users click 'Purchase' within 2 milliseconds of each other.

## TASK:
1. Explain the concurrency race hazard and double-allocation risk.
2. Implement a bulletproof resolution using PostgreSQL Atomic Updates or Optimistic Concurrency Control with Prisma.
3. Detail how misuse of `Promise.all` introduces subtle race conditions in Node.js.""",
            "code_lang": "typescript",
            "code_naive": """// Felaket: Önce oku, sonra kontrol et, sonra yaz (Race Condition Açığı!)
export async function buyTicketNaive(ticketId: string, userId: string) {
  const ticket = await db.ticket.findUnique({ where: { id: ticketId } });
  
  // İki istek aynı anda burayı geçerse ikisi de bileti aldığını sanır!
  if (ticket.isSold) throw new Error("Bilet tükendi.");

  await db.ticket.update({
    where: { id: ticketId },
    data: { isSold: true, ownerId: userId }
  });
  return { success: true };
}""",
            "code_robust": """// Kurşun Geçirmez: Atomik SQL Güncellemesi (Tek İşlemde Oku ve Kilitle)
export async function buyTicketAtomic(ticketId: string, userId: string) {
  // Veritabanı seviyesinde tek satırlık koşullu güncelleme (Row-level atomic write)
  const updatedRows = await db.$executeRaw`
    UPDATE tickets 
    SET is_sold = TRUE, owner_id = ${userId}, version = version + 1
    WHERE id = ${ticketId} AND is_sold = FALSE
  `;

  // Eğer etkilenen satır sayısı 0 ise, yarışı diğer kullanıcı kazanmıştır!
  if (updatedRows === 0) {
    throw new ConflictError("Bilet sizden önce başka bir kullanıcı tarafından satın alındı.");
  }

  return { success: true, message: "Bilet başarıyla adınıza rezerve edildi." };
}""",
            "code_notes_tr": "`UPDATE ... WHERE is_sold = FALSE` sorgusu veritabanı motorunun dahili satır kilidini (Row-level lock) kullanır. İki istek aynı milisaniyede gelse bile veritabanı istekleri kuyruğa sokar; ilki günceller, ikincisi 0 satır etkilediği için `ConflictError` fırlatır.",
            "code_notes_en": "The single atomic `UPDATE ... WHERE is_sold = FALSE` leverages database row-level locking. The database serializes the two requests: the first succeeds, while the second affects 0 rows and trips a `ConflictError`.",
            "pitfalls_tr": [
                {"trap": "Asenkron döngülerde `forEach` kullanmak (forEach asenkron await'leri beklemez!).", "solution": "Sıralı asenkron işlemlerde daima `for (const item of items)` döngüsü kullanın."},
                {"trap": "Para veya stok gibi kritik verileri hafızada (in-memory) tutup veritabanına sonradan yazmak.", "solution": "Kritik kaynakları daima veritabanının atomik kilitleri veya Redis mutex ile koruyun."},
                {"trap": "Heisenbug çıktığında 'şimdi geçti bir şey olmaz' diyerek sorunu görmezden gelmek.", "solution": "Zamanlama hataları canlıda bin kat daha sık çıkar; sorunu izole edip kilit mekanizması ekleyin."}
            ],
            "pitfalls_en": [
                {"trap": "Invoking `await` inside an `Array.forEach` loop (`forEach` ignores promises!).", "solution": "Always use `for (const item of items)` for sequential asynchronous loops."},
                {"trap": "Managing balances or inventory counters purely in Node memory before persisting.", "solution": "Enforce concurrency checks at the persistence layer via atomic database updates."},
                {"trap": "Ignoring Heisenbugs that disappear upon re-running.", "solution": "Timing bugs amplify in production; isolate the concurrency window and implement atomic serialization."}
            ],
            "udemy_title_tr": "Ders 39: Heisenbug ve Race Condition - Asenkron Hatalarla Savaş",
            "udemy_title_en": "Lecture 39: Heisenbugs & Race Conditions - Asynchronous Debugging",
            "udemy_slides_tr": [
                "Heisenbug nedir? İncelendikçe kaybolan hayalet hatalar.",
                "Race Condition (Yarış Durumu) ve Çift Harcama (Double-Spending) tehlikesi.",
                "JavaScript Event Loop ve asenkron döngü tuzakları (forEach vs for..of).",
                "Veritabanı seviyesinde Atomik Kilitler (Atomic Updates) ile mutlak koruma."
            ],
            "udemy_slides_en": [
                "What is a Heisenbug? Phantom defects that mutate under inspection.",
                "Race conditions and the double-spending exploit.",
                "JavaScript Event Loop concurrency traps (`forEach` vs. `for..of`).",
                "Atomic row-level database updates as the ultimate concurrency shield."
            ],
            "udemy_demo_tr": "Node.js'te `Promise.all` ile aynı bakiye fonksiyonuna 10 eşzamanlı istek atan bir script çalıştırın. Naive kodda bakiyenin eksiye düştüğünü gösterin. Ardından atomik SQL kodunu çalıştırıp sadece ilk isteğin geçtiğini, kalan 9'unun engellendiğini kanıtlayın.",
            "udemy_demo_en": "Fire 10 concurrent requests via `Promise.all` against an unhardened balance function. Watch the balance plunge negative. Switch to the atomic SQL update and verify that exactly 1 request succeeds while 9 fail safely.",
            "action_task_tr": "Projenizde bakiye düşürme, stok güncelleme veya kupon kullanma gibi kritik bir fonksiyonu inceleyin. `find` ve `update` iki ayrı adımda yapılıyorsa bunu tek bir atomik sorguya dönüştürün.",
            "action_task_en": "Audit a balance or inventory mutation in your workspace. If implemented as a separate read-then-write, refactor it into a single atomic query.",
            "quiz_tr": [
                {
                    "question": "JavaScript kodunda `[1, 2, 3].forEach(async (id) => { await doTask(id); })` yazıldığında ne olur?",
                    "options": [
                        "A) Görevler sırayla çalışır",
                        "B) `forEach` asenkron Promise dönüşünü beklemez; tüm görevler aynı anda yarışarak asenkron kaos yaratır",
                        "C) Kod hiç çalışmaz",
                        "D) Bilgisayar kapanır"
                    ],
                    "answer": "B",
                    "explanation": "`Array.prototype.forEach` geriye dönen Promise'leri beklemez (await etmez). Sıralı yürütme için `for..of` döngüsü kullanılmalıdır."
                },
                {
                    "question": "Veritabanında eşzamanlı iki isteğin aynı anda stok düşürmesini engellemenin en zarif ve performanslı yolu nedir?",
                    "options": [
                        "A) Sunucuyu 1 saniye bekletmek",
                        "B) `UPDATE products SET stock = stock - 1 WHERE id = 1 AND stock > 0` gibi tek satırlık atomik koşullu güncelleme kullanmak",
                        "C) Kullanıcılara aynı anda tıklamamalarını rica etmek",
                        "D) Veritabanını silmek"
                    ],
                    "answer": "B",
                    "explanation": "Koşullu atomik SQL güncellemesi, veritabanı motorunun dahili satır kilidini kullanarak yarış durumunu (race condition) sıfır ek maliyetle çözer."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the runtime consequence of running `[1, 2].forEach(async (id) => await process(id))`?",
                    "options": [
                        "A) Invocations execute sequentially in ascending order",
                        "B) `forEach` is promise-oblivious; it triggers asynchronous callbacks concurrently without awaiting completion",
                        "C) Syntax errors halt compilation",
                        "D) The thread terminates"
                    ],
                    "answer": "B",
                    "explanation": "`forEach` does not await promises returned by its callback; use standard `for..of` loops for sequential async operations."
                },
                {
                    "question": "What is the most performant architectural defense against concurrent inventory race conditions?",
                    "options": [
                        "A) Injecting a 1-second `setTimeout`",
                        "B) Executing an atomic conditional update (`UPDATE products SET stock = stock - 1 WHERE id = 1 AND stock > 0`)",
                        "C) Admonishing users via UI text not to double-click",
                        "D) Dropping database tables"
                    ],
                    "answer": "B",
                    "explanation": "Atomic conditional updates leverage internal engine locks, serializing mutations and rejecting requests when conditions fail."
                }
            ]
        },

        # Chapter 40
        {
            "id": 40,
            "section_id": 7,
            "slug_tr": "ch40_memory_leak_ve_cpu_bogulmasi_teshisi",
            "slug_en": "ch40_diagnosing_memory_leaks_and_cpu_spikes",
            "title_tr": "Bellek Sızıntısı (Memory Leak) ve CPU Boğulması Teşhisi",
            "title_en": "Diagnosing Memory Leaks & CPU Spikes with AI Flamegraphs",
            "subtitle_tr": "Sunucunun Her 4 Saatte Bir Şişip Çökmesini Node Profiler ile Önlemek",
            "subtitle_en": "Halting 4-Hour Server Crash Cycles Using Node Heap Snapshots and Flamegraphs",
            "level_tr": "İleri Seviye",
            "level_en": "Advanced",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Sunucunuz her gün saat 16:00'da RAM'i tüketip çöküyor ve yeniden başlıyor. Bu gizli bellek sızıntısını (Memory Leak) yapay zeka ve Heap Snapshot ile nasıl teşhis ederiz?",
            "podcast_hook_en": "Your production node cluster exhausts its 8GB RAM every afternoon and crashes. How do you isolate the offending closure or global array using Heap Snapshots?",
            "takeaways_tr": [
                "Bellek Sızıntısı (Memory Leak), artık ihtiyaç duyulmayan nesnelerin referansları silinmediği için Garbage Collector tarafından temizlenememesidir.",
                "En yaygın sızıntı kaynakları: Temizlenmeyen Event Listener'lar, global dizilere sonsuz veri eklemek ve kapanış (Closure) tuzaklarıdır.",
                "Chrome DevTools / Node Inspector ile alınan iki 'Heap Snapshot' karşılaştırılarak hangi nesnelerin biriktiği saniyeler içinde bulunur."
            ],
            "takeaways_en": [
                "A Memory Leak occurs when obsolete heap objects retain active references, preventing the Garbage Collector from freeing RAM.",
                "The primary leak culprits: uncleaned event listeners, unbounded global caches/arrays, and unintended closure scope retention.",
                "Comparing two successive Heap Snapshots in Chrome DevTools pinpoints leaking constructors and retaining trees instantly."
            ],
            "story_tr": """Evinizde bir çöp kovası olduğunu düşünün. 

Her gün eve alışveriş poşetleri, kargo kutuları geliyor. Siz bunları kullanıp çöpe atıyorsunuz ve haftada iki gün çöpçü gelip kovayı boşaltıyor (Garbage Collector).

Peki ya siz kargo kutularını çöpe atmak yerine: *"Aman belki lazım olur"* diyerek yatak odanızın tavanına doğru üst üste yığmaya başlarsanız ne olur? 3 ay sonra odaya sığamaz hale gelirsiniz, kapı kapanmaz ve ev çöker!

Yazılımda **Bellek Sızıntısı (Memory Leak)** tam olarak budur:
Geliştirici global bir diziye her gelen isteğin logunu atar. 10 gün sonra sunucunun 8 GB RAM'i biter ve işletim sistemi uygulamayı acımasızca öldürür (OOM - Out of Memory Kill).""",
            "story_en": """Picture your kitchen trash bin.

Packages, wrappers, and mail arrive daily. You discard them, and municipal sanitation trucks empty your bin twice weekly (Garbage Collector).

Now suppose you hoard every cardboard box in your hallway saying: *"I might need this box in 4 years."* Within 6 months, boxes block your front door and collapse ceiling-high.

That is an enterprise **Memory Leak**:
A developer appends request metrics to an unbounded global array for quick debugging. Two weeks later, the Node process exhausts its 8GB container ceiling, and the Linux kernel executes a brutal Out-Of-Memory (OOM) kill.""",
            "mental_tr": """Garbage Collection ve Referans Tutma Mantığı:

```
[Kök Nesne: Global Scope / Window / Process]
                    │
            (Aktif Referans Var)
                    ▼
          [GlobalCache Dizisi]
                    │
            (Binlerce Eski İstek)
                    ▼
          [UserSession Objesi] ──> GARBAGE COLLECTOR DİYOR Kİ:
                                   "Buna hâlâ globalden erişim var, 
                                    bu yüzden bu nesneyi RAM'den SİLEMEM!"
───────────────────────────────────────────────────────────────────────
ÇÖZÜM: Referansı kopar (session = null) veya LRU Cache kullan!
```""",
            "mental_en": """Garbage Collector Reachability Traversal:

```
[GC Root: Global Scope / Active Closure]
                   │
         (Retaining Reference)
                   ▼
       [GlobalRequestCache Array]
                   │
         (100,000 Expired Contexts)
                   ▼
          [UserPayload Object] ──> GARBAGE COLLECTOR DECISION:
                                   "Reference path to Root exists.
                                    Retention mandated; RAM cannot be reclaimed!"
───────────────────────────────────────────────────────────────────────
REMEDY: Sever retaining pointers (`user = null`) or deploy bounded LRU Caches!
```""",
            "prompt_tr": """# ROL: Node.js Performans ve Profiling Mimarı
Aşağıdaki Express kodunda gizli ve ölümcül bir bellek sızıntısı (Memory Leak) bulunmaktadır.

## KOD:
```typescript
const requestHistory = []; // Global dizi

app.get("/api/data", (req, res) => {
  const context = {
    ip: req.ip,
    headers: req.headers,
    timestamp: new Date()
  };
  requestHistory.push(context); // Her istekte şişiyor!
  res.json({ message: "Başarılı" });
});
```

## GÖREV:
1. Bu kodun neden OOM (Out Of Memory) çöküşüne yol açacağını açıkla.
2. Sınırsız büyüyen dizi yerine 'LRU (Least Recently Used) Cache' mantığını uygulayan güvenli kodu yaz.
3. Node.js'te `--inspect` ve Chrome DevTools ile Heap Snapshot alma adımlarını özetle.""",
            "prompt_en": """# ROLE: Node.js Performance & Memory Profiling Specialist
Analyze this Express handler containing a fatal memory leak:

## SNIPPET:
```typescript
const requestHistory = [];

app.get("/api/data", (req, res) => {
  const context = {
    ip: req.ip,
    headers: req.headers,
    timestamp: new Date()
  };
  requestHistory.push(context);
  res.json({ message: "Success" });
});
```

## TASK:
1. Explain how unbounded retention triggers an Out-Of-Memory (OOM) crash.
2. Refactor using a bounded Least Recently Used (LRU) buffer to strictly cap memory consumption.
3. Outline the forensic protocol for generating and comparing Heap Snapshots via Chrome DevTools.""",
            "code_lang": "typescript",
            "code_naive": """// Felaket: Event Listener temizlenmiyor ve global dizi sınırsız büyüyor
const EventEmitter = require('events');
const eventBus = new EventEmitter();

app.get("/subscribe", (req, res) => {
  // Her istekte yeni bir dinleyici eklenir ama asla silinmez! (Memory Leak)
  eventBus.on("notification", (msg) => {
    res.write(msg);
  });
});""",
            "code_robust": """import { lru } from "tiny-lru";

// 1. Sınırlı Bellek: En fazla 1.000 kayıt tutan LRU Cache (Sabit RAM Kullanımı)
const requestCache = lru<RequestContext>(1000);

export function trackRequestSafe(req: Request) {
  const requestId = crypto.randomUUID();
  requestCache.set(requestId, {
    ip: req.ip,
    timestamp: Date.now()
  });
  // 1001. kayıt geldiğinde en eski kayıt otomatik bellekten atılır (Eviction)
}

// 2. Event Listener Temizliği (Hafıza Güvenliği)
export function attachCleanListener(req: Request, res: Response) {
  const onNotification = (data: string) => {
    res.write(data);
  };

  eventBus.on("notification", onNotification);

  // İstemci bağlantıyı kapattığında dinleyiciyi MUTLAKA kaldır!
  req.on("close", () => {
    eventBus.removeListener("notification", onNotification);
  });
}""",
            "code_notes_tr": "`lru(1000)` kullanılarak bellek tüketimi tavan bir sınırla sabitlenmiş; `req.on('close')` içinde `removeListener` çağrılarak bağlantı kapandığında nesnenin bellekten temizlenmesi garanti edilmiştir.",
            "code_notes_en": "Bounding cache capacity with an LRU queue caps memory allocation deterministically. Registering `req.on('close')` to invoke `removeListener` severs memory retention paths when sockets disconnect.",
            "pitfalls_tr": [
                {"trap": "Geçici verileri global değişkenlerde veya dosya kapsamındaki (module-level) dizilerde saklamak.", "solution": "Global state'ten kaçının; saklanması gereken verileri Redis veya veritabanına yazın."},
                {"trap": "Event listener ekleyip (`socket.on`) bağlantı koptuğunda temizlemeyi (`socket.off`) unutmak.", "solution": "Her listener için mutlaka bir cleanup (temizlik) fonksiyonu tanımlayın."},
                {"trap": "Büyük resim veya dosya işlemlerini belleğe (Buffer) tek parça yüklemek.", "solution": "Büyük verileri işlerken RAM'i şişirmemek için Stream (Akış) API'lerini kullanın."}
            ],
            "pitfalls_en": [
                {"trap": "Storing ephemeral telemetry inside module-level global arrays.", "solution": "Avoid unbounded global structures; persist metrics into external time-series datastores."},
                {"trap": "Registering event handlers without companion deregistration hooks on teardown.", "solution": "Always pair `.on()` subscriptions with `.off()` or abort controller signals."},
                {"trap": "Buffering multi-gigabyte video or binary files completely in memory.", "solution": "Process heavy payloads via Node Streams (`fs.createReadStream`) to maintain bounded memory ceilings."}
            ],
            "udemy_title_tr": "Ders 40: Bellek Sızıntısı & CPU Profiling - OOM Çöküşlerini Önlemek",
            "udemy_title_en": "Lecture 40: Memory Leaks & CPU Profiling - Halting OOM Crashes",
            "udemy_slides_tr": [
                "Bellek Sızıntısı (Memory Leak) nedir? V8 Garbage Collector nasıl çalışır?",
                "En yaygın 3 sızıntı tuzağı: Global arrays, uncleaned listeners, closures.",
                "Chrome DevTools ile Heap Snapshot alma ve karşılaştırma.",
                "Stream kullanarak devasa dosyaları sıfır RAM ile işlemek."
            ],
            "udemy_slides_en": [
                "What is a Memory Leak? Inside the V8 generational Garbage Collector.",
                "The 3 most common leak archetypes: Global arrays, dangling listeners, closures.",
                "Capturing and comparing Heap Snapshots via Chrome DevTools.",
                "Stream processing: Handling gigabyte payloads with flat 20MB memory profiles."
            ],
            "udemy_demo_tr": "Node uygulamasını `node --inspect index.js` ile başlatın. Chrome'da `chrome://inspect` sayfasını açın. Heap Snapshot alın. Koda kasıtlı bir sızıntı ekleyip ikinci snapshot'ı alın. 'Comparison' görünümünde hangi objenin biriktiğini canlı kanıtlayın.",
            "udemy_demo_en": "Launch Node with `node --inspect server.js`. Connect Chrome DevTools to the process. Take an initial Heap Snapshot, execute a leaking loop, capture a second snapshot, and demonstrate the differential retained size.",
            "action_task_tr": "Projenizi `node --inspect` ile çalıştırıp Chrome DevTools üzerinde ilk Heap Snapshot'ınızı alın ve bellekte en çok yer tutan ilk 3 nesne tipini inceleyin.",
            "action_task_en": "Spin up your Node app with `--inspect`, capture a baseline Heap Snapshot in Chrome DevTools, and identify the top 3 constructors by retained size.",
            "quiz_tr": [
                {
                    "question": "Node.js (V8) Garbage Collector'ı bellekteki bir nesneyi neden silemez ve bellek sızıntısına (Memory Leak) yol açar?",
                    "options": [
                        "A) Bilgisayarın pili bittiği için",
                        "B) Nesneye hâlâ kök (Global Scope, aktif Closure veya temizlenmemiş Listener) üzerinden ulaşan aktif bir referans zinciri bulunduğu için",
                        "C) Sadece C++ dilinde kod yazıldığı için",
                        "D) Dosya isimleri çok uzun olduğu için"
                    ],
                    "answer": "B",
                    "explanation": "Garbage Collector sadece hiçbir kök nesneden ulaşılamayan (unreachable) nesneleri temizler. Bir referans unutulduğunda nesne sonsuza kadar bellekte kalır."
                },
                {
                    "question": "1 GB boyutundaki büyük bir CSV dosyasını sunucunun 512 MB RAM'ini patlatmadan işlemek için hangi mimari yaklaşım kullanılmalıdır?",
                    "options": [
                        "A) Dosyayı tek seferde `fs.readFileSync` ile hafızaya almak",
                        "B) Node.js Streams (Akış) kullanarak dosyayı parça parça (chunk by chunk) okuyup işlemek",
                        "C) Dosyayı silmek",
                        "D) Tarayıcıyı kapatmak"
                    ],
                    "answer": "B",
                    "explanation": "Stream'ler veriyi tümüyle RAM'e almak yerine küçük tamponlar (buffer) halinde sırayla işler; böylece dosya ne kadar büyük olursa olsun RAM kullanımı sabit kalır."
                }
            ],
            "quiz_en": [
                {
                    "question": "Why does the V8 Garbage Collector fail to reclaim leaked memory objects?",
                    "options": [
                        "A) Battery exhaustion",
                        "B) The target object remains reachable through an unbroken reference chain anchored to a GC Root (global variable, active closure, dangling listener)",
                        "C) Exclusivity to C++ bindings",
                        "D) File paths exceeding 255 characters"
                    ],
                    "answer": "B",
                    "explanation": "Garbage collectors purge only unreachable objects. As long as any active reference chain traces back to a root, memory cannot be freed."
                },
                {
                    "question": "How should an engineer process a 2GB file on a micro-instance with only 512MB RAM without triggering an OOM crash?",
                    "options": [
                        "A) Load the entire string via `fs.readFileSync`",
                        "B) Process data in discrete chunks via Node Streams (`createReadStream`)",
                        "C) Truncate the file to zero bytes",
                        "D) Restart the runtime"
                    ],
                    "answer": "B",
                    "explanation": "Streams process data incrementally in small buffers, maintaining a flat memory profile regardless of total dataset volume."
                }
            ]
        },

        # Chapter 41
        {
            "id": 41,
            "section_id": 7,
            "slug_tr": "ch41_sucsuz_post_mortem_kulturu_olay_analizi",
            "slug_en": "ch41_blameless_post_mortems_and_incident_analysis",
            "title_tr": "Post-Mortem Kültürü: 'Kimi Suçlayacağız?' Değil, 'Nasıl Öğreneceğiz?'",
            "title_en": "Blameless Post-Mortems: Transforming Incidents into Engineering Wisdom",
            "subtitle_tr": "Production Çöktüğünde Mühendisleri Suçlamayan Şirketlerin Yükselişi",
            "subtitle_en": "Building High-Psychological-Safety Engineering Teams That Learn from Outages",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Bir junior mühendis ilk haftasında yanlışlıkla canlı veritabanını sildiğinde kovulmalı mı, yoksa bir junior'ın canlı veritabanını silebildiği bir sisteme izin veren mimari mi hatalıdır?",
            "podcast_hook_en": "If a junior engineer accidentally drops the production database on Day 3, should they be fired, or is an architecture that permits a junior to drop production the real failure?",
            "takeaways_tr": [
                "Suçsuz Post-Mortem (Blameless Post-Mortem), insan hatasını sistemik bir tasarım zaafı olarak ele alma disiplinidir.",
                "Eğer bir mühendis bir tuşa basarak tüm sistemi çökertebiliyorsa, hata mühendiste değil; o tuşa korkuluk koymayan süreçtedir.",
                "5 Neden (5 Whys) analizi ile yüzeysel bahaneleri aşıp kök mimari zafiyete ulaşılır."
            ],
            "takeaways_en": [
                "A Blameless Post-Mortem treats human error as a symptom of underlying systemic and architectural vulnerabilities.",
                "If an engineer can drop a production cluster with a single CLI command, the fault lies with missing guardrails, not the human.",
                "The '5 Whys' root-cause methodology bypasses superficial finger-pointing to isolate procedural and tooling gaps."
            ],
            "story_tr": """2017 yılında Amazon AWS'de çalışan bir mühendis, faturalandırma sunucularındaki birkaç test sunucusunu kapatmak için terminale bir komut yazdı. Küçük bir yazım hatası (typo) yaptı ve Kuzey Amerika'daki S3 depolama sunucularının devasa bir kısmını kapattı! Tüm dünya çapında binlerce popüler internet sitesi 4 saat boyunca çöktü.

Amazon o mühendisi kovdu mu? **HAYIR!**

Amazon yönetimi şunu söyledi: *"Mühendisimiz kötü niyetli değildi. Sorun, tek bir insanın yazdığı tek bir komutla bu kadar devasa bir sistemin çökmesine izin veren güvenlik bariyerlerimizin eksikliğidir."*

Komutun etkisini kısıtlayan yeni güvenlik sistemleri kuruldu ve o mühendis şirketin en kıdemli çalışanlarından biri olarak kalmaya devam etti.

İşte olgun bir mühendislik kültürü budur: İnsanları suçlamak hataları gizlemeye iter; sistemleri düzeltmek ise şirketi ölümsüz kılar.""",
            "story_en": """In 2017, an Amazon S3 systems engineer executed an operational debugging command intended to take a few billing subsystem servers offline. A subtle typo within the CLI arguments inadvertently dismantled a massive swath of primary US-EAST-1 storage servers. Hundreds of global enterprises collapsed offline for 4 hours.

Did Amazon fire that engineer? **ABSOLUTELY NOT.**

Executive engineering leadership stated: *"Our engineer operated in good faith. The systemic failure was that our operational tooling allowed a single human command to decommission critical infrastructure without circuit-breaker guardrails."*

Automated safety locks were engineered, and that engineer remained a trusted technical leader.

This is the hallmark of elite engineering cultures: Punishing human errors incentivizes hiding mistakes; repairing systemic guardrails guarantees institutional resilience.""",
            "mental_tr": """5 Neden (5 Whys) Kök Neden Analizi Örneği:

```
[OLAY: Canlı veritabanı 45 dakika boyunca çöktü]
  │
  ├─ 1. Neden çöktü? ──> Disk doldu.
  │
  ├─ 2. Disk neden doldu? ──> Debug log dosyaları 500 GB yer kapladı.
  │
  ├─ 3. Loglar neden silinmedi? ──> Log rotasyonu (logrotate) yapılandırılmamıştı.
  │
  ├─ 4. Neden yapılandırılmamıştı? ──> Yeni kurulan sunucu için checklist takip edilmedi.
  │
  └─ 5. KÖK NEDEN: Sunucu kurulumları elle (manual) yapılıyor; Infrastructure as Code (Terraform) otomasyonu yok!
───────────────────────────────────────────────────────────────────────
AKSIYON: "Mühendisi azarla" değil -> "Tüm sunucuları Terraform ile otomatik kur ve log alarmı ekle!"
```""",
            "mental_en": """The '5 Whys' Root-Cause Analysis Framework:

```
[INCIDENT: Production API returned 500 Internal Server Errors for 42 minutes]
  │
  ├─ Why 1: Database connection pool was exhausted.
  │
  ├─ Why 2: Queries on `/orders` were taking 15 seconds instead of 4ms.
  │
  ├─ Why 3: An unindexed join query was introduced to production.
  │
  ├─ Why 4: The CI pipeline lacked an automated query regression gate.
  │
  └─ ROOT CAUSE (Why 5): Feature PRs were merged without schema migration reviews!
───────────────────────────────────────────────────────────────────────
ACTIONABLE REMEDY: "Reprimand the junior" -> NO! "Add an automated migration lint step to GitHub Actions."
```""",
            "prompt_tr": """# ROL: Site Reliability Engineering (SRE) ve Olay Analiz Uzmanı
Dün gece yaşanan bir kesinti için 'Suçsuz Post-Mortem (Blameless Post-Mortem)' raporu hazırlayacağız.

## OLAY BİLGİSİ:
- Tarih: 15 Ekim 2026, 22:15 - 23:00 (45 dk kesinti)
- Etki: Kullanıcılar ödeme yapamadı, yaklaşık 40.000 TL ciro kaybı oluştu.
- Tetikleyici: Yeni yayınlanan güncellemedeki hatalı bir `.env` ortam değişkeni.

## GÖREV:
Profesyonel bir Post-Mortem markdown raporu hazırla:
1. Olay Özeti & Zaman Çizelgesi (Timeline)
2. 5 Neden (5 Whys) Kök Neden Analizi
3. 'Neler İyi Gitti?' ve 'Neler Kötü Gitti?'
4. Önleyici Eylem Maddeleri (Action Items - Sahibi ve Bitiş Tarihi olan somut görevler)""",
            "prompt_en": """# ROLE: Staff SRE & Incident Commander
Author a formal Blameless Post-Mortem document for a critical payment gateway outage:

## INCIDENT DETAILS:
- Window: Oct 15, 2026 (22:15 - 23:00 UTC, 45 minutes duration).
- Impact: Checkout failures across 100% of web traffic; estimated revenue impact: $12,000.
- Trigger: A malformed environment variable deployed during an unscheduled release.

## TASK:
Produce an enterprise-grade Blameless Post-Mortem markdown report:
1. Executive Summary & Minute-by-Minute Timeline
2. 5 Whys Root-Cause Trace
3. What Went Well vs. Where We Got Lucky vs. Gaps
4. Actionable Preventive Corrective Tasks with owners and deadlines""",
            "code_lang": "markdown",
            "code_naive": """# Kötü / Suçlayıcı Rapor:
Dün gece Ahmet yanlış .env dosyasını yüklediği için sistem çöktü.
Ahmet uyarıldı, bir daha yapmayacak.""",
            "code_robust": """# POST-MORTEM RAPORU: [INC-2026-10-15] Ödeme Servisi Kesintisi

## 📋 Yönetici Özeti
15 Ekim 2026 saat 22:15'te ödeme servisi, eksik bir ortam değişkeni (`STRIPE_WEBHOOK_SECRET`) nedeniyle başlatılamamış ve 45 dakika boyunca ödeme alınamamıştır. Toplam 120 işlem etkilenmiştir.

## ⏱️ Olay Zaman Çizelgesi
- **22:10:** v2.4.0 sürümü üretime dağıtıldı (deploy).
- **22:15:** Sentry üzerinde HTTP 500 alarmları tetiklendi.
- **22:25:** Nöbetçi mühendis (On-call) olaya müdahale etti ve rollback kararı aldı.
- **22:50:** Veritabanı geri alma adımı tamamlandı.
- **23:00:** Sistem tamamen sağlıklı duruma döndü.

## 🔍 5 Neden (5 Whys) Analizi
1. **Ödeme servisi neden çöktü?** -> `STRIPE_WEBHOOK_SECRET` değişkeni `undefined` geldi.
2. **Değişken neden eksikti?** -> Prod ortamına değişken elle eklenmemişti.
3. **Neden elle eklenmesi gerekiyordu?** -> Ortam değişkenlerini yöneten merkezi bir Secrets yöneticisi yoktu.
4. **Deploy öncesi neden fark edilmedi?** -> Uygulama ayağa kalkarken değişkenleri kapıda doğrulayan bir kontrol (Zod env check) yoktu.
5. **KÖK NEDEN:** Uygulama eksik konfigürasyonla çalışmaya başlayabilmektedir; 'Fail-Fast' mekanizması eksiktir.

## 🛠️ Düzeltici Eylem Maddeleri (Action Items)
| Görev | Sorumlu | Termin |
| :--- | :--- | :--- |
| `env.mjs` şeması kurularak eksik değişkende derlemenin durdurulması | Can (Backend) | 18 Ekim |
| Staging ortamında deploy öncesi duman testi (smoke test) eklenmesi | Elif (DevOps) | 20 Ekim |
| Müşteri destek ekibine etkilenen kullanıcılara özür kuponu tanımlanması | Zeynep (Ürün) | 16 Ekim |""",
            "code_notes_tr": "Rapor bireyleri suçlamak yerine; eksik konfigürasyonla sunucunun ayağa kalkmasını engelleyen 'Fail-Fast' doğrulama sistemi kurmayı hedefler. Böylece aynı hata gelecekte hiç kimse tarafından tekrarlanamaz.",
            "code_notes_en": "The report diagnoses missing fail-fast configuration gates rather than scapegoating the deploying engineer. Introducing strict schema validation permanently immunizes the organization against this entire class of bugs.",
            "pitfalls_tr": [
                {"trap": "Post-Mortem toplantılarında 'Falanca kişi dikkatsiz davrandı' diyerek insanları hedef almak.", "solution": "Soruyu her zaman 'Sistemimiz dikkatsizliği neden engellemedi?' şeklinde sorun."},
                {"trap": "Post-Mortem raporunu yazıp bir dokümana gömmek ve aksiyon maddelerini yapmamak.", "solution": "Aksiyon maddelerini hemen Jira biletlerine dönüştürün ve bir sonraki sprinte dahil edin."},
                {"trap": "Küçük kesintileri 'nasılsa çabuk çözüldü' diyerek belgelendirmemek.", "solution": "Her kesintiyi şirketin kurumsal hafızasını güçlendiren bir eğitim vakası olarak kaydedin."}
            ],
            "pitfalls_en": [
                {"trap": "Singling out individuals in incident reviews ('The engineer should have been more careful').", "solution": "Frame the post-mortem inquiry: 'Why did our automation fail to catch this human oversight?'"},
                {"trap": "Drafting post-mortem documents and neglecting follow-up action items.", "solution": "Immediately convert action items into high-priority sprint engineering tickets."},
                {"trap": "Sweeping near-miss incidents under the rug because 'it only lasted 2 minutes'.", "solution": "Document near-misses; they are cheap early warnings for impending catastrophic outages."}
            ],
            "udemy_title_tr": "Ders 41: Suçsuz Post-Mortem - Hatalardan Kurumsal Bilgelik Üretmek",
            "udemy_title_en": "Lecture 41: Blameless Post-Mortems - Learning from Engineering Failure",
            "udemy_slides_tr": [
                "Neden suçlama kültürü şirketleri teknik iflasa sürükler?",
                "Blameless Post-Mortem ilkeleri ve psikolojik güvenlik.",
                "5 Neden (5 Whys) analizi ile kök nedene inmek.",
                "Örnek Vaka: 45 dakikalık prod kesintisini aksiyon planına dönüştürmek."
            ],
            "udemy_slides_en": [
                "Why cultures of blame destroy engineering velocity and encourage concealment.",
                "The principles of Blameless Post-Mortems and psychological safety.",
                "The 5 Whys framework for root-cause isolation.",
                "Case Study: Converting a 45-minute production outage into resilient infrastructure."
            ],
            "udemy_demo_tr": "Sentry'de patlayan bir hatanın loglarını açın. Yapay zekaya bu logları verip '5 Whys analizi yap ve suçsuz bir Post-Mortem taslağı oluştur' deyin. Çıkan rapordaki aksiyon maddelerini inceleyin.",
            "udemy_demo_en": "Feed real Sentry telemetry logs into an AI prompt: 'Generate a Blameless Post-Mortem draft and 5 Whys analysis'. Review the generated action items and show how to ticket them in an agile backlog.",
            "action_task_tr": "Geçmişte projenizde yaşadığınız küçük bir hatayı düşünün. Kendinize '5 Neden' sorusunu sorarak hatanın arkasındaki asıl sistemsel eksikliği bir kağıda yazın.",
            "action_task_en": "Pick a defect you introduced recently. Conduct a personal '5 Whys' root-cause trace to isolate the missing tooling or validation check that permitted it.",
            "quiz_tr": [
                {
                    "question": "'Suçsuz Post-Mortem' (Blameless Post-Mortem) yaklaşımının en temel felsefesi nedir?",
                    "options": [
                        "A) Hata yapan çalışanlara ceza kesilmemesi",
                        "B) İnsan hatasını kaçınılmaz kabul edip, hataya izin veren sistemik ve mimari süreçleri iyileştirerek aynı sorunun bir daha ASLA yaşanmamasını sağlamak",
                        "C) Kesintileri müşterilerden gizlemek",
                        "D) Sadece haftalık toplantı yapmak"
                    ],
                    "answer": "B",
                    "explanation": "Suçsuz kültür, hatayı bireylere yüklemek yerine sistemik korumalar (linter, test, CI/CD) inşa ederek kurumun güvenilirliğini artırır."
                },
                {
                    "question": "Bir Post-Mortem raporunda en değerli ve kalıcı bölüm hangisidir?",
                    "options": [
                        "A) Hatanın olduğu günün hava durumu",
                        "B) Somut sorumluları ve teslim tarihleri belirlenmiş 'Önleyici Eylem Maddeleri' (Action Items)",
                        "C) Şirket sahibinin imzası",
                        "D) Hatanın kaç satır sürdüğü"
                    ],
                    "answer": "B",
                    "explanation": "Aksiyon maddeleri olmadan bir post-mortem sadece bir şikayet metnidir. Kalıcı iyileşmeyi sağlayan somut düzeltici görevlerdir."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the core philosophical pillar of a Blameless Post-Mortem?",
                    "options": [
                        "A) Eliminating all performance accountability",
                        "B) Treating human slips as inevitable symptoms of flawed tooling, focusing on systemic safeguards so errors cannot recur",
                        "C) Hiding infrastructure outages from consumers",
                        "D) Weekly status calls"
                    ],
                    "answer": "B",
                    "explanation": "Blameless analysis assumes engineers act with good intent; it reinforces process and automation to absorb human error safely."
                },
                {
                    "question": "What is the most critical and enduring section of an incident Post-Mortem report?",
                    "options": [
                        "A) Ambient office temperature logs",
                        "B) Concrete, measurable Preventive Action Items with designated owners and clear delivery timelines",
                        "C) Executive signature stamps",
                        "D) Stack trace line counts"
                    ],
                    "answer": "B",
                    "explanation": "Without actionable, tracked corrective tasks, post-mortems degenerate into empty documentation. Action items drive real resilience."
                }
            ]
        },

        # Chapter 42
        {
            "id": 42,
            "section_id": 7,
            "slug_tr": "ch42_canli_ortam_gozlemlenebilirligi_sentry_datadog",
            "slug_en": "ch42_production_observability_sentry_telemetry",
            "title_tr": "Canlı Ortam Gözlemlenebilirliği: Sentry, Datadog ve Log Analizi",
            "title_en": "Production Observability: Sentry, Telemetry & AI-Driven Log Triaging",
            "subtitle_tr": "Kullanıcılar 'Site Bozuk' Demeden Önce Hataları Canlıda Yakalamak",
            "subtitle_en": "Catching Crashes and Latency Spikes in Production Before Users Ever Tweet About Them",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Bir şirkette canlıdaki bir hatayı ilk olarak müşteriler Twitter'da şikayet edince öğreniyorsanız, gözlemlenebilirlik (Observability) açısından neden sınıfta kalmışsınızdır?",
            "podcast_hook_en": "If your team first learns about a production crash when customers complain on social media, why has your observability strategy catastrophically failed?",
            "takeaways_tr": [
                "Gözlemlenebilirlik (Observability) 3 temel ayaktan oluşur: Metrikler (Metrics), Loglar (Logs) ve İzler (Traces).",
                "Sentry, kullanıcı tarayıcısında veya sunucuda patlayan hataları anında yakalayarak tam stack trace ve kullanıcı oturumuyla önünüze serer.",
                "AI modelleri, binlerce satırlık Datadog/CloudWatch log akışını tarayarak 'anomali' ve 'kök neden' özetini saniyeler içinde çıkarabilir."
            ],
            "takeaways_en": [
                "Observability rests on 3 core telemetry pillars: Metrics (Aggregations), Logs (Events), and Traces (Request Journeys).",
                "Sentry captures uncaught exceptions across frontends and backends, providing breadcrumbs, network waterfalls, and user context.",
                "AI engines digest massive, noisy log streams in real-time to isolate statistical anomalies and trace signatures."
            ],
            "story_tr": """Hastanenin yoğun bakım ünitesini (ICU) hayal edin.

Hastanın parmağında nabız ölçer (Metrik), başında kalp elektrosu (Trace), hemşirenin elinde saatlik gözlem defteri (Log) vardır. Eğer hastanın kalbi durursa sirenler anında çalar ve doktorlar odaya dalar!

Peki ya yoğun bakımda hiçbir cihaz olmasaydı? Doktorlar hastanın durumunu ancak koridordaki bir ziyaretçi: *"Galiba 3. odadaki hasta nefes almıyor!"* dediğinde öğrenirdi!

İşte canlıya Sentry veya Datadog kurmadan kod atmak, o cihazsız yoğun bakım odasıdır. 

Profesyonel bir ekip, kullanıcı hatayı henüz fark etmeden önce Sentry bildirimini alır, düzeltmeyi yapar ve güncellemeyi yayına alır.""",
            "story_en": """Visit an intensive care unit (ICU) at a trauma hospital.

A pulse oximeter monitors oxygen saturation (Metrics), telemetry screens chart electrocardiograms (Traces), and the nurse maintains a chronological event ledger (Logs). If cardiac rhythms destabilize, alarms sound instantly, dispatching the trauma team before the patient even loses consciousness.

Now imagine an ICU with zero monitors. Doctors would only discover a patient stopped breathing when a visitor walks down the hall and screams: *"I think Room 3 is unresponsive!"*

Deploying production code without Sentry or OpenTelemetry is operating an ICU without monitors.

World-class engineering squads receive Sentry alerts, triage root causes with AI, and deploy fixes before end users ever notice a disruption.""",
            "mental_tr": """Gözlemlenebilirliğin (Observability) 3 Sacayağı:

```
┌────────────────────────────────────────────────────────┐
│                   GÖZLEMLENEBİLİRLİK                   │
└──────────────────────────┬─────────────────────────────┘
                           │
       ┌───────────────────┼───────────────────┐
       ▼                   ▼                   ▼
[1. METRİKLER (Metrics)] [2. LOGLAR (Logs)]  [3. İZLER (Traces)]
- "CPU kullanımı %92"   - Yapılandırılmış JSON- "İstek 1500 ms sürdü:
- "Hata oranı %0.05"    - "Kullanıcı giriş yaptı"  1200 ms DB sorgusu,
- Araç: Prometheus      - Araç: Winston / Pino    300 ms Stripe API"
                                             - Araç: OpenTelemetry
```""",
            "mental_en": """The 3 Pillars of Observability:

```
┌────────────────────────────────────────────────────────┐
│                  OBSERVABILITY TELEMETRY               │
└──────────────────────────┬─────────────────────────────┘
                           │
       ┌───────────────────┼───────────────────┐
       ▼                   ▼                   ▼
[1. METRICS (Aggregates)][2. LOGS (Events)]  [3. TRACES (Lifecycles)]
- "CPU load at 94%"     - Structured JSON events- "Request took 1,400ms:
- "Error rate 0.08%"    - "Order #12 created"     1,200ms slow SQL,
- Tool: Prometheus      - Tool: Winston / Pino    200ms Stripe egress"
                                             - Tool: OpenTelemetry / Sentry
```""",
            "prompt_tr": """# ROL: Observability ve SRE Uzmanı
Next.js / Node.js backend projemize kurumsal düzeyde Sentry entegrasyonu yapacağız.

## GÖREV:
1. `sentry.server.config.ts` yapılandırmasını oluştur (Tracing ve Profiling açık).
2. Hassas kullanıcı verilerinin (şifre, kredi kartı, auth token) Sentry'ye gitmesini engelleyen `beforeSend` filtresini yaz (Sanitization).
3. Yakalanan bir hataya kullanıcı ID'si ve ek iş bağlamı (tags / extra context) ekleme örneğini göster.""",
            "prompt_en": """# ROLE: Staff SRE & Telemetry Specialist
We are integrating production-grade Sentry monitoring into our Node.js/Next.js application.

## TASK:
1. Author a robust `sentry.server.config.ts` configuration enabling distributed tracing and profiling.
2. Implement a `beforeSend` data scrubbing hook stripping authorization headers and sensitive PII.
3. Demonstrate attaching user identities and custom tags (`orderId`, `tier`) to captured exception contexts.""",
            "code_lang": "typescript",
            "code_naive": """// Kötü: console.error ile loglamak (Sunucu çökünce loglar kaybolur, kimse görmez!)
app.post("/checkout", async (req, res) => {
  try {
    await processPayment(req.body);
  } catch (err) {
    console.error("Hata oldu:", err); // Canlıda hiç kimse fark etmez!
    res.status(500).send("Sunucu hatası");
  }
});""",
            "code_robust": """import * as Sentry from "@sentry/node";

// 1. Sentry Başlatma ve Güvenlik Filtresi (sentry.server.ts)
Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV || "production",
  tracesSampleRate: 0.2, // Performans izleme için %20 örnekleme

  // GÜVENLİK: Hassas verileri Sentry'ye göndermeden önce temizle (Scrubbing)
  beforeSend(event) {
    if (event.request?.headers) {
      delete event.request.headers["authorization"];
      delete event.request.headers["cookie"];
    }
    return event;
  }
});

// 2. Güvenli Hata Yakalama ve Bağlam Ekleme
export async function handleCheckout(req: Request, res: Response) {
  try {
    await processPayment(req.body);
    res.json({ success: true });
  } catch (error) {
    // Hatayı zengin bağlamla Sentry'ye bildir
    Sentry.withScope((scope) => {
      scope.setUser({ id: req.user?.id, email: req.user?.email });
      scope.setTag("transaction_type", "subscription_renewal");
      scope.setExtra("cart_payload", req.body);
      Sentry.captureException(error);
    });

    res.status(500).json({ error: "İşlem sırasında beklenmedik bir hata oluştu." });
  }
}""",
            "code_notes_tr": "`beforeSend` filtresiyle hassas auth token ve çerezler temizlenerek KVKK / GDPR uyumu sağlanmış; `withScope` ile hatanın tam olarak hangi kullanıcıda ve hangi işlem tipinde patladığı etiketlenmiştir.",
            "code_notes_en": "The `beforeSend` hook scrubs authentication headers and session cookies to ensure GDPR compliance. `withScope` attaches user context and transactional tags to accelerate debugging triage.",
            "pitfalls_tr": [
                {"trap": "Loglara şifre, TC kimlik no veya kredi kartı bilgilerini düz metin olarak basmak (PII Leak).", "solution": "Hassas alanları log kütüphanelerinde (Pino/Winston) otomatik maskeleyen redactor kullanın."},
                {"trap": "Sentry'ye her milisaniyede log gönderip kotayı 1 günde bitirmek.", "solution": "`tracesSampleRate` oranını production'da makul bir seviyeye (%10 - %20) ayarlayın."},
                {"trap": "Hata oluştuğunda try/catch ile hatayı sessizce yutup hiçbir yere bildirmemek.", "solution": "Catch bloklarında hatayı mutlaka Sentry veya merkezi log sistemine gönderin."}
            ],
            "pitfalls_en": [
                {"trap": "Logging plaintext passwords, credit cards, or national IDs (PII violations).", "solution": "Configure automated redaction masks inside logging transports (Pino serializers)."},
                {"trap": "Configuring 100% trace sampling on high-traffic production APIs, exhausting Sentry quotas in hours.", "solution": "Set `tracesSampleRate: 0.1` (10%) to capture statistically significant telemetry cheaply."},
                {"trap": "Swallowing exceptions silently in catch blocks without reporting to telemetry sinks.", "solution": "Always dispatch unhandled errors to Sentry before returning fallback HTTP responses."}
            ],
            "udemy_title_tr": "Ders 42: Canlı Ortam Gözlemlenebilirliği - Sentry ve Telemetri",
            "udemy_title_en": "Lecture 42: Production Observability - Sentry, Logs & Tracing",
            "udemy_slides_tr": [
                "Gözlemlenebilirliğin (Observability) 3 Sacayağı: Metrics, Logs, Traces.",
                "Sentry kurulumu ve 'Breadcrumbs' ile hatanın adımlarını izlemek.",
                "Hassas veri temizliği (PII Data Scrubbing) ile KVKK uyumu.",
                "Bölüm 7 Özeti: Hata Ayıklama, Profiling ve Sistem Sağlığı."
            ],
            "udemy_slides_en": [
                "The 3 pillars of modern observability: Metrics, Logs, and Traces.",
                "Setting up Sentry: Reconstructing crash lifecycles via Breadcrumbs.",
                "PII Data Scrubbing for GDPR and HIPAA compliance.",
                "Module 7 Recap: Forensic Debugging, Profiling, and Resilient Observability."
            ],
            "udemy_demo_tr": "Sentry dashboard'unu açın. Canlı API'de kasıtlı bir hata tetikleyin. Sentry'nin 2 saniye içinde hatayı nasıl yakaladığını, kullanıcının tıkladığı önceki butonları (breadcrumbs) ve stack trace'i harita gibi gösterdiğini inceleyin.",
            "udemy_demo_en": "Open a Sentry dashboard. Trigger a synthetic error in your app. Demonstrate the incident arriving in under 2 seconds, complete with breadcrumbs, client device metadata, and pinpoint stack traces.",
            "action_task_tr": "Kişisel bir projenize ücretsiz bir Sentry hesabı bağlayın (`@sentry/node` veya `@sentry/react`) ve canlıda kasıtlı bir hata yakalatarak dashboard'da inceleyin.",
            "action_task_en": "Install Sentry into a side project, trigger a simulated exception, and audit the resulting stack trace and breadcrumbs in the Sentry web dashboard.",
            "quiz_tr": [
                {
                    "question": "Yazılım sistemlerinde 'Gözlemlenebilirlik' (Observability) hangi 3 temel veriden oluşur?",
                    "options": [
                        "A) HTML, CSS, JavaScript",
                        "B) Metrikler (Metrics), Loglar (Logs) ve Dağıtık İzler (Traces)",
                        "C) Klavye, Fare, Ekran",
                        "D) Git, Docker, Kubernetes"
                    ],
                    "answer": "B",
                    "explanation": "Modern gözlemlenebilirlik; sayısal metrikler, olay logları ve isteklerin tüm sistem boyunca izlediği dağıtık izlerden (traces) meydana gelir."
                },
                {
                    "question": "Sentry gibi hata izleme araçlarında 'Breadcrumbs' (Ekmek Kırıntıları) ne işe yarar?",
                    "options": [
                        "A) Kuşlara yem vermek için",
                        "B) Hata patlamadan önceki son 10 adımda kullanıcının hangi butonlara bastığını, hangi URL'leri ziyaret ettiğini ve hangi ağ çağrılarının yapıldığını adım adım göstermek",
                        "C) Şifreleri kaydetmek",
                        "D) Dosyaları sıkıştırmak"
                    ],
                    "answer": "B",
                    "explanation": "Breadcrumbs, bir çöküş anından önce sistemde nelerin yaşandığını kronolojik olarak göstererek hatayı dakikalar içinde yeniden üretmeyi sağlar."
                }
            ],
            "quiz_en": [
                {
                    "question": "What three telemetry data types constitute the 'Three Pillars of Observability'?",
                    "options": [
                        "A) HTML, CSS, JavaScript",
                        "B) Metrics, Logs, and Traces",
                        "C) Motherboards, CPUs, and Power Supplies",
                        "D) Repositories, Branches, and Commits"
                    ],
                    "answer": "B",
                    "explanation": "Metrics provide statistical trends, Logs capture discrete events, and Traces visualize end-to-end request latency across services."
                },
                {
                    "question": "What diagnostic capability is conferred by Sentry 'Breadcrumbs'?",
                    "options": [
                        "A) Recompiling broken JavaScript syntax",
                        "B) Recording a chronological timeline of user clicks, route navigations, and console messages leading up to an exception",
                        "C) Encrypting user passwords",
                        "D) Compressing server disk files"
                    ],
                    "answer": "B",
                    "explanation": "Breadcrumbs capture the precise sequence of user interactions and network events that culminated in a crash."
                }
            ]
        }
    ]
