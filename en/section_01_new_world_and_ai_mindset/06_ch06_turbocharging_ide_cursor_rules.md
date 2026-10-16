# 6. Turbocharging Your IDE: Cursor Rules, Shortcuts & Workflows

**Stop Repeating Yourself: Systematize Your Workflow with Custom Rules**  
*Module 1 • Difficulty Level: Beginner Level • Estimated Reading Time: 13 min*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Briefing
> **Podcast Discussion Hook:**  
> *"Does introducing a repository `.cursorrules` or context config truly double daily engineering velocity, or is it just setup overhead?"*  
> 
> **3 Core Audio Takeaways:**  
> - 📌 Repository rules (`.cursorrules`) permanently anchor architectural standards into the AI's system prompt.
- 📌 Stop manually typing 'Use TypeScript, write tests, follow functional style' into every prompt; codify it.
- 📌 Mastering shortcuts (Cmd+K for inline edits, Cmd+L for chat, Cmd+I for multi-file composer) aligns coding speed with thinking speed.

---

## 📖 1. The Story & Real-World Analogy

Consider visiting your local coffee shop every morning. Is it productive to repeat: *"Hello, I would like an oat milk cortado with a single shot in a ceramic cup"* every single day? Or is it superior when the barista nods and hands you your cortado in 20 seconds?

System rule files (like `.cursorrules` or `.agents/rules`) serve as that barista.

Placing a concise rules file in your repository root constantly reminds the AI model about your conventions, linting rules, test frameworks, and architectural red lines without you typing a single extra character.

---

## 🧠 2. The AI Mental Model & Paradigm Shift

Anatomy of an Effective `.cursorrules` File:

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
```

---

## 🤖 3. AI Prompt Lab (Production-Ready Templates)

You can directly paste and adapt this prompt template in Cursor, Claude Code, ChatGPT, or Copilot:

```markdown
# TASK: Generate a Production-Grade .cursorrules Configuration
We are launching a modern backend service with:
- FastAPI (Python 3.12)
- Pydantic v2
- SQLAlchemy 2.0 (Async engine)
- PostgreSQL
- PyTest

Generate a concise, 5-pillar `.cursorrules` markdown file.
Focus on type safety, async/await correctness, and automated test generation.
```

---

## 💻 4. Code Walkthrough: Naive / Hallucination vs. Production-Grade

#### ❌ Naive / Unchecked AI Output (Risky):
```markdown
# Kötü .cursorrules: Çok uzun, laf kalabalığı dolu ve kural içermeyen metin
Sen harika bir yardımcısın. Benim için en iyi python kodlarını yaz.
Lütfen hata yapma ve her zaman nazik ol. Kodların çok temiz olsun.
```

#### ✅ Senior-Refined Version (Robust & Clean):
```markdown
# PROJE KURALLARI (.cursorrules)
## TEKNOLOJİ YIĞINI:
- Python 3.12, FastAPI, Pydantic v2, SQLAlchemy 2.0 (Async).

## KODLAMA STANDARTLARI:
1. TIP GÜVENLİĞİ: Tüm fonksiyonlarda type hints zorunludur. 'Any' yasaktır.
2. VERİTABANI: Asla senkron sorgu yazma; daima `await session.execute(...)` kullan.
3. MODELLER: Giriş/Çıkış için daima Pydantic şemalarını SQLAlchemy modellerinden ayır.
4. HATA YÖNETİMİ: HTTPException fırlatırken daima standart JSON hata yapısı kullan.
5. TESTLER: Her endpoint için en az 1 başarı ve 2 hata durumunu kapsayan pytest fonksiyonu yaz.
```

**💡 Code Analysis:**
High-impact rule files use imperative instructions, strict constraints, and explicit version designations. The model digests these as system instructions on every interaction.

---

## ⚠️ 5. Junior Pitfalls & Senior Perspective

- **Trap:** Dumping 500 lines of prose into rules, exhausting system tokens.
  - **Remedy:** Keep rules concise, actionable, and under 50 lines.
- **Trap:** Keeping rules local without committing to Git.
  - **Remedy:** Commit `.cursorrules` so the entire engineering team shares uniform AI output quality.
- **Trap:** Navigating entirely with mouse clicks rather than keyboard shortcuts.
  - **Remedy:** Practice modal shortcuts (Cmd+K, Cmd+L, Cmd+I) until they become muscle memory.

---

## 🎬 6. Udemy Video Lecture Blueprint & Slide Deck

### 🎥 Lecture Title: *Lecture 6: Supercharging Your IDE - Standardizing Output via .cursorrules*
- 🖥️ **Slide 1:** What is a rules file and how do IDEs inject it?
- 🖥️ **Slide 2:** Eliminating repetitive prompt boilerplate forever.
- 🖥️ **Slide 3:** Essential keyboard shortcuts for high-velocity coding.
- 🖥️ **Slide 4:** Module 1 Recap: The Mental Shift of the AI-Driven Engineer.

**Live Coding / Screencast Scenario:**  
Create a `.cursorrules` file in the repo root. Add a directive: 'Always generate JSDoc comments and strict TypeScript return types'. Prompt for a function and observe the rules take effect automatically.

---

## 🎯 7. Daily Action Task & Mini Quiz

### 🛠️ Daily Action Task:
Author a 20-line rules file in your active workspace specifying your runtime version, lint conventions, and testing library.

### 🧠 Chapter Review Quiz:

**Question 1:** What is the primary architectural purpose of a `.cursorrules` file?
  - A) Increasing hardware clock speeds
  - B) Automatically injecting repository standards and constraints into the model's system context
  - C) Purging Git commit history
  - D) Compressing CSS bundles
> **Correct Answer:** B
> **Explanation:** Rules files automate context delivery, eliminating the need to repeatedly paste guidelines into every prompt.

**Question 2:** Which keyboard shortcut opens the inline AI editing prompt in Cursor?
  - A) Ctrl + Alt + Delete
  - B) Cmd + K (or Ctrl + K on Windows/Linux)
  - C) F5
  - D) Shift + Escape
> **Correct Answer:** B
> **Explanation:** Cmd+K activates the inline edit interface directly in the editor buffer.

