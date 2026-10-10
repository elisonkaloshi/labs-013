#!/usr/bin/env python3
import os

from flask import Flask, abort, render_template, request

app = Flask(__name__)

CURRENT_USER_ID = "1001"

USERS = {
    "1001": {
        "name": "Alice Morgan",
        "role": "Standard User",
        "email": "alice@example.local",
        "note": "This is your normal profile.",
    },
    "1002": {
        "name": "Bob Admin",
        "role": "Administrator",
        "email": "admin@example.local",
        "note": "Secret: LAB-013-HPP",
    },
}


@app.route("/")
def index():
    return render_template("index.html", current_user_id=CURRENT_USER_ID)


@app.route("/profile")
def profile():
    user_ids = request.args.getlist("user_id")
    if not user_ids:
        abort(400, "Missing user_id parameter.")

    validated_user_id = user_ids[0]
    if validated_user_id != CURRENT_USER_ID:
        abort(403, "You can only view your own profile.")

    selected_user_id = user_ids[-1]
    profile_data = USERS.get(selected_user_id)
    if profile_data is None:
        abort(404, "Profile not found.")

    return render_template(
        "profile.html",
        user_id=selected_user_id,
        profile=profile_data,
        repeated=len(user_ids) > 1,
    )


if __name__ == "__main__":
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "5013"))
    print(f"Open http://{host}:{port}")
    app.run(host=host, port=port, debug=False)
