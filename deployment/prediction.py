import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title='NBA Shot Prediction',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Load model
with open('model_dt.pkl', 'rb') as model_file:
    best_dt_model = pickle.load(model_file)

# Load data
df_inf = pd.read_csv('nba_shot.csv')

def run():
    # Header
    col1, col2, col3 = st.columns([1, 4, 1])  # Kolom tengah lebih besar agar judul seimbang

    with col1:
        st.image("nba.png", width=80)  # Gambar ikon kiri

    with col2:
        st.markdown("<h1 style='text-align: center;'>Input Data Untuk Di Predict</h1>", unsafe_allow_html=True)  # Judul di tengah

    with col3:
        st.image("nba.png", width=80)  # Gambar ikon kanan

    # Jika belum ada df_inf_new di session_state, buat DataFrame baru
    if "df_inf_new" not in st.session_state:
        st.session_state.df_inf_new = pd.DataFrame(columns=[
            'team_name', 'player_name', 'position_group', 'home_team', 'away_team',
            'action_type', 'shot_type', 'zone_name', 'zone_range',
            'loc_x', 'loc_y', 'shot_distance', 'quarter', 'mins_left', 'secs_left',
            'game_year', 'game_month', 'game_day'
        ])

    df_inf_new = st.session_state.df_inf_new  # Ambil DataFrame dari session_state

    # Input team_name
    team = st.selectbox('Team Name', df_inf['team_name'].unique())

    # Input player_name
    players = df_inf.loc[df_inf['team_name'] == team, 'player_name'].unique().tolist()
    player_name = st.selectbox("Player Name", players)

    # Input Position Group
    position_group = df_inf.loc[df_inf['player_name'] == player_name, 'position_group'].unique()
    position = st.radio("Position Group", position_group)

    # Input Home/Away
    home_or_away = st.radio("Ingin menjadikan team ini sebagai:", ["Home", "Away"])

    # Input tim lawan
    if home_or_away == "Home":
        away_team = st.selectbox("Pilih Away Team", df_inf.loc[df_inf['team_name'] != team, 'away_team'].unique())
        home_team = df_inf.loc[df_inf['team_name'] == team, 'home_team'].unique()[0]  
    else:
        home_team = st.selectbox("Pilih Home Team", df_inf.loc[df_inf['team_name'] != team, 'home_team'].unique())
        away_team = df_inf.loc[df_inf['team_name'] == team, 'away_team'].unique()[0] 

    # Input action_type
    action_type = st.selectbox('Action Type', df_inf['action_type'].unique())

    # Input shot_type
    shot_type = st.radio('Shot Type', df_inf['shot_type'].unique())

    # Input zone_name
    zone_name = st.radio('Zone Name', df_inf['zone_name'].unique())

    # Input zone_range
    zone_range = st.radio('Zone Range', df_inf['zone_range'].unique())

    # Input loc_x
    loc_x = st.number_input('Loc_x (min: -25, max: 25)', min_value=-25, max_value=25)

    # Input loc_y
    loc_y = st.number_input('Loc_y (min=0, max=94)', min_value=0, max_value=94 )

    # Input shot_distance
    shot_dist = st.number_input('Shot Distance (samakan dengan nilai y)', min_value=0, max_value=94)

    # Input quarter
    quarter = st.radio('Quarter', df_inf['quarter'].unique())

    # Input waktu tersisa
    mins = st.number_input('Minute Left', min_value=1, max_value=12)
    secs = st.number_input('Second Left', min_value=1, max_value=59)

    # Input tanggal pertandingan
    game_y = st.number_input('Game Year (minimal 2023)', min_value=2023)
    game_m = st.number_input('Game Month', min_value=1, max_value=12)
    game_d = st.number_input('Game Day', min_value=1, max_value=31)

    with st.form(key="form_input"):
        # Jika tombol submit ditekan, data akan disimpan ke DataFrame
        submit = st.form_submit_button("Submit")

        if submit:
            # Buat DataFrame baru dari inputan
            new_data = pd.DataFrame([{
                'team_name': team, 
                'player_name': player_name, 
                'position_group': position,  
                'home_team': home_team,
                'away_team': away_team, 
                'action_type': action_type,
                'shot_type': shot_type, 
                'zone_name': zone_name,  
                'zone_range': zone_range,
                'loc_x': loc_x, 
                'loc_y': loc_y, 
                'shot_distance': shot_dist, 
                'quarter': quarter, 
                'mins_left': mins, 
                'secs_left': secs,
                'game_year': game_y,
                'game_month': game_m,
                'game_day': game_d
            }])

            # Tambahkan data baru ke df_inf_new tanpa duplikasi
            df_inf_new = pd.concat([df_inf_new, new_data], ignore_index=True)

            # Simpan perubahan ke session_state
            st.session_state.df_inf_new = df_inf_new

    # Tampilkan DataFrame terbaru
    st.dataframe(df_inf_new)

    # Jika ada data, lakukan prediksi
    if not df_inf_new.empty:
        # Pastikan hanya menggunakan kolom yang sesuai dengan model
        num = ['loc_x', 'loc_y', 'shot_distance', 'quarter', 'mins_left', 'secs_left']
        cat_nom = ['team_name', 'player_name', 'position_group', 'home_team', 'away_team', 'action_type', 'shot_type', 'zone_name']
        cat_ord = ['zone_range']

        # Pastikan semua kategori dikonversi ke tipe yang sesuai sebelum prediksi
        for col in cat_nom + cat_ord:
            df_inf_new[col] = df_inf_new[col].astype(str)

        # Lakukan prediksi
        prediction = best_dt_model.predict(df_inf_new)

        st.write('# Predicted Shot Success: ', str(int(prediction)))

    st.image('nba_team.png',use_container_width=True)

if __name__ == '__main__':
    run()
