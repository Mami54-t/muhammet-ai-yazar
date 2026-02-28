import streamlit as st
import google.generativeai as genai

# 1. Gemini API Anahtarını Tanımla
# API anahtarını doğrudan buraya yazıyoruz (Senin anahtarın)
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 2. Sayfa Ayarları
st.set_page_config(page_title="Muhammet AI", page_icon="✍️")
st.title("✍️ Muhammet AI - Akıllı İçerik Yazarı")
st.markdown("---")

# 3. Yan Panel (Sidebar)
st.sidebar.title("🚀 Muhammet AI Premium")
st.sidebar.write("Yapay zeka ile profesyonel içerikler oluşturun.")

# 4. Ana Ekran
konu = st.text_input("Hangi konuda içerik yazılsın?", placeholder="Örn: Yapay zekanın geleceği")

if st.button("İçerik Oluştur"):
    if konu:
        with st.spinner('Yapay zeka yazıyor...'):
            try:
                # Modeli başlat (Hata vermeyen kararlı sürüm)
                model = genai.GenerativeModel('gemini-pro')
                
                # İçerik üret
                response = model.generate_content(f"{konu} hakkında profesyonel ve ilgi çekici bir blog yazısı yaz.")
                
                st.success("✅ İçerik Başarıyla Oluşturuldu!")
                st.markdown("### 📝 Oluşturulan Metin:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Bir hata oluştu: {e}")
    else:
        st.warning("Lütfen bir konu başlığı girin!")
        
