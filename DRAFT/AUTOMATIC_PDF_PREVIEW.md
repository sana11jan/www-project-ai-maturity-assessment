# PDF Preview Tool for Documentation Development
This repository includes a **PDF Preview Tool** that generates a combined, draft-quality PDF from all Markdown files in the document structure. It provides a unified, high-level view of the evolving documentation during development.
**Note:** The preview PDF is intended for internal use only and is **not final**.

# Purpose
* Offer a **full-document perspective** beyond individual Markdown files.
* Help maintain a **consistent structure** across chapters and sections (headings, tables, emphasis, terminology, etc.).
* Encourage careful use of **abbreviations vs. full names** (e.g., AIMA vs. AIMA (AI Maturity Assessment)).
* Support **logical flow**: thinking critically about when and where concepts are introduced.
* Foster **professional typography** (e.g., correct usage of em dashes, quotation marks, and punctuation).
* Inspire a mindset of **writing locally** but **thinking globally**.

⠀The tool is intended to **catch structural issues early**, **improve overall document quality**, and **simplify cross-author collaboration**.

# How It Works
* All .md files are automatically collected from the document root and its subdirectories.
* Files are sorted **lexicographically** based on path, reflecting the intended document structure.
* Headings are automatically **numbered** for clarity (1, 1.2, 1.2.3).
* A **Table of Contents** is generated, listing all h1 and h2 headings.
* The PDF includes a **draft watermark** and a **disclaimer** to avoid confusion with production outputs.
* **Branch** and **commit** information is embedded for version traceability.

⠀
# GitHub Actions
The PDF is generated automatically via GitHub Actions after each commit to the repository or your fork.
* Visit the **Actions** tab after pushing your changes.
* Locate the latest workflow run and download your generated PDF.
* No local execution required — the build process typically takes less than a minute.

⠀
# Important Notes
* Respect the **folder and file structure**: it defines the document order.
* Ensure each major section begins with a **single** # Heading 1.
* Use ## Heading 2 and ### Heading 3 consistently for subsections.
* Be mindful of **terminology consistency**, especially for abbreviations, acronyms, and technical terms.
* Strive for **clean, readable typography** — it matters as much as the content.
