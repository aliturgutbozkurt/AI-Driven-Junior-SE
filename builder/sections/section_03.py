"""
Section 3: Git, Versiyon Kontrolü & Takım İşbirliği (Chapters 13 to 18)
"""

def get_section_chapters():
    return [
        # Chapter 13
        {
            "id": 13,
            "section_id": 3,
            "slug_tr": "ch13_git_temelleri_ve_akilli_commit_stratejisi",
            "slug_en": "ch13_git_essentials_ai_commit_hooks",
            "title_tr": "Git Temelleri & Akıllı Commit Stratejisi: AI ile Anlamlı Geçmiş",
            "title_en": "Git Essentials & AI Commit Hooks: Crafting Meaningful Version History",
            "subtitle_tr": "'WIP', 'Fixed Bug', 'asdasd' Commitlerinden Kurtulma Rehberi",
            "subtitle_en": "Eradicating 'WIP', 'fix bug', and 'asdasd' from Your Professional Repository",
            "level_tr": "Temel / Orta Seviye",
            "level_en": "Foundational / Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Git geçmişi neden bir şirketin en değerli dokümantasyonudur ve yapay zeka ile Conventional Commits standardı nasıl otomatikleştirilir?",
            "podcast_hook_en": "Why is Git history considered an engineering team's most valuable forensic audit trail, and how can AI automate Conventional Commits?",
            "takeaways_tr": [
                "Git commit mesajları sadece ne yaptığınızı değil, o kararı neden aldığınızı anlatmalıdır.",
                "Conventional Commits (feat, fix, refactor, chore) standardı, yapay zekanın kod tabanını daha iyi anlamasını sağlar.",
                "AI destekli Git hook'ları (Husky + Git hooks) ile kalitesiz commit mesajları daha terminalden çıkmadan engellenebilir."
            ],
            "takeaways_en": [
                "Commit messages should document the architectural rationale ('why'), not merely the diff ('what').",
                "The Conventional Commits standard creates machine-readable semantic history that significantly boosts AI reasoning across repos.",
                "AI-powered Git pre-commit and commit-msg hooks catch substandard messages before they pollute remote branches."
            ],
            "story_tr": """Bir adli tıp uzmanının suç mahallini incelediğini düşünün. Masanın üzerinde bir günlük var; ancak sayfaların hepsinde sadece *"Bir şeyler yaptım"*, *"Düzeltme"*, *"Son hali"* yazıyor. Katili bu notlarla bulabilir misiniz? İmkansız!

İşte canlı sunucunuz gece saat 03:00'te çöktüğünde ve acil geri alma (rollback) yapmanız gerektiğinde, o 50 adet *"fixed bug"* veya *"asdasd"* yazan commit mesajları tam olarak o işe yaramaz günlüktür.

Oysa *"fix(auth): prevent token expiration crash by validating clock skew"* yazan bir commit, sistemi saniyeler içinde kurtarır. 

Yapay zeka sayesinde artık harika commit mesajları yazmak 2 saniye sürüyor; tembellik için hiçbir mazeret kalmadı.""",
            "story_en": """Imagine a forensic investigator examining a crime scene diary. Every single entry reads: *"Did some stuff"*, *"Fixed something"*, *"Final update"*. Could anyone reconstruct what transpired? Not a chance.

When your production server crashes at 3:00 AM and you must execute an emergency rollback, 50 uninformative commits reading *"update"* or *"wip"* are that useless diary.

Conversely, a commit titled: *"fix(auth): prevent session expiration crash by validating clock skew"* pinpoints the fix instantly.

With AI Git integrations, generating articulate Conventional Commits requires literally 2 seconds. Laziness is no longer an excuse.""",
            "mental_tr": """Conventional Commits Standardı Formülü:

```
<tür>(<kapsam>): <kısa özet (emir kipi)>

[İsteğe bağlı: Neden bu değişiklik yapıldı? (Motivation & Why)]
[İsteğe bağlı: Varsa kırıcı değişiklik (BREAKING CHANGE)]

Türler:
- feat: Yeni bir kullanıcı özelliği
- fix: Bir hatanın düzeltilmesi
- refactor: Davranışı değiştirmeden kodu temizleme
- test: Test ekleme veya düzeltme
- chore: Bağımlılık güncellemesi, yapılandırma
```""",
            "mental_en": """The Conventional Commits Semantic Formula:

```
<type>(<scope>): <imperative summary>

[Optional Body: What was the architectural motivation? Why now?]
[Optional Footer: References issue #123, BREAKING CHANGE]

Standard Types:
- feat: New consumer-facing feature
- fix: Resolving a functional defect
- refactor: Restructuring logic without altering runtime behavior
- test: Adding or updating assertions
- chore: Build tooling, dependencies, config updates
```""",
            "prompt_tr": """# ROL: Git ve Sürüm Kontrol Uzmanı
Aşağıda `git diff` çıktım bulunmaktadır.

## GİRDİ (git diff):
```diff
diff --git a/src/auth.ts b/src/auth.ts
--- a/src/auth.ts
+++ b/src/auth.ts
@@ -12,3 +12,6 @@ export function verifyToken(token: string) {
+  if (!token || token.trim() === '') {
+    throw new InvalidTokenError('Token boş olamaz');
+  }
```

## GÖREV:
Bu diff için Conventional Commits standardına tam uyumlu:
1. Başlık satırı (Title - en fazla 50 karakter)
2. Açıklama gövdesi (Body - neden yapıldığı ve çözülen güvenlik riski)
çıkar.""",
            "prompt_en": """# ROLE: Git Release Specialist
Analyze the provided `git diff`:

## GIT DIFF INPUT:
```diff
diff --git a/src/auth.ts b/src/auth.ts
--- a/src/auth.ts
+++ b/src/auth.ts
@@ -12,3 +12,6 @@ export function verifyToken(token: string) {
+  if (!token || token.trim() === '') {
+    throw new InvalidTokenError('Token cannot be empty');
+  }
```

## TASK:
Produce a strict Conventional Commit payload:
1. Semantic subject line (< 50 chars, imperative tense).
2. Descriptive body explaining architectural intent and security risk mitigated.""",
            "code_lang": "bash",
            "code_naive": """# Kötü Alışkanlık: Anlamsız, tek satırlık acele commit
git add .
git commit -m "auth duzeltildi"
git push origin main""",
            "code_robust": """# AI Destekli Profesyonel Conventional Commit
git add src/auth.ts
git commit -m "fix(auth): validate empty tokens before verification

Guard against empty and whitespace-only authorization tokens.
Prevents unhandled runtime crashes and rejects malicious empty bearer headers
at the perimeter. Closes #104."

# CLI AI Aracıyla Tek Komutta Üretmek:
# npx czg veya aicommits kullanarak otomatik üretin""",
            "code_notes_tr": "Kıdemli commit mesajı; hatanın kapsamını (`auth`), eylemi (`validate`), gerekçeyi (çökme ve güvenlik açığı engelleme) ve ilişkili bilet numarasını (`#104`) içerir.",
            "code_notes_en": "The robust commit identifies module scope (`auth`), exact action (`validate`), technical justification (guarding against perimeter crashes), and links tracking tickets (`#104`).",
            "pitfalls_tr": [
                {"trap": "Tek bir devasa commit içine 20 farklı ilgisiz işi koyup 'tüm işler bitti' yazmak.", "solution": "Atomik commit prensibini uygulayın; her commit tek bir mantıksal değişikliği temsil etmelidir."},
                {"trap": "Doğrudan `main` veya `master` branch'ine commit atmak.", "solution": "Daima `feat/kullanici-adi` veya `fix/sorun` şeklinde bir feature branch açarak çalışın."},
                {"trap": "Commit mesajını geçmiş zaman ('düzeltildi') ile yazmak.", "solution": "Emir kipi ('düzelt', 'ekle' / 'fix', 'add') kullanarak yazın."}
            ],
            "pitfalls_en": [
                {"trap": "Bundling 20 unrelated architectural modifications into a single monster commit.", "solution": "Adhere to atomic commits: one logical concern per commit."},
                {"trap": "Pushing unreviewed changes directly to `main`.", "solution": "Always isolate work inside dedicated feature branches (`feat/feature-name`)."},
                {"trap": "Writing commit messages in the past tense ('fixed bug').", "solution": "Use imperative present tense ('fix bug', 'add validation') matching Git's internal commit style."}
            ],
            "udemy_title_tr": "Ders 13: Git Ustalığı - AI Destekli Anlamlı Commitler",
            "udemy_title_en": "Lecture 13: Git Mastery - Crafting Semantic Commits with AI",
            "udemy_slides_tr": [
                "Neden kötü commit mesajları şirketlere milyonlarca dolar kaybettirir?",
                "Conventional Commits standardının anatomisi.",
                "Atomik commit felsefesi: Küçük, odaklı, geri alınabilir adımlar.",
                "AICOMMITS ve IDE eklentileriyle tek tuşla commit mesajı üretmek."
            ],
            "udemy_slides_en": [
                "The financial and operational costs of sloppy Git history.",
                "Anatomy of the Conventional Commits specification.",
                "The atomic commit philosophy: Small, reversible, focused diffs.",
                "Automating semantic commit generation via IDE AI tools and CLI hooks."
            ],
            "udemy_demo_tr": "Bir dosyada bilinçli bir değişiklik yapın. Terminalde `git diff` alın. Cursor'ın entegre AI commit butonuna veya `aicommits` CLI aracına basarak diff'i analiz ettirip mükemmel bir Conventional Commit başlığı ürettirin.",
            "udemy_demo_en": "Stage a discrete refactor. Run `git diff`. Trigger an automated AI commit generator in the terminal or IDE, showing how it reads the AST diff to produce a compliant commit message.",
            "action_task_tr": "Bugünden itibaren yapacağınız sonraki 5 commit için Conventional Commits formatını uygulayın (Örn: `feat:`, `fix:`, `refactor:`).",
            "action_task_en": "Commit your next 5 code changes strictly using the Conventional Commits syntax (`feat:`, `fix:`, `refactor:`).",
            "quiz_tr": [
                {
                    "question": "Conventional Commits standardında yeni bir kullanıcı özelliğini sisteme eklerken hangi ön ek kullanılır?",
                    "options": [
                        "A) fix:",
                        "B) feat:",
                        "C) chore:",
                        "D) docs:"
                    ],
                    "answer": "B",
                    "explanation": "`feat` (feature) sisteme yeni bir kullanıcı özelliği veya fonksiyon eklendiğini belirtir."
                },
                {
                    "question": "Atomik commit (Atomic Commit) yapmanın birincil teknik faydası nedir?",
                    "options": [
                        "A) Sabit diski daha hızlı çalıştırması",
                        "B) Bir hata durumunda sadece o küçük değişikliği `git revert` ile sistemi bozmadan geri alabilmek",
                        "C) Sadece Python projelerinde zorunlu olması",
                        "D) GitHub yıldız sayısını otomatik artırması"
                    ],
                    "answer": "B",
                    "explanation": "Atomik commitler sayesinde bir hata tespit edildiğinde 1000 satırlık devasa bir blok yerine sadece sorunlu 5 satırlık commit güvenle geri alınabilir."
                }
            ],
            "quiz_en": [
                {
                    "question": "Which prefix designates a new user-facing functionality under Conventional Commits?",
                    "options": [
                        "A) fix:",
                        "B) feat:",
                        "C) chore:",
                        "D) docs:"
                    ],
                    "answer": "B",
                    "explanation": "`feat:` denotes introducing novel functionality to the consumer application."
                },
                {
                    "question": "What is the primary operational advantage of maintaining atomic commits?",
                    "options": [
                        "A) Accelerating solid-state disk speeds",
                        "B) Enabling granular rollbacks via `git revert` without impacting unrelated features",
                        "C) Compliance with Python-only standards",
                        "D) Automatically boosting GitHub star counts"
                    ],
                    "answer": "B",
                    "explanation": "Atomic commits isolate changes so regressions can be bisected and reverted cleanly without collateral damage."
                }
            ]
        },

        # Chapter 14
        {
            "id": 14,
            "section_id": 3,
            "slug_tr": "ch14_merge_conflict_kabusunu_ai_ile_cozmek",
            "slug_en": "ch14_solving_merge_conflicts_ai_diff",
            "title_tr": "Merge Conflict Kabusunu AI ile 60 Saniyede Çözmek",
            "title_en": "Demystifying Merge Conflicts: Resolving Branch Collisions with AI in 60 Seconds",
            "subtitle_tr": "<<<<<<< HEAD ve >>>>>>> Çatışmalarını Korkusuzca Yönetmek",
            "subtitle_en": "Navigating <<<<<<< HEAD and >>>>>>> Git Conflicts with Strategic Confidence",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Junior mühendisler neden merge conflict çıktığında panikleyip branch'i silme noktasına gelir ve AI her iki tarafın niyetini nasıl birleştirebilir?",
            "podcast_hook_en": "Why do merge conflicts trigger intense junior anxiety, and how can an LLM harmonize the dual intent of colliding branches without breaking tests?",
            "takeaways_tr": [
                "Merge Conflict bir hata değil; iki geliştiricinin aynı kod bloğunu aynı anda değiştirdiğini bildiren bir işbirliği sinyalidir.",
                "Çözüm 'benimkini al' ya da 'onunkini al' ikileminde değil; her iki tarafın iş mantığını harmanlamaktadır.",
                "AI modelleri, conflict marker'larını (`<<<<<<<`, `=======`, `>>>>>>>`) okuyup her iki mantığı kusursuzca sentezleyebilir."
            ],
            "takeaways_en": [
                "A merge conflict is not an error; it is Git's intentional safety mechanism when two developers touch concurrent lines.",
                "The resolution is rarely a binary 'accept current' vs 'accept incoming'; it is synthesizing both business intentions.",
                "LLMs excel at parsing collision markers (`<<<<<<<`, `=======`, `>>>>>>>`) to produce a coherent merged syntax."
            ],
            "story_tr": """İki ressamın aynı tuval üzerinde çalıştığını hayal edin. 

Ahmet tuvalin sağ köşesine güzel bir çınar ağacı çiziyor. Aynı anda Zeynep de tuvalin tam o köşesine bir göl ve kuğu çiziyor. Akşam olup resimleri birleştirmeye kalktıklarında boyalar birbirine giriyor!

İşte bu bir **Merge Conflict**'tir. Git boyaları karıştırmak istemediği için fırçayı elinizden alır ve sorar: *"Burada hem ağaç hem kuğu mu olacak, yoksa birinden vaz mı geçeceksiniz?"*

Junior yazılımcılar genellikle panikleyip rastgele tuşlara basar veya başkasının kodunu siler. Oysa yapay zeka harika bir sanat eleştirmeni gibi bakar: *"Gölün kıyısına ağacı yerleştirelim, ikisi de kalsın"* diyerek çatışmayı çözer.""",
            "story_en": """Imagine two artists collaborating on a single canvas.

Alex paints an oak tree in the lower right quadrant. Simultaneously, Zoey paints a swan swimming across that exact same quadrant. When merging their layers, the wet oil paints clash.

That is a **Merge Conflict**. Because Git refuses to guess your artistic intent, it halts and asks: *"Do we keep the tree, the swan, or integrate both?"*

Unprepared developers often panic and discard a teammate's hard work. An AI assistant acts as the master curator: *"Let us place the swan gliding beneath the overhanging oak branches,"* harmonizing both branches smoothly.""",
            "mental_tr": """Merge Conflict Anatomisi:

```
<<<<<<< HEAD (Senin Değişikliğin - Current Change)
const taxRate = 0.20; // Türkiye KDV güncellemesi
=======
const taxRate = 0.18;
const hasCustomDiscount = true; // Takım arkadaşının eklediği yeni özellik
>>>>>>> incoming-branch (Gelen Değişiklik)

───────────────────────────────────────────────────────
AI Sentezi (Doğru Çözüm):
const taxRate = 0.20; // Güncel oran korundu
const hasCustomDiscount = true; // Arkadaşının özelliği dahil edildi
```""",
            "mental_en": """Anatomy of a Conflict Block:

```
<<<<<<< HEAD (Your Branch - Current Change)
const taxRate = 0.20; // Regulatory tax rate update
=======
const taxRate = 0.18;
const hasCustomDiscount = true; // Teammate's new promo feature
>>>>>>> incoming-branch (Their Branch - Incoming Change)

───────────────────────────────────────────────────────
AI Synthesis (Harmonious Resolution):
const taxRate = 0.20; // Kept latest tax compliance
const hasCustomDiscount = true; // Preserved teammate's new feature
```""",
            "prompt_tr": """# ROL: Git Merge ve Çatışma Çözüm Uzmanı
Aşağıdaki dosyada bir Git Merge Conflict meydana geldi.

## ÇATIŞAN KOD BLOĞU:
```typescript
<<<<<<< HEAD
export async function fetchUserOrders(userId: string) {
  // Sıralama özelliği eklendi
  return await db.orders.findMany({ where: { userId }, orderBy: { createdAt: 'desc' } });
}
=======
export async function fetchUserOrders(userId: string, limit: number = 10) {
  // Sayfalama (pagination) limiti eklendi
  return await db.orders.findMany({ where: { userId }, take: limit });
}
>>>>>>> feature/pagination
```

## GÖREV:
1. Her iki tarafın ne amaçladığını ayrı ayrı açıkla.
2. Her iki özelliği de (hem orderBy hem take limiti) içeren birleşik ve hatasız nihai fonksiyonu yaz.
3. Conflict marker'larını tamamen temizle.""",
            "prompt_en": """# ROLE: Git Conflict Resolution Specialist
The following merge collision occurred in our repository:

## CONFLICTED SNIPPET:
```typescript
<<<<<<< HEAD
export async function fetchUserOrders(userId: string) {
  return await db.orders.findMany({ where: { userId }, orderBy: { createdAt: 'desc' } });
}
=======
export async function fetchUserOrders(userId: string, limit: number = 10) {
  return await db.orders.findMany({ where: { userId }, take: limit });
}
>>>>>>> feature/pagination
```

## TASK:
1. Summarize the intent of each branch.
2. Deliver a unified production-grade function combining both intents (descending order AND pagination limit).
3. Strip all Git conflict boundary markers.""",
            "code_lang": "typescript",
            "code_naive": """// Kötü / Aceleci Çözüm: Takım arkadaşının limit parametresini silip sadece kendi kodunu bırakmak
export async function fetchUserOrders(userId: string) {
  // Arkadaşının yaptığı tüm sayfalama mantığı çöpe gitti!
  return await db.orders.findMany({ where: { userId }, orderBy: { createdAt: 'desc' } });
}""",
            "code_robust": """// AI ile Sentezlenmiş Doğru Çözüm: Her iki özellik korunur
export interface FetchOrdersOptions {
  limit?: number;
  direction?: 'asc' | 'desc';
}

export async function fetchUserOrders(
  userId: string, 
  options: FetchOrdersOptions = {}
) {
  const { limit = 10, direction = 'desc' } = options;

  return await db.orders.findMany({
    where: { userId },
    orderBy: { createdAt: direction },
    take: limit
  });
}""",
            "code_notes_tr": "Çatışma çözülürken tek bir tarafın kodunu ezmek yerine, fonksiyon bir seçenekler objesi (`FetchOrdersOptions`) alacak şekilde genişletilmiş; böylece hem sıralama hem de sayfalama özellikleri kusursuzca birleştirilmiştir.",
            "code_notes_en": "Rather than discarding either branch, the function signature is generalized with an options object (`FetchOrdersOptions`), satisfying both ordering requirements and pagination limits seamlessly.",
            "pitfalls_tr": [
                {"trap": "Panikleyip `git checkout --ours` veya `git checkout --theirs` diyerek bir tarafı tamamen ezmek.", "solution": "Her zaman iki tarafın kodunu da dikkatle okuyup birleştirin."},
                {"trap": "Conflict marker'larını (`<<<<<<<`, `=======`) dosyada unutup commit etmek.", "solution": "Commit etmeden önce mutlaka `git diff` ve testleri (`npm test`) çalıştırın."},
                {"trap": "Haftalarca ana branch'ten (`main`) pull almayıp çatışmaların devasa bir boyuta ulaşmasına izin vermek.", "solution": "Her sabah çalışmaya başlarken `git pull origin main` ile yerel branch'inizi güncel tutun."}
            ],
            "pitfalls_en": [
                {"trap": "Blindly running `git checkout --ours` and obliterating a teammate's changes.", "solution": "Audit the diff to synthesize both logical intents."},
                {"trap": "Leaving conflict markers (`<<<<<<<`, `>>>>>>>`) in files and committing broken syntax.", "solution": "Always run project test suites and linter before staging resolved files."},
                {"trap": "Working in an isolated branch for weeks without rebasing against main.", "solution": "Rebase or merge from upstream `main` daily to resolve micro-conflicts continuously."}
            ],
            "udemy_title_tr": "Ders 14: Korkusuz Git - Merge Conflict'leri AI ile Çözmek",
            "udemy_title_en": "Lecture 14: Fearless Git - Resolving Merge Conflicts via AI",
            "udemy_slides_tr": [
                "Merge Conflict nedir ve neden korkulmamalıdır?",
                "HEAD vs Incoming: Çatışma etiketlerini okumak.",
                "Cursor ve VS Code 3-Way Merge Editörünü kullanmak.",
                "AI ile çatışan iki iş mantığını tek bir fonksiyonda sentezlemek."
            ],
            "udemy_slides_en": [
                "Demystifying merge conflicts: Git's built-in safety net.",
                "Reading HEAD vs. Incoming change delimiters.",
                "Leveraging 3-way merge tools inside modern IDEs.",
                "AI synthesis: Blending colliding logic into clean abstractions."
            ],
            "udemy_demo_tr": "Lokalde iki farklı branch açın. Aynı dosyanın 10. satırını iki branch'te farklı değiştirip merge çatışması üretin. IDE'nin conflict arayüzünü ve AI 'Resolve Conflict' butonunu kullanarak çatışmayı 30 saniyede çözün ve testleri çalıştırın.",
            "udemy_demo_en": "Create two dummy Git branches modifying the same line in a file. Trigger a merge conflict. Open the IDE merge tool, feed the conflict into AI, generate the synthesized resolution, and run tests.",
            "action_task_tr": "Bir test reposunda bilerek bir merge conflict yaratın. Conflict etiketlerini AI'a vererek çözdürmeyi deneyin.",
            "action_task_en": "Simulate a merge collision in a scratch repository and resolve it using your AI editor's inline assistant.",
            "quiz_tr": [
                {
                    "question": "Git merge conflict çıktığında `<<<<<<< HEAD` etiketi neyi temsil eder?",
                    "options": [
                        "A) Uzaktaki sunucuda silinen kodları",
                        "B) Şu an üzerinde bulunduğunuz mevcut branch'teki yerel değişiklikleri",
                        "C) GitHub şifrenizi",
                        "D) Hatalı yazılmış CSS kodunu"
                    ],
                    "answer": "B",
                    "explanation": "`HEAD`, şu an aktif olarak bulunduğunuz branch'teki (mevcut) değişiklikleri simgeler."
                },
                {
                    "question": "Büyük ve sancılı merge conflict'lerini önlemenin en etkili takım alışkanlığı nedir?",
                    "options": [
                        "A) Hiç kod yazmamak",
                        "B) Küçük branch'lerle çalışmak ve her gün ana branch'ten (`main`) güncellemeleri çekmek (Pull/Rebase)",
                        "C) Sadece ayda bir commit atmak",
                        "D) Tüm ekibin aynı bilgisayardan kod yazması"
                    ],
                    "answer": "B",
                    "explanation": "Sık aralıklarla ana branch ile senkronize olmak ve küçük branch'ler kullanmak çatışmaların büyümesini engeller."
                }
            ],
            "quiz_en": [
                {
                    "question": "In a Git conflict marker, what is enclosed by `<<<<<<< HEAD`?",
                    "options": [
                        "A) Deletions on the remote master server",
                        "B) Changes residing on your currently active local branch",
                        "C) User authentication tokens",
                        "D) Broken stylesheet declarations"
                    ],
                    "answer": "B",
                    "explanation": "`HEAD` designates the local commit state of the branch currently checked out."
                },
                {
                    "question": "What team practice most effectively prevents catastrophic merge conflicts?",
                    "options": [
                        "A) Freezing all code commits",
                        "B) Maintaining short-lived feature branches and regularly pulling/rebasing against `main`",
                        "C) Committing once per month",
                        "D) Sharing a single physical workstation"
                    ],
                    "answer": "B",
                    "explanation": "Short-lived branches merged continuously prevent divergence between concurrent feature streams."
                }
            ]
        },

        # Chapter 15
        {
            "id": 15,
            "section_id": 3,
            "slug_tr": "ch15_kusursuz_pull_request_yazma_sanati",
            "slug_en": "ch15_authoring_world_class_pull_requests",
            "title_tr": "Kusursuz Pull Request (PR) Yazma Sanatı: AI ile PR Açıklamaları",
            "title_en": "Authoring World-Class Pull Requests: AI-Driven Contextual PR Descriptions",
            "subtitle_tr": "Senior Mühendislerin İlk Bakışta Onaylayacağı (LGTM) PR'lar Hazırlamak",
            "subtitle_en": "Engineering PRs That Earn Instant Approval (LGTM) from Senior Leads",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Senior mühendisler neden boş veya 'değişiklikler yapıldı' yazan PR'ları görmekten nefret eder ve AI ile nasıl kusursuz bir PR şablonu doldurulur?",
            "podcast_hook_en": "Why do tech leads dread reviewing PRs with blank descriptions, and how can AI turn raw git diffs into structured, self-explanatory PR reviews?",
            "takeaways_tr": [
                "Bir Pull Request sadece kod değişikliği değil; takım arkadaşlarınıza yaptığınız bir satış sunumudur.",
                "İyi bir PR: 'Neyi değiştirdim?', 'Neden değiştirdim?' ve 'Nasıl test ettim?' sorularına eksiksiz yanıt verir.",
                "AI CLI araçları veya GitHub Actions, git diff'ini okuyarak ekran görüntüleri hariç PR açıklamasını saniyeler içinde taslaklaştırabilir."
            ],
            "takeaways_en": [
                "A Pull Request is not merely code; it is a technical pitch demonstrating competence and respect for reviewers' time.",
                "A world-class PR explicitly answers: 'What changed?', 'Why was it necessary?', and 'How was it verified?'.",
                "AI tooling converts raw git diffs into structured markdown PR templates with checkboxes and testing steps in seconds."
            ],
            "story_tr": """Bir restorana gittiğinizi ve garsonun masanıza kapağı kapalı, dumanlar tüten bir tabak bırakıp tek kelime etmeden gittiğini düşünün. İçinde ne olduğunu, alerjen içerip içermediğini, et mi sebze mi olduğunu bilmiyorsunuz. O yemeği hemen yer misiniz? Asla!

Açıklaması boş bırakılmış veya *"bug fix"* yazılmış bir Pull Request de o kapalı tabaktır. Kıdemli mühendis o PR'ı incelemek için saatlerce kodun içine dalıp *"Bu çocuk burada ne yapmaya çalışmış?"* diye dedektiflik yapmak zorunda kalır.

Oysa tabağı açıp: *"Şefimizin özel mantarlı risotto yemeği, glütensizdir ve fırında 20 dakika pişti"* diyen bir garson güven verir.

Kusursuz bir PR açıklaması, kıdemli mühendise *"Gözüm kapalı onaylayabilirim (LGTM)"* dedirten en büyük profesyonellik göstergesidir.""",
            "story_en": """Picture sitting at a fine restaurant when a server drops a covered metal platter on your table and walks away without saying a word. You have no idea what ingredients it contains or if you are allergic to it. Would you eat it? Unlikely.

A Pull Request with an empty description or a one-line comment like *"updates"* is that mysterious covered plate. Reviewers are forced to play detective: *"What was this engineer trying to accomplish here?"*

Conversely, a server who lifts the cloche and presents the dish inspires complete confidence.

An articulate PR description demonstrates professional maturity and earns rapid 'Looks Good To Me' (LGTM) approvals.""",
            "mental_tr": """Altın Standart PR Şablonu:

```markdown
## 🎯 Amaç & Çözülen Problem
- [Jira-123]: Kullanıcı şifre sıfırlama akışında yaşanan zaman aşımı hatası giderildi.

## 🛠️ Yapılan Değişiklikler
- `authService.ts`: Token geçerlilik süresi 15 dakikadan 30 dakikaya çıkarıldı.
- `mailer.ts`: Şifre sıfırlama e-postasına yeni şablon entegre edildi.

## 🧪 Nasıl Test Edildi?
- [x] Unit testler çalıştırıldı (`npm run test:auth`).
- [x] Yerel ortamda MailHog ile sahte e-posta gönderimi doğrulandı.

## 📸 Ekran Görüntüleri / Kanıt (UI Değişiklikleri İçin)
[Ekran Görüntüsü / GIF]
```""",
            "mental_en": """The Gold-Standard PR Blueprint:

```markdown
## 🎯 Objective & Motivation
- Closes [ISSUE-404]: Resolves intermittent session drops during multi-factor auth.

## 🛠️ Summary of Changes
- `authService.ts`: Adjusted token validity window to accommodate slow networks.
- `mailer.ts`: Integrated responsive password reset email template.

## 🧪 Verification & Testing Evidence
- [x] Unit test suites executed (`npm run test:auth`).
- [x] Manual verification tested against MailHog local SMTP server.

## 📸 Visual Evidence (UI / Behavioral Diffs)
[Attached Loom / GIF / Screenshots]
```""",
            "prompt_tr": """# ROL: Kıdemli Yazılım Ekip Lideri
Aşağıdaki `git diff --stat` ve kod değişikliklerimi incele.

## DEĞİŞİKLİK ÖZETİ:
- `src/controllers/payment.ts`: İki adımlı ödeme doğrulama eklendi.
- `src/services/stripe.ts`: Webhook imza kontrolü eklendi.
- `tests/payment.test.ts`: 4 yeni unit test eklendi.

## GÖREV:
GitHub için profesyonel, markdown formatında eksiksiz bir Pull Request (PR) açıklaması hazırla.
İçinde:
1. Problem tanımı
2. Teknik çözüm özeti
3. Test adımları kontrol listesi (checkbox)
4. Güvenlik notu
bulunsun.""",
            "prompt_en": """# ROLE: Staff Engineer & Reviewer
Analyze these branch diff summary metrics:

## DIFF SUMMARY:
- `src/controllers/payment.ts`: Added two-step idempotency check.
- `src/services/stripe.ts`: Enforced HMAC webhook signature validation.
- `tests/payment.test.ts`: Added 4 unit assertions covering replay attacks.

## TASK:
Generate a structured, professional Markdown Pull Request description:
1. Executive summary & motivation
2. Architectural diff highlights
3. Verification checklist
4. Security implications note""",
            "code_lang": "markdown",
            "code_naive": """# Kötü PR Açıklaması:
odeme duzeltildi testler geciyor""",
            "code_robust": """## 🎯 Problem & Çözüm Özeti
Stripe üzerinden gelen mükerrer webhook bildirimleri nedeniyle bazı kullanıcıların kartından iki kez para çekilme riski bulunuyordu. 

Bu PR ile **Idempotency Key (Tekillik Anahtarı)** deseni uygulanmış ve webhook istekleri için HMAC imza doğrulaması zorunlu kılınmıştır.

## 🛠️ Değişiklik Maddeleri
- `payment.ts`: İşlem öncesinde Redis üzerinden `idempotencyKey` varlığı sorgulanır.
- `stripe.ts`: `stripe.webhooks.constructEvent` kullanılarak sahte bildirimler engellenir.
- `payment.test.ts`: Aynı payload iki kez gönderildiğinde ikincisinin engellendiği test edildi.

## 🧪 Test Kontrol Listesi
- [x] Tüm unit testler başarıyla geçti (`npm test`).
- [x] Stripe CLI ile yerel ortamda webhook tetiklendi (`stripe trigger payment_intent.succeeded`).
- [x] Kötü niyetli (imzasız) isteklerin 400 Bad Request aldığı doğrulandı.

## 🔒 Güvenlik Notu
Yeni bir kütüphane eklenmemiştir; Stripe SDK'nın yerel doğrulama metodu kullanılmıştır.""",
            "code_notes_tr": "Bu derece ayrıntılı bir PR açıklaması gören bir tech lead, kod tabanına güven duyar ve gereksiz soru-cevap turlarına girmeden onay verir.",
            "code_notes_en": "Reviewing an articulate, evidence-backed PR description builds immense team trust and cuts review cycle latencies from days to minutes.",
            "pitfalls_tr": [
                {"trap": "1000'den fazla satır içeren devasa ('canavar') PR'lar açmak.", "solution": "Bir PR'ın maksimum 200-400 satır arasında kalmasına özen gösterin; büyük işleri küçük parçalara bölün."},
                {"trap": "Test sonuçlarını veya ekran görüntülerini PR'a eklememek.", "solution": "Özellikle frontend değişikliklerinde öncesi/sonrası ekran görüntüsü ekleyin."},
                {"trap": "PR açtıktan sonra CI/CD boru hattının (GitHub Actions) kırmızı yandığını fark etmemek.", "solution": "PR açtıktan sonra en az 3 dakika testlerin yeşile dönmesini ekrandan takip edin."}
            ],
            "pitfalls_en": [
                {"trap": "Submitting gargantuan 1,500-line monster Pull Requests.", "solution": "Cap PRs between 200 and 400 lines; decompose large initiatives into incremental stacks."},
                {"trap": "Omitting visual proof on UI modifications.", "solution": "Attach before/after screenshots or short Loom recordings."},
                {"trap": "Filing a PR and immediately logging off while CI tests fail in the background.", "solution": "Monitor the CI pipeline until all green checkmarks confirm a passing build."}
            ],
            "udemy_title_tr": "Ders 15: Kusursuz Pull Request - Senior'ların Güvenini Kazanmak",
            "udemy_title_en": "Lecture 15: World-Class Pull Requests - Earning Senior Trust",
            "udemy_slides_tr": [
                "PR nedir? Bir kod değişikliğinden öte bir iletişim aracı.",
                "Altın Standart PR şablonunun bileşenleri.",
                "AI ile git diff'inden otomatik PR açıklaması üretmek.",
                "Büyük PR'ları küçük parçalara bölme stratejisi."
            ],
            "udemy_slides_en": [
                "PRs as communicative storytelling, not raw code dumps.",
                "Anatomy of the gold-standard PR template.",
                "Generating automated PR summaries from Git diffs using AI CLI tools.",
                "Strategies for breaking down monolithic diffs into stacked PRs."
            ],
            "udemy_demo_tr": "GitHub üzerinde yeni bir PR açma ekranını gösterin. Terminaldeki diff'i AI'a kopyalayıp 15 saniyede markdown PR metni ürettirin. PR açıklamasına yapıştırıp önizlemesini gösterin.",
            "udemy_demo_en": "Navigate to the GitHub New Pull Request interface. Pipe your branch diff into an AI prompt to draft a complete PR markdown body with testing checkboxes. Paste and preview it live.",
            "action_task_tr": "Açacağınız bir sonraki PR'da 'Altın Standart PR Şablonu'nu kullanın ve en az bir test ekran görüntüsü veya terminal test çıktısı ekleyin.",
            "action_task_en": "Structure your very next Pull Request using the 4-part blueprint (Problem, Solution, Test Verification, Security).",
            "quiz_tr": [
                {
                    "question": "Bir Pull Request açılırken kıdemli bir mühendisin en çok görmek istediği bilgi hangisidir?",
                    "options": [
                        "A) Geliştiricinin en sevdiği müzik",
                        "B) Değişikliğin neden yapıldığı (problem tanımı) ve nasıl test edildiğinin kanıtı",
                        "C) PR'ın kaç dakikada yazıldığı",
                        "D) Bilgisayarın işlemci markası"
                    ],
                    "answer": "B",
                    "explanation": "Kıdemli mühendis kodun ne olduğunu diff'te görür; ancak 'neden' yapıldığını ve güvenilirliğini ancak PR açıklamasından ve test kanıtlarından anlar."
                },
                {
                    "question": "Bir Pull Request'in ideal büyüklüğü (satır sayısı) ne kadar olmalıdır?",
                    "options": [
                        "A) En az 5.000 satır",
                        "B) 10.000 satır",
                        "C) 200 - 400 satır arası odaklanmış küçük parçalar",
                        "D) Sadece 1 karakter"
                    ],
                    "answer": "C",
                    "explanation": "Araştırmalar, 400 satırdan büyük PR'larda inceleme kalitesinin dramatik şekilde düştüğünü ve hataların gözden kaçtığını göstermektedir."
                }
            ],
            "quiz_en": [
                {
                    "question": "What information does a tech lead prioritize most when evaluating a Pull Request?",
                    "options": [
                        "A) The author's personal workstation configuration",
                        "B) The architectural motivation ('why') and concrete verification evidence ('how tested')",
                        "C) How many minutes the developer spent typing",
                        "D) CPU clock speeds"
                    ],
                    "answer": "B",
                    "explanation": "Code diffs demonstrate syntax; PR descriptions clarify intent, business context, and safety verification."
                },
                {
                    "question": "What is the optimal line count for a standard Pull Request to ensure thorough review?",
                    "options": [
                        "A) 5,000+ lines",
                        "B) 10,000 lines",
                        "C) 200 to 400 focused lines",
                        "D) Exactly 1 character"
                    ],
                    "answer": "C",
                    "explanation": "Empirical studies prove review comprehension declines steeply beyond 400 lines, letting subtle bugs slip into production."
                }
            ]
        },

        # Chapter 16
        {
            "id": 16,
            "section_id": 3,
            "slug_tr": "ch16_code_reviewde_seniorlari_etkilemek",
            "slug_en": "ch16_impressing_seniors_in_code_reviews",
            "title_tr": "Code Review'de Senior'ları Etkilemek: Kendi Kodunun Şeytanının Avukatı Ol",
            "title_en": "Pre-flight Code Reviews: Be Your Own Devil's Advocate with AI",
            "subtitle_tr": "PR'ı Ekibe Göndermeden Önce AI ile Sanal Code Review Simülasyonu",
            "subtitle_en": "Simulating a Ruthless Senior Code Review Before Teammates Ever See Your Diff",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Kendi kodunuzu PR olarak açmadan önce yapay zekaya 'Beni acımasızca eleştir' dediğinizde yakaladığınız hatalar, kariyerinizi nasıl hızlandırır?",
            "podcast_hook_en": "How does running an adversarial 'roast my PR diff' AI pre-flight review transform a junior developer's reputation among senior colleagues?",
            "takeaways_tr": [
                "En iyi mühendisler kodlarını başkası incelemeden önce kendi kendilerine en sert eleştiriyi yapanlardır.",
                "PR açmadan önce AI'a 'Kıdemli Güvenlik Mimarı' rolü vererek diff'i inceletmek basit hataları eler.",
                "Code Review yorumlarına kişisel bir saldırı gibi değil; ücretsiz bir mentorluk fırsatı gibi yaklaşın."
            ],
            "takeaways_en": [
                "Exceptional engineers audit their own diffs adversarially before requesting human peer review.",
                "Running a pre-flight prompt cast as a 'Ruthless Security & Performance Lead' catches low-hanging bugs instantly.",
                "Treat code review feedback not as personal criticism, but as high-leverage professional mentorship."
            ],
            "story_tr": """Uzaya roket fırlatan bir NASA ekibini düşünün. Mühendisler roketi fırlatma rampasına koyup *"Hadi fırlatalım, bakalım havada ne olacak"* der mi?

Asla! Fırlatmadan önce 'Kırmızı Takım' (Red Team) adı verilen bir grup uzman gelir. Görevleri roketi kırmak, patlatmak ve en küçük zayıflığı bulmaktır. Bu testleri geçen roket güvenle uçar.

Yazılımda da Pull Request açmadan önce kendi 'Kırmızı Takım'ınızı kurabilirsiniz. Yapay zekaya: *"Sen şirketin en huysuz, en titiz kıdemli mimarısın. Bu koddaki tüm açıkları bul"* dediğinizde, gerçek code review'e çıktığınızda senior'lar kodunuzun mükemmelliğine hayran kalır.""",
            "story_en": """Consider an aerospace engineering squad preparing a launch. Do they roll the booster onto the pad and say: *"Let's light the engines and see what happens in the stratosphere"?*

Never. A dedicated 'Red Team' subjects every valve and heat shield to grueling stress simulations, intentionally trying to cause a failure.

In software engineering, you can deploy your own private Red Team before requesting peer review. Prompt an LLM: *"Act as an uncompromising Staff Architect; expose every performance flaw and memory leak in this diff."* By the time human reviewers inspect your code, it is already hardened.""",
            "mental_tr": """Pre-Flight (Uçuş Öncesi) Code Review Döngüsü:

```
[Yerel Kod Değişiklikleri]
            │
            ▼
[Adım 1: git diff Çıktısını Al]
            │
            ▼
[Adım 2: AI'a "Kıdemli Mimar Gözüyle İncele" Promptu Gönder]
            │
            ├── "Burada bellek sızıntısı var mı?"
            ├── "SQL Injection veya tip kaçağı var mı?"
            └── "İsimlendirmeler temiz kod standartlarına uyuyor mu?"
            │
            ▼
[Adım 3: Düzeltmeleri Yap & Testleri Çalıştır]
            │
            ▼
[Adım 4: Kusursuz PR'ı Takıma Sun]
```""",
            "mental_en": """The Pre-Flight Code Review Protocol:

```
[Local Feature Complete]
            │
            ▼
[Step 1: Extract `git diff`]
            │
            ▼
[Step 2: Subject Diff to Adversarial AI Audit]
            │
            ├── "Identify potential race conditions or unhandled rejections"
            ├── "Detect memory leaks or unindexed database queries"
            └── "Audit naming conventions against clean architecture"
            │
            ▼
[Step 3: Refactor Findings & Verify Tests Pass]
            │
            ▼
[Step 4: Publish Bulletproof Pull Request]
```""",
            "prompt_tr": """# ROL: Titiz ve Huysuz Kıdemli Yazılım Mimarı
Ben ekibinde çalışan bir junior mühendisim. Aşağıda hazırladığım Pull Request diff'i yer alıyor.

## GÖREV:
Bana kibar davranma; koddaki teknik eksiklikleri acımasızca ortaya çıkar:
1. Hangi sınır durum (edge case) gözden kaçmış?
2. Performans veya bellek tüketimi açısından nerede patlayabilir?
3. Kod okunabilirliği ve SOLID prensipleri açısından hangi 2 kritik eleştirin var?

## DIFF İÇERİĞİ:
```typescript
export async function updateUserEmail(userId: string, newEmail: string) {
  const user = await db.user.findUnique({ where: { id: userId } });
  user.email = newEmail;
  await db.user.update({ where: { id: userId }, data: { email: newEmail } });
  await sendVerificationEmail(newEmail);
  return { success: true };
}
```""",
            "prompt_en": """# ROLE: Uncompromising Staff Architect
I am a junior engineer preparing a Pull Request.

## TASK:
Do not sugarcoat feedback. Conduct a rigorous, critical code review:
1. Which edge cases or concurrency hazards were overlooked?
2. Are there transaction boundary issues or side-effect ordering flaws?
3. What 2 high-priority clean architecture refactors do you demand?

## CODE DIFF:
```typescript
export async function updateUserEmail(userId: string, newEmail: string) {
  const user = await db.user.findUnique({ where: { id: userId } });
  user.email = newEmail;
  await db.user.update({ where: { id: userId }, data: { email: newEmail } });
  await sendVerificationEmail(newEmail);
  return { success: true };
}
```""",
            "code_lang": "typescript",
            "code_naive": """// Pre-Flight Öncesi: E-posta formatı kontrol edilmemiş, mükerrer kontrolü yok, transaction yok!
export async function updateUserEmailNaive(userId: string, newEmail: string) {
  // Eğer newEmail başka bir kullanıcıda zaten varsa veritabanı çöker!
  // Eğer e-posta servisi hata verirse DB güncellenmiş kalır (inconsistent state)!
  return await db.user.update({ where: { id: userId }, data: { email: newEmail } });
}""",
            "code_robust": """import { z } from "zod";

const EmailSchema = z.string().email("Geçersiz e-posta formatı").toLowerCase();

export async function updateUserEmailRobust(userId: string, rawEmail: string) {
  // 1. Giriş Doğrulaması
  const validatedEmail = EmailSchema.parse(rawEmail);

  // 2. İşlem bütünlüğü (Database Transaction)
  return await db.$transaction(async (tx) => {
    // Çakışma kontrolü
    const existing = await tx.user.findUnique({ where: { email: validatedEmail } });
    if (existing && existing.id !== userId) {
      throw new ConflictError("Bu e-posta adresi başka bir hesap tarafından kullanılıyor.");
    }

    const updatedUser = await tx.user.update({
      where: { id: userId },
      data: { email: validatedEmail, emailVerified: false }
    });

    // 3. Yan etki (Outbox deseni veya güvenli e-posta kuyruğu)
    await emailQueue.add("send-verification", { userId, email: validatedEmail });

    return { success: true, user: updatedUser };
  });
}""",
            "code_notes_tr": "Sanal review sonrasında: E-posta normalizasyonu (lowercase), mükerrer kayıt kontrolü, `db.$transaction` ile veri tutarlılığı ve doğrudan API çağırmak yerine kuyruk (queue) kullanımı eklenmiştir.",
            "code_notes_en": "The pre-flight audit caught missing validation, collision bugs, and non-atomic mutations. The hardened version wraps database operations in a transaction and offloads notifications to an asynchronous queue.",
            "pitfalls_tr": [
                {"trap": "Code review'de gelen eleştirilere savunmaya geçip kırılmak.", "solution": "Eleştirilen siz değilsiniz, koddur. Her yorumu öğrenme fırsatı olarak görün."},
                {"trap": "AI pre-flight review yapmadan doğrudan PR açıp basit hatalarla senior'ın vaktini almak.", "solution": "Her PR öncesi en az 1 kez AI'a diff kontrolü yaptırın."},
                {"trap": "Review yorumunu uygulayıp testleri tekrar çalıştırmadan push etmek.", "solution": "Her review revizyonundan sonra tüm test paketini yeniden çalıştırın."}
            ],
            "pitfalls_en": [
                {"trap": "Reacting defensively to constructive code review feedback.", "solution": "Separate your ego from your code; critiques target syntax and architecture, not identity."},
                {"trap": "Wasting senior engineer review cycles on typos caught by basic linters.", "solution": "Run pre-flight audits and linters before notifying human reviewers."},
                {"trap": "Pushing review revisions without re-running local test suites.", "solution": "Always re-execute your complete test suite before updating your PR branch."}
            ],
            "udemy_title_tr": "Ders 16: Code Review Başarısı - Kendi Kodunun Şeytanının Avukatı Olmak",
            "udemy_title_en": "Lecture 16: Code Review Mastery - Adversarial Self-Auditing with AI",
            "udemy_slides_tr": [
                "Neden en iyi mühendisler kendi kodlarını acımasızca eleştirir?",
                "Pre-Flight Check: AI ile Sanal Kıdemli Mimar Simülasyonu.",
                "Review yorumlarına profesyonel yanıt verme sanatı.",
                "Veri tutarlılığı: Database Transaction ve Hata Sınırları."
            ],
            "udemy_slides_en": [
                "Why top-tier engineers audit their own diffs before peer review.",
                "The Pre-Flight Check: Simulating a staff architect via AI.",
                "Professional etiquette: Responding to review comments constructively.",
                "Atomic data consistency: Database transactions and error boundaries."
            ],
            "udemy_demo_tr": "Basit bir veritabanı güncelleme fonksiyonunu AI'a verin. 'Bu koddaki race condition ve transaction açıklarını bul' deyin. AI'ın sunduğu eleştirileri inceleyip kodu refactor edin.",
            "udemy_demo_en": "Submit an unhardened database update function to an AI prompt. Command it to expose race conditions and unhandled error cases. Review the findings and apply transaction wrappers live.",
            "action_task_tr": "Bugün yazacağınız bir kodu GitHub'a push etmeden önce AI'a 'Sen bir güvenlik müfettişisin, bu diff'i eleştir' diyerek taratın ve bulduğu en az 1 noktayı düzeltin.",
            "action_task_en": "Before your next Git push, run your staged diff through an AI 'Staff Security Engineer' prompt and address the top finding.",
            "quiz_tr": [
                {
                    "question": "Bir veritabanı işleminde birden fazla ilişkili adımın ya hep ya hiç (atomik) olarak çalışmasını garanti eden mekanizma nedir?",
                    "options": [
                        "A) CSS Flexbox",
                        "B) Database Transaction ($transaction)",
                        "C) setTimeout fonksiyonu",
                        "D) console.warn"
                    ],
                    "answer": "B",
                    "explanation": "Veritabanı işlemleri (Transaction), içindeki adımlardan biri başarısız olduğunda tüm değişiklikleri geri alarak (rollback) veri tutarsızlığını önler."
                },
                {
                    "question": "Code Review sürecinde gelen teknik bir eleştiriye profesyonel bir junior mühendis nasıl yaklaşmalıdır?",
                    "options": [
                        "A) Eleştiriyi kişisel bir hakaret sayıp PR'ı silmelidir",
                        "B) Eleştirinin arkasındaki mimari nedeni anlamaya çalışıp yapıcı şekilde tartışmalı veya kodu iyileştirmelidir",
                        "C) Yorum yapan senior'ı şikayet etmelidir",
                        "D) Yorumları görmezden gelip PR'ı doğrudan merge etmelidir"
                    ],
                    "answer": "B",
                    "explanation": "Code Review, yazılım mühendisliğinde en hızlı öğrenme ve mentorluk kanalıdır; yapıcı yaklaşım profesyonelliğin temelidir."
                }
            ],
            "quiz_en": [
                {
                    "question": "Which database mechanism guarantees that a sequence of interdependent writes succeeds atomically or reverts entirely?",
                    "options": [
                        "A) CSS Grid layouts",
                        "B) Database Transactions (`BEGIN ... COMMIT / ROLLBACK`)",
                        "C) `setTimeout` timers",
                        "D) `console.warn` telemetry"
                    ],
                    "answer": "B",
                    "explanation": "Transactions enforce ACID atomicity, rolling back all intermediate mutations if any step in the sequence fails."
                },
                {
                    "question": "How should an engineer professionally respond to architectural critiques on their Pull Request?",
                    "options": [
                        "A) Conclude the feedback is personal hostility and delete the branch",
                        "B) Discern the architectural principle behind the critique and discuss trade-offs or apply the refactor",
                        "C) Escalate complaints to HR",
                        "D) Bypass branch protection rules and merge unilaterally"
                    ],
                    "answer": "B",
                    "explanation": "Peer review is collaborative engineering. Exploring the rationale behind critiques accelerates professional mastery."
                }
            ]
        },

        # Chapter 17
        {
            "id": 17,
            "section_id": 3,
            "slug_tr": "ch17_github_actions_ve_otomasyon_ci_cd",
            "slug_en": "ch17_github_actions_automated_ci_cd_pipelines",
            "title_tr": "GitHub Actions ve Otomasyon: AI Destekli CI/CD Boru Hatları",
            "title_en": "GitHub Actions & Automated AI Quality Gates: Building CI/CD Pipelines",
            "subtitle_tr": "Her Push'ta Otomatik Test, Lint ve AI Kod Kalitesi Denetimi",
            "subtitle_en": "Automating Test Suites, Linter Validation, and AI Code Gates on Every Push",
            "level_tr": "Orta / İleri Seviye",
            "level_en": "Intermediate / Advanced",
            "read_time_tr": "13 dk",
            "read_time_en": "13 min",
            "podcast_hook_tr": "Şirketler neden 'benim makinemde çalışıyor' sözüne güvenmez ve GitHub Actions gibi CI/CD sistemleri insan denetiminin yerini nasıl alır?",
            "podcast_hook_en": "Why does enterprise engineering reject 'it works on my machine' claims, and how does GitHub Actions enforce objective automated quality gates?",
            "takeaways_tr": [
                "CI/CD (Continuous Integration / Continuous Delivery), kodun her commit'te izole bir sunucuda otomatik test edilmesidir.",
                "Eğer testler CI ortamında geçmiyorsa, o kod 'çalışmıyor' kabul edilir; mazeret geçerli değildir.",
                "GitHub Actions YAML dosyalarını yapay zekaya yazdırmak, karmaşık pipeline kurulumlarını saatlerden dakikalara indirir."
            ],
            "takeaways_en": [
                "CI/CD guarantees that every incremental commit is validated in a clean, ephemeral sandbox environment.",
                "If an automated pipeline fails in CI, the code is considered broken regardless of local execution claims.",
                "Leveraging AI to author GitHub Actions workflow YAMLs cuts deployment pipeline setup from days to minutes."
            ],
            "story_tr": """Bir otomobil fabrikasındaki montaj hattını düşünün.

Her araba hattan çıkmadan önce otomatik bir test istasyonuna girer: Robot kollar kapıları 1000 kez çarpar, su fıskiyeleri su sızdırmazlığını kontrol eder, bilgisayarlar fren hidroliğini ölçer. Eğer araç bu testlerin tek birinden bile kalırsa hattan dışarı çıkarılamaz.

GitHub Actions işte o otomatik test robotudur! 

Siz kodunuzu GitHub'a gönderdiğiniz anda, bulutta tertemiz sanal bir sunucu (Ubuntu) açılır. Projenizi kurar, linter'ı çalıştırır, tüm testleri koşar ve derler. Eğer her şey yeşil yanarsa kodunuz birleşmeye hak kazanır.""",
            "story_en": """Visit a high-precision automotive assembly plant.

Before any vehicle rolls off the line, it enters an automated stress chamber: robotic arms slam doors 1,000 times, high-pressure water nozzles test window seals, and telemetry sensors audit braking dynamics. A single failing metric halts the vehicle immediately.

GitHub Actions is that automated testing chamber for software engineering.

The instant you push a branch, an ephemeral Linux container spins up in the cloud. It installs dependencies, verifies formatting, executes unit test suites, and validates builds. Only green runs earn merge eligibility.""",
            "mental_tr": """CI/CD Boru Hattı Akışı:

```
[git push origin feat/yeni-ozellik]
               │
               ▼
[GitHub Actions Runner (Ubuntu)]
               │
       ┌───────┴───────┐
       ▼               ▼
[Adım 1: Lint]  [Adım 2: Type Check]
(eslint/prettier)  (tsc --noEmit)
       │               │
       └───────┬───────┘
               ▼
[Adım 3: Unit & Integration Testler] (npm test)
               │
               ▼
[Adım 4: Build / Derleme] (npm run build)
               │
       ┌───────┴───────┐
       ▼               ▼
[BAŞARILI: Yeşil Tik] [BAŞARISIZ: Kırmızı Çarpı]
(Merge edilebilir)     (PR bloke edilir)
```""",
            "mental_en": """The CI Quality Pipeline Architecture:

```
[git push origin feat/new-feature]
               │
               ▼
[Ephemeral GitHub Runner (Ubuntu Latest)]
               │
       ┌───────┴───────┐
       ▼               ▼
[Job 1: Linter]   [Job 2: Type Check]
(eslint/prettier)   (tsc --noEmit)
       │               │
       └───────┬───────┘
               ▼
[Job 3: Automated Test Runner] (npm test)
               │
               ▼
[Job 4: Production Artifact Build] (npm run build)
               │
       ┌───────┴───────┐
       ▼               ▼
[SUCCESS: Green Check]  [FAILURE: Red Check]
(Merge permitted)       (PR automatically blocked)
```""",
            "prompt_tr": """# ROL: DevOps ve CI/CD Mühendisi
Next.js ve TypeScript kullanan bir projemiz var.

## GÖREV:
GitHub Actions için `.github/workflows/ci.yml` dosyasını hazırla.
Boru hattı şu gereksinimleri karşılamalıdır:
1. `main` ve `develop` branch'lerine açılan PR'larda ve push'larda otomatik tetiklensin.
2. Node.js 20 sürümünü kullansın ve `npm ci` ile bağımlılıkları önbelleklesin (cache).
3. Sırasıyla şu adımları çalıştırsın:
   - Lint kontrolü (`npm run lint`)
   - TypeScript derleme kontrolü (`npx tsc --noEmit`)
   - Testler (`npm test`)
4. Herhangi bir adım çökerse pipeline anında dursun.""",
            "prompt_en": """# ROLE: DevOps & Automation Engineer
We have a modern Next.js / TypeScript repository.

## TASK:
Author a production-grade `.github/workflows/ci.yml` workflow.
Requirements:
1. Trigger on pushes and pull requests targeting `main` and `develop`.
2. Target Node.js LTS (v20) and cache `~/.npm` dependencies via `actions/setup-node`.
3. Sequentially execute:
   - Static analysis (`npm run lint`)
   - Type verification (`npx tsc --noEmit`)
   - Test execution (`npm test -- --coverage`)
4. Fail fast upon any job error.""",
            "code_lang": "yaml",
            "code_naive": """# Kötü CI Dosyası: Önbellekleme yok, sürüm belirtilmemiş, testleri atlıyor
name: CI
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: npm install # npm ci yerine install kullanmak lockfile'ı bozar!
      - run: npm run build""",
            "code_robust": """name: Continuous Integration (CI)

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  quality-gate:
    name: Lint, Typecheck & Tests
    runs-on: ubuntu-latest

    steps:
      - name: 📥 Depoyu Klonla
        uses: actions/checkout@v4

      - name: 🟢 Node.js Kurulumu & Önbellek
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - name: 📦 Bağımlılıkları Kur (Deterministic)
        run: npm ci

      - name: 🔍 Linter & Format Kontrolü
        run: npm run lint

      - name: 🛡️ TypeScript Tip Kontrolü
        run: npx tsc --noEmit

      - name: 🧪 Unit Testleri Çalıştır
        run: npm test -- --ci --maxWorkers=2

      - name: 🏗️ Production Build Doğrulaması
        run: npm run build""",
            "code_notes_tr": "`npm ci` kullanılarak `package-lock.json` ile birebir uyumlu kurulum sağlanmış, `concurrency` bloğu ile aynı branch'e yeni push geldiğinde eski gereksiz CI koşuları otomatik iptal edilerek fatura maliyeti düşürülmüştür.",
            "code_notes_en": "Using `npm ci` guarantees deterministic dependency resolution matching `package-lock.json`. The `concurrency` block cancels redundant in-flight runs when new commits are pushed, conserving CI minutes.",
            "pitfalls_tr": [
                {"trap": "CI ortamında `npm install` kullanmak.", "solution": "CI sunucularında her zaman deterministik olan `npm ci` komutunu kullanın."},
                {"trap": "CI kırmızı yanarken 'nasılsa yerelde çalışıyor' deyip PR'ı zorla merge etmek.", "solution": "CI kırmızıysa kod bozuktur; hatayı CI loglarından okuyup düzeltin."},
                {"trap": "Secret (API anahtarları) bilgilerini CI yaml dosyasına düz metin yazmak.", "solution": "Hassas bilgileri her zaman GitHub Secrets (`${{ secrets.API_KEY }}`) üzerinden çekin."}
            ],
            "pitfalls_en": [
                {"trap": "Invoking `npm install` instead of `npm ci` in automation scripts.", "solution": "Always use `npm ci` in headless environments to enforce exact lockfile state."},
                {"trap": "Bypassing branch protection rules to merge while CI checks are failing.", "solution": "A red pipeline is a hard stop; diagnose failure logs in the Actions tab."},
                {"trap": "Hardcoding API secrets in workflow YAML configurations.", "solution": "Reference credentials exclusively via GitHub Encrypted Secrets (`${{ secrets.TOKEN }}`)."}
            ],
            "udemy_title_tr": "Ders 17: GitHub Actions ile CI/CD - Kalite Kapılarını Kurmak",
            "udemy_title_en": "Lecture 17: GitHub Actions CI/CD - Enforcing Automated Quality Gates",
            "udemy_slides_tr": [
                "CI/CD nedir ve şirketler için neden hayati önem taşır?",
                "GitHub Actions anatomisi: Workflow, Event, Job, Step.",
                "Deterministik kurulum: npm install vs npm ci.",
                "Canlı Demo: Sıfırdan GitHub Actions CI pipeline kurmak."
            ],
            "udemy_slides_en": [
                "What is CI/CD and why does continuous integration de-risk delivery?",
                "Anatomy of GitHub Actions: Workflows, Triggers, Jobs, and Steps.",
                "Deterministic builds: `npm install` vs `npm ci` explained.",
                "Live demo: Crafting an end-to-end CI pipeline from scratch."
            ],
            "udemy_demo_tr": "Reponuzda `.github/workflows/ci.yml` oluşturun. Kasıtlı olarak bir TypeScript tip hatası yapıp push edin. GitHub Actions sekmesinde build'in kırmızıya düştüğünü ve PR'ın kilitlendiğini gösterin. Hatayı düzeltip yeşil tiki alın.",
            "udemy_demo_en": "Author `.github/workflows/ci.yml`. Push a deliberate TypeScript error. Watch the Actions tab trip and block merge eligibility. Fix the type error, re-push, and demonstrate the green checkmark.",
            "action_task_tr": "Kişisel bir GitHub projenizde `.github/workflows/ci.yml` oluşturun ve testleri her push'ta otomatik çalıştıracak şekilde yapılandırın.",
            "action_task_en": "Set up a working GitHub Actions workflow in a personal repository that lints and runs tests on pull requests.",
            "quiz_tr": [
                {
                    "question": "CI sunucularında `npm install` yerine `npm ci` kullanılmasının temel sebebi nedir?",
                    "options": [
                        "A) `npm ci` komutunun daha renkli çıktılar vermesi",
                        "B) `package-lock.json` dosyasını değiştirmeden, kilitli sürümleri birebir ve temiz kurarak determinizm sağlaması",
                        "C) Sadece Mac bilgisayarlarda çalışması",
                        "D) İnternet bağlantısı gerektirmemesi"
                    ],
                    "answer": "B",
                    "explanation": "`npm ci` mevcut lockfile'ı asla değiştirmez ve sıfırdan temiz bir kurulum yaparak beklenmedik sürüm uyuşmazlıklarını önler."
                },
                {
                    "question": "GitHub Actions'ta `concurrency: cancel-in-progress: true` ayarının sağladığı fayda nedir?",
                    "options": [
                        "A) Bilgisayarı kapatması",
                        "B) Aynı branch'e yeni bir commit geldiğinde eski ve artık gereksiz olan çalışan CI işini otomatik iptal ederek sunucu süresi tasarrufu sağlaması",
                        "C) Kodları otomatik silmesi",
                        "D) Testleri yapmadan geçmesi"
                    ],
                    "answer": "B",
                    "explanation": "Geliştirici arka arkaya commit attığında önceki eski test koşularını iptal etmek hem kaynak tasarrufu sağlar hem de CI kuyruklarını rahatlatır."
                }
            ],
            "quiz_en": [
                {
                    "question": "Why is `npm ci` strictly mandated over `npm install` in CI/CD automation?",
                    "options": [
                        "A) It prints vibrant ANSI terminal colors",
                        "B) It installs exact lockfile dependencies deterministically without modifying `package-lock.json`",
                        "C) It executes exclusively on macOS hosts",
                        "D) It functions completely offline"
                    ],
                    "answer": "B",
                    "explanation": "`npm ci` guarantees deterministic, reproducible installations by adhering strictly to `package-lock.json`."
                },
                {
                    "question": "What is the operational purpose of `concurrency: cancel-in-progress: true` in GitHub Workflows?",
                    "options": [
                        "A) Powering down runner nodes",
                        "B) Automatically terminating stale in-flight CI runs when a fresh commit is pushed to the same branch",
                        "C) Purging source code from storage",
                        "D) Skipping unit assertions"
                    ],
                    "answer": "B",
                    "explanation": "Canceling superseded runs conserves billable runner minutes and keeps build queues clear."
                }
            ]
        },

        # Chapter 18
        {
            "id": 18,
            "section_id": 3,
            "slug_tr": "ch18_koddan_canli_dokumantasyon_uretmek",
            "slug_en": "ch18_living_documentation_from_codebases",
            "title_tr": "Dokümantasyon Artık Yük Değil: Koddan Canlı Dokümantasyon Üretmek",
            "title_en": "Living Documentation: Generating Real-Time Docs from Code with AI",
            "subtitle_tr": "Eski ve Güncelliğini Yitirmiş Wiki Sayfalarına Son Verme Rehberi",
            "subtitle_en": "Eradicating Stale Confluence Wikis via Code-First Markdown Automation",
            "level_tr": "Orta Seviye",
            "level_en": "Intermediate",
            "read_time_tr": "12 dk",
            "read_time_en": "12 min",
            "podcast_hook_tr": "Geliştiriciler neden dokümantasyon yazmaktan nefret eder ve AI ile dokümantasyonu kodun doğal bir yan ürünü haline nasıl getirebiliriz?",
            "podcast_hook_en": "Why do software engineers notoriously despise authoring documentation, and how can AI transform documentation into a live byproduct of code?",
            "takeaways_tr": [
                "Güncellenmeyen dokümantasyon, hiç yazılmamış dokümantasyondan daha tehlikelidir çünkü yanlış yönlendirir.",
                "En iyi dokümantasyon kodun hemen yanında yaşayan dokümantasyondur (JSDoc, TypeDoc, OpenAPI/Swagger).",
                "AI araçları, TypeScript tiplerini ve API endpoint'lerini okuyarak Markdown belgelerini ve API referanslarını anında güncelleyebilir."
            ],
            "takeaways_en": [
                "Outdated documentation is more toxic than no documentation because it actively deceives engineers.",
                "The most resilient documentation lives directly alongside the code (JSDoc, TypeDoc, OpenAPI / Swagger schemas).",
                "Modern AI tools digest types and routes to generate synchronized Markdown specs and API catalogs automatically."
            ],
            "story_tr": """Tarihi bir kaleye girdiğinizi ve elinizde 1850 yılından kalma bir harita olduğunu düşünün. Haritada *"Burada gizli bir altın odası var"* yazıyor; gidiyorsunuz ama orada derin bir uçurum var! Harita güncellenmediği için hayatınızı kaybedebilirsiniz.

Yazılım şirketlerindeki eski Confluence sayfaları ve unutulmuş Word dosyaları tam olarak o 1850 yılı haritasıdır. Kod değişir, mimari gelişir ama doküman 2 yıl önceki haliyle kalır.

Modern mühendislikte çözüm **Canlı Dokümantasyon (Living Documentation)** yaklaşımıdır:
Dokümantasyon kodun içine yazılır (JSDoc ve Şemalar). Yapay zeka bu şemaları okuyup saniyeler içinde güncel web sitelerine ve markdown sayfalarına dönüştürür.""",
            "story_en": """Imagine exploring an ancient fortress holding a hand-drawn map from 1850. The map marks a treasury room; you step through the threshold and plunge into a deep collapsed dungeon pit. The outdated map deceived you.

Corporate wiki portals and abandoned Word docs are that exact misleading 1850 map. The codebase moves at lightning speed, while the documentation gathers digital dust.

The modern paradigm is **Living Documentation**:
Document truth directly in code via JSDoc, Docstrings, and Type contracts. AI engines then compile these authoritative sources into synchronized Markdown portals automatically.""",
            "mental_tr": """Koddan Dokümantasyona Otomasyon Piramidi:

```
[Tip ve Fonksiyon Açıklamaları (JSDoc / TypeDoc)]
                    │
                    ▼
[Otomatik Şema Çıkarımı (OpenAPI / Swagger / Zod)]
                    │
                    ▼
[AI İle Zenginleştirme: Kullanım Örnekleri & Senaryolar]
                    │
                    ▼
[Canlı Dokümantasyon Sitesi (Mintlify / Docusaurus / README.md)]
```""",
            "mental_en": """The Living Documentation Pipeline:

```
[In-Code Annotations (TSDoc / Docstrings / JSDoc)]
                    │
                    ▼
[Deterministic Contract Schemas (OpenAPI / Zod / Swagger)]
                    │
                    ▼
[AI Contextual Enrichment: Edge-Case Samples & Guides]
                    │
                    ▼
[Living Documentation Portal (Mintlify / Starlight / README.md)]
```""",
            "prompt_tr": """# ROL: Teknik Yazar ve API Mimarı
Aşağıdaki TypeScript servis fonksiyonunu incele.

## KOD:
```typescript
export async function calculateShippingCost(
  weightKg: number, 
  destinationZone: 'LOCAL' | 'NATIONAL' | 'INTERNATIONAL',
  isExpress: boolean = false
): Promise<number> {
  // Mantık...
}
```

## GÖREV:
Bu fonksiyon için:
1. Standartlara tam uyumlu TSDoc / JSDoc bloğu oluştur (@param, @returns, @throws).
2. Bir junior geliştiricinin kolayca anlayacağı pratik bir kullanım örneği (code example) ekle.
3. API dokümantasyonu için bir Markdown tablosu ve açıklama paragrafı hazırla.""",
            "prompt_en": """# ROLE: Technical Documentation & Developer Experience Architect
Review this TypeScript service method:

## CODE:
```typescript
export async function calculateShippingCost(
  weightKg: number, 
  destinationZone: 'LOCAL' | 'NATIONAL' | 'INTERNATIONAL',
  isExpress: boolean = false
): Promise<number> {
  // Implementation...
}
```

## TASK:
Produce:
1. Fully compliant TSDoc / JSDoc documentation (`@param`, `@returns`, `@throws`).
2. A realistic code integration example.
3. A Markdown API specification section suitable for a developer docs portal.""",
            "code_lang": "typescript",
            "code_naive": """// Kötü Dokümantasyon: Ne parametrelerin anlamı belli ne de olası hatalar
// Kargo hesaplar
export function calc(w: number, z: string, e: boolean) {
  // ...
}""",
            "code_robust": """/**
 * Bir siparişin ağırlığına ve teslimat bölgesine göre kargo ücretini hesaplar.
 *
 * @remarks
 * Uluslararası kargolarda ekspres seçeneği ekstra gümrük işlem ücreti içerir.
 *
 * @param weightKg - Paketin kilogram cinsinden ağırlığı (0.01 - 100.0 arası).
 * @param destinationZone - Teslimat bölgesi ('LOCAL', 'NATIONAL', 'INTERNATIONAL').
 * @param isExpress - Hızlı teslimat seçeneği (Varsayılan: false).
 *
 * @returns KDV dahil toplam kargo tutarı (TRY cinsinden).
 *
 * @throws {RangeError} Ağırlık 0 veya negatifse ya da 100 kg'dan büyükse.
 *
 * @example
 * ```typescript
 * const cost = await calculateShippingCost(2.5, 'NATIONAL', true);
 * console.log(`Ödenecek tutar: ${cost} TL`);
 * ```
 */
export async function calculateShippingCost(
  weightKg: number,
  destinationZone: 'LOCAL' | 'NATIONAL' | 'INTERNATIONAL',
  isExpress: boolean = false
): Promise<number> {
  if (weightKg <= 0 || weightKg > 100) {
    throw new RangeError("Paket ağırlığı 0 ile 100 kg arasında olmalıdır.");
  }
  // Hesaplama implementasyonu...
  return 150.0;
}""",
            "code_notes_tr": "TSDoc formatında yazılan bu açıklamalar hem IDE içinde fareyle üzerine gelindiğinde zengin ipucu (IntelliSense) olarak görünür, hem de TypeDoc gibi araçlarla tek komutta HTML dokümantasyonuna dönüştürülebilir.",
            "code_notes_en": "TSDoc-compliant documentation renders directly inside IDE hover tooltips (IntelliSense) and compiles into automated web documentation portals with zero manual synchronization.",
            "pitfalls_tr": [
                {"trap": "Dokümantasyonu Confluence veya Word dosyalarında tutup koddan koparmak.", "solution": "Dokümantasyonu daima kodun içinde (TSDoc) veya aynı repoda markdown dosyalarında tutun."},
                {"trap": "Kodun ne yaptığını bariz şekilde tekrarlayan anlamsız yorumlar yazmak (Örn: `i++; // i'yi bir artır`).", "solution": "Yorumlarda 'ne' yapıldığını değil, 'neden' yapıldığını ve iş kuralı gerekçelerini açıklayın."},
                {"trap": "API değişikliklerinde dokümantasyonu güncellemeyi unutmak.", "solution": "Zod veya OpenAPI şemalarını kullanarak dokümanı koddan otomatik türetin."}
            ],
            "pitfalls_en": [
                {"trap": "Stashing documentation in isolated external wikis disconnected from Git repos.", "solution": "Keep docs co-located inside the codebase as markdown or structured code docstrings."},
                {"trap": "Writing redundant comments stating the obvious (e.g., `count++; // increment count`).", "solution": "Document the architectural 'why', business invariants, and non-obvious constraints."},
                {"trap": "Forgetting to update documentation when adjusting API interfaces.", "solution": "Derive documentation deterministically from schemas using tools like Swagger or Zod-to-OpenAPI."}
            ],
            "udemy_title_tr": "Ders 18: Canlı Dokümantasyon - Koddan Otomatik Belge Üretmek",
            "udemy_title_en": "Lecture 18: Living Documentation - Generating Docs from Code with AI",
            "udemy_slides_tr": [
                "Neden geleneksel dokümantasyon ölmeye mahkumdur?",
                "Canlı Dokümantasyon (Living Docs) felsefesi.",
                "TSDoc, TypeDoc ve Mintlify ile otomatik dokümantasyon üretimi.",
                "Bölüm 3 Özeti: Takım İşbirliği, Git ve Otomasyonun Gücü."
            ],
            "udemy_slides_en": [
                "Why disconnected manual wiki documentation inevitably becomes stale.",
                "The Living Documentation philosophy.",
                "Automating docs with TSDoc, OpenAPI, and modern static site engines.",
                "Module 3 Recap: Collaborative Engineering, Git, and Quality Automation."
            ],
            "udemy_demo_tr": "Bir TypeScript fonksiyonuna JSDoc ekleyin. TypeDoc veya AI kullanarak bu fonksiyondan anında profesyonel bir `API_REFERENCE.md` sayfası üretin ve önizlemesini gösterin.",
            "udemy_demo_en": "Annotate a TypeScript service with TSDoc blocks. Execute a documentation generator or AI prompt to synthesize an `API_REFERENCE.md` catalog, demonstrating how changes in code instantly update docs.",
            "action_task_tr": "Projenizdeki en kritik 2 servis fonksiyonuna eksiksiz TSDoc açıklamaları (@param, @returns, @example) ekleyin.",
            "action_task_en": "Add comprehensive TSDoc or Docstring annotations (`@param`, `@returns`, `@example`) to two core service functions in your active project.",
            "quiz_tr": [
                {
                    "question": "Yazılım geliştirmede 'Canlı Dokümantasyon' (Living Documentation) kavramı neyi ifade eder?",
                    "options": [
                        "A) Dokümanın canlı yayında okunmasını",
                        "B) Dokümantasyonun doğrudan kodun içindeki tiplerden ve açıklamalardan otomatik olarak türetilerek her zaman güncel kalmasını",
                        "C) Sadece video şeklinde doküman hazırlanmasını",
                        "D) Dokümanın her gün elle yeniden yazılmasını"
                    ],
                    "answer": "B",
                    "explanation": "Canlı dokümantasyon, kod değiştikçe otomatik güncellenen; tek gerçeklik kaynağının (Single Source of Truth) kod olduğu yaklaşımdır."
                },
                {
                    "question": "TSDoc veya JSDoc bloklarında `@example` etiketinin temel amacı nedir?",
                    "options": [
                        "A) Fonksiyonu silmek",
                        "B) Diğer geliştiricilere fonksiyonun nasıl çağrılacağına dair çalışan, somut bir kod örneği sunmak",
                        "C) Sadece CSS renklerini tanımlamak",
                        "D) Bilgisayarı hızlandırmak"
                    ],
                    "answer": "B",
                    "explanation": "`@example` etiketi, geliştiricilerin API'yi nasıl kullanacağını hemen görmesini sağlayan en etkili dokümantasyon aracıdır."
                }
            ],
            "quiz_en": [
                {
                    "question": "What is the defining principle of 'Living Documentation' in software engineering?",
                    "options": [
                        "A) Broadcasting documentation over live streaming video",
                        "B) Deriving documentation deterministically from code contracts and schemas so it remains perpetually synchronized",
                        "C) Authoring documentation exclusively in video format",
                        "D) Re-typing wiki pages manually every 24 hours"
                    ],
                    "answer": "B",
                    "explanation": "Living documentation treats code and schemas as the single source of truth, generating documentation automatically upon change."
                },
                {
                    "question": "What is the architectural purpose of the `@example` tag in TSDoc/JSDoc blocks?",
                    "options": [
                        "A) Purging unused methods",
                        "B) Providing peer engineers with an immediate, copy-pasteable, valid usage demonstration",
                        "C) Setting CSS color tokens",
                        "D) Overclocking CPU execution"
                    ],
                    "answer": "B",
                    "explanation": "`@example` gives consumers instant clarity on expected calling conventions and argument formats."
                }
            ]
        }
    ]
