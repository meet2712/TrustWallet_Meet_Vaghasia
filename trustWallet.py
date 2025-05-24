import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load cleaned data
df = pd.read_csv('cleaned_crypto_transactions.csv')  # Ensure correct path

# Handle any date columns
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])

app = dash.Dash(__name__)

# KPI Calculations
total_tx = len(df)
total_volume = df['amount'].sum() if 'amount' in df.columns else 0
unique_assets = df['asset'].nunique() if 'asset' in df.columns else 0

# Charts
# 1. Transactions over Time
fig1 = px.line(df, x='date', y='amount', title='Transaction Volume Over Time') if 'date' in df.columns and 'amount' in df.columns else None

# 2. Top Assets by Transaction Value
if 'asset' in df.columns and 'amount' in df.columns:
    asset_summary = df.groupby('asset')['amount'].sum().sort_values(ascending=False).head(10)
    fig2 = px.bar(asset_summary, x=asset_summary.index, y=asset_summary.values, title='Top 10 Assets by Transaction Value', labels={'x': 'Asset', 'y': 'Total Value'})
else:
    fig2 = None

# 3. Distribution of Transaction Amounts
fig3 = px.histogram(df, x='amount', nbins=50, title='Distribution of Transaction Amounts') if 'amount' in df.columns else None

# Layout
app.layout = html.Div([
    html.H1("Crypto Transactions Dashboard", style={'textAlign': 'center'}),
    html.Div([
        html.Div([
            html.H3(f"Total Transactions: {total_tx}"),
            html.H3(f"Total Volume: {total_volume:,.2f}"),
            html.H3(f"Unique Assets: {unique_assets}")
        ], style={'width': '30%', 'display': 'inline-block', 'verticalAlign': 'top'}),
    ], style={'textAlign': 'center'}),
    html.Br(),
    html.Div([
        dcc.Graph(figure=fig1) if fig1 else html.P("Time data not available."),
        dcc.Graph(figure=fig2) if fig2 else html.P("Asset data not available."),
        dcc.Graph(figure=fig3) if fig3 else html.P("Amount data not available."),
    ]),
])

if __name__ == '__main__':
    app.run(debug=True)