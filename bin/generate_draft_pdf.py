#!/usr/bin/env python3
import argparse
import re
from datetime import datetime
from markdown import markdown
from pathlib import Path
from weasyprint import HTML


def sanitize_heading(text):
    return re.sub(r'[^a-zA-Z0-9_-]', '', text.replace(' ', '_'))


def generate_pdf(input_dir: Path, output_file: Path):
    markdown_files = sorted(input_dir.rglob('*.md'), key=lambda p: str(p))

    toc_entries = []
    content_blocks = []

    for file in markdown_files:
        with open(file, encoding='utf-8') as f:
            html = markdown(f.read(), extensions=['extra', 'nl2br', 'sane_lists'])
            headings = re.findall(r'<h1>(.*?)</h1>', html)
            for heading in headings:
                anchor = sanitize_heading(heading)
                toc_entries.append(f"<li><a href='#{anchor}'>{heading}</a></li>")
                html = html.replace(f"<h1>{heading}</h1>", f"<h1 id='{anchor}'>{heading}</h1>")
            content_blocks.append(html)

    current_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')

    combined_html = f"""
<html>
<head>
    <meta charset='utf-8'>
    <style>
        @page {{
            size: A4;
            margin: 3cm 2.8cm;
        }}

        body {{
            font-family: 'Georgia', 'Times New Roman', serif;
            font-size: 11.5pt;
            line-height: 1.6;
            color: #222;
            margin: 0 auto;
            max-width: 75ch;
        }}

        h1, h2, h3 {{
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            color: #111;
        }}

        h1 {{
            font-size: 2.4em;
            margin-top: 2.5em;
            margin-bottom: 0.5em;
            border-bottom: 2px solid #888;
            page-break-before: always;
            line-height: 1.1;
        }}

        h2 {{
            font-size: 1.8em;
            margin-top: 2em;
            margin-bottom: 0.4em;
            line-height: 1.2;
        }}

        h3 {{
            font-size: 1.4em;
            margin-top: 1.4em;
            margin-bottom: 0.3em;
            letter-spacing: 0.05em;
            line-height: 1.25;
        }}

        .watermark {{
            position: fixed;
            top: 35%;
            left: 0;
            width: 100%;
            text-align: center;
            opacity: 0.15;
            transform: rotate(-45deg);
            z-index: 9999;
            font-size: 12em;
            font-weight: bold;
            color: red;
            pointer-events: none;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 2em 0;
            font-size: 10.5pt;
        }}

        th, td {{
            border: 1px solid #ddd;
            padding: 6px 10px;
            text-align: left;
        }}

        th {{
            background-color: #f5f5f5;
            font-weight: 600;
        }}

        .cover {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            page-break-after: always;
        }}

        .cover h1 {{
            padding-top: 4em;
            font-size: 4em;
            margin: 0;
        }}

        .cover p {{
            font-size: 1.2em;
            margin-top: 1em;
        }}

        .toc {{
            page-break-after: always;
        }}

        .toc h2 {{
            font-family: 'Georgia', serif;
            font-size: 2em;
            margin-bottom: 1em;
            border-bottom: 1px solid #ccc;
        }}

        .toc ul {{
            list-style: none;
            padding-left: 0;
        }}

        .toc li {{
            margin: 0.4em 0;
            font-size: 1.1em;
        }}
    </style>
</head>
<body>
    <div class='watermark'>DRAFT</div>
    <div class='cover'>
        <h1>Project AIMA</h1>
        <p>Draft generated on: {current_date}</p>
    </div>
    <div class='toc'>
        <h2>Table of Contents</h2>
        <ul>
            {''.join(toc_entries)}
        </ul>
    </div>
    {''.join(content_blocks)}
</body>
</html>
"""

    output_file.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=combined_html).write_pdf(str(output_file))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Concatenate Markdown files and generate a PDF with DRAFT watermark."
    )
    parser.add_argument("input_dir", type=Path, help="Root directory containing markdown files")
    parser.add_argument("output_file", type=Path, help="Path to output PDF file")

    args = parser.parse_args()
    generate_pdf(args.input_dir, args.output_file)
