import numpy as np
import graph_generation
import matplotlib.pyplot as plt


from envelope_game_network import EnvelopeGameNetwork, MultiplexEnvelopeGameNetwork

N = 100
d = 10
m = 10
T = 10000
L = 5
a = 4
cl = 1
ch = 5
b = 4
d1 = -10
d2 = -2
beta = 10
mu = 0.5

def sim1():
    G_1 = graph_generation.generate_barabasi_albert_graph(N, m, plot=True)
    G_2 = graph_generation.generate_random_d_regular_graph(N, d, plot=True)

    p_options = [0.1, 0.4, 0.8]
    count = 1
    frequencies = plt.figure('Looking frequency for p = ({}, {}, {})'.format(0.1, 0.4, 0.8))
    exits = plt.figure('Exit frequency for p = ({}, {}, {})'.format(0.1, 0.4, 0.8))
    cooperations = plt.figure('Cooperation frequency for p = ({}, {}, {})'.format(0.1, 0.4, 0.8))
    for p in p_options:

        simulation_r = EnvelopeGameNetwork(N, G_2, T, p, a, cl, ch, b, d1, d2, 0, beta, mu)
        simulation_r.perform_simulation()

        simulation_ba = EnvelopeGameNetwork(N, G_1, T, p, a, cl, ch, b, d1, d2, 0, beta, mu)
        simulation_ba.perform_simulation()

        plt.figure(frequencies.number)
        ax = plt.subplot(len(p_options), 2, count)
        plt.plot(simulation_r.get_f_look(), '#F44B4A')
        plt.xlabel('t')
        plt.ylabel('Look Frequency')
        plt.figure(exits.number)
        ax = plt.subplot(len(p_options), 2, count)
        plt.plot(simulation_r.get_f_exit(), '#F44B4A')
        plt.xlabel('t')
        plt.ylabel('Exit Frequency')
        plt.figure(cooperations.number)
        ax = plt.subplot(len(p_options), 2, count)
        plt.plot(simulation_r.get_f_coop(), '#F44B4A')
        plt.xlabel('t')
        plt.ylabel('Cooperation Frequency')
        #ax.set_title("p = {}".format(p), y=1.08)
        count += 1
        plt.figure(frequencies.number)
        ax = plt.subplot(len(p_options), 2, count)
        plt.plot(simulation_ba.get_f_look())
        plt.xlabel('t')
        #plt.ylabel('Look Frequency')
        plt.figure(exits.number)
        ax = plt.subplot(len(p_options), 2, count)
        plt.plot(simulation_ba.get_f_exit())
        plt.xlabel('t')
        #plt.ylabel('Exit Frequency')
        plt.figure(cooperations.number)
        ax = plt.subplot(len(p_options), 2, count)
        plt.plot(simulation_ba.get_f_coop())
        plt.xlabel('t')
        #plt.ylabel('Cooperation Frequency')
        #ax.set_title("p = {}".format(p), y=1.08)
        count += 1

    plt.show()

def sim2(step):
    G = graph_generation.generate_barabasi_albert_graph(N, m, plot=True)
    total = step*step
    p_vector = np.linspace(0, 1, step)
    lmbd_vector = np.linspace(0, 1, step)
    frequencies = np.zeros((step, step))
    exits = np.zeros((step, step))
    coops = np.zeros((step, step))
    count = 0
    print(p_vector, lmbd_vector)
    for i in range(step):
        for j in range(step):
            simulation = EnvelopeGameNetwork(N, G, T, p_vector[i], a, cl, ch, b, d1, d2, lmbd_vector[j], beta, mu)
            simulation.perform_simulation()
            frequencies[i][j] = np.mean(simulation.get_f_look())
            exits[i][j] = np.mean(simulation.get_f_exit())
            coops[i][j] = np.mean(simulation.get_f_coop())
            print("Progress:", count, "out of", total)
            count += 1

    np.save("sim2-frequencies", frequencies)
    np.save("sim2-exits", exits)
    np.save("sim2-coops", coops)

def sim2_multiplex(step, all_layers=False):
    G = graph_generation.generate_multiplex_barabasi_albert_graph(N, m, L, plot=True)
    total = step * step
    p_vector = np.array([np.linspace(0, 1, step),]*L).transpose()
    lmbd_vector = np.array([np.linspace(0, 1, step),]*L).transpose()
    frequencies = np.zeros((L, step, step))
    exits = np.zeros((L, step, step))
    coops = np.zeros((L, step, step))
    count = 0
    print(p_vector, lmbd_vector)
    for i in range(step):
        for j in range(step):
            simulation = MultiplexEnvelopeGameNetwork(N, G, T, L, p_vector[i], np.full(L, a), np.full(L, cl), np.full(L, ch), np.full(L, b), np.full(L, d1), np.full(L, d2), lmbd_vector[j], np.full(L, beta), np.full(L, mu), all_layers=all_layers)
            simulation.perform_simulation()
            f_look = simulation.get_f_look()
            f_exit = simulation.get_f_exit()
            f_coop = simulation.get_f_coop()
            for l in range(L):
                frequencies[l][i][j] = np.mean(f_look[l])
                exits[l][i][j] = np.mean(f_exit[l])
                coops[l][i][j] = np.mean(f_coop[l])
            print("Progress:", count, "out of", total)
            count += 1

    if all_layers == True:
        np.save("output/sim2-frequencies-multiplex-full", frequencies)
        np.save("output/sim2-exits-multiplex-full", exits)
        np.save("output/sim2-coops-multiplex-full", coops)
    else:
        np.save("output/sim2-frequencies-multiplex", frequencies)
        np.save("output/sim2-exits-multiplex", exits)
        np.save("output/sim2-coops-multiplex", coops)

sim2_multiplex(51, all_layers=True)