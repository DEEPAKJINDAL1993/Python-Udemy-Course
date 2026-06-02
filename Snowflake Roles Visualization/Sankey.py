import plotly.graph_objects as go

# Define roles & links
roles = ["ACCOUNTADMIN", "SECURITYADMIN", "SYSADMIN", "USERADMIN", "READ_ONLY_ROLE", "ANALYST_ROLE", "DEVELOPER_ROLE", "DATA_ENGINEER_ROLE", "REPORTING_ROLE"]
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

# Convert roles to indices
role_map = {role: i for i, role in enumerate(roles)}
sources = [role_map[src] for src, _ in role_hierarchy]
targets = [role_map[tgt] for _, tgt in role_hierarchy]

# Create Sankey diagram
fig = go.Figure(go.Sankey(
    node=dict(label=roles, pad=20, thickness=30),
    link=dict(source=sources, target=targets, value=[1] * len(sources))
))
fig.update_layout(title_text="Snowflake Role Hierarchy - Sankey Diagram", font_size=10)
fig.show()
