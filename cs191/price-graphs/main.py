import matplotlib.pyplot as plt

def example():
    # https://stackoverflow.com/questions/14432557/matplotlib-scatter-plot-with-different-text-at-each-data-point
    y = [2.56422, 3.77284, 3.52623, 3.51468, 3.02199]
    z = [0.15, 0.3, 0.45, 0.6, 0.75]
    n = [58, 651, 393, 203, 123]

    fig, ax = plt.subplots()
    ax.scatter(z, y)

    for i, txt in enumerate(n):
        ax.annotate(txt, (z[i], y[i]))

    plt.show()
    
if __name__ == '__main__':
    print("hi")
    example()