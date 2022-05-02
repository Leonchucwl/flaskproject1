from flask import (Blueprint,
                   render_template,
                   request,
                   redirect,
                   url_for,
                   jsonify,
                   session,
                   flash)
from exts import mail, db
from flask_mail import Message
import string
import random
from models import EmailCaptchModel
from datetime import datetime
from .form import RegisterForm, LoginForm
from models import UserModel
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                session["user_id"] = user.id
                return redirect("/")
            else:
                flash("邮箱和密码不匹配!")
                # flash("邮箱和密码不匹配!")
                return redirect(url_for("user.login"))
        else:
            flash("邮箱和密码格式错误!")
            return redirect(url_for("user.login"))


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            hash_password = generate_password_hash(password)
            user = UserModel(email=email, username=username, password=hash_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user.login"))
        else:
            return redirect(url_for("user.register"))


@bp.route("logout")
def logout():
    session.clear()
    return redirect(url_for("user.login"))


@bp.route("/captcha", methods=['POST'])
def get_captcha():
    email = request.form.get("email")
    letters = string.ascii_letters+string.digits
    captcha = "".join(random.sample(letters, 4))
    if email:
        message = Message(
            subject="mail test",
            recipients=["1035743997@qq.com"],
            body=f"this is a test mail, captcha: {captcha}. Don't tell anyone!",
        )
        mail.send(message)
        captcha_email = EmailCaptchModel.query.filter_by(email=email).first()
        if captcha_email:
            captcha_email.captcha = captcha
            captcha_email.create_time = datetime.now()
            db.session.commit()
        else:
            captcha_email = EmailCaptchModel(email=email, captcha=captcha)
            db.session.add(captcha_email)
            db.session.commit()
        return jsonify({"code": 200})
    else:
        return jsonify({"code": 400, "message": "请先传递邮箱!"})
