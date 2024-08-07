from flask import Flask, request, render_template

app = Flask(__name__)

from models.pipes import run_pipe

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        processed_prompt = run_pipe(prompt)
        return f"Processed prompt: {processed_prompt}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)