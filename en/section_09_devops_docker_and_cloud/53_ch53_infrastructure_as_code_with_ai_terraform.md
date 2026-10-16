# 53. Infrastructure as Code: Writing Terraform & Pulumi with AI

**Retiring 'ClickOps' and Managing Cloud Fleets via Version-Controlled Declarative Code**  
*Module 9 • Difficulty Level: Advanced • Estimated Reading Time: 13 min*

---

> ### 🎙️ NotebookLM & Audio Overview Podcast Briefing
> **Podcast Discussion Hook:**  
> *"Why is configuring cloud infrastructure via manual console clicks ('ClickOps') an unmitigated disaster waiting to happen, and how does Terraform make infrastructure repeatable?"*  
> 
> **3 Core Audio Takeaways:**  
> - 📌 'ClickOps'—manually clicking cloud console buttons—creates unreplicable infrastructure snowflakes and invites human error.
- 📌 Infrastructure as Code (IaC) models servers, databases, and networks as declarative code checked into version control.
- 📌 Terraform's `plan` phase generates an exact execution preview, eliminating guesswork before applying changes to production.

---

## 📖 1. The Story & Real-World Analogy

Imagine building a metropolis.

If municipal workers bury water mains, high-voltage lines, and fiber cables wherever they feel like on a given morning without blueprints, within 6 months nobody knows what lies beneath the pavement. The next excavator slices the main power grid. That is **ClickOps**.

**Infrastructure as Code (Terraform)** is the master digital blueprint.

Declared in declarative code:
- One PostgreSQL cluster
- Two Application Load Balancers
- One private S3 bucket
If a regional data center suffers a catastrophic power outage, running `terraform apply` reconstructs the entire infrastructure in a secondary region within 10 minutes.

---

## 🧠 2. The AI Mental Model & Paradigm Shift

The Terraform Operational Workflow:

```
[Author `main.tf` Declarations]
              │
              ▼
[1. terraform init]  ──> Downloads required provider plugins (AWS / GCP / Azure).
              │
              ▼
[2. terraform plan]  ──> Forensic dry-run preview: asserts mutations without executing.
              │
              ▼
[3. terraform apply] ──> Executes real API calls to provision cloud resources.
              │
              ▼
[terraform.tfstate]  ──> Authoritative state ledger mapping code to live cloud IDs.
```

---

## 🤖 3. AI Prompt Lab (Production-Ready Templates)

You can directly paste and adapt this prompt template in Cursor, Claude Code, ChatGPT, or Copilot:

```markdown
# ROLE: Infrastructure as Code & Terraform Specialist
Author a modular Terraform (HCL) specification for an AWS storage module.

## TASK:
Deliver a production-grade `main.tf`:
1. Provision a private AWS S3 bucket with server-side encryption enabled (AES-256).
2. Enforce strict public access blocks.
3. Enable bucket versioning to protect against accidental deletions.
```

---

## 💻 4. Code Walkthrough: Naive / Hallucination vs. Production-Grade

#### ❌ Naive / Unchecked AI Output (Risky):
```hcl
# Kötü Terraform: Güvensiz, şifreleme yok, public erişim açık!
resource "aws_s3_bucket" "insecure_bucket" {
  bucket = "sirket-gizli-veriler"
  # Şifreleme yok, versiyonlama yok!
}
```

#### ✅ Senior-Refined Version (Robust & Clean):
```hcl
# Profesyonel ve Güvenli Terraform Mimarisi (main.tf)

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# 1. S3 Depolama Alanı
resource "aws_s3_bucket" "secure_assets" {
  bucket        = "sirket-guvenli-depo-${var.environment}"
  force_destroy = false

  tags = {
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}

# 2. Versiyonlama Koruması (Yanlışlıkla silinmeyi önler)
resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.secure_assets.id
  versioning_configuration {
    status = "Enabled"
  }
}

# 3. Sunucu Taraflı Şifreleme (AES-256)
resource "aws_s3_bucket_server_side_encryption_configuration" "crypto" {
  bucket = aws_s3_bucket.secure_assets.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# 4. İnternete Tamamen Kapat (Block Public Access)
resource "aws_s3_bucket_public_access_block" "public_block" {
  bucket = aws_s3_bucket.secure_assets.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
```

**💡 Code Analysis:**
Codifying storage via Terraform guarantees encryption, object versioning, and public-access blocks by default, completely eliminating human configuration drift.

---

## ⚠️ 5. Junior Pitfalls & Senior Perspective

- **Trap:** Committing local `terraform.tfstate` files to Git (they contain plaintext cloud secrets).
  - **Remedy:** Store state files in remote encrypted backends (S3 with DynamoDB state locking).
- **Trap:** Running `terraform apply` without auditing the preceding `terraform plan` output.
  - **Remedy:** Always review plan diffs for unexpected resource destructions (`- destroy`).
- **Trap:** Manually tweaking settings in the cloud console, inducing Configuration Drift.
  - **Remedy:** Once codified in Terraform, strictly prohibit out-of-band ClickOps edits.

---

## 🎬 6. Udemy Video Lecture Blueprint & Slide Deck

### 🎥 Lecture Title: *Lecture 53: Infrastructure as Code - Cloud Automation via Terraform*
- 🖥️ **Slide 1:** The ClickOps catastrophe: Why manual console edits destroy reliability.
- 🖥️ **Slide 2:** The Infrastructure as Code paradigm: Versioning topologies in Git.
- 🖥️ **Slide 3:** The Terraform lifecycle: `init`, `plan`, `apply`, `destroy`.
- 🖥️ **Slide 4:** Live demo: Provisioning an encrypted S3 bucket in 60 seconds with Terraform.

**Live Coding / Screencast Scenario:**  
Execute `terraform init` followed by `terraform plan`. Walk through the execution summary showing planned resource additions, then execute `terraform apply` to provision the resource live.

---

## 🎯 7. Daily Action Task & Mini Quiz

### 🛠️ Daily Action Task:
Install Terraform CLI and execute `terraform plan` against a simple local storage configuration.

### 🧠 Chapter Review Quiz:

**Question 1:** What is the primary function of the `terraform plan` command?
  - A) Deleting cloud infrastructure
  - B) Generating an execution preview comparing code against live state to declare which resources will be added, altered, or destroyed without modifying cloud state
  - C) Calculating estimated cloud costs
  - D) Powering down runner instances
> **Correct Answer:** B
> **Explanation:** `terraform plan` serves as a read-only speculative execution preview, ensuring visibility prior to executing mutations.

**Question 2:** Why must `terraform.tfstate` files never be committed to public Git repositories?
  - A) They exceed GitHub file size caps
  - B) They often store sensitive cloud metadata and database passwords in plaintext
  - C) They execute strictly on Linux runtimes
  - D) They break TypeScript compilation
> **Correct Answer:** B
> **Explanation:** State files store live configuration metadata, including sensitive secrets and database connection strings, mandating encrypted remote backends.

