import streamlit as st
import pandas as pd
from db_utils import init_db # db_utilsからinit_dbをインポート

# --- DB初期化 ---
init_db() # アプリ起動時にテーブルを作成

# --- アプリ設定 ---
st.set_page_config(
    page_title="インシデント報告システム",
    page_icon="🏥",
    layout="wide"
)

# --- トップページの表示 ---
st.title("🏥 インシデント報告システム")
st.markdown("---")
st.header("ようこそ！")
st.write("このシステムは、院内で発生したインシデント・アクシデントを報告・管理するためのものです。")
st.write("左のサイドバーからメニューを選択してください。")
