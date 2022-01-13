import streamlit as st
import time

st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'


latest_literation = st.empty()
bar = st.progress(0)


for i in range(100):
    latest_literation.text(f'Interation{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!'


left_column, righta_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    righta_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
