<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>PDF Outline Extractor</title>
  <style>
    body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 900px; margin: auto; background-color: #f9f9f9; }
    h1, h2, h3 { color: #2c3e50; }
    pre { background: #f4f4f4; padding: 12px; border-left: 4px solid #ccc; overflow-x: auto; }
    code { background: #eee; padding: 2px 4px; font-family: monospace; }
    ul { padding-left: 20px; }
    a { color: #2980b9; text-decoration: none; }
  </style>
</head>
<body>

  <h1>🧠 PDF Outline Extractor</h1>
  <p>This Python script extracts the <strong>Title</strong> and hierarchical <strong>Headings (H1, H2, H3)</strong> from PDF files and saves the results in a structured JSON format.</p>

  <h2>📁 Directory Structure</h2>
  <pre>
pdf_outline_extractor/
├── main.py               # Main script
├── requirements.txt      # Python dependencies
├── input/                # Place your PDF files here
│   └── sample.pdf
├── output/               # JSON output will be saved here
  </pre>

  <h2>🚀 How to Run (Locally)</h2>

  <h3>1. ✅ Install Python</h3>
  <p>Ensure you have <strong>Python 3.7+</strong> installed.</p>

  <h3>2. 📦 Install Required Dependencies</h3>
  <pre><code>pip install -r requirements.txt</code></pre>

  <h3>3. 📂 Add PDF Files</h3>
  <p>Place your PDF files (up to 50 pages) inside the <code>input/</code> folder.</p>

  <h3>4. 🏃 Run the Script</h3>
  <pre><code>python main.py</code></pre>

  <h2>📤 Output Format</h2>
  <p>Each PDF in <code>input/</code> generates a <code>.json</code> file in the <code>output/</code> folder.</p>

  <h3>✅ Sample Output</h3>
  <pre><code>{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "Applications", "page": 2 },
    { "level": "H3", "text": "AI in Healthcare", "page": 3 }
  ]
}</code></pre>

  <h2>📌 Features</h2>
  <ul>
    <li>✅ Supports PDFs up to 50 pages</li>
    <li>✅ Automatically detects Title and Headings based on font size</li>
    <li>✅ Outputs clean and structured JSON</li>
    <li>❌ No OCR support (text-based PDFs only)</li>
    <li>❌ No paragraph, list, or table extraction</li>
  </ul>

  <h2>🔧 Customization Tips</h2>
  <ul>
    <li>Adjust font-size thresholds to refine H1, H2, H3 detection</li>
    <li>Add regex or rules for filtering non-heading text</li>
    <li>Use <code>pytesseract</code> for OCR if supporting scanned PDFs</li>
  </ul>

  <h2>🛠 Requirements</h2>
  <ul>
    <li>Python 3.7 or above</li>
    <li><a href="https://github.com/jsvine/pdfplumber" target="_blank">pdfplumber</a></li>
  </ul>
  <pre><code>pip install -r requirements.txt</code></pre>

</body>
</html>
