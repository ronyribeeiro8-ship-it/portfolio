class Developer:
    """Modelo com os dados pessoais e profissionais do desenvolvedor."""

    def __init__(self):
        self.name = "Rony Ribeiro"
        self.title = "Desenvolvedor Full Stack"
        self.tagline = "Construindo sistemas robustos. Entregando resultados reais."
        self.email = "ronyribeeiro8@gmail.com"
        self.linkedin = "https://www.linkedin.com/in/rony-ribeiro-47b3a4201"
        self.github = "https://github.com/ronyribeeiro8-ship-it"
        self.whatsapp = "https://wa.me/55994094719"
        self.skills = [
            {"name": "Python / Flask / Django / FastAPI", "level": 85},
            {"name": "JavaScript ",    "level": 40},
            {"name": "PostgreSQL / Redis",       "level": 65},
            {"name": "Docker / Render",             "level": 80},
            {"name": "TypeScript",           "level": 35},
        ]

    def to_dict(self):
        return self.__dict__
