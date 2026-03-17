import streamlit as st
from gtts import gTTS # Google'ın ses motorunu şirketimize bağlıyoruz
import io

# Sayfa Ayarları
st.set_page_config(page_title="Yalix Easy", page_icon="🎙️")

# Başlık ve Tasarım
st.title("🎙️ Yalix Easy")
st.markdown("### *Type it. Hear it. Easy.*")

# Yazı Giriş Kutusu
user_text = st.text_area("Enter your text here:", placeholder="Hello Yiğit Ali! Let's build the future...", height=150)

# Seslendirme Butonu
if st.button("🚀 CONVERT TO VOICE", use_container_width=True):
    if user_text:
        with st.spinner("Yalix Easy is thinking..."):
            # 1. Metni sese çeviriyoruz
            tts = gTTS(text=user_text, lang='en')
            
            # 2. Sesi hafızaya alıyoruz
            audio_data = io.BytesIO()
            tts.write_to_fp(audio_data)
            
            # 3. İŞTE SES BURADA! Siteye bir ses çalar ekliyoruz:
            st.audio(audio_data, format='audio/mp3')
            
            st.success("Now you can listen, Boss! 😎")
    else:
        st.warning("Please enter some text first!")

# Şirket İmzası
st.caption("© 2026 Yalix Easy Software Co. | CEO: Yiğit Ali Arslan Doğan")
