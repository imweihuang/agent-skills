from __future__ import annotations

import unittest
from pathlib import Path


SKILL = Path(__file__).resolve().parents[1] / "scheduled-work-loop" / "SKILL.md"


class ScheduledWorkLoopPolicyTests(unittest.TestCase):
    def test_scheduler_route_and_safety_contract(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        for phrase in (
            "explicitly asks for scheduled or repeated work",
            "`cron`",
            "`heartbeat`",
            "automation_update",
            "never emit raw scheduler directives",
            "durable sources",
            "report threshold",
            "stop condition",
            "Require explicit scheduling language",
        ):
            self.assertIn(phrase, text)

        for gate in (
            "secrets",
            "production",
            "live data",
            "money or trading",
            "destructive cleanup",
            "merges or shared-branch pushes",
            "dependencies or lockfiles or CI",
            "external messages",
            "shared infrastructure",
        ):
            self.assertIn(gate, text)

        self.assertNotIn("## Examples", text)
        self.assertNotIn("## Common Mistakes", text)


if __name__ == "__main__":
    unittest.main()
