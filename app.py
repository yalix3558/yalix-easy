import streamlit as st
import requests
import io
from gtts import gTTS # Ücretsiz ses için lazım

# Sayfa Ayarları
st.set_page_config(page_title="Yalix Easy CEO Edition", page_icon="🎙️")

# --- CEO PANEL (SIDEBAR) ---
st.sidebar.header("⚙️ CEO Control Center")

# SES MOTORU SEÇİMİ (Karakter tasarrufu için!)
voice_engine = st.sidebar.radio(
    "Ses Motoru Seçin:",
    ("Ücretsiz Mod (Sınırsız 🆓)", "Pro Mod (ElevenLabs 💎)")
)

if voice_engine == "Pro Mod (ElevenLabs 💎)":
    raw_api_key = st.sidebar.text_input("1. ElevenLabs API Key:", type="password")
    api_key = raw_api_key.strip() if raw_api_key else None
    voice_id = st.sidebar.text_input("2. Voice ID:", value="pNInz6obpgnuM0sLSYoM")
else:
    st.sidebar.info("Şu an Ücretsiz Moddasınız. Karakter limitiniz eksilmez! 😎")

team = st.sidebar.radio("3. Stadyum Seçin:", ["Galatasaray 🦁", "Fenerbahçe 🐂", "Beşiktaş 🦅"])

# Tasarım ve Renkler
if "Galatasaray" in team: p, s = "#A32638", "#FDB912"
elif "Fenerbahçe" in team: p, s = "#002366", "#FDB912"
else: p, s = "#000000", "#FFFFFF"

st.markdown(f"<style>.stApp {{ background-color: #0E1117; }} .stButton>button {{ background-color: {p} !important; color: {s} !important; border-radius: 20px; border: 2px solid {s} !important; font-weight: bold; width: 100%; }} h1, h2, h3, label {{ color: {s} !important; text-align: center; }} </style>", unsafe_allow_html=True)

st.title(f"🎙️ Yalix Easy: {voice_engine.split()[0]}")

user_text = st.text_area("Metninizi yazın:", placeholder="Karakterlerini idareli kullan patron!")

if st.button("🚀 SESLENDİR"):
    if user_text:
        if voice_engine == "Ücretsiz Mod (Sınırsız 🆓)":
            with st.spinner("Ücretsiz ses hazırlanıyor..."):
                tts = gTTS(text=user_text, lang='tr')
                audio_fp = io.BytesIO()
                tts.write_to_fp(audio_fp)
                st.audio(audio_fp.getvalue(), format='audio/mp3')
                st.success("Ücretsiz motor kullanıldı, kredin güvende! 🛡️")
        
        else: # ElevenLabs Kısmı
            if not api_key:
                st.error("Pro mod için API Key lazım patron!")
            else:
                with st.spinner("Pro ses hazırlanıyor (Kredi harcanıyor...)..."):
                    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id.strip()}"
                    headers = {"xi-api-key": api_key, "Content-Type": "application/json", "Accept": "audio/mpeg"}
                    data = {"text": user_text, "model_id": "eleven_multilingual_v2"}
                    resp = requests.post(url, json=data, headers=headers)
                    if resp.status_code == 200:
                        st.audio(resp.content, format='audio/mp3')
                        st.warning("Dikkat: Karakter limitinden harcandı! 💎")
                    else:
                        st.error(f"Hata: {resp.status_code}")
