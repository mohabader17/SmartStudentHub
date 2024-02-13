import hashlib
import json
import sqlite3
from pathlib import Path

import pandas as pd
import streamlit as st
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
import base64
import streamlit as st
import plotly.express as px

df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

DEFAULT_PAGE = "1_login.py"
SECOND_PAGE_NAME = "Home"

def get_all_pages():
    default_pages = get_pages(DEFAULT_PAGE)

    pages_path = Path("pages.json")

    if pages_path.exists():
        saved_default_pages = json.loads(pages_path.read_text())
    else:
        saved_default_pages = default_pages.copy()
        pages_path.write_text(json.dumps(default_pages, indent=4))

    # Add "Home" to the list of available pages with a default icon and script_path
    saved_default_pages[SECOND_PAGE_NAME] = {
        "page_name": SECOND_PAGE_NAME,
        "icon": "⚙️",
        "script_path": "C:/Users/User/Desktop/project/chat with multiple pdfs/pages/2_🤖_الصفحة الرئيسيه.py",  # Replace with your actual script path
    }

    return saved_default_pages



def clear_all_but_first_page():
    current_pages = get_pages(DEFAULT_PAGE)

    if len(current_pages.keys()) == 1:
        return

    get_all_pages()

    key, val = list(current_pages.items())[0]
    current_pages.clear()
    current_pages[key] = val

    _on_pages_changed.send()

def show_all_pages():
    current_pages = get_pages(DEFAULT_PAGE)
    saved_pages = get_all_pages()

    for key in saved_pages:
        if key not in current_pages:
            current_pages[key] = saved_pages[key]

    _on_pages_changed.send()

def hide_page(name: str):
    current_pages = get_pages(DEFAULT_PAGE)

    for key, val in current_pages.items():
        if val["page_name"] == name:
            del current_pages[key]
            _on_pages_changed.send()
            break

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

conn = sqlite3.connect("user_data.db")
c = conn.cursor()

def create_usertable():
    c.execute("CREATE TABLE IF NOT EXISTS userstable(username TEXT,email TEXT, password TEXT)")

def add_userdata(username, email, password):
    c.execute("INSERT INTO userstable(username,email,password) VALUES (?,?,?)", (username, email, password))
    conn.commit()

def login_user(email, password):
    c.execute("SELECT * FROM userstable WHERE email =? AND password = ?", (email, password))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute("SELECT * FROM userstable")
    data = c.fetchall()
    return data

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

def main():
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


    st.title("!مرحبا")

    menu = ["تسجيل دخول", "انشاء حساب"]
    choice = st.selectbox("▾قم باختيار(تسجيل الدخول) او (انشاء حساب) ", menu)

    st.markdown("<h10 style='text-align: left; color: #ffffff;'> اذا لم تمتلك حساب، قم بإنشاء حساب</h10>", unsafe_allow_html=True)

    if choice == "":
        st.subheader("تسجيل دخول")
    elif choice == "تسجيل دخول":
        st.write("-------")
        st.subheader("تسجيل الدخول الى الموقع")

        email = st.text_input("الإيميل", placeholder="example@exapmle.com")
        password = st.text_input("كلمة المرور", type="password")

        if st.button("تسجيل دخول"):
            create_usertable()
            hashed_pswd = make_hashes(password)

            result = login_user(email, check_hashes(password, hashed_pswd))
            if result:
                st.session_state["logged_in"] = True
                st.success('تم تسجيل الدخول بنجاح')
            else:
                st.warning('الإيميل أو كلمة المرور غير صحيحة')
    elif choice == "SignUp":
        st.write("-----")
        st.subheader("Create New Account")
        new_user = st.text_input("Username", placeholder="name")
        new_user_email = st.text_input("Email id", placeholder="email")
        new_password = st.text_input("Password", type="password")

        if st.button("Signup"):
            if new_user == "" or new_user_email == "" or new_password == "":
                st.warning("يرجى ملء جميع الحقول")
            else:
                create_usertable()
                add_userdata(new_user, new_user_email, make_hashes(new_password))
                st.success("تم إنشاء حسابك بنجاح")
                st.info("انتقل للتسجيل دخول لحسابك")

    if st.session_state["logged_in"]:
        show_all_pages()
        hide_page(DEFAULT_PAGE.replace("C:/Users/User/Desktop/project/chat with multiple pdfs/pages/2_🤖_الصفحة الرئيسيه.py", ""))
        switch_page(SECOND_PAGE_NAME)
        st.subheader("User Profiles")
        user_result = view_all_users()
        clean_db = pd.DataFrame(user_result, columns=["Username", "Email", "Password"])
        st.dataframe(clean_db)
    else:
        clear_all_but_first_page()

if __name__ == "__main__":
    main()
