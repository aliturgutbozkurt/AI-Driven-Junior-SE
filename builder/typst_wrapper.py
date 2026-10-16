import os
import subprocess
import tempfile
from pathlib import Path

TYPST_MASTER_TEMPLATE = """
#set page(
  paper: "a4",
  margin: (x: 2.2cm, top: 2.8cm, bottom: 2.5cm),
  header: context [
    #let p = counter(page).get().first()
    #if p > 1 [
      #grid(
        columns: (1fr, 1fr),
        align: (left, right),
        text(size: 8.5pt, fill: rgb("#64748b"))[__BOOK_TITLE__],
        text(size: 8.5pt, fill: rgb("#94a3b8"))[__SUBTITLE__]
      )
      #v(-4pt)
      #line(length: 100%, stroke: 0.5pt + rgb("#e2e8f0"))
    ]
  ],
  footer: context [
    #let p = counter(page).get().first()
    #if p > 1 [
      #line(length: 100%, stroke: 0.5pt + rgb("#e2e8f0"))
      #v(2pt)
      #grid(
        columns: (1fr, 1fr),
        align: (left, right),
        text(size: 8.5pt, fill: rgb("#94a3b8"))[__FOOTER_NOTE__],
        text(size: 8.5pt, fill: rgb("#64748b"), weight: "bold")[__PAGE_STR__ #p / #counter(page).final().first()]
      )
    ]
  ]
)

#set text(font: ("Helvetica", "Arial"), size: 10.5pt, fill: rgb("#1e293b"), lang: "__LANG__")
#set par(justify: true, leading: 0.72em)

#let horizontalrule = v(0.6em) + line(length: 100%, stroke: 0.5pt + rgb("#e2e8f0")) + v(0.6em)

#show terms: it => {
  it.children
    .map(child => [
      #strong[#child.term]
      #block(inset: (left: 1.5em, top: -0.4em))[#child.description]
      ])
    .join()
}

// Styled Headings
#show heading.where(level: 1): it => {
  v(1.4em)
  rect(
    width: 100%,
    fill: rgb("#f8fafc"),
    radius: 6pt,
    inset: (x: 16pt, y: 14pt),
    stroke: (left: 5pt + rgb("#2563eb"), rest: 0.5pt + rgb("#e2e8f0"))
  )[
    #text(size: 20pt, weight: "bold", fill: rgb("#0f172a"))[#it.body]
  ]
  v(0.8em)
}

#show heading.where(level: 2): it => {
  v(1.2em)
  text(size: 13.5pt, weight: "bold", fill: rgb("#1e40af"))[#it.body]
  v(0.4em)
}

#show heading.where(level: 3): it => {
  v(0.9em)
  text(size: 11pt, weight: "bold", fill: rgb("#334155"))[#it.body]
  v(0.3em)
}

// Styled Quotes as Callout Boxes
#show quote.where(block: true): it => {
  rect(
    width: 100%,
    fill: rgb("#f8fafc"),
    radius: 6pt,
    stroke: (left: 4pt + rgb("#6366f1"), rest: 0.5pt + rgb("#e0e7ff")),
    inset: (x: 12pt, y: 10pt)
  )[
    #it.body
  ]
}

// Styled Tables
#show table: set table(
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#eff6ff") } else if calc.even(row) { rgb("#f8fafc") } else { none },
  inset: 7pt
)

// Code Blocks Styling
#show raw.where(block: true): it => {
  rect(
    width: 100%,
    fill: rgb("#0f172a"),
    radius: 6pt,
    inset: 11pt
  )[
    #text(fill: rgb("#f8fafc"), size: 8.8pt, font: ("Menlo", "Courier New"))[#it]
  ]
}

#show raw.where(block: false): it => {
  box(
    fill: rgb("#f1f5f9"),
    radius: 3pt,
    inset: (x: 4pt, y: 2pt)
  )[
    #text(fill: rgb("#0f766e"), size: 9pt, font: ("Menlo", "Courier New"), weight: "bold")[#it]
  ]
}

__COVER_PAGE__

__OUTLINE__

__CONTENT__
"""

def md_to_typst_body(markdown_text: str) -> str:
    """Converts a Markdown string to a Typst string using pandoc."""
    cmd = ["pandoc", "-f", "markdown-citations", "-t", "typst"]
    proc = subprocess.run(
        cmd,
        input=markdown_text,
        capture_output=True,
        text=True,
        check=True
    )
    return proc.stdout

def compile_typst_to_pdf(typst_source: str, output_pdf_path: str):
    """Compiles Typst code into a PDF file using the Typst CLI."""
    dirname = os.path.dirname(output_pdf_path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".typ", delete=False) as f:
        f.write(typst_source)
        temp_typ_path = f.name
    
    try:
        cmd = ["typst", "compile", temp_typ_path, output_pdf_path]
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Typst compilation error for {output_pdf_path}: {e.stderr}")
        raise
    finally:
        if os.path.exists(temp_typ_path):
            os.remove(temp_typ_path)

def render_markdown_to_pdf(
    markdown_content: str,
    output_pdf_path: str,
    title: str,
    subtitle: str,
    lang: str = "tr",
    is_full_book: bool = False
):
    """Converts Markdown to Typst and compiles directly to PDF."""
    typst_body = md_to_typst_body(markdown_content)
    
    cover_page_code = ""
    outline_code = ""
    
    if is_full_book:
        if lang == "tr":
            cover_page_code = f"""
#place(top + left, dx: 0cm, dy: 3cm)[
  #rect(fill: rgb("#1e3a8a"), radius: 4pt, inset: (x: 10pt, y: 6pt))[
    #text(size: 11pt, weight: "bold", fill: white)[2026 EDİSYONU • EĞİTİM & REHBER]
  ]
  #v(1.5cm)
  #text(size: 32pt, weight: "bold", fill: rgb("#0f172a"))[{title}]\
  #v(0.6cm)
  #text(size: 18pt, weight: "medium", fill: rgb("#2563eb"))[{subtitle}]\
  #v(1.5cm)
  #line(length: 100%, stroke: 2pt + rgb("#3b82f6"))
  #v(1cm)
  #text(size: 12pt, fill: rgb("#475569"))[
    *Yazar / Geliştirici:* AI-Driven Junior Software Engineering Team\
    *Kapsam:* 10 Ana Bölüm, 60 Kapsamlı Alt Bölüm\
    *Format:* NotebookLM & Udemy Uyumlu Sesli/Videolu Müfredat Rehberi
  ]
]
#pagebreak()
"""
            outline_code = """
#v(1cm)
#outline(title: [İçindekiler Tablosu], depth: 2, indent: 1.5em)
#pagebreak()
"""
        else:
            cover_page_code = f"""
#place(top + left, dx: 0cm, dy: 3cm)[
  #rect(fill: rgb("#1e3a8a"), radius: 4pt, inset: (x: 10pt, y: 6pt))[
    #text(size: 11pt, weight: "bold", fill: white)[2026 EDITION • COURSE & GUIDE]
  ]
  #v(1.5cm)
  #text(size: 32pt, weight: "bold", fill: rgb("#0f172a"))[{title}]\
  #v(0.6cm)
  #text(size: 18pt, weight: "medium", fill: rgb("#2563eb"))[{subtitle}]\
  #v(1.5cm)
  #line(length: 100%, stroke: 2pt + rgb("#3b82f6"))
  #v(1cm)
  #text(size: 12pt, fill: rgb("#475569"))[
    *Author / Developer:* AI-Driven Junior Software Engineering Team\
    *Curriculum:* 10 Core Modules, 60 Comprehensive Chapters\
    *Format:* NotebookLM & Udemy Ready Video & Audio Curriculum Guide
  ]
]
#pagebreak()
"""
            outline_code = """
#v(1cm)
#outline(title: [Table of Contents], depth: 2, indent: 1.5em)
#pagebreak()
"""

    footer_note = "AI-Driven Junior SE • NotebookLM & Udemy Curriculum" if lang == "en" else "AI Çağında Junior Yazılımcılık • NotebookLM & Udemy Müfredatı"
    page_str = "Page" if lang == "en" else "Sayfa"

    safe_title = title.replace("$", "\\$")
    safe_subtitle = subtitle.replace("$", "\\$")

    final_typst = TYPST_MASTER_TEMPLATE \
        .replace("__BOOK_TITLE__", safe_title) \
        .replace("__SUBTITLE__", safe_subtitle) \
        .replace("__FOOTER_NOTE__", footer_note) \
        .replace("__PAGE_STR__", page_str) \
        .replace("__LANG__", lang) \
        .replace("__COVER_PAGE__", cover_page_code) \
        .replace("__OUTLINE__", outline_code) \
        .replace("__CONTENT__", typst_body)

    compile_typst_to_pdf(final_typst, output_pdf_path)
