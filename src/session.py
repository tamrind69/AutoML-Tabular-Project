import streamlit as st

DEFAULT_SESSION_STATE = {
    "uploaded_csv" : None
}

def initialze_session():
    for key,value in DEFAULT_SESSION_STATE.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_session():
    '''
    reset dependent info
    '''