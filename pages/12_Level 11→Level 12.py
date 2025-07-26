import streamlit as st

st.title("Level 11 → Level 12")

st.write("### Level Goal:")
st.write("The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions.")

expand = st.expander("💡 **Hint**")
expand.write("* Sounds like pure **translation** to me! 😌")

if st.checkbox("I give up 🥹"):
    expand = st.expander("You gave up already!? 😭")
    expand.write("`cat data.txt | tr 'N-ZA-Mn-za-m' 'A-Za-z'`")