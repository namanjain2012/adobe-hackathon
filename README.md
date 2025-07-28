PDF Outline Extractor
=====================

This Python script extracts the Title and hierarchical Headings (H1, H2, H3) from PDF files and saves the results in a structured JSON format.

-----------------------
📁 Project Structure:
-----------------------

pdf_outline_extractor/
├── main.py               -> Main script
├── requirements.txt      -> Python dependencies
├── input/                -> Place your PDF files here
│   └── sample.pdf
├── output/               -> JSON results will be saved here

-----------------------
🚀 How to Run:
-----------------------

1. Install Python (version 3.7 or higher)

2. Install required dependencies:
   pip install -r requirements.txt

3. Add your PDF(s) to the `input/` folder (up to 50 pages).

4. Run the script:
   python main.py

-----------------------
📤 Output Format:
-----------------------

For each PDF in `input/`, the script will create a `.json` file in the `output/` folder.

Example output:

{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "Applications", "page": 2 },
    { "level": "H3", "text": "AI in Healthcare", "page": 3 }
  ]
}

-----------------------
✅ Features:
-----------------------

- Supports PDF files with up to 50 pages
- Automatically detects Title and Headings based on font size
- Outputs a clean and structured JSON
- Works offline (no internet required)

Limitations:
- Does not support image-based PDFs (no OCR)
- Does not extract paragraphs, lists, or tables

-----------------------
🛠 Requirements:
-----------------------

- Python 3.7+
- pdfplumber

Install with:
pip install -r requirements.txt

-----------------------
📬 Support:
-----------------------

If you have any questions or issues, feel free to reach out at your.email@example.com

-----------------------
License:
-----------------------

This project is open-source and free to use under the MIT License.
