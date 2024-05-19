Keterangan File 
1. DATASET_CYBERBULLYING.csv --> dataset berisi komentar dari instagram dan analisisnya
2. NLP_Coba_.ipynb --> code untuk pemodelan dalam percobaan analisis sentimen 
3. Web.py --> code untuk mengimplementasikan ke web streamlit 
4. (clf.pkl, model.pkl, tfidf.pkl) --> file yang dibuat untuk menyimpan model pada penelitian yang akan membantu dalam pengimkplementasian
5. data_clean --> data baru setelah dataset melewati semua proses (case folding, tokenisasi, stopword, dan stemming) untuk melanjutkan ke tahap permodelan.

*File inti untuk sampai hingga pengimplementasian menggunakan web yaitu DATASET_CYBERBULLYING.csv, NLP_Coba_.ipynb, dan Web.py dikarenakan file lainnya akan otomatis terbuat jika file NLP_Coba_.ipynb dijalankan, dan jika tidak ada keempat file (clf.pkl, model.pkl, tfidf.pkl, dan data_clean) maka file Web.py tidak bisa berjalan

*untuk menjalankan file Web.py, tuliskan "streamlit run web.py" (tanpa "") dalam terminal dan tempatkan semua file berada di folder yang sama.

*jika terjadi error saat menjalankan web.py maka bisa mendowload sesuatu yang membuat web tidak berfungsi (pip...) misal error pada streamlit maka tuliskan "pip streamlit" (tanpa "") pada terminal, tunggu hingga proses download selesai kemudian reload web atau ulangi proses run streamlit.