import yfinance as yf
import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go


import plotly.io as poi

poi.renderers.default = 'browser'

# global_Styles
CHARTS_TEMPLATE = go.layout.Template(
    layout=dict(
        font=dict(family='Century Gothic')
    )
)

tickers = [
    'CL=F',
    'GC=F'
]  # CL - данные по нефти, #GC данные по золоту \\ все это к баксу
####Раздел где формируются датасет и на основе него ричуется график для OIL_GOLD
new_column = []
for memos in tickers:
    ticker = yf.Ticker(memos)
    dxx = ticker.history(period='max')['Close']
    dxx.name = memos
    new_column += [dxx]
df_clgc = pd.concat(new_column, axis=1)
df_clgc['CL/GC'] = df_clgc['CL=F'] / df_clgc['GC=F']
column_gc = df_clgc['CL/GC']
# print(column)
fig_clgc = px.line(df_clgc, y="CL/GC", title='Oil / GoldOZ')  # формирование графика
fig_clgc.update_layout(template=CHARTS_TEMPLATE)
# раздел, где формируется дата и график на нефть к баксу
data_closedprice_oil_usd = yf.Ticker('CL=F').history(period='max')['Close']
fig_oil_usd = px.line(data_closedprice_oil_usd, y="Close", title='Oil / USD')
fig_oil_usd.update_layout(template=CHARTS_TEMPLATE)
####Раздел где формируются датасет и на основе него ричуется график для GAS_GOLD
empresas = [
    'NG=F',
    'GC=F'
]  # NG - данные по натуральному газу, #GC данные по золоту \\ все это к баксу

recolector = []
for nemo in empresas:
    ticker = yf.Ticker(nemo)
    dx = ticker.history(period='max')['Close']
    dx.name = nemo
    recolector += [dx]
df_clgc = pd.concat(recolector, axis=1)
df_clgc['NG/GC'] = df_clgc['NG=F'] / df_clgc['GC=F']

fig = px.line(df_clgc, y="NG/GC", title='Natural Gas / GoldOZ')  # формирование графика
fig.update_layout(template=CHARTS_TEMPLATE)

####Раздел где формируются датасет и на основе него ричуется график для GAS_USD

gas_usd = 'NG=F'
data_closedprice_gas_usd = yf.Ticker(gas_usd).history(period='max')['Close']
# print(data_closedprice_gas_usd)
fig_gas_usd = px.line(data_closedprice_gas_usd, y="Close", title='Natural Gas / USD')
fig_gas_usd.update_layout(template=CHARTS_TEMPLATE)
#####Раздел где формируется дата и график для рсходов в USD


food = pd.read_csv("food1.csv")

# Create a Plotly chart
food_plotly = px.line(food, x="DATE", y="Expenditures", title='Expenditures/USD')
fig_gas_usd.update_layout(template=CHARTS_TEMPLATE)

#####Раздел где формируется дата и график для рсходов в GOLD

food_gold = pd.read_csv("food1.csv")
food_gold_plotly = px.line(food_gold, x="DATE", y="Ratio_gd", title='Expenditures/GoldOZ')
food_gold_plotly.update_layout(template=CHARTS_TEMPLATE)

#####Раздел где формируется дата и график для нефти бакса

data_closedprice_oil_usd = yf.Ticker('CL=F').history(period='max')['Close']
fig_oil_usd = px.line(data_closedprice_oil_usd, y="Close", title='Oil / USD')
fig_oil_usd.update_layout(template=CHARTS_TEMPLATE)



####Раздел, где формируется дата и графики относительно стоиомсти биткоина
tickers_for_btc = [
    'CL=F',
    'BTC=F'
]  # CL - данные по нефти, #GC данные по bitcoin \\ все это к баксу

new_column_btc = []
for memos_btc in tickers_for_btc:
    ticker = yf.Ticker(memos_btc)
    dxx_btc = ticker.history(period='max')['Close']
    dxx_btc.name = memos_btc
    new_column_btc += [dxx_btc]
df_cl_btc = pd.concat(new_column_btc, axis=1)
df_cl_btc['CL/BTC'] = df_cl_btc['CL=F'] / df_cl_btc['BTC=F']
column_btc = df_cl_btc['CL/BTC']

fig_cl_btc = px.line(df_cl_btc, y="CL/BTC", title='Oil/BTC')  # формирование графика
fig_cl_btc.update_layout(template=CHARTS_TEMPLATE)

# раздел, где формируется дата и график на нефть к баксу
data_closedprice_oil_usd_btc = yf.Ticker('CL=F').history(period='max')['Close']
fig_oil_usd_btc = px.line(data_closedprice_oil_usd_btc, y="Close", title='Oil / USD')
fig_oil_usd_btc.update_layout(template=CHARTS_TEMPLATE)

####Раздел где формируются датасет и на основе него ричуется график для GAS_GOLD
empresas_btc = [
    'NG=F',
    'BTC=F'
]  # NG - данные по натуральному газу, #BTC-USD данные по bitcoin \\ все это к баксу

recolector_btc = []
for nemo_btc in empresas_btc:
    ticker = yf.Ticker(nemo_btc)
    dx = ticker.history(period='max')['Close']
    dx.name = nemo_btc
    recolector_btc += [dx]
df_cl_btc = pd.concat(recolector_btc, axis=1)
df_cl_btc['NG/BTC'] = df_cl_btc['NG=F'] / df_cl_btc['BTC=F']

fig_btc = px.line(df_cl_btc, y="NG/BTC", title='Natural Gas / BTC')  # формирование графика
fig_btc.update_layout(template=CHARTS_TEMPLATE)

####Раздел где формируются датасет и на основе него ричуется график для GAS_USD

gas_usd = 'NG=F'
data_closedprice_gas_usd = yf.Ticker(gas_usd).history(period='max')['Close']
# print(data_closedprice_gas_usd)
fig_gas_usd = px.line(data_closedprice_gas_usd, y="Close", title='Natural Gas / USD')
fig_gas_usd.update_layout(template=CHARTS_TEMPLATE)
#####Раздел где формируется дата и график для рсходов в USD

food = pd.read_csv("food1.csv")
food_plotly_usd_1 = px.line(food, x="DATE", y="Expenditures", title='Expenditures/USD')
food_plotly_usd_1.update_layout(template=CHARTS_TEMPLATE)

#####Раздел где формируется дата и график для рсходов в GOLD

food_btc = pd.read_csv("food1.csv")
food_btc_plotly = px.line(food_btc, x="DATE", y="Ratio_BTC", log_y=True, title='Expenditures/BTC')
food_btc_plotly.update_layout(template=CHARTS_TEMPLATE)

#####Раздел где формируется дата и график для нефти бакса

data_closedprice_oil_usd_btc = yf.Ticker('CL=F').history(period='max')['Close']
fig_oil_usd_btc = px.line(data_closedprice_oil_usd_btc, y="Close", title='Oil / USD')
fig_oil_usd_btc.update_layout(template=CHARTS_TEMPLATE)
#####Раздел где объединяются даты нефти и золота и формируется новая графа ratioOilvsGold

empresas_btc = [
    'NG=F',
    'BTC=F'
]

####TabsContent
tab1_gold = [
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=food_plotly),
            html.Q('''Данный график показывает общие среднегодовые расходы американца (включая траты на ипотеку, здравоохранение, 
            крупные траты, повседневные траты и тд). Общий тренд графика говорит о том, что с каждым годом среднегодовые расходы американца в долларах растут.''')
        ]),
        dbc.Col([
            dcc.Graph(figure=food_gold_plotly),
            html.Q('''Данный график, как и соседний, показывает общие среднегодовые расходы американца, но уже по отношению не к доллару, а к одной тройской унции золота(включая траты на ипотеку, здравоохранение, 
            крупные траты, повседневные траты и тд). То есть на графике отражено то, сколько унций золота требуется американцу в год, чтобы покрыть личные расходы.
            Общий тренд графика говорит о том, что с каждым годом среднегодовые расходы американца в золоте падают.''')
        ])

    ]),

    dbc.Row([

        dbc.Col([
            dcc.Graph(figure=fig),
            html.Q('''График выше отражает соотношение унций золота к одному лоту газа.
             Иными словами график показывает то, сколько унций было необходимо в каждый момент времени, чтобы купить 1 лот газа по биржевой цене.''')
        ],
            width={'size': 6}),
        dbc.Col([
            dcc.Graph(figure=fig_gas_usd),
            html.Q(
                '''График Natural Gas/USD в реальном времени показывает стоимость за 1 лот газа на бирже в долларах.''')
        ])
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig_clgc),
            html.Q('''Данный график показывает динамику стоимости одного барреля нефти в унциях золота.''')
        ]),
        dbc.Col([
            dcc.Graph(figure=fig_oil_usd),
            html.Q('''На графике Oil/USD отражена стоимость барреля нефти в долларах США .''')
        ])

    ]),
    # dbc.Row([
    #     html.Footer(["Footer"])
    # ])
]

tab2_bitcoin = [
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=food_btc_plotly),
            html.Q('''Данный график, как и соседний, показывает общие среднегодовые расходы американца, но уже по отношению не к доллару, а к bitcoin (включая траты на ипотеку, здравоохранение, 
            крупные траты, повседневные траты и тд). То есть на графике отражено то, сколько монет bitcoin требуется американцу в год, чтобы покрыть личные расходы.
            Общий тренд графика говорит о том, что с каждым годом среднегодовые расходы американца в золоте падают.''')

        ],
            width={'size': 6}),
        dbc.Col([
            dcc.Graph(figure=food_plotly),
            html.Q('''Данный график показывает общие среднегодовые расходы американца (включая траты на ипотеку, здравоохранение, 
            крупные траты, повседневные траты и тд). Общий тренд графика говорит о том, что с каждым годом среднегодовые расходы американца в долларах растут.''')
        ],
            width={'size': 6})
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig_cl_btc),
            html.Q('''Oil/BTC отображает динамику стоимости барреля нефти в bitcoin.''')
        ],
            width={'size': 6}),
        dbc.Col([
            dcc.Graph(figure=fig_oil_usd_btc),
            html.Q('''Oil/USD отображает динамику стоимости барреля нефти в долларах США.''')
        ],
            width={'size': 6}),
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig_btc),
            html.Q('''Данный график показывает стоимость газа (одного биржевого лота фьючерса на газ) в bitcoin. То есть шкала Y показывает колличество необходимых монет bitcoin.''')
        ],
            width={'size': 6}),
        dbc.Col([
            dcc.Graph(figure=fig_gas_usd),
            html.Q('''Данный график показывает стоимость газа (одного биржевого лота фьючерса на газ) в долларах США.''')
        ],
            width={'size': 6})
    ]),
    # dbc.Row([
    #     html.Footer(["Footer"])
    # ])
]
tab3_about = [
    dbc.Row([html.Mark('''
    Проект создан, чтобы каждый мог наглядно увидеть выгоду если бы были частные деньги обеспеченные активами, как пример золотом или криптовалютой.
     Я склонен считать, что криптовалюта может являться альтернативой фиатным деньгам (деньги без обеспечния, на сегодняшний день обеспечением не пользуются, начиная с 1971 года),
     по скольку не возможно нарушить темп эмиссии ( иначе говоря создания нового объема монет ), а также на производство монеты и обработку транзакций затрачиваются вполне реальные ресурсы ( главным образом электроэнергия ), также криптовалютные майнеры осуществляют инвестиции в оборудование, помещения для его размещения и инфраструктуру для коммутации asic/gpu, для присоединения к вычислениям.
     Проект не является завершенным и будет дорабатываться.
    ''')])
]
####Раздел со стилем
'''LAYOUT'''
app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
# Header

app.layout = html.Div([
    dbc.Row([
        dbc.Col(
            html.Img(src=app.get_asset_url('images/icon.png'),
                     style={'width': '50px', 'marginLeft': '10px'}),
            width={'size': 1}
        ),
        dbc.Col(html.H1('Awaiking Project'),
                width={'size': 7}),
        dbc.Col(width={'size': 4})],
        className='app-header'),
    html.Div([
        # Body
        # Tabs
        dbc.Tabs([
            dbc.Tab(tab1_gold, label='*/Gold'),
            dbc.Tab(tab2_bitcoin, label='*/Bitcoin'),
            dbc.Tab(tab3_about, label='About Pjct')
        ])

    ],
        style={'marginLeft': '80px',
               'marginRight': '80px',
               'marginTop': '20px'}, )
])

if __name__ == '__main__':
   #app.run_server(debug=True)

