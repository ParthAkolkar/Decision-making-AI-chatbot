import gradio as gr
import google.generativeai as genai

# ✅ Configure API
genai.configure(api_key="AIzaSyBh9hvDRglbMRw4aa2K7nhuLyRQdClyWb4")

# ✅ Load the model
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# ✅ Assistant logic with error handling
def decision_assistant(message, history):
    try:
        prompt = f"""You are a friendly decision-making assistant. The user asked:
"{message}"
Give a thoughtful and concise suggestion that helps them make a decision."""
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# ✅ Custom CSS for UI/UX boost
css = """
#component-0 {font-family: 'Segoe UI', sans-serif ;}
footer {visibility: hidden;}
"""

# ✅ Interface with better UX
chatbot_ui = gr.ChatInterface(
    fn=decision_assistant,
    chatbot=gr.Chatbot(label="💬 Smart Decision-Making Assistant", show_copy_button=True),
    title="🤖 Smart Decision-Making Assistant",
    description="An AI assistant that helps you make thoughtful decisions. Powered by Gemini ✨",
    theme="soft",
    examples=["Should I choose biology or commerce?", "Pizza or burger?", "Study at night or morning?"],
    submit_btn="Ask 🚀",
    css=css
)

# ✅ Launch it
chatbot_ui.launch(share=True)
