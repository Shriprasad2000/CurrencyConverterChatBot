# CurrencyConverterChatBot

### Overview
This project is a Chatbot built using Flask and Dialogflow, hosted on Render, and integrated with Telegram. The chatbot's primary function is to convert currency rates between different units and also engage in basic conversations with users. The project was developed for learning purposes and gaining hands-on experience in chatbot development and deployment.

### Features
- Chatbot built using **Dialogflow** (Google's NLU platform).
- **Flask** backend to handle webhook requests.
- Currency conversion using Exchange Rate API.
- Hosted on **Render** for public access.
- Integrated with **Telegram** Bot for live interaction.

## Tech Stack
- **Backend:** Flask (Python)
- **AI/NLP:** Dialogflow
- **Messaging Platform:** Telegram
- **Deployment:** Render

---

## Development Phase
1. **Set up Flask project** and run it on `localhost:5000`.
2. **Dialogflow runs online**, so local Flask needs to be accessible.
3. Use **Cloudflare Tunnel** to make the Flask app publicly accessible.
4. **Steps to use Cloudflare Tunnel:**
   - Download `cloudflared.exe` from [Cloudflare GitHub Releases](https://github.com/cloudflare/cloudflared/releases).
   - Move it to `C:\Windows\System32`.
   - Run:
     ```sh
     cloudflared tunnel --url http://localhost:5000
     ```
   - Copy the generated **public URL** and add it to **Dialogflow Webhook** settings.

---

## Telegram Bot Integration
1. Open Telegram and search for **BotFather**.
2. Use `/newbot` to create a bot.
3. Set a **bot name** and **username (must end in 'bot')**.
4. Copy the **API Token** provided.
5. In **Dialogflow > Integrations**, select **Telegram** and paste the API Token.

Now, the chatbot is live on Telegram!

---

## Deployment on Render
Before hosting:
1. Install `gunicorn`:
   ```sh
   pip install gunicorn
   ```
2. Create `requirements.txt`:
   ```sh
   pip freeze > requirements.txt
   ```
3. Create `Procfile` with content:
   ```
   web: gunicorn app:app
   ```
4. Create `runtime.txt` with Python version:
   ```
   python-3.11
   ```

### Hosting Steps:
1. Push your project to **GitHub**.
2. Log in to **Render** and select your GitHub repo.
3. Set a name for your service.
4. Add **start command**: `gunicorn app:app`.
5. Deploy using **free plan**.
6. Copy the **Render URL** and update **Dialogflow Webhook URL**.

---

## Working with Dialogflow
1. **Create an agent** and set up **intents**.
2. Add **training phrases** to map user queries.
3. Define **responses** to return chatbot replies.
4. Enable **Small Talks** for a conversational experience.
5. Set up **entities** (e.g., `currency-name`, `unit-currency`).
6. Test queries using **"Try it out"** in Dialogflow.

Now, your chatbot is fully functional and hosted!

---

## Summary
✅ **Local Development** → Flask + Cloudflare Tunnel  
✅ **Dialogflow Integration** → Webhook URL setup  
✅ **Telegram Bot** → Hosted on Telegram using API Token  
✅ **Deployment** → Hosted on **Render**  
