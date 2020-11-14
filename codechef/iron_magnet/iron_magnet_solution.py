from sys import stdin
IM = {'I','M'}

def clean(s,n) :
    i = 0
    j = n-1
    while i<n and s[i] not in IM :
        i+=1
    while j>=0 and s[j] not in IM :
        j-=1
    m_costs = []
    i_costs = []
    current = -1
    s = s[i:j+1]
    for ch in s :
        if ch in IM :
            current+=1
            if ch == 'M' :
                m_costs.append(current)
            else :
                i_costs.append(current)
        elif ch == '_' :
            current+=1
        else :
            current+=2
    return m_costs,i_costs

def counter(a,b,k) :
    i = 0
    counts = 0
    for cost in a :
        while i<len(b) :
            if k >= abs(cost-b[i]) :
                counts += 1
                i+=1
                break
            elif cost < b[i] :
                break
            else :
                i+=1
    return counts

for testcase in range(int(stdin.readline().strip())) :
    n,k = tuple(map(int,stdin.readline().split()))
    split_offs = stdin.readline().split('X')
    # I : Iron
    # M : Magnet
    # _ : Empty
    # : : Conductor
    # X : Blockage
    total = 0
    for piece in split_offs :
        magnets,irons = clean(piece,len(piece))
        # print(magnets,irons)
        m_num = len(magnets)
        i_num = len(irons)
        if i_num <= m_num :
            total += counter(irons,magnets,k)
        else :
            total += counter(magnets,irons,k)
    print(total)
