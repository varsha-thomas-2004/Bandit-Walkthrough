import streamlit as st

st.title("Level 4 → Level 5")

st.write("### Level Goal:")
st.write("The password for the next level is stored in the only human-readable file in the inhere directory.")

expand = st.expander("💡 **Hint**")
expand.write("Try a smart way to get the **file type** of all files, give a Google search if needed ☺️")

if st.checkbox("I give up 🥹"):
    expand = st.expander("You gave up already!? 😭")
    expand.write("* `file ./*`\n" \
    "* `cat < -file07`")