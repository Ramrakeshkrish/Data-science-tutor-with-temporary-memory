# Data-science-tutor-with-temporary-memory

 # 🎓 AI Powered Data Science Tutor

This is a **Streamlit** web application that serves as an **AI-powered tutor** for **Data Science**, using **Google Gemini API** and **LangChain**.

## 🚀 Features
- **Interactive AI Tutor**: Provides answers to Data Science-related queries.
- **Chat History Storage**: Uses SQLite to store chat messages.
- **Secure API Key Handling**: API key is stored securely using Streamlit Secrets.
- **User Session Management**: Unique session handling for users.

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository

2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

🔑 Setup API Key (Secure Method)

Create a .streamlit/secrets.toml file in the repository directory:
mkdir -p ~/.streamlit
nano ~/.streamlit/secrets.toml

add following content in the file
[API]
API_KEY = "your-api-key-here"
