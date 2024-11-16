"""Streamlit main

起動コマンド: streamlit run app.py [-- script args]
"""

import pandas as pd
import requests
import streamlit as st


URL = "https://zipcloud.ibsnet.co.jp/api/search"


# 住所検索処理
def search_address(zipcode: int) -> dict:
    request_url = f"{URL}?zipcode={zipcode}"
    response = requests.get(request_url)

    return response.json()


# リクエスト送信画面の作成
st.title("住所検索アプリ at Streamlitやで")
st.header("住所検索")
zipcode = st.text_input(
    "検索したい郵便番号を入力してください。(半角数字のみ、ハイフン不要)"
)

is_post = st.button("検索")

# 検索処理実行
if is_post:
    response: dict = search_address(zipcode)
    df = pd.DataFrame(response)
    st.write(df)

# レスポンス結果画面
