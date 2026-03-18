import streamlit as st
import requests
import io

# Sayfa Ayarları
st.set_page_config(page_title="Yalix Easy Pro", page_icon="🎙️")

# --- CEO PANEL ---
st.sidebar.header("🔑 Boss Security")
# Kullanıcıya anahtarın sk_ ile başlaması gerektiğini hatırlatalım
api_key = st.sidebar.text_input("ElevenLabs API Key Yapıştırın:", type="password")

team = st.sidebar.radio("Stadyumunuzu Seçin:", 
                         ("Galatasaray (Rams Park) 🦁", 
                          "Fenerbahçe (Ülker Stadyumu) 🐂", 
                          "Beşiktaş (Tüpraş Stadyumu) 🦅"))

# Renk Ayarları ve DİREKT Resim Linkleri (Aracı site kullanmadan)
if "Galatasaray" in team:
    p, s, img = "#A32638", "#FDB912", "https://upload.wikimedia.org/wikipedia/commons/e/e0/Nef_Stadium_%28Galatasaray_SK%29_Istanbul.jpg"
elif "Fenerbahçe" in team:
    p, s, img = "#002366", "#FDB912", "https://upload.wikimedia.org/wikipedia/commons/3/30/Şükrü_Saracoğlu_Stadyumu%2C_İstanbul.jpg"
else:
    p, s, img = "#000000", "#FFFFFF", "https://upload.wikimedia.org/wikipedia/commons/4/4b/Tüpraş_Stadyumu_Gece_Görünümü.jpg"

st.markdown(f"""
    <style>
    .stApp {{ background-color: #0E1117; }}
    .stButton>button {{
        background-color: {p} !important; color: {s} !important;
        border-radius: 20px; border: 2px solid {s} !important;
        font-weight: bold; height: 50px; width: 100%;
    }}
    h1, h2, h3, label {{ color: {s} !important; text-align: center; }}
    </style>
    """, unsafe_allow_html=True)

# Görsel ve Başlık
st.image(img, use_container_width=True)
st.title(f"🎙️ Yalix Easy: {team.split()[0]} Live")

# Ses Seçenekleri
voices = {
    "Antoni (Heyecanlı)": "ErXwVwoD7JW99R99S65H", 
    "Rachel (Akıcı)": "21m00Tcm4TlvDq8ikWAM",
    "Bella (Sakin)": "EXAVITQu4vr4xnSDxMaL"
}
selected_voice = st.selectbox("Bir Ses Seçin:", list(voices.keys()))

user_text = st.text_area("Ne söyleyelim patron?", placeholder="Mete konuşmadan oyna!")

if st.button("🚀 GERÇEK SESLE KONUŞTUR"):
    if not api_key:
        st.error("Soldaki menüye API Key'i yapıştırmayı unutma patron!")
    elif user_text:
        with st.spinner("Ses hazırlanıyor..."):
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{voices[selected_voice]}"
            headers = {
                "xi-api-key": api_key, 
                "Content-Type": "application/json",
                "Accept": "audio/mpeg"
            }
            data = {
                "text": user_text, 
                "model_id": "eleven_multilingual_v2",
                "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
            }
            
            try:
                resp = requests.post(url, json=data, headers=headers)
                
                if resp.status_code == 200:
                    st.audio(resp.content, format='audio/mp3')
                    st.success("İşte bu! Sesi duyuyor musun? 😎")
                else:
                    # BURASI ÖNEMLİ: Hatanın ne olduğunu ekrana yazdırıyoruz!
                    st.error(f"Hata Kodu: {resp.status_code}")
                    st.write("Hata Detayı:", resp.text) # Neden çalışmadığını burada göreceğiz!
            except Exception as e:
                st.error(f"Bir bağlantı sorunu oluştu: {e}")

st.divider()
st.video("https://www.youtube.com/watch?v=833sZ0qW83Q")
st.caption("© 2026 Yalix Easy Software Co. | CEO: Yiğit Ali Arslan Doğan")
