# 🦇 BatComputer

A local voice-enabled AI assistant inspired by the BatComputer. This project uses JavaScript for voice UI, Python Flask for backend logic, and a local LLM (Mistral via [Ollama](https://ollama.com/)) to respond to user questions without needing the cloud.

---

## 🌐 Features

- Ask questions by typing or saying “Computer …”  
- Get spoken and visual responses using Web Speech API  
- Local large language model via Ollama (no OpenAI key required)  
- Stylish Batman-themed interface (SVG + custom CSS)  
- Google search fallback for unsupported prompts  
- Done and Mute controls

---

## 🧠 Tech Stack

| Layer       | Tools/Frameworks |
|-------------|------------------|
| Frontend    | HTML5, CSS3, Bootstrap, JavaScript (DOM) |
| Voice       | Web Speech API (SpeechRecognition + SpeechSynthesis) |
| Backend     | Python, Flask, Flask-CORS |
| LLM         | Mistral via Ollama (`http://localhost:11434`) |
| Dev Tools   | Live Server (VSCode), Git/GitHub, Python `venv` |

---

## 📁 Project Structure

```plaintext
BatComputer/
├── engine/
├── node_modules/
├── venv/
│   ├── bin/
│   ├── lib/
│   ├── include/
│   ├── .gitignore
│   └── pyvenv.cfg
├── www/
│   ├── assets/
│   │   └── vendore/
│   │       └── batman-svgrepo-com.svg
│   ├── index.html
│   ├── main.js
│   └── style.css
├── .env
├── main.py
└── README.md


Activate python virtual environment:
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install Flask Dependencies:
pip install flask flask-cors requests

Install and RUN Ollama:
brew install ollama         # macOS (or download from https://ollama.com)
ollama serve
ollama run mistral          # Downloads Mistral LLM and runs it locally

Run the flask backend:
python main.py

Open Index.html or Live Server
