import math
from datetime import datetime, timedelta, timezone
from typing import Any


class EnhancedStudyAssistant:
    """A local rule-based study planner and progress tracker."""

    def __init__(self):
        self.session_memory: list[dict[str, Any]] = []
        self.student_progress: dict[str, dict[str, Any]] = {}
        self.difficulty_levels = ["Beginner", "Intermediate", "Advanced"]

    def create_study_plan(self, subject: str, hours_per_week: int, deadline_days: int) -> dict[str, Any]:
        """Create a simple weekly schedule with validated, internally consistent totals."""
        clean_subject = subject.strip() if isinstance(subject, str) else ""
        if not clean_subject:
            raise ValueError("Subject must not be empty.")
        if isinstance(hours_per_week, bool) or not isinstance(hours_per_week, int) or hours_per_week < 1:
            raise ValueError("hours_per_week must be a positive integer.")
        if isinstance(deadline_days, bool) or not isinstance(deadline_days, int) or deadline_days < 1:
            raise ValueError("deadline_days must be a positive integer.")

        sessions_per_week = min(7, hours_per_week)
        hours_per_session = hours_per_week / sessions_per_week
        total_weeks = math.ceil(deadline_days / 7)
        full_weeks, remaining_days = divmod(deadline_days, 7)
        total_sessions = sessions_per_week * full_weeks + min(sessions_per_week, remaining_days)
        schedule_days = min(sessions_per_week, deadline_days)
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][:schedule_days]
        plan = {
            "subject": clean_subject,
            "total_sessions": total_sessions,
            "sessions_per_week": sessions_per_week,
            "hours_per_session": round(hours_per_session, 2),
            "total_weeks": total_weeks,
            "planned_hours": round(total_sessions * hours_per_session, 2),
            "completion_date": (datetime.now(timezone.utc) + timedelta(days=deadline_days)).date().isoformat(),
            "schedule": [f"{day} - {hours_per_session:g} hours" for day in days],
        }
        self._log("study_plan_created", plan)
        return plan

    def recommend_resources(self, topic: str, level: str = "Intermediate") -> dict[str, Any]:
        """Return a small curated set of static resources for supported topics."""
        if not isinstance(topic, str) or not topic.strip():
            raise ValueError("Topic must not be empty.")
        if not isinstance(level, str) or not level.strip():
            raise ValueError("Level must not be empty.")
        resources_db = {
            "python": [
                {"name": "Python.org Tutorial", "rating": 4.8, "hours": "10"},
                {"name": "Real Python", "rating": 4.9, "hours": "30"},
                {"name": "Automate Boring Stuff", "rating": 4.9, "hours": "20"},
            ],
            "math": [
                {"name": "Khan Academy", "rating": 4.9, "hours": "40"},
                {"name": "3Blue1Brown", "rating": 5.0, "hours": "15"},
                {"name": "Brilliant.org", "rating": 4.8, "hours": "30"},
            ],
        }
        result = {
            "topic": topic.strip(),
            "level": level.strip(),
            "resources": resources_db.get(topic.strip().lower(), []),
        }
        self._log("resources_recommended", result)
        return result

    def track_progress(
        self,
        subject: str,
        sessions: int,
        scores: list[float] | None = None,
        hours_per_session: float = 2.0,
        target_sessions: int | None = None,
    ) -> dict[str, Any]:
        """Track completed sessions and optional scores without assuming a fixed target."""
        if not isinstance(subject, str) or not subject.strip():
            raise ValueError("Subject must not be empty.")
        if isinstance(sessions, bool) or not isinstance(sessions, int) or sessions < 0:
            raise ValueError("sessions must be a non-negative integer.")
        if isinstance(hours_per_session, bool) or not isinstance(hours_per_session, (int, float)) or not math.isfinite(hours_per_session) or hours_per_session <= 0:
            raise ValueError("hours_per_session must be a positive finite number.")
        if target_sessions is not None and (
            isinstance(target_sessions, bool)
            or not isinstance(target_sessions, int)
            or target_sessions < 1
        ):
            raise ValueError("target_sessions must be a positive integer when provided.")

        clean_scores = scores or []
        if not isinstance(clean_scores, list):
            raise ValueError("scores must be a list of numbers.")
        for score in clean_scores:
            if isinstance(score, bool) or not isinstance(score, (int, float)) or not math.isfinite(score) or not 0 <= score <= 100:
                raise ValueError("Each score must be a finite number between 0 and 100.")

        average = sum(clean_scores) / len(clean_scores) if clean_scores else None
        completion_rate = (
            f"{min(100, (sessions / target_sessions) * 100):.1f}%"
            if target_sessions is not None
            else None
        )
        progress = {
            "subject": subject.strip(),
            "sessions_completed": sessions,
            "hours_studied": round(sessions * float(hours_per_session), 2),
            "average_score": round(average, 2) if average is not None else None,
            "completion_rate": completion_rate,
        }
        self.student_progress[subject.strip()] = progress
        self._log("progress_tracked", progress)
        return progress

    def get_support(self, question: str) -> dict[str, Any]:
        """Return an honest local placeholder; no AI model or external support is connected."""
        if not isinstance(question, str) or not question.strip():
            raise ValueError("Question must not be empty.")
        response = {
            "question": question.strip(),
            "response": "This prototype does not yet connect to an AI tutor. Use your course materials or add a model provider to enable generated explanations.",
            "resources": [],
            "mode": "placeholder",
        }
        self._log("support_placeholder_returned", response)
        return response

    def _log(self, action: str, data: Any) -> None:
        self.session_memory.append({
            "action": action,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "data": data,
        })

    def get_summary(self) -> dict[str, Any]:
        return {
            "total_interactions": len(self.session_memory),
            "subjects": list(self.student_progress.keys()),
        }


if __name__ == "__main__":
    print("Smart Study Assistant loaded.")
    print("This is a local rule-based prototype; no AI model is connected.")
