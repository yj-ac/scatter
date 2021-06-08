from PIL.Image import NONE
from numpy import short
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import streamlit as st
from streamlit.caching import cache

@st.cache
def create_plot_data(file,code,select):

    df = pd.read_csv(file,encoding='cp932')
    df = df[df['店舗']!='合計']
    df = df[df[select]!=0]
    df['商品コード'] = df['商品コード'].astype('str').str[-6:]
    
    df = df[df['商品コード']==code]
    
    x = df['平均単価']
    y = df[select]
    
    return x,y,df
    
st.title(' 売上金額散布図')
df = st.file_uploader('ファイル選択',type='csv')
select = st.selectbox('選択',['売上金額','売上金額PI','売上数量'])

if df is not None:
    code = st.text_input('商品コードを入力:半角6桁',max_chars=6)
    if code is not '':
    #for code in ['194700', '087386']:
        x,y,df = create_plot_data(df,code,select)
        name = df[df['商品コード']==code]['商品名称'].iloc[1]
                
        fig = plt.figure(figsize=(12,9))
        plt.scatter(x,y)
        plt.xlabel('平均単価')
        plt.ylabel(select)
        plt.title(name)

        st.pyplot(fig)


