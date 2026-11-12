from .llm import GeminiClient

class ProjectPlanner:
    role = "Project Planner / Software Architect"

    def __init__(self, llm: GeminiClient):
        self.llm = llm

    def run(self, requirement: str) -> str:
        instructions = """
You are a senior software architect. Analyze the user's software requirement.
Produce:
1. Requirement summary
2. Assumptions and scope
3. Functional requirements
4. Proposed modules and function names
5. Step-by-step implementation plan
6. Input validation and error-handling strategy
7. Acceptance criteria
Be specific and use Python as the implementation language. Do not write the full code yet.
"""
        return self.llm.generate(instructions, requirement)
