import streamlit as st

st.title("Level 0")

st.write("### Level Goal:")
st.write("The goal of this level is for you to log into the game using SSH. The host to which you need to connect is **bandit.labs.overthewire.org**, on **port 2220**. The username is bandit0 and the password is **bandit0**.")

expand = st.expander("💡 **Hint**")
expand.write("\nYou are given with three things:\n" \
"* ssh\n" \
"* bandit.labs.overthewire.org\n" \
"* Port number\n" \
"\nRead the manual for ssh and connect the above dots! 🤗")

if st.checkbox("I give up 🥹"):
    expand = st.expander("You gave up already!? 😭")
    expand.write("`ssh bandit0@bandit.labs.overthewire.org -p 2220`")