import pandas as pd

# --- Step 0: Create a dummy CSV for demonstration (Optional) ---
data = {
    'title': ['Python Basics', 'Data Science 101', 'AI Fundamentals', 'Web Dev', 'Algorithms'],
    'author': ['John Doe', 'Jane Smith', 'John Doe', 'Alice Brown', 'Bob Wilson'],
    'edition': ['1st', '3rd', '2nd', '1st', '4th'],
    'publication_year': [2020, 2021, 2019, 2022, 2018],
    'publishing_house': ['TechPress', 'DataPub', 'TechPress', 'WebWorks', 'AcademicPress'],
    'price': [25.50, 45.00, 30.00, 20.00, 55.00]
}
pd.DataFrame(data).to_csv('books.csv', index=False)

# --- Main Application ---

# Load the dataframe
df = pd.read_csv('books.csv')

# a) Print the complete report in Tabular form
print("--- Full Book Report ---")
print(df.to_string(index=False))

# b) Print list of available books of a given author
author_name = "John Doe"
print(f"\n--- Books by {author_name} ---")
print(df[df['author'] == author_name])

# c) Print list of available books of a given publishing house
pub_house = "TechPress"
print(f"\n--- Books published by {pub_house} ---")
print(df[df['publishing_house'] == pub_house])

# d) Print the Titles of cheapest & costliest book available
cheapest_title = df.loc[df['price'].idxmin(), 'title']
costliest_title = df.loc[df['price'].idxmax(), 'title']
print(f"\nCheapest Book: {cheapest_title}")
print(f"Costliest Book: {costliest_title}")

# e) Print the list by sorting based on the year of publication
print("\n--- Books Sorted by Year ---")
print(df.sort_values(by='publication_year').to_string(index=False))
