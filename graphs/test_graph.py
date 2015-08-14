from graph import *
import sys


def test1():
    gr = \
    """a: b, c
    b: c, d
    c: b
    d: c
    """
    print "Test #1:"
    print gr

    al = adjlist(gr)
    am = adjmatrix(al)
    nl = ['a','b','c','d']
    reach = {}
    for n in nl:
        reach[n] = nodes(al, n)

    #print al
    assert set(al['a']) == {'b','c'}
    assert set(al['b']) == {'c','d'}
    assert set(al['c']) == {'b'}
    assert set(al['d']) == {'c'}
    #print am
    assert str(am), "[[0, 1, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0]]"

    #print reach
    # use a set to check equality to ignore order
    assert set(reach['a']) == {'a','b','c','d'}
    assert set(reach['b']) == {'b','c','d'}
    assert set(reach['c']) == {'b','c','d'}
    assert set(reach['d']) == {'b','c','d'}

def test2():
    gr = \
    """Paul: Jenny
    Jenny: Marcelo
    Marcelo: Chris, Eileen, Pamela
    Chris: Terence
    Eileen: Paul
    Pamela: Paul
    Terence: Paul

    """

    print "Test #2:"
    print gr

    al = adjlist(gr)
    am = adjmatrix(al)
    nl = ['Paul', 'Jenny', 'Marcelo', 'Chris', 'Eileen', 'Pamela', 'Terence']
    reach = {}
    for n in nl:
        reach[n] = nodes(al, n)

    #print al
    assert set(al['Paul']) == {'Jenny'}
    assert set(al['Jenny']) == {'Marcelo'}
    assert set(al['Marcelo']) == {'Chris', 'Eileen', 'Pamela'}
    assert set(al['Eileen']) == {'Paul'}
    assert set(al['Pamela']) == {'Paul'}
    assert set(al['Terence']) == {'Paul'}
    
    #print am
    assert str(am), "[[0, 1, 0, 0, 0, 0, 0],"+\
                          " [0, 0, 1, 0, 0, 0, 0],"+\
                          " [0, 0, 0, 1, 1, 1, 0],"+\
                          " [0, 0, 0, 0, 0, 0, 1],"+\
                          " [1, 0, 0, 0, 0, 0, 0],"+\
                          " [1, 0, 0, 0, 0, 0, 0],"+\
                          " [1, 0, 0, 0, 0, 0, 0]]"

    #print reach
    # use a set to check equality to ignore order
    assert set(reach['Paul']) == {'Paul', 'Jenny', 'Marcelo', 'Chris', 'Eileen', 'Pamela', 'Terence'}
    assert set(reach['Jenny']) == {'Paul', 'Jenny', 'Marcelo', 'Chris', 'Eileen', 'Pamela', 'Terence'}
    assert set(reach['Marcelo']) == {'Paul', 'Jenny', 'Marcelo', 'Chris', 'Eileen', 'Pamela', 'Terence'}
    assert set(reach['Eileen']) == {'Paul', 'Jenny', 'Marcelo', 'Chris', 'Eileen', 'Pamela', 'Terence'}
    assert set(reach['Pamela']) == {'Paul', 'Jenny', 'Marcelo', 'Chris', 'Eileen', 'Pamela', 'Terence'}
    assert set(reach['Terence']) == {'Paul', 'Jenny', 'Marcelo', 'Chris', 'Eileen', 'Pamela', 'Terence'}
