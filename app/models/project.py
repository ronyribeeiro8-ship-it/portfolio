class Project:
    """Modelo que representa um projeto do portfólio."""

    def __init__(self, title, description, tags, result, link="#"):
        self.title = title
        self.description = description
        self.tags = tags
        self.result = result
        self.link = link

    def to_dict(self):
        return self.__dict__


class ProjectRepository:
    """Repositório com todos os projetos cadastrados."""

    @staticmethod
    def get_all():
        return [
            Project(
                title="App Agendou",
                description="Aplicativo web para agendamento de serviços, facilitando a gestão de horários e reservas para usuários e prestadores.",
                tags=["Web App", "Agendamento", "Lovable"],
                result="Simplifica o processo de agendamento online",
                link="https://app-agendou.lovable.app/",
            ),
            Project(
                title="ChatForge",
                description="Plataforma de criação e gerenciamento de chats personalizados, hospedada no Render para alta disponibilidade.",
                tags=["Chat", "Web App", "Render"],
                result="Ferramenta inovadora para construção de interfaces de chat",
                link="https://chatforge-owj9.onrender.com/",
            ),
        ]

    @staticmethod
    def get_by_index(index):
        projects = ProjectRepository.get_all()
        if 0 <= index < len(projects):
            return projects[index]
        return None
