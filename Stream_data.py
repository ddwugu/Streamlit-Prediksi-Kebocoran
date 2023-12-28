import pickle
import streamlit as st

# Set background image
st.markdown(
    """
    <style>
        body {
            background-image: url('bg1.png');
            background-size: cover;
        }
    </style>
    """,
    unsafe_allow_html=True
)

Leak = pickle.load(open('Prediksi_Kebocoran_Pipa.sav', 'rb'))

# Judul Web
st.title('Finding Oil Losses Pertamina Field Jambi')

Titik_1_PSI = st.text_input('Input Pressure di titik 1 (PSI)')
Titik_2_PSI = st.text_input('Input Pressure di titik 2 (PSI)')

# Code prediction
suspect_loct = ''

# Tombol prediksi
if st.button('Prediksi Lokasi Kebocoran'):
    prediksi_lokasi = Leak.predict([[float(Titik_1_PSI), float(Titik_2_PSI)]])

    if prediksi_lokasi[0] == 0:
        suspect_loct = 'Tidak Terdapat Kebocoran'
    elif prediksi_lokasi[0] == 26.8:
        suspect_loct = 'Tidak Terdapat Fluida yang Mengalir'
    else:
        suspect_loct = f'Terjadi Kebocoran di titik {prediksi_lokasi[0]} KM'

    st.success(suspect_loct)
