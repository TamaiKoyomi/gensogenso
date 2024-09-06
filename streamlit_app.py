import streamlit as st
import pandas as pd
import numpy as np
import random

@st.cache
def load_data():
    return pd.read_excel("元素元素.xlsx")

words_df = load_data()

def decide():
    if st.button('シャッフル'):
        rarity_probs = {
            'N' : 0.4,
            'R' : 0.3,
            'SR': 0.2,
            'SSR' : 0.1
        }
        chosen_rarity = np.random.choice(list(rarity_probs.keys()),p = list(rarity_probs.values()))

        subset_df = words_df[words_df['レアリティ'] == chosen_rarity]
        selected_word = subset_df.sample.iloc[0]

        st.session_state.selected_word = selected_word
        st.session_state.display_meaning = False

def game():
    st.title('元素')
    st.write('シャッフルで元素シャッフルです。頑張ろう。間違っていたら適宜教えてください。')

    decide()

    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        if st.button('元素番号'):
            st.write(st.session_state.selected_word['元素番号'])
    with col2:
        if st.button('元素名'):
            st.write(st.session_state.selected_word['元素名'])
    with col3:
        if st.button('原子量')
            st.write(st.session_state.selected_word['原子量'])

game()