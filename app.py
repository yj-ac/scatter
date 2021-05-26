from PIL.Image import NONE
from numpy import short
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import streamlit as st
from streamlit.caching import cache

@cache
def create_plot_data(file,shohin_code):
    
    df = pd.read_csv(file,encoding='cp932')
    df = df[df['店舗']!='合計']
    df = df[df['売上金額']!=0]
    df['商品コード'] = df['商品コード'].astype('str').str.lstrip('4')
    
    df = df[df['商品コード']==shohin_code]
    
    x = df['平均単価']
    y = df['売上金額']
    
    return x,y,df
st.title('売上金額散布図')
df = st.file_uploader('ファイル選択',type='csv')

if df is not None:
    shohin_code = st.text_input('商品コードを入力',max_chars=6)
    if shohin_code is not '':
        x,y,df = create_plot_data(df,shohin_code)
        name = df[df['商品コード']==shohin_code]['商品名称'].iloc[1]

        fig = plt.figure(figsize=(12,9))
        plt.scatter(x,y)
        plt.xlabel('平均単価')
        plt.ylabel('売上金額')
        plt.title(name)

        st.pyplot(fig)


