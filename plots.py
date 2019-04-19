import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def sim1_plots():
    p_options = [1, 2, 3]
    count = 1
    rr = plt.figure('RR Graph')
    rr.suptitle("Random 10 Regular Graph")
    ba = plt.figure('BA graph')
    ba.suptitle("Barabasi-Albert Graph")
    for p in p_options:
        rr_looking = np.load("output/sim1_rr_looking_p{}.npy".format(p))
        rr_exits= np.load("output/sim1_rr_exit_p{}.npy".format(p))
        rr_coops = np.load("output/sim1_rr_coop_p{}.npy".format(p))
        ba_looking = np.load("output/sim1_ba_looking_p{}.npy".format(p))
        ba_exits = np.load("output/sim1_ba_exit_p{}.npy".format(p))
        ba_coops = np.load("output/sim1_ba_coop_p{}.npy".format(p))
        # Figure 1
        plt.figure(rr.number)
        ax = plt.subplot(len(p_options), 3, count)
        ax.set_ylim(0, 1)
        plt.plot(rr_looking)
        if p == 1:
            plt.ylabel('Look Frequency')
            ax.set_title('p = 0.1')
        elif p == 2:
            ax.set_title('p = 0.4')
        else:
            ax.set_title('p = 0.8')
        ax = plt.subplot(len(p_options), 3, count + len(p_options))
        ax.set_ylim(0, 1)
        plt.plot(rr_exits, '#F44B4A')
        if p == 1:
            plt.ylabel('Exit Frequency')
        ax = plt.subplot(len(p_options), 3, count + 2 * len(p_options))
        ax.set_ylim(0, 1)
        plt.plot(rr_coops, '#FF7F0E')
        plt.xlabel('t')
        if p == 1:
            plt.ylabel('Cooperation Frequency')
        # Figure 2
        plt.figure(ba.number)
        ax = plt.subplot(len(p_options), 3, count)
        ax.set_ylim(0, 1)
        plt.plot(ba_looking)
        if p == 1:
            plt.ylabel('Look Frequency')
            ax.set_title('p = 0.1')
        elif p == 2:
            ax.set_title('p = 0.4')
        else:
            ax.set_title('p = 0.8')
        ax = plt.subplot(len(p_options), 3, count + len(p_options))
        ax.set_ylim(0, 1)
        plt.plot(ba_exits, '#F44B4A')
        if p == 1:
            plt.ylabel('Exit Frequency')
        ax = plt.subplot(len(p_options), 3, count + 2 * len(p_options))
        ax.set_ylim(0, 1)
        plt.plot(ba_coops, '#FF7F0E')
        plt.xlabel('t')
        if p == 1:
            plt.ylabel('Cooperation Frequency')
        count += 1

def sim1_multiplex_plots(L, num_p, strategy):
    player1_strategies = []
    initial_player1_strategies = []
    player2_strategies = []
    initial_player2_strategies = []
    for p in range(num_p):
        player1_strategies.append(np.zeros(6))
        initial_player1_strategies.append(np.zeros(6))
        player2_strategies.append(np.zeros(4))
        initial_player2_strategies.append(np.zeros(4))
        player_strategies = np.load("output/sim1_multiplex_{}_strategy_{}.npy".format(p, strategy))
        initial_player_strategies = np.load("output/sim1_multiplex_initial_{}_strategy_{}.npy".format(p, strategy))
        for i in range(player_strategies.shape[1]):
            p1_strategies = set()
            initial_p1_strategies = set()
            p2_strategies = set()
            initial_p2_strategies = set()
            for l in range(player_strategies.shape[0]):
                p1_strategies.add(player_strategies[l][i][0])
                initial_p1_strategies.add(initial_player_strategies[l][i][0])
                p2_strategies.add(player_strategies[l][i][1])
                initial_p2_strategies.add(initial_player_strategies[l][i][1])
            player1_strategies[p][len(p1_strategies)-1] += 1
            initial_player1_strategies[p][len(initial_p1_strategies) - 1] += 1
            player2_strategies[p][len(p2_strategies)-1] += 1
            initial_player2_strategies[p][len(initial_p2_strategies) - 1] += 1
    # Figure 1
    fig, ax = plt.subplots(nrows=2, ncols=3)
    fig.suptitle("Player 1 strategies")
    g = sns.barplot(x=[1,2,3,4,5,6], y=initial_player1_strategies[0], ax=ax[0,0], palette="Reds_d")
    g.set_title("p = 0.1")
    g.set_ylabel("Number of players\n(before playing)")
    g = sns.barplot(x=[1,2,3,4,5,6], y=initial_player1_strategies[1], ax=ax[0,1], palette="Reds_d")
    g.set_title("p = 0.4")
    g = sns.barplot(x=[1,2,3,4,5,6], y=initial_player1_strategies[2], ax=ax[0,2], palette="Reds_d")
    g.set_title("p = 0.8")
    g = sns.barplot(x=[1, 2, 3, 4, 5, 6], y=player1_strategies[0], ax=ax[1, 0], palette="Blues_d")
    g.set_ylabel("Number of players\n(after playing)")
    g.set_xlabel("Ns")
    g = sns.barplot(x=[1, 2, 3, 4, 5, 6], y=player1_strategies[1], ax=ax[1, 1], palette="Blues_d")
    g.set_xlabel("Ns")
    g = sns.barplot(x=[1, 2, 3, 4, 5, 6], y=player1_strategies[2], ax=ax[1, 2], palette="Blues_d")
    g.set_xlabel("Ns")
    # Figure 2
    fig, ax = plt.subplots(nrows=2, ncols=3)
    fig.suptitle("Player 2 strategies")
    g = sns.barplot(x=[1,2,3,4], y=initial_player2_strategies[0], ax=ax[0,0], palette="Reds_d")
    g.set_title("p = 0.1")
    g.set_ylabel("Number of players\n(before playing)")
    g = sns.barplot(x=[1,2,3,4], y=initial_player2_strategies[1], ax=ax[0,1], palette="Reds_d")
    g.set_title("p = 0.4")
    g = sns.barplot(x=[1,2,3,4], y=initial_player2_strategies[2], ax=ax[0,2], palette="Reds_d")
    g.set_title("p = 0.8")
    g = sns.barplot(x=[1, 2, 3, 4], y=player2_strategies[0], ax=ax[1, 0], palette="Blues_d")
    g.set_ylabel("Number of players\n(after playing)")
    g.set_xlabel("Ns")
    g = sns.barplot(x=[1, 2, 3, 4], y=player2_strategies[1], ax=ax[1, 1], palette="Blues_d")
    g.set_xlabel("Ns")
    g = sns.barplot(x=[1, 2, 3, 4], y=player2_strategies[2], ax=ax[1, 2], palette="Blues_d")
    g.set_xlabel("Ns")

def sim2_plots():
    # read data
    frequencies = np.load("sim2-frequencies.npy")
    exits = np.load("sim2-exits.npy")
    coops = np.load("sim2-coops.npy")
    # initialize variables
    dim = frequencies.shape[0]
    print(dim)
    labels = [0, 0.2, 0.4, 0.6, 0.8, 1]
    fig, ax = plt.subplots(nrows=1, ncols=3)
    g = sns.heatmap(np.transpose(frequencies), xticklabels=10, yticklabels=10, ax=ax[0])
    g.set_xticklabels(labels, rotation=0)
    g.set_yticklabels(labels, rotation=0)
    g.set_title("Looking frequency")
    g.set_xlabel("p")
    g.set_ylabel("lambda")
    g.invert_yaxis()
    g = sns.heatmap(np.transpose(exits), xticklabels=10, yticklabels=10, ax=ax[1])
    g.set_xticklabels(labels, rotation=0)
    g.set_yticklabels(labels, rotation=0)
    g.set_title("Exit frequency")
    g.set_xlabel("p")
    g.set_ylabel("lambda")
    g.invert_yaxis()
    g = sns.heatmap(np.transpose(coops), xticklabels=10, yticklabels=10, ax=ax[2])
    g.set_xticklabels(labels, rotation=0)
    g.set_yticklabels(labels, rotation=0)
    g.set_title("Cooperation frequency")
    g.set_xlabel("p")
    g.set_ylabel("lambda")
    g.invert_yaxis()

def sim2_multiplex_plot(data, title):
    L = data.shape[0]
    labels = [0, 0.2, 0.4, 0.6, 0.8, 1]
    fig, ax = plt.subplots(nrows=2, ncols=3)
    fig.suptitle(title)
    for l in range(L):
        g = sns.heatmap(np.transpose(data[l]), xticklabels=10, yticklabels=10, ax=ax[l // 3, l % 3])
        g.set_xticklabels(labels, rotation=0)
        g.set_yticklabels(labels, rotation=0)
        g.set_title("Layer {}".format(l + 1))
        if l>2:
            g.set_xlabel("p")
        if l == 0 or l == 3:
            g.set_ylabel("lambda")
        g.invert_yaxis()
    avg_freq = np.sum(data, axis=0) / L
    g = sns.heatmap(np.transpose(avg_freq), xticklabels=10, yticklabels=10, ax=ax[1, 2])
    g.set_xticklabels(labels, rotation=0)
    g.set_yticklabels(labels, rotation=0)
    g.set_title("Average")
    g.set_xlabel("p")
    g.invert_yaxis()

def sim2_multiplex_plots(strategy=0):
    # read data
    if strategy == 0:
        frequencies = np.load("output/sim2-frequencies-multiplex-strat0.npy")
        exits = np.load("output/sim2-exits-multiplex-strat0.npy")
        coops = np.load("output/sim2-coops-multiplex-strat0.npy")
    elif strategy == 1:
        frequencies = np.load("output/sim2-frequencies-multiplex-strat1.npy")
        exits = np.load("output/sim2-exits-multiplex-strat1.npy")
        coops = np.load("output/sim2-coops-multiplex-strat1.npy")
    else:
        frequencies = np.load("output/sim2-frequencies-multiplex-strat2.npy")
        exits = np.load("output/sim2-exits-multiplex-strat2.npy")
        coops = np.load("output/sim2-coops-multiplex-full-strat2.npy")
    sim2_multiplex_plot(frequencies, "Looking frequency")
    sim2_multiplex_plot(exits, "Exit frequency")
    sim2_multiplex_plot(coops, "Coop frequency")

# sim2_plots()
# sim2_multiplex_plots(strategy=2)
# sim1_plots()
# sim1_multiplex_plots(5, 3, 2)
# plt.show()