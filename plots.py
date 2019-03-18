import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def sim2_plots():
    # read data
    frequencies = np.load("sim2-frequencies.npy")
    exits = np.load("sim2-exits.npy")
    coops = np.load("sim2-coops.npy")

    dim = frequencies.shape[0]
    labels = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

    fig1, ax1 = plt.subplots()
    g = sns.heatmap(np.transpose(frequencies), xticklabels=5, yticklabels=5, ax=ax1)
    g.set_xticklabels(labels, rotation=0)
    g.set_yticklabels(labels, rotation=0)
    ax1.set_title("Looking frequency")
    fig1.tight_layout()
    plt.gca().invert_yaxis()
    plt.xlabel("p")
    plt.ylabel("lambda")
    fig2, ax2 = plt.subplots()


    ax2.set_title("Exit frequency")
    ax2.set_xticks(range(dim))
    ax2.set_xticklabels([x / (dim-1) for x in range(dim)])
    ax2.set_yticks(range(dim))
    print(np.linspace(0, 1, 6))
    ax2.set_yticklabels([x / (dim-1) for x in range(dim)])
    g = sns.heatmap(np.transpose(exits), xticklabels=5, yticklabels=5, ax=ax2)
    g.set_xticklabels(labels, rotation =0)
    g.set_yticklabels(labels, rotation=0)
    fig2.tight_layout()
    plt.gca().invert_yaxis()
    plt.xlabel("p")
    plt.ylabel("lambda")
    fig3, ax3 = plt.subplots()
    g = sns.heatmap(np.transpose(coops), xticklabels=5, yticklabels=5, ax=ax3)
    g.set_xticklabels(labels, rotation=0)
    g.set_yticklabels(labels, rotation=0)
    ax3.set_title("Cooperation frequency")
    #ax3.set_xticks(np.arange(0, 1, 0.2))
    #ax3.set_yticks(np.arange(0, 1, 0.2))
    fig3.tight_layout()
    plt.gca().invert_yaxis()
    plt.xlabel("p")
    plt.ylabel("lambda")
    #plt.show()

def sim2_multiplex_plot(data, title):
    L = data.shape[0]
    labels = [0, 0.2, 0.4, 0.6, 0.8, 1]
    fig, ax = plt.subplots(nrows=2, ncols=3)
    fig.suptitle(title)
    for l in range(L):
        # fig1, ax1 = plt.subplots()
        g = sns.heatmap(np.transpose(data[l]), xticklabels=10, yticklabels=10, ax=ax[l // 3, l % 3])
        g.set_xticklabels(labels, rotation=0)
        g.set_yticklabels(labels, rotation=0)
        g.set_title("Layer {}".format(l + 1))
        # fig.tight_layout()
        g.set_xlabel("p")
        g.set_ylabel("lambda")
        g.invert_yaxis()
    avg_freq = np.sum(data, axis=0) / L
    g = sns.heatmap(np.transpose(avg_freq), xticklabels=10, yticklabels=10, ax=ax[1, 2])
    g.set_xticklabels(labels, rotation=0)
    g.set_yticklabels(labels, rotation=0)
    g.set_title("Average")
    # fig.tight_layout()
    g.set_xlabel("p")
    g.set_ylabel("lambda")
    g.invert_yaxis()

def sim2_multiplex_plots(all_layers=False):
    # read data
    if all_layers == True:
        frequencies = np.load("output/sim2-frequencies-multiplex-full.npy")
        exits = np.load("output/sim2-exits-multiplex-full.npy")
        coops = np.load("output/sim2-coops-multiplex-full.npy")
    else:
        frequencies = np.load("output/sim2-frequencies-multiplex.npy")
        exits = np.load("output/sim2-exits-multiplex.npy")
        coops = np.load("output/sim2-coops-multiplex.npy")
    sim2_multiplex_plot(frequencies, "Looking frequency")
    sim2_multiplex_plot(exits, "Exit frequency")
    sim2_multiplex_plot(coops, "Coop frequency")
    #plt.show()

sim2_plots()
sim2_multiplex_plots(all_layers=False)
plt.show()