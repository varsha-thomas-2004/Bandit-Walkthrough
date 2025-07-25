import streamlit as st

st.title("Level 10 → Level 11")

st.write("### Level Goal:")
st.write("The password for the next level is stored in the file **data.txt**, which contains base64 encoded data.")

expand = st.expander("💡 **Hint**")
expand.write("* Just decode the data"
"\n* Maybe consider some readability too?")

if st.checkbox("I give up 🥹"):
    expand = st.expander("You gave up already!? 😭")
    expand.write("`strings data.txt | base64 -d`")