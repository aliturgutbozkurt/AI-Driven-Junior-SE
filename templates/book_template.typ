// Premium Typst Book Template for AI-Driven Junior Software Engineering
#let book_theme(
  title: "",
  subtitle: "",
  author: "AI-Driven Junior Software Engineering Team",
  edition: "2026 Edition",
  lang: "tr",
  is_full_book: false,
  doc
) = {
  // Page setup
  set page(
    paper: "a4",
    margin: (x: 2.2cm, top: 2.8cm, bottom: 2.5cm),
    header: locate(loc => {
      let page_number = counter(page).at(loc).first()
      if page_number > 2 or not is_full_book {
        align(center)[
          #text(size: 8.5pt, fill: rgb("#64748b"), font: ("Helvetica", "Arial"))[
            #title #h(1fr) #if lang == "tr" [AI Çağında Junior Yazılımcılık] else [AI-Driven Junior Software Engineering]
          ]
          #v(-4pt)
          #line(length: 100%, stroke: 0.5pt + rgb("#e2e8f0"))
        ]
      }
    }),
    footer: locate(loc => {
      let page_number = counter(page).at(loc).first()
      if page_number > 1 or not is_full_book {
        align(center)[
          #line(length: 100%, stroke: 0.5pt + rgb("#e2e8f0"))
          #v(2pt)
          #text(size: 8.5pt, fill: rgb("#94a3b8"), font: ("Helvetica", "Arial"))[
            #if lang == "tr" [Sayfa #page_number] else [Page #page_number] #h(1fr) #edition
          ]
        ]
      }
    })
  )

  // Typography
  set text(
    font: ("Helvetica", "Arial"),
    lang: lang,
    size: 10.5pt,
    fill: rgb("#1e293b"),
    weight: "regular"
  )
  
  set par(
    justify: true,
    leading: 0.72em,
    first-line-indent: 0pt
  )

  // Headings
  show heading.where(level: 1): it => {
    v(1.5em)
    block(width: 100%)[
      #rect(
        fill: rgb("#f1f5f9"),
        radius: 6pt,
        inset: (x: 16pt, y: 14pt),
        stroke: (left: 5pt + rgb("#3b82f6"))
      )[
        #text(size: 20pt, weight: "bold", fill: rgb("#0f172a"))[#it.body]
      ]
    ]
    v(0.8em)
  }

  show heading.where(level: 2): it => {
    v(1.2em)
    text(size: 14pt, weight: "bold", fill: rgb("#1e3a8a"))[#it.body]
    v(0.4em)
  }

  show heading.where(level: 3): it => {
    v(0.9em)
    text(size: 11.5pt, weight: "bold", fill: rgb("#334155"))[#it.body]
    v(0.3em)
  }

  // Code blocks styling
  show raw.where(block: true): it => {
    rect(
      width: 100%,
      fill: rgb("#0f172a"),
      radius: 6pt,
      inset: 12pt
    )[
      #text(fill: rgb("#f8fafc"), size: 9pt, font: ("Menlo", "Courier New"))[#it]
    ]
  }

  show raw.where(block: false): it => {
    box(
      fill: rgb("#f1f5f9"),
      radius: 3pt,
      inset: (x: 4pt, y: 2pt)
    )[
      #text(fill: rgb("#0f766e"), size: 9.5pt, font: ("Menlo", "Courier New"), weight: "medium")[#it]
    ]
  }

  doc
}

// Callout Box Helpers
#let callout_notebook(body) = {
  rect(
    width: 100%,
    fill: rgb("#f5f3ff"),
    stroke: (left: 4pt + rgb("#8b5cf6"), rest: 0.5pt + rgb("#ddd6fe")),
    radius: 6pt,
    inset: 12pt,
    outset: 0pt
  )[
    #text(weight: "bold", fill: rgb("#6d28d9"), size: 10.5pt)[🎙️ NotebookLM & Audio Overview Briefing]\
    #v(4pt)
    #body
  ]
}

#let callout_prompt(body) = {
  rect(
    width: 100%,
    fill: rgb("#ecfdf5"),
    stroke: (left: 4pt + rgb("#10b981"), rest: 0.5pt + rgb("#a7f3d0")),
    radius: 6pt,
    inset: 12pt
  )[
    #text(weight: "bold", fill: rgb("#047857"), size: 10.5pt)[🤖 AI Prompt Laboratuvarı (Ready-to-Use)][ \
    #v(4pt)
    #body
  ]
}

#let callout_pitfall(body) = {
  rect(
    width: 100%,
    fill: rgb("#fffbeb"),
    stroke: (left: 4pt + rgb("#f59e0b"), rest: 0.5pt + rgb("#fde68a")),
    radius: 6pt,
    inset: 12pt
  )[
    #text(weight: "bold", fill: rgb("#b45309"), size: 10.5pt)[⚠️ Junior Tuzağı & Kıdemli Bakış Açısı]\
    #v(4pt)
    #body
  ]
}

#let callout_udemy(body) = {
  rect(
    width: 100%,
    fill: rgb("#eff6ff"),
    stroke: (left: 4pt + rgb("#3b82f6"), rest: 0.5pt + rgb("#bfdbfe")),
    radius: 6pt,
    inset: 12pt
  )[
    #text(weight: "bold", fill: rgb("#1d4ed8"), size: 10.5pt)[🎬 Udemy Video Dersi Taslağı & Uygulama]\
    #v(4pt)
    #body
  ]
}
