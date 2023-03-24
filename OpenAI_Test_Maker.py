import openai
import random
openai.api_key = "API-KEY"

course_name = input("Enter the name of your course: ")
school_year = input("Enter the school year of the course: ")
course_content = input("Enter the course content (seperated by commas): ")


model_engine = "davinci"
prompt = (f"Generate 10 multiple-choice questions for a {course_name} course in {school_year} year university. The course content covered is about {course_content}.")
completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=10, stop=None, temperature=0.7)

questions = []
for choice in completions.choices:
    question = choice.text.strip()
    if question:
        questions.append(question)


print("Here are your practice multiple-choice questions:")
for i, question in enumerate(questions):
    print(f"{i+1}. {question}")
