# -*- coding: utf-8 -*-
"""Wanshouxigong1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WQMymU8isMe_B9zL8u4HazrIUG3uDWhG
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
def load_data():
    df = pd.read_csv("/content/PRSA_Data_Wanshouxigong_20130301-20170228.csv")
    return df

df = load_data()

# Sidebar
st.sidebar.title("Menu")
option = st.sidebar.radio("Pilih Pertanyaan:", ["Jenis Polusi Udara yang Paling Tinggi yang Mencemari Kota Wanshouxigong", "Trend Suhu Udara dan Dew Point", "Korelasi Dew Point dan Suhu Udara"])

# Main content
st.title("Air Quality in Wanshouxigong")

if option == "Jenis Polusi Udara yang Paling Tinggi yang Mencemari Kota Wanshouxigong":
    st.header("Rata-rata Jumlah Polusi Udara dalam 5 Tahun")
    air_polution = df.groupby('year').agg({
            "PM2.5" : "mean",
            "PM10" : "mean",
            "SO2" : "mean",
            "NO2" : "mean",
            "CO" : "mean",
            "O3" : "mean"}).mean()
    air_polution = air_polution.drop(columns=['year'])
    fig, ax = plt.subplots(figsize=(10, 5))
    air_polution.plot(kind='bar', color='purple', ax=ax)
    plt.xlabel('Jenis Polusi Udara')
    plt.ylabel('Nilai rata-rata')
    st.pyplot(fig)

    # Conclusion
    st.header("Kesimpulan")
    st.markdown("""
    Terdapat 6 jenis polusi udara, yaitu PM2.5, PM10, SO2, NO2, CO dan O3. Dari keenam jenis tersebut, jenis polusi udara yang paling tinggi mencemari kota Wanshouxigong adalah CO. Hal ini dapat terlihat dari nilai rata-rata selama 5 tahun bahwa terdapat konsentrasi CO paling tinggi mencemari udara.
    """)

elif option == "Trend Suhu Udara dan Dew Point":
    st.header("Trend Suhu dan Dew Point Selama 5 Tahun")
    temp_dewp = df.groupby('year')[['TEMP', 'DEWP']].mean()
    fig, air = plt.subplots(figsize=(10, 5))
    for column in temp_dewp.columns:
        air.plot(temp_dewp.index, temp_dewp[column], label=column, marker='o')
    plt.xlabel('Tahun')
    plt.ylabel('Nilai rata-rata')
    plt.legend()
    st.pyplot(fig)

    # Conclusion
    st.header("Kesimpulan")
    st.markdown("""
    Trend perubahan suhu udara dan dew point di kota Wanshouxigong cenderung stabil setiap tahunnya, kecuali pada tahun 2017 dimana suhu dan dew point mengalami penurunan yang cukup drastis. Dapat terlihat juga pada grafik bahwa trend suhu dan dew point memiliki trend yang sangat mirip.
    """)

else:
    st.header("Dew Point vs Suhu Udara")
    dewpoint_suhu = df[['TEMP', 'DEWP']].copy()
    corr = dewpoint_suhu.corr(method="pearson")
    st.write("Nilai Korelasi:", corr)
    st.subheader("Scatter Plot Dew Point vs Suhu Udara")
    plt.figure(figsize=(10, 5))
    plt.scatter(df['TEMP'], df['DEWP'], color="skyblue", marker='o', s=5, alpha=0.5)
    plt.plot([df['TEMP'].min(), df['TEMP'].max()], [df['DEWP'].min(), df['DEWP'].max()], color='grey', linestyle='--')
    plt.xlabel("Suhu Udara")
    plt.ylabel("Dew Point")
    plt.title("Dew Point vs Suhu")
    st.pyplot(plt)
    st.subheader("Heatmap Korelasi Dew Point dan Suhu Udara")
    sns.heatmap(corr, vmax=1, vmin=-1, center=0, cmap="plasma")
    st.pyplot()

    # Conclusion
    st.header("Kesimpulan")
    st.markdown("""
    Suhu dan dew point memiliki tingkat korelasi yang tinggi dengan nilai korelasi 0.818, dimana artinya suhu udara dan dew point berkaitan dan saling mempengaruhi satu sama lain.
    """)

