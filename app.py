import streamlit as st
from gtts import gTTS
import io

# Sayfa Ayarları
st.set_page_config(page_title="Yalix Easy", page_icon="🏟️")

# --- ZİYARETÇİ SAYACI ---
if 'count' not in st.session_state:
    st.session_state.count = 150 # Global açılış şerefine 150'den başlasın!
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
st.title(f"🎙️ Yalix Easy: Global Edition")

# --- YENİ ÖZELLİK: GENİŞLETİLMİŞ DİL SEÇENEKLERİ ---
languages = {
    "Turkish 🇹🇷": "tr",
    "English 🇺🇸": "en",
    "German 🇩🇪": "de",
    "French 🇫🇷": "fr",
    "Spanish 🇪🇸": "es",
    "Italian 🇮🇹": "it",
    "Japanese 🇯🇵": "ja"
}

language_option = st.selectbox("Select Voice Language / Ses Dilini Seçin:", list(languages.keys()))
lang_code = languages[language_option]

user_text = st.text_area("Enter text / Metin yazın:", placeholder="Type something to translate...", height=100)

if st.button("🚀 CONVERT TO VOICE"):
    if user_text:
        with st.spinner("Yalix Easy is translating..."):
            tts = gTTS(text=user_text, lang=lang_code)
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            st.audio(audio_fp.getvalue(), format='audio/mp3')
            st.download_button(label="📥 DOWNLOAD MP3", data=audio_fp.getvalue(), file_name=f"yalix_easy_{lang_code}.mp3")
    else:
        st.warning("Please type something first, CEO!")

# --- MÜZİK VE PAYLAŞIM (DEĞİŞMEDİ) ---
st.divider()
st.markdown("## 🎹 Yalix Music Station")
col1, col2 = st.columns(2)
with col1:
    if st.button("🎹 PIANO"): st.audio("https://www.soundjay.com/misc/sounds/bell-ringing-01c.mp3")
with col2:
    if st.button("🥁 DRUM"): st.audio("https://www.soundjay.com/buttons/sounds/button-2.mp3")

st.divider()
share_text = "Check out Yalix Easy! The best voice app: https://yalix-easy-app.streamlit.app/"
whatsapp_link = f"https://wa.me/?text={share_text.replace(' ', '%20')}"
st.link_button("🟢 SHARE ON WHATSAPP", whatsapp_link, use_container_width=True)

# --- CEO BİLGİ VE VİDEO ---
st.markdown("## 👨‍💻 Meet the CEO")
st.markdown(f"""<div class="about-box"><p style="color: white;">Ben <b>Yiğit Ali Arslan Doğan</b>. Geleceğin <b>Pilotu</b> ve <b>Yazılımcısıyım</b>. 🎮✈️</p></div>""", unsafe_allow_html=True)
st.video("https://www.youtube.com/watch?v=833sZ0qW83Q")
st.link_button("📺 VISIT YALIXGAMER CHANNEL", "https://www.youtube.com/@Yalixgamer")

st.caption("© 2026 Yalix Easy Software Co. | CEO: Yiğit Ali Arslan Doğan")
