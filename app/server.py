from flask import Flask, render_template, send_file, request

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def home():
    return  render_template('home.html')

@app.route("/home.html")
def home_page():
    return render_template('home.html')

@app.route("/ourStory.html")
def ourStore():
    return  render_template('ourStory.html')

@app.route("/hotel.html")
def hotel():
    return  render_template('hotel.html')

@app.route("/info.html")
def info():
    return  render_template('info.html')

@app.route("/party.html")
def party():
    return  render_template('party.html')

@app.route("/seating.html")
def seating():
    return  render_template('seating.html')

@app.route("/rsvp.html", methods=['GET', 'POST'])
def rsvp():
    if request.method == 'GET':
        return  render_template('rsvp.html')
    elif request.method == 'POST':
        form_data = request.form
        file = open("rsvp.txt", "a")
        file.write(str(form_data['nameField']) + " " + str(form_data['attendanceField']) + " " + str(form_data['guestField']) + "\n")
        file.close()
        return render_template('rsvp.html')

@app.route("/static/background.jpg")
def background():
    return send_file('static/background.jpg', mimetype="image/jpg")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)