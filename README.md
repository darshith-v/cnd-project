# AI-Powered Spelling Correction and Text Suggestion

This project is a Flask-based web application that provides **spelling correction** and **AI-generated text suggestions** using `TextBlob` and the `distilGPT-2` model from the `transformers` library.

## Features

- **Spelling Correction**: Automatically corrects spelling errors in user-provided text using `TextBlob`.
- **AI Text Suggestions**: Generates AI-based text continuations using the `distilGPT-2` model.
- **Web Interface**: A user-friendly web interface for inputting text and viewing results.

## Project Structure
cnd-project-main/ ├── app.py # Main application file ├── Dockerfile # Docker configuration for containerized deployment ├── requirements.txt # Python dependencies ├── templates/ │ └── index.html # HTML template for the web interface


## Prerequisites

- Python 3.9 or higher
- Docker (optional, for containerized deployment)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd cnd-project-main

2.Install dependencies:

pip install -r requirements.txt

3. Run the application:
  python app.py

4.Open your browser and navigate to http://127.0.0.1:5000.

Usage
1.Enter text into the input box on the web page.
2.Click the Correct and Suggest button.
3.View the corrected text and AI-generated suggestions.

Docker Deployment
1. Build the Docker image:
   docker build -t ai-spelling-correction .
2. Run the Docker container:
   docker run -p 5000:5000 ai-spelling-correction

Dependencies
The project uses the following Python libraries:

Flask==2.3.2
textblob==0.15.3
transformers==4.31.0
torch==2.0.1
numpy==1.24.4

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
TextBlob for spelling correction.
Hugging Face Transformers for AI text generation.
   
5. Open your browser and navigate to http://127.0.0.1:5000.


   
