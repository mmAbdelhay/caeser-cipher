# filepath: /Users/abdelhaym/projects/caeser-cipher/app.py
import streamlit as st
import requests

API_BASE_URL = "http://localhost:8000"

def main():
    st.title("Caesar Cipher Web App")

    file = st.file_uploader("Choose a file")
    shift = st.number_input("Shift", min_value=0, max_value=25)

    if st.button("Encrypt"):
        if file is not None:
            files = {"file": file.getvalue()}
            data = {"shift": shift}
            response = requests.post(f"{API_BASE_URL}/encrypt/", files=files, data=data)
            if response.status_code == 200:
                encrypted_text = response.json().get("encrypted_text", "")
                st.success(f"Encrypted: {encrypted_text}")
            else:
                st.error("Encryption failed")
        else:
            st.error("File not found")

    if st.button("Decrypt"):
        if file is not None:
            files = {"file": file.getvalue()}
            response = requests.post(f"{API_BASE_URL}/decrypt/", files=files)
            if response.status_code == 200:
                data = response.json()
                decrypted_text = data.get("decrypted_text", "")
                best_shift = data.get("best_shift", shift)
                st.success(f"Decrypted: {decrypted_text}\nShift: {best_shift}")
            else:
                st.error("Decryption failed")
        else:
            st.error("File not found")

if __name__ == "__main__":
    main()