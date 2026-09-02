import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Rule-Based Chatbot",
    page_icon="🤖",
    layout="centered"
)

def chatbot_response(user_input):
    text = user_input.lower().strip()

    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello! 👋 How can I help you today?"
    elif "your name" in text or "who are you" in text:
        return "I am a simple Rule-Based Chatbot 🤖."
    elif "how are you" in text:
        return "I'm doing great! 😊 Thanks for asking."
    elif "help" in text:
        return ("Sure! I can answer basic questions about myself. "
                "Try asking: 'What is your name?' or 'How are you?'")
    elif "time" in text:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}. ⏰"
    elif "date" in text or "today" in text:
        current_date = datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {current_date}. 📅"
    elif "thank" in text:
        return "You're welcome! 😊"
    elif any(word in text for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! 👋 Have a great day!"
    else:
        return ("Sorry, I don't understand that yet. 😕 "
                "Please try asking something like 'Hello', "
                "'What is your name?', or 'How are you?'")

st.title("🤖 Rule-Based Chatbot")
st.write(
    "A simple chatbot using predefined rules, "
    "if-else statements, and keyword matching."
)
st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    response = chatbot_response(user_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    st.rerun()

if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()