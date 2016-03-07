#!/usr/bin/env python

"""
tools.py

Contains helper functions that manipulate input files and connect analysis code
 and user interface code.


"""
# import sys
import networkx as nx


def read_mir_target_sif(sif_f):
    with open(sif_f, 'rb') as handle:
        lines = handle.read().splitlines()
    edges = [x.split() for x in lines]
    edges_data = ["%s %s %s" % (x[0], x[2], x[1]) for x in edges]

    g = nx.parse_edgelist(edges_data, nodetype=str, data=(('strand', float),))
    return g
