# 50. Multi-Service Stacks with Docker Compose: One-Command Environments

**Spinning Up Full-Stack Apps, PostgreSQL, and Redis in 10 Seconds via Code**  
*Module 9 • Difficulty Level: Intermediate • Estimated Reading Time: 12 min*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Briefing
> **Podcast Discussion Hook:**  
> *"Why spend 3 days wrestling with manual database installations when Docker Compose scaffolds backend, database, and cache stacks in 15 seconds?"*  
> 
> **3 Core Audio Takeaways:**  
> - 📌 Docker Compose coordinates multi-container stacks (App, PostgreSQL, Redis) via a declarative `compose.yaml` specification.
- 📌 Containers on the shared Compose bridge network address each other using service names (`postgres:5432`) instead of hardcoded IPs.
- 📌 Named Volumes persist database storage across container teardowns and restarts.

---

## 📖 1. The Story & Real-World Analogy

Picture conducting a symphony orchestra.

If you phone the violinist saying: *"Warm up your strings"*, then 15 minutes later text the cellist: *"Come to the hall"*, and an hour later ask the percussionist to set up drums, you'll never start.

The maestro steps onto the podium, raises the baton, and gives the downbeat: 50 musicians strike the opening chord in unified harmony.

Docker Compose is that conductor:
- Node.js API
- PostgreSQL Database
- Redis In-Memory Cache
- MailHog SMTP sandbox

You run `docker compose up`, and the entire multi-service stack bootstraps, links network bridges, and accepts requests immediately.

---

## 🧠 2. The AI Mental Model & Paradigm Shift

The Docker Compose Network Topology:

```
[docker compose up]
         │
         ▼
┌────────────────────────────────────────────────────────┐
│             DOCKER COMPOSE BRIDGE NETWORK              │
│                                                        │
│   [Service: api] ──(postgres:5432)──> [Service: db]    │
│          │                                   │         │
│          │ (redis:6379)                      ▼         │
│          ▼                             [NAMED VOLUME]  │
│   [Service: cache]                     (postgres_data) │
│                                        (Durable Disk)  │
└────────────────────────────────────────────────────────┘
         │
 (Host Mapping: 3000:3000)
         ▼
[Local Browser: http://localhost:3000]
```

---

## 🤖 3. AI Prompt Lab (Production-Ready Templates)

You can directly paste and adapt this prompt template in Cursor, Claude Code, ChatGPT, or Copilot:

```markdown
# ROLE: DevEx & Infrastructure Automation Specialist
Author a declarative `compose.yaml` file for local development.

## REQUIREMENTS:
1. `api`: Builds local Dockerfile, maps port 3000, and mounts workspace code for hot-reloading.
2. `postgres`: PostgreSQL 16 Alpine, persists storage via `pg_data` named volume, includes health check.
3. `cache`: Redis Alpine.
4. `api` waits until `postgres` evaluates as healthy via `depends_on: condition: service_healthy`.
```

---

## 💻 4. Code Walkthrough: Naive / Hallucination vs. Production-Grade

#### ❌ Naive / Unchecked AI Output (Risky):
```yaml
# Kötü Compose Dosyası: Volume yok (veriler silinir), healthcheck yok, şifreler açık
services:
  db:
    image: postgres
  web:
    image: my-web-app
# db hazır olmadan web başlarsa bağlantı hatasıyla çöker!
```

#### ✅ Senior-Refined Version (Robust & Clean):
```yaml
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgresql://postgres:gizlisifre123@postgres:5432/uygulamadb
      - REDIS_URL=redis://redis:6379
    volumes:
      - .:/app
      - /app/node_modules # Host makinenin node_modules'ünü ezmeyi engeller
    depends_on:
      postgres:
        condition: service_healthy # Veritabanı TAM hazır olana kadar bekle!

  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: gizlisifre123
      POSTGRES_DB: uygulamadb
    ports:
      - "5432:5432"
    volumes:
      - pg_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres -d uygulamadb"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  pg_data: # Konteyner silinse bile veritabanı verisi diske kaydedilir!
```

**💡 Code Analysis:**
Using `condition: service_healthy` ensures the application never attempts to connect before PostgreSQL accepts sockets. The `pg_data` volume ensures data persists across container lifecycles.

---

## ⚠️ 5. Junior Pitfalls & Senior Perspective

- **Trap:** Configuring inter-service database hosts as `localhost:5432`.
  - **Remedy:** Containers connect across Compose networks via internal service identifiers (`postgres:5432`).
- **Trap:** Omitting named volumes, wiping the entire database on `docker compose down`.
  - **Remedy:** Mount database state to an explicitly declared named volume (`pg_data`).
- **Trap:** Getting overwhelmed by stdout noise from all services simultaneously.
  - **Remedy:** Run detached (`docker compose up -d`) and tail logs for specific targets (`docker compose logs -f api`).

---

## 🎬 6. Udemy Video Lecture Blueprint & Slide Deck

### 🎥 Lecture Title: *Lecture 50: Multi-Service Stacks with Docker Compose*
- 🖥️ **Slide 1:** What is Docker Compose and how does it automate multi-tier stacks?
- 🖥️ **Slide 2:** Inter-container networking and service resolution.
- 🖥️ **Slide 3:** Health checks and deterministic startup ordering with `depends_on`.
- 🖥️ **Slide 4:** Live demo: Bootstrapping Next.js, PostgreSQL, and Redis in 15 seconds.

**Live Coding / Screencast Scenario:**  
Run `docker compose up`. Show the healthcheck polling until Postgres is ready, triggering the web app bootstrap. Run `docker compose down`, restart the stack, and demonstrate data persistence.

---

## 🎯 7. Daily Action Task & Mini Quiz

### 🛠️ Daily Action Task:
Author a `compose.yaml` file orchestrating a local database and cache, running the stack in detached mode.

### 🧠 Chapter Review Quiz:

**Question 1:** How does an application container resolve a PostgreSQL container on a Docker Compose network?
  - A) `localhost`
  - B) `127.0.0.1`
  - C) By using the declared service name identifier (e.g., `postgres` or `db`)
  - D) Machine MAC addresses
> **Correct Answer:** C
> **Explanation:** Docker Compose deploys an embedded DNS resolver mapping service names directly to container IP addresses.

**Question 2:** What configuration ensures an application container pauses until its database dependency is fully operational?
  - A) Hardcoded `sleep 30` loops
  - B) A `healthcheck` definition combined with `depends_on: condition: service_healthy`
  - C) Restarting the Docker daemon
  - D) Standard port forwarding declarations
> **Correct Answer:** B
> **Explanation:** `service_healthy` conditions poll database socket readiness before spinning up dependent application processes.

