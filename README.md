# Decision-making-AI-chatbot
Decision making assistant an AI chatbot which helps user to make decision
Decision-Making Assistant – An AI Chatbot for Smarter Choices
Description
The Decision-Making Assistant is an AI-powered chatbot designed to help users make better, more thoughtful decisions by engaging in interactive conversations. Whether it's choosing a career path, selecting between products, managing time, or making everyday personal decisions, this tool assists users in organizing their thoughts and reaching logical conclusions.

The assistant works by asking guided questions, analyzing priorities, weighing pros and cons, and simulating outcomes. Its goal is not to make the decision for the user, but to support the user’s thought process and reduce decision fatigue.

Features
🧠 Smart Conversations: Understands user queries using natural language processing.

⚖️ Pros and Cons Analysis: Helps weigh the advantages and disadvantages of each option.

🎯 Priority-Based Suggestions: Considers user-defined criteria such as urgency, cost, interest, or long-term impact.

🔄 Scenario Simulation: Imagines possible outcomes based on user preferences.

📝 Multi-Option Evaluation: Handles decisions involving more than two options.

📊 Summary View: Provides a clear overview to aid final decision-making.

Tech Stack
Frontend: Gradio – for interactive web UI.
Demo Youtube link - (https://youtu.be/hUw3_zXtZF4?si=pyA2xXc3PhZRkdmQ)

Backend: Python

AI/ML Model: Replicate API (using an open-source language model)

Hosting: Can be run locally or deployed on platforms like Hugging Face Spaces or Replit.

Optional Tools: Pandas (for decision tables), Langchain (for chaining prompts), dotenv (for API key management)

How to Run
🛠️ Prerequisites
Python 3.8+

Replicate account and API key

Basic knowledge of virtual environments (optional but recommended)

📦 Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/your-username/decision-making-assistant.git
cd decision-making-assistant

# Install dependencies
pip install -r requirements.txt
🔑 Add Your Replicate API Key
Create a .env file in the project root:

ini
Copy
Edit
REPLICATE_API_TOKEN=your_replicate_api_key_here
▶️ Run the App
bash
Copy
Edit
python app.py
The Gradio interface will launch in your browser where you can start chatting with the AI.
