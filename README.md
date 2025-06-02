# 🦇 BatComputer

A local voice-enabled AI assistant inspired by the BatComputer. This project uses JavaScript for voice UI, Python Flask for backend logic, and a local LLM (Mistral via [Ollama](https://ollama.com/)) to respond to user questions without needing the cloud.

You can try out the live frontend here:  
🔗 **[https://batcomputer-flame.vercel.app](https://batcomputer-flame.vercel.app)**  
> Note: The assistant requires a running backend and Ollama server. Without it, prompts will not be processed.

---

## 🌐 Features

- Ask questions by typing or saying “Computer …”  
- Get spoken and visual responses using Web Speech API  
- Local large language model via Ollama (no OpenAI key required)  
- Stylish Batman-themed interface (SVG + custom CSS)  
- Google search fallback for unsupported prompts  
- Done and Mute controls  
- Hosted frontend publicly via Vercel

---

## 🧠 Tech Stack

| Layer       | Tools/Frameworks |
|-------------|------------------|
| Frontend    | HTML5, CSS3, Bootstrap, JavaScript (DOM) |
| Voice       | Web Speech API (SpeechRecognition + SpeechSynthesis) |
| Backend     | Python, Flask, Flask-CORS |
| LLM         | Mistral via Ollama (`http://localhost:11434`) |
| Dev Tools   | Vercel, Live Server (VSCode), Git/GitHub, Python `venv` |

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
```

---

## 🚀 Setup Instructions

### 1. Activate Python virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 2. Install Flask Dependencies
```bash
pip install flask flask-cors requests
```

### 3. Install and Run Ollama
```bash
brew install ollama         # macOS (or download from https://ollama.com)
ollama serve
ollama run mistral          # Downloads Mistral LLM and runs it locally
```

### 4. Run the Flask Backend
```bash
python main.py
```

---

## 🗺️ **Deployment Notes**

The frontend is deployed on Vercel at:  
🔗 [https://batcomputer-flame.vercel.app](https://batcomputer-flame.vercel.app)

The backend (`main.py`) and Ollama must be running locally for full functionality.

If you want global access to the assistant, consider deploying the Flask + Ollama backend to a public server and update `main.js` with your public backend URL.

---

## 📸 **Screenshots**

#### 🔧 Main Hub  
<img width="749" alt="Main Hub" src="https://github.com/user-attachments/assets/d78e656f-113a-4fb2-ae5a-c5a0c6ee0637" />

#### 🦇 Batcomputer Demo  
<img width="749" alt="Batcomputer Demo" src="https://github.com/user-attachments/assets/5a444080-efe2-437c-add9-f4f3956fcd33" />

#### 🧑‍💻 Batman Personalization  
<img width="755" alt="Batman Personalization" src="https://github.com/user-attachments/assets/fe8fdc45-2bfd-4aea-b7f5-8bafc46b60b0" />
