from fastapi import FastAPI, UploadFile, File, Form
import string
import numpy as np

app = FastAPI()

def caesar_cipher(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# English letter frequency distribution
ENGLISH_FREQ = {
    'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70, 'f': 2.23, 'g': 2.02, 'h': 6.09, 'i': 6.97,
    'j': 0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93, 'q': 0.10, 'r': 5.99,
    's': 6.33, 't': 9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97, 'z': 0.07
}

def letter_frequencies(text: str):
    text = text.lower()
    total_letters = sum(c.isalpha() for c in text)
    freq = {char: 0 for char in string.ascii_lowercase}
    
    for char in text:
        if char in freq:
            freq[char] += 1
    
    if total_letters > 0:
        for char in freq:
            freq[char] = (freq[char] / total_letters) * 100
    
    return list(freq.values())

def find_best_shift(text: str):
    best_shift = 0
    best_corr = -1
    eng_freq_list = list(ENGLISH_FREQ.values())
    
    for shift in range(26):
        decrypted_text = caesar_cipher(text, -shift)
        text_freq = letter_frequencies(decrypted_text)
        
        correlation = np.corrcoef(text_freq, eng_freq_list)[0, 1]
        if correlation > best_corr:
            best_corr = correlation
            best_shift = shift
    
    return best_shift

@app.post("/encrypt/")
async def encrypt_text(file: UploadFile = File(...), shift: int = Form(...)):
    content = await file.read()
    encrypted_text = caesar_cipher(content.decode("utf-8"), shift)
    return {"encrypted_text": encrypted_text}

@app.post("/decrypt/")
async def decrypt_text(file: UploadFile = File(...)):
    content = await file.read()
    best_shift = find_best_shift(content.decode("utf-8"))
    decrypted_text = caesar_cipher(content.decode("utf-8"), -best_shift)
    return {"best_shift": best_shift, "decrypted_text": decrypted_text}
