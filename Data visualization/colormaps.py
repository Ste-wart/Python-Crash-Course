import matplotlib as mpl
import matplotlib.pyplot as plt


def plot_colormaps(cmap):
    fig, ax = plt.subplots(figsize=(4, 0.4))
    col_map = plt.get_cmap(cmap)
    mpl.colorbar.ColorbarBase(ax, cmap=col_map, orientation='horizontal')

    plt.show()


for cmap_id in plt.colormaps():
    print(cmap_id)
    plot_colormaps(cmap_id)

print(plt.style.available)  # To see available styles.
