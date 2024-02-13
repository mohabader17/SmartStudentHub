import streamlit as st
import sqlite3

import base64
import streamlit as st
import plotly.express as px

df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Create a SQLite database connection
conn = sqlite3.connect('chat_app.db')
c = conn.cursor()

# Create a table to store messages
c.execute('''
          CREATE TABLE IF NOT EXISTS messages (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              sender TEXT NOT NULL,
              message TEXT NOT NULL,
              timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
          )
          ''')
conn.commit()

# Streamlit app
def main():
    st.markdown("<h1 style='text-align: center; color: white;'>الدردشه</h1>", unsafe_allow_html=True)
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


    st.markdown("<div dir='rtl'><h1>منتدى المدرسة</h1></div>", unsafe_allow_html=True)

    #st.markdown("<div dir='rtl'><h1 style='font-size: 20px;'>قم بكتابة اسمك</h1></div>", unsafe_allow_html=True)

    user_name = st.text_input("قم بكتابة اسمك", "مستخدم")

    # Display chat messages
    display_messages()

    # Input box for sending messages
    message = st.text_area("قم بكتابة رسالتك هنا", key="message_input")
    if st.button("ارسال"):
        send_message(user_name, message)
        st.experimental_rerun()

    # Button to clear messages
    if st.button("مسح الرسائل"):
        clear_messages()
        st.experimental_rerun()

# Function to display chat messages
def display_messages():
    messages = get_messages()
    for msg in messages:
        st.write(f"{msg[1]}: {msg[2]}")

# Function to retrieve messages from the database
def get_messages():
    c.execute("SELECT * FROM messages")
    return c.fetchall()

# Function to send a message and update the database
def send_message(sender, message):
    if message:
        c.execute("INSERT INTO messages (sender, message) VALUES (?, ?)", (sender, message))
        conn.commit()

# Function to clear messages from the database
def clear_messages():
    c.execute("DELETE FROM messages")
    conn.commit()
    st.success("تم مسح الرسائل بنجاح.")

if __name__ == "__main__":
    main()
