import streamlit as st

st.title("Level 3 → Level 4")

st.write("### Level Goal:")
st.write("The password for the next level is stored in a hidden file in the **inhere** directory.")

expand = st.expander("💡 **Hint 1**")
expand.write("Did you get in the **inhere** directory? 🤨")

expand = st.expander("💡 **Hint 2**")
expand.write("Try **finding** the hidden file 👀")

if st.checkbox("I give up 🥹"):
    expand = st.expander("You gave up already!? 😭")
    expand.write("* `cd inhere`\n" \
    "* `find`\n" \
    "* `cat ./...Hiding-From-You`")