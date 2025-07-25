import streamlit as st

st.title("Level 8 → Level 9")

st.write("### Level Goal:")
st.write("The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once.")

expand = st.expander("💡 **Hint 1**")
expand.write("* The password is **unique** indeed!")
expand = st.expander("💡 **Hint 2**")
expand.write("* Uh oh, does everything in it seem unique? Why not try sorting it?"
"\n* Search about piping")

if st.checkbox("I give up 🥹"):
    expand = st.expander("You gave up already!? 😭")
    expand.write("`sort data.txt | uniq -u`")