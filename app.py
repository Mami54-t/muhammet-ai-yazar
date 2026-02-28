import streamlit as st
import google.generativeai as genai

# 1. Gemini API Anahtarını Tanımla
genai.configure(api_key="AIzaSyBdecRQwrxHWBn5itWZhlSrZa2TkZ_xudc")

# 2. Sayfa Ayarları
st.set_page_config(page_title="Muhammet AI", page_icon="✍️")
st.title("✍️ Muhammet AI - Akıllı İçerik Yazarı")
st.markdown("---")

# 3. Yan Panel (Sidebar)
st.sidebar.title("🚀 Premium Paket")
st.sidebar.write("Sınırsız içerik için yükseltin.")
st.sidebar.markdown("[💳 Hemen Satın Al](https://www.shopier.com)")

# 4. Ana Ekran
konu = st.text_input("Hangi konuda içerik yazılsın?", placeholder="Örn: Teknolojinin Geleceği")

if st.button("İçerik Oluştur"):
    if konu:
        with st.spinner('Yapay zeka senin için yazıyor...'):
            try:
                # Yapay zeka modelini çağırıyoruz
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(konu)
                
                st.success("İçerik Hazır!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Bir hata oluştu: {e}")
    else:
        st.warning("Lütfen bir konu başlığı girin!")
