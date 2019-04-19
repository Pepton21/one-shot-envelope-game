# The Multiplex One-shot Envelope Game
The code in this repository contains a **simulation** of the **one-shot envelope game**, as described in the work of **Christian Hilbe**, **Moshe Hoffman** and **Martin A. Nowak** in their article *"Cooperate without Looking in a Non-Repeated Game"* [1]. The code **reproduces** their results and **extends** the simulation to a **multiplex network**. In addition, the simulation is extended to a multiplex network, providing a **framework** for future experimentation and observing different outcomes of the game for different game parameters.

## Simulating the Nash equilibria in a single layer network
According to [1], the one-shot envelope game has the following **Nash equilibria**:
1. Player 1 **looks**, Player 2 **continues** the game and Player 1 **cooperates** if **defection temptation is low** (**ONLYL**)
2. Player one **does not look**, Player 2 **continues** the game and Player 1 **always cooperates** (**CWOL**)
3. Player 2 **always ends** the game, no matter if player 1 looks or not (**EXIT**)

Reproducing the simulations from [1] with this framework yields the following results:

<p align="center">
<img src="https://github.com/Pepton21/one-shot-envelope-game/blob/master/images/RR_Graph_labeled.png" width="950" alt="RR">
</p>

<p align="center">
<img src="https://github.com/Pepton21/one-shot-envelope-game/blob/master/images/BA_graph_labeled.png" width="950" alt="BA">
</p>

The results are **in-line** with the **theoretical descriptions** of the Nash equilibria. The equilibrium states can be shown even more clearly by plotting a **density matrix** for different game parameters of the one-shot envelope game:

<p align="center">
<img src="https://github.com/Pepton21/one-shot-envelope-game/blob/master/images/frequency_heatmaps.png" width="1200" alt="heatmaps">
</p>

## Extending the game to a multiplex network
The **code** provides the option to run the simulations on a **multiplex network**, where players are allowed to have **different neighbors** and have **different strategies**. In addition, the **game parameters** in each layer may also be **different**. If we repeat the simulation, with the same game parameters in all layers and follow the multiplex **simulation strategy** defined by **Battiston et al.** [2], the following heat maps for the **looking**, **exit** and **cooperation frequencies** are obtained:

<p align="center">
<img src="https://github.com/Pepton21/one-shot-envelope-game/blob/master/images/multiplex_looking.png" width="1200" alt="multiplex_looking">
</p>

<p align="center">
<img src="https://github.com/Pepton21/one-shot-envelope-game/blob/master/images/multiplex_exits.png" width="1200" alt="multiplex_exits">
</p>

<p align="center">
<img src="https://github.com/Pepton21/one-shot-envelope-game/blob/master/images/multiplex_coops.png" width="1200" alt="multiplex_coops">
</p>

We can also plot the **contingency table** for the amount of **unique strategies across layers** players have, before and after they have had the chance to **play** with other players and **copy** their strategies:

<p align="center">
<img src="https://github.com/Pepton21/one-shot-envelope-game/blob/master/images/strat_changes_player1.png" width="1200" alt="player1">
</p>

<p align="center">
<img src="https://github.com/Pepton21/one-shot-envelope-game/blob/master/images/strat_changes_player2.png" width="1200" alt="player2">
</p>

## References
1. C. Hilbe, M. Hoffman, and M. Nowak, "Cooperate without looking in a non-repeated game," Games, vol. 6,no. 4, pp. 458–472, 2015. (https://www.mdpi.com/2073-4336/6/4/458)
2. F. Battiston, M. Perc, and V. Latora, "Determinants of public cooperation in multiplex networks," New Journalof Physics, vol. 19, no. 7, p. 073017, 2017. (https://iopscience.iop.org/article/10.1088/1367-2630/aa6ea1/meta)
