import streamlit as st
import streamlit.components.v1 as components

# ページの設定
st.set_page_config(page_title="運用ミス分析レポート", layout="wide")

# HTMLの読み込み
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# HTMLを埋め込み（高さは必要に応じて調整）
components.html(html_content, height=3200, scrolling=True)
