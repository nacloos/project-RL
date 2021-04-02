import numpy as np
import matplotlib.pyplot as plt

from snakes_and_ladders import SECURITY_DICE, NORMAL_DICE, RISKY_DICE
from value_iteration import markovDecision
from agent import ConstantAgent, OptimalAgent, RandomAgent
from simulation import estimate_cost

colors = ["#e07a5f","#3d405b","#f2cc8f", "#83bcff", "#81b29a"]

def plot_cost():
    layout = np.zeros(15)
    circle = False

    agents = [OptimalAgent(layout, circle), ConstantAgent(SECURITY_DICE), ConstantAgent(NORMAL_DICE),
              ConstantAgent(RISKY_DICE), RandomAgent([SECURITY_DICE, NORMAL_DICE, RISKY_DICE])]
    labels = ["Optimal", "Security dice", "Normal dice", "Risky dice", "Random"]
    costs = [estimate_cost(layout, circle, pi) for pi in agents]

    plt.figure(figsize=(6, 4), dpi=120)
    ax = plt.gca()

    # for s in range(len(costs[0])):
    #     C = [costs[i][s] for i in range(len(costs))]
    #     idx = np.argsort(C)[::-1]
    #     for i in idx:
    #         plt.bar(s+1, costs[i][s], color=(0,0,0,0), edgecolor=colors[i], lw=1.8, width=0.7, label=labels[i] if s==0 else "")
        
    states = np.arange(14)+1
    for i, C in enumerate(costs):
        plt.plot(states, C, marker="o", color=colors[i], lw=1.8, label=labels[i])


    plt.xlabel("States")
    plt.ylabel("Total expected cost")
    plt.legend()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False) 
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.show()


def plot_estimates():
    layout = np.zeros(15)
    circle = False

    pi = OptimalAgent(layout, circle)
    C_sim = estimate_cost(layout, circle, pi, n_episodes=200)

    C_th, _ = markovDecision(layout, circle)

    states = np.arange(14)+1
    plt.figure(figsize=(6, 4), dpi=120)
    ax = plt.gca()
    plt.plot(states, C_th, marker="o", label="Theory", color=colors[1])
    plt.plot(states, C_sim, marker="o", label="Simulation", color=colors[0])

    plt.xlabel("States")
    plt.ylabel("Total expected cost")
    plt.legend()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False) 
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.show()
    plt.show()



if __name__ == '__main__':
    # plot_cost()
    plot_estimates()
