#!/usr/bin/env python3
import argparse
from pathlib import Path
from markdown import markdown
from weasyprint import HTML

def generate_pdf(input_dir: Path, output_file: Path):
    markdown_files = sorted(input_dir.rglob('*.md'), key=lambda p: str(p))

    combined_html = """
    <html>
    <head>
        <meta charset='utf-8'>
        <style>
            @page {
                size: A4;
                margin: 2cm 2.5cm;
            }
            body {
                font-family: 'Georgia', 'Times New Roman', serif;
                margin: 0;
            }
            h1, h2, h3 {
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            }
            h1 {
                font-size: 2.2em;
                border-bottom: 1px solid #ccc;
                margin-top: 1.5em;
            }
            h2 {
                font-size: 1.6em;
                margin-top: 1.2em;
            }
            h3 {
                font-size: 1.3em;
                margin-top: 1em;
            }
            .watermark {
                position: fixed;
                top: 35%;
                left: 0;
                width: 100%;
                text-align: center;
                opacity: 0.20;
                transform: rotate(-45deg);
                z-index: 9999;
                font-size: 12em;
                font-weight: bold;
                color: red;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin: 1em 0;
            }
            th, td {
                border: 1px solid #ccc;
                padding: 8px;
                text-align: left;
            }
        </style>
    </head>
    <body>
        <div class='watermark'>DRAFT</div>
    """

    for file in markdown_files:
        with open(file, encoding='utf-8') as f:
            html = markdown(f.read(), extensions=['extra'])
            combined_html += f"{html}\n"

    combined_html += "</body></html>"

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