# File: ptfun 
# Functions for gnuradio-companion PAM p(t) generation
from pylab import *
import numpy as np
def pampt(sps, ptype, pparms=[]):
    """ PAM pulse p(t) = p(n*TB/sps) generation
    >>>>> pt = pampt(sps, ptype, pparms) <<<<< 
    where sps: ptype: pulse type (’rect’, ’sinc’, ’tri’) 
    pparms not used for ’rect’, ’tri’ pparms = [k, beta] for sinc 
    k: "tail" truncation parameter for ’sinc’ 
    (truncates p(t) to -k*sps <= n < k*sps) 
    beta: Kaiser window parameter for ’sinc’ 
    pt: pulse p(t) at t=n*TB/sps 
    Note: In terms of sampling rate Fs and baud rate FB, 
    sps = Fs/FB 
    """
    ptype = ptype.lower() # Convert ptype to lowercase 
    # Set left/right limits for p(t) 
   
    if (ptype=='rect'):
        kL = -0.5; kR = -kL 
    elif(ptype=='tri'):
        kL = -1.0; kR = -kL
    elif(ptype=='man'):
        kL = -0.5; kR = -kL
    else: 
        kL = -pparms[0]; kR = -kL # Default left/right limits 
    ixpL = np.ceil(kL*sps) # Left index for p(t) time axis 
    ixpR = np.ceil(kR*sps) # Right index for p(t) time axis 
    ttp = arange(ixpL,ixpR) # Time axis for p(t) 
    pt = zeros(len(ttp)) # Initialize pulse p(t) 
    if (ptype=='rect'): # Rectangular p(t) 
        ix = where(logical_and(ttp>=kL*sps, ttp<kR*sps))[0] 
        pt[ix] = ones(len(ix)) 
    elif (ptype=='tri') :
        pt = zeros(len(ttp))
        ixtn = where(logical_and(ttp>=kL*sps, ttp<0*sps))[0]
        pt[ixtn] = 1+(ttp[ixtn]/sps)
        ixtp = where(logical_and(ttp>=0*sps, ttp<kR*sps))[0]
        pt[ixtp] = 1-(ttp[ixtp]/sps)
    
       
    elif (ptype=='sinc') :
        ixsc = where(logical_and(ttp>=kL*sps,ttp<kR*sps))[0]
        ixnz = where(mod(ttp,sps)!=0)[0]
        pt[int(len(ixsc)/2)] = 1     # At exception t=0, assign value of sinc directly at t =0 point
        pt[ixnz] = sin(pi*ttp[ixnz]/sps)/(pi*ttp[ixnz]/sps)
        pt = pt * kaiser(len(pt),pparms[1])
    
    elif (ptype=='man') :
        ixmn = where(logical_and(ttp>=kL*sps, ttp<0*sps))[0]     # taking negative half of time period
        pt[ixmn] = -ones(len(ixmn)) 
        ixmp = where(logical_and(ttp>=0*sps, ttp<kR*sps))[0]      # taking positive half of time period
        pt[ixmp] = ones(len(ixmp))  
        #ast = ast- 0.5
        
    elif (ptype=='rcf') :
        pt = zeros(len(ttp))
        for i in range(len(ttp)):
            if ttp[i]==0:
                pt[i]=1
            elif((ttp[i]==(sps/2*pparms[1])) or (ttp[i]==(-1*sps/2*pparms[1])) or (((2*pparms[1]*ttp[i])/sps)**2==1) or (pparms[1]==(sps/2*ttp[i])) or (pparms[1]==(-1*sps/2*ttp[i]))):
                pt[i]=(sin(pi*ttp[i]/sps)/(pi*ttp[i]/sps))*pi/4
                
            else:
                pt[i]= ((sin((pi*ttp[i])/sps)/(pi*ttp[i]/sps))*(cos((pi*pparms[1]*ttp[i])/(sps))/(1-(2*pparms[1]*ttp[i]/sps)**2)))
         
    return pt



# In[ ]: