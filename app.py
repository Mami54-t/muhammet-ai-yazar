import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="Muhammet AI", page_icon="✍️")

# Başlık
st.title("✍️ Muhammet AI - Akıllı İçerik Yazarı")
st.markdown("---")

# Yan Panel - Satış Alanı
st.sidebar.header("🚀 Premium Üyelik")
st.sidebar.write("Sınırsız içerik üretmek için üye olun.")

# BURAYA DİKKAT: Shopier linkini aldığında 'https://www.shopier.com' yazan yeri onunla değiştireceğiz.
st.sidebar.markdown('[💳 Hemen Satın Al](https://www.shopier.com)')

# Ana Ekran
konu = st.text_input("Hangi konuda içerik yazılsın?")
st.button("İçerik Oluştur")

st.info("Sistem şu an kurulum aşamasındadır. Çok yakında tam kapasite hizmetinizde!")
