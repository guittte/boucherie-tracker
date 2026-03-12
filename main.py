import os
import subprocess
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool
from crewai_tools import FileWriterTool

load_dotenv()

@tool("terminal_tool")
def terminal_tool(command: str) -> str:
    """Exécute une commande shell. Attention: ne pas lister des milliers de fichiers."""
    try:
        # On limite la sortie pour ne pas saturer le contexte de l'IA
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        output = result.stdout[:5000] # On ne prend que les 5000 premiers caractères
        return f"Sortie (tronquée si trop longue): {output}\nErreur: {result.stderr}"
    except Exception as e:
        return str(e)

mon_llm = LLM(model="gemini/gemini-2.5-flash", api_key=os.getenv("GOOGLE_API_KEY"))
file_tool = FileWriterTool()

po = Agent(role="PO", goal="Backlog", backstory="Expert produit", llm=mon_llm)
tech = Agent(role="Architecte", goal="Structure", backstory="Expert IT", llm=mon_llm)
dev = Agent(role="Dev", goal="Code", backstory="Senior Python", llm=mon_llm, tools=[file_tool], verbose=True)
devops = Agent(role="DevOps", goal="Deploy", backstory="Expert Git", llm=mon_llm, tools=[file_tool, terminal_tool], verbose=True)

t1 = Task(description="Backlog pour l'app de boucheries du 44.", expected_output="Backlog MD.", agent=po)
t2 = Task(description="Arborescence technique.", expected_output="Plan.", agent=tech, context=[t1])
t3 = Task(description="Écrire le code source.", expected_output="Fichiers créés.", agent=dev, context=[t2])

t4 = Task(
    description=(
        "1. Créer le README.md. "
        "2. Utiliser terminal_tool pour: git add . && git commit -m 'Clean AI Update' && git push origin main. "
        "IMPORTANT: Le .gitignore est déjà là, respecte-le !"
    ),
    expected_output="Projet propre sur GitHub.",
    agent=devops,
    context=[t3]
)

studio = Crew(agents=[po, tech, dev, devops], tasks=[t1, t2, t3, t4], process=Process.sequential)

print("### 🚀 Studio Turbo - Version Sécurisée ###")
studio.kickoff(inputs={'idee_projet': 'Application de tracking des meilleures boucheries de Loire-Atlantique'})
