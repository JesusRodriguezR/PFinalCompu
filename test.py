from matplotlib import pyplot as plt
import numpy as np
#Resistor voltage measured/simulated data
VR_data = [1.00E-07, 2.50E-02, 1.00E-01, 2.25E-01, 4.00E-01, 6.25E-01, \
            9.00E-01, 1.23E+00, 1.57E+00, 1.84E+00, 2.07E+00]
#gate-to-source voltage sweep  
VGS = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
#fixed parameters
VDS = 5         #drain-to-source voltage  
VT = 0.69       #treshold voltage (for silicon)
beta = 4.5e-6   #transistor's beta 
rsq = 25        #sheet resistance, ohms per square
#transistor variables
W = 15e-6        #gate width
L = 0.6e-6      #gate length
print('W: '+str(round(1e6*W,1))+'μm\t'+'L: '+str(round(1e6*L,1))+'μm')
#resistor
m = 12          #resistor squares per line
n = 13 
nd = (n+1)/2         #resistor lines
R = 25*((m*nd)+(nd-1)-((1/3)*(nd-1)*2))        # R(rsq, m, n)
print("R:", R, 'Ω')
#transistor's drain current I_D (for each V_GS value)
#resistor voltage V_R = I_D * R


VR = []
for i in range(len(VGS)):
    if VGS[i] <= VT:
        ID = 0.0
    else:
        ID = (beta/2)*(W/L)*((VGS[i]-VT)**2)*(1 + 0.01*VDS)
    VR.append(R*ID)
# mean square error
MSE = (1/len(VR_data))*(sum((np.array(VR_data)-np.array(VR))**2))
print("mean sq error: ", round(MSE, 7))
plt.figure(1)
plt.plot(VGS,VR_data)
plt.plot(VGS,VR)
plt.grid()
plt.legend(['data','calculated'])
plt.title('$V_R$ vs $V_{GS}$')
plt.ylabel('resistor voltage (V)')
plt.xlabel('gate-to-source voltage (V)')
plt.show()