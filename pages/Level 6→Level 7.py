import streamlit as st

st.title("Level 6 → Level 7")

st.write("### Level Goal:")
st.write("The password for the next level is stored somewhere on the server and has all of the following properties:\n" \
"* owned by user bandit7\n" \
"* owned by group bandit6\n" \
"33 bytes in size")

expand = st.expander("💡 **Hint**")
expand.write("* We may NOT be given with the filetype, but should that bother you, dear Bandit? 😏\n"
"* I hope you **find** what you are looking for 😌 (go through the man page) \n"
"* Consider all the given points in the command")

if st.checkbox("I give up 🥹"):
    expand = st.expander("You gave up already!? 😭")
    expand.write("* `find / -type -f -user bandit7 -group bandit6 -size 33c`\n" \
    "* Now that you have the file, you know what to do!")