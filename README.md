Perfect — here’s the **updated detailed README.md** with **Conda included properly**.
Everything is clean, accurate, and professional.

You can copy-paste this directly.

---

# 📄 Resume Skill Analyzer & PDF Text Extractor

A Python-based web application built using **Streamlit** that extracts text from resumes in PDF format and compares the extracted content with predefined skills to generate a resume matching score.

This project focuses on **PDF text extraction and keyword-based skill comparison**, making it suitable for learning resume parsing fundamentals.

---

## ✅ What This Application Does

* Upload resumes in **PDF format**
* Extract readable text from the resume
* Load required skills from a configuration file (`roles.txt`)
* Compare resume content with skill keywords
* Calculate a **skill match percentage**
* Display:

  * ✔ Found skills
  * ❌ Missing skills
* Generate downloadable files:

  * Extracted resume text (`.txt`)
  * Skill analysis report (`.txt`)
* Provide a clean and interactive web interface

---

## 🧠 How the System Works

```
1. Upload PDF resume
2. Extract text using pdfplumber
3. Convert text to lowercase
4. Load skills from roles.txt
5. Compare skills with resume content
6. Calculate matching percentage
7. Display results
8. Allow report downloads
```

---

## ⚠️ Supported Resume Types

This application works **only with text-based PDF files**, including:

* Microsoft Word–generated PDFs
* Google Docs–exported PDFs
* Digitally created resumes

---

### ❌ Not Supported

* Scanned image PDFs
* Photos of resumes
* Camera-captured documents
* Handwritten documents

These formats contain images instead of selectable text and cannot be processed correctly.

---

### 🔍 How to Check PDF Compatibility

Open the PDF and try selecting text:

* Text selectable → ✅ Supported
* Text not selectable → ❌ Not supported

---

## 📂 Project Structure

```
Resume Scorer/
│
├── resume.py                 # Main Streamlit application
├── roles.txt                 # Skills database
├── requirements1.txt         # Python dependencies
├── README.md                 # Documentation
│
└── .vscode/
    └── settings.json
```

---

## 📑 roles.txt Format

Skills are listed one per line and can be grouped by category.

Example:

```
=== WEB DEVELOPMENT ===
html
css
javascript
bootstrap
tailwind css
react
react.js
angular
vue
next.js
node.js
web development
```

---

## 🧰 Technologies Used

* Python 3.10+
* Streamlit
* pdfplumber
* PyPDF2
* Pillow
* NumPy
* Conda environment
* Temporary file handling

---

## 🧪 Environment Setup (Conda)

This project uses **Conda** for environment management.

---

### 1️⃣ Create Conda environment

```bash
conda create -n resume-scorer python=3.10
```

---

### 2️⃣ Activate environment

```bash
conda activate resume-scorer
```

---

### 3️⃣ Install required packages

```bash
pip install -r requirements1.txt
```

> pip is used inside the Conda environment.

---

## ▶️ Run the Application

```bash
streamlit run resume.py
```

---

## 🌐 Open in Browser

```
http://localhost:8501
```

---

## 📊 Output

* Resume match percentage
* Skills found in the resume
* Skills missing from the resume
* Downloadable extracted text file
* Downloadable analysis report

---

## 🧩 Notes

* Matching is **keyword-based**
* Accuracy depends on wording in resumes and skills file
* Best results with clean, digitally created resumes
  
---

