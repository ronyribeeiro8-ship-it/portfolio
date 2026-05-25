from flask import Blueprint, render_template, abort
from app.models import ProjectRepository

projects_bp = Blueprint("projects", __name__, url_prefix="/projetos")


@projects_bp.route("/")
def index():
    """Lista todos os projetos do portfólio."""
    projects = ProjectRepository.get_all()
    return render_template("projects/index.html", projects=projects)


@projects_bp.route("/<int:project_id>")
def detail(project_id):
    """Detalhe de um projeto específico pelo índice."""
    project = ProjectRepository.get_by_index(project_id)
    if project is None:
        abort(404)
    return render_template("projects/detail.html", project=project, project_id=project_id)
