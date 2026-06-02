import networkx as nx
import matplotlib.pyplot as plt

# Define role hierarchy
role_hierarchy = [
    ("ACCOUNTADMIN", "SECURITYADMIN"),
    ("ACCOUNTADMIN", "SYSADMIN"),
    ("SECURITYADMIN", "USERADMIN"),
    ("SECURITYADMIN", "ANALYST_ROLE"),
    ("USERADMIN", "DEVELOPER_ROLE"),
    ("SYSADMIN", "DATA_ENGINEER_ROLE"),
    ("SYSADMIN", "REPORTING_ROLE"),
]

# Create a directed graph
G = nx.DiGraph()
G.add_edges_from(role_hierarchy)

# Alternative layout if PyGraphviz is unavailable
pos = nx.spring_layout(G, seed=42)  # Uses a force-directed algorithm

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=3000, edge_color="gray", font_size=10, font_weight="bold", arrows=True)

plt.title("Snowflake Role Hierarchy - Tree Diagram")
plt.show()
