import streamlit as st

st.set_page_config(page_title="첫 웹페이지", page_icon="🎉")

# 세션 상태 초기화
if "greeted" not in st.session_state:
    st.session_state.greeted = False

# 배경색과 글씨색 설정
st.markdown(
    """
    <style>
    .stApp {
        background-color: #001f3f;
        color: white;
    }

    h1, h2, h3, p, div, span {
        color: white;
    }

    .center-box {
        text-align: center;
        margin-top: 180px;
    }

    .big-text {
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 30px;
    }

    .stButton > button {
        background-color: white;
        color: #001f3f;
        font-size: 20px;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 28px;
        border: none;
    }

    .stButton > button:hover {
        background-color: #e6e6e6;
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 시작 화면
if not st.session_state.greeted:
    st.markdown(
        """
        <div class="center-box">
            <div class="big-text">👋 안녕하세요 😊</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("나도 인사하기"):
            st.session_state.greeted = True
            st.rerun()

# 축하 화면
else:
    st.balloons()

    st.markdown(
        """
        <div class="center-box">
            <div class="big-text">🎉 첫 웹페이지 제작을 축하해요! 🎉</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("돌아가기"):
            st.session_state.greeted = False
            st.rerun()
