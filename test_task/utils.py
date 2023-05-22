from datetime import timedelta

import plotly.express as px


def calculate_duration(df):
    """
    This function calculates duration of each period of work
    :param df: dataframe
    :return: dict
    (key: type of period,
    value: percentage of all time that was occupied by this period)
    """

    durations = {}

    for value in df['state'].unique():

        filtered_df = df[df['state'] == value]

        duration = 0

        for index, row in filtered_df.iterrows():
            period = float(row['duration_hour']) * 3600
            duration += period

        durations[value] = timedelta(duration)

    total_duration = sum(durations.values(), timedelta())

    percentages = {}
    for key, value in durations.items():
        percentages[key] = value / total_duration * 100

    return percentages


def create_timeline(df):

    """
        This function creates timeline graph
        with the use of original or filtered
        dataframe
    """

    fig = px.timeline(df, x_start="state_begin",
                      x_end="state_end",
                      y="endpoint_name",
                      custom_data=['state', 'reason', 'state_begin',
                                   'duration_min', 'shift_day', 'operator'],
                      color="state")

    fig.update_layout(
        xaxis=dict(title='Время'),
    )

    fig.update_traces(hovertemplate='<br>'.join([
        'Состояние: %{customdata[0]}',
        'Причина: %{customdata[1]}',
        'Начало: %{customdata[2]}',
        'Длительность: %{customdata[3]}',
        'Сменный день: %{customdata[4]}',
        'Оператор: %{customdata[5]}'
    ]
    ))

    return fig
