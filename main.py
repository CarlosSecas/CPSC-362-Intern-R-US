import streamlit as st
from internshipsLists import csList, eeList, ceList, meList, businessList, accountingList, communicationList
from city_to_county import get_county_from_city

# Map majors to their corresponding internship lists
internship_data = {
    "Computer Science": csList,
    "Electrical Engineering": eeList,
    "Civil Engineering": ceList,
    "Mechanical Engineering": meList,
    "Business": businessList,
    "Accounting": accountingList,
    "Communication": communicationList
}

# Streamlit app setup
st.set_page_config(page_title="Interns R Us", page_icon=":tada:", layout="wide")

st.set_page_config(page_title="Interns R Us", page_icon=":tada:", layout="wide")

# Title of the app
st.title("Intern R Us :sparkles:")

# Subtitle
st.subheader("A database of internships categorized by major :technologist:")

# Sidebar for user input
st.sidebar.header("Filter Internships")
major = st.sidebar.selectbox("Select your major", ["", "Computer Science", "Electrical Engineering", "Civil Engineering", "Mechanical Engineering", "Business", "Accounting", "Communication"])
county = st.sidebar.selectbox("Select your county", ["", "Los Angeles County", "Orange County"])

# Run the app
if __name__ == "__main__":
    st.write("Welcome to the Intern R Us platform! Use the sidebar to find a list of internships.")

# Display internships based on the selected major and county
if major:
    st.header(f"Available Internships for {major}")
    internships = internship_data.get(major, [])
    
    if internships:
        for internship in internships:
            company, position, location, link = internship
            # Get the county from the location
            internship_county = get_county_from_city(location)
            
            # Filter by county if selected
            if county and internship_county != county:
                continue
            
            # Display the internship without the county in the location
            st.write(f"- **{company}**: {position} ({location.split(',')[0]}) - [More Info]({link})")
    else:
        st.write("No internships available for this major.")

# Contact form
st.sidebar.header("Contact Us")
name = st.sidebar.text_input("Your Name")
email = st.sidebar.text_input("Your Email")
message = st.sidebar.text_area("Message")

if st.sidebar.button("Submit"):
    st.sidebar.success("Thank you for your message!")
