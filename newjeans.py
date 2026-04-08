import streamlit as st

st.set_page_config(page_title="NJWMX - NewJeans Finder", page_icon="🐰")

st.title("🐰 NewJeans Bias & Song Finder")
st.write("yuk cari tau bias dan lagu yang cocok buat nemenin harimu!")

tab1, tab2 = st.tabs(["cari bias", "rekomendasi lagu"])

with tab1:
    st.header("siapa biasmu di NewJeans?")
    vibes = st.radio(
        "pilih vibe yang paling menggambarkan dirimu:",
        ["keren & sporty", "ceria & enerjik", "kalem & estetik", "lucu & random", "chic & elegan"]
    )

    if st.button("biasmu adalah ..."):
        
        if vibes == "keren & sporty":
            st.success("biasmu mungkin adalah **Minji**! leader yang punya aura cool.")
        elif vibes == "ceria & enerjik":
            st.success("biasmu mungkin adalah **Hanni**! si vitamin yang selalu penuh semangat.")
        elif vibes == "kalem & estetik":
            st.success("biasmu mungkin adalah **Haerin**! si kucing yang tenang tapi punya aura unik.")
        elif vibes == "lucu & random":
            st.success("biasmu mungkin adalah **Hyein**! maknae yang tinggi tapi tingkahnya menggemaskan.")
        else:
            st.success("biasmu mungkin adalah **Danielle**! si 'sunshine' yang selalu ramah dan stylish.")

with tab2:
    st.header("lagu apa ya yang cocok?")
    suasana = st.selectbox(
        "lagi ngapain sekarang?",
        ["lagi kesemsem", "lagi pengen chill", "lagi have a crush on someone", "lagi loyo butuh semangat"]
    )

    if st.button("cek lagu"):
        if suasana == "lagi kesemsem":
            st.info("Kamu harus dengerin: **'Ditto'** ❄️ (vibe nostalgic & dreamy banget!)")
        elif suasana == "lagi pengen chill":
            st.info("Kamu harus dengerin: **'Hype Boy'** 👟 (lagu wajib buat vibing!)")
        elif suasana == "lagi have a crush on someone":
            st.info("Kamu harus dengerin: **'Attention'** ✨ (Kasih perhatian dikit dong!)")
        else:
            st.info("Kamu harus dengerin: **'Super Shy'** 🎀 (Biar makin pede!)")
            
    st.image("https://www.nme.com/wp-content/uploads/2023/01/newjeans-get-up-ep.jpg", caption="NewJeans Bunnies!")