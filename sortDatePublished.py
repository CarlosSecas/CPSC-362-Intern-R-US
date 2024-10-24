"""Sort List by Date-Published: most recent to oldest"""
from datetime import datetime

def sort_internships(internships):
    # Function to extract the date for sorting
    def get_date(internship):
        return datetime.strptime(internship[4], "%m-%d-%Y")

    # Sort internships by date in descending order
    sorted_internships = sorted(internships, key=get_date, reverse=True)
    
    return sorted_internships


"""
::::::::::SAMPLE CODE::::::::::

# Example usage
internship_list = [
    ["Company A", "Intern", "New York", "http://linkA.com", "10-12-2024"],
    ["Company B", "Intern", "San Francisco", "http://linkB.com", "05-15-2023"],
    ["Company C", "Intern", "Los Angeles", "http://linkC.com", "03-01-2022"],
    ["Company D", "Intern", "Chicago", "http://linkD.com", "01-10-2024"]
]

print("Printing sorted date List--------")
sorted_internships = sort_internships(internship_list)
for internship in sorted_internships:
    print(internship)

::::::::::SAMPLE CODE::::::::::

"""