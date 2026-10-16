# 30. Authentication & Authorization: JWT, OAuth2 & Role-Based Access Control

**Securing Web APIs: The Clear Divide Between Authentication and Authorization**  
*Module 5 • Difficulty Level: Intermediate / Advanced • Estimated Reading Time: 13 min*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Briefing
> **Podcast Discussion Hook:**  
> *"Why is persisting JWTs in `localStorage` an open invitation to XSS attacks, and how do HttpOnly cookies combined with Refresh Tokens safeguard APIs?"*  
> 
> **3 Core Audio Takeaways:**  
> - 📌 Authentication answers 'Who are you?'; Authorization answers 'What permissions do you hold?'.
- 📌 JWTs are cryptographically signed, NOT encrypted; anyone can decode the payload, so never store secrets inside them.
- 📌 Guard tokens against Cross-Site Scripting (XSS) by storing them in `HttpOnly, Secure, SameSite=Strict` cookies rather than `localStorage`.

---

## 📖 1. The Story & Real-World Analogy

Picture navigating an international airport terminal.

1. **Authentication:** You approach border control. The officer checks your passport and facial biometrics: *"You are indeed Jordan."* That is identity verification.
2. **Authorization:** You walk down the jet bridge. Your boarding pass designates Seat 18B. You cannot walk into First Class or unlock the cockpit door. Your role-based pass grants entry strictly to Seat 18B.

Holding a verified passport does not authorize you to fly the plane.

In software engineering, successfully logging in (AuthN) does not confer permission to delete other tenants' invoices (AuthZ). Role-Based Access Control (RBAC) enforces these operational boundaries.

---

## 🧠 2. The AI Mental Model & Paradigm Shift

Hardened Modern Auth Topology:

```
[Browser Client] ──(POST /api/login)──> [Authentication Server]
                                                │
                                  ┌─────────────┴─────────────┐
                                  ▼                           ▼
                      [Access Token (15 min)]     [Refresh Token (7 days)]
                      (Stateless Signed JWT)      (Opaque, hashed in DB)
                                  │                           │
                                  └─────────────┬─────────────┘
                                                ▼
                         Set-Cookie: HttpOnly, Secure, SameSite=Strict
```

---

## 🤖 3. AI Prompt Lab (Production-Ready Templates)

You can directly paste and adapt this prompt template in Cursor, Claude Code, ChatGPT, or Copilot:

```markdown
# ROLE: Application Security & IAM Specialist
We are securing an Express/TypeScript API with Role-Based Access Control (RBAC).

## TASK:
1. Implement an `authenticate` middleware verifying JWT signatures and attaching claims to `req.user`.
2. Implement a higher-order `authorize(...allowedRoles)` middleware enforcing access permissions.
3. Emit semantically correct status codes: 401 Unauthorized vs. 403 Forbidden.
```

---

## 💻 4. Code Walkthrough: Naive / Hallucination vs. Production-Grade

#### ❌ Naive / Unchecked AI Output (Risky):
```typescript
// Güvensiz Yaklaşım: Rolü frontend'den gelen parametreye göre kontrol etmek!
app.delete("/users/:id", async (req, res) => {
  // Saldırgan URL'e ?role=ADMIN yazarak herkesi silebilir!
  if (req.query.role === "ADMIN") {
    await db.user.delete({ where: { id: req.params.id } });
    return res.send("Silindi");
  }
  res.status(403).send("Yetkisiz");
});
```

#### ✅ Senior-Refined Version (Robust & Clean):
```typescript
import { Request, Response, NextFunction } from "express";
import jwt from "jsonwebtoken";

export interface UserTokenPayload {
  userId: string;
  email: string;
  role: "USER" | "ADMIN" | "SUPERVISOR";
}

// 1. Kimlik Doğrulama (Authentication - 401)
export function authenticate(req: Request, res: Response, next: NextFunction) {
  const token = req.cookies?.accessToken || req.headers.authorization?.split(" ")[1];

  if (!token) {
    return res.status(401).json({ error: "Oturum açılmadı (Token eksik)." });
  }

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET!) as UserTokenPayload;
    (req as any).user = decoded;
    next();
  } catch (err) {
    return res.status(401).json({ error: "Geçersiz veya süresi dolmuş token." });
  }
}

// 2. Yetkilendirme (Authorization / RBAC - 403)
export function authorize(...allowedRoles: Array<UserTokenPayload["role"]>) {
  return (req: Request, res: Response, next: NextFunction) => {
    const user = (req as any).user as UserTokenPayload;

    if (!user || !allowedRoles.includes(user.role)) {
      return res.status(403).json({ error: "Yetersiz yetki: Bu kaynağa erişim izniniz yok." });
    }

    next();
  };
}

// 3. Güvenli Rota Kullanımı:
// app.delete("/users/:id", authenticate, authorize("ADMIN"), deleteUserHandler);
```

**💡 Code Analysis:**
Respects the critical distinction: `401 Unauthorized` means authentication failed; `403 Forbidden` means identity is verified, but permissions are insufficient.

---

## ⚠️ 5. Junior Pitfalls & Senior Perspective

- **Trap:** Embedding passwords or sensitive PII inside JWT payloads.
  - **Remedy:** JWT payloads are easily decoded Base64 strings; store only public IDs and role claims.
- **Trap:** Storing authorization tokens in browser `localStorage`, exposing them to XSS exfiltration.
  - **Remedy:** Persist tokens in `HttpOnly` cookies inaccessible to JavaScript injection attacks.
- **Trap:** Conflating 401 Unauthorized with 403 Forbidden.
  - **Remedy:** Emit 401 when authentication is absent or expired; emit 403 when authenticated identity lacks role permissions.

---

## 🎬 6. Udemy Video Lecture Blueprint & Slide Deck

### 🎥 Lecture Title: *Lecture 30: Authentication & Authorization - JWTs & RBAC in Action*
- 🖥️ **Slide 1:** Authentication vs. Authorization: Understanding the boundary.
- 🖥️ **Slide 2:** Anatomy of a JWT: Header, Claims Payload, Cryptographic Signature.
- 🖥️ **Slide 3:** Mitigating XSS: Why `HttpOnly` cookies trump `localStorage`.
- 🖥️ **Slide 4:** Module 5 Recap: Databases, Relational Modeling & Backend Mastery.

**Live Coding / Screencast Scenario:**  
Navigate to jwt.io. Paste a sample token to illustrate that payloads are plain Base64 JSON. Test an Express route with an unprivileged token to demonstrate a 403 Forbidden response.

---

## 🎯 7. Daily Action Task & Mini Quiz

### 🛠️ Daily Action Task:
Refactor a route in your project to read user roles strictly from verified JWT claims rather than request bodies or query parameters.

### 🧠 Chapter Review Quiz:

**Question 1:** What is the precise RFC HTTP distinction between 401 Unauthorized and 403 Forbidden?
  - A) They are interchangeable status codes
  - B) 401 implies missing or invalid credentials (unauthenticated); 403 implies authenticated identity with insufficient privileges (unauthorized)
  - C) 401 is exclusive to mobile clients
  - D) 403 indicates database infrastructure failures
> **Correct Answer:** B
> **Explanation:** 401 indicates unauthenticated requests; 403 indicates that credentials were recognized but lack authorization for the target resource.

**Question 2:** What is the primary security justification for storing authentication JWTs inside `HttpOnly` cookies rather than `localStorage`?
  - A) Accelerating CSS rendering pipelines
  - B) Preventing cross-site scripting (XSS) malicious scripts from accessing and exfiltrating the token payload
  - C) Compatibility restricted to Google Chrome
  - D) Compressing token string lengths
> **Correct Answer:** B
> **Explanation:** The browser blocks JavaScript from accessing `HttpOnly` cookies, preventing compromised client scripts from exfiltrating credentials.

