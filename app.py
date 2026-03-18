import streamlit as st
import requests
import io

# Sayfa Ayarları
st.set_page_config(page_title="Yalix Easy Pro", page_icon="🎙️")

# --- CEO PANEL (SIDEBAR) ---
st.sidebar.header("🔑 Boss Security")
raw_api_key = st.sidebar.text_input("1. ElevenLabs API Key:", type="password")
api_key = raw_api_key.strip() if raw_api_key else None

# BURASI YENİ: Kendi Voice ID'ni buraya yapıştıracaksın patron!
st.sidebar.divider()
st.sidebar.subheader("🎙️ Voice Settings")
voice_id = st.sidebar.text_input("2. Voice ID Yapıştırın:", value="pNInz6obpgnuM0sLSYoM") # Varsayılan: Adam sesi

team = st.sidebar.radio("3. Stadyum Seçin:", ["Galatasaray 🦁", "Fenerbahçe 🐂", "Beşiktaş 🦅"])

# Tasarım ve Renkler
if "Galatasaray" in team: p, s = "#A32638", "#FDB912"
elif "Fenerbahçe" in team: p, s = "#002366", "#FDB912"
else: p, s = "#000000", "#FFFFFF"

st.markdown(f"<style>.stApp {{ background-color: #0E1117; }} .stButton>button {{ background-color: {p} !important; color: {s} !important; border-radius: 20px; border: 2px solid {s} !important; font-weight: bold; width: 100%; }} h1, h2, h3, label {{ color: {s} !important; text-align: center; }} </style>", unsafe_allow_html=True)

st.title(f"🎙️ Yalix Easy: {team.split()[0]} Live")

user_text = st.text_area("Ne söyleyelim patron?", placeholder="Merhaba Yiğit Ali, sitemiz artık kükremeye hazır!")

if st.button("🚀 GERÇEK SESLE KONUŞTUR"):
    if not api_key:
        st.error("Lütfen soldaki menüye API Key yapıştırın!")
    elif not voice_id:
        st.error("Lütfen bir Voice ID yapıştırın!")
    elif user_text:
        with st.spinner("Ses hazırlanıyor..."):
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id.strip()}"
            headers = {"xi-api-key": api_key, "Content-Type": "application/json", "Accept": "audio/mpeg"}
            data = {"text": user_text, "model_id": "eleven_multilingual_v2"}
            
            resp = requests.post(url, json=data, headers=headers)
            
            if resp.status_code == 200:
                st.audio(resp.content, format='audio/mp3')
                st.success("İşte bu! Sesi duyuyor musun Yiğit Ali? 😎")
            else:
                st.error(f"Hata: {resp.status_code}")
                st.write("Hata Detayı:", resp.text)
