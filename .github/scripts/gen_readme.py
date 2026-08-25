#!/usr/bin/env python3
"""Generate the four localized READMEs from one source of truth."""

from pathlib import Path

OUT = Path(__file__).resolve().parents[2]

SW = "https://img.shields.io/badge"


def b(label: str, color: str, logo: str = "", logo_color: str = "white") -> str:
    label_esc = label.replace(" ", "%20").replace("-", "--")
    url = f"{SW}/{label_esc}-{color}?style=flat-square"
    if logo:
        url += f"&logo={logo}&logoColor={logo_color}"
    return f"![{label}]({url})"


# --------------------------------------------------------------------------
# Stack — taken from the CV, grouped the way a recruiter reads it
# --------------------------------------------------------------------------
STACK = [
    (
        "languages",
        [
            b("Python", "3776AB", "python"),
            b("SQL", "4479A1", "postgresql"),
            b("C", "A8B9CC", "c", "black"),
            b("C++", "00599C", "cplusplus"),
            b("TypeScript", "3178C6", "typescript"),
            b("Java", "ED8B00", "openjdk"),
            b("Julia", "9558B2", "julia"),
            b("Haskell", "5D4F85", "haskell"),
            b("MATLAB", "0076A8"),
            b("Bash", "4EAA25", "gnubash"),
            b("LaTeX", "008080", "latex"),
        ],
    ),
    (
        "data",
        [
            b("Apache Spark", "E25A1C", "apachespark"),
            b("PySpark", "E25A1C", "apachespark"),
            b("Airflow", "017CEE", "apacheairflow"),
            b("dbt", "FF694B", "dbt"),
            b("Kafka", "231F20", "apachekafka"),
            b("Polars", "CD792C", "polars"),
            b("DuckDB", "FFF000", "duckdb", "black"),
            b("pandas", "150458", "pandas"),
            b("NumPy", "013243", "numpy"),
            b("PostgreSQL", "4169E1", "postgresql"),
            b("MySQL", "4479A1", "mysql"),
        ],
    ),
    (
        "ml",
        [
            b("scikit-learn", "F7931E", "scikitlearn"),
            b("TensorFlow", "FF6F00", "tensorflow"),
            b("Keras", "D00000", "keras"),
            b("LightGBM", "9ACD32"),
            b("XGBoost", "337AB7"),
            b("MLflow", "0194E2", "mlflow"),
        ],
    ),
    (
        "cloud",
        [
            b("AWS", "232F3E", "amazonwebservices"),
            b("Docker", "2496ED", "docker"),
            b("Linux", "FCC624", "linux", "black"),
            b("Git", "F05032", "git"),
            b("GitHub Actions", "2088FF", "githubactions"),
            b("uv", "DE5FE9", "uv"),
            b("Jira", "0052CC", "jira"),
            b("VS Code", "007ACC", "visualstudiocode"),
        ],
    ),
    (
        "viz",
        [
            b("Superset", "20A6C9", "apachesuperset"),
            b("Plotly", "3F4F75", "plotly"),
            b("Matplotlib", "11557C"),
            b("seaborn", "4C72B0"),
            b("Jupyter", "F37626", "jupyter"),
        ],
    ),
]

# --------------------------------------------------------------------------
# Projects. link=None means "no public repo yet" — no fabricated URLs.
# --------------------------------------------------------------------------
PROJECTS = [
    {
        "key": "phishing",
        "name": "Phishing Email Detection",
        "link": None,
        "year": "2026",
        "stack": "Python · LightGBM · Naive Bayes · LSTM",
    },
    {
        "key": "uvkit",
        "name": "uvkit",
        "link": "https://github.com/DmytroPalahin/uvkit",
        "year": "2026",
        "stack": "Python · uv · Ruff · pytest",
    },
    {
        "key": "logistics",
        "name": "Logistics Center Placement",
        "link": None,
        "year": "2025",
        "stack": "Python · Julia · CPLEX",
    },
    {
        "key": "reaction",
        "name": "Reaction System",
        "link": None,
        "year": "2024",
        "stack": "Haskell",
    },
    {
        "key": "tsp",
        "name": "Traveling Salesman Problem",
        "link": "https://github.com/DmytroPalahin/Probleme_du_Voyageur_de_Commerce",
        "year": "2023",
        "stack": "C · Reinforcement Learning",
    },
    {
        "key": "langrec",
        "name": "Language Recognizer",
        "link": "https://github.com/DmytroPalahin/Reconnaisseur_de_Langue",
        "year": "—",
        "stack": "C",
    },
    {
        "key": "anomaly",
        "name": "Anomaly Detection",
        "link": "https://github.com/DmytroPalahin/Anomaly_Detection",
        "year": "2021",
        "stack": "Python · scikit-learn",
    },
    {
        "key": "paper",
        "name": "Research publication",
        "link": None,
        "year": "2021",
        "stack": "Mathematical algorithms",
    },
]

# --------------------------------------------------------------------------
# Localized copy
# --------------------------------------------------------------------------
L = {
    "en": {
        "file": "README.md",
        "switch": [
            ("Langue-Français-white", "README.fr.md"),
            ("Язык-Русский-red", "README.ru.md"),
            ("Мова-Українська-yellow", "README.ua.md"),
        ],
        "title": "Dima — Dmytro Palahin",
        "tagline": "Data Engineer / MLOps apprentice · Paris, France",
        "intro": (
            "Final-year engineering student at [Sup Galilée](https://www.sup-galilee.univ-paris13.fr/)\n"
            "(Computer Science, class of 2026), with 3 years of work-study experience in **data engineering,\n"
            "machine learning and MLOps** at **Société Générale Assurances**."
        ),
        "bullets": [
            "🛠️ I build **data pipelines, internal developer tooling and ML systems**",
            "📐 Strong background in **applied mathematics, probability, statistics and optimization**",
            "📈 Interested in **quantitative research, systematic trading and market data analysis**",
            "🌍 I work in **English**, **French**, **Ukrainian** and **Russian**",
        ],
        "h_exp": "Experience",
        "exp_title": "**Data Engineer / MLOps (work-study)** — Société Générale Assurances · La Défense · 09/2023 → present",
        "exp": [
            "Designed an **automated SAS → Python migration system** built on GitHub Copilot — prompt engineering, reusable Skills and persistent context (`copilot-instructions.md`), validated by a two-tier test suite *(Python · Polars · DuckDB · AWS S3)*",
            "Designed and automated a **migration pipeline moving 500+ GB of SAS datasets to AWS S3**, making them available to the data teams *(Python · fsspec · smbfs · Bash)*",
            "Built and shipped **3 VS Code extensions** for the internal data platform used by **30+ data scientists and analysts**; maintain **35+ extensions** and `code-server` for **40+ users** *(TypeScript · Python · Linux)*",
            "Built a **monitoring dashboard tracking 10+ operational KPIs** for the Zaion callbot, and analysed **1 year of production data** to identify the main error causes → 3 improvement recommendations *(Apache Superset · PostgreSQL · pandas)*",
        ],
        "h_stack": "Stack",
        "stack_labels": {
            "languages": "Languages",
            "data": "Data engineering",
            "ml": "Machine learning",
            "cloud": "Cloud, DevOps & tooling",
            "viz": "Analysis & visualization",
        },
        "h_proj": "Selected work",
        "proj_head": ["Project", "What it is", "Stack", "Year"],
        "proj": {
            "phishing": "Phishing email classifier trained on **76,677 emails** from 5 real-world datasets — full NLP pipeline (TF-IDF, URL extraction) with a LightGBM + Naive Bayes + LSTM ensemble",
            "uvkit": "CLI that scaffolds Python projects from a `uv` + Ruff + pytest template",
            "logistics": "Facility location problem modelled as a MILP and solved with CPLEX plus heuristic methods",
            "reaction": "Representation of reaction systems and processes in functional programming",
            "tsp": "Ant colony optimization applied to the travelling salesman problem",
            "langrec": "Perceptron neural network for language identification, written from scratch",
            "anomaly": "Anomaly detection using partial data labeling methods",
            "paper": "Impulse noise filtering method for video images — *Informatics and Mathematical Methods in Simulation*, Vol. 11 (2021), No. 4",
        },
        "proj_note": "<sub>Some of these are coursework or work projects without a public repository — the ones that do have code are linked.</sub>",
        "h_metrics": "GitHub metrics",
        "metrics_alt": "GitHub metrics",
        "h_contact": "Contact",
        "footer": "<sub>This profile is built and checked in CI — see [`.github/workflows`](.github/workflows) and [SETUP.md](SETUP.md).</sub>",
    },
    "fr": {
        "file": "README.fr.md",
        "switch": [
            ("Language-English-blue", "README.md"),
            ("Язык-Русский-red", "README.ru.md"),
            ("Мова-Українська-yellow", "README.ua.md"),
        ],
        "title": "Dimitri — Dmytro Palahin",
        "tagline": "Apprenti Data Engineer / MLOps · Paris, France",
        "intro": (
            "Élève ingénieur en dernière année à [Sup Galilée](https://www.sup-galilee.univ-paris13.fr/)\n"
            "(Informatique, promotion 2026), avec 3 ans d'alternance en **data engineering,\n"
            "machine learning et MLOps** chez **Société Générale Assurances**."
        ),
        "bullets": [
            "🛠️ Je construis des **pipelines de données, de l'outillage développeur interne et des systèmes ML**",
            "📐 Solides bases en **mathématiques appliquées, probabilités, statistiques et optimisation**",
            "📈 Intéressé par la **recherche quantitative, le trading systématique et l'analyse de données de marché**",
            "🌍 Je travaille en **français**, **anglais**, **ukrainien** et **russe**",
        ],
        "h_exp": "Expérience",
        "exp_title": "**Data Engineer / MLOps (alternance)** — Société Générale Assurances · La Défense · 09/2023 → aujourd'hui",
        "exp": [
            "Conception d'un **système de migration automatisée SAS → Python** basé sur GitHub Copilot — prompt engineering, Skills réutilisables et contexte persistant (`copilot-instructions.md`), validé par une suite de tests à 2 niveaux *(Python · Polars · DuckDB · AWS S3)*",
            "Conception et automatisation d'un **pipeline de migration de 500+ Go de datasets SAS vers AWS S3**, mis à disposition des équipes Data *(Python · fsspec · smbfs · Bash)*",
            "Développement et déploiement de **3 extensions VS Code** pour la plateforme Data interne utilisée par **30+ Data Scientists et Analysts** ; maintenance de **35+ extensions** et de `code-server` pour **40+ utilisateurs** *(TypeScript · Python · Linux)*",
            "Mise en place d'un **dashboard de monitoring suivant 10+ KPI opérationnels** pour le callbot Zaion, et analyse d'**1 an de données de production** pour identifier les causes d'erreurs → 3 recommandations d'amélioration *(Apache Superset · PostgreSQL · pandas)*",
        ],
        "h_stack": "Stack",
        "stack_labels": {
            "languages": "Langages",
            "data": "Data engineering",
            "ml": "Machine learning",
            "cloud": "Cloud, DevOps & outillage",
            "viz": "Analyse & visualisation",
        },
        "h_proj": "Projets sélectionnés",
        "proj_head": ["Projet", "Description", "Stack", "Année"],
        "proj": {
            "phishing": "Classifieur d'e-mails de phishing entraîné sur **76 677 e-mails** issus de 5 jeux de données réels — pipeline NLP complet (TF-IDF, extraction d'URL) et ensemble LightGBM + Naive Bayes + LSTM",
            "uvkit": "CLI qui génère des projets Python à partir d'un template `uv` + Ruff + pytest",
            "logistics": "Problème de localisation d'entrepôts modélisé en MILP et résolu avec CPLEX et des heuristiques",
            "reaction": "Représentation de systèmes et de processus de réaction en programmation fonctionnelle",
            "tsp": "Optimisation par colonies de fourmis appliquée au problème du voyageur de commerce",
            "langrec": "Réseau de neurones Perceptron pour l'identification de langue, écrit de zéro",
            "anomaly": "Détection d'anomalies par méthodes d'étiquetage partiel des données",
            "paper": "Méthode de filtrage du bruit impulsionnel dans les images vidéo — *Informatics and Mathematical Methods in Simulation*, Vol. 11 (2021), No. 4",
        },
        "proj_note": "<sub>Certains sont des projets académiques ou professionnels sans dépôt public — ceux qui ont du code sont liés.</sub>",
        "h_metrics": "Statistiques GitHub",
        "metrics_alt": "Statistiques GitHub",
        "h_contact": "Contact",
        "footer": "<sub>Ce profil est généré et vérifié en CI — voir [`.github/workflows`](.github/workflows) et [SETUP.md](SETUP.md).</sub>",
    },
    "ru": {
        "file": "README.ru.md",
        "switch": [
            ("Language-English-blue", "README.md"),
            ("Langue-Français-white", "README.fr.md"),
            ("Мова-Українська-yellow", "README.ua.md"),
        ],
        "title": "Дима — Dmytro Palahin",
        "tagline": "Data Engineer / MLOps, альтернанс · Париж, Франция",
        "intro": (
            "Студент выпускного курса инженерной школы [Sup Galilée](https://www.sup-galilee.univ-paris13.fr/)\n"
            "(информатика, выпуск 2026), 3 года по альтернансу в **data engineering,\n"
            "machine learning и MLOps** в **Société Générale Assurances**."
        ),
        "bullets": [
            "🛠️ Строю **дата-пайплайны, внутренние инструменты для разработчиков и ML-системы**",
            "📐 Сильная база в **прикладной математике, теории вероятностей, статистике и оптимизации**",
            "📈 Интересуюсь **количественными исследованиями, системным трейдингом и анализом рыночных данных**",
            "🌍 Работаю на **русском**, **французском**, **английском** и **украинском**",
        ],
        "h_exp": "Опыт работы",
        "exp_title": "**Data Engineer / MLOps (альтернанс)** — Société Générale Assurances · La Défense · 09/2023 → настоящее время",
        "exp": [
            "Спроектировал **систему автоматической миграции SAS → Python** на базе GitHub Copilot — prompt engineering, переиспользуемые Skills и постоянный контекст (`copilot-instructions.md`), с двухуровневым набором тестов *(Python · Polars · DuckDB · AWS S3)*",
            "Спроектировал и автоматизировал **пайплайн переноса 500+ ГБ SAS-датасетов в AWS S3** и открыл к ним доступ дата-командам *(Python · fsspec · smbfs · Bash)*",
            "Разработал и выкатил **3 расширения для VS Code** для внутренней Data-платформы, которыми пользуются **30+ дата-сайентистов и аналитиков**; поддерживаю **35+ расширений** и `code-server` для **40+ пользователей** *(TypeScript · Python · Linux)*",
            "Собрал **дашборд мониторинга с 10+ операционными KPI** для колл-бота Zaion и проанализировал **год продакшн-данных**, выявив основные причины ошибок → 3 рекомендации по улучшению *(Apache Superset · PostgreSQL · pandas)*",
        ],
        "h_stack": "Стек",
        "stack_labels": {
            "languages": "Языки",
            "data": "Data engineering",
            "ml": "Machine learning",
            "cloud": "Облако, DevOps и инструменты",
            "viz": "Анализ и визуализация",
        },
        "h_proj": "Избранные проекты",
        "proj_head": ["Проект", "Что это", "Стек", "Год"],
        "proj": {
            "phishing": "Классификатор фишинговых писем, обученный на **76 677 письмах** из 5 реальных датасетов — полный NLP-пайплайн (TF-IDF, извлечение URL) и ансамбль LightGBM + Naive Bayes + LSTM",
            "uvkit": "CLI, создающий Python-проекты из шаблона `uv` + Ruff + pytest",
            "logistics": "Задача размещения логистических центров: модель MILP, решение через CPLEX и эвристики",
            "reaction": "Представление реакционных систем и процессов средствами функционального программирования",
            "tsp": "Муравьиный алгоритм для задачи коммивояжёра",
            "langrec": "Перцептрон для определения языка, написанный с нуля",
            "anomaly": "Поиск аномалий методами частичной разметки данных",
            "paper": "Метод фильтрации импульсного шума на видеоизображениях — *Informatics and Mathematical Methods in Simulation*, Vol. 11 (2021), No. 4",
        },
        "proj_note": "<sub>Часть работ — учебные или рабочие проекты без публичного репозитория; ссылки стоят там, где код открыт.</sub>",
        "h_metrics": "Статистика GitHub",
        "metrics_alt": "Статистика GitHub",
        "h_contact": "Контакты",
        "footer": "<sub>Профиль собирается и проверяется в CI — см. [`.github/workflows`](.github/workflows) и [SETUP.md](SETUP.md).</sub>",
    },
    "ua": {
        "file": "README.ua.md",
        "switch": [
            ("Language-English-blue", "README.md"),
            ("Langue-Français-white", "README.fr.md"),
            ("Язык-Русский-red", "README.ru.md"),
        ],
        "title": "Діма — Dmytro Palahin",
        "tagline": "Data Engineer / MLOps, апprentice · Париж, Франція",
        "intro": (
            "Студент випускного курсу інженерної школи [Sup Galilée](https://www.sup-galilee.univ-paris13.fr/)\n"
            "(інформатика, випуск 2026), 3 роки навчання за контрактом у **data engineering,\n"
            "machine learning та MLOps** у **Société Générale Assurances**."
        ),
        "bullets": [
            "🛠️ Будую **дата-пайплайни, внутрішні інструменти для розробників і ML-системи**",
            "📐 Сильна база в **прикладній математиці, теорії ймовірностей, статистиці та оптимізації**",
            "📈 Цікавлюся **кількісними дослідженнями, системним трейдингом і аналізом ринкових даних**",
            "🌍 Працюю **українською**, **французькою**, **англійською** та **російською**",
        ],
        "h_exp": "Досвід роботи",
        "exp_title": "**Data Engineer / MLOps (навчання за контрактом)** — Société Générale Assurances · La Défense · 09/2023 → дотепер",
        "exp": [
            "Спроєктував **систему автоматичної міграції SAS → Python** на базі GitHub Copilot — prompt engineering, багаторазові Skills і постійний контекст (`copilot-instructions.md`), з дворівневим набором тестів *(Python · Polars · DuckDB · AWS S3)*",
            "Спроєктував і автоматизував **пайплайн перенесення 500+ ГБ SAS-датасетів до AWS S3** та відкрив до них доступ дата-командам *(Python · fsspec · smbfs · Bash)*",
            "Розробив і випустив **3 розширення для VS Code** для внутрішньої Data-платформи, якими користуються **30+ дата-сайєнтистів і аналітиків**; підтримую **35+ розширень** і `code-server` для **40+ користувачів** *(TypeScript · Python · Linux)*",
            "Зібрав **дашборд моніторингу з 10+ операційними KPI** для колбота Zaion і проаналізував **рік продакшн-даних**, визначивши основні причини помилок → 3 рекомендації щодо покращення *(Apache Superset · PostgreSQL · pandas)*",
        ],
        "h_stack": "Стек",
        "stack_labels": {
            "languages": "Мови",
            "data": "Data engineering",
            "ml": "Machine learning",
            "cloud": "Хмара, DevOps та інструменти",
            "viz": "Аналіз і візуалізація",
        },
        "h_proj": "Обрані проєкти",
        "proj_head": ["Проєкт", "Що це", "Стек", "Рік"],
        "proj": {
            "phishing": "Класифікатор фішингових листів, навчений на **76 677 листах** із 5 реальних датасетів — повний NLP-пайплайн (TF-IDF, вилучення URL) та ансамбль LightGBM + Naive Bayes + LSTM",
            "uvkit": "CLI, що створює Python-проєкти з шаблону `uv` + Ruff + pytest",
            "logistics": "Задача розміщення логістичних центрів: модель MILP, розв'язання через CPLEX та евристики",
            "reaction": "Подання реакційних систем і процесів засобами функційного програмування",
            "tsp": "Мурашиний алгоритм для задачі комівояжера",
            "langrec": "Перцептрон для розпізнавання мови, написаний з нуля",
            "anomaly": "Пошук аномалій методами часткового розмічування даних",
            "paper": "Метод фільтрації імпульсного шуму на відеозображеннях — *Informatics and Mathematical Methods in Simulation*, Vol. 11 (2021), No. 4",
        },
        "proj_note": "<sub>Частина робіт — навчальні або робочі проєкти без публічного репозиторію; посилання стоять там, де код відкритий.</sub>",
        "h_metrics": "Статистика GitHub",
        "metrics_alt": "Статистика GitHub",
        "h_contact": "Контакти",
        "footer": "<sub>Профіль збирається та перевіряється в CI — див. [`.github/workflows`](.github/workflows) і [SETUP.md](SETUP.md).</sub>",
    },
}

L["ua"]["tagline"] = "Data Engineer / MLOps, навчання за контрактом · Париж, Франція"

CONTACT = (
    "[![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)]"
    "(mailto:dmytro.palahin@gmail.com)\n"
    "[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)]"
    "(https://www.linkedin.com/in/dmytro-palahin/)\n"
    "[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=flat-square&logo=telegram&logoColor=white)]"
    "(https://t.me/dmitry_plhn)"
)


def render(lang: str) -> str:
    t = L[lang]
    p: list[str] = []

    p.append('<div align="center">\n')
    for badge, target in t["switch"]:
        alt = badge.split("-")[1]
        p.append(
            f"[![{alt}](https://img.shields.io/badge/{badge}?style=flat-square)]({target})"
        )
    p.append("\n</div>\n")

    p.append(f"# {t['title']}\n")
    p.append(f"**{t['tagline']}**\n")
    p.append(t["intro"] + "\n")
    p.extend(f"- {x}" for x in t["bullets"])
    p.append("\n---\n")

    p.append(f"## {t['h_exp']}\n")
    p.append(t["exp_title"] + "\n")
    p.extend(f"- {x}" for x in t["exp"])
    p.append("\n---\n")

    p.append(f"## {t['h_stack']}\n")
    for key, badges in STACK:
        p.append(f"**{t['stack_labels'][key]}**\n")
        p.append("\n".join(badges))
        p.append("")
    p.append("---\n")

    p.append(f"## {t['h_proj']}\n")
    head = t["proj_head"]
    p.append(f"| {head[0]} | {head[1]} | {head[2]} | {head[3]} |")
    p.append("| --- | --- | --- | --- |")
    for proj in PROJECTS:
        name = f"[{proj['name']}]({proj['link']})" if proj["link"] else proj["name"]
        p.append(
            f"| {name} | {t['proj'][proj['key']]} | {proj['stack']} | {proj['year']} |"
        )
    p.append("")
    p.append(t["proj_note"])
    p.append("\n---\n")

    p.append(f"## {t['h_metrics']}\n")
    p.append(
        "<picture>\n"
        '  <source media="(prefers-color-scheme: dark)" srcset="assets/metrics.dark.svg">\n'
        '  <source media="(prefers-color-scheme: light)" srcset="assets/metrics.light.svg">\n'
        f'  <img alt="{t["metrics_alt"]}" src="assets/metrics.light.svg" width="100%">\n'
        "</picture>\n"
    )
    p.append("---\n")

    p.append(f"## {t['h_contact']}\n")
    p.append(CONTACT + "\n")
    p.append(t["footer"])

    return "\n".join(p).rstrip() + "\n"


for lang, meta in L.items():
    (OUT / meta["file"]).write_text(render(lang), encoding="utf-8")
    print("wrote", meta["file"])
