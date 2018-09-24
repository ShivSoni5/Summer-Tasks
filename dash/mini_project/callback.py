import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children=[
    dcc.Input(id='input', value='Enter something', type='text'),
    html.Div(id='output')
    ])

@app.callback(
       Output(component_id='output', component_property='children'),
       [Input(component_id='input', component_property='value')]) 
def update_value(input_data):
    try:
        return str(float(input_data)**2)
    except:
        return "Some Error"


app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
