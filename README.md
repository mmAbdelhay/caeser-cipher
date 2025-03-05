# Caesar Cipher Web App

This project is a web application that allows users to encrypt and decrypt text files using the Caesar Cipher algorithm. The backend is built with FastAPI, and the frontend is built with Streamlit.

## Features

- Encrypt text files using the Caesar Cipher algorithm.
- Decrypt text files using the Caesar Cipher algorithm.
- Automatically determine the best shift value for decryption.

## Requirements

- Python 3.7 or higher
- FastAPI
- Uvicorn
- Streamlit
- Requests
- Python-Multipart

## Installation

Follow these steps to set up and run the project:

### 1. Clone the repository

```sh
git clone https://github.com/your-username/caesar-cipher.git
cd caesar-cipher
```

### 2. Create a virtual environment

Create a virtual environment to manage the project's dependencies:

```sh
python -m venv venv
```

### 3. Activate the virtual environment

Activate the virtual environment:

- On Windows:

```sh
venv\Scripts\activate
```

- On macOS and Linux:

```sh
source venv/bin/activate
```

### 4. Install the requirements

Install the required packages using the requirments.txt file:

```sh
pip install -r requirments.txt
```

## Running the Project
### 1. Start the FastAPI backend

Run the FastAPI backend using Uvicorn:

```sh
uvicorn main:app --reload
```

The backend will be available at http://localhost:8000.

### 2. Start the Streamlit frontend

In a new terminal window, run the Streamlit frontend:

```sh
streamlit run app.py
```

The frontend will be available at the URL provided by Streamlit (usually http://localhost:8501).

## Usage
1.Open the Streamlit web app in your browser.
2.Upload a text file.
3.Enter a shift value for encryption.
4.Click the "Encrypt" button to encrypt the file.
5.Click the "Decrypt" button to decrypt the file.
6.Click the "Reset" button to reset the app.

## File Structure
- main.py: FastAPI backend implementation.
- app.py: Streamlit frontend implementation.
- requirments.txt: List of required packages.