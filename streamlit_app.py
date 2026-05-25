import streamlit as st

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="E-Lab Kimia Organik",
    page_icon="🧪",
    layout="wide"
)

# --- Sidebar Navigasi ---
st.sidebar.title("🧪 PKO-Lab App")
st.sidebar.write("Aplikasi Praktikum Kimia Organik")
st.sidebar.markdown("---")

# Pilihan Bab (Untuk sekarang fokus Bab III)
pilihan_bab = st.sidebar.selectbox(
    "Pilih Bab Praktikum:",
    [
        "Bab I (Segera Hadir)", 
        "Bab II (Segera Hadir)", 
        "Bab III: Aldehid dan Keton", 
        "Bab IV s/d VIII (Segera Hadir)"
    ],
    index=2 # Default langsung ke Bab III
)

# Navigasi Menu Utama
menu_utama = st.sidebar.radio(
    "Navigasi Menu:",
    ["Beranda", "Menu 1: Materi Pembelajaran", "Menu 2: Games Penentuan Senyawa", "Menu 3: Games Mengidentifikasi Senyawa"]
)

st.sidebar.markdown("---")
st.sidebar.caption("Dibuat untuk memudahkan pemahaman reaksi identifikasi senyawa organik.")

# --- KONTEN APLIKASI ---

# Memastikan user memilih Bab III, jika pilih yang lain beri pesan interaktif
if pilihan_bab != "Bab III: Aldehid dan Keton":
    st.title("🚧 Fitur Sedang Dikembangkan")
    st.info("Saat ini sistem sedang difokuskan untuk pengembangan **Bab III: Aldehid dan Keton**. Silakan pilih Bab III pada sidebar di sebelah kiri!")

else:
    # ==================== BERANDA ====================
    if menu_utama == "Beranda":
        st.title("👋 Selamat Datang di E-Lab Kimia Organik")
        st.subheader("Bab III: Analisis Kualitatif Aldehid dan Keton")
        
        st.markdown("""
        Web aplikasi ini dirancang khusus untuk membantu mahasiswa memahami reaksi-reaksi identifikasi 
        gugus fungsi karbonil, spesifiknya **Aldehid** dan **Keton**. Melalui aplikasi ini, kamu bisa mempelajari 
        teori dasar sekaligus menguji kemampuanmu lewat *games* simulasi laboratorium.
        
        ### 📌 Daftar Percobaan Bab III:
        1. **Percobaan 1:** Pereaksi Na-Bisulfit (Adisi Nukleofilik)
        2. **Percobaan 2:** Pereaksi Schiff (Uji Kepekaan Aldehid)
        3. **Percobaan 3:** Pereaksi Fehling (Oksidasi Aldehid Alifatik)
        4. **Percobaan 4:** Pereaksi Tollens (Uji Cermin Perak)
        5. **Percobaan 5:** Pembentukan Hemiasetal dan Asetal
        
        *Silakan gunakan menu di sidebar sebelah kiri untuk mulai belajar atau bermain games!*
        """)
        st.image("https://images.unsplash.com/photo-1532187863486-abf9d39d6618?auto=format&fit=crop&q=80&w=1000", caption="E-Lab Praktikum Kimia Organik", use_container_width=True)

    # ==================== MENU 1: MATERI PEMBELAJARAN ====================
    elif menu_utama == "Menu 1: Materi Pembelajaran":
        st.title("📚 Materi Pembelajaran: Aldehid & Keton")
        st.write("Klik pada tab di bawah ini untuk mempelajari detail setiap percobaan di laboratorium.")

        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "1. Na-Bisulfit", "2. Pereaksi Schiff", "3. Pereaksi Fehling", "4. Pereaksi Tollens", "5. Hemiasetal/Asetal"
        ])

        with tab1:
            st.header("Percobaan 1: Pereaksi Natrium Bisulfit ($NaHSO_3$)")
            st.markdown("""
            * **Prinsip:** Reaksi adisi nukleofilik pada gugus karbonil. Aldehid dan beberapa keton metil (metil keton) dapat bereaksi dengan larutan jenuh $NaHSO_3$ membentuk senyawa adisi yang berbentuk **kristal putih**.
            * **Fungsi:** Sering digunakan untuk memisahkan senyawa karbonil dari campuran senyawa organik lainnya karena produk kristalnya dapat dimurnikan kembali.
            * **Hasil Positif:** Terbentuknya endapan kristal putih.
            """)
            
        with tab2:
            st.header("Percobaan 2: Pereaksi Schiff")
            st.markdown("""
            * **Prinsip:** Pereaksi Schiff (fushsin yang dadekolorisasi oleh $SO_2$) digunakan untuk membedakan aldehid dan keton dengan tingkat kepekaan yang tinggi.
            * **Hasil Positif:** * **Aldehid:** Memberikan warna **merah keunguan / ungu pekat** secara cepat tanpa pemanasan.
                * **Keton:** Tidak memberikan perubahan warna (tetap bening/pucat) atau lambat sekali.
            """)

        with tab3:
            st.header("Percobaan 3: Pereaksi Fehling")
            st.markdown("""
            * **Prinsip:** Oksidasi lemah menggunakan ion $Cu^{2+}$ dalam suasana basa (Fehling A: $CuSO_4$, Fehling B: Kalium Natrium Tartrat + $NaOH$). Gugus aldehid akan teroksidasi menjadi asam karboksilat, sedangkan ion $Cu^{2+}$ akan tereduksi menjadi $Cu_2O$.
            * **Hasil Positif:**
                * **Aldehid (Alifatik):** Terbentuk **endapan merah bata** ($Cu_2O$).
                * **Keton:** Negatif (tidak bereaksi, larutan tetap biru).
            """)

        with tab4:
            st.header("Percobaan 4: Pereaksi Tollens")
            st.markdown("""
            * **Prinsip:** Disebut juga uji cermin perak. Menggunakan pereaksi $[Ag(NH_3)_2]^+$. Gugus aldehid dioksidasi menjadi gugus karboksilat, sedangkan ion $Ag^+$ direduksi menjadi logam perak ($Ag$).
            * **Hasil Positif:**
                * **Aldehid:** Terbentuk **cermin perak** pada dinding tabung reaksi setelah dipanaskan perlahan.
                * **Keton:** Negatif (tidak terbentuk cermin perak).
            """)

        with tab5:
            st.header("Percobaan 5: Pembentukan Hemiasetal dan Asetal")
            st.markdown("""
            * **Prinsip:** Reaksi antara senyawa karbonil (aldehid/keton) dengan alkohol dalam suasana asam. 
                * Reaksi 1 molekul alkohol + aldehid $\rightarrow$ **Hemiasetal** (memiliki gugus -OH dan -OR pada karbon yang sama).
                * Reaksi berlanjut dengan molekul alkohol kedua $\rightarrow$ **Asetal** (memiliki dua gugus -OR).
            * **Fungsi:** Reaksi ini sangat penting dalam kimia karbohidrat (pembentukan struktur siklik glukosa) dan sebagai gugus pelindung (*protecting group*) karbonil dalam sintesis organik.
            """)

    # ==================== MENU 2: GAMES PENENTUAN SENYAWA ====================
    elif menu_utama == "Menu 2: Games Penentuan Senyawa":
        st.title("🎮 Game 1: Penentuan Senyawa Misteri")
        st.write("Uji pemahamanmu! Tebak senyawa misteri berdasarkan data hasil uji laboratorium di bawah ini.")
        st.markdown("---")

        # Kasus Soal
        st.subheader("📋 Studi Kasus:")
        st.info("""
        Seorang praktikan menemukan botol sampel tanpa label berisi cairan bening. 
        Hasil uji laboratorium menunjukkan data sebagai berikut:
        1. Saat direaksikan dengan **Pereaksi Schiff**, larutan langsung berubah menjadi **ungu pekat**.
        2. Saat diuji dengan **Pereaksi Fehling**, terbentuk **endapan merah bata**.
        3. Saat direaksikan dengan **Na-Bisulfit**, terbentuk **kristal putih**.
        """)

        # Pilihan Jawaban
        pilihan = st.radio(
            "Berdasarkan data di atas, senyawa misteri tersebut kemungkinan besar adalah...",
            ["Aseton (Propanon)", "Formaldehid (Metanal)", "Etanol", "Asam Asetat"]
        )

        # Tombol Cek Jawaban
        if st.button("Kirim Jawaban"):
            if pilihan == "Formaldehid (Metanal)":
                st.success("🎉 BETUL SEKALI! Formaldehid adalah golongan aldehid yang memberikan hasil positif terhadap uji Schiff, Fehling, dan Na-Bisulfit.")
                st.balloons()
            elif pilihan == "Aseton (Propanon)":
                st.error("❌ Salah. Aseton adalah keton, keton tidak bereaksi positif dengan Pereaksi Fehling (tidak menghasilkan endapan merah bata).")
            else:
                st.error("❌ Salah. Senyawa tersebut bukan golongan aldehid/keton. Silakan baca kembali prinsip materinya.")

    # ==================== MENU 3: GAMES MENGIDENTIFIKASI SENYAWA ====================
    elif menu_utama == "Menu 3: Games Mengidentifikasi Senyawa":
        st.title("🔬 Game 2: Detektif Pereaksi Laboratorium")
        st.write("Pilihlah pereaksi yang tepat untuk membedakan dua senyawa yang diberikan!")
        st.markdown("---")

        score = 0

        # Pertanyaan 1
        st.subheader("Soal 1: Membedakan Propanal dan Propanon")
        st.write("Pereaksi mana yang paling tepat dan efisien untuk membedakan Propanal (Aldehid) dan Propanon (Keton)?")
        q1 = st.selectbox("Pilih Pereaksi untuk Soal 1:", ["", "Pereaksi Tollens", "Larutan NaOH pekat", "Indikator PP"], key="q1")
        
        if q1 == "Pereaksi Tollens":
            st.caption("🟢 Pilihan tepat untuk Soal 1 (Tollens hanya bereaksi dengan aldehid menghasilkan cermin perak).")
            score += 50
        elif q1 != "":
            st.caption("🔴 Kurang tepat, pereaksi tersebut tidak spesifik membedakan keduanya.")

        st.markdown("---")

        # Pertanyaan 2
        st.subheader("Soal 2: Pemurnian Senyawa Karbonil")
        st.write("Jika kamu ingin memisahkan dan memurnikan senyawa Benzaldehid dari campuran minyak hidrokarbon melalui pembentukan kristal, pereaksi apa yang kamu gunakan?")
        q2 = st.selectbox("Pilih Pereaksi untuk Soal 2:", ["", "Pereaksi Fehling", "Pereaksi Schiff", "Natrium Bisulfit (Na-Bisulfit)"], key="q2")

        if q2 == "Natrium Bisulfit (Na-Bisulfit)":
            st.caption("🟢 Pilihan tepat untuk Soal 2 (Adisi Na-Bisulfit menghasilkan kristal putih yang bisa dimurnikan kembali).")
            score += 50
        elif q2 != "":
            st.caption("🔴 Kurang tepat, pereaksi ini digunakan untuk uji identifikasi warna/oksidasi, bukan pemisahan kristal.")

        # Total Skor
        st.markdown("---")
        if q1 != "" and q2 != "":
            st.metric(label="Total Skor Kamu", value=f"{score} / 100")
            if score == 100:
                st.success("🥇 Sempurna! Kamu sudah siap melakukan Praktikum Kimia Organik Bab III!")
                
