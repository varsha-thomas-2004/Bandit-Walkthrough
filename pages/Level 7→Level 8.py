import streamlit as st

st.title("Level 7 → Level 8")

st.write("### Level Goal:")
st.write("The password for the next level is stored in the file **data.txt** next to the word **millionth**.")

expand = st.expander("💡 **Hint 1**")
expand.write("* Does **millionth** seem like a 'pattern' to you?")
expand = st.expander("💡 **Hint 2**")
expand.write("* Read the man page of grep")

if st.checkbox("I give up 🥹"):
    expand = st.expander("You gave up already!? 😭")
    expand.write("`grep -i 'millionth' data.txt`")