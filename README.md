# 🎓 AI Powered Data Science Tutor

This is a **Streamlit** web application that serves as an **AI-powered tutor** for **Data Science**, using **Google Gemini API** and **LangChain**.

## 🚀 Features
- **Interactive AI Tutor**: Provides answers to Data Science-related queries.
- **Chat History Storage**: Uses SQLite to store chat messages.
- **Secure API Key Handling**: API key is stored securely using Streamlit Secrets.
- **User Session Management**: Unique session handling for users.

---

## 📚 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
# Activate environment
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Setup
1. Create a **.streamlit** directory in your project root.
2. Inside **.streamlit**, create a file named `secrets.toml`.
3. Add the following content:

```toml
[API]
API_KEY = "your-google-gemini-api-key"
```

4. Ensure the file is **ignored in version control** (`.gitignore` should include `.streamlit/secrets.toml`).

---

## 📱 Running the Application
```bash
streamlit run app.py
```

---

## 📝 Deployment
### Deploy on **Streamlit Cloud**
1. Push your project to **GitHub**.
2. Go to **Streamlit Cloud**: [https://share.streamlit.io](https://share.streamlit.io)
3. Connect your repository and set **secrets** in the Streamlit Cloud settings.

---

## 🔧 Technologies Used
- **Python**
- **Streamlit**
- **Google Gemini API**
- **LangChain**
- **SQLite** (for chat history)

---

## 🌟 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📖 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

