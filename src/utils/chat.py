import streamlit as st
from utils.roles import get_avatar

sessionName = "messages"

def init_session_state():
    if sessionName not in st.session_state:
        st.session_state.messages = []

def displayChat(role, content):
    avatar = get_avatar(role)
    with st.chat_message(name=role, avatar=avatar):
        st.markdown(content)

def displayChatHistory():
    for message in st.session_state[sessionName]:
        with st.chat_message(message["role"], avatar = get_avatar(message["role"])):
            st.markdown(message["content"])

def add_to_chat_history(role, content):
    st.session_state[sessionName].append({"role" : role, "content" : content})

def remove_from_chat_history(idx):
    if 0 <= idx < len(st.session_state[sessionName]):
        st.session_state[sessionName].pop(idx)

def get_context(max_turns=5):

    history = st.session_state[sessionName][-max_turns:]

    context = "Based on given csv file, answer the following conversation:\n"
    context += "\n".join(
        f"{msg['role'].capitalize()}: {msg['content']}" for msg in history
    )
    context += "\nAssistant:"
    return f"{context}"