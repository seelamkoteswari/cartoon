from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from app.extensions import db
from app.models.image import Image
from app.models.filters import cartoon, pencil, detail, edge
import os, cv2

main = Blueprint("main", __name__)

UPLOAD = "app/static/uploads/"
OUTPUT = "app/static/outputs/"

@main.route("/")
def home():
    return redirect("/login")


@main.route("/dashboard", methods=["GET","POST"])
@login_required
def dashboard():

    if request.method == "POST":
        file = request.files["image"]
        filter_type = request.form.get("filter")

        if file:
            path = os.path.join(UPLOAD, file.filename)
            file.save(path)

            img = cv2.imread(path)

            if filter_type == "cartoon":
                output = cartoon(img)
            elif filter_type == "pencil":
                output = pencil(img)
            elif filter_type == "detail":
                output = detail(img)
            elif filter_type == "edge":
                output = edge(img)
            else:
                output = img

            name = f"{filter_type}_{file.filename}"
            cv2.imwrite(os.path.join(OUTPUT, name), output)

            db.session.add(Image(filename=name, filter_used=filter_type, user_id=current_user.id))
            db.session.commit()

    images = Image.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", images=images)