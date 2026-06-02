import pandas as pd
import plotly.graph_objects as go
import ipywidgets as widgets
import random
from IPython.display import display
import plotly.io as pio
pio.renderers.default = "browser"

# **Step 1: Load the Excel file**
file_path = "Role_Hierarchy.xlsx"  # Update with actual path
df = pd.read_excel(file_path)

# **Step 2: Extract relevant columns**
df = df.rename(columns={"Grantee Name": "source", "Name": "target"})  # Ignore 'Privilege' for now

# **Step 3: Pick a Random Default Role as Focus**
all_roles = list(set(df["source"]).union(set(df["target"])))
default_focus_node = random.choice(all_roles)  # Select a random role for initial view

# **Step 4: Function to filter ±3 nodes**
def filter_sankey(data, focus_node, depth=3):
    selected_nodes = {focus_node}
    for _ in range(depth):
        upstream = data[data["target"].isin(selected_nodes)]["source"].tolist()
        downstream = data[data["source"].isin(selected_nodes)]["target"].tolist()
        selected_nodes.update(upstream + downstream)

    # Filter dataset
    filtered_data = data[data["source"].isin(selected_nodes) | data["target"].isin(selected_nodes)]
    return filtered_data

# **Step 5: Create Dropdown for Role Selection**
focus_node_dropdown = widgets.Dropdown(
    options=sorted(all_roles),
    value=default_focus_node,  # Set default node
    description="Focus Role:",
    style={'description_width': 'initial'}
)

# **Step 6: Function to Update Sankey**
def update_sankey(focus_node):
    filtered_data = filter_sankey(df, focus_node)

    # **Map roles to unique indices**
    unique_labels = list(set(filtered_data["source"]).union(set(filtered_data["target"])))
    label_map = {label: i for i, label in enumerate(unique_labels)}

    # Convert role names to indices
    filtered_data["source_idx"] = filtered_data["source"].map(label_map)
    filtered_data["target_idx"] = filtered_data["target"].map(label_map)

    # **Step 7: Create Sankey Diagram**
    fig = go.Figure(go.Sankey(
        node=dict(
            label=unique_labels,
            pad=20, thickness=15,  # Thinner lines for better readability
            color=["lightblue" if node != focus_node else "red" for node in unique_labels]
        ),
        link=dict(
            source=filtered_data["source_idx"],
            target=filtered_data["target_idx"],
            value=[1] * len(filtered_data)  # Uniform flow for simplicity
        )
    ))

    fig.update_layout(title_text=f"Sankey Focused on Role: {focus_node}", font_size=12)
    fig.show()

# **Step 8: Attach Function to Dropdown**
widgets.interactive(update_sankey, focus_node=focus_node_dropdown)

# **Step 9: Display Dropdown and Default Chart**
display(focus_node_dropdown)
update_sankey(default_focus_node)  # Automatically render with default focus
