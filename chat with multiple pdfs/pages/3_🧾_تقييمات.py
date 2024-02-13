import streamlit as st
import base64
import streamlit as st
import plotly.express as px


def form_pick_a_form():
    st.caption("يمكنك حل التقييم اكثر من مره")


def form_altqeyyem_1():
    st.subheader("التقييم 1")
    questions_altqeyyem_1 = [
        "حركة سياسية تدعو إلى إقامة دولة تجمعها روابط اللغة والتاريخ  يشير التعريف الي ؟",
    ]
    answers_altqeyyem_1 = {}
    
    for question in questions_altqeyyem_1:
        # Use st.markdown with HTML tags to set the font size
        st.markdown(f"<p style='font-size: 25px; direction: rtl;'>{question}</p>", unsafe_allow_html=True)
        
        choices = st.multiselect("اختر الإجابة", ["النازية", "الصهيونية", " القومية"])
        answers_altqeyyem_1[question] = choices
        
    return answers_altqeyyem_1

def form_altqeyyem_1_2():
    questions_altqeyyem_1_2 = [
        "أي الشخصيات التالية قاد المانيا نحو تحقيق وحدتها القومية ؟",
    ]
    answers_altqeyyem_1_2 = {}
    for question in questions_altqeyyem_1_2:
        st.markdown(f"<p style='font-size: 25px; direction: rtl;'>{question}</p>", unsafe_allow_html=True)
        choices = st.multiselect(question, ["هنوفر", "ميركل", " بسمارك"])
        answers_altqeyyem_1_2[question] = choices
    return answers_altqeyyem_1_2


def form_altqeyyem_1_3():
    questions_altqeyyem_1_3 = [
        "أي الدول التالية اتبعت نظام مبدأ العزلة المجيدة في القرن 19 الميالدي ؟",
    ]
    answers_altqeyyem_1_3 = {}
    for question in questions_altqeyyem_1_3:
        st.markdown(f"<p style='font-size: 25px; direction: rtl;'>{question}</p>", unsafe_allow_html=True)
        choices = st.multiselect(question, ["فرنسا", "بريطانيا", "المانيا"])
        answers_altqeyyem_1_3[question] = choices
    return answers_altqeyyem_1_3

def form_altqeyyem_1_4():
    questions_altqeyyem_1_4 = [
        "بم تفسر, سبقت بريطانيا الدول األوروبية في دخول ميدان الصناعة",
    ]
    answers_altqeyyem_1_4 = {}
    for question in questions_altqeyyem_1_4:
        st.markdown(f"<p style='font-size: 25px; direction: rtl;'>{question}</p>", unsafe_allow_html=True)
        choices = st.text_input("اكتب اجابتك هنا ")
        answers_altqeyyem_1_4[question] = choices
    return answers_altqeyyem_1_4

def form_altqeyyem_2():
    st.subheader("التقييم 2")
    questions_altqeyyem_2 = [
        "عقد مؤتمر دولي لمناقشة المسألة المصرية 1882 في مدينة",
    ]
    answers_altqeyyem_2 = {}
    for question in questions_altqeyyem_2:
        st.markdown(f"<p style='font-size: 25px; direction: rtl;'>{question}</p>", unsafe_allow_html=True)
        choices = st.multiselect(question, ["لندن", "اآلستانة", " برلين"])
        answers_altqeyyem_2[question] = choices
    return answers_altqeyyem_2


def form_altqeyyem_2_1():
    questions_altqeyyem_2_1 = [
        "زادت الديون المصرية في عهد كال من الخديوي سعيد و الخديوي ؟",
    ]
    answers_altqeyyem_2_1 = {}
    for question in questions_altqeyyem_2_1:
        st.markdown(f"<p style='font-size: 25px; direction: rtl;'>{question}</p>", unsafe_allow_html=True)
        choices = st.multiselect(question, ["فاروق", "توفيق", " إسماعيل"])
        answers_altqeyyem_2_1[question] = choices
    return answers_altqeyyem_2_1


def form_altqeyyem_2_2():
    questions_altqeyyem_2_2 = [
        "طبقة اجتماعية ظهرت في بريطانيا في القرن التاسع عشر ؟",
    ]
    answers_altqeyyem_2_2 = {}
    for question in questions_altqeyyem_2_2:
        st.markdown(f"<p style='font-size: 25px; direction: rtl;'>{question}</p>", unsafe_allow_html=True)
        choices = st.multiselect(question, ["البرجوازية", "العمال", " العامة"])
        answers_altqeyyem_2_2[question] = choices
    return answers_altqeyyem_2_2

def form_altqeyyem_2_3():
    questions_altqeyyem_2_3 = [
        "وضح اغفل مؤتمر في ينا رغبات الشعوب في حق تقرير المصير ؟",
    ]
    answers_altqeyyem_2_3 = {}
    for question in questions_altqeyyem_2_3:
        st.markdown(f"<p style='font-size: 25px; direction: rtl;'>{question}</p>", unsafe_allow_html=True)
        choices = st.text_input(question,"")
        answers_altqeyyem_2_3[question] = choices
    return answers_altqeyyem_2_3



def form_altqeyyem_2_4():
    questions_altqeyyem_2_4 = [
        "ما العالقة بين ازمة مراكش عام 1905م و مؤتمر الجزيرة الخضراء عام 1906م ؟",
    ]
    answers_altqeyyem_2_4 = {}
    for question in questions_altqeyyem_2_4:
        st.markdown(f"<p style='font-size: 25px; direction: rtl;'>{question}</p>", unsafe_allow_html=True)
        choices = st.text_input(question,"")
        answers_altqeyyem_2_4[question] = choices
    return answers_altqeyyem_2_4




def form_altqeyyem_3():
    st.subheader("التقييم 3")
    questions_altqeyyem_3 = [
        "س1",
        "س2",
        "س3",
    ]
    answers_altqeyyem_3 = {}
    for question in questions_altqeyyem_3:
        st.markdown(f"<p style='font-size: 25px; direction: rtl;'>{question}</p>", unsafe_allow_html=True)
        choices = st.multiselect(question, ["Choice 1", "Choice 2", "Choice 3"])
        answers_altqeyyem_3[question] = choices
    return answers_altqeyyem_3

df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
    st.markdown("<h1 style='text-align: center; color: white;'>التقييمات</h1>", unsafe_allow_html=True)
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



    form_choice = st.selectbox("قم باختيار تقييم", ["قم باختيار تقييم", "التقييم 1", "التقييم 2", "التقييم 3"])

    if form_choice == "قم باختيار تقييم":
        form_pick_a_form()
    elif form_choice == "التقييم 1":
        answers = form_altqeyyem_1()
        answers = form_altqeyyem_1_2()
        answers = form_altqeyyem_1_3()
        answers = form_altqeyyem_1_4()

    elif form_choice == "التقييم 2":
        answers = form_altqeyyem_2()
        answers = form_altqeyyem_2_1()
        answers = form_altqeyyem_2_2()
        answers = form_altqeyyem_2_3()
        answers = form_altqeyyem_2_4()

    elif form_choice == "التقييم 3":
        answers = form_altqeyyem_3()

    if form_choice != "قم باختيار تقييم":
        st.subheader("")
        for question, choices in answers.items():
            st.write('')

if __name__ == "__main__":
    main()
