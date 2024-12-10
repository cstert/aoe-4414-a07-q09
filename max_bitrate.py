# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
# Calculation for the maximum achievable bitrate

# Input:
#  tx_w: Transmitted power (W)
#  tx_gain_db: Transmitter gain (dB)
#  freq_hz: Transmission frequency (Hz)
#  dist_km: Separation vector magnitude (km)
#  rx_gain_db: Receiver gain (dB)
#  n0_j: Noise spectral density (W/Hz)
#  bw_hz: Channel bandwidth (Hz)
# Output:
#  Print r_max (maximum achievable bitrate)
#
# Written by Celia Sterthous
# Other contributors: None
#
# See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
c = 2.99792458e8 # speed of light (m/s)


if len(sys.argv) == 8:
     tx_w = float(sys.argv[1])
     tx_gain_db = float(sys.argv[2])
     freq_hz = float(sys.argv[3])
     dist_km = float(sys.argv[4])
     rx_gain_db = float(sys.argv[5])
     n0_j = float(sys.argv[6])
     bw_hz = float(sys.argv[7])

else:
   print(\
    'Usage: '\
    'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
   )
   exit()

# write script below this line

wavelength = c/freq_hz

L_a = 10**(0/10);
L_l = 10**(-1/10);

G_t = 10**(tx_gain_db/10)
G_r = 10**(rx_gain_db/10)

C = tx_w * L_l * G_t * (wavelength/(4*math.pi*(dist_km*1000)))**2 * L_a * G_r

N = n0_j * bw_hz
r_max = bw_hz * math.log((1 + C/N),2)

# print result
print(math.floor(r_max)) # bps (bits per second)