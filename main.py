import streamlit as st
import json

def load_internships(filename='internships.json'):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['internships']

# Load the internships from the JSON file
internships = load_internships()

st.set_page_config(page_title="Interns R Us", page_icon=":tada:", layout="wide")

# Title of the app
st.title("Intern R Us :sparkles:")

# Subtitle
st.subheader("A database of CS internships by CS students :100:")

# Sidebar for user input
st.sidebar.header("Filter Internships")
major = st.sidebar.selectbox("Select your major", ["", "Computer Science"])  # Added empty string as default option

# Run the app
if __name__ == "__main__":
    st.write("Welcome to the Intern R Us platform! Use the sidebar to find a list of internships.")

# Display internships based on the selected major
if major == "Computer Science":
    st.header("Available Internships")
    for internship in internships:
        if internship["major"] == major:
            st.write(f"- **{internship['company_name']}**: {internship['position']} ({internship['location']}) - [More Info]({internship['link']})")

# Optionally, add a contact form
st.sidebar.header("Contact Us")
name = st.sidebar.text_input("Your Name")
email = st.sidebar.text_input("Your Email")
message = st.sidebar.text_area("Message")

if st.sidebar.button("Submit"):
    st.sidebar.success("Thank you for your message!")