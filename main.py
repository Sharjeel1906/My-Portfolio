from flask import Flask,render_template,url_for,request
from contact import send_response
import os
app = Flask(__name__)
response  = send_response()
form_link = " https://docs.google.com/forms/d/e/1FAIpQLSeF5QdXPA8h7_Sw11gHSY2d7XxDB3GaxSFOhxbBojUpSPTEng/viewform?usp=sharing&ouid=116599140460711299047"
visitor = "visitor.txt"
TEXT_FILE = "form_data.txt"

def handler(request, response):
    return handle_request(app, request, response)

def update_visitor_count():
    try:
        count = int(open(visitor).read()) + 1
    except(FileNotFoundError,ValueError):
        count=1
    with open(visitor, "w") as f:
        f.write(str(count))
    return count

@app.route("/")
def home():
    no_of_visitor  = update_visitor_count()
    return render_template("index.html",num=no_of_visitor)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        with open(TEXT_FILE, "a", encoding="utf-8") as file:
            file.write(f"{name:<20} {email:<30} {subject:<20} {message}\n")
        #response.fill_form(name, email, subject, message)
        return "Message has been sent. Thank you!"

    # GET request → render the form
    return render_template("contact.html")


@app.route("/project/<name>")
def project(name):
    projects = {
        "data_entry": {"title": "Automated Data Entry", "video": "automated data entry.mp4"},
        "text_description": {"title": "Image Description", "video": "text_description.mp4"},
        "stacky_trend": {"title": "Stacky Trend", "video": "stacky_trend.mp4"},
        "quizzler": {"title": "Quizler App", "video": "quizzler.mp4"},
        "ecommerce": {"title": "Ecommerce App", "video": "ecommerce.mp4"},
        "movie_info":{"title":"Movie Info App","video":"movie_info.mp4"},
        "ai_chat_app":{"title":"AI Chat App","video":"ai_chat_app.mp4"},
        "billspot":{"title":"BillSpot","video":"billspot.mp4"}
    }
    project = projects.get(name)
    if not project:
        return "Project not found", 404
    return render_template("general.html", **project)


if __name__ == "__main__":
    app.run(debug=True)
