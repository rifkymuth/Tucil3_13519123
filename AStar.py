import matplotlib.pyplot as plt
import networkx as nx
import math


def h(N, a, b):
    return (math.sqrt(math.pow((N[a][0] - N[b][0]), 2) + math.pow((N[a][1] - N[b][1]), 2)))


def g(N, route, a):
    cost = 0.0
    for i in range(len(route)-1):
        cost += h(N, route[i], route[i+1])
    cost += h(N, route[-1], a)
    return cost


def AStar(G, start, goal):
    result = []
    nodes = nx.get_node_attributes(G, 'pos')
    f = h(nodes, start, goal)
    stack = [[start, f]]
    BFS(G, goal, stack, result, nodes)
    return result


def BFS(G, goal, stack, result, nodes):
    if (stack and checkSmallerThanResult(stack, result)):
        currRoute = stack.pop(0)
        route_list = currRoute[0].split("-")
        route_cost = currRoute[1]
        if (route_list[-1] == goal):
            if (not result):
                result.append(currRoute)
            elif (route_cost < result[0][1]):
                result.clear()
                result.append(currRoute)
        else:
            for node in G[route_list[-1]]:
                if (node in [route_list]):
                    continue
                else:
                    f = g(nodes, route_list, node) + h(nodes, node, goal)
                    route_list.append(node)
                    stack.append(["-".join(route_list), f])
                    route_list.pop()
            stack.sort(key=lambda item: item[1])
            BFS(G, goal, stack, result, nodes)


def checkSmallerThanResult(stack, result):
    if (not result):
        return True
    else:
        for item in stack:
            if item[1] < result[0][1]:
                return True
        return False
