jobs={
    "Data Scientist":["Python","Machine learning","pandas"],
    "backend developer" : ["python","sql","api"],
    "web developer":["html","css", "javascript"],
    "AI Engineer":["python","deep learning","machine learning"], 
    "Software developer":["Python","java","javascript","SQL","C++"],
    "Android App Developer":["kotlin","java","Dart","c++"],
    "Gen AI Engineer":["python","RAG pipelines","LLM","vector database"],
}
ui=input("enter your skills: ").lower().split(" ")

best_role=""
similarity_rate=0

for role,skills in jobs.items():
    score=0
    for skill in ui:
        if skill.strip() in skills:
            score += 1
    if score>similarity_rate:
        similarity_rate=score
        best_role=role

print("Recommended role is : ",best_role)
