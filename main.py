from flask import Flask,render_template,url_for,request
from contact import send_response
app = Flask(__name__)

response  = send_response()
form_link = " https://docs.google.com/forms/d/e/1FAIpQLSeF5QdXPA8h7_Sw11gHSY2d7XxDB3GaxSFOhxbBojUpSPTEng/viewform?usp=sharing&ouid=116599140460711299047"

def update_visitor_count():
    try:
        count = int(open("visitor.txt").read())+1
    except(FileNotFoundError,ValueError):
        count=1
    with open("visitor.txt","w") as f:
        f.write(str(count))
    return count

@app.route("/")
def home():
    no_of_visitor  = update_visitor_count()
    return render_template("index.html",num=no_of_visitor)

@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        response.fill_form(name, email, subject, message)
        return "Message has been sent. Thank you!"

    # GET request → render the form
    return render_template("contact.html")

@app.route("/quizzler.html")
def quizzler():
    return render_template("quizzler.html")

@app.route("/automation.html")
def automation():
    return render_template("automation.html")

@app.route("/password.html")
def password():
    return render_template("password.html")

@app.route("/spotify.html")
def spotify():
    return render_template("spotify.html")

if __name__ == "__main__":
    app.run(debug=True)