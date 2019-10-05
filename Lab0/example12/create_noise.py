# this module will be imported in the into your flowgraph
import cmath
import numpy as np

# When playing noise against a captured signal, it is often convenient
# to create the noise by specifying number of samples needed and sample
# rate of target signal.  The function createNoise() provides this.
#
# Mike Markowski, mike.ab3ap@gmail.com
# Feb 10, 2015

# cart2pol
#
# Convert arrays of cartesian coordinates to arrays of polar coordinates.

def cart2pol(x, y):
    rho = np.hypot(x, y)
    phi = np.arctan2(y, x)
    return phi, rho

# pol2cart
#
# Convert arrays of polar coordinates to arrays of cartesian coordinates.

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return x, y

# Generate a Gauusian noise waveform based on number of samples needed.
#
# Create white Gaussian noise.
# Using input properties, creates noise curve.
# Input: desired noise properties.
# Output: noise curve as described by intputs.
#
# Based on Matlab code by Vikas Singh.

def createNoise(centerFreq_Hz, bandwidth_Hz, sampleRate_Hz, numSamples):
    
    toneGap = float(bandwidth_Hz) / sampleRate_Hz # Gap between noise samples.
    
    # Make noise tones of magnitude 1 in freq domain, centered at 0 Hz:
    # 1 ---+          +---
    #      |          |
    # 0    +----------+
    
    halfBwSamples = int(toneGap * numSamples) / 2 # WHAT IF ODD????
    noiseTones = np.ones(numSamples)
    noiseTones[halfBwSamples : 1 + numSamples - halfBwSamples] = 0
    
    # Random phase noise, -pi to pi radians, for each noise tone.
    randomPhase = np.pi * (2 * np.random.rand(numSamples) - 1)
    
    # Convert polar mag/phase to Cartesian.
    x, y = pol2cart(noiseTones, randomPhase)
    c = np.vectorize(complex)(x, y)
    # Move to time domain.
    timeDomSig = np.fft.ifft(c)
    
    # Mix to user specified center frequency.
    if centerFreq_Hz != 0:
        t = np.arange(numSamples) / float(sampleRate_Hz)
        centerSig = np.cos(2 * np.pi * t * centerFreq_Hz)
        timeDomSig *= centerSig
    
    #   If IQ needed to feed to ARB, use following line
    #   IQdata = real(timeDomSig), imag(timeDomSig)
    #   return IQdata
    
    return timeDomSig
