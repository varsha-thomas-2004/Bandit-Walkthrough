import streamlit as st

st.title("Level 9 → Level 10")

st.write("### Level Goal:")
st.write("The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several '=' characters.")

expand = st.expander("💡 **Hint 1**")
expand.write("* I smell a **pattern** 😌")
expand = st.expander("💡 **Hint 2**")
expand.write("* Seems there are a lot of == patterns 🥴"
"\n* Did you see a human-readable **string**?")

if st.checkbox("I give up 🥹"):
    expand = st.expander("You gave up already!? 😭")
    expand.write("`strings data.txt | grep -i '=='`")