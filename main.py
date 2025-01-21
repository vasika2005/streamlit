import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected=option_menu(
        menu_title="vinsup",
        options=["Home","About","Contact"],
        icons=["house-fill","file-person","person-lines-fill"]

    )
if selected=="Home":
    st.title("Home page")
elif selected=="About":
    st.title("About page")
elif selected=="Contact":
    st.title("Contact page")
        
# st.title("📚💻✍🏼📓Vinsup info tech")
# st.header("🗣Full Stack")
# st.write("### My text")
# st.write("- _My text 1_")
# st.code("""
#     #include <stdio.h>
# int main() {
#    // printf() displays the string inside quotation
#    printf("Hello, World!");
#    return 0;
# }

# """,language="c")

# with st.sidebar:
#     name=st.text_input("enter name")
#     st.button("click me")
#     st.write(name)
#     st.balloons()

# col1,col2,col3=st.columns(3)
# with col1:
#     st.metric("vinsup", "python", 30)
# with col2:
#     st.metric("vinsup", "python",- 30)
# with col3:
#     st.metric("vinsup", "python",30)
