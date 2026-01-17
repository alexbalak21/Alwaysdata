# Flask application that serves a React single-page application (SPA)

from flask import Flask, send_from_directory, render_template

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="templates/assets",
    static_url_path="/assets"
)


## Put the dist files from React build in the templates/ folder

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    # Serve static assets from templates/
    if path and (path.startswith("assets") or "." in path):
        return send_from_directory("templates", path)

    # Otherwise return index.html
    return render_template("index.html")

