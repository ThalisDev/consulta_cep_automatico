from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Winmed_API',
        year=datetime.now().year,
    )


if __name__ == '__main__':
    app.run()
