import streamlit as st

# Sayfa tasarımı
st.set_page_config(page_title="Özel Hesaplama Aracı", layout="centered")

st.title("🧮 Özel Matematiksel İşlem Paneli")
st.write("Hesaplanan farkın, yeni rakamdan çıkarılıp ikiye bölündüğü model.")

# İki ayrı bölüm için sütunlar
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Aşama: Farkı Bul")
    sayi_1 = st.number_input("5,80 hesabı yapılacak sayı:", min_value=0.0, step=0.01, format="%.2f", key="input1")

with col2:
    st.subheader("2. Aşama: Yeni Rakam")
    sayi_2 = st.number_input("Çıkartma yapılacak yeni rakam:", min_value=0.0, step=0.01, format="%.2f", key="input2")

if st.button("Hesaplamayı Tamamla"):
    if sayi_1 > 0:
        # Ana rakamı bul (%100'ü)
        ana_rakam = sayi_1 / 0.058
        # Aradaki farkı hesapla
        fark = ana_rakam - sayi_1
        
        # Sonuç işlemi: (Yeni Rakam - Fark) / 2
        nihai_sonuc = (sayi_2 - fark) / 2
        
        st.markdown("---")
        
        # Sonuç Ekranı
        res_col1, res_col2 = st.columns(2)
        
        with res_col1:
            st.metric("Hesaplanan Fark", f"{fark:,.2f}")
            st.caption(f"({ana_rakam:,.2f} - {sayi_1:,.2f})")
            
        with res_col2:
            st.metric("Nihai Sonuç", f"{nihai_sonuc:,.2f}")
            st.caption(f"({sayi_2:,.2f} - {fark:,.2f}) / 2")

        # Özet metni
        st.success(f"İşlem başarıyla tamamlandı. Nihai değer: **{nihai_sonuc:,.2f}**")
    else:
        st.warning("Lütfen birinci bölüme 0'dan büyük bir değer giriniz.")

# Alt bilgi
st.info("Formül: [Yeni Rakam - ((Girdi / 0,058) - Girdi)] / 2")
