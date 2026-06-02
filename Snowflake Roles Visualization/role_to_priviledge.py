import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Load the Excel file
file_path = "Role_Hierarchy.xlsx"  # Change this to your file path
df = pd.read_excel(file_path)

# Step 2: Create a directed graph
G = nx.DiGraph()

# Step 3: Add edges (role → privilege → object)
for _, row in df.iterrows():
    role = row["Grantee Name"]
    privilege = row["Privilege"]
    obj = row["Name"]

    # Create edges from role to privilege and privilege to object
    G.add_edge(role, privilege)
    G.add_edge(privilege, obj)

# Step 4: Define layout
pos = nx.spring_layout(G, seed=42)

# Step 5: Draw the graph
plt.figure(figsize=(10, 7))
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=3000, edge_color="gray", font_size=10,
        font_weight="bold", arrows=True)

# Step 6: Show the graph
plt.title("Snowflake Role Privileges Visualization")
plt.show()
