import numpy as np
import graph_generation
from envelope_game_network import EnvelopeGameNetwork, MultiplexEnvelopeGameNetwork

# Parameters
N = 1000
d = 10
m = 10
T = 100000
L = 5
a = 4
cl = 1
ch = 5
b = 4
d1 = -10
d2 = -2
beta = 10
mu = 0.05

def sim1():
    G_1 = graph_generation.generate_barabasi_albert_graph(N, m, plot=True)
    G_2 = graph_generation.generate_random_d_regular_graph(N, d, plot=True)
    p_options = [0.1, 0.4, 0.8]
    rez_num = 1
    for p in p_options:
        simulation_r = EnvelopeGameNetwork(N, G_2, T, p, a, cl, ch, b, d1, d2, 0, beta, mu)
        simulation_r.perform_simulation()
        simulation_ba = EnvelopeGameNetwork(N, G_1, T, p, a, cl, ch, b, d1, d2, 0, beta, mu)
        simulation_ba.perform_simulation()
        np.save("output/sim1_rr_looking_p{}".format(rez_num), simulation_r.get_f_look())
        np.save("output/sim1_rr_exit_p{}".format(rez_num), simulation_r.get_f_exit())
        np.save("output/sim1_rr_coop_p{}".format(rez_num), simulation_r.get_f_coop())
        np.save("output/sim1_ba_looking_p{}".format(rez_num), simulation_ba.get_f_look())
        np.save("output/sim1_ba_exit_p{}".format(rez_num), simulation_ba.get_f_exit())
        np.save("output/sim1_ba_coop_p{}".format(rez_num), simulation_ba.get_f_coop())
        rez_num += 1

def sim1_multiplex(strategy=0):
    p_options = [0.1, 0.4, 0.8]
    lmbd_vector = np.zeros(L)
    G = graph_generation.generate_multiplex_barabasi_albert_graph(N, m, L, plot=True)
    for i in range(len(p_options)):
        p_vector = np.repeat(p_options[i], L)
        simulation = MultiplexEnvelopeGameNetwork(N, G, T, L, p_vector, np.full(L, a), np.full(L, cl), np.full(L, ch),
                                                  np.full(L, b), np.full(L, d1), np.full(L, d2), lmbd_vector,
                                                  np.full(L, beta), np.full(L, mu), strategy=strategy)
        player_strategies = simulation.get_players()
        np.save("output/sim1_multiplex_initial_{}_strategy_{}".format(i, strategy), player_strategies)
        simulation.perform_simulation()
        player_strategies = simulation.get_players()
        print(player_strategies)
        np.save("output/sim1_multiplex_{}_strategy_{}".format(i, strategy), player_strategies)

def sim2(step):
    G = graph_generation.generate_barabasi_albert_graph(N, m, plot=True)
    total = step * step
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

def sim2_multiplex(step, strategy=0):
    G = graph_generation.generate_multiplex_barabasi_albert_graph(N, m, L, plot=True)
    total = step * step
    p_vector = np.array([np.linspace(0, 1, step), ] * L).transpose()
    lmbd_vector = np.array([np.linspace(0, 1, step), ] * L).transpose()
    frequencies = np.zeros((L, step, step))
    exits = np.zeros((L, step, step))
    coops = np.zeros((L, step, step))
    count = 0
    print(p_vector, lmbd_vector)
    for i in range(step):
        for j in range(step):
            simulation = MultiplexEnvelopeGameNetwork(N, G, T, L, p_vector[i], np.full(L, a), np.full(L, cl),
                                                      np.full(L, ch), np.full(L, b), np.full(L, d1), np.full(L, d2),
                                                      lmbd_vector[j], np.full(L, beta), np.full(L, mu),
                                                      strategy=strategy)
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
    if strategy == 0:
        np.save("output/sim2-frequencies-multiplex-strat0", frequencies)
        np.save("output/sim2-exits-multiplex-strat0", exits)
        np.save("output/sim2-coops-multiplex-strat0", coops)
    elif strategy == 1:
        np.save("output/sim2-frequencies-multiplex-strat1", frequencies)
        np.save("output/sim2-exits-multiplex-strat1", exits)
        np.save("output/sim2-coops-multiplex-full-strat1", coops)
    else:
        np.save("output/sim2-frequencies-multiplex-strat2", frequencies)
        np.save("output/sim2-exits-multiplex-strat2", exits)
        np.save("output/sim2-coops-multiplex-strat2", coops)

# sim1()
# sim1_multiplex(strategy=1)
# sim2(51)
# sim2_multiplex(51)
# sim2_multiplex(51, strategy=2)