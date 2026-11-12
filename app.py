import streamlit as st
from dotenv import load_dotenv
from agents.workflow import DevelopmentTeam

load_dotenv()

st.set_page_config(page_title="AI Multi-Agent Development Team", page_icon="🤖", layout="wide")
st.title("🤖 AI Multi-Agent Software Development Team")
st.write("Submit a software requirement and let four specialized AI agents plan, code, test, and review it.")

with st.sidebar:
    st.header("Configuration")
    st.caption("Add your Gemini API key to the .env file to enable AI-generated results.")
    st.info("The app does not execute generated code. Review it before using it in a real project.")

requirement = st.text_area(
    "Software requirement",
    height=180,
    placeholder="Example: Build a command-line task manager that lets users add, view, complete, and delete tasks."
)

if st.button("Start Development Workflow", type="primary", use_container_width=True):
    if not requirement.strip():
        st.warning("Please enter a software requirement first.")
    else:
        team = DevelopmentTeam()
        with st.spinner("The AI development team is working..."):
            try:
                result = team.run(requirement.strip())
                st.session_state["development_result"] = result
            except Exception as exc:
                st.error(f"Workflow failed: {exc}")

result = st.session_state.get("development_result")
if result:
    st.success("Development workflow completed.")
    tabs = st.tabs(["1. Plan", "2. Python Code", "3. QA Tests", "4. Code Review", "5. Final Report"])
    with tabs[0]:
        st.markdown(result["plan"])
    with tabs[1]:
        st.code(result["code"], language="python")
        st.download_button("Download generated_code.py", result["code"], "generated_code.py", "text/x-python")
    with tabs[2]:
        st.code(result["tests"], language="python")
        st.download_button("Download test_generated_code.py", result["tests"], "test_generated_code.py", "text/x-python")
    with tabs[3]:
        st.markdown(result["review"])
    with tabs[4]:
        st.markdown(result["report"])
        st.download_button("Download development_report.md", result["report"], "development_report.md", "text/markdown")
