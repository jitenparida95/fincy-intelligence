import streamlit as st

if "active_module" not in st.session_state:
    st.session_state.active_module = None

query = st.query_params
if "module" in query:
    st.session_state.active_module = query["module"]

def back():
    if st.button("Back"):
        st.session_state.active_module = None
        st.rerun()

m = st.session_state.active_module

if m is None:
    st.title("Fincy Intelligence")
    if st.button("FP&A"): st.session_state.active_module="fpa"; st.rerun()
    if st.button("Recon"): st.session_state.active_module="recon"; st.rerun()
    if st.button("Budget"): st.session_state.active_module="budget"; st.rerun()
    if st.button("Cost"): st.session_state.active_module="cost"; st.rerun()

elif m=="fpa":
    back()
    st.title("FP&A")
    f=st.file_uploader("Upload")
    if f: st.success("Uploaded")

elif m=="recon":
    back()
    st.title("Recon")

elif m=="budget":
    back()
    st.title("Budget")

elif m=="cost":
    back()
    st.title("Cost")
