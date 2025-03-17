import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
import uuid

# Load API key from Streamlit's secrets
api_key = st.secrets["API"]["API_KEY"]

# Initialize the Chat Model
chat_model = ChatGoogleGenerativeAI(api_key=api_key, model="models/gemini-1.5-pro")

# Streamlit UI
st.set_page_config(page_title="Data Science Tutor", layout="wide")
st.title('🎓 AI Powered Data Science Tutor')

query = st.text_area(label='Enter the query', placeholder='Explain the topics related to data science')
submit = st.button('Submit')

# Initialize session ID
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Function to retrieve chat history from SQLite database
def get_message_from_history():
    chat_history = SQLChatMessageHistory(
        session_id=st.session_state.session_id,
        connection="sqlite:////Users/jrudram/Downloads/raksenv/intership/my_database.db"
    )
    return chat_history

# Handling user query submission
if submit:
    if not query.strip():
        st.error("Please enter a query.")
    else:
        # Creating Chat Template
        chat_template = ChatPromptTemplate(messages=[
            ("system", """You are an AI Tutor specializing in Data Science.
                          Your role is to assist students by answering their questions in detail,
                          providing clear explanations with examples.
                          If a student asks a question outside Data Science, politely guide them to relevant topics."""),
            MessagesPlaceholder(variable_name='history'),
            ("human", """{human_input}""")
        ])

        # Creating Chat Model
        chat_model = ChatGoogleGenerativeAI(api_key=api_key, model="models/gemini-1.5-pro")

        # Creating Output Parser
        output_parser = StrOutputParser()

        # Combining all components into a processing chain
        chain = chat_template | chat_model | output_parser

        # Managing message history
        chaining = RunnableWithMessageHistory(
            chain,
            get_message_from_history,
            input_messages_key="human_input",
            history_messages_key="history"
        )

        # Session Configuration
        user_id = st.session_state.session_id
        config = {"configurable": {"session_id": user_id}}
        human_input = {"human_input": query}

        # Generating and displaying response
        response = chaining.stream(human_input, config=config)
        st.write(response)