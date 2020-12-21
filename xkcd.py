import matplotlib.pyplot as plt
import numpy as np

with plt.xkcd():
    # Based on "Stove Ownership" from XKCD by Randall Monroe
    # http://xkcd.com/418/

    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.xticks([])
    plt.yticks([])
    ax.set_ylim([-30, 10])

    data = np.ones(100)
    data[70:] -= np.arange(30)


    plt.annotate(
        'THE DAY I REALIZED\nI MUST PREACH TOTALLY IRRELEVANT \n SOCIO-POLITICAL THEORY\n FROM MY IVORY TOWER',
        xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

    plt.plot(data)

    plt.xlabel('time')
    plt.ylabel('my productivity')
    fig.text(
        0.5, 0.05,
        'MY LIFE IN SUISSE/SCHWEIZ/SVIZZERA/SWITZERLAND',
        ha='center')

    # Based on "The Data So Far" from XKCD by Randall Monroe
    # http://xkcd.com/373/

    
plt.show()