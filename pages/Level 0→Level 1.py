import streamlit as st

st.title("Level 0 → Level 1")

st.write("### Level Goal:")
st.write("The password for the next level is stored in a file called **readme** located in the home directory.")

expand = st.expander("💡 **Hint**")
expand.write("Read the manual for cat")

if st.checkbox("I give up 🥹"):
    expand = st.expander("You gave up already!? 😭")
    expand.write("`cat readme`")