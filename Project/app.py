from flask import Flask, render_template, request
from textblob import TextBlob
from transformers import pipeline

app = Flask(__name__)

# Load the distilGPT-2 model
generator = pipeline('text-generation', model='distilgpt2')

@app.route('/', methods=['GET', 'POST'])
def index():
    corrected_text = ""
    ai_suggested_text = ""
    
    if request.method == 'POST':
        user_text = request.form['text']
        
        # Basic spelling correction using TextBlob
        blob = TextBlob(user_text)
        corrected_text = str(blob.correct())
        
        # Simple AI-based text suggestion using distilGPT-2
        ai_suggestion = generator(corrected_text, max_length=50, num_return_sequences=1)[0]['generated_text']
        ai_suggested_text = ai_suggestion[len(corrected_text):]  # Show only the AI continuation
    
    return render_template('index.html', corrected_text=corrected_text, ai_suggested_text=ai_suggested_text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
