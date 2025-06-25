import streamlit as st
import pandas as pd

# --- アプリ設定 ---
st.set_page_config(
    page_title="インシデント報告システム",
    page_icon="🏥",
    layout="wide"
)

# --- データの初期化 ---
# session_stateにデータフレームがなければ作成する
# この処理はアプリの起動時に一度だけ行われる
if 'report_df' not in st.session_state:
    st.session_state.report_df = pd.DataFrame(columns=[
        "報告ID", "発生日時", "影響度レベル", "報告者", "職種", "発生場所", 
        "インシデント内容", "状況詳細", "今後の対策"
    ])

# --- トップページの表示 ---
st.title("🏥 インシデント報告システム")
st.markdown("---")
st.header("ようこそ！")
st.write("このシステムは、院内で発生したインシデント・アクシデントを報告・管理するためのものです。")
st.write("左のサイドバーからメニューを選択してください。")

st.subheader("現在の報告件数")
num_reports = len(st.session_state.report_df)
st.metric(label="総報告件数", value=f"{num_reports} 件")

st.info("👈 **サイドバーから操作を選択してください**", icon="ℹ️")