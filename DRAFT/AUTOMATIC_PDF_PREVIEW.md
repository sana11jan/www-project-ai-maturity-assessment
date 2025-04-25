# PDF Preview Tool for Documentation Development
This repository includes a **PDF preview tool** that generates a combined PDF from all Markdown files starting at the
document root.

Its purpose is to help authors maintain a consistent structure, catch rendering issues early, and provide a high-level
view of the work in progress.

**Important:** The preview PDF is for internal use only and is **not** intended to represent the final, publish-ready
output.


# Purpose
* Provide a **single, combined view** of all documentation content.
* Help authors **verify structure**, **spot rendering issues**, and **maintain consistency** across sections.
* Offer an **early detection mechanism** for missing or malformed headings, inconsistent hierarchy, or broken
  formatting.
* Enable a **high-level quality check** while work is still ongoing in individual Markdown files.
  ⠀

# How It Works
* All .md files are collected from the document root and its subdirectories.
* Files are sorted **lexicographically** according to their path, reflecting the intended document structure.
* Headings are automatically **numbered** (e.g., 1, 1.1, 1.1.1) for easier navigation.
* A **Table of Contents** is generated based on h1 and h2 headings.
* A **DRAFT** watermark is applied to clearly mark the PDF as non-final.

⠀The resulting PDF gives a faithful impression of the overall document flow without requiring local setup.


# GitHub Actions
* The PDF is **automatically generated** as part of a GitHub Action workflow.
* After committing changes to the repository (or a fork), you can find the latest preview PDFs under the **Actions**
  tab.
* Please allow a few minutes for the action to complete after pushing your changes.


# Structure and Validation
The **PDF preview tool** follows the [Content Guidelines](./CONTENT_GUIDELINES.md) in terms of structure and naming.
Any structural issues will cause the GitHub Action to fail, if validation is enabled in the future.


# Important Notes
* The preview is **not stylistically polished** for final publication—it focuses on correctness and coherence.
* Figures, special formatting, or production-specific layout tweaks may not be fully represented.
* Please **treat the preview as a draft** and refer to specific publishing guidelines when preparing final content.
