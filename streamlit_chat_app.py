import streamlit as st

# Initialize session state for received texts
if 'received_texts' not in st.session_state:
    st.session_state['received_texts'] = []

# Function to handle text submission
def submit_text():
    text_data = st.session_state.text_input
    if text_data:
        st.session_state.received_texts.append(text_data)
        st.session_state.text_input = ""  # Clear input field

# Streamlit app layout
st.title("Text Receiver")

# Input form
with st.form(key='text_form', clear_on_submit=True):
    st.text_input("Enter Text:", key='text_input')
    submit_button = st.form_submit_button(label='Submit', on_click=submit_text)

# Display received texts
if st.session_state.received_texts:
    st.header("Received:")
    for text in st.session_state.received_texts:
        st.write(text)