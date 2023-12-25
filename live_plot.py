import sys

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd


assert len(sys.argv) == 3, f'2 parameters, file name and interval, needed ({len(sys.argv) - 1} parameters given)'

STEPS_SHOWN = 200

plt.style.use('fivethirtyeight')
plt.tight_layout()


def animate(i):
    data = pd.read_csv(sys.argv[1])

    plt.cla()

    x_axis_column = data.columns[0]
    data.iloc[-STEPS_SHOWN:]
    for column in data.columns[1:]:
        plt.plot(data[x_axis_column], data[column], label=column, linewidth=2)
    if len(data[x_axis_column]) >= STEPS_SHOWN - 5:
        plt.xlim([data[x_axis_column][len(data[x_axis_column]) - STEPS_SHOWN + 10],
                  data[x_axis_column][len(data[x_axis_column]) - 1]])
    plt.legend(loc='upper left')
    plt.tight_layout()


animation = FuncAnimation(plt.gcf(), animate, interval=sys.argv[2],  cache_frame_data=False)
plt.show()
