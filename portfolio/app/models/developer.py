class Developer:
    """Modelo com os dados pessoais e profissionais do desenvolvedor."""

    def __init__(self):
        self.name = "Rony Ribeiro"
        self.title = "Desenvolvedor Full Stack"
        self.tagline = "Construindo sistemas robustos. Entregando resultados reais."
        self.about = (
            "Transformando requisitos complexos em soluções escaláveis. "
            "Arquitetura de back-end, APIs e automações "
            "que economizam tempo e dinheiro para meus clientes."
        )
        self.email = "ronyribeeiro8@gmail.com"
        self.github = "https://github.com/ronyribeeiro8-ship-it"
        self.linkedin = "https://www.linkedin.com/in/rony-ribeiro-47b3a4201"
        self.skills = [
            {"name": "Python / Flask ", "level": 85},
            {"name": "JavaScript ",    "level": 58},
            {"name": "PostgreSQL / Redis", "level": 74},
            {"name": "Docker", "level": 80},
        ]

    def to_dict(self):
        return self.__dict__
