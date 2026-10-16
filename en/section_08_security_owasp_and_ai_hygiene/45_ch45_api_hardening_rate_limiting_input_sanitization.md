# 45. API Hardening: Rate Limiting, CORS & Input Sanitization

**Thwarting Brute-Force and DoS Outages via Sliding-Window Rate Limiters and CORS**  
*Module 8 • Difficulty Level: Intermediate / Advanced • Estimated Reading Time: 12 min*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Briefing
> **Podcast Discussion Hook:**  
> *"When a botnet hammers your `/api/login` endpoint with 10,000 credential guesses per second, why does your server freeze, and how does token-bucket rate limiting shield APIs?"*  
> 
> **3 Core Audio Takeaways:**  
> - 📌 Rate limiting bounds incoming request volume per IP or token, providing a critical circuit-breaker against brute-force attacks.
- 📌 Helmet.js automatically injects security headers (CSP, HSTS, X-Content-Type-Options) to harden client browsers.
- 📌 CORS prevents arbitrary third-party web domains from issuing unauthorized credentialed requests against your API.

---

## 📖 1. The Story & Real-World Analogy

Consider the entrance of a high-capacity concert hall.

A team of door security guards manages admission. If the doors were left completely unmonitored, an unruly mob of 10,000 would charge the foyer simultaneously, trampling patrons and shattering doors (DoS attack).

Door security enforces structural safety:
- Admission throttling: *"Only 5 patrons through the turnstiles every 60 seconds"* (Rate Limiting).
- Bag inspections: Metal detectors confiscate weapons (Input Sanitization).
- Ticket verification: Rejecting visitors without authorized passes (CORS).

Exposing an API to the public internet invites automated scanners and credential-stuffing botnets. Deploying without admission rate limiters guarantees operational collapse.

---

## 🧠 2. The AI Mental Model & Paradigm Shift

The Hardened API Gateway Pipeline:

```
[Inbound Traffic: POST /api/v1/auth/login]
                   │
                   ▼
[1. HELMET HEADERS] (Enforces HSTS, CSP, X-Frame-Options)
                   │
                   ▼
[2. CORS ENFORCEMENT] ──> "Does origin header match allowed whitelist?"
                   │
                   ▼
[3. RATE LIMITER (Redis Token Bucket)] ──> "Has this IP exceeded 5 attempts/min?"
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
[LIMIT TRIPPED: 429]   [ADMITTED: PASS]
(Too Many Requests)           │
                              ▼
                    [4. SCHEMA PARSER (Zod)]
                    (Strip unexpected properties)
```

---

## 🤖 3. AI Prompt Lab (Production-Ready Templates)

You can directly paste and adapt this prompt template in Cursor, Claude Code, ChatGPT, or Copilot:

```markdown
# ROLE: Infrastructure Security Specialist
We are hardening an Express.js API cluster.

## TASK:
1. Implement a rate-limiting middleware restricting `/api/auth/*` routes to 5 requests per minute, returning HTTP 429.
2. Configure `helmet` and strict `cors` origins for production.
3. Explain why distributed Redis Sliding-Window rate limiters are mandatory over in-memory limiters across container clusters.
```

---

## 💻 4. Code Walkthrough: Naive / Hallucination vs. Production-Grade

#### ❌ Naive / Unchecked AI Output (Risky):
```typescript
// Kötü / Güvensiz Express Kurulumu: CORS her yere açık, hız sınırı yok, güvenlik başlığı yok!
import express from 'express';
const app = express();

app.use(cors()); // Tehlikeli: Tüm siteler (saldırganlar dahil) API'ye erişebilir!
// Rate limit yok: Saldırgan saniyede 100.000 şifre deneyebilir!
app.post('/login', (req, res) => { /* ... */ });
```

#### ✅ Senior-Refined Version (Robust & Clean):
```typescript
import express from "express";
import helmet from "helmet";
import cors from "cors";
import rateLimit from "express-rate-limit";

const app = express();

// 1. Güvenlik Başlıkları (Helmet)
app.use(helmet());

// 2. Katı CORS Yapılandırması
const allowedOrigins = ["https://app.sirketimiz.com"];
app.use(cors({
  origin: (origin, callback) => {
    if (!origin || allowedOrigins.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error("CORS İlkesi İhlali: Bu domaine erişim izni yok."));
    }
  },
  credentials: true, // HttpOnly çerezlere izin ver
  methods: ["GET", "POST", "PUT", "DELETE"]
}));

// 3. Hassas Giriş Rotaları İçin Hız Sınırı (Rate Limiting)
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 Dakika
  max: 5, // IP başına maksimum 5 başarısız deneme
  standardHeaders: true, // RateLimit-* standart başlıklarını dön
  legacyHeaders: false,
  message: {
    status: 429,
    error: "Çok fazla başarısız giriş denemesi. Lütfen 15 dakika sonra tekrar deneyin."
  }
});

// Giriş rotasına limitleyiciyi bağla
app.use("/api/auth/login", authLimiter);
```

**💡 Code Analysis:**
`helmet` injects defensive HTTP response headers, `cors` restricts browser requests strictly to authorized company domains, and `authLimiter` locks down brute-force attacks after 5 attempts per window.

---

## ⚠️ 5. Junior Pitfalls & Senior Perspective

- **Trap:** Deploying in-memory rate limiters across multi-container Kubernetes pods.
  - **Remedy:** In distributed topologies, back rate-limiting state via shared Redis clusters so limits apply globally.
- **Trap:** Permitting wildcard origins (`origin: '*'`) alongside credentialed cookies.
  - **Remedy:** Enforce explicit domain whitelists for cross-origin API exchanges.
- **Trap:** Attempting to absorb volumetric multi-gigabit DDoS attacks at the Node.js application layer.
  - **Remedy:** Deflect volumetric flood attacks upstream via Cloudflare or AWS CloudFront/WAF edge shields.

---

## 🎬 6. Udemy Video Lecture Blueprint & Slide Deck

### 🎥 Lecture Title: *Lecture 45: API Hardening - Thwarting Attacks via Rate Limiting & CORS*
- 🖥️ **Slide 1:** Quantifying the operational risk of credential stuffing and DoS attacks.
- 🖥️ **Slide 2:** Rate limiting algorithms: Sliding Windows vs. Token Buckets.
- 🖥️ **Slide 3:** Injecting 11 hardened security headers instantly with Helmet.js.
- 🖥️ **Slide 4:** Demystifying CORS (Cross-Origin Resource Sharing) policies.

**Live Coding / Screencast Scenario:**  
Attach a rate limiter to an Express route. Fire 6 rapid curl requests in a bash loop. Observe the first 5 return HTTP 200, while the 6th immediately trips an HTTP 429 Too Many Requests response.

---

## 🎯 7. Daily Action Task & Mini Quiz

### 🛠️ Daily Action Task:
Integrate Helmet and an Express rate-limiter into your project, capping authentication attempts to 10 per 15-minute window per IP.

### 🧠 Chapter Review Quiz:

**Question 1:** Which RFC HTTP status code must be returned when a client breaches an active rate limit threshold?
  - A) 200 OK
  - B) 404 Not Found
  - C) 429 Too Many Requests
  - D) 500 Internal Server Error
> **Correct Answer:** C
> **Explanation:** HTTP 429 explicitly communicates rate exhaustion, conventionally paired with a `Retry-After` header.

**Question 2:** What is the primary security mandate of Cross-Origin Resource Sharing (CORS)?
  - A) Increasing global network bandwidth
  - B) Governing which foreign web origins browsers permit to initiate cross-domain network requests to an API
  - C) Automating database dumps
  - D) Minifying stylesheet bundles
> **Correct Answer:** B
> **Explanation:** CORS enforces browser-level restrictions, preventing malicious websites from issuing unauthorized requests to authenticated backend services.

