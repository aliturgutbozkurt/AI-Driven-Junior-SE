# 32. Unit Testing Accelerated by AI: Jest, PyTest & Mocking Masters

**Mocking Databases and Network Calls to Run 1,000 Tests in 2 Seconds**  
*Module 6 • Difficulty Level: Intermediate • Estimated Reading Time: 12 min*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Briefing
> **Podcast Discussion Hook:**  
> *"Why is connecting to real production databases or live payment gateways during unit tests reckless, and how does mock virtualization make test runs lightning fast?"*  
> 
> **3 Core Audio Takeaways:**  
> - 📌 Unit assertions must remain strictly deterministic and decoupled from ambient side effects (network, disk, system clocks).
- 📌 Mocking substitutes real external collaborators (Stripe, PostgreSQL, SES) with predictable, controlled test doubles.
- 📌 AI tooling excels at generating comprehensive mock fixtures and boundary test suites on demand.

---

## 📖 1. The Story & Real-World Analogy

Consider a surgical resident in their first week of medical residency.

Does the chief surgeon hand them a scalpel and command: *"Proceed to perform open-heart surgery on this living patient in Room 4"?* Never. Residents practice on synthetic silicone mannequins and VR haptic simulators hundreds of times.

In software engineering, a **Mock** is that synthetic silicone mannequin.

If your automated unit test suite charges a live production Stripe card during every run, you will bankrupt the organization. By substituting live APIs with deterministic mock doubles, you verify business execution safely.

---

## 🧠 2. The AI Mental Model & Paradigm Shift

The Mock Isolation Boundary:

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
```

---

## 🤖 3. AI Prompt Lab (Production-Ready Templates)

You can directly paste and adapt this prompt template in Cursor, Claude Code, ChatGPT, or Copilot:

```markdown
# ROLE: Lead Test Architect & Jest Specialist
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
3. Assert that when an invoice is already marked paid, Stripe's charge API is never invoked (`expect(...).not.toHaveBeenCalled()`).
```

---

## 💻 4. Code Walkthrough: Naive / Hallucination vs. Production-Grade

#### ❌ Naive / Unchecked AI Output (Risky):
```typescript
// Kötü Test: Dış bağımlılıkları mocklamadan gerçek veritabanı beklemek
it("faturayı öder", async () => {
  // Eğer PostgreSQL sunucusu açık değilse test patlar!
  const res = await payInvoice("123", new RealStripe(), new RealDB());
  expect(res.success).toBe(true);
});
```

#### ✅ Senior-Refined Version (Robust & Clean):
```typescript
import { payInvoice } from "./paymentService";

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
});
```

**💡 Code Analysis:**
These tests execute with zero external network connectivity or database instances. A suite of 1,000 such tests runs in under 2 seconds, verifying edge-case business invariants deterministically.

---

## ⚠️ 5. Junior Pitfalls & Senior Perspective

- **Trap:** Failing to reset mocks between test cases, inducing state leakage and flaky runs.
  - **Remedy:** Call `beforeEach(() => jest.clearAllMocks())` to guarantee state hygiene.
- **Trap:** Testing the mock implementation rather than system-under-test logic.
  - **Remedy:** Mocks supply preconditions; assertions must validate domain behavior.
- **Trap:** Letting mock schemas drift out of sync with evolving external APIs (Stale Mocks).
  - **Remedy:** Enforce strict TypeScript interfaces on mock factories.

---

## 🎬 6. Udemy Video Lecture Blueprint & Slide Deck

### 🎥 Lecture Title: *Lecture 32: Accelerated Unit Testing - Mastering Jest, PyTest & Mocks*
- 🖥️ **Slide 1:** The determinism mandate: Isolating unit tests from ambient I/O.
- 🖥️ **Slide 2:** Demystifying test doubles: Mocks, Stubs, and Spies.
- 🖥️ **Slide 3:** Mocking dependency injection boundaries in Jest.
- 🖥️ **Slide 4:** Live demo: Executing 1,000 mock assertions in 2 seconds.

**Live Coding / Screencast Scenario:**  
Author a weather lookup function. Disconnect local network connectivity. Execute a mock Jest suite and demonstrate passing assertions in 5ms without live internet.

---

## 🎯 7. Daily Action Task & Mini Quiz

### 🛠️ Daily Action Task:
Author an isolated unit test for an external third-party API integration in your project, replacing network calls with `jest.fn()` mocks.

### 🧠 Chapter Review Quiz:

**Question 1:** What is the primary technical rationale for utilizing Mocks in unit testing suites?
  - A) Artificially expanding project code volume
  - B) Decoupling tests from slow, non-deterministic external I/O (network calls, disks, third-party APIs) to guarantee fast, deterministic runs
  - C) Compliance with Python-only standards
  - D) Preventing CSS layout glitches
> **Correct Answer:** B
> **Explanation:** Mocks virtualize external boundaries, ensuring test execution completes in milliseconds without network or database dependencies.

**Question 2:** What invariant is validated by `expect(mockFunction).not.toHaveBeenCalled()` in Jest?
  - A) The method suffered a stack overflow
  - B) The target mock was never executed during the test, ensuring unintended side-effects were properly averted
  - C) The host machine terminated execution
  - D) The suite failed
> **Correct Answer:** B
> **Explanation:** It proves that guarded execution paths prevent dangerous side-effects (like duplicate credit card charges) under negative conditions.

