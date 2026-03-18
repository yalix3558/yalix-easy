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

# Takımlara göre renk ve YENİ VE ÇALIŞAN STADYUM RESİMLERİ
if "Galatasaray" in team:
    primary_color = "#A32638" # Kırmızı
    secondary_color = "#FDB912" # Sarı
    # Güvenilir direct link: Rams Park atmosferi
    img_url = "https://upload.wikimedia.org/wikipedia/commons/e/e0/Nef_Stadium_%28Galatasaray_SK%29_Istanbul.jpg" 
    stadium_name = "Rams Park 🦁"
elif "Fenerbahçe" in team:
    primary_color = "#002366" # Lacivert
    secondary_color = "#FDB912" # Sarı
    # Güvenilir direct link: Ülker Stadyumu atmosferi
    img_url = "https://upload.wikimedia.org/wikipedia/commons/3/30/Şükrü_Saracoğlu_Stadyumu%2C_İstanbul.jpg" 
    stadium_name = "Ülker Stadyumu 🐂"
else: # Beşiktaş
    primary_color = "#000000" # Siyah
    secondary_color = "#FFFFFF" # Beyaz
    # Güvenilir direct link: Tüpraş Stadyumu atmosferi
    img_url = "https://upload.wikimedia.org/wikipedia/commons/4/4b/Tüpraş_Stadyumu_Gece_Görünümü.jpg" 
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

# --- STADYUM GÖRSELİ VE BAŞLIK ---
# Hata kontrolü ekleyelim - eğer resim açılmazsa placeholder göstersin
try:
    st.image(img_url, caption=f"Welcome to {stadium_name} 🏟️", use_container_width=True)
except Exception:
    st.warning("⚠️ Stadyum resmi şu an yüklenemedi patron, ama ses motorumuz çalışıyor!")

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
