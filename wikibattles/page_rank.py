import argparse
import operator

from wikibattles.utils import parse


def rank(graph, iters):
    V = len(graph)
    d = 0.85
    ranks = dict()
    for k, _ in graph.nodes(data=True):
        ranks[k] = 1.0 / V

    for _ in range(iters):
        for key, node in graph.nodes(data=True):
            rank_sum = 0
            curr_rank = node.get('rank')
            neighbors = graph.out_edges(key)
            for neigh in neighbors:
                outlinks = len(graph.out_edges(neigh[1]))
                if outlinks > 0:
                    rank_sum += (1 / float(outlinks)) * ranks[neigh[1]]
            # actual page rank compution
            ranks[key] = ((1 - float(d)) * (1/float(V))) + d*rank_sum
    return ranks


def rank_by_file(filename, iters):
    graph = parse(filename)
    ranks = rank(graph, iters)
    return sorted(ranks.iteritems(), key=operator.itemgetter(1), reverse=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("--iters", default=10, type=int)
    args = parser.parse_args()
    sorted_r = rank_by_file(args.filename, args.iters)
    for tup in sorted_r:
        print '{0:30} :{1:10}'.format(str(tup[0]), tup[1])


if __name__ == '__main__':
    main()
