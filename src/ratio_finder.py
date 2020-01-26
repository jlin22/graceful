from fractions import Fraction
def ratio(x, y):
    return str([('%.3f' % (x / y)), str(Fraction(x, y))]) + "\n"

fns = ['1-1-1', '2-1-1', '3-1-1', '4-1-1', '5-1-1', '6-1-1', '7-1-1', '8-1-1', 
        '9-1-1', '10-1-1', '11-1-1']
fns = list(map(lambda s: 'ratio_ends_lattice/'+s, fns))

# ratio_ends_lattice
pairs = [(12, 20), (12, 23), (12, 48), (44, 131), (92, 192), (152, 263),
        (384, 416), (992, 595), (2040, 824), (5424, 1059), (13764, 1320)]

for i in range(len(fns)):
    f = open(fns[i], 'w')
    f.write(ratio(pairs[i][0], pairs[i][1]))

