# Portfólio Profissional — Python + Flask

Portfólio de desenvolvedor com visual escuro, efeito Matrix e arquitetura MVC.
Inclui também um efeito Matrix standalone executável direto no terminal em Python puro.

---

## Estrutura do Projeto

```
portfolio/
│
├── run.py                              ← Entry point da aplicação Flask
├── matrix_rain.py                      ← Efeito Matrix no terminal (Python puro)
├── requirements.txt                    ← Dependências
│
├── config/
│   ├── __init__.py
│   └── settings.py                     ← Configurações por ambiente (dev/prod)
│
└── app/
    ├── __init__.py                     ← Factory da aplicação (create_app)
    │
    ├── models/                         ── M (Model)
    │   ├── __init__.py
    │   ├── developer.py                ← Dados do desenvolvedor e skills
    │   └── project.py                  ← Modelo Project + ProjectRepository
    │
    ├── controllers/                    ── C (Controller / Blueprints)
    │   ├── __init__.py
    │   ├── home_controller.py          ← Rotas: GET /  e  GET /sobre
    │   ├── projects_controller.py      ← Rotas: GET /projetos  e  GET /projetos/<id>
    │   └── contact_controller.py       ← Rotas: GET /contato  e  POST /contato/enviar
    │
    └── views/                          ── V (View)
        ├── templates/
        │   ├── shared/
        │   │   └── base.html           ← Template base com Matrix, CSS e nav
        │   ├── home/
        │   │   ├── index.html          ← Página inicial (hero)
        │   │   └── sobre.html          ← Sobre mim + skills
        │   ├── projects/
        │   │   ├── index.html          ← Lista de projetos
        │   │   └── detail.html         ← Detalhe de um projeto
        │   └── contact/
        │       └── index.html          ← Formulário de contato
        └── static/
            ├── css/
            │   └── style.css           ← Estilos globais
            └── js/
                ├── matrix.js           ← Chuva Matrix no canvas do browser
                └── main.js             ← Animações de scroll e skill bars
```

---

## Rotas

| Método | Rota                  | Controller            | Descrição                        |
|--------|-----------------------|-----------------------|----------------------------------|
| GET    | `/`                   | home_controller       | Página inicial — hero            |
| GET    | `/sobre`              | home_controller       | Sobre mim + stack técnica        |
| GET    | `/projetos`           | projects_controller   | Lista todos os projetos          |
| GET    | `/projetos/<id>`      | projects_controller   | Detalhe de um projeto pelo índice|
| GET    | `/contato`            | contact_controller    | Página de contato com formulário |
| POST   | `/contato/enviar`     | contact_controller    | Processa envio do formulário     |

---

## Como rodar o portfólio web

```bash
# 1. Instale as dependências
pip install -r requirements.txt

# 2. Suba o servidor
python run.py

# 3. Acesse no navegador
http://localhost:5000
```

---

## Como rodar o Matrix no terminal

Não precisa de nenhuma dependência extra — usa apenas `curses`, que já vem no Python.

```bash
python matrix_rain.py
```

- Pressione **q** ou **ESC** para sair
- Funciona em qualquer terminal com suporte a cores (Linux, macOS, WSL no Windows)

---

## Como personalizar

Edite os arquivos de model — sem precisar tocar em HTML ou CSS:

**Seus dados pessoais** → `app/models/developer.py`
```python
self.name     = "Seu Nome"
self.title    = "Sua Especialidade"
self.email    = "voce@email.com"
self.github   = "https://github.com/seuperfil"
#self.linkedin = "https://linkedin.com/in/seuperfil"
```

**Seus projetos** → `app/models/project.py`, método `ProjectRepository.get_all()`
```python
Project(
    title="Nome do Projeto",
    description="O que foi feito.",
    tags=["Python", "Flask"],
    result="Resultado gerado para o cliente",
    link="https://link-do-projeto.com",
),
```

---

## Ambiente de produção

Altere o ambiente no `run.py`:

```python
app = create_app("production")
```

Ou via variável de ambiente com Gunicorn:

```bash
pip install gunicorn
gunicorn "app:create_app('production')" -w 4 -b 0.0.0.0:8000
```
