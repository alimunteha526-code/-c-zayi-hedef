import streamlit as st

# Sayfa ayarları
st.set_page_config(page_title="Özel Hesaplama", layout="centered")

st.title("🧮 Güncellenmiş Hesaplama Modülü")
st.write("Ana rakamdan ikinci rakamı çıkarır ve ikiye böler.")

# Giriş alanları
col1, col2 = st.columns(2)

with col1:
    sayi_1 = st.number_input("5,80'in kaynağı olan sayı:", min_value=0.0, step=0.01, format="%.2f", key="s1")

with col2:
    sayi_2 = st.number_input("Çıkarılacak rakam:", min_value=0.0, step=0.01, format="%.2f", key="s2")

if st.button("Hesapla"):
    if sayi_1 > 0:
        # 1. Aşama: %5,80'den ana rakama ulaş
        ana_rakam = sayi_1 / 0.058
        
        # 2. Aşama: Ana rakamdan yeni rakamı çıkar ve ikiye böl
        nihai_sonuc = (ana_rakam - sayi_2) / 2
        
        st.markdown("---")
        
        # Görsel Sonuçlar
        res_col1, res_col2 = st.columns(2)
        
        with res_col1:
            st.metric("Bulunan Ana Rakam", f"{ana_rakam:,.2f}")
            st.caption(f"Hesaplama: {sayi_1:,.2f} / 0,058")
            
        with res_col2:
            st.metric("Nihai Sonuç", f"{nihai_sonuc:,.2f}")
            st.caption(f"İşlem: ({ana_rakam:,.2f} - {sayi_2:,.2f}) / 2")
            
        # Bilgilendirme
        st.success(f"İşlem tamamlandı. Sonuç: **{nihai_sonuc:,.2f}**")
            
    else:
        st.error("Lütfen ilk kutuya 0'dan büyük bir sayı giriniz.")

# Formül Bilgisi
st.info("Mantık: [Ana Rakam - Girdi 2] / 2")
