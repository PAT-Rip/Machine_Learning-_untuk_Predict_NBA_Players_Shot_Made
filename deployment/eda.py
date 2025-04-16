import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.image as mpimg

def run():

    # Load data
    df = pd.read_csv('nba_shot.csv')
    
    # Title
    st.title('Aplikasi Prediksi NBA Player Shot Made')

    # membuat 2 kolom
    col_nba, col_data = st.columns([1,5])
    with col_nba:
        st.image('nba.png', width=80)
    
    with col_data:
        st.dataframe(df)

    # Membuat sub header
    st.subheader('1. Exploratory Dataset (EDA)')

    # EDA pertama
    st.write('### A. Stephen curry paling banyak mencetak 3pt atau 2 pt, dan dimanakah posisi terbaik dia dalam mencetak point?')
    #membuat 2 kolom
    col1, col2, col3 = st.columns([1,2,3])

    with col1:
        # load gambar
        st.image('steph.png', use_container_width=True)
    
    with col2:
        # Buat figure pertama (Pie Chart)
        count_shot = df[df['player_name'] == 'Stephen Curry']['shot_type'].value_counts()
        fig1, ax1 = plt.subplots(figsize=(2, 2)) 
        ax1.pie(count_shot, labels=count_shot.index, autopct='%1.1f%%', startangle=140, colors=['green', 'red'])
        ax1.set_title("Persentase Tipe Tembakan", fontsize=10, color="white")

        st.pyplot(fig1)
    
    with col3:
        # Buat figure kedua (Heatmap)
        court_img = mpimg.imread('basket_court.jpg')

        fig2, ax2 = plt.subplots(figsize=(2, 2))  # Ukuran yang sama agar proporsional
        plt.style.use('dark_background')

        ax2.imshow(court_img, extent=[-50, 50, -6, 50], aspect='auto')

        made_shots = df[(df['player_name'] == 'Stephen Curry') & (df['shot_made'] == 1)]
        sns.kdeplot(x=made_shots['loc_x'], y=made_shots['loc_y'], cmap="Reds", fill=True, thresh=0, alpha=0.6)

        ax2.set_title("Heatmap Lokasi Tembakan yang Berhasil - Stephen Curry", fontsize=10, color="white")
        ax2.set_xlabel("Posisi X (Lebar Lapangan)", fontsize=8, color="white")
        ax2.set_ylabel("Posisi Y (Panjang Lapangan)", fontsize=8, color="white")
        ax2.tick_params(colors="white")

        st.pyplot(fig2)
    
    # Conclusi EDA 1
    st.write('Dari piechart yang dibuat menunjukkan kalau Stephen curry lebih banyak mencetak 3pt dari pada 2pt dan dari heat map kita bisa lihat kalau posisi shot curry terbaik berada di bagian tengah 3pt field')

    #Membuat garis pemisah
    st.markdown("---") 

    # EDA ke 2
    st.write('### B. Berapa rata-rata point yang di raik oleh lebron james per game dan Tipe shot seperti apa yang sering digunakan oleh lebron james untuk mencetak point?')
    #membuat 2 kolom
    col_leb, col_leb_tab = st.columns([1,1])

    with col_leb:
        st.image('leb.png', use_container_width=True)
    
    with col_leb_tab:
        # Rata-rata point lebron james per game
        lj_avg = df[df['player_name'] == 'LeBron James'].groupby('game_id')['shot_type'].count().mean()
        st.write(f'Rata-rata point per game Lebron James: {round(lj_avg)}')

        # Best action_type lebron james dalam mencetak point
        lj_shot = df[(df['player_name'] == 'LeBron James') & (df['shot_made'] == 1)]['action_type'].value_counts()

        # Buat bar chart
        lj = plt.figure(figsize=(10, 6))
        lj_shot.plot(kind='barh', color='dodgerblue')

        plt.title("Jumlah Action Type LeBron James dalam Mencetak Poin")
        plt.xlabel("Action Type")
        plt.ylabel("Jumlah Shot Made")
        plt.xticks()
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        st.pyplot(lj)
    
    # Conclusi EDA 2
    st.write('Dari hasil di atas kita bisa menarik kesimpulan kalau Lebron James dalam 1 game rata-rata point yang dia buat adalah 18 dan jenis shot yang sering mendapatkan point adalah driving layup dan jump shot')

if __name__ == '__main__':
    run()