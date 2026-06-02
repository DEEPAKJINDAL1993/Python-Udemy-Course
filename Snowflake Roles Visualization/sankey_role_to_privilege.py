import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = "browser"


# Step 1: Load the Excel file
file_path = "Role_Hierarchy.xlsx"  # Change to your actual file path
df = pd.read_excel(file_path)

# Step 2: Prepare unique nodes
nodes = list(set(df["Grantee Name"].tolist() + df["Name"].tolist()))  # Roles & Objects only
node_indices = {node: i for i, node in enumerate(nodes)}

# Step 3: Create source-target pairs (Role → Object)
sources = [node_indices[row["Grantee Name"]] for _, row in df.iterrows()]
targets = [node_indices[row["Name"]] for _, row in df.iterrows()]
values = [1] * len(sources)  # Equal weight for all connections

# Step 4: Assign colors based on Privilege type
privilege_colors = {
    "OWNERSHIP": "rgba(255,0,0,0.6)",      # Red for Ownership
    "USAGE": "rgba(0,128,0,0.6)",          # Green for Usage
    "SELECT": "rgba(0,0,255,0.6)",         # Blue for Select
    "INSERT": "rgba(255,165,0,0.6)",       # Orange for Insert
    "GRANT": "rgba(128,0,128,0.6)",        # Purple for Grant
    "CREATE": "rgba(75,0,130,0.6)",        # Indigo for Create
}
link_colors = [privilege_colors.get(row["Privilege"], "rgba(128,128,128,0.6)") for _, row in df.iterrows()]  # Default: Gray

# Step 5: Create Sankey Diagram
fig = go.Figure(go.Sankey(
    node=dict(
        pad=15, thickness=10, line=dict(color="black", width=0.5),
        label=nodes, color="lightblue"
    ),
    link=dict(
        source=sources, target=targets, value=values,
        color=link_colors  # Color-coded links based on Privilege
    )
))

# Step 6: Show the diagram
fig.update_layout(title_text="Snowflake Role Hierarchy (Sankey - Privilege Colored Links)", font_size=12)
fig.show()
