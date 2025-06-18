import unittest
from scoring import calculate_pillar_score, calculate_overall_maturity_score, map_score_to_level, PILLAR_WEIGHTS, MATURITY_LEVELS

class TestScoring(unittest.TestCase):

    def test_calculate_pillar_score(self):
        self.assertAlmostEqual(calculate_pillar_score([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(calculate_pillar_score([5, 5, 5, 5, 5]), 5.0)
        self.assertAlmostEqual(calculate_pillar_score([1, 1, 1, 1, 1]), 1.0)
        self.assertAlmostEqual(calculate_pillar_score([]), 0.0) # As per current design
        self.assertAlmostEqual(calculate_pillar_score([2, 3, 4]), 3.0)

    def test_calculate_overall_maturity_score(self):
        # Test case 1: All scores are 3.0
        overall_raw, overall_pct = calculate_overall_maturity_score(3.0, 3.0, 3.0, 3.0, 3.0, 3.0)
        self.assertAlmostEqual(overall_raw, 3.0)
        self.assertAlmostEqual(overall_pct, 50.0)

        # Test case 2: All scores are 1.0
        overall_raw, overall_pct = calculate_overall_maturity_score(1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        self.assertAlmostEqual(overall_raw, 1.0)
        self.assertAlmostEqual(overall_pct, 0.0)

        # Test case 3: All scores are 5.0
        overall_raw, overall_pct = calculate_overall_maturity_score(5.0, 5.0, 5.0, 5.0, 5.0, 5.0)
        self.assertAlmostEqual(overall_raw, 5.0)
        self.assertAlmostEqual(overall_pct, 100.0)

        # Test case 4: Mixed scores
        # Business: 4 (w:0.25), People: 3 (w:0.15), Governance: 2 (w:0.10), Platform: 5 (w:0.25), Security: 3 (w:0.10), Operations: 4 (w:0.15)
        # Expected raw: (4*0.25) + (3*0.15) + (2*0.10) + (5*0.25) + (3*0.10) + (4*0.15)
        #              = 1.00 + 0.45 + 0.20 + 1.25 + 0.30 + 0.60 = 3.80
        # Expected pct: (3.80 - 1) * 25 = 2.80 * 25 = 70.0
        overall_raw, overall_pct = calculate_overall_maturity_score(business_score=4.0, people_score=3.0, governance_score=2.0, platform_score=5.0, security_score=3.0, operations_score=4.0)
        self.assertAlmostEqual(overall_raw, 3.80)
        self.assertAlmostEqual(overall_pct, 70.0)

    def test_map_score_to_level(self):
        # Test boundaries and within levels
        self.assertEqual(map_score_to_level(1.0), MATURITY_LEVELS["Level 1"])
        self.assertEqual(map_score_to_level(1.80), MATURITY_LEVELS["Level 1"])
        self.assertEqual(map_score_to_level(1.5), MATURITY_LEVELS["Level 1"])

        self.assertEqual(map_score_to_level(1.81), MATURITY_LEVELS["Level 2"])
        self.assertEqual(map_score_to_level(2.60), MATURITY_LEVELS["Level 2"])
        self.assertEqual(map_score_to_level(2.2), MATURITY_LEVELS["Level 2"])

        self.assertEqual(map_score_to_level(2.61), MATURITY_LEVELS["Level 3"])
        self.assertEqual(map_score_to_level(3.40), MATURITY_LEVELS["Level 3"])
        self.assertEqual(map_score_to_level(3.0), MATURITY_LEVELS["Level 3"])

        self.assertEqual(map_score_to_level(3.41), MATURITY_LEVELS["Level 4"])
        self.assertEqual(map_score_to_level(4.20), MATURITY_LEVELS["Level 4"])
        self.assertEqual(map_score_to_level(3.8), MATURITY_LEVELS["Level 4"])

        self.assertEqual(map_score_to_level(4.21), MATURITY_LEVELS["Level 5"])
        self.assertEqual(map_score_to_level(5.0), MATURITY_LEVELS["Level 5"])
        self.assertEqual(map_score_to_level(4.6), MATURITY_LEVELS["Level 5"])

        # Test invalid scores
        self.assertEqual(map_score_to_level(0.5), "Invalid score: Score must be between 1.0 and 5.0")
        self.assertEqual(map_score_to_level(5.01), "Invalid score: Score must be between 1.0 and 5.0")
        self.assertEqual(map_score_to_level(-1.0), "Invalid score: Score must be between 1.0 and 5.0")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
