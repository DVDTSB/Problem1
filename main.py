import networkx as nx
from sequences import *


def main():
    """
    This program generates a graph based on a given parameter type and sequence type.
    It then finds the connected components, number of edges, and possible lengths of cycles in the graph.
    """

    n = int(input("Length of V:"))

    print("a. P(x,y)=x+y")
    print("b. P(x,y)=x*y")

    prmtr_type = input("Type of the parameter:")

    if prmtr_type not in ["a", "b"]:
        print("Wrong type of the parameter")
        exit(1)

    P = lambda x, y: x + y if prmtr_type == "a" else x * y

    maxn = 2 * n if prmtr_type == "a" else n * n

    print("a. Arithmetic sequence")
    print("b. Geometric sequence")
    print("c. Fibonacci sequence")
    print("d. Recursive sequence")
    print("e. Primes sequence")
    print("f. Binomial coefficients")
    print("g. Semiprimes sequence")

    seq_type = input("Type of the sequence:")

    match seq_type:
        case "a":
            start = int(input("Start of the sequence:"))
            step = int(input("Step of the sequence:"))
            sequence = generate_arithmetic_sequence(maxn, start, step)
        case "b":
            start = int(input("Start of the sequence:"))
            factor = int(input("Factor of the sequence:"))
            sequence = generate_geometric_sequence(maxn, start, factor)
        case "c":
            sequence = generate_fibonacci_sequence(maxn)
        case "d":
            start1 = int(input("Start of the sequence:"))
            start2 = int(input("Start of the sequence:"))
            weight1 = int(input("Weight of the sequence:"))
            weight2 = int(input("Weight of the sequence:"))
            sequence = generate_recursive_sequence(
                maxn, start1, start2, weight1, weight2
            )
        case "e":
            sequence = generate_primes_sequence(maxn)
        case "f":
            sequence = generate_binomial_sequence(maxn)
        case "g":
            sequence = generate_semiprimes_sequence(maxn)
        case _:
            print("Wrong type of the sequence")
            exit(1)

    G = nx.Graph()
    G.add_nodes_from(range(1, n + 1))

    # connect two nodes x and y if P(x,y) is part of the sequence
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if P(i, j) in sequence:
                G.add_edge(i, j)

    print("Number of connected components: ", nx.number_connected_components(G))
    print("Number of edges: ", G.number_of_edges())

    import matplotlib.pyplot as plt

    nx.draw(G, with_labels=True, node_size=10, font_size=2, width=0.5)
    plt.show()
    plt.savefig("graph.svg")

    f = open("graph.txt", "w")

    for i in G.nodes:
        f.write(str(i) + " " + "\n")
    for i in G.edges:
        f.write(str(i[0]) + " " + str(i[1]) + "\n")

    f.close()

    calc_cycles = input("Calculate cycles (might take a long time)? (y/n):")

    if calc_cycles == "n":
        exit(0)

    import cycles

    cyc = cycles.find_all_cycles(G)

    lengths = [len(i) for i in cyc]
    # remove duplicates
    lengths = list(dict.fromkeys(lengths))
    lengths.sort()

    if len(lengths) == 0:
        print("No cycles found")
    else:
        print("Possible lengths of the cycles: ", end="")
        for i in lengths:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    main()
