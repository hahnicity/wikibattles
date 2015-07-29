import argparse
import operator

from wikibattles.utils import parse


def rank(graph, iters):
    V = len(graph)
    d = 0.85
    ranks = dict()
    for k, _ in graph.nodes(data=True):
        ranks[k] = 1.0 / V

    for _ in xrange(iters):
        tmp_ranks = ranks.copy()
        for key, node in graph.nodes(data=True):
            rank_sum = 0
            # In page rank the entry pi,pj is denoted > 0 if j links to i so look for all in edges to
            # a node i.
            neighbors = graph.in_edges(key)
            for neigh in neighbors:
                outlinks = len(graph.out_edges(neigh[0]))
                if outlinks > 0:
                    rank_sum += (1 / float(outlinks)) * ranks[neigh[0]]
            # actual page rank compution
            tmp_ranks[key] = ((1 - d) * (1.0 / V)) + d * rank_sum
        ranks = tmp_ranks
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
