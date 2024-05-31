from flask import Flask, request, render_template, render_template_string, jsonify
from flask_cors import CORS
from flaskext.markdown import Markdown

app = Flask(__name__)
CORS(app)
Markdown(app)

# List to store received text messages
received_texts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global received_texts
    if request.method == 'POST':
        text_data = request.form['inputTextArea']
        # Convert markdown to HTML before appending
        html_text = render_template_string("{{ text_data | markdown }}", text_data=text_data)
        received_texts.append(html_text)
    return render_template('chat_ui.html')

@app.route('/messages', methods=['GET'])
def get_messages():
    global received_texts
    return jsonify(received_texts=received_texts[::-1])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8181)