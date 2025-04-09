# Project Structure and Contribution Guidelines
This project is designed for asynchronous collaboration and final PDF generation. 
The content is structured as chapters and sections in Markdown. Please Follow these guidelines to ensure consistency.

# Folder and File Structure
* Top-level folders represent major chapters (H1).
* Each folder contains:
    * 00_index.md → Defines the chapter title (starts with `#`).
    * Numbered .md files → Each file is a section (starts with `##`).
    * Optional assets (images, diagrams) stored in /assets/ or relative paths.

**Example**:
```
./10_Leadership/
├── _index.md                   # Starts with "# Leadership"
├── 10_AI_Governance.md         # Starts with "## AI Governance"
├── 20_Strategy_Metrics.md      # Starts with "## Strategy and Metrics"
├── 30_Risk_Safety.md           # Starts with "## Risk and Safety"
```

Sorting note: The 00_index.md file will always be the first file, hence the 00 prefix. 
Numbered files (10_, 20_, 30_) define section order.

# Markdown Heading Rules
|     **File type**      | **Required first heading** |      **Syntax**      |
|:----------------------:|:--------------------------:|:--------------------:|
|      00_index.md       |       Chapter title        |      `#` Title       |
|   Section .md files    |       Section title        |      `##` Title      |
| Subsections (optional) |        Subheadings         | `###`, `####`, etc.  |

* Do not use `#` headings inside section .md files.
* Only one `#` heading per chapter — located in 00_index.md.
⠀
# Numbering and File Naming Conventions
* Prefix section files with 10_, 20_, 30_, etc., to control sort order. 00 is reserved for index. 
* Use gaps between numbers for future insertions.
* Avoid renumbering existing files without a valid reason.
⠀
# Pull Request Requirements
* Work inside ./docs/DRAFT/.
* One section or focused change per pull request.
* Respect the folder structure and naming conventions.
* Do not change headings or numbering  (filename changes) without prior discussion on Slack to avoid merge conflicts.
* Include assets in the correct folder if used.
⠀
# Markdown Style Guidelines
* Use sentence-per-line formatting where possible (makes diffs easier to review).
* Keep formatting minimal and consistent.
* Footnotes or references go at the end of the file in a "References" section if necessary.


For questions, reach out via the [Slack Project Channel](https://owasp.slack.com/archives/C089K6KFZMG).