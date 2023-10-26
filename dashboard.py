import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
import numpy as np

sns.set(style='dark')

st.header('Proyek Analisis Bike Sharing Dataset :sparkles:')
st.subheader('By : Hilman Mauludin (Dicoding ID : hilmatrix)')
st.subheader('1. Visualisassi rata-rata pengguna sepeda untuk User Casual dan Registered tiap hari')

df = pd.read_csv('main_data.csv')

penggunaTiapHari=df.groupby("weekday")[["casual","registered"]].mean()

fig, ax = plt.subplots(figsize=(16, 8))

ax.plot(
    ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"],
    penggunaTiapHari["casual"],
    marker='o', 
    linewidth=2,
    color="blue"
)
ax.plot(
    ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"],
    penggunaTiapHari["registered"],
    marker='o', 
    linewidth=2,
    color="red"
)
ax.legend(["Casual","Registered"])
ax.set_ylabel("Rata-rata pengguna")

for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(24)

st.pyplot(fig)

############################################
st.subheader('2. Visualisassi penggunaan sepeda untuk User Casual di hari libur berdasarkan jam')

penggunaCasualLibur=df[df["holiday"]>0].groupby("hr")["casual"].mean()

fig, ax = plt.subplots(figsize=(16, 8))
ax.bar(
    range(0,24),
    penggunaCasualLibur,
    linewidth=2,
    color="blue"
)

ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata pengguna")

for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(24)

st.pyplot(fig)

############################################
st.subheader('3. Visualisassi pengaruh temperatur terhadap jumlah pengguna sepeda untuk User Casual dan Registered')

penggunaKondisiCuaca=df.groupby("atemp")[["casual","registered"]].mean()

fig, ax = plt.subplots(figsize=(16, 8))

ax.plot(
    penggunaKondisiCuaca["casual"],
    marker='o', 
    linewidth=2,
    color="blue"
)

ax.plot(
    penggunaKondisiCuaca["registered"],
    marker='o', 
    linewidth=2,
    color="red"
)

ax.set_xticks(np.arange(0,1.1,0.1), (np.arange(0,1.1,0.1)*66-16).round())

ax.legend(["Casual","Registered"])
ax.set_xlabel("Temperature yang dirasakan dalam Celcius")
ax.set_ylabel("Rata-rata pengguna")

for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
            ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(24)

st.pyplot(fig)

#import session_info
#session_info.show()