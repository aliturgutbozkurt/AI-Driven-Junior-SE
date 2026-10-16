"""
Formatter module to convert structured Chapter data into rich, pedagogical Markdown
compatible with NotebookLM (audio overview / podcast / notes) and Udemy courses.
"""

def format_chapter_markdown(ch: dict, lang: str = "tr") -> str:
    is_tr = (lang == "tr")
    
    title = ch["title_tr"] if is_tr else ch["title_en"]
    subtitle = ch["subtitle_tr"] if is_tr else ch["subtitle_en"]
    level = ch["level_tr"] if is_tr else ch["level_en"]
    read_time = ch["read_time_tr"] if is_tr else ch["read_time_en"]
    
    # Headers
    lbl_level = "Zorluk Derecesi" if is_tr else "Difficulty Level"
    lbl_time = "Tahmini Okuma Süresi" if is_tr else "Estimated Reading Time"
    lbl_module = f"Bölüm {ch['section_id']}" if is_tr else f"Module {ch['section_id']}"
    
    # NotebookLM Section
    lbl_nlm_title = "🎙️ NotebookLM & Audio Overview Podcast Notları" if is_tr else "🎙️ NotebookLM & Audio Overview Podcast Briefing"
    lbl_nlm_hook = "**Podcast Tartışma Sorusu:**" if is_tr else "**Podcast Discussion Hook:**"
    lbl_nlm_takeaways = "**Bölümden Çıkarılacak 3 Altın Cümle:**" if is_tr else "**3 Core Audio Takeaways:**"
    
    podcast_hook = ch["podcast_hook_tr"] if is_tr else ch["podcast_hook_en"]
    takeaways = ch["takeaways_tr"] if is_tr else ch["takeaways_en"]
    takeaways_md = "\n".join([f"- 📌 {t}" for t in takeaways])
    
    # Story & Core Concept
    lbl_story = "📖 1. Giriş Hikayesi & Günlük Hayat Analojisi" if is_tr else "📖 1. The Story & Real-World Analogy"
    story = ch["story_tr"] if is_tr else ch["story_en"]
    
    # AI Mental Model
    lbl_mental = "🧠 2. AI Çağında Yeni Zihniyet Modeli" if is_tr else "🧠 2. The AI Mental Model & Paradigm Shift"
    mental = ch["mental_tr"] if is_tr else ch["mental_en"]
    
    # AI Prompt Lab
    lbl_prompt_lab = "🤖 3. AI Prompt Laboratuvarı (Kopyala-Yapıştır Hazır Prompt)" if is_tr else "🤖 3. AI Prompt Lab (Production-Ready Templates)"
    prompt_desc = "Aşağıdaki prompt şablonunu Cursor, Claude Code, ChatGPT veya Copilot ortamınızda doğrudan kullanabilirsiniz:" if is_tr else "You can directly paste and adapt this prompt template in Cursor, Claude Code, ChatGPT, or Copilot:"
    prompt_box = ch["prompt_tr"] if is_tr else ch["prompt_en"]
    
    # Code Walkthrough
    lbl_code = "💻 4. Kod İncelemesi: Acemi / Halüsinasyon vs. Üretim Kalitesi" if is_tr else "💻 4. Code Walkthrough: Naive / Hallucination vs. Production-Grade"
    lbl_naive = "❌ Acemi / Kontrolsüz AI Çıktısı (Riskli):" if is_tr else "❌ Naive / Unchecked AI Output (Risky):"
    lbl_robust = "✅ Kıdemli Mühendis Tarafından İyileştirilmiş Sürüm (Güvenli & Temiz):" if is_tr else "✅ Senior-Refined Version (Robust & Clean):"
    code_lang = ch.get("code_lang", "python")
    code_naive = ch["code_naive"]
    code_robust = ch["code_robust"]
    code_notes = ch["code_notes_tr"] if is_tr else ch["code_notes_en"]
    
    # Junior Pitfalls
    lbl_pitfalls = "⚠️ 5. Junior Tuzakları & Kıdemli Bakış Açısı" if is_tr else "⚠️ 5. Junior Pitfalls & Senior Perspective"
    pitfalls = ch["pitfalls_tr"] if is_tr else ch["pitfalls_en"]
    pitfalls_md = "\n".join([f"- **Tuzak:** {p['trap']}\n  - **Çözüm:** {p['solution']}" if is_tr else f"- **Trap:** {p['trap']}\n  - **Remedy:** {p['solution']}" for p in pitfalls])
    
    # Udemy Lecture Blueprint
    lbl_udemy = "🎬 6. Udemy Video Dersi Taslağı & Slayt Maddeleri" if is_tr else "🎬 6. Udemy Video Lecture Blueprint & Slide Deck"
    udemy_title = ch["udemy_title_tr"] if is_tr else ch["udemy_title_en"]
    udemy_slides = ch["udemy_slides_tr"] if is_tr else ch["udemy_slides_en"]
    slides_md = "\n".join([f"- 🖥️ **Slayt {i+1}:** {s}" if is_tr else f"- 🖥️ **Slide {i+1}:** {s}" for i, s in enumerate(udemy_slides)])
    udemy_demo = ch["udemy_demo_tr"] if is_tr else ch["udemy_demo_en"]
    
    # Daily Task & Mini Quiz
    lbl_task = "🎯 7. Günün Uygulamalı Görevi & Mini Sınav" if is_tr else "🎯 7. Daily Action Task & Mini Quiz"
    action_task = ch["action_task_tr"] if is_tr else ch["action_task_en"]
    quiz = ch["quiz_tr"] if is_tr else ch["quiz_en"]
    
    quiz_md = ""
    for i, q in enumerate(quiz):
        q_text = q["question"]
        options_md = "\n".join([f"  - {opt}" for opt in q["options"]])
        q_lbl = f"**Soru {i+1}:**" if is_tr else f"**Question {i+1}:**"
        answer_lbl = "**Doğru Yanıt:**" if is_tr else "**Correct Answer:**"
        exp_lbl = "**Açıklama:**" if is_tr else "**Explanation:**"
        quiz_md += f"\n{q_lbl} {q_text}\n{options_md}\n> {answer_lbl} {q['answer']}\n> {exp_lbl} {q['explanation']}\n"

    lbl_analysis = "**💡 Kod Analizi:**" if is_tr else "**💡 Code Analysis:**"
    lbl_lecture = "🎥 Ders Başlığı:" if is_tr else "🎥 Lecture Title:"
    lbl_screencast = "**Canlı Kodlama / Ekran Kaydı Senaryosu:**" if is_tr else "**Live Coding / Screencast Scenario:**"
    lbl_action_hdr = "### 🛠️ Günün Görevi:" if is_tr else "### 🛠️ Daily Action Task:"
    lbl_quiz_hdr = "### 🧠 Bölüm Sonu Kontrol Testi:" if is_tr else "### 🧠 Chapter Review Quiz:"

    md = f"""# {ch['id']}. {title}

**{subtitle}**  
*{lbl_module} • {lbl_level}: {level} • {lbl_time}: {read_time}*

---

> ### {lbl_nlm_title}
> {lbl_nlm_hook}  
> *"{podcast_hook}"*  
> 
> {lbl_nlm_takeaways}  
> {takeaways_md}

---

## {lbl_story}

{story}

---

## {lbl_mental}

{mental}

---

## {lbl_prompt_lab}

{prompt_desc}

```markdown
{prompt_box}
```

---

## {lbl_code}

#### {lbl_naive}
```{code_lang}
{code_naive}
```

#### {lbl_robust}
```{code_lang}
{code_robust}
```

{lbl_analysis}
{code_notes}

---

## {lbl_pitfalls}

{pitfalls_md}

---

## {lbl_udemy}

### {lbl_lecture} *{udemy_title}*
{slides_md}

{lbl_screencast}  
{udemy_demo}

---

## {lbl_task}

{lbl_action_hdr}
{action_task}

{lbl_quiz_hdr}
{quiz_md}
"""
    return md
