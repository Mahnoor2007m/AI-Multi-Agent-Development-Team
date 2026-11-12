from .llm import GeminiClient

class PythonDeveloper:
    role = "Python Developer / Backend Developer"

    def __init__(self, llm: GeminiClient):
        self.llm = llm

    def run(self, requirement: str, plan: str) -> str:
        instructions = """
You are an experienced Python backend developer.
Generate complete, modular, readable Python source code based on the requirement and plan.
Requirements:
- Use functions and/or classes with clear names.
- Include docstrings and helpful comments where useful.
- Validate inputs and handle expected errors.
- Prefer Python standard-library modules unless a dependency is essential.
- Do not include Markdown fences; return only valid Python source code.
- Do not claim that the code has been executed or verified.
"""
        return self.llm.generate(instructions, f"REQUIREMENT:\n{requirement}\n\nIMPLEMENTATION PLAN:\n{plan}")
