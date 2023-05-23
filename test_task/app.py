from dash import Input, Output, State
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import (DashProxy, MultiplexerTransform,
                                    ServersideOutputTransform)
from database import df
from layouts import fig, get_layout, color_sequence
from utils import create_timeline


class EncostDash(DashProxy):
    def __init__(self, **kwargs):
        self.app_container = None
        super().__init__(transforms=[ServersideOutputTransform(),
                                     MultiplexerTransform()], **kwargs)


app = EncostDash(name=__name__, external_stylesheets=['/assets/styles.css'])
app.layout = get_layout()


@app.callback(
    Output('graph', 'figure'),
    [Input('filter', 'n_clicks')],
    [State('input-dropdown', 'value')],
    prevent_initial_call=True
)
def filtering(
    n_clicks, value
):
    if n_clicks is None:
        raise PreventUpdate

    if not value:
        # No values selected, return the original figure
        return fig
    # Filter the dataframe based on the selected values
    filtered_df = df[df['state'].isin(value)]

    filtered_fig = create_timeline(filtered_df, color_sequence)

    return filtered_fig


if __name__ == '__main__':
    app.run_server(debug=True)
