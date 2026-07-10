from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = 0
        self.age = 0
        self.course = ""

    def get_details(self):
        self.name = input("Enter student name: ")
        self.roll_no = int(input("Enter roll number: "))
        self.age = int(input("Enter age: "))
        self.course = input("Enter course: ")

    def display_details(self):
        print("\n----- Student Details -----")
        print(f"Name       : {self.name}")
        print(f"Roll No    : {self.roll_no}")
        print(f"Age        : {self.age}")
        print(f"Course     : {self.course}")
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300, 
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)