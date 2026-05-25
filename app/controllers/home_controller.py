from flask import Blueprint, render_template
from app.models import Developer

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def index():
    """Página inicial — apresenta o desenvolvedor."""
    dev = Developer()
    return render_template("home/index.html", dev=dev)


@home_bp.route("/sobre")
def sobre():
    """Página de detalhes sobre o desenvolvedor e suas skills."""
    dev = Developer()
    return render_template("home/sobre.html", dev=dev)
