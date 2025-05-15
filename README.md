# 🤖 WhatsApp AI Bot

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-Automation-brightgreen?style=flat-square&logo=selenium)
![Groq API](https://img.shields.io/badge/Groq%20API-AI%20Assistant-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)

> A real-time WhatsApp automation bot powered by Selenium and Groq API.  
> Automatically replies to text-based queries using an AI-powered assistant.

---

## ✨ Features

- ✅ Automates WhatsApp Web using Selenium
- 🧠 Integrates with Groq API for intelligent AI responses
- 📨 Responds only to text-based messages
- 🛡 Ignores images, videos, and non-text media
- 🚀 Lightweight and easy to set up

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/momina02/whatsapp-ai-bot.git
cd whatsapp-ai-bot
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

### 4. Run the Bot

```bash
python main.py
```

Use WhatsApp Web QR code to log in via your browser window that Selenium opens.

---

## 📦 Tech Stack

* **Python 3.10+**
* **Selenium**
* **Groq API**
* **dotenv**

---

## 🛑 Limitations

* Only responds to plain **text messages**
* Does not support media responses (e.g., images, videos, stickers)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

1. Fork the repo
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -m 'add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request 🚀

---

## 📬 Contact

Have questions or feedback? Reach out!
