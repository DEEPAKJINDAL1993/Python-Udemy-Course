import networkx as nx
import matplotlib.pyplot as plt

# Define role hierarchy
role_hierarchy = [
    ("ACCOUNTADMIN", "SECURITYADMIN"),
    ("ACCOUNTADMIN", "SYSADMIN"),
    ("SECURITYADMIN", "USERADMIN"),
    ("SECURITYADMIN", "READ_ONLY_ROLE"),
    ("USERADMIN", "ANALYST_ROLE"),
    ("USERADMIN", "DEVELOPER_ROLE"),
    ("SYSADMIN", "DATA_ENGINEER_ROLE"),
    ("SYSADMIN", "REPORTING_ROLE"),
]

# Create directed graph
G = nx.DiGraph()
G.add_edges_from(role_hierarchy)

# Radial layout
pos = nx.shell_layout(G)

# Draw graph
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", edge_color="gray", font_size=10, font_weight="bold", arrows=True)
plt.title("Snowflake Role Hierarchy - Radial Layout")
plt.show()
