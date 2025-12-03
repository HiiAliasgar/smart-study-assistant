# 🎓 Smart Study Assistant - AI Learning Agent

## Overview

The **Smart Study Assistant** is an intelligent multi-agent AI system designed to empower students with personalized learning support. This project was developed as part of the **Agents Intensive - Capstone Project** (Track: Agents for Good - Education).

## Problem Statement

Students often struggle with:
- Creating effective study plans
- Finding quality learning resources
- Maintaining consistent study habits
- Getting help when stuck on topics
- Tracking their learning progress

## Solution

Our Smart Study Assistant provides a comprehensive AI-powered learning companion with the following features:

### Core Features

1. **📅 Intelligent Study Planning**
   - Creates customized study schedules based on subject, available hours, and deadlines
   - Automatically calculates optimal sessions per week and total study duration
   - Generates completion dates and schedules

2. **📚 Resource Recommendations**
   - Suggests curated learning materials based on topic and difficulty level
   - Provides ratings and estimated learning hours for each resource
   - Adapts recommendations to learner's pace

3. **📊 Progress Tracking**
   - Monitors study sessions completed
   - Tracks hours studied
   - Calculates average performance scores
   - Displays completion rate percentages

4. **💬 24/7 Learning Support**
   - Provides instant responses to student questions
   - Suggests relevant learning materials and resources
   - Recommends reviewing previous sessions when needed

5. **🧠 Adaptive Learning**
   - Adjusts to each student's learning pace
   - Maintains session memory for continuous improvement
   - Personalized feedback based on progress

## Installation

### Prerequisites
- Python 3.7+
- No external dependencies required for core functionality

### Setup

```bash
# Clone the repository
git clone https://github.com/HiiAliasgar/smart-study-assistant.git
cd smart-study-assistant

# Run the main program
python study_assistant.py
```

## Usage

### Basic Example

```python
from study_assistant import EnhancedStudyAssistant

# Initialize the assistant
agent = EnhancedStudyAssistant()

# Create a study plan
plan = agent.create_study_plan('Python', hours_per_week=10, deadline_days=30)
print(plan)

# Get resource recommendations
resources = agent.recommend_resources('python', 'Intermediate')
print(resources)

# Track progress
progress = agent.track_progress('Python', sessions=10, scores=[85, 90, 88, 92])
print(progress)

# Get study support
support = agent.get_support('How do I use list comprehensions?')
print(support)

# Get session summary
summary = agent.get_summary()
print(summary)
```

## File Structure

```
smart-study-assistant/
├── study_assistant.py          # Main implementation
├── demo.py                     # Demo script with examples
├── README.md                   # This file
└── requirements.txt            # Python dependencies (if any)
```

## Key Components

### EnhancedStudyAssistant Class

The main class that implements all AI agent functionality:

**Methods:**
- `create_study_plan(subject, hours_per_week, deadline_days)` - Generates customized study plans
- `recommend_resources(topic, level='Intermediate')` - Provides learning resource recommendations
- `track_progress(subject, sessions, scores=None)` - Monitors student progress
- `get_support(question)` - Provides learning support
- `get_summary()` - Returns session summary

## Example Output

### Study Plan
```json
{
  "subject": "Python",
  "total_sessions": 20,
  "sessions_per_week": 5,
  "hours_per_session": 2,
  "total_weeks": 4,
  "completion_date": "2025-12-23",
  "schedule": ["Mon - 2 hours", "Wed - 2 hours", "Fri - 2 hours"]
}
```

## Educational Impact

- **Personalization**: Each student receives a customized learning journey
- **Accessibility**: Available 24/7 for student support
- **Motivation**: Progress tracking helps maintain student motivation
- **Efficiency**: Optimized study plans maximize learning outcomes
- **Adaptability**: System learns and adapts to individual learning patterns

## Technology Stack

- **Language**: Python 3.7+
- **Architecture**: Multi-Agent AI System
- **Paradigm**: Object-Oriented Programming
- **Core Concepts**: Session memory, progress tracking, intelligent recommendations

## Future Enhancements

- Integration with real learning platforms (Coursera, Udemy, etc.)
- Machine learning models for personalized recommendations
- Natural Language Processing for better question understanding
- Mobile app support
- Gamification features for increased engagement
- Parent/Teacher dashboard for progress monitoring

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is released under the Apache 2.0 License. See LICENSE file for details.

## Author

**Aliasgar Lohawala**
- GitHub: [@HiiAliasgar](https://github.com/HiiAliasgar)
- Track: Agents for Good (Education)

## Acknowledgments

- Built as part of the Agents Intensive - Capstone Project
- Inspired by the need to democratize quality education
- Dedicated to students worldwide pursuing their learning goals

---

**Last Updated**: December 2025

*Empowering education through AI - One student at a time* 🚀
