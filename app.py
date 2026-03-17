import streamlit as st

# 1. Sayfa Ayarları (Karanlık Mod ve Başlık)
st.set_page_config(page_title="Yalix Easy", page_icon="🎙️", layout="centered")

# 2. Şirket Logosu ve Sloganı
st.title("🎙️ Yalix Easy")
st.markdown("### *Type it. Hear it. Easy.*")

# 3. Kullanıcı Giriş Alanı (Senin istediğin o sade tasarım)
user_text = st.text_area("Enter your text below:", placeholder="Welcome to Yalix Easy! The best app in the world...", height=200)

# 4. Basit Ses Seçenekleri
st.write("Choose your voice style:")
col1, col2, col3 = st.columns(3)
with col1:
    gamer = st.checkbox("Gamer Voice 🎮")
with col2:
    alien = st.checkbox("Alien Voice 👽")
with col3:
    robot = st.checkbox("Fast Robot 🤖")

# 5. O Efsanevi Büyük Buton
st.divider() # Araya şık bir çizgi çeker
if st.button("🚀 CONVERT TO VOICE", use_container_width=True):
    if user_text:
        st.success("Yalix Easy is processing your request... Done! 😎")
        # Burası ileride sesi gerçekten çalacak olan kısım!
    else:
        st.warning("Please enter some text first, Boss!")

# 6. Alt Bilgi
st.caption("© 2026 Yalix Easy Software Co. | Developed by Yiğit Ali Arslan Doğan")
