import unittest

from planner import build_itinerary, estimate_total


class PlannerTests(unittest.TestCase):
    def test_builds_requested_number_of_days(self):
        self.assertEqual(len(build_itinerary("Lisbon", 4, ["food"])), 4)

    def test_interests_are_respected_when_available(self):
        plan = build_itinerary("Kyoto", 3, ["nature"])
        self.assertTrue(all(item["interest"] == "nature" for item in plan))

    def test_budget_is_reproducible(self):
        plan = build_itinerary("Vancouver", 2)
        self.assertEqual(estimate_total(plan, 20), sum(x["cost"] for x in plan) + 40)

    def test_invalid_days_raise(self):
        with self.assertRaises(ValueError):
            build_itinerary("Lisbon", 0)


if __name__ == "__main__":
    unittest.main()
