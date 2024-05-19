import streamlit as st
import pickle
import re

# Case Folding dan Pembersihan Teks
def casefolding(text):
    text = text.lower()
    text = text.strip(" ")
    text = re.sub(r'(<[A-Za-z0-9]+>)|(#[A-Za-z0-9]+)|(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)',"",text)
    return text

# Tokenization
def token(komen):
    nstr = komen.split(" ")
    dat = []
    a = -1

    for karakter in nstr:
        a = a + 1

    if karakter == "":
        dat.append(a)

    p = 0
    b = 0

    for q in dat:
        b = q - p
        del nstr[b]
        p = p + 1

    return nstr

# Filtering
stopword = ["yaa", "aja", "yang", "dari", "adalah", "sih", "deh", "ya",
            "ciaaaa", "aja", "kok", "gitu", "ko", "wkwk", "gt",
            "sekarang", "udah", "sepertinya", "ini", "woy", "lah",
            "apasih", "plus", "kyk", "udh", "masih", "aj", "yg", "sekaligus",
            "sih", "kalau", "emang", "wkwkwk", "itu", "lu", "dah", "kenapa", 
            "hey", "dah", "hahaha", "itu", "hai", "kak",
            "deh", "herann", "skrg", "nya", "makin", "kayak", "udah", "kk",
            "sepertinya","di","haha","msh","ah","niiii","in","ih","yehh","wahh"]
def stopword_removal(komen):
    x = []
    data = []
    def myFunc(x):
        if x in stopword:
            return False
        else:
            return True

    fit = filter(myFunc, komen)
    for x in fit:
        data.append(x)

    return data

# Stemming
def stemming_kata(kata):

    # Kamus kata dasar (contoh: kata -> kat)
    kamus = {
        "membacakan": "baca", "buku-buku": "buku","memutuskan": "putus","menemukan" : "temu", "permainan": "main","menggambar": "gambar",
        "memperlancar": "lancar","kebahagiaan": "bahagia","memutihkan": "putih","berlapis lapis": "lapis","melebihi":"lebih","mainin":"main",
        "dilancarkan":"lancar","serasa":"rasa", "mempunyai":"punya","kekurangan" : "kurang","keliatan" : "liat","ngebully2" : "bully",
        "menyakitkan" : "sakit","kehaluanmu" : "halu","kesalahan" : "salah","menjadikanmu" : "jadi","kesalahannya" : "salah",
        "keberanian" : "berani","ngegemesin" : "gemes","bertanya" : "tanya","berenang" : "renang", "mengeluarkan" : "keluar"}

    dasar = {"tanya", "berani", "mereka", "makan", "dia", "diam","kamu","kalian","penuh"} #kata dasar yang tidak berimbuhan 
    akhiran = ["2", "nya", "2nya", "lah", "in", "kan", "pun", "an", "mu"] #kata imbuhan akhir
    awalan = ["me", "mem", "men", "meny", "meng", "menge", "pe", "ber", "nge", "di", "ng"] #kata imbuhan awal
     
    # Cek apakah kata ada dalam kamus kata dasar
    if kata in kamus:
        return kamus[kata]
    
    if kata in dasar:
        return kata
    
    # Implementasi aturan-aturan stemming tambahan di sini

    for aw in awalan:
        if kata.startswith(aw):
            kata = kata[len(aw):]
            break  
        
    for ak in akhiran:
        if kata.endswith(ak):
            kata = kata[:-len(ak)]
            break

    # Jika tidak ada aturan yang cocok, kembalikan kata asli
    return kata

# Fungsi untuk melakukan stemming pada kalimat
def stemming_kalimat(kalimat):
    kata_kunci_stemmed = [stemming_kata(kata) for kata in kalimat]
    kata_kunci_stemmed = [stemming_kata(kata) for kata in kalimat]
    kalimat_stemmed = " ".join(kata_kunci_stemmed)
    return kalimat_stemmed

# Buka data 
with open('tfIdf.pkl', mode='rb') as tf:
    tfid_load = pickle.load(tf)
with open('model.pkl', mode='rb') as model:
    model_load = pickle.load(model)
with open('clf.pkl', mode='rb') as cl:
    clf_load = pickle.load(cl)

# Streamlit
st.title('Analisis Sentimen Komentar')
comment = st.text_input('Masukan Komentar')
ok = st.button('OK')

if ok:
    dt_pred_clean = casefolding(comment)
    dt_pred_clean = token(dt_pred_clean)
    dt_pred_clean = stopword_removal(dt_pred_clean)
    dt_pred_clean = stemming_kalimat(dt_pred_clean)

    dt_pred = [dt_pred_clean]
    dt_pred_tfid = tfid_load.transform(dt_pred)
    pred = clf_load.predict(dt_pred_tfid)
    proba = clf_load.predict_proba(dt_pred_tfid)

    st.write('')

    st.write('')

    st.write('Komentar Bersih :')
    st.text(dt_pred)

    st.write('Prediksi Sentimen :')
    if pred == "Bullying":
        st.error(pred[0])
        st.write(f'Probabilitas Prediksi Bullying: {proba[0][0]*100:.2f}%')
        st.write(f'Probabilitas Prediksi Non-bullying: {proba[0][1]*100:.2f}%')
    elif pred == "Non-bullying":
        st.success(pred[0])
        st.write(f'Probabilitas Prediksi Bullying: {proba[0][0]*100:.2f}%')
        st.write(f'Probabilitas Prediksi Non-bullying: {proba[0][1]*100:.2f}%')