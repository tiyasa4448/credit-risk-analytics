class Gradebook:
    def __init__(self):
        # Initialize an empty gradebook as a dictionary
        self.gradebook = {}

    def add_entry(self, entry):
        # Add a new entry to the gradebook
        student_name, exam1_score, exam2_score, exam3_score = entry.split(', ')
        exam1_score = float(exam1_score)
        exam2_score = float(exam2_score)
        exam3_score = float(exam3_score)

        # Calculate the total score (average of three exam scores)
        total_score = (exam1_score + exam2_score + exam3_score) / 3

        # Store the entry in the gradebook dictionary
        self.gradebook[student_name] = {
            'exam1_score': exam1_score,
            'exam2_score': exam2_score,
            'exam3_score': exam3_score,
            'total_score': total_score
        }

    def get_entry(self, student_name):
        # Retrieve an entry from the gradebook using the student's name
        return self.gradebook.get(student_name, None)

# Example usage:
gradebook = Gradebook()

# Add entries to the gradebook
gradebook.add_entry("Alice, 85.5, 90.0, 78.5")
gradebook.add_entry("Bob, 92.0, 88.5, 95.5")

# Retrieve and print entries
print(gradebook.get_entry("Alice"))
print(gradebook.get_entry("Bob"))
