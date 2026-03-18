import streamlit as st
from gtts import gTTS
import io

# Sayfa Ayarları
st.set_page_config(page_title="Yalix Easy", page_icon="🏟️")

# --- ZİYARETÇİ SAYACI ---
if 'count' not in st.session_state:
    st.session_state.count = 120 # Yeni sürümde 120'den başlayalım patron!
else:
    st.session_state.count += 1

# --- TAKIM SEÇİMİ VE TASARIM ---
st.sidebar.header("🚀 CEO Dashboard")
st.sidebar.metric(label="Total Visitors", value=f"{st.session_state.count}")

team = st.sidebar.radio("Stadyumunuzu Seçin / Choose Stadium:", 
                         ("Galatasaray (Rams Park) 🦁", 
                          "Fenerbahçe (Ülker Stadyumu) 🐂", 
                          "Beşiktaş (Tüpraş Stadyumu) 🦅"))

if "Galatasaray" in team:
    primary_color, secondary_color = "#A32638", "#FDB912"
    img_url = "https://upload.wikimedia.org/wikipedia/commons/e/e0/Nef_Stadium_%28Galatasaray_SK%29_Istanbul.jpg"
    stadium_name = "Rams Park 🦁"
elif "Fenerbahçe" in team:
    primary_color, secondary_color = "#002366", "#FDB912"
    img_url = "https://upload.wikimedia.org/wikipedia/commons/3/30/Şükrü_Saracoğlu_Stadyumu%2C_İstanbul.jpg"
    stadium_name = "Ülker Stadyumu 🐂"
else:
    primary_color, secondary_color = "#000000", "#FFFFFF"
    img_url = "https://upload.wikimedia.org/wikipedia/commons/4/4b/Tüpraş_Stadyumu_Gece_Görünümü.jpg"
    stadium_name = "Tüpraş Stadyumu 🦅"

st.markdown(f"""
    <style>
    .stApp {{ background-color: #0E1117; }}
    .stButton>button {{
        background-color: {primary_color} !important; color: {secondary_color} !important;
        border-radius: 20px; border: 2px solid {secondary_color} !important;
        font-weight: bold; width: 100%;
    }}
    h1, h2, h3 {{ color: {secondary_color} !important; text-align: center; }}
    label {{ color: {secondary_color} !important; }}
    .about-box {{ background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 15px; border-left: 5px solid {primary_color}; }}
    </style>
    """, unsafe_allow_html=True)

# --- ANA EKRAN ---
st.image(img_url, caption=f"Welcome to {stadium_name} 🏟️", use_container_width=True)
st.title(f"🎙️ Yalix Easy: {stadium_name.split()[0]} Live")

# --- SESLENDİRME ---
language_option = st.selectbox("Language / Dil:", ("Turkish", "English"))
lang_code = 'tr' if language_option == "Turkish" else 'en'
user_text = st.text_area("Enter text / Metin yazın:", placeholder="Konuşmak istediğiniz metni yazın...", height=100)

if st.button("🚀 CONVERT TO VOICE"):
    if user_text:
        tts = gTTS(text=user_text, lang=lang_code)
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        st.audio(audio_fp.getvalue(), format='audio/mp3')
        st.download_button(label="📥 DOWNLOAD MP3", data=audio_fp.getvalue(), file_name="yalix_easy.mp3")
    else:
        st.warning("Please type something first!")

# --- YENİ ÖZELLİK: MÜZİK İSTASYONU ---
st.divider()
st.markdown("## 🎹 Yalix Music Station")
col1, col2 = st.columns(2)

with col1:
    if st.button("🎹 PIANO CHORD"):
        st.audio("https://www.soundjay.com/misc/sounds/bell-ringing-01c.mp3") # Tatlı bir piyano tınısı

with col2:
    if st.button("🥁 DRUM BEAT"):
        st.audio("https://www.soundjay.com/buttons/sounds/button-2.mp3") # Güçlü bir davul vuruşu

# --- PAYLAŞ BUTONU ---
st.divider()
share_text = "Hey! Check out Yalix Easy by Yiğit Ali: https://yalix-easy-app.streamlit.app/"
whatsapp_link = f"https://wa.me/?text={share_text.replace(' ', '%20')}"
st.link_button("🟢 SHARE ON WHATSAPP", whatsapp_link, use_container_width=True)

# --- CEO HAKKINDA ---
st.markdown("## 👨‍💻 Meet the CEO")
st.markdown(f"""<div class="about-box"><p style="color: white;">Ben <b>Yiğit Ali Arslan Doğan</b>. 7 yaşındayım. İstanbul'da yaşıyorum ve Galatasaraylıyım! Geleceğin <b>Pilotu</b> ve <b>Yazılımcısıyım</b>. 🎮✈️</p></div>""", unsafe_allow_html=True)

# --- VİDEO ---
st.divider()
st.markdown("## 📺 Latest Video")
st.video("https://www.youtube.com/watch?v=833sZ0qW83Q")
st.link_button("📺 VISIT YALIXGAMER CHANNEL", "https://www.youtube.com/@Yalixgamer")

st.caption("© 2026 Yalix Easy Software Co. | CEO: Yiğit Ali Arslan Doğan")
