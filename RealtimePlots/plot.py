import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('data.csv')
    # x = data['idx']
    current_time = data['time']
    value = data['OOB']

    plt.cla()

    plt.plot( current_time,value)

    # plt.legend(loc='upper right')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=10000)

plt.tight_layout()
plt.show()