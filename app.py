import streamlit as st
from gtts import gTTS
import io

# Sayfa Ayarları
st.set_page_config(page_title="Yalix Easy", page_icon="🎙️")

# Başlık ve Tasarım
st.title("🎙️ Yalix Easy")
st.markdown("### *Type it. Hear it. Easy.*")

# Yazı Giriş Kutusu
user_text = st.text_area("Enter your text here:", placeholder="Type something cool...", height=150)

# Seslendirme ve İndirme Bölümü
if st.button("🚀 CONVERT TO VOICE", use_container_width=True):
    if user_text:
        with st.spinner("Yalix Easy is processing..."):
            # 1. Metni sese çevir
            tts = gTTS(text=user_text, lang='en')
            
            # 2. Sesi hafızaya kaydet
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            audio_bytes = audio_fp.getvalue()
            
            # 3. SESİ OYNAT
            st.audio(audio_bytes, format='audio/mp3')
            
            # 4. YENİ ÖZELLİK: SESİ İNDİR BUTONU
            st.download_button(
                label="📥 DOWNLOAD AUDIO (MP3)",
                data=audio_bytes,
                file_name="yalix_easy_audio.mp3",
                mime="audio/mp3",
                use_container_width=True
            )
            
            st.success("Perfect! You can play or download your voice now. 😎")
    else:
        st.warning("Please enter some text first, Boss!")

# Şirket İmzası
st.caption("© 2026 Yalix Easy Software Co. | CEO: Yiğit Ali Arslan Doğan")
