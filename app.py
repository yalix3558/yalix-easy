import streamlit as st
from gtts import gTTS
import io

# Sayfa Ayarları
st.set_page_config(page_title="Yalix Easy", page_icon="🦁")

# --- GALATASARAY TASARIMI (CSS) ---
# Burada "unsafe_allow_html" kullanarak hatayı düzelttik!
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
    }
    .stButton>button {
        background-color: #A32638 !important; /* GS Kırmızısı */
        color: #FDB912 !important; /* GS Sarısı */
        border-radius: 20px;
        border: 2px solid #FDB912 !important;
        font-weight: bold;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #FDB912 !important;
        color: #A32638 !important;
    }
    h1, h3 { color: #FDB912 !important; }
    label { color: #FDB912 !important; }
    </style>
    """, unsafe_allow_html=True)

# Başlık
st.title("🦁 Yalix Easy: GS Edition")
st.markdown("### *Şampiyonların Seslendirme Uygulaması*")

# --- DİL SEÇİMİ ---
language_option = st.selectbox("Dil Seçin / Select Language:", ("Turkish", "English"))
lang_code = 'tr' if language_option == "Turkish" else 'en'

# Yazı Giriş Kutusu
user_text = st.text_area("Metninizi buraya yazın:", placeholder="Şampiyon Galatasaray!...", height=150)

# Seslendirme ve İndirme Bölümü
if st.button("🚀 SESLENDİR VE İNDİR"):
    if user_text:
        with st.spinner("Yalix Easy sesi hazırlıyor..."):
            tts = gTTS(text=user_text, lang=lang_code)
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            audio_bytes = audio_fp.getvalue()
            
            # Sesi Oynat
            st.audio(audio_bytes, format='audio/mp3')
            
            # Sesi İndir
            st.download_button(
                label="📥 SES DOSYASINI İNDİR (MP3)",
                data=audio_bytes,
                file_name=f"yalix_easy_audio.mp3",
                mime="audio/mp3"
            )
            st.success("Ses hazır, keyfini çıkar patron! 😎")
    else:
        st.warning("Lütfen önce bir metin yazın!")

# --- YOUTUBE BUTONU ---
st.divider()
st.link_button("📺 YALIXGAMER YOUTUBE KANALI", "https://www.youtube.com/@Yalixgamer")

# İmza
st.caption("© 2026 Yalix Easy Software Co. | CEO: Yiğit Ali Arslan Doğan")
