# 🤖 Local AI Chatbot using LangChain, Ollama & Streamlit

A fully local chatbot built using:
- 🧠 LangChain for intelligent prompts
- 🧊 Ollama to run free local LLMs (Mistral, Llama3, etc.)
- 🖥️ Streamlit for simple web UI

> ✅ No OpenAI API needed  
> ✅ 100% offline chatbot  
> ✅ Fast, free, and easy to customize

---

## 🚀 Features

- Local LLMs using Ollama (`mistral`, `llama3`, etc.)
- LangChain-powered prompt management
- Beautiful UI with Streamlit
- Fully offline after model download
- No API keys or paid services required

---

## 📁 Project Structure

my-chatbot/
├── ollama.py # Main Streamlit file
├── requirements.txt # Python dependencies
├── venv
├── .exe
└── README.md # You're reading this


---

## 🛠️ Step-by-Step Installation (100% Local)

### 🔽 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ChatBot.git
cd ChatBot

💻 2. Install Conda (if not installed)
Download Miniconda and install for your OS.

🧪 3. Create & Activate Virtual Environment
bash
Copy
Edit
conda create -n chatbot_env python=3.11 -y
conda activate chatbot_env
📦 4. Install Python Requirements
bash
Copy
Edit
pip install -r requirements.txt
Or install manually:

bash
Copy
Edit
pip install streamlit langchain python-dotenv requests
🤖 5. Install and Run Ollama
Ollama allows you to run open-source LLMs locally.

Download Ollama from: https://ollama.com/download

Install and open terminal, then run:

bash
Copy
Edit
ollama pull mistral
ollama run mistral
You can also use:

bash
Copy
Edit
ollama pull llama3
ollama run llama3
Leave Ollama running in a separate terminal window.

🌐 6. Run the Chatbot
In a new terminal window (in your project folder):

bash
Copy
Edit
streamlit run app.py
Open your browser and go to: http://localhost:8501

🔧 Optional .env Setup (If Used)
If your chatbot.py or app.py uses environment variables:

Create a file named .env in the root folder.

Example content:

ini
Copy
Edit
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_PROJECT="MyLocalChatbot"

---

## 📚 Credits

This project is inspired by the YouTube tutorial:  
📺 [LangChain Chatbot using Ollama and Streamlit - Full Build] https://youtu.be/qYq5xQ6pE_Q?si=SAdZ8eElyGUDAXaf 
Created by **Krish Naik Hindi** https://github.com/krishnaik06/Updated-Langchain

> This repository builds upon the ideas from the tutorial, with modifications and enhancements for learning and personal development purposes.

