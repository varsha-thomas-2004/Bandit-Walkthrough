import streamlit as st

st.title("Level 5 → Level 6")

st.write("### Level Goal:")
st.write("The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:\n" \
    "* human-readable \n" \
    "* 1033 bytes in size \n" \
    "* not executable")

expand = st.expander("💡 **Hint**")
expand.write("**find** the file that has size 1033 bytes.")

if st.checkbox("I give up 🥹"):
    expand = st.expander("You gave up already!? 😭")
    expand.write("* `find -size 1033c`\n" \
    "* You should be knowing what to do after this 🤨")