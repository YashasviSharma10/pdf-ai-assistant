# 📄 PDF AI Assistant

An AI-powered PDF Question Answering system built using **LangChain**, **Google Gemini**, and **Qdrant Vector Database**. The application allows users to ask natural language questions about a PDF document and retrieves accurate answers using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 📄 Load PDF documents
- ✂️ Split documents into semantic chunks
- 🧠 Generate embeddings using Google Gemini
- 🗄️ Store embeddings in Qdrant Vector Database
- 🔍 Perform semantic similarity search
- 💬 Answer user queries using Retrieval-Augmented Generation (RAG)
- 📍 Display relevant page numbers and source file information

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **Google Gemini API**
- **Qdrant Vector Database**
- **OpenAI Python SDK (Gemini Compatible Endpoint)**
- **PyPDF**
- **Docker**

---

## 📂 Project Structure

```text
pdf-ai-assistant/
│── chat.py                 # Chat interface
│── index.py                # PDF indexing
│── sample.pdf              # Sample PDF (Replace with your own PDF)
│── docker-compose.yml      # Qdrant setup
│── requirements.txt
│── .gitignore
│── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YashasviSharma10/pdf-ai-assistant.git
cd pdf-ai-assistant
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Start Qdrant

```bash
docker compose up
```

---

## 🔑 Configure Environment Variables

Create a `.env` file inside the project directory.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 📄 Add Your PDF

1. Place your PDF inside the project folder.
2. Rename it to:

```text
sample.pdf
```

or update the filename in `index.py`.

---

## 📥 Index the PDF

```bash
python index.py
```

---

## 💬 Start Chat

```bash
python chat.py
```

---

## 🧠 How It Works

```text
                    PDF
                     │
                     ▼
              PyPDFLoader
                     │
                     ▼
                 Chunking
                     │
                     ▼
        Gemini Embedding Model
                     │
                     ▼
      Qdrant Vector Database
                     │
                     ▼
          Semantic Search
                     │
                     ▼
          Retrieved Context
                     │
                     ▼
           Gemini 2.5 Flash
                     │
                     ▼
              Final Response
```

---

## 📌 Future Improvements

- 📤 Upload multiple PDF files
- 🌐 Streamlit Web Interface
- 💬 Chat History
- 📚 Source Citation
- 🧠 Conversation Memory
- ☁️ Cloud Deployment

---

## 👨‍💻 Author

**Yashasvi Sharma**

- GitHub: https://github.com/YashasviSharma10

---

⭐ If you found this project useful, consider giving it a star.