Gemini Invoice ExtractorA smart invoice analysis tool built with Streamlit and Google Gemini 2.0. This application allows users to upload invoice images (PNG, JPG, JPEG) and ask natural language questions about them, such as "What is the total amount?" or "What is the invoice date?".FeaturesImage Support: Upload invoices in JPG, JPEG, or PNG formats.AI Analysis: Uses Google's gemini-2.0-flash-exp model for multimodal understanding.Interactive Chat: Ask specific questions about the uploaded document.Secure Key Management: Supports API keys via .env file, Streamlit Secrets, or direct sidebar input.PrerequisitesPython 3.9 or higherA Google Cloud API Key (Get one here)InstallationClone the repository (or download the files):git clone <repository-url>
cd invoice-extractor
Create a virtual environment (recommended):python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
Install dependencies:Create a requirements.txt file (if you haven't already) with the following content:streamlit
google-genai
python-dotenv
Pillow
Then run:pip install -r requirements.txt
ConfigurationYou can configure your API key in one of three ways:Option 1: .env file (Local Development)Create a file named .env in the root directory and add your key:GOOGLE_API_KEY=your_actual_api_key_here
Option 2: Sidebar Input (easiest)Simply run the app, and paste your API key into the text box that appears in the sidebar if no environment variable is found.Option 3: Streamlit Secrets (Cloud Deployment)If deploying to Streamlit Community Cloud, add your key to the secrets manager:[secrets]
GOOGLE_API_KEY = "your_actual_api_key_here"
UsageRun the Streamlit application:streamlit run app.py
The application will open in your default browser at http://localhost:8501.Upload an image of an invoice.Type your question (e.g., "List all items bought").Click Analyze Invoice.Project Structureapp.py: The main application script containing the UI and logic..env: Configuration file for environment variables (do not commit this to GitHub).requirements.txt: List of Python dependencies.README.md: Project documentation.TroubleshootingError 400 (API Key): Ensure your API key is valid and does not contain extra spaces.Image Errors: Ensure the uploaded file is a valid image (PNG/JPG) and not a PDF.
