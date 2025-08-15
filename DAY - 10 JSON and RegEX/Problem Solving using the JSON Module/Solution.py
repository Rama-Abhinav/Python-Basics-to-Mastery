import json 

#Taking Multi-line json input
""" The Multi - Line input as below
json_string = [
    {"name": "Alice", "marks": {"math": 95, "science": 92, "english": 88}},
    {"name": "Bob", "marks": {"math": 72, "science": 68, "english": 74}},
    {"name": "Charlie", "marks": {"math": 45, "science": 50, "english": 40}}
]
""" 

print("Enter JSON Data (Type END on a new line to finish input): ")

lines = []

while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

json_string = "\n".join(lines)

def Average(Val):
    Avg = sum(Val)/len(Val)
    return round(Avg,2)

Student_Data = json.loads(json_string)
# Grade = "" ----> No need for Grade = "" outside the loop

Result_List = []

for student in Student_Data:
    Marks_Rec = student["marks"]
    Mark_Vals = Marks_Rec.values()
    Avg_Marks = Average(Mark_Vals)
    if Avg_Marks >= 90:
        Grade = "A"
    elif Avg_Marks >=75 and Avg_Marks < 90:
        Grade = "B"
    elif Avg_Marks >=50 and Avg_Marks < 75:
        Grade = "C"
    elif Avg_Marks < 50 :
        Grade = "F"
    Result_List.append({"name":student["name"], "Average Marks":Avg_Marks, "Grade":Grade})


Json_File = json.dumps(Result_List,indent=4)

print(Json_File)
