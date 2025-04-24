# Project Structure and Contribution Guidelines

This project is designed for asynchronous collaboration and final PDF generation.
The content is structured as chapters and sections in Markdown. Please follow these guidelines to ensure consistency.

# Folder and File Structure

* Top-level folders represent major chapters (H1).
* Each folder contains:
  * 00_index.md → Defines the chapter title (starts with `#`).
  * Numbered .md files → Each file is a section (starts with `##`).
  * Optional assets (images, diagrams) stored in /assets/ or relative paths.

**Example**:
```
./10_Governance/
├── 00_index.md                 // Represents the Chapter, starts with "# Governance"
├── 10_Strategy_and_Metrics.md  // Represents a section, starts with "## Strategy and Metrics"
├── 20_Policy_and_Compliance.md // Represents a section, starts with "## Policy and Compliance"
```

Sorting note: The 00_index.md file will always be the first file, hence the 00 prefix. It represents the folder, which is a chapter in AIMA terms. Numbered files (10_, 20_, 30_) define section order.

# Markdown Heading Rules

|     **File type**      | **Required first heading** |      **Syntax**      |
|:----------------------:|:--------------------------:|:--------------------:|
|      00_index.md       |       Chapter title        |      `#` Title       |
|   Section .md files    |       Section title        |      `##` Title      |
| Subsections (optional) |        Subheadings         | `###`, `####`, etc.  |

* Please use only one `#` heading per chapter — located in 00_index.md.

# Numbering and File Naming Conventions

* Prefix section files with 10_, 20_, 30_, etc., to control sort order. 00 is reserved for index.
* Use gaps between numbers for future insertions.
* Avoid renumbering existing files without a valid reason.

# Content Style and Tone for Section Files

Each section (`10_*.md`, `20_*.md`, etc.) should:
- Begin with a `##` title (e.g., `## Strategy and Metrics`)
- Use `###` and `####` for subheadings as needed
- Be written in a clear, professional tone suitable for an executive or security governance audience
- Use imperative language: _implement this_, _check that_, etc.
- Aim for ~3 bullet points per stream. In this early phase, it's fine to have more—we’ll condense later.
- Use the current best example file for reference: 10_Governance/10_Strategy_and_Metrics.md

# Pull Request Requirements

* Work inside ./docs/DRAFT/.
* One section or focused change per pull request.
* Respect the folder structure and naming conventions.
* Do not change headings or numbering (filename changes) without prior discussion on Slack to avoid merge conflicts.
* Include assets in the correct folder if used.

# Markdown Style Guidelines

* Use sentence-per-line formatting where possible (makes diffs easier to review).
* Keep formatting minimal and consistent.
* Footnotes or references go at the end of the file in a "References" section if necessary.

For questions, reach out via the [Slack Project Channel](https://owasp.slack.com/archives/C089K6KFZMG).
