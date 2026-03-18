import streamlit as st
from gtts import gTTS
import io

# Sayfa Ayarları
st.set_page_config(page_title="Yalix Easy", page_icon="🦁")

# --- GALATASARAY TASARIMI (CSS) ---
st.markdown("""
    <style>
    .stButton>button {
        background-color: #A32638; /* GS Kırmızısı */
        color: #FDB912; /* GS Sarısı */
        border-radius: 20px;
        border: 2px solid #FDB912;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #FDB912;
        color: #A32638;
    }
    h1 { color: #FDB912; }
    h3 { color: #A32638; }
    </style>
    """, unsafe_allow_stdio=True)

# Başlık
st.title("🦁 Yalix Easy: GS Edition")
st.markdown("### *Şampiyonların Seslendirme Uygulaması*")

# --- DİL SEÇİMİ ---
language_option = st.selectbox("Dil Seçin / Select Language:", ("Turkish", "English"))
lang_code = 'tr' if language_option == "Turkish" else 'en'

# Yazı Giriş Kutusu
user_text = st.text_area("Metninizi buraya yazın:", placeholder="Şampiyon Galatasaray!...", height=150)

# Seslendirme ve İndirme
if st.button("🚀 SESLENDİR VE İNDİR", use_container_width=True):
    if user_text:
        with st.spinner("Yalix Easy hazırlanıyor..."):
            tts = gTTS(text=user_text, lang=lang_code)
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            audio_bytes = audio_fp.getvalue()
            
            st.audio(audio_bytes, format='audio/mp3')
            
            st.download_button(
                label="📥 DOSYAYI İNDİR (MP3)",
                data=audio_bytes,
                file_name=f"yalix_easy_gs.mp3",
                mime="audio/mp3",
                use_container_width=True
            )
    else:
        st.warning("Lütfen önce bir metin yazın patron!")

# --- YOUTUBE BUTONU ---
st.divider()
st.link_button("📺 YALIXGAMER YOUTUBE KANALI", "https://www.youtube.com/@Yalixgamer", use_container_width=True)

# İmza
st.caption("© 2026 Yalix Easy Software Co. | CEO: Yiğit Ali Arslan Doğan")
