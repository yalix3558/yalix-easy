import streamlit as st
from gtts import gTTS
import io

# Sayfa Ayarları
st.set_page_config(page_title="Yalix Easy", page_icon="🏟️")

# --- TAKIM SEÇİMİ VE TASARIM AYARLARI ---
st.sidebar.header("🏟️ Choose Your Home Ground")
team = st.sidebar.radio("Stadyumunuzu Seçin:", 
                         ("Galatasaray (Rams Park) 🦁", 
                          "Fenerbahçe (Ülker Stadyumu) 🐂", 
                          "Beşiktaş (Tüpraş Stadyumu) 🦅"))

# Takımlara göre renk ve STADYUM RESİMLERİ
if "Galatasaray" in team:
    primary_color = "#A32638" # Kırmızı
    secondary_color = "#FDB912" # Sarı
    img_url = "https://images.unsplash.com/photo-1598282367500-2f3b79ce4d13?w=800" # Rams Park atmosferi
    stadium_name = "Rams Park 🦁"
elif "Fenerbahçe" in team:
    primary_color = "#002366" # Lacivert
    secondary_color = "#FDB912" # Sarı
    img_url = "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800" # Ülker Stadyumu atmosferi
    stadium_name = "Ülker Stadyumu 🐂"
else: # Beşiktaş
    primary_color = "#000000" # Siyah
    secondary_color = "#FFFFFF" # Beyaz
    img_url = "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800" # Tüpraş Stadyumu atmosferi
    stadium_name = "Tüpraş Stadyumu 🦅"

# Dinamik CSS Entegrasyonu
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0E1117; }}
    .stButton>button {{
        background-color: {primary_color} !important; 
        color: {secondary_color} !important; 
        border-radius: 20px;
        border: 2px solid {secondary_color} !important;
        font-weight: bold; width: 100%;
    }}
    .stButton>button:hover {{
        background-color: {secondary_color} !important;
        color: {primary_color} !important;
    }}
    h1, h3 {{ color: {secondary_color} !important; text-align: center; }}
    label {{ color: {secondary_color} !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- STADYUM LOGOSU VE BAŞLIK ---
st.image(img_url, caption=f"Welcome to {stadium_name} 🏟️", use_container_width=True)
st.title(f"🎙️ Yalix Easy: {stadium_name.split()[0]} Live")
st.markdown("### *Your Voice, Your Stadium.*")

# --- SESLENDİRME BÖLÜMÜ ---
language_option = st.selectbox("Language / Dil:", ("Turkish", "English"))
lang_code = 'tr' if language_option == "Turkish" else 'en'
user_text = st.text_area("Enter text / Metin yazın:", placeholder="Şampiyonluk sözlerini buraya yazın...", height=150)

if st.button("🚀 CONVERT TO VOICE"):
    if user_text:
        with st.spinner("Yalix Easy processing in the stadium..."):
            tts = gTTS(text=user_text, lang=lang_code)
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            st.audio(audio_fp.getvalue(), format='audio/mp3')
            st.download_button(label="📥 DOWNLOAD MP3", data=audio_fp.getvalue(), file_name="yalix_easy_stadium.mp3")
            st.success(f"Perfect voice from {stadium_name}! 😎")
    else:
        st.warning("Please type something first, Boss!")

# --- YOUTUBE VE İMZA ---
st.divider()
st.link_button("📺 YALIXGAMER YOUTUBE KANALI", "https://www.youtube.com/@Yalixgamer")
st.caption("© 2026 Yalix Easy Software Co. | CEO: Yiğit Ali Arslan Doğan")
