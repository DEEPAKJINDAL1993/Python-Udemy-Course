import json
from jinja2 import Template
from nse_data import NSEData

# Instantiate the NSEData class
nse = NSEData()

# Fetch stock data for RELIANCE (RELIANCE)
stock_data = nse.get_stock_data('RELIANCE')

# stock_data_df = pd.json_normalize(stock_data)
if stock_data:
    print("Current Stock Data:")
    print(json.dumps(stock_data, indent=4))


# Function to convert JSON data to an HTML grid layout
def json_to_html_grid(json_data):
    html = '<html>\n<head>\n<style>\n'

    # Add CSS for grid layout and tile styling
    html += """
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        padding: 20px;
    }
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));  /* Increased min-width for tiles */
        gap: 20px;
    }
    .tile {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;  /* Increased padding */
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        overflow: hidden;  /* Prevent overflow */
        word-wrap: break-word;  /* Ensure long text wraps properly */
    }
    .tile:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    .tile h3 {
        margin-top: 0;
        font-size: 20px;
        background-color: #007BFF;
        color: white;
        padding: 12px;  /* Increased padding */
        border-radius: 5px;
        text-align: center;  /* Center title */
    }
    table {
        width: 100%;
        border-collapse: collapse;
    }
    td, th {
        padding: 10px;  /* Increased padding for better spacing */
        text-align: left;
        font-size: 14px;
    }
    td {
        font-weight: 400;
        color: #333;
    }
    th {
        font-weight: 600;
        color: #007BFF;
    }
    </style>\n</head>\n<body>\n"""

    # Start the grid container
    html += '<div class="grid-container">\n'

    # Call recursive function to generate tiles for each section
    for section_name, section_data in json_data.items():
        html += f'<div class="tile">\n<h3>{section_name.capitalize()}</h3>\n'
        html += json_to_html_recursive(section_data)
        html += '</div>\n'

    # End the grid container
    html += '</div>\n</body>\n</html>'
    return html


# Recursive function to handle different types of data (unchanged)
def json_to_html_recursive(data):
    html_content = ""

    if isinstance(data, dict):  # Handle JSON object
        html_content += "<table>\n"
        for key, value in data.items():
            html_content += f"<tr><th>{key}</th><td>{json_to_html_recursive(value)}</td></tr>\n"
        html_content += "</table>\n"

    elif isinstance(data, list):  # Handle JSON array
        html_content += "<ul>\n"
        for item in data:
            html_content += f"<li>{json_to_html_recursive(item)}</li>\n"
        html_content += "</ul>\n"

    else:  # Handle primitive data types (string, int, float, etc.)
        html_content += str(data)

    return html_content


# Convert JSON data to HTML grid
html_output = json_to_html_grid(stock_data)

# Save the generated HTML to a file
with open("json_to_grid.html", "w") as f:
    f.write(html_output)

# Print HTML output to the console (optional)
print(html_output)
