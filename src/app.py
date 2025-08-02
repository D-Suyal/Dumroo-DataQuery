import streamlit as st
import pandas as pd
from utils.api import get_api_key
from utils.llm import load_llm, create_agent
from utils.chat import init_session_state, displayChatHistory, displayChat, add_to_chat_history, get_context
from utils.roles import filter_dataframe_by_role, ROLE_DATA
from io import StringIO

def main():
    st.set_page_config(page_title="Dumroo.ai - Data Query")
    st.header("Data Query for Dumroo Admins")

    get_api_key()

    role_options = list(ROLE_DATA.keys())
    role_options = [k for k in ROLE_DATA.keys() if k != "dumroo_assistant"]

    selected_role = st.selectbox(
        "Select Your Role",
        options=role_options,
        format_func=lambda x: f"{ROLE_DATA[x]['avatar']} {x.replace('_', ' ').title()}"
    )

    print(selected_role)

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    
    init_session_state()
    displayChatHistory()

    if csv_file is not None:
        df = pd.read_csv(csv_file)
        filtered_df = filter_dataframe_by_role(df, selected_role)

        csv_buffer = StringIO()
        filtered_df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        llm = load_llm()
        agent = create_agent(llm, csv_buffer)        
        if ques := st.chat_input("Ask a Question about your CSV:"):
            displayChat(selected_role, ques)
            add_to_chat_history(selected_role, ques)

            with st.spinner(text="In Progress..."):
                prompt = get_context()
                try:
                    response = agent.invoke(prompt)
                except ValueError:
                    response = {"output" : "Greetings! Ask questions specific to CSV file."}
                answer = response.get("output", "No answer returned.")
                displayChat("dumroo_assistant", answer)
                add_to_chat_history("dumroo_assistant", answer)
                

if __name__ == "__main__":
    main()
