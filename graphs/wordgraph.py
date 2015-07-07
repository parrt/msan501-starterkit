def gml2adjlist(G):
    """
    Return a dict mapping word to adjacent nodes. G.node dict in memory
    looks like:

    {0: {'id': 0, 'value': 0, 'label': 'agreeable'},
    1: {'id': 1, 'value': 1, 'label': 'man'}, ... }

    and G.edge dict looks like:

    {0: {1: {}, 2: {}, 3: {}}, 1: {0: {}, 19: {}, 2: {}, 102: {}, ...}, ...}

    and we need:

    {agreeable:['man', 'old', 'person'], man:[['agreeable', 'best', 'old', ...], ...}
    """
    words = collections.OrderedDict()  # keep stuff in order read from GML
    ...
    return words
