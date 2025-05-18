import dash
from dash import html, dcc, dash_table
import pandas as pd
import dash_bootstrap_components as dbc

# Dados fictícios com base na imagem
data = {
    'Linha': ['Solução de Dívidas', 'BB Conta Garantida', 'Ourocard Empresarial',
              'BB Capital de Giro Digital', 'BNDES'],
    'Opr': ['49396904', '49396904', '49396904', '822406540', '21933'],
    'Cronograma': ['Mensal'] * 5,
    'Saldo Devedor': ['R$ 403.654,25', 'R$ 403.654,25', 'R$ 15.654,00', 'R$ 775.463,81', 'R$ 3.555.380,78'],
    'Saldo em Atraso': ['R$ 193.654,25', 'R$ 193.654,25', 'R$ 5.654,54', 'R$ 660,51', 'R$ 749.993,05'],
    'Dias em Atraso': [0, 30, 60, 18, 92],
    'Átivo Problemático': ['N', 'N', 'N', 'N', 'S']
}

df = pd.DataFrame(data)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(style={'fontFamily': 'Arial', 'padding': '20px'}, children=[
    html.Div([
        html.H3('Acerta Inad', style={'color': 'white', 'backgroundColor': '#0026a4', 'padding': '10px'}),
        html.Label('MCI'),
        dcc.Input(id='mci-input', type='text', style={'marginBottom': '20px'}),

        html.H5('Operações do Cliente'),
        dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left', 'padding': '5px'},
            style_header={'backgroundColor': 'lightgrey', 'fontWeight': 'bold'}
        )
    ]),

    html.Br(),
    html.H5('Soluções de negociação'),

    dbc.Row([
        dbc.Col([
            html.Div([
                html.Div('BB Conta Garantida\nOurocard Empresarial\nBB Capital de Giro Digital',
                         style={'backgroundColor': '#ffe600', 'padding': '5px'}),
                html.Div([
                    html.Div('1', style={'backgroundColor': '#0026a4', 'color': 'white', 'width': '30px',
                                          'textAlign': 'center', 'borderRadius': '50%', 'marginRight': '10px'}),
                    html.Div([
                        html.B('Parcelamento PJ'),
                        html.P('Essa solução permite alongar a dívida do cliente.\nBusque agregar garantia adicional.')
                    ])
                ], style={'display': 'flex'})
            ], style={'border': '1px solid lightgrey', 'borderRadius': '10px', 'padding': '10px', 'backgroundColor': '#e1ecfa'})
        ], width=4),

        dbc.Col([
            html.Div([
                html.Div('Solução de Dívidas PJ', style={'backgroundColor': '#ffe600', 'padding': '5px'}),
                html.Div([
                    html.Div('2', style={'backgroundColor': '#0026a4', 'color': 'white', 'width': '30px',
                                          'textAlign': 'center', 'borderRadius': '50%', 'marginRight': '10px'}),
                    html.Div([
                        html.B('Solução de Dívidas PJ'),
                        html.P('Essa linha gera restrição interna 126. O cliente não opera com o BB até a quitação da operação.\nPode ser feita com Abatimento Negocial.')
                    ])
                ], style={'display': 'flex'})
            ], style={'border': '1px solid lightgrey', 'borderRadius': '10px', 'padding': '10px', 'backgroundColor': '#e1ecfa'})
        ], width=4)
    ]),

    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div([
                html.Div('BNDES', style={'backgroundColor': '#ffe600', 'padding': '5px'}),
                html.Div([
                    html.Div('1', style={'backgroundColor': '#0026a4', 'color': 'white', 'width': '30px',
                                          'textAlign': 'center', 'borderRadius': '50%', 'marginRight': '10px'}),
                    html.Div([
                        html.B('Refinanciamento de BNDES'),
                        html.P('Essa solução só pode ser feita 1 vez. Não recomendamos fazer na carência.')
                    ])
                ], style={'display': 'flex'})
            ], style={'border': '1px solid lightgrey', 'borderRadius': '10px', 'padding': '10px', 'backgroundColor': '#e1ecfa'})
        ], width=6)
    ]),

    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div([
                html.Div('Solução de Dívidas', style={'backgroundColor': '#ffe600', 'padding': '5px'}),
                html.Div([
                    html.Div('1', style={'backgroundColor': '#0026a4', 'color': 'white', 'width': '30px',
                                          'textAlign': 'center', 'borderRadius': '50%', 'marginRight': '10px'}),
                    html.Div([
                        html.B('Solução de Dívidas PJ'),
                        html.P('Atenção, essa linha gera restrição interna 126.\nO cliente não opera com o BB até a quitação da operação.')
                    ])
                ], style={'display': 'flex'})
            ], style={'border': '1px solid lightgrey', 'borderRadius': '10px', 'padding': '10px', 'backgroundColor': '#e1ecfa'})
        ], width=6),

        dbc.Col([
            html.Div([
                html.Div('Solução de Dívidas UCR', style={'backgroundColor': '#ffe600', 'padding': '5px'}),
                html.Div([
                    html.Div('2', style={'backgroundColor': '#0026a4', 'color': 'white', 'width': '30px',
                                          'textAlign': 'center', 'borderRadius': '50%', 'marginRight': '10px'}),
                    html.Div([
                        html.B('Solução de Dívidas UCR'),
                        html.P('Linha de crédito negociada exclusivamente na UCR.')
                    ])
                ], style={'display': 'flex'})
            ], style={'border': '1px solid lightgrey', 'borderRadius': '10px', 'padding': '10px', 'backgroundColor': '#e1ecfa'})
        ], width=6)
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)

app.run_server(host='0.0.0.0', port=8050, debug=True)

