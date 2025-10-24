import plotly.graph_objects as go
import json

# Parse the data
data = {"metrics": [{"metric": "Font Downloads", "before": 150, "after": 0}, {"metric": "CSS Size", "before": 75, "after": 2.5}, {"metric": "Page Weight", "before": 40, "after": 15}, {"metric": "JavaScript", "before": 0, "after": 5}]}

# Extract metrics and values
metrics = [item["metric"] for item in data["metrics"]]
before_values = [item["before"] for item in data["metrics"]]
after_values = [item["after"] for item in data["metrics"]]

# Abbreviate metric names to fit 15 character limit
abbreviated_metrics = []
for metric in metrics:
    if metric == "Font Downloads":
        abbreviated_metrics.append("Font Downloads")
    elif metric == "CSS Size":
        abbreviated_metrics.append("CSS Size")
    elif metric == "Page Weight":
        abbreviated_metrics.append("Page Weight")
    elif metric == "JavaScript":
        abbreviated_metrics.append("JavaScript")

# Create horizontal bar chart
fig = go.Figure()

# Add "Before" bars
fig.add_trace(go.Bar(
    name='Before',
    y=abbreviated_metrics,
    x=before_values,
    orientation='h',
    marker_color='#1FB8CD',
    hovertemplate='%{y}<br>Before: %{x} KB<extra></extra>'
))

# Add "After" bars
fig.add_trace(go.Bar(
    name='After',
    y=abbreviated_metrics,
    x=after_values,
    orientation='h',
    marker_color='#DB4545',
    hovertemplate='%{y}<br>After: %{x} KB<extra></extra>'
))

# Update layout
fig.update_layout(
    title='Portfolio Optimization Results',
    xaxis_title='Size (KB)',
    yaxis_title='',
    barmode='group',
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.05,
        xanchor='center',
        x=0.5
    )
)

# Update traces for better visual appearance
fig.update_traces(cliponaxis=False)

# Save as PNG and SVG
fig.write_image("portfolio_optimization.png")
fig.write_image("portfolio_optimization.svg", format="svg")

fig.show()