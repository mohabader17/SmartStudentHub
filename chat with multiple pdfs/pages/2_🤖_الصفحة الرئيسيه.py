import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from htmlTempletes import css, bot_template, user_template
import base64
import streamlit as st
import plotly.express as px

df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()




def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader =  PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()

    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    
    return chunks
       

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory

    )
    return conversation_chain

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
            
load_dotenv()
img = get_img_as_base64("logo.jpg")
img2 = get_img_as_base64("logo2.jpg")

img = get_img_as_base64("logo.jpg")

page_bg_img_and_color = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:logo.jpg;base64,{img}");
    background-size: 100%;
    background-position: center;
    background-repeat: repeat;
    background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
    background: rgb(33,33,33);
    background: linear-gradient(239deg, rgba(33,33,33,1) 0%, rgba(112,109,109,1) 83%);    background-repeat: repeat; 
    background-attachment: local;
    }}  


[data-testid="stHeader"] {{
    background: rgba(0, 0, 0, 0);
}}

[data-testid="stToolbar"] {{
    right: 2rem;
}}

/* Responsive design for small screens */
@media only screen and (max-width: 600px) {{
    [data-testid="stAppViewContainer"] > .main {{
        background-size: cover;
    }}

    [data-testid="stSidebar"] > div:first-child {{
        background-size: 100%;
    }}
}}
</style>
"""

st.markdown(page_bg_img_and_color, unsafe_allow_html=True)


#st.set_page_config(page_title="المجيب الذكي", page_icon=":books:", layout="wide")
st.write(css, unsafe_allow_html=True)

if "conversation" not in st.session_state:
        st.session_state.conversation = None

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = None

    # Use HTML and CSS for right-to-left text direction
st.markdown('<div style="direction: rtl; text-align: right;">'
                '<h1> المجيب الذكي لتساؤلات الطلاب 📚</h1></div>',
                unsafe_allow_html=True)

user_question = st.text_input(label="", value="", key="question", help=":قم بطرح سؤالك عن مادة التاريخ هنا")
st.markdown(
    """
    <style>
        input {
            direction: rtl;
            text-align: right;
        }
    </style>
    """,
    unsafe_allow_html=True
        )
if not user_question or st.session_state.conversation is None:
        # Automatically start the service if there is no user input or conversation is not initiated
        with st.spinner("جاري المعالجه"):
            # 1) Get PDF Text
            pdf_url = "/Users/moha./Documents/project /chat with multiple pdfs/كتاب التاريخ 12 .pdf"            
            # 2) Get the text chunks
            text_chunks = get_text_chunks(pdf_url)
            # 3) Create vector store
            vectorstore = get_vectorstore(text_chunks)
            # 4) Create conversation chain
            st.session_state.conversation = get_conversation_chain(vectorstore)

if user_question:
        handle_userinput(user_question)






#st.set_option('client.showErrorDetails', False)




