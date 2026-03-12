import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import FileWriterTool

# 1. Chargement des secrets
load_dotenv()

# 2. Config du cerveau (Le survivant des quotas)
mon_llm = LLM(
    model="gemini/gemini-flash-latest", 
    api_key=os.getenv("GOOGLE_API_KEY")
)

# 3. Les outils (Le bras armé)
file_writer = FileWriterTool()

# 4. LES AGENTS
po = Agent(
    role="Product Owner",
    goal="Transformer l'idée de projet en backlog structuré.",
    backstory="Expert en gestion de produit IT, pragmatique.",
    llm=mon_llm,
    verbose=True
)

tech = Agent(
    role="Tech Lead",
    goal="Concevoir l'architecture technique et la structure des fichiers.",
    backstory="Architecte logiciel senior. Tu définis la structure du projet.",
    llm=mon_llm,
    verbose=True
)

dev = Agent(
    role="Developer",
    goal="Écrire le code source complet et créer les fichiers sur le disque.",
    backstory="Codeur Python efficace. Tu utilises tes outils pour créer les fichiers.",
    llm=mon_llm,
    tools=[file_writer],
    verbose=True
)

# 5. LES TÂCHES
t1 = Task(
    description="Analyse l'idée : {idee_projet}. Produis 3 User Stories.",
    expected_output="Un backlog Markdown détaillé.",
    agent=po,
    human_input=True
)

t2 = Task(
    description="À partir du backlog, définis l'arborescence des fichiers nécessaires.",
    expected_output="Un plan d'architecture technique.",
    agent=tech,
    context=[t1]
)

t3 = Task(
    description="Crée les fichiers et écris le code source en te basant sur l'architecture.",
    expected_output="Les fichiers sont créés sur le disque.",
    agent=dev,
    context=[t2]
)

# 6. L'ÉQUIPAGE
equipe = Crew(
    agents=[po, tech, dev],
    tasks=[t1, t2, t3],
    process=Process.sequential
)

print("### Lancement de l'usine (Fix FileWriterTool) ###")
equipe.kickoff(inputs={'idee_projet': 'Une app pour tracker mes boucheries en Loire-Atlantique'})
