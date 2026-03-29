from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')  # templates folder me index.html ko load karega

if __name__ == '__main__':
    app.run(debug=True)  # debug=True se har change ke baad reload easy hota hai