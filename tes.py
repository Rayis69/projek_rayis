import streamlit as st

st.title("Contoh Program Bergizi gratis")
with st.form(key="my_form"):
    nama = st.text_input("Nama Lengkap")
    jenis_kelamin = st.radio("jenis kelamin", ("laki laki", "perempuan"))
    submit = st.form_submit_button(label="Kirim")