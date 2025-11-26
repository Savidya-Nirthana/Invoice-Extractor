from google import genai
from google.genai import types
import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image


load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title="Invoice Extractor", page_icon=":robot:")


def get_gemini_response(system_instruction, user_instruction, image):
    try:
        if not API_KEY:
            st.error("API Key not found. Please set the GOOGLE_API_KEY environment variable.")
            return None
        
        client = genai.Client(api_key=API_KEY)


        mime_type = image.type
        image_byte = image.getvalue()

        response = client.models.generate_content(
            model="gemini-2.5-pro", 
            contents=[
                types.Part.from_bytes(
                    data=image_byte,
                    mime_type=mime_type,
                ),
                types.Part.from_text(
                    text=f"{system_instruction}\n\nUser Question: {user_instruction}",
                ),
            ],
        )
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"
    


st.header("Invoice Extractor using Google Gemini")
input_text = st.text_input("Enter your instruction:", "Extract key details from the invoice.")
uploaded_file = st.file_uploader("Upload an invoice image:", type=["png", "jpg", "jpeg"])


image_upload=None

if uploaded_file is not None:
    image_upload = Image.open(uploaded_file)
    st.image(image_upload, caption="Uploaded Invoice", use_column_width=True)

submit = st.button("Analyze Invoice")

input_prompt = """
You are an expert in understanding invoices. 
You will receive input images of invoices and you must answer questions based on the invoice provided. 
If the information is not clearly visible, admit that you cannot see it.
"""

if submit:
    if image_upload is None:
        st.error("Please upload an invoice image.")
    elif not input_text:
        st.warning("Please enter a question about the invoice.")
       
    else:
        with st.spinner("Analyzing invoice..."):
            response = get_gemini_response(input_prompt, input_text, uploaded_file)
            
            st.subheader("Analysis Result")
            st.write(response)