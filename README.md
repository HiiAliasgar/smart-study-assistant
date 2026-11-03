# Smart Study Assistant

A Python learning-support project developed for the Agents Intensive capstone (Agents for Good — Education track). It explores how a single assistant can help a learner plan study sessions, find resources, record progress and ask study questions.

## Problem

Learners often need help turning a broad learning goal into a manageable plan. They may also need a simple way to record completed sessions and revisit questions.

## Project capabilities

The repository describes an assistant with methods for:

- Creating a study plan from a subject, weekly study hours and a deadline.
- Recommending learning resources for a topic and level.
- Recording completed sessions and optional scores.
- Answering study-support questions.
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
```

Check the source code for the current runtime dependencies and available entry points.

## Technology and scope

- Python
- Object-oriented application structure
- Study planning and progress-tracking logic
- Resource recommendation and question-support methods

This repository is a learning prototype. The README's described functionality should not be interpreted as a validated adaptive-learning model, a 24/7 hosted service, or a production multi-agent platform.

[Source code](https://github.com/HiiAliasgar/smart-study-assistant)
