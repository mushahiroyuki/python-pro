# pip install plotly==5.3.1
# plotly.pyという名前にすると、名前の「衝突」が起きてしまうので、ファイル名を変えてください
# グラフを表示する例は plotly-example2.py にあります
#@@range_begin(list1)  # ←この行は無視してください
import plotly.graph_objects as go

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[4, 5, 6],
    marker={'color': 'red', 'symbol': 104},
    mode='markers+lines',
    text=['one', 'two', 'three'],
    name='1st Trace',
)
#@@range_end(list1)  # ←この行は無視してください
