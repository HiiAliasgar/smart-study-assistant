import unittest

from study_assistant import EnhancedStudyAssistant


class StudyAssistantTests(unittest.TestCase):
    def setUp(self):
        self.assistant = EnhancedStudyAssistant()

    def test_plan_has_consistent_schedule_and_totals(self):
        plan = self.assistant.create_study_plan(" Python ", 10, 30)
        self.assertEqual(plan["subject"], "Python")
        self.assertEqual(plan["sessions_per_week"], 7)
        self.assertEqual(plan["total_weeks"], 5)
        self.assertEqual(len(plan["schedule"]), 7)
        self.assertAlmostEqual(plan["planned_hours"], plan["total_sessions"] * plan["hours_per_session"])

    def test_short_deadline_does_not_schedule_beyond_deadline(self):
        plan = self.assistant.create_study_plan("Python", 5, 1)
        self.assertEqual(plan["total_sessions"], 1)
        self.assertEqual(len(plan["schedule"]), 1)

    def test_rejects_invalid_plan_inputs(self):
        for args in [("", 2, 7), ("Python", 0, 7), ("Python", 2, 0), ("Python", -1, 7)]:
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    self.assistant.create_study_plan(*args)

    def test_unknown_resource_topic_returns_empty_list(self):
        self.assertEqual(self.assistant.recommend_resources("quantum computing")["resources"], [])

    def test_progress_does_not_claim_completion_without_target(self):
        progress = self.assistant.track_progress("Python", 3, scores=[80, 90])
        self.assertEqual(progress["hours_studied"], 6.0)
        self.assertEqual(progress["average_score"], 85.0)
        self.assertIsNone(progress["completion_rate"])

    def test_progress_uses_explicit_target(self):
        progress = self.assistant.track_progress("Python", 5, target_sessions=10)
        self.assertEqual(progress["completion_rate"], "50.0%")

    def test_rejects_invalid_scores_and_negative_sessions(self):
        with self.assertRaises(ValueError):
            self.assistant.track_progress("Python", -1)
        with self.assertRaises(ValueError):
            self.assistant.track_progress("Python", 1, scores=[101])

    def test_support_is_honestly_marked_as_placeholder(self):
        result = self.assistant.get_support("Explain recursion")
        self.assertEqual(result["mode"], "placeholder")
        self.assertIn("does not yet connect", result["response"])

    def test_summary_tracks_subjects_and_interactions(self):
        self.assistant.track_progress("Python", 1)
        summary = self.assistant.get_summary()
        self.assertEqual(summary["subjects"], ["Python"])
        self.assertEqual(summary["total_interactions"], 1)


if __name__ == "__main__":
    unittest.main()
