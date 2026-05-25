from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models import Developer

contact_bp = Blueprint("contact", __name__, url_prefix="/contato")


@contact_bp.route("/")
def index():
    """Página de contato."""
    dev = Developer()
    return render_template("contact/index.html", dev=dev)


@contact_bp.route("/enviar", methods=["POST"])
def send():
    """Recebe o formulário de contato."""
    name    = request.form.get("name", "").strip()
    email   = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Preencha todos os campos.", "error")
        return redirect(url_for("contact.index"))

    # Aqui você pode integrar SMTP, SendGrid, etc.
    # Por ora apenas confirma o recebimento.
    flash(f"Mensagem recebida, {name}! Entrarei em contato em breve.", "success")
    return redirect(url_for("contact.index"))
