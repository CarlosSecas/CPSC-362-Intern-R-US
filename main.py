import sqlite3
import streamlit as st
from datetime import datetime
from internshipsLists import csList, eeList, ceList, meList, businessList, accountingList, communicationList
from city_to_county import get_county_from_city
from sortDatePublished import sort_internships
import pandas as pd

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

# Title of the app
st.title("Intern R Us :sparkles:")
st.subheader("A database of internships categorized by major :technologist:")

# Sidebar for user input
st.sidebar.header("Filter Internships")
major = st.sidebar.selectbox("Select your major", ["", "Computer Science", "Electrical Engineering", "Civil Engineering", "Mechanical Engineering", "Business", "Accounting", "Communication"])
county = st.sidebar.selectbox("Select your county", ["", "Los Angeles County", "Orange County"])

# Connect to SQLite database or create it if it doesn't exist
def get_db_connection():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    # Create a table to store messages if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    return conn

conn = get_db_connection()
cursor = conn.cursor()

# Function to save a message
def save_message(name, email, message):
    cursor.execute("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
                   (name, email, message))
    conn.commit()

# Display internships based on the selected major and county
if major:
    st.header(f"Available Internships for {major}")
    internships = internship_data.get(major, [])
    
    if internships:
        i = 1
        for internship in internships:
            company, position, location, link, date = internship
            internship_county = get_county_from_city(location)
            
            # Filter by county if selected by the user
            if county and internship_county != county:
                continue
            
            # st.write(f"- **{company}** {date}: {position} ({location.split(',')[0]}) - [More Info]({link})")
            df = pd.DataFrame(
                [
                    {"Company": company, 
                     "Date": date, 
                     "Position": position, 
                     "Location": location, 
                     "More Info": link,}
                ]
            )
            
            if i == 1:
                table = st.dataframe(
                df,
                width=9999,
                column_config={
                    "More Info": st.column_config.LinkColumn("Website URL"),
                },
                hide_index=True,
            )
                i += 1
            else:
                table.add_rows(df)
    else:
        st.write("No internships available for this major.")

# Contact form feature
st.sidebar.header("Contact Us")
name = st.sidebar.text_input("Your Name")
email = st.sidebar.text_input("Your Email")
message = st.sidebar.text_area("Message")

if st.sidebar.button("Submit"):
    if name and email and message:
        save_message(name, email, message)
        st.sidebar.success("Thank you for your message!")
    else:
        st.sidebar.error("Please fill out all fields.")

# Closes the database connection
conn.close()