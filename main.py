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
st.title(":red[I]:orange[n]:green[t]:red[e]:orange[r]:green[n]:red[s] :blue[R] :green[U]:red[s] :sparkles:")
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

# Display search bar
intern_search = st.text_input("Search Internships by Company or Position!", value="")

# Space Separator
st.text("")

# Display internships based on the selected major and county
if major or intern_search:  # Trigger search if either a major is selected or the search bar is used
    if major:
        st.subheader(f"Available Internships for {major}")
        internships = internship_data.get(major, [])
    else:
        # If no major is selected, include all internships for the search
        internships = sum(internship_data.values(), [])

    if internships:
        # Create a DataFrame for the internships
        df = pd.DataFrame(internships, columns=["Company", "Position", "Location", "Link", "Date"])
        df["County"] = df["Location"].apply(get_county_from_city)

        # Apply search filter first if a search query is provided
        if intern_search:
            df = df[
                df["Company"].str.contains(intern_search, case=False, na=False) |
                df["Position"].str.contains(intern_search, case=False, na=False)
            ]

        # Apply major filter (if selected)
        if major:
            df_major = pd.DataFrame(
                internship_data.get(major, []),
                columns=["Company", "Position", "Location", "Link", "Date"]
            )
            df_major["County"] = df_major["Location"].apply(get_county_from_city)

            # Merge the filtered DataFrame with the major-specific DataFrame
            # Ensure both DataFrames have the same columns
            df = pd.merge(
                df,
                df_major,
                how="inner",
                on=["Company", "Position", "Location", "Link", "Date", "County"]
            )

        # Apply county filter if selected
        if county:
            df = df[df["County"] == county]

        # Display the filtered internships
        if not df.empty:
            st.dataframe(
                df[["Company", "Date", "Position", "Location", "Link"]],
                width=9999,
                column_config={"Link": st.column_config.LinkColumn("Website URL")},
                hide_index=True
            )
            st.markdown(f"**{len(df)}** internships found matching your criteria.")
        else:
            st.write("No internships found matching your search criteria.")
    else:
        st.write("No internships available for the selected major.")

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