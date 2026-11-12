from .llm import GeminiClient

class CodeReviewer:
    role = "Code Reviewer / Senior Developer"

    def __init__(self, llm: GeminiClient):
        self.llm = llm

    def run(self, requirement: str, plan: str, code: str, tests: str) -> str:
        instructions = """
You are a strict senior Python code reviewer.
Compare the code with the requirement and plan. Review correctness, security,
input validation, exception handling, readability, maintainability, and test coverage.
Return:
- Overall assessment
- Critical issues (if any)
- Other issues / risks
- Test coverage observations
- Specific recommended fixes
- Approval status: APPROVE, APPROVE WITH CHANGES, or REJECT
Do not say tests passed because you have not executed them.
"""
        content = (
            f"REQUIREMENT:\n{requirement}\n\nPLAN:\n{plan}\n\n"
            f"PYTHON CODE:\n{code}\n\nTEST CASES:\n{tests}"
        )
        return self.llm.generate(instructions, content)
