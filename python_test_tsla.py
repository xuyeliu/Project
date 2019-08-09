import datetime as dt
import pandas_datareader as pdr
import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates


start = dt.datetime(2016,1,1)
end = dt.datetime(2017,1,1)#声明开始和结束的时间
df = pdr.get_data_yahoo('TSLA',start,end)
'''
df = web.DataReader('TSLA','yahoo',start,end)
print(df.head())'''

df.to_csv('tsla.csv')#将截取的数据存到本地
df = pd.read_csv('tsla.csv',parse_dates=True,index_col=0)#index是按照第0列进行索引，即日期。按照日期索引,parse_date把csv的date把它处理成python里的date形式，按日期索引

df['10ma'] = df['Close'].rolling(window=10,min_periods=0).mean()#df[10ma]是定义一个新的列（十日均线，即前十天的价格数据），用close计算，rolling就是对当前进行操作，window去往前多少天的数据，min_periouds,如果拿不掉前十天就那当天的数据，mean是取均值

ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)#画的图占了6*1的格子一横排，(0,0z是画布上面的坐标)，rowspan列展开为几块，sharex图二的x轴和图一的x轴是一样的
ax2 = plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)

ax1.plot(df.index,df['Close'])
ax1.plot(df.index,df['10ma'])#index是x轴即日期
ax2.bar(df.index,df['Volume'])#条形图，看成交量，蓝色是十日均线，红的是除权后的价格

plt.show()
