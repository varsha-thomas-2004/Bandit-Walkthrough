import streamlit as st

st.title("Level 12 → Level 13")

st.write("### Level Goal:")
st.write("The password for the next level is stored in the file **data.txt**, which is a hexdump of a file that has been repeatedly compressed.")

expand = st.expander("💡 **Hint 1**")
expand.write("* You are about to witness a massacre, better create a temporary folder and copy data.txt. 🔪")
expand = st.expander("💡 **Hint 2**")
expand.write("* AAAAAAHHHHH I can't **read** hexdump!!! 😵")
expand = st.expander("💡 **Hint 3**")
expand.write("* Are you unzipping the right zip? 🤐"
"\n* I know it's tedious, but you've got this! Don't give up! 💪")

if st.checkbox("I give up 🥹"):
    expand = st.expander("You gave up already!? 😭")
    expand.write("* Make a temporary folder using `mktemp -d` and copy data.txt to that folder." \
    "\n* `xxd -r data.txt output` stores hex dump from data.txt to output." \
    "\n* Find the file type of output, rename it with the extension you got from the file type." \
    "\n* Unzip as per the file type.")