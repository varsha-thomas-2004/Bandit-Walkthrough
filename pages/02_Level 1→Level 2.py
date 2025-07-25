import streamlit as st

st.title("Level 1 → Level 2")

st.write("### Level Goal:")
st.write("The password for the next level is stored in a file called **-** located in the home directory")

expand = st.expander("💡 **Hint**")
expand.write("Read the manual for cat, or maybe give a google search 🧐")

if st.checkbox("I give up 🥹"):
    expand = st.expander("You gave up already!? 😭")
    expand.write("`cat < -`")