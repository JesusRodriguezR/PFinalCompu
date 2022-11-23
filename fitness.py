import numpy as np
def fitness(R):
    ip1 = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
    ip = np.array(ip1)
    t1  = [1.001e-7,2.50001e-2,1.000001e-1,2.250001e-1,4.000001e-1,6.250001e-1,9.000001e-1,1.225,1.467761,1.844197,2.070994]
    t = np.array(t1)
    dif = t-np.array(voltage(R,ip))
    
    dif2 = dif**2
    
    f = (1/11)*sum(dif2)
    f = 1/f
    
    #print(np.array(voltage(R,ip)))
    return f

def voltage(R,vgs):
    v = []
    b = 4.5e-6
    gamma = 0.01
    vds = 5
    vth = 0.69

    nd = (R[3]+1)/2
    resistor = 25*((R[2]*nd)+(nd-1)-((1/3)*(nd-1)*2))
    
    for vgsi in vgs:
        v.append((b/2)*(R[0]/R[1])*((vgsi-vth)**2)*(1 + gamma*vds)*resistor)
    return v