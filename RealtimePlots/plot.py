import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.ticker as mtick

plt.style.use('fivethirtyeight')

# x_vals = []
# y_vals = []

# index = count()
fig= plt.figure()
ax1=fig.add_subplot(1,1,1)
ax1.grid(False)
# ax1.set_ylim(0,20)

def animate(i):
    leng=200
    data = pd.read_csv('data.csv')
    # x = data['idx']
    current_time = data['time'].to_list()[-leng:]
    value = data['OOB'].to_list()[-leng:]
    # print(current_time)
    # plt.cla()
    # ax = data["OOB"].plot()

    # ax.yaxis.set_major_formatter(mtick.PercentFormatter())

    # ax=plt.plot(current_time,value)
    # print(type(ax))
    # print(ax)
    # ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    # plt.legend(loc='upper right')
    # plt.tight_layout()

    ax1.clear()
    ax1.grid(False)
    ax1.set_ylim(0,max(value)+5)
    ax1.plot(current_time,value)
    ax1.fill_between([13]*leng,[11]*leng,[15]*leng,alpha=0.2)
    plt.axhline(y=13, color='r', linestyle='--')
    plt.gca().axes.xaxis.set_ticklabels([])
    plt.gcf().autofmt_xdate()


    



ani = FuncAnimation(fig, animate, interval=100)

# plt.tight_layout()
plt.show()