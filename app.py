import streamlit as st
from gtts import gTTS
import io

# Sayfa Ayarları
st.set_page_config(page_title="Yalix Easy", page_icon="🏟️")

# --- TAKIM SEÇİMİ VE TASARIM AYARLARI ---
st.sidebar.header("🏟️ Customize Your Experience")
team = st.sidebar.radio("Stadyumunuzu Seçin / Choose Stadium:", 
                         ("Galatasaray (Rams Park) 🦁", 
                          "Fenerbahçe (Ülker Stadyumu) 🐂", 
                          "Beşiktaş (Tüpraş Stadyumu) 🦅"))

# Takımlara göre renk ve stadyum resimleri
if "Galatasaray" in team:
    primary_color = "#A32638" 
    secondary_color = "#FDB912" 
    img_url = "https://upload.wikimedia.org/wikipedia/commons/e/e0/Nef_Stadium_%28Galatasaray_SK%29_Istanbul.jpg" 
    stadium_name = "Rams Park 🦁"
elif "Fenerbahçe" in team:
    primary_color = "#002366" 
    secondary_color = "#FDB912" 
    img_url = "https://upload.wikimedia.org/wikipedia/commons/3/30/Şükrü_Saracoğlu_Stadyumu%2C_İstanbul.jpg" 
    stadium_name = "Ülker Stadyumu 🐂"
else: 
    primary_color = "#000000" 
    secondary_color = "#FFFFFF" 
    img_url = "https://upload.wikimedia.org/wikipedia/commons/4/4b/Tüpraş_Stadyumu_Gece_Görünümü.jpg" 
    stadium_name = "Tüpraş Stadyumu 🦅"

# Dinamik CSS
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0E1117; }}
    .stButton>button {{
        background-color: {primary_color} !important; 
        color: {secondary_color} !important; 
        border-radius: 20px; border: 2px solid {secondary_color} !important;
        font-weight: bold; width: 100%;
    }}
    .stButton>button:hover {{
        background-color: {secondary_color} !important; color: {primary_color} !important;
    }}
    h1, h2, h3 {{ color: {secondary_color} !important; text-align: center; }}
    label {{ color: {secondary_color} !important; }}
    .about-box {{
        background-color: rgba(255, 255, 255, 0.05);
        padding: 20px; border-radius: 15px; border-left: 5px solid {primary_color};
    }}
    </style>
    """, unsafe_allow_html=True)

# --- STADYUM GÖRSELİ VE BAŞLIK ---
st.image(img_url, caption=f"Welcome to {stadium_name} 🏟️", use_container_width=True)
st.title(f"🎙️ Yalix Easy: {stadium_name.split()[0]} Live")

# --- SESLENDİRME BÖLÜMÜ ---
language_option = st.selectbox("Language / Dil:", ("Turkish", "English"))
lang_code = 'tr' if language_option == "Turkish" else 'en'
user_text = st.text_area("Enter text / Metin yazın:", placeholder="Şampiyonluk sözlerini buraya yazın...", height=100)

if st.button("🚀 CONVERT TO VOICE"):
    if user_text:
        with st.spinner("Processing..."):
            tts = gTTS(text=user_text, lang=lang_code)
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            st.audio(audio_fp.getvalue(), format='audio/mp3')
            st.download_button(label="📥 DOWNLOAD MP3", data=audio_fp.getvalue(), file_name="yalix_easy.mp3")
    else:
        st.warning("Please type something first!")

# --- YENİ ÖZELLİK: HAKKIMDA (ABOUT ME) ---
st.divider()
st.markdown("## 👨‍💻 Meet the CEO: Yiğit Ali")
st.markdown(f"""
<div class="about-box">
    <p style="color: white; font-size: 18px;">
    Merhaba! Ben <b>Yiğit Ali Arslan Doğan</b>. 7 yaşındayım ve Yakacık Final Okulu 2. sınıf öğrencisiyim. 
    İstanbul'da yaşıyorum ve tam bir <b>Galatasaray</b> taraftarıyım! 🦁<br><br>
    Gelecekte hem gökyüzünde süzülen bir <b>Pilot</b> hem de harika uygulamalar yapan bir <b>Yazılım Geliştiricisi</b> olmayı hedefliyorum. 
    Aynı zamanda <b>YalixGamer</b> kanalımda oyun maceralarımı paylaşıyorum. 🎮✈️<br><br>
    Evdeki en iyi dostum ise gri tüylü kedim <b>Ponpon</b>! 🐱
    </p>
</div>
""", unsafe_allow_html=True)

# --- YENİ ÖZELLİK: MESAJ BIRAKIN (CONTACT) ---
st.markdown("### ✉️ Leave a Message for Yiğit Ali")
visitor_name = st.text_input("Your Name / Adınız:")
visitor_message = st.text_area("Your Message / Mesajınız:")
if st.button("📩 SEND MESSAGE"):
    if visitor_name and visitor_message:
        st.success(f"Teşekkürler {visitor_name}! Mesajın CEO'muza iletildi. 😎")
    else:
        st.error("Lütfen adınızı ve mesajınızı yazın!")

# --- VİDEO VE YOUTUBE ---
st.divider()
st.markdown("## 📺 Latest Adventure on YalixGamer")
st.video("https://www.youtube.com/watch?v=833sZ0qW83Q")
st.link_button("📺 VISIT YALIXGAMER CHANNEL", "https://www.youtube.com/@Yalixgamer")

# İmza
st.caption("© 2026 Yalix Easy Software Co. | CEO: Yiğit Ali Arslan Doğan")
