import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from sqlalchemy import create_engine

# Conectar a la base de datos
engine = create_engine('mysql+pymysql://root:1234@host:3306/ticket')

# Crear la aplicación Dash
app = dash.Dash()

# Cargar los datos iniciales
def cargar_datos(municipio=None):
    query = "SELECT Municipio, Status, COUNT(*) as Quantity FROM solicitudes"
    if municipio:
        query += f" WHERE Municipio = '{municipio}'"
    query += " GROUP BY Municipio, Status"
    
    df = pd.read_sql(query, engine)
    return df

# Función para crear la gráfica
def crear_grafica(df):
    pv = pd.pivot_table(df, index=['Municipio'], columns=["Status"], values=['Quantity'], aggfunc=sum, fill_value=0)
    
    trace1 = go.Bar(x=pv.index, y=pv[('Quantity', 'Resuelto')], name='Resuelto')
    trace2 = go.Bar(x=pv.index, y=pv[('Quantity', 'Pendiente')], name='Pendiente')
    
    return {
        'data': [trace1, trace2],
        'layout': go.Layout(title='Estado de solicitudes por municipio', barmode='stack')
    }

# Layout de la aplicación
app.layout = html.Div(children=[
    html.H1(children='Reporte de Solicitudes'),
    html.Div(children='''Reporte de estado de solicitudes por municipio.'''),
    dcc.Dropdown(
        id='municipio-dropdown',
        options=[
            {'label': 'Todos', 'value': 'Todos'},
            # Agrega aquí más municipios según sea necesario
            {'label': 'Municipio 1', 'value': 'Municipio 1'},
            {'label': 'Municipio 2', 'value': 'Municipio 2'}
        ],
        value='Todos'
    ),
    dcc.Graph(
        id='status-graph'
    )
])

# Callback para actualizar la gráfica según el municipio seleccionado
@app.callback(
    Output('status-graph', 'figure'),
    [Input('municipio-dropdown', 'value')]
)
def actualizar_grafica(municipio):
    if municipio == 'Todos':
        df = cargar_datos()
    else:
        df = cargar_datos(municipio)
    
    return crear_grafica(df)

if __name__ == '__main__':
    app.run_server(debug=True)
