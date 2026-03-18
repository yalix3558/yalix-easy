import streamlit as st
from gtts import gTTS
import io

# Sayfa Ayarları
st.set_page_config(page_title="Yalix Easy", page_icon="⚽")

# --- TAKIM SEÇİMİ VE TASARIM AYARLARI ---
st.sidebar.header("🎨 Customize Your App")
team = st.sidebar.radio("Choose Your Team / Takımınızı Seçin:", 
                         ("Galatasaray 🦁", "Fenerbahçe 🐂", "Beşiktaş 🦅"))

# Takımlara göre renk, resim ve güçlü slogan ayarları
if team == "Galatasaray 🦁":
    primary_color = "#A32638" # Kırmızı
    secondary_color = "#FDB912" # Sarı
    img_url = "https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=800"
    caption = "Yalix Easy: The Voice of the Lion 🦁 - Aslanın Sesi"
elif team == "Fenerbahçe 🐂":
    primary_color = "#002366" # Lacivert
    secondary_color = "#FDB912" # Sarı
    # Fenerbahçe için Güçlü Boğa Resmi
    img_url = "https://images.unsplash.com/photo-1599723023028-09559c38f1f7?w=800"
    caption = "Yalix Easy: The Voice of the Bull 🐂 - Boğanın Sesi (Kadıköy Gücü)"
else: # Beşiktaş 🦅
    primary_color = "#000000" # Siyah
    secondary_color = "#FFFFFF" # Beyaz
    # Beşiktaş için Heybetli Kartal Resmi
    img_url = "https://images.unsplash.com/photo-1611689225620-3e70248bc0f0?w=800"
    caption = "Yalix Easy: The Voice of the Black Eagle 🦅 - Kara Kartalın Sesi"

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

# --- LOGO VE BAŞLIK ---
st.image(img_url, caption=caption, use_container_width=True)
st.title(f"🎙️ Yalix Easy: {team.split()[0]} Edition")
st.markdown("### *Type it. Hear it. Easy.*")

# --- SESLENDİRME BÖLÜMÜ ---
language_option = st.selectbox("Language / Dil:", ("Turkish", "English"))
lang_code = 'tr' if language_option == "Turkish" else 'en'
user_text = st.text_area("Enter text / Metin yazın:", placeholder="Type something...", height=150)

if st.button("🚀 CONVERT TO VOICE"):
    if user_text:
        with st.spinner("Yalix Easy processing..."):
            tts = gTTS(text=user_text, lang=lang_code)
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            st.audio(audio_fp.getvalue(), format='audio/mp3')
            st.download_button(label="📥 DOWNLOAD MP3", data=audio_fp.getvalue(), file_name="yalix_easy.mp3")
            st.success("Done! 😎")
    else:
        st.warning("Please type something first!")

# --- YOUTUBE VE İMZA ---
st.divider()
st.link_button("📺 YALIXGAMER YOUTUBE KANALI", "https://www.youtube.com/@Yalixgamer")
st.caption("© 2026 Yalix Easy Software Co. | CEO: Yiğit Ali Arslan Doğan")
