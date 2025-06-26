import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="運用ミス分析レポート", layout="wide")

# ↓ ここで Streamlit の余白背景を黒に上書き
st.markdown("""
<style>
/* アプリ全体の背景 */
.stApp {
    background-color: #1A1A2E !important;
}

/* メインコンテナ（余白含む）の背景＆パディング調整 */
.block-container {
    background-color: #1A1A2E !important;
    padding-top: 0;
    padding-bottom: 0;
}

/* サイドバーがある場合はこちらも */
.sidebar-content {
    background-color: #2A2A4A !important;
}
</style>
""", unsafe_allow_html=True)

# 既存の埋め込みコード
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()
components.html(html_content, height=3200, scrolling=True)
