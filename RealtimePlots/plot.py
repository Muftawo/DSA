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


def animate(i):
    data = pd.read_csv('data.csv')
    # x = data['idx']
    current_time = data['time']
    value = data['OOB']

    # plt.cla()
    ax = data["OOB"].plot()

    ax.yaxis.set_major_formatter(mtick.PercentFormatter())

    # ax=plt.plot(current_time,value)
    # print(type(ax))
    # print(ax)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    # plt.legend(loc='upper right')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate,frames = 200, interval=10000, blit = True)

plt.tight_layout()
plt.show()