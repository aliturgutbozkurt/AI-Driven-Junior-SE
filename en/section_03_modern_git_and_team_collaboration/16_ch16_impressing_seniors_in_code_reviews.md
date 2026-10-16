# 16. Pre-flight Code Reviews: Be Your Own Devil's Advocate with AI

**Simulating a Ruthless Senior Code Review Before Teammates Ever See Your Diff**  
*Module 3 • Difficulty Level: Intermediate • Estimated Reading Time: 12 min*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Briefing
> **Podcast Discussion Hook:**  
> *"How does running an adversarial 'roast my PR diff' AI pre-flight review transform a junior developer's reputation among senior colleagues?"*  
> 
> **3 Core Audio Takeaways:**  
> - 📌 Exceptional engineers audit their own diffs adversarially before requesting human peer review.
- 📌 Running a pre-flight prompt cast as a 'Ruthless Security & Performance Lead' catches low-hanging bugs instantly.
- 📌 Treat code review feedback not as personal criticism, but as high-leverage professional mentorship.

---

## 📖 1. The Story & Real-World Analogy

Consider an aerospace engineering squad preparing a launch. Do they roll the booster onto the pad and say: *"Let's light the engines and see what happens in the stratosphere"?*

Never. A dedicated 'Red Team' subjects every valve and heat shield to grueling stress simulations, intentionally trying to cause a failure.

In software engineering, you can deploy your own private Red Team before requesting peer review. Prompt an LLM: *"Act as an uncompromising Staff Architect; expose every performance flaw and memory leak in this diff."* By the time human reviewers inspect your code, it is already hardened.

---

## 🧠 2. The AI Mental Model & Paradigm Shift

The Pre-Flight Code Review Protocol:

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
```

---

## 🤖 3. AI Prompt Lab (Production-Ready Templates)

You can directly paste and adapt this prompt template in Cursor, Claude Code, ChatGPT, or Copilot:

```markdown
# ROLE: Uncompromising Staff Architect
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
```
```

---

## 💻 4. Code Walkthrough: Naive / Hallucination vs. Production-Grade

#### ❌ Naive / Unchecked AI Output (Risky):
```typescript
// Pre-Flight Öncesi: E-posta formatı kontrol edilmemiş, mükerrer kontrolü yok, transaction yok!
export async function updateUserEmailNaive(userId: string, newEmail: string) {
  // Eğer newEmail başka bir kullanıcıda zaten varsa veritabanı çöker!
  // Eğer e-posta servisi hata verirse DB güncellenmiş kalır (inconsistent state)!
  return await db.user.update({ where: { id: userId }, data: { email: newEmail } });
}
```

#### ✅ Senior-Refined Version (Robust & Clean):
```typescript
import { z } from "zod";

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
}
```

**💡 Code Analysis:**
The pre-flight audit caught missing validation, collision bugs, and non-atomic mutations. The hardened version wraps database operations in a transaction and offloads notifications to an asynchronous queue.

---

## ⚠️ 5. Junior Pitfalls & Senior Perspective

- **Trap:** Reacting defensively to constructive code review feedback.
  - **Remedy:** Separate your ego from your code; critiques target syntax and architecture, not identity.
- **Trap:** Wasting senior engineer review cycles on typos caught by basic linters.
  - **Remedy:** Run pre-flight audits and linters before notifying human reviewers.
- **Trap:** Pushing review revisions without re-running local test suites.
  - **Remedy:** Always re-execute your complete test suite before updating your PR branch.

---

## 🎬 6. Udemy Video Lecture Blueprint & Slide Deck

### 🎥 Lecture Title: *Lecture 16: Code Review Mastery - Adversarial Self-Auditing with AI*
- 🖥️ **Slide 1:** Why top-tier engineers audit their own diffs before peer review.
- 🖥️ **Slide 2:** The Pre-Flight Check: Simulating a staff architect via AI.
- 🖥️ **Slide 3:** Professional etiquette: Responding to review comments constructively.
- 🖥️ **Slide 4:** Atomic data consistency: Database transactions and error boundaries.

**Live Coding / Screencast Scenario:**  
Submit an unhardened database update function to an AI prompt. Command it to expose race conditions and unhandled error cases. Review the findings and apply transaction wrappers live.

---

## 🎯 7. Daily Action Task & Mini Quiz

### 🛠️ Daily Action Task:
Before your next Git push, run your staged diff through an AI 'Staff Security Engineer' prompt and address the top finding.

### 🧠 Chapter Review Quiz:

**Question 1:** Which database mechanism guarantees that a sequence of interdependent writes succeeds atomically or reverts entirely?
  - A) CSS Grid layouts
  - B) Database Transactions (`BEGIN ... COMMIT / ROLLBACK`)
  - C) `setTimeout` timers
  - D) `console.warn` telemetry
> **Correct Answer:** B
> **Explanation:** Transactions enforce ACID atomicity, rolling back all intermediate mutations if any step in the sequence fails.

**Question 2:** How should an engineer professionally respond to architectural critiques on their Pull Request?
  - A) Conclude the feedback is personal hostility and delete the branch
  - B) Discern the architectural principle behind the critique and discuss trade-offs or apply the refactor
  - C) Escalate complaints to HR
  - D) Bypass branch protection rules and merge unilaterally
> **Correct Answer:** B
> **Explanation:** Peer review is collaborative engineering. Exploring the rationale behind critiques accelerates professional mastery.

