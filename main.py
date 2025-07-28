import pdfplumber
import os
import json
from collections import defaultdict

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def extract_text_blocks(pdf_path):
    blocks = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            words = page.extract_words(extra_attrs=["size", "top"])

            line_map = defaultdict(list)
            for word in words:
                top = round(word["top"], 1)
                line_map[top].append(word)

            for top, line_words in sorted(line_map.items()):
                line_words = sorted(line_words, key=lambda w: w["x0"])
                line_text = " ".join([w["text"] for w in line_words])
                avg_size = sum(w["size"] for w in line_words) / len(line_words)

                blocks.append({
                    "text": line_text.strip(),
                    "font_size": round(avg_size, 2),
                    "page": page_num
                })

    return blocks

def extract_title(blocks):
    return max(blocks, key=lambda x: x["font_size"])["text"]

def classify_headings(blocks):
    sizes = sorted(set(b["font_size"] for b in blocks), reverse=True)
    size_to_level = {size: f"H{idx+1}" for idx, size in enumerate(sizes[:3])}

    headings = []
    for b in blocks:
        if b["font_size"] in size_to_level:
            headings.append({
                "level": size_to_level[b["font_size"]],
                "text": b["text"],
                "page": b["page"]
            })
    return headings

def process_pdf(pdf_path):
    blocks = extract_text_blocks(pdf_path)
    title = extract_title(blocks)
    outline = classify_headings(blocks)

    return {
        "title": title,
        "outline": outline
    }

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            input_pdf = os.path.join(INPUT_DIR, filename)
            output_json = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))

            print(f"Processing: {filename}")
            result = process_pdf(input_pdf)

            with open(output_json, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

            print(f"Saved: {output_json}")

if __name__ == "__main__":
    main()
