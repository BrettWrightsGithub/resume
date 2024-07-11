import streamlit as st
from pages import resume, ai_note_reviewer

def navigate_to(page):
    st.query_params["page"] = page
    st.experimental_rerun()

current_page = st.query_params.get("page", ["resume"])[0]

st.sidebar.title("Navigation")
if st.sidebar.button("Go to Resume"):
    navigate_to("resume")
if st.sidebar.button("Go to AI Note Reviewer"):
    navigate_to("ai_note_reviewer")

if current_page == "resume":
    resume.app()
elif current_page == "ai_note_reviewer":
    ai_note_reviewer.app()