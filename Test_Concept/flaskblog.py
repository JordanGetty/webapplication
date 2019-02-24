from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Bobby Flay',
        'title': 'Crimson Code Hackathon',
        'content': 'I know literally no code and my team dipped\
                    anyone wanna team?',
        'date_posted': 'February 23, 2019'
    },
    {
        'author': 'Andy OFallon',
        'title': 'Study group',
        'content': 'studying for 122 anyone wanna join\
                    ill be in EME 125',
        'date_posted': 'February 25, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/map")
def map():
    return render_template('about.html', title='Map')


@app.route("/sloan")
def sloan():
    return render_template('sloan.html', title='sloan')


@app.route("/dana")
def dana():
    return render_template('dana.html', title='dana')


@app.route("/eme")
def eme():
    return render_template('eme.html', title='eme')


if __name__ == '__main__':
    app.run(debug=True)
