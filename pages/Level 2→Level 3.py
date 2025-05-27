import streamlit as st

st.title("Level 2 → Level3")

st.write("### Level Goal:")
st.write("The password for the next level is stored in a file called **spaces in this filename** located in the home directory")

expand = st.expander("💡 **Hint**")
expand.write('Heard of " " ?')

if st.checkbox("I give up 🥹"):
    expand = st.expander("You gave up already!? 😭")
    expand.write('`cat "spaces in this filename"`')