import itertools

def execute():
    A = {1, 2, 'ee', 'a', 'd'}
    B = {1, 'd', 'tt', 4, 3}
    U = {1, 2, 3, 4, 'a', 'b', 'c', 'd', 'ee', 'tt', 'ww'}
    print(' A = ', A, '\n', 'B = ', B, '\n', 'U = ', U)
    print("а) C=A∪B ", A.union(B))
    print("б) C=A∩B ", A.intersection(B))
    print("в) C=A\B  ", A.difference(B))
    print("г) C=B\A", B.difference(A))
    print("д) А+В", A.symmetric_difference(B))
    print("е) С=А' ", U.difference(A))
    print("э) С=В' ", U.difference(B))
    print("ж) C=A×B")
    res = ((x, y) for x, y in itertools.product(A, B))
    for p in res:
        print(p, end=",")
    else:
        print()
    print("з) C=B×A ")
    res_2 = ((x, y) for x, y in itertools.product(B, A))
    for p in res_2:
        print(p, end=",")
    else:
        print()

    print('и) C = ((A∪B)∩(A\B)) =', (A.union(B)).intersection(A.difference(B)))
