import streamlit as st
import os, subprocess, time, yaml
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool
from crewai_tools import FileWriterTool

load_dotenv()

# --- CONFIG ---
MODERN_MODEL = "gemini/gemini-2.5-flash"
st.set_page_config(page_title="IA Agent Studio", layout="wide", page_icon="⚙️")
mon_llm = LLM(model=MODERN_MODEL, api_key=os.getenv("GOOGLE_API_KEY"))

# --- LOGIQUE YAML ---
def load_yaml(file):
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    return {}

# --- TOOLS ---
@tool("terminal_tool")
def terminal_tool(command: str) -> str:
    """Exécute une commande shell sur le serveur."""
    try:
        res = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        return f"Sortie: {res.stdout}\nErreur: {res.stderr}"
    except Exception as e:
        return str(e)

file_writer = FileWriterTool()

# --- SIDEBAR ---
with st.sidebar:
    st.header("📂 Projets")
    new_p = st.text_input("Nom du nouveau projet :")
    if st.button("➕ Créer"):
        if new_p:
            os.makedirs(new_p, exist_ok=True)
            st.rerun()

    projs = [d for d in os.listdir('.') if os.path.isdir(d) and d not in ['.venv', '.git', '__pycache__']]
    choice = st.selectbox("Projet actif :", ["---"] + projs)
    if choice != "---":
        st.session_state['active_project'] = choice
    
    st.divider()
    if st.button("🧨 Kill Processes"):
        subprocess.run("pkill -9 python", shell=True)
        st.rerun()

# --- MAIN ---
st.title("⚙️ IA Agent Studio")

if 'active_project' not in st.session_state or st.session_state['active_project'] == "---":
    st.warning("👈 Sélectionnez un projet.")
    st.stop()

p_path = os.path.abspath(st.session_state['active_project'])
agents_config = load_yaml('agents.yaml')
tasks_config = load_yaml('tasks.yaml')

t1, t2, t3, t4 = st.tabs(["🚀 Pilotage", "📜 Backlog", "📂 Code", "🧪 Test"])

with t1:
    goal = st.chat_input("Demande...")
    if goal:
        # Initialisation agents
        dev = Agent(config=agents_config['dev'], tools=[file_writer], llm=mon_llm)
        qa = Agent(config=agents_config['qa'], llm=mon_llm)
        ops = Agent(config=agents_config['ops'], tools=[terminal_tool], llm=mon_llm)

        # Crew
        crew = Crew(
            agents=[dev, qa, ops],
            tasks=[
                Task(config=tasks_config['dev_task'], agent=dev, inputs={'user_goal': goal, 'project_path': p_path}),
                Task(config=tasks_config['qa_task'], agent=qa),
                Task(config=tasks_config['ops_task'], agent=ops, inputs={'project_name': st.session_state['active_project']})
            ],
            process=Process.sequential, # Retour au séquentiel pour debug la stabilité
            verbose=True
        )

        with st.status("🛠️ Brigade en cours d'exécution...", expanded=True) as status:
            result = crew.kickoff()
            status.update(label="✅ Mission terminée", state="complete")
        st.markdown(result)

with t3:
    st.subheader(f"Fichiers dans {st.session_state['active_project']}")
    files = [f for f in os.listdir(p_path) if os.path.isfile(os.path.join(p_path, f))]
    if files:
        f_sel = st.selectbox("Voir le contenu :", files)
        with open(os.path.join(p_path, f_sel), 'r', encoding='utf-8') as f:
            st.code(f.read())
    else:
        st.info("Aucun fichier créé pour le moment.")

with t4:
    if st.button("🚀 Lancer l'App sur 8502"):
        subprocess.run("pkill -f 'port 8502'", shell=True)
        # Cherche le premier fichier .py pour le lancer
        py_files = [f for f in os.listdir(p_path) if f.endswith('.py')]
        if py_files:
            target = py_files[0]
            subprocess.Popen(f"streamlit run {target} --server.port 8502 --server.headless true", shell=True, cwd=p_path)
            st.success(f"Lancement de {target}...")
            time.sleep(2)
            st.link_button("Ouvrir", "http://185.203.56.53:8502")
        else:
            st.error("Pas de fichier .py trouvé.")
