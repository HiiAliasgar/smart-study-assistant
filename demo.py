# Demo - Multi-Agent System in Action

from study_assistant import EnhancedStudyAssistant
import json

def main():
    print("\n" + "="*60)
    print("🎓 Smart Study Assistant - Demo Execution")
    print("="*60 + "\n")
    
    # Initialize the assistant
    agent = EnhancedStudyAssistant()
    
    # 1. Create Study Plan
    print("📅 CREATING STUDY PLAN")
    print("="*50)
    plan = agent.create_study_plan('Python', 10, 30)
    print(json.dumps(plan, indent=2))
    print("\n")
    
    # 2. Get Resource Recommendations
    print("📚 RECOMMENDING RESOURCES")
    print("="*50)
    resources = agent.recommend_resources('python', 'Intermediate')
    print(json.dumps(resources, indent=2))
    print("\n")
    
    # 3. Track Progress
    print("📊 TRACKING PROGRESS")
    print("="*50)
    progress = agent.track_progress('Python', 10, [85, 90, 88, 92])
    print(json.dumps(progress, indent=2))
    print("\n")
    
    # 4. Get Study Support
    print("💡 GETTING STUDY SUPPORT")
    print("="*50)
    support = agent.get_support('How do I use list comprehensions?')
    print(json.dumps(support, indent=2))
    print("\n")
    
    # 5. Session Summary
    print("📈 SESSION SUMMARY")
    print("="*50)
    summary = agent.get_summary()
    print(json.dumps(summary, indent=2))
    print("\n")
    
    print("✅ Demo Complete! All agents working successfully!")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
