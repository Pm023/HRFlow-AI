# HRflow AI - Enterprise HR Document Automation Specialist

HRflow AI is a production-level, Python-based document generation platform designed to automate and streamline the creation of high-fidelity, legally appropriate corporate letters and certificates. 

By leveraging advanced Generative AI capabilities (Google Gemini) alongside 15+ years of HR best practices, HRflow AI enables human resource teams to instantly draft, customize, and print crucial employment documents.

---

## 🌟 Key Capabilities & Features

*   **Generative AI Document Engine**: Seamlessly integrated with Google Gemini AI to draft highly contextualized, professionally styled, and uniquely worded documents.
*   **Production-Grade Fallbacks**: Includes a robust library of high-end corporate templates developed by HR professionals to ensure flawless operation even in offline or API-limited environments.
*   **Glassmorphism UI**: A modern, responsive dark-mode dashboard tailored for a premium user experience.
*   **Real-Time Dynamic Preview**: Visualizes document updates instantly side-by-side with the configuration panel.
*   **Ready-to-Print**: Specifically structured with clean print stylesheets for precise A4 output (perfect margins, professional letterheads, and signatures).

---

## 🛠️ Supported Documents
HRflow AI currently automates several crucial corporate documents:
*   **Offer Letters** (detailed terms, compensation structure, and warm onboarding copy)
*   **Internship Certificates** (dedication, duration, and proactive contribution validation)
*   **Experience Certificates** (leadership, core competencies, and professional reference)
*   **Letters of Appreciation** (performance recognition and milestone achievements)
*   **Relieving Letters** (formal resignation acceptance and service period records)

---

## ⚙️ Tech Stack & Architecture

*   **Backend**: Python, FastAPI (High-performance, asynchronous REST framework)
*   **Server**: Uvicorn (ASGI web server implementation)
*   **Templating**: Jinja2 (Dynamic HTML rendering)
*   **AI Integration**: Google GenAI SDK (Gemini-1.5-Flash model)
*   **Frontend**: Vanilla HTML5, Modern CSS3 (Glassmorphism layout), and responsive Vanilla JavaScript.

---

## 🚀 Getting Started

### 1. Clone & Setup Environment
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

### 2. Configure API Credentials
Create a `.env` file in the root directory (using `.env.example` as a template) and add your Gemini API Key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Run the Production Server
Start the application using the runner script:
```bash
python main.py
```
Alternatively, launch it directly via Uvicorn:
```bash
python -m uvicorn app.main:app --port 8003 --reload
```

Open your browser and navigate to **[http://127.0.0.1:8003](http://127.0.0.1:8003)** to begin managing your HR workflows.
