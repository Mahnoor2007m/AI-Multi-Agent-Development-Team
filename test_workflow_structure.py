import unittest
from unittest.mock import patch
from agents.workflow import DevelopmentTeam

class FakePlanner:
    def run(self, requirement):
        return "Plan"

class FakeDeveloper:
    def run(self, requirement, plan):
        return "def hello():\n    return 'hello'"

class FakeQA:
    def run(self, requirement, code):
        return "import unittest\nclass TestHello(unittest.TestCase):\n    pass"

class FakeReviewer:
    def run(self, requirement, plan, code, tests):
        return "APPROVE WITH CHANGES"

class WorkflowStructureTests(unittest.TestCase):
    @patch("agents.workflow.GeminiClient")
    def test_team_runs_all_stages_and_returns_deliverables(self, mock_client):
        team = DevelopmentTeam.__new__(DevelopmentTeam)
        team.planner = FakePlanner()
        team.developer = FakeDeveloper()
        team.qa = FakeQA()
        team.reviewer = FakeReviewer()

        result = team.run("Create a hello function")

        self.assertEqual(result["plan"], "Plan")
        self.assertIn("def hello", result["code"])
        self.assertIn("unittest", result["tests"])
        self.assertIn("APPROVE", result["review"])
        self.assertIn("Important Verification Note", result["report"])

if __name__ == "__main__":
    unittest.main()
