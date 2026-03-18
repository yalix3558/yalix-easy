import streamlit as st
from gtts import gTTS
import io

# Sayfa Ayarları
st.set_page_config(page_title="Yalix Easy", page_icon="🎙️")

# Başlık ve Tasarım
st.title("🎙️ Yalix Easy")
st.markdown("### *Type it. Hear it. Easy.*")

# --- DİL SEÇİMİ ---
language_option = st.selectbox(
    "Select Language / Dil Seçin:",
    ("English", "Turkish")
)

lang_code = 'en' if language_option == "English" else 'tr'

# Yazı Giriş Kutusu
placeholder_text = "Type something..." if lang_code == 'en' else "Bir şeyler yazın..."
user_text = st.text_area(f"Enter {language_option} text:", placeholder=placeholder_text, height=150)

# Seslendirme ve İndirme Bölümü
if st.button("🚀 CONVERT TO VOICE", use_container_width=True):
    if user_text:
        with st.spinner("Yalix Easy is processing..."):
            tts = gTTS(text=user_text, lang=lang_code)
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            audio_bytes = audio_fp.getvalue()
            
            st.audio(audio_bytes, format='audio/mp3')
            
            st.download_button(
                label=f"📥 DOWNLOAD {language_option} AUDIO",
                data=audio_bytes,
                file_name=f"yalix_easy_{lang_code}.mp3",
                mime="audio/mp3",
                use_container_width=True
            )
            st.success("Quality sound is ready! 😎")
    else:
        st.warning("Please enter some text first!")

# --- YENİ ÖZELLİK: YOUTUBE BUTONU ---
st.divider() # Araya şık bir çizgi çeker
st.markdown("### 📢 Stay Connected!")
youtube_url = "https://www.youtube.com/@Yalixgamer" # Senin kanal linkin

st.link_button("📺 FOLLOW ME ON YOUTUBE (YalixGamer)", youtube_url, use_container_width=True, type="primary")

# Şirket İmzası
st.caption("© 2026 Yalix Easy Software Co. | CEO: Yiğit Ali Arslan Doğan")
