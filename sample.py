from flask import Flask , redirect, url_for, request, render_template
app=Flask(__name__)


# @app.route("/")
# def admin():
#     return "admin"

# @app.route("/name")
# def name():
# #     return "hello devi"


# def hello_world():
#     return "hello word"
# app.add_url_rule('/hello','hello',hello_world)

# variable routing
# @app.route("/user/<name>")
# def user(name):
#     # return f"hello {name}"
# @app.route("/user/<int:id>")
# def user(id):
# #     return f"user {id}"
# @app.route("/revision/<float:rev no>")
# def revision(rev_no):
#     return f"revision number {rev_no}"


# # url building
# @app.route("/admin")
# def admin():
#     return "admin page"
# @app.route("/guest")
# def guest():
#     return "guest page"
# @app.route("/user/<name>")
# def user(name):
#     if name == "admin":
#         return redirect(url_for(admin()))
#     else:
#         return redirect(url_for(guest()))


# http methods
@app.route("/login", methods=["GET"])
def login():
    uname = request.form.get('uname')
    password = request.form.get('password')
    if uname =="devi" and password=="1234":
        return f"Welcome {uname}"
    else:
        return f"invalid {uname} "

# @app.route('/hello/<user>')
# def hello_name(user):
#    return render_template('hello.html', name = user)


if __name__ == "__main__":
    app.run(debug=True)  