import pandas as pd

# Create the initial table showing information about 5 states
data = {
    'State': ['California', 'Texas', 'Florida', 'New York', 'Alaska'],
    'Area': [163696, 268597, 65758, 54555, 665384], # in sq miles
    'Population': [39237836, 29527941, 21781128, 19835913, 732673]
}
df_states = pd.DataFrame(data)

# a) Print the complete information of states
print("--- State Information ---")
print(df_states.to_string(index=False))

# b) Print the name of the State having largest Area
largest_area_state = df_states.loc[df_states['Area'].idxmax(), 'State']
print(f"\nState with largest area: {largest_area_state}")

# c) Print the name of State having largest population
largest_pop_state = df_states.loc[df_states['Population'].idxmax(), 'State']
print(f"\nState with largest population: {largest_pop_state}")

# d) Create a mechanism to calculate the population density (Pop / Area)
df_states['Population_Density'] = df_states['Population'] / df_states['Area']
print("\n--- Table with Population Density ---")
print(df_states.to_string(index=False))

# e) Determine the name of State with highest population density
highest_density_state = df_states.loc[df_states['Population_Density'].idxmax(), 'State']
print(f"\nState with highest population density: {highest_density_state}")
