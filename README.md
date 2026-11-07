# Smart Study Assistant (Rule-Based Prototype)

A Python learning-support prototype developed for the Agents Intensive capstone (Agents for Good — Education track). It provides deterministic study planning, a small static resource catalogue and local progress tracking. It does not currently use an AI model or multiple agents.

## Problem

Learners often need help turning a broad learning goal into a manageable plan. They may also need a simple way to record completed sessions and revisit questions.

## Project capabilities

The application currently provides:

- Creating a study plan from a subject, weekly study hours and a deadline.
- Recommending learning resources for a topic and level.
- Recording completed sessions and optional scores.
- Returning an explicit placeholder for study-support questions (no AI tutor is connected).
- Producing a summary of the current session's tracked progress.

## Example

```python
from study_assistant import EnhancedStudyAssistant

assistant = EnhancedStudyAssistant()

plan = assistant.create_study_plan(
    "Python",
    hours_per_week=10,
    deadline_days=30,
)
print(plan)

resources = assistant.recommend_resources("python", "Intermediate")
print(resources)

progress = assistant.track_progress(
    "Python",
    sessions=10,
    scores=[85, 90, 88, 92],
)
print(progress)

print(assistant.get_support("How do list comprehensions work?"))
print(assistant.get_summary())
```

## Run locally

```bash
git clone https://github.com/HiiAliasgar/smart-study-assistant.git
cd smart-study-assistant
python study_assistant.py

# Run the tests
python -m unittest discover -s tests -v
```

Check the source code for the current runtime dependencies and available entry points.

## Technology and scope

- Python
- Object-oriented application structure
- Study planning and progress-tracking logic
- Resource recommendation and question-support methods

This repository is a local rule-based learning prototype. Study plans and progress summaries are simple heuristics, not an adaptive-learning model. Resource suggestions are a small static catalogue. The support method is a placeholder and does not call an LLM or provide a 24/7 service.

[Source code](https://github.com/HiiAliasgar/smart-study-assistant)
