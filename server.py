from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def main():
    username = request.args.get("username", "Guest")
    template = f"<h1>Hello {username}!</h1>"
    return render_template_string(template)

if __name__ == "__main__":
    app.run(debug=True)
