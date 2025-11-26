# Gemini Invoice Extractor

A smart invoice analysis tool built with Streamlit and Google Gemini 2.5. This application allows users to upload invoice images (PNG, JPG, JPEG) and ask natural language questions about them, such as "What is the total amount?" or "What is the invoice date?".

## Features

* **Image Support:** Upload invoices in JPG, JPEG, or PNG formats.
* **AI Analysis:** Uses Google's `gemini-2.5-pro` model for multimodal understanding.
* **Interactive Chat:** Ask specific questions about the uploaded document.
* **Secure Key Management:** Supports API keys via `.env` file, Streamlit Secrets, or direct sidebar input.

## Prerequisites

* Python 3.9 or higher
* A Google Cloud API Key ([Get one here](https://aistudio.google.com/))

## Installation

1.  **Clone the repository** (or download the files):
    ```bash
    git clone https://github.com/Savidya-Nirthana/Invoice-Extractor.git
    cd invoice-extractor
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    
    # On Windows
    venv\Scripts\activate
    
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    
    First, create a `requirements.txt` file with the following content:
    ```text
    streamlit
    google-genai
    python-dotenv
    Pillow
    ```

    Then run:
    ```bash
    pip install -r requirements.txt
    ```

