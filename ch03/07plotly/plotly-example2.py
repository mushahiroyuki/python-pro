# https://plotly.com/python/getting-started/  参照
# $ pip install plotly==5.3.1
# $ pip install dash
# $ python3 plotly-example2.py
#@@range_begin(list1)  # ←この行は無視してください
import plotly.graph_objects as go

fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.write_html('first_figure.html', auto_open=True)


# trace1 = go.Scatter(
#     x=[1, 2, 3],
#     y=[4, 5, 6],
#     marker={'color': 'red', 'symbol': 104},
#     mode='markers+lines',
#     text=['one', 'two', 'three'],
#     name='1st Trace',
# )

#@@range_end(list1)  # ←この行は無視してください
