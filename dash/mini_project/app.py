import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Dash Practise'),
    dcc.Graph(id='example',
        figure ={
            'data': [
                {'x':[1,2,3,4,5], 'y':[5,6,7,3,9], 'type':'line', 'name':'boats'},
                {'x':[1,2,3,4,5], 'y':[5,6,7,3,9], 'type':'bar', 'name':'cars'},
                ],
            'layout': {
                'title':'Basic Dash Example'
                }
            })
        ])

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
