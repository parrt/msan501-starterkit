from graph import *
import sys

def assertequals(result, expecting):
	if result != expecting:
		sys.stderr.write("Failure: expecting %s found %s\n" % (expecting, result))

# TEST 1

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
assertequals(set(al['a']), {'b','c'})
assertequals(set(al['b']), {'c','d'})
assertequals(set(al['c']), {'b'})
assertequals(set(al['d']), {'c'})
#print am
assertequals(str(am), "[[0, 1, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0]]")

#print reach
# use a set to check equality to ignore order
assertequals(set(reach['a']), {'a','b','c','d'})
assertequals(set(reach['b']), {'b','c','d'})
assertequals(set(reach['c']), {'b','c','d'})
assertequals(set(reach['d']), {'b','c','d'})

# TEST 2

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
assertequals(set(al['Paul']), {'Jenny'})
assertequals(set(al['Jenny']), {'Marcelo'})
assertequals(set(al['Marcelo']), {'Chris', 'Eileen', 'Pamela'})
assertequals(set(al['Eileen']), {'Paul'})
assertequals(set(al['Pamela']), {'Paul'})
assertequals(set(al['Terence']), {'Paul'})

#print am
assertequals(str(am), "[[0, 1, 0, 0, 0, 0, 0],"+\
					  " [0, 0, 1, 0, 0, 0, 0],"+\
					  " [0, 0, 0, 1, 1, 1, 0],"+\
					  " [0, 0, 0, 0, 0, 0, 1],"+\
					  " [1, 0, 0, 0, 0, 0, 0],"+\
					  " [1, 0, 0, 0, 0, 0, 0],"+\
					  " [1, 0, 0, 0, 0, 0, 0]]")

#print reach
# use a set to check equality to ignore order
assertequals(set(reach['Paul']), {'Paul', 'Jenny', 'Marcelo', 'Chris', 'Eileen', 'Pamela', 'Terence'})
assertequals(set(reach['Jenny']), {'Paul', 'Jenny', 'Marcelo', 'Chris', 'Eileen', 'Pamela', 'Terence'})
assertequals(set(reach['Marcelo']), {'Paul', 'Jenny', 'Marcelo', 'Chris', 'Eileen', 'Pamela', 'Terence'})
assertequals(set(reach['Eileen']), {'Paul', 'Jenny', 'Marcelo', 'Chris', 'Eileen', 'Pamela', 'Terence'})
assertequals(set(reach['Pamela']), {'Paul', 'Jenny', 'Marcelo', 'Chris', 'Eileen', 'Pamela', 'Terence'})
assertequals(set(reach['Terence']), {'Paul', 'Jenny', 'Marcelo', 'Chris', 'Eileen', 'Pamela', 'Terence'})

print "All tests pass"