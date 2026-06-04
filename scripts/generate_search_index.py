#!/usr/bin/env python3
import json
import os
import re
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IGNORE_FILES = {"search.html", "search.json"}
IGNORE_DIRS = {"_layouts", ".git", ".idea", "scripts"}

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_parts = []
        self._skip = False
        self._skip_stack = []

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self._skip = True
            self._skip_stack.append(tag)

    def handle_endtag(self, tag):
        if self._skip and self._skip_stack and self._skip_stack[-1] == tag:
            self._skip_stack.pop()
            self._skip = bool(self._skip_stack)
        if tag in {"p", "div", "br", "li", "section", "article", "header", "footer", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.text_parts.append(" ")

    def handle_data(self, data):
        if self._skip:
            return
        self.text_parts.append(data)

    def get_text(self):
        text = "".join(self.text_parts)
        return re.sub(r"\s+", " ", text).strip()


def parse_html_file(path):
    title = None
    raw = open(path, "r", encoding="utf-8").read()

    if raw.startswith("---"):
        end_marker = raw.find("---", 3)
        if end_marker != -1:
            front_matter = raw[3:end_marker].strip()
            raw = raw[end_marker + 3 :].lstrip()
            title_match = re.search(r"^title:\s*(.+)$", front_matter, re.IGNORECASE | re.MULTILINE)
            if title_match:
                title = title_match.group(1).strip().strip('"').strip("'")

    title_match = re.search(r"<title>(.*?)</title>", raw, re.IGNORECASE | re.DOTALL)
    if title_match:
        title = title_match.group(1).strip()

    start = raw.lower().find("<body")
    if start != -1:
        start = raw.find(">", start)
    if start != -1:
        html = raw[start + 1 :]
    else:
        html = raw

    parser = TextExtractor()
    parser.feed(html)
    content = parser.get_text()
    return title or os.path.basename(path).replace(".html", ""), content


def main():
    records = []
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for name in files:
            if not name.endswith(".html"):
                continue
            if name in IGNORE_FILES:
                continue
            path = os.path.join(root, name)
            rel = os.path.relpath(path, ROOT).replace(os.path.sep, "/")
            if rel.startswith("_layouts/"):
                continue
            title, content = parse_html_file(path)
            records.append({
                "title": title,
                "url": "/" + rel,
                "content": content,
            })

    records.sort(key=lambda item: item["title"].lower())
    out_path = os.path.join(ROOT, "search.json")
    with open(out_path, "w", encoding="utf-8") as out:
        json.dump(records, out, indent=2, ensure_ascii=False)
        out.write("\n")
    print(f"Generated {len(records)} search entries in {out_path}")

if __name__ == "__main__":
    main()
