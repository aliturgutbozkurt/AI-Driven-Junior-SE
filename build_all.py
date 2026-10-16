#!/usr/bin/env python3
"""
Master Build Script for AI-Driven Junior Software Engineering Book Project
Generates:
  1. 60 Individual Turkish Chapter Markdown files (grouped in 10 section folders)
  2. 60 Individual English Chapter Markdown files (grouped in 10 section folders)
  3. Combined Master Turkish Markdown book (tr/combined/)
  4. Combined Master English Markdown book (en/combined/)
  5. 60 Individual Turkish Chapter PDFs (pdf_exports/tr/chapters/)
  6. 60 Individual English Chapter PDFs (pdf_exports/en/chapters/)
  7. Master Combined Turkish PDF (pdf_exports/tr/)
  8. Master Combined English PDF (pdf_exports/en/)
  9. Comprehensive book_outline.json metadata
"""

import os
import json
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

from builder.sections import (
    section_01, section_02, section_03, section_04, section_05,
    section_06, section_07, section_08, section_09, section_10
)
from builder.formatter import format_chapter_markdown
from builder.typst_wrapper import render_markdown_to_pdf

BASE_DIR = Path(__file__).resolve().parent

SECTIONS_CONFIG = [
    {
        "id": 1,
        "module": section_01,
        "tr_dir": "bolum_01_yeni_dunya_ve_ai_zihniyeti",
        "en_dir": "section_01_new_world_and_ai_mindset",
        "title_tr": "Bölüm 1: Yeni Dünyaya Giriş & AI Zihniyeti",
        "title_en": "Section 1: The New World & The AI Mindset",
        "desc_tr": "Yapay zekanın yazılım dünyasını nasıl değiştirdiğini anlayın; klavye ameleliğinden mimari orkestrasyona geçiş yapın.",
        "desc_en": "Understand how AI has reshaped engineering; transition from syntax typist to architectural orchestrator."
    },
    {
        "id": 2,
        "module": section_02,
        "tr_dir": "bolum_02_algoritmik_dusunce_ve_veri_yapilari",
        "en_dir": "section_02_algorithmic_thinking_and_data_structures",
        "title_tr": "Bölüm 2: Algoritmik Düşünce, Veri Yapıları & AI ile Problem Çözme",
        "title_en": "Section 2: Algorithmic Thinking, Data Structures & Problem Solving",
        "desc_tr": "Ezber kodlamanın ötesine geçip temel algoritmik mantığı kavrayın; yapay zekanın karmaşıklık analizlerini denetleyin.",
        "desc_en": "Look beyond rote coding to master computational fundamentals and audit AI time/space complexity."
    },
    {
        "id": 3,
        "module": section_03,
        "tr_dir": "bolum_03_modern_git_ve_takim_calismasi",
        "en_dir": "section_03_modern_git_and_team_collaboration",
        "title_tr": "Bölüm 3: Modern Git, Takım Çalışması & AI-Destekli Kod İnceleme",
        "title_en": "Section 3: Modern Git, Team Collaboration & AI-Assisted Code Reviews",
        "desc_tr": "Takım ortamında kusursuz sürüm kontrolü, rebase, branch stratejileri ve AI destekli PR süreçlerini yönetin.",
        "desc_en": "Master professional version control, rebasing, branching workflows, and AI-augmented code reviews."
    },
    {
        "id": 4,
        "module": section_04,
        "tr_dir": "bolum_04_yazilim_mimarisi_ve_tasarim_kaliplari",
        "en_dir": "section_04_software_architecture_and_design_patterns",
        "title_tr": "Bölüm 4: Yazılım Mimarisi, Tasarım Kalıpları & Temiz Kod",
        "title_en": "Section 4: Software Architecture, Design Patterns & Clean Code",
        "desc_tr": "SOLID prensipleri, tasarım kalıpları ve katmanlı mimarilerle spagetti kodları önleyin; AI çıktısını yapılandırın.",
        "desc_en": "Prevent spaghetti code through SOLID, design patterns, and layered architectures while disciplining AI code generation."
    },
    {
        "id": 5,
        "module": section_05,
        "tr_dir": "bolum_05_veritabanlari_ve_backend_temelleri",
        "en_dir": "section_05_databases_and_backend_fundamentals",
        "title_tr": "Bölüm 5: Veritabanları, Veri Modelleme & Backend Temelleri",
        "title_en": "Section 5: Databases, Data Modeling & Backend Engineering",
        "desc_tr": "İlişkisel ve NoSQL modelleme, indeksleme, N+1 sorgu optimizasyonu ve dayanıklı API tasarım ilkelerini öğrenin.",
        "desc_en": "Master relational & NoSQL schemas, database indexing, N+1 query elimination, and resilient API contracts."
    },
    {
        "id": 6,
        "module": section_06,
        "tr_dir": "bolum_06_test_odakli_gelistirme_ve_kalite",
        "en_dir": "section_06_test_driven_development_and_quality",
        "title_tr": "Bölüm 6: Test Odaklı Geliştirme (TDD) & Kalite Güvencesi",
        "title_en": "Section 6: Test-Driven Development (TDD) & Quality Assurance",
        "desc_tr": "Birim, entegrasyon ve E2E test stratejileri kurun; yapay zekanın ürettiği kodun en büyük savunma kalkanı olan testleri yönetin.",
        "desc_en": "Build unit, integration, and E2E safety nets to fearlessly verify and guide AI-generated codebases."
    },
    {
        "id": 7,
        "module": section_07,
        "tr_dir": "bolum_07_hata_ayiklama_ve_gozlemlenebilirlik",
        "en_dir": "section_07_debugging_and_observability",
        "title_tr": "Bölüm 7: Hata Ayıklama (Debugging), Profiling & Gözlemlenebilirlik",
        "title_en": "Section 7: Debugging, Profiling & Observability",
        "desc_tr": "Gelişmiş loglama, metrikler, trace takibi, bellek sızıntısı tespiti ve AI ile kök neden analizi gerçekleştirin.",
        "desc_en": "Master structured logging, distributed tracing, memory profiling, and AI-accelerated root cause analysis."
    },
    {
        "id": 8,
        "module": section_08,
        "tr_dir": "bolum_08_guvenlik_owasp_ve_ai_hijyeni",
        "en_dir": "section_08_security_owasp_and_ai_hygiene",
        "title_tr": "Bölüm 8: Güvenlik, OWASP & AI Kod Hijyeni",
        "title_en": "Section 8: Security, OWASP & AI Code Hygiene",
        "desc_tr": "OWASP Top 10 açıkları, gizli anahtar yönetimi, prompt enjeksiyonları ve yapay zeka halüsinasyon risklerine karşı sisteminizi zırhlandırın.",
        "desc_en": "Fortify applications against OWASP Top 10 vulnerabilities, leaked credentials, prompt injections, and AI hallucinations."
    },
    {
        "id": 9,
        "module": section_09,
        "tr_dir": "bolum_09_devops_docker_ve_bulut",
        "en_dir": "section_09_devops_docker_and_cloud",
        "title_tr": "Bölüm 9: DevOps, Konteynerizasyon & Bulut Dağıtımı",
        "title_en": "Section 9: DevOps, Containerization & Cloud Deployment",
        "desc_tr": "Docker çok aşamalı derlemeler, CI/CD pipeline otomasyonu ve bulut dağıtım mimarilerini hayata geçirin.",
        "desc_en": "Build multi-stage Docker containers, automate CI/CD pipelines, and deploy production microservices to the cloud."
    },
    {
        "id": 10,
        "module": section_10,
        "tr_dir": "bolum_10_kariyer_ve_kidemli_zihniyeti",
        "en_dir": "section_10_career_and_senior_mindset",
        "title_tr": "Bölüm 10: Kariyer Hızlandırma, İletişim & Kıdemli Zihniyeti",
        "title_en": "Section 10: Career Acceleration, Soft Skills & The Senior Mindset",
        "desc_tr": "Teknik liderlik, mülakat hazırlığı, mentörlük ve AI çağında aranan 10x mühendis olma vizyonunu edinin.",
        "desc_en": "Cultivate technical leadership, master modern AI-era interviews, and develop the 10x senior engineering mindset."
    }
]

def load_all_chapters():
    all_chapters = []
    for sec in SECTIONS_CONFIG:
        chs = sec["module"].get_section_chapters()
        for ch in chs:
            ch["section_meta"] = sec
            all_chapters.append(ch)
    return all_chapters

def compile_pdf_task(task_args):
    """Worker function for concurrent PDF compilation."""
    md_content, pdf_path, title, subtitle, lang, is_full_book = task_args
    try:
        render_markdown_to_pdf(
            markdown_content=md_content,
            output_pdf_path=str(pdf_path),
            title=title,
            subtitle=subtitle,
            lang=lang,
            is_full_book=is_full_book
        )
        return True, str(pdf_path), None
    except Exception as e:
        return False, str(pdf_path), str(e)

def main():
    print("=" * 70)
    print("🚀 STARTING FULL BOOK BUILD: AI-DRIVEN JUNIOR SOFTWARE ENGINEERING")
    print("=" * 70)
    start_time = time.time()

    chapters = load_all_chapters()
    print(f"📦 Successfully loaded {len(chapters)} chapters across 10 sections.\n")

    # 1. Directory Setup
    dirs_to_create = [
        BASE_DIR / "tr" / "combined",
        BASE_DIR / "en" / "combined",
        BASE_DIR / "pdf_exports" / "tr" / "chapters",
        BASE_DIR / "pdf_exports" / "en" / "chapters",
    ]
    for sec in SECTIONS_CONFIG:
        dirs_to_create.append(BASE_DIR / "tr" / sec["tr_dir"])
        dirs_to_create.append(BASE_DIR / "en" / sec["en_dir"])

    for d in dirs_to_create:
        d.mkdir(parents=True, exist_ok=True)

    print("📁 Verified directory structure.")

    # 2. Generate Individual Markdown Files
    print("\n📝 Generating 120 Individual Markdown Files (60 TR + 60 EN)...")
    tr_chapter_mds = []
    en_chapter_mds = []

    for ch in chapters:
        sec = ch["section_meta"]
        ch_id = ch["id"]
        slug_tr = ch["slug_tr"]
        slug_en = ch["slug_en"]

        # TR Markdown
        md_tr = format_chapter_markdown(ch, lang="tr")
        tr_file = BASE_DIR / "tr" / sec["tr_dir"] / f"{ch_id:02d}_{slug_tr}.md"
        tr_file.write_text(md_tr, encoding="utf-8")
        tr_chapter_mds.append((ch, md_tr, tr_file))

        # EN Markdown
        md_en = format_chapter_markdown(ch, lang="en")
        en_file = BASE_DIR / "en" / sec["en_dir"] / f"{ch_id:02d}_{slug_en}.md"
        en_file.write_text(md_en, encoding="utf-8")
        en_chapter_mds.append((ch, md_en, en_file))

    print("✅ All 120 individual Markdown files generated successfully.")

    # 3. Generate Combined Master Markdown Files
    print("\n📚 Assembling Combined Master Markdown Books...")
    
    # Turkish Master Book
    tr_toc_items = []
    tr_body_parts = []
    current_sec_id = None

    for ch, md, _ in tr_chapter_mds:
        sec = ch["section_meta"]
        if sec["id"] != current_sec_id:
            current_sec_id = sec["id"]
            tr_toc_items.append(f"\n### {sec['title_tr']}\n*{sec['desc_tr']}*\n")
            tr_body_parts.append(f"\n\n# {sec['title_tr']}\n\n> **{sec['desc_tr']}**\n\n---\n\n")
        tr_toc_items.append(f"- **{ch['id']:02d}. {ch['title_tr']}** — *{ch['subtitle_tr']}*")
        tr_body_parts.append(md)

    tr_master_md = f"""# AI Çağında Junior Yazılım Mühendisliği
## Sıfırdan Uzmanlığa Yapay Zeka Destekli Mühendislik Rehberi

**Yazar:** AI-Driven Software Engineering Collective  
**Baskı:** 2026 İlkbahar / Kapsamlı Başvuru & Eğitim Edisyonu  
**Hedef Kitle:** Yazılıma yeni başlayanlar, stajyerler, junior geliştiriciler ve ekibini modernize etmek isteyen teknik liderler.  
**Özellik:** NotebookLM sesli genel bakış (Audio Overview Podcast) ve Udemy kurs üretimi için özel olarak tasarlanmıştır.

---

## 🎯 Kitabın Amacı ve AI Çağında Hayatta Kalma Rehberi

Bu kitap, yapay zekanın kod yazabildiği bir dünyada junior bir mühendisin nasıl vazgeçilmez, yüksek etki yaratan ve aranan bir teknik profesyonele dönüşebileceğini adım adım anlatmaktadır. 

Geleneksel yazılım eğitimleri söz dizimi (syntax) ezberletmeye odaklanırken, bu kitap sizi **mimari düşünen, AI ajanlarını denetleyen, test odaklı çalışan ve güvenlik açıklarını koklayabilen bir orkestra şefine** dönüştürmeyi amaçlar.

---

## 📋 Detaylı Müfredat & İçindekiler Tablosu

{chr(10).join(tr_toc_items)}

---

{"\n\n---\n\n".join(tr_body_parts)}
"""
    tr_combined_path = BASE_DIR / "tr" / "combined" / "AI_Driven_Junior_Yazilim_Muhendisligi_Tam_Kitap.md"
    tr_combined_path.write_text(tr_master_md, encoding="utf-8")
    print(f"✅ Turkish Master Book Markdown saved: {tr_combined_path} ({len(tr_master_md):,} chars)")

    # English Master Book
    en_toc_items = []
    en_body_parts = []
    current_sec_id = None

    for ch, md, _ in en_chapter_mds:
        sec = ch["section_meta"]
        if sec["id"] != current_sec_id:
            current_sec_id = sec["id"]
            en_toc_items.append(f"\n### {sec['title_en']}\n*{sec['desc_en']}*\n")
            en_body_parts.append(f"\n\n# {sec['title_en']}\n\n> **{sec['desc_en']}**\n\n---\n\n")
        en_toc_items.append(f"- **{ch['id']:02d}. {ch['title_en']}** — *{ch['subtitle_en']}*")
        en_body_parts.append(md)

    en_master_md = f"""# AI-Driven Junior Software Engineering
## From Zero to Mastery: The Production-Ready AI Era Playbook

**Author:** AI-Driven Software Engineering Collective  
**Edition:** Spring 2026 / Comprehensive Reference & Curriculum Edition  
**Target Audience:** Aspiring engineers, interns, junior developers, and engineering managers looking to modernize teams.  
**Special Feature:** Fully optimized for Google NotebookLM Audio Overviews (Podcasts) and Udemy course development.

---

## 🎯 Mission Statement: Engineering in the Age of Generative AI

This book provides a pragmatic roadmap for junior software engineers navigating a landscape where AI models write code in milliseconds.

While conventional computer science courses emphasize syntax memorization, this playbook elevates you into an **architectural orchestrator who supervises AI agents, guarantees test reliability, and mitigates security risks with senior precision**.

---

## 📋 Comprehensive Syllabus & Table of Contents

{chr(10).join(en_toc_items)}

---

{"\n\n---\n\n".join(en_body_parts)}
"""
    en_combined_path = BASE_DIR / "en" / "combined" / "AI_Driven_Junior_Software_Engineering_Full_Book.md"
    en_combined_path.write_text(en_master_md, encoding="utf-8")
    print(f"✅ English Master Book Markdown saved: {en_combined_path} ({len(en_master_md):,} chars)")

    # 4. Generate Outline JSON Metadata
    print("\n📑 Generating book_outline.json...")
    outline_data = {
        "project": "AI-Driven Junior Software Engineering",
        "edition": "2026",
        "total_modules": 10,
        "total_chapters": 60,
        "modules": []
    }

    for sec in SECTIONS_CONFIG:
        sec_chs = [c for c in chapters if c["section_id"] == sec["id"]]
        sec_dict = {
            "section_id": sec["id"],
            "title_tr": sec["title_tr"],
            "title_en": sec["title_en"],
            "description_tr": sec["desc_tr"],
            "description_en": sec["desc_en"],
            "chapters": []
        }
        for c in sec_chs:
            sec_dict["chapters"].append({
                "chapter_id": c["id"],
                "slug_tr": c["slug_tr"],
                "slug_en": c["slug_en"],
                "title_tr": c["title_tr"],
                "title_en": c["title_en"],
                "subtitle_tr": c["subtitle_tr"],
                "subtitle_en": c["subtitle_en"],
                "level_tr": c["level_tr"],
                "level_en": c["level_en"],
                "read_time_tr": c["read_time_tr"],
                "read_time_en": c["read_time_en"],
                "udemy_lecture_tr": c["udemy_title_tr"],
                "udemy_lecture_en": c["udemy_title_en"],
                "podcast_hook_tr": c["podcast_hook_tr"],
                "podcast_hook_en": c["podcast_hook_en"]
            })
        outline_data["modules"].append(sec_dict)

    outline_path = BASE_DIR / "book_outline.json"
    with open(outline_path, "w", encoding="utf-8") as f:
        json.dump(outline_data, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved syllabus metadata to: {outline_path}")

    # 5. Compile All PDFs (120 Chapters + 2 Full Books = 122 PDFs)
    print("\n⚙️ Compiling 120 Individual Chapter PDFs in Parallel...")
    tasks = []

    # 60 Turkish Chapters
    for ch, md, _ in tr_chapter_mds:
        pdf_path = BASE_DIR / "pdf_exports" / "tr" / "chapters" / f"bolum_{ch['id']:02d}_{ch['slug_tr']}.pdf"
        tasks.append((md, pdf_path, ch["title_tr"], ch["subtitle_tr"], "tr", False))

    # 60 English Chapters
    for ch, md, _ in en_chapter_mds:
        pdf_path = BASE_DIR / "pdf_exports" / "en" / "chapters" / f"chapter_{ch['id']:02d}_{ch['slug_en']}.pdf"
        tasks.append((md, pdf_path, ch["title_en"], ch["subtitle_en"], "en", False))

    # Run in parallel with ThreadPoolExecutor
    completed_count = 0
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = {executor.submit(compile_pdf_task, t): t for t in tasks}
        for future in as_completed(futures):
            ok, pdf_name, err = future.result()
            if not ok:
                print(f"❌ Error compiling {pdf_name}: {err}")
            else:
                completed_count += 1
                if completed_count % 20 == 0 or completed_count == len(tasks):
                    print(f"  [Progress] {completed_count}/{len(tasks)} chapter PDFs compiled...")

    print(f"✅ Successfully compiled {completed_count}/120 chapter PDFs!")

    # 6. Compile Master Books
    print("\n📖 Compiling Master Combined Books...")
    
    # Master Turkish PDF
    print("  -> Compiling Master Turkish PDF (AI_Driven_Junior_Yazilim_Muhendisligi_TAM_KITAP.pdf)...")
    tr_master_pdf = BASE_DIR / "pdf_exports" / "tr" / "AI_Driven_Junior_Yazilim_Muhendisligi_TAM_KITAP.pdf"
    render_markdown_to_pdf(
        markdown_content=tr_master_md,
        output_pdf_path=str(tr_master_pdf),
        title="AI Çağında Junior Yazılım Mühendisliği",
        subtitle="Sıfırdan Uzmanlığa Yapay Zeka Destekli Mühendislik Rehberi",
        lang="tr",
        is_full_book=True
    )
    print(f"  ✅ Master Turkish PDF completed: {tr_master_pdf} ({os.path.getsize(tr_master_pdf) / (1024*1024):.2f} MB)")

    # Master English PDF
    print("  -> Compiling Master English PDF (AI_Driven_Junior_Software_Engineering_FULL_BOOK.pdf)...")
    en_master_pdf = BASE_DIR / "pdf_exports" / "en" / "AI_Driven_Junior_Software_Engineering_FULL_BOOK.pdf"
    render_markdown_to_pdf(
        markdown_content=en_master_md,
        output_pdf_path=str(en_master_pdf),
        title="AI-Driven Junior Software Engineering",
        subtitle="From Zero to Mastery: The Production-Ready AI Era Playbook",
        lang="en",
        is_full_book=True
    )
    print(f"  ✅ Master English PDF completed: {en_master_pdf} ({os.path.getsize(en_master_pdf) / (1024*1024):.2f} MB)")

    elapsed = time.time() - start_time
    print("\n" + "=" * 70)
    print(f"🎉 BUILD COMPLETED IN {elapsed:.2f} SECONDS!")
    print(f"📊 Summary of Generated Assets:")
    print(f"  - 60 Turkish Chapter Markdown Files (10 Modules)")
    print(f"  - 60 English Chapter Markdown Files (10 Modules)")
    print(f"  - 1 Master Turkish Combined Markdown Book")
    print(f"  - 1 Master English Combined Markdown Book")
    print(f"  - 60 Individual Turkish Chapter PDFs")
    print(f"  - 60 Individual English Chapter PDFs")
    print(f"  - 1 Master Combined Turkish PDF (Full Book)")
    print(f"  - 1 Master Combined English PDF (Full Book)")
    print(f"  - 1 Syllabus Metadata JSON (book_outline.json)")
    print(f"  - Total PDFs: 122 production-ready vector PDFs")
    print("=" * 70)

if __name__ == "__main__":
    main()
