def gray2real(indiv):
    g0 = indiv[0:8]
    g1 = indiv[8:16]
    g2 = indiv[16:24]
    g3 = indiv[24:32]
    
    b0 = [g0[0]]
    b1 = [g1[0]]
    b2 = [g2[0]]
    b3 = [g3[0]]
    for i in range(7):
        b0.append(int(b0[i])^int(g0[i+1]))
        b1.append(int(b1[i])^int(g1[i+1]))
        b2.append(int(b2[i])^int(g2[i+1]))
        b3.append(int(b3[i])^int(g3[i+1]))
    r0 = 0
    r1 = 0
    r2 = 0
    r3 = 0
    for i in range(len(b0)):
        r0 += b0[i]*2**(7-i)
        r1 += b1[i]*2**(7-i)
        r2 += b2[i]*2**(7-i)
        r3 += b3[i]*2**(7-i)
        
    r0 = ((r0*4)/15)-2
    r1 = ((r1*4)/15)-2
    r2 = ((r2*4)/31)-2
    r3 = ((r3*4)/31)-2
    
    r0 = abs(r0)
    r1 = abs(r1)
    r2 = abs(r2)
    r3 = abs(r3)

    r0 = int(r0)*0.3+0.6
    r1 = int(r1)*0.3+0.6
    r2 = int(r2)
    if r2%2 == 0:
        r3 = r2+1
    else:
        r3 = r2
            
    R = [abs(r0),abs(r1),abs(r2),abs(r3)]
    
    return R