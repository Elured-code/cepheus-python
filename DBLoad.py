from tinydb import TinyDB, Query


db = TinyDB('db.json')
db.truncate()

# Bright Supergiants (Luminositu Class I / Ia)
# Load Blue-Tinted White

db.insert({'type': 'O0 I', 'lum': 2150000, 'mass': 130, 'diameter': 0.218, 'roche limit': 1.528, 'H-': 1101, 'H': 1324, 'H+': 2588, 'Frost Line': -1, 'Limit': 7150})
db.insert({'type': 'O1 I', 'lum': 2020000, 'mass': 125, 'diameter': 0.211, 'roche limit': 1.469, 'H-': 987, 'H': 1188, 'H+': 2322, 'Frost Line': -1, 'Limit': 6875})
db.insert({'type': 'O2 I', 'lum': 1890000, 'mass': 121, 'diameter': 0.207, 'roche limit': 1.422, 'H-': 926, 'H': 1114, 'H+': 2177, 'Frost Line': -1, 'Limit': 6655})
db.insert({'type': 'O3 I', 'lum': 1760000, 'mass': 117, 'diameter': 0.204, 'roche limit': 1.375, 'H-': 826, 'H': 994, 'H+': 1942, 'Frost Line': -1, 'Limit': 6435})
db.insert({'type': 'O4 I', 'lum': 1630000, 'mass': 113, 'diameter': 0.200, 'roche limit': 1.328, 'H-': 736, 'H': 886, 'H+': 1730, 'Frost Line': -1, 'Limit': 6215})
db.insert({'type': 'O5 I', 'lum': 1500000, 'mass': 109, 'diameter': 0.196, 'roche limit': 1.281, 'H-': 654, 'H': 787, 'H+': 1538, 'Frost Line': -1, 'Limit': 5995})
db.insert({'type': 'O6 Ia', 'lum': 1360000, 'mass': 90, 'diameter': 0.186, 'roche limit': 1.058, 'H-': 875, 'H': 1171, 'H+': 2059, 'Frost Line': -1, 'Limit': 4950})
db.insert({'type': 'O7 Ia', 'lum': 1120000, 'mass': 75, 'diameter': 0.200, 'roche limit': 0.882, 'H-': 795, 'H': 1040, 'H+': 1774, 'Frost Line': -1, 'Limit': 4125})
db.insert({'type': 'O8 Ia', 'lum': 913000, 'mass': 65, 'diameter': 0.214, 'roche limit': 0.764, 'H-': 717, 'H': 960, 'H+': 1687, 'Frost Line': -1, 'Limit': 3575})
db.insert({'type': 'O9 Ia', 'lum': 731000, 'mass': 55, 'diameter': 0.228, 'roche limit': 0.647, 'H-': 642, 'H': 859, 'H+': 1510, 'Frost Line': -1, 'Limit': 3025})

# Main Sequence Stars (Luminosity Class V)

# Blue-White

db.insert({'type': 'A0 V', 'lum': 90, 'mass': 3.5, 'diameter': 0.0149, 'roche limit': 0.0412, 'H-': 7.2, 'H': 9.6, 'H+': 17, 'Frost Line': 46, 'Limit': 175})
db.insert({'type': 'A1 V', 'lum': 75.2, 'mass': 3.22, 'diameter': 0.0136, 'roche limit': 0.0379, 'H-': 6.6, 'H': 8.4, 'H+': 16, 'Frost Line': 42, 'Limit': 161})
db.insert({'type': 'A2 V', 'lum': 60.4, 'mass': 2.94, 'diameter': 0.0123, 'roche limit': 0.0346, 'H-': 5.9, 'H': 7.9, 'H+': 14, 'Frost Line': 37.7, 'Limit': 147})
db.insert({'type': 'A3 V', 'lum': 45.6, 'mass': 2.66, 'diameter': 0.011, 'roche limit': 0.0313, 'H-': 5.1, 'H': 6.9, 'H+': 12, 'Frost Line': 32.8, 'Limit': 133})
db.insert({'type': 'A4 V', 'lum': 30.8, 'mass': 2.38, 'diameter': 0.0097, 'roche limit': 0.028, 'H-': 4.2, 'H': 5.6, 'H+': 9.8, 'Frost Line': 27.0, 'Limit': 119})
db.insert({'type': 'A5 V', 'lum': 16, 'mass': 2.1, 'diameter': 0.0084, 'roche limit': 0.0247, 'H-': 3.1, 'H': 4.1, 'H+': 7.1, 'Frost Line': 19.4, 'Limit': 105})
db.insert({'type': 'A6 V', 'lum': 14.42, 'mass': 2.02, 'diameter': 0.0083, 'roche limit': 0.0238, 'H-': 2.9, 'H': 3.9, 'H+': 6.7, 'Frost Line': 18.5, 'Limit': 101})
db.insert({'type': 'A7 V', 'lum': 12.84, 'mass': 1.94, 'diameter': 0.0082, 'roche limit': 0.0228, 'H-': 2.7, 'H': 3.7, 'H+': 6.4, 'Frost Line': 17.5, 'Limit': 97})
db.insert({'type': 'A8 V', 'lum': 11.26, 'mass': 1.86, 'diameter': 0.0081, 'roche limit': 0.0219, 'H-': 2.6, 'H': 3.5, 'H+': 6.0, 'Frost Line': 16.3, 'Limit': 93})
db.insert({'type': 'A9 V', 'lum': 9.68, 'mass': 1.78, 'diameter': 0.0080, 'roche limit': 0.021, 'H-': 2.4, 'H': 3.2, 'H+': 5.5, 'Frost Line': 15.1, 'Limit': 89})

# White

db.insert({'type': 'F0 V', 'lum': 8.1, 'mass': 1.7, 'diameter': 0.0079, 'roche limit': 0.0200, 'H-': 2.2, 'H': 2.9, 'H+': 5.1, 'Frost Line': 13.8, 'Limit': 68})
db.insert({'type': 'F1 V', 'lum': 7.18, 'mass': 1.62, 'diameter': 0.0077, 'roche limit': 0.0191, 'H-': 2.1, 'H': 2.8, 'H+': 4.8, 'Frost Line': 13.0, 'Limit': 65})
db.insert({'type': 'F2 V', 'lum': 6.26, 'mass': 1.54, 'diameter': 0.0074, 'roche limit': 0.0181, 'H-': 1.9, 'H': 2.6, 'H+': 4.5, 'Frost Line': 12.14, 'Limit': 62})
db.insert({'type': 'F3 V', 'lum': 5.34, 'mass': 1.46, 'diameter': 0.0071, 'roche limit': 0.0172, 'H-': 1.8, 'H': 2.4, 'H+': 4.1, 'Frost Line': 11.21, 'Limit': 59})
db.insert({'type': 'F4 V', 'lum': 4.42, 'mass': 1.38, 'diameter': 0.0068, 'roche limit': 0.0163, 'H-': 1.6, 'H': 2.2, 'H+': 3.8, 'Frost Line': 10.2, 'Limit': 56})
db.insert({'type': 'F5 V', 'lum': 3.5, 'mass': 1.3, 'diameter': 0.0066, 'roche limit': 0.0153, 'H-': 1.5, 'H': 2.0, 'H+': 3.3, 'Frost Line': 9.08, 'Limit': 59})
db.insert({'type': 'F6 V', 'lum': 3.042, 'mass': 1.248, 'diameter': 0.0062, 'roche limit': 0.0147, 'H-': 1.4, 'H': 1.9, 'H+': 3.1, 'Frost Line': 8.46, 'Limit': 50})
db.insert({'type': 'F7 V', 'lum': 2.584, 'mass': 1.196, 'diameter': 0.0059, 'roche limit': 0.0141, 'H-': 1.3, 'H': 1.7, 'H+': 3.1, 'Frost Line': 7.80, 'Limit': 48})
db.insert({'type': 'F8 V', 'lum': 2.126, 'mass': 1.144, 'diameter': 0.0055, 'roche limit': 0.0135, 'H-': 1.1, 'H': 1.5, 'H+': 2.6, 'Frost Line': 7.08, 'Limit': 46})
db.insert({'type': 'F9 V', 'lum': 1.668, 'mass': 1.092, 'diameter': 0.0052, 'roche limit': 0.0129, 'H-': 1.0, 'H': 1.4, 'H+': 2.3, 'Frost Line': 6.27, 'Limit': 44})

# Yellow

db.insert({'type': 'G0 V', 'lum': 1.21, 'mass': 1.040, 'diameter': 0.0048, 'roche limit': 0.0123, 'H-': 0.83, 'H': 1.10, 'H+': 1.95, 'Frost Line': 5.34, 'Limit': 52})
db.insert({'type': 'G1 V', 'lum': 1.102, 'mass': 1.020, 'diameter': 0.0048, 'roche limit': 0.0120, 'H-': 0.79, 'H': 1.05, 'H+': 1.86, 'Frost Line': 5.10, 'Limit': 51})
db.insert({'type': 'G2 V', 'lum': 0.994, 'mass': 1, 'diameter': 0.0047, 'roche limit': 0.0118, 'H-': 0.75, 'H': 1, 'H+': 1.76, 'Frost Line': 4.84, 'Limit': 50})
db.insert({'type': 'G3 V', 'lum': 0.886, 'mass': 0.98, 'diameter': 0.0045, 'roche limit': 0.0116, 'H-': 0.71, 'H': 0.95, 'H+': 1.67, 'Frost Line': 4.57, 'Limit': 49})
db.insert({'type': 'G4 V', 'lum': 0.778, 'mass': 0.96, 'diameter': 0.0044, 'roche limit': 0.0113, 'H-': 0.67, 'H': 0.90, 'H+': 1.58, 'Frost Line': 4.28, 'Limit': 48})
db.insert({'type': 'G5 V', 'lum': 0.67, 'mass': 0.94, 'diameter': 0.0043, 'roche limit': 0.0111, 'H-': 0.62, 'H': 0.84, 'H+': 1.45, 'Frost Line': 3.97, 'Limit': 47})
db.insert({'type': 'G6 V', 'lum': 0.62, 'mass': 0.917, 'diameter': 0.0043, 'roche limit': 0.0108, 'H-': 0.59, 'H': 0.79, 'H+': 1.39, 'Frost Line': 3.82, 'Limit': 46})
db.insert({'type': 'G7 V', 'lum': 0.57, 'mass': 0.894, 'diameter': 0.0043, 'roche limit': 0.0106, 'H-': 0.57, 'H': 0.76, 'H+': 1.34, 'Frost Line': 3.67, 'Limit': 45})
db.insert({'type': 'G8 V', 'lum': 0.52, 'mass': 0.871, 'diameter': 0.0043, 'roche limit': 0.0103, 'H-': 0.54, 'H': 0.73, 'H+': 1.28, 'Frost Line': 3.50, 'Limit': 44})
db.insert({'type': 'G9 V', 'lum': 0.47, 'mass': 0.848, 'diameter': 0.0043, 'roche limit': 0.0100, 'H-': 0.52, 'H': 0.7, 'H+': 1.21, 'Frost Line': 3.33, 'Limit': 43})

# Orange

db.insert({'type': 'K0 V', 'lum': 0.420, 'mass': 0.825, 'diameter': 0.0043, 'roche limit': 0.0097, 'H-': 0.49, 'H': 0.66, 'H+': 1.15, 'Frost Line': 3.15, 'Limit': 42})
db.insert({'type': 'K1 V', 'lum': 0.352, 'mass': 0.774, 'diameter': 0.0039, 'roche limit': 0.0091, 'H-': 0.45, 'H': 0.6, 'H+': 1.05, 'Frost Line': 2.88, 'Limit': 39})
db.insert({'type': 'K2 V', 'lum': 0.284, 'mass': 0.723, 'diameter': 0.0036, 'roche limit': 0.0085, 'H-': 0.4, 'H': 0.54, 'H+': 0.95, 'Frost Line': 2.59, 'Limit': 36})
db.insert({'type': 'K3 V', 'lum': 0.216, 'mass': 0.672, 'diameter': 0.0033, 'roche limit': 0.0079, 'H-': 0.36, 'H': 0.47, 'H+': 0.82, 'Frost Line': 2.26, 'Limit': 34})
db.insert({'type': 'K4 V', 'lum': 0.148, 'mass': 0.621, 'diameter': 0.003, 'roche limit': 0.0073, 'H-': 0.29, 'H': 0.39, 'H+': 0.68, 'Frost Line': 1.87, 'Limit': 31})
db.insert({'type': 'K5 V', 'lum': 0.08, 'mass': 0.57, 'diameter': 0.0027, 'roche limit': 0.0069, 'H-': 0.21, 'H': 0.29, 'H+': 0.5, 'Frost Line': 1.38, 'Limit': 29})
db.insert({'type': 'K6 V', 'lum': 0.072, 'mass': 0.558, 'diameter': 0.0027, 'roche limit': 0.0066, 'H-': 0.20, 'H': 0.27, 'H+': 0.48, 'Frost Line': 1.31, 'Limit': 28})
db.insert({'type': 'K7 V', 'lum': 0.064, 'mass': 0.537, 'diameter': 0.0026, 'roche limit': 0.0063, 'H-': 0.19, 'H': 0.26, 'H+': 0.45, 'Frost Line': 1.23, 'Limit': 27})
db.insert({'type': 'K8 V', 'lum': 0.056, 'mass': 0.522, 'diameter': 0.0026, 'roche limit': 0.0062, 'H-': 0.18, 'H': 0.24, 'H+': 0.42, 'Frost Line': 1.15, 'Limit': 26})
db.insert({'type': 'K9 V', 'lum': 0.048, 'mass': 0.506, 'diameter': 0.0026, 'roche limit': 0.0060, 'H-': 0.17, 'H': 0.23, 'H+': 0.39, 'Frost Line': 1.07, 'Limit': 25})

# Red

db.insert({'type': 'M0 V', 'lum': 0.040, 'mass': 0.489, 'diameter': 0.0058, 'roche limit': 0.0058, 'H-': 0.15, 'H': 0.21, 'H+': 0.36, 'Frost Line': 0.97, 'Limit': 24})
db.insert({'type': 'M1 V', 'lum': 0.034, 'mass': 0.458, 'diameter': 0.0054, 'roche limit': 0.0054, 'H-': 0.14, 'H': 0.18, 'H+': 0.32, 'Frost Line': 0.895, 'Limit': 23})
db.insert({'type': 'M2 V', 'lum': 0.027, 'mass': 0.426, 'diameter': 0.0051, 'roche limit': 0.0051, 'H-': 0.13, 'H': 0.15, 'H+': 0.28, 'Frost Line': 0.797, 'Limit': 21})
db.insert({'type': 'M3 V', 'lum': 0.021, 'mass': 0.395, 'diameter': 0.0047, 'roche limit': 0.0047, 'H-': 0.11, 'H': 0.13, 'H+': 0.24, 'Frost Line': 0.703, 'Limit': 19})
db.insert({'type': 'M4 V', 'lum': 0.012, 'mass': 0.363, 'diameter': 0.0043, 'roche limit': 0.0043, 'H-': 0.09, 'H': 0.11, 'H+': 0.20, 'Frost Line': 0.532, 'Limit': 16})
db.insert({'type': 'M5 V', 'lum': 0.007, 'mass': 0.331, 'diameter': 0.0039, 'roche limit': 0.0039, 'H-': 0.07, 'H': 0.09, 'H+': 0.16, 'Frost Line': 0.406, 'Limit': 15})
db.insert({'type': 'M6 V', 'lum': 0.006, 'mass': 0.302, 'diameter': 0.0036, 'roche limit': 0.0036, 'H-': 0.05, 'H': 0.07, 'H+': 0.12, 'Frost Line': 0.376, 'Limit': 14})
db.insert({'type': 'M7 V', 'lum': 0.004, 'mass': 0.273, 'diameter': 0.0032, 'roche limit': 0.0032, 'H-': 0.04, 'H': 0.05, 'H+': 0.09, 'Frost Line': 0.307, 'Limit': 13})
db.insert({'type': 'M8 V', 'lum': 0.003, 'mass': 0.244, 'diameter': 0.0029, 'roche limit': 0.0029, 'H-': 0.03, 'H': 0.04, 'H+': 0.07, 'Frost Line': 0.266, 'Limit': 12})
db.insert({'type': 'M9 V', 'lum': 0.001, 'mass': 0.215, 'diameter': 0.0026, 'roche limit': 0.0026, 'H-': 0.02, 'H': 0.03, 'H+': 0.06, 'Frost Line': 0.154, 'Limit': 11})

# Dwarf Stars

db.insert({'type': 'D0', 'lum': 0.046, 'mass': 1.4, 'diameter': 0.0017, 'roche limit': 0.0165, 'H-': 0.161, 'H': 0.216, 'H+': 0.379, 'Frost Line': 1.042, 'Limit': 70})
db.insert({'type': 'D1', 'lum': 0.0265, 'mass': 1.1, 'diameter': 0.0016, 'roche limit': 0.013, 'H-': 0.122, 'H': 0.164, 'H+': 0.287, 'Frost Line': 0.789, 'Limit': 55})
db.insert({'type': 'D2', 'lum': 0.0165, 'mass': 0.986, 'diameter': 0.0015, 'roche limit': 0.0116, 'H-': 0.096, 'H': 0.129, 'H+': 0.227, 'Frost Line': 0.623, 'Limit': 50})
db.insert({'type': 'D3', 'lum': 0.006, 'mass': 0.872, 'diameter': 0.0014, 'roche limit': 0.0103, 'H-': 0.058, 'H': 0.078, 'H+': 0.137, 'Frost Line': 0.376, 'Limit': 44})
db.insert({'type': 'D4', 'lum': 0.0018, 'mass': 0.758, 'diameter': 0.0013, 'roche limit': 0.009, 'H-': 0.032, 'H': 0.042, 'H+': 0.071, 'Frost Line': 0.206, 'Limit': 38})
db.insert({'type': 'D5', 'lum': 0.0007, 'mass': 0.643, 'diameter': 0.0012, 'roche limit': 0.0076, 'H-': 0.02, 'H': 0.027, 'H+': 0.047, 'Frost Line': 0.129, 'Limit': 33})
db.insert({'type': 'D6', 'lum': 0.0005, 'mass': 0.529, 'diameter': 0.0011, 'roche limit': 0.0063, 'H-': 0.017, 'H': 0.023, 'H+': 0.039, 'Frost Line': 0.109, 'Limit': 27})
db.insert({'type': 'D7', 'lum': 0.0004, 'mass': 0.42, 'diameter': 0.0009, 'roche limit': 0.05, 'H-': 0.015, 'H': 0.02, 'H+': 0.035, 'Frost Line': 0.097, 'Limit': 21})
db.insert({'type': 'D8', 'lum': 0.0003, 'mass': 0.3, 'diameter': 0.0007, 'roche limit': 0.0036, 'H-': 0.013, 'H': 0.019, 'H+': 0.029, 'Frost Line': 0.084, 'Limit': 15})
db.insert({'type': 'D9', 'lum': 0.0002, 'mass': 0.15, 'diameter': 0.0006, 'roche limit': 0.0018, 'H-': 0.011, 'H': 0.015, 'H+': 0.024, 'Frost Line': 0.069, 'Limit': 7.5})

# Brown Dwarf Stars

# L-Class Brown Dwarf Stars

db.insert({'type': 'L0', 'lum': 0.00063, 'mass': 0.083, 'diameter': 0.00053, 'roche limit': 0.00098, 'H-': 0.019, 'H': 0.026, 'H+': 0.044, 'Frost Line': 0.122, 'Limit': 4.2})
db.insert({'type': 'L1', 'lum': 0.0005, 'mass': 0.0807, 'diameter': 0.00053, 'roche limit': 0.00095, 'H-': 0.017, 'H': 0.023, 'H+': 0.039, 'Frost Line': 0.109, 'Limit': 4.1})
db.insert({'type': 'L2', 'lum': 0.00037, 'mass': 0.0784, 'diameter': 0.00052, 'roche limit': 0.00093, 'H-': 0.014, 'H': 0.019, 'H+': 0.034, 'Frost Line': 0.094, 'Limit':4.0})
db.insert({'type': 'L3', 'lum': 0.00024, 'mass': 0.0761, 'diameter': 0.00051, 'roche limit': 0.0009, 'H-': 0.012, 'H': 0.016, 'H+': 0.027, 'Frost Line': 0.076, 'Limit': 3.9})
db.insert({'type': 'L4', 'lum': 0.00011, 'mass': 0.0738, 'diameter': 0.00050, 'roche limit': 0.00087, 'H-': 0.008, 'H': 0.011, 'H+': 0.019, 'Frost Line': 0.051, 'Limit': 3.7})
db.insert({'type': 'L5', 'lum': 0.000095, 'mass': 0.0715, 'diameter': 0.00050, 'roche limit': 0.00085, 'H-': 0.007, 'H': 0.01, 'H+': 0.017, 'Frost Line': 0.048, 'Limit': 3.6})
db.insert({'type': 'L6', 'lum': 0.00008, 'mass': 0.0692, 'diameter': 0.00049, 'roche limit': 0.00082, 'H-': 0.007, 'H': 0.01, 'H+': 0.016, 'Frost Line': 0.044, 'Limit': 3.5})
db.insert({'type': 'L7', 'lum': 0.000065, 'mass': 0.0669, 'diameter': 0.00048, 'roche limit': 0.00079, 'H-': 0.006, 'H': 0.008, 'H+': 0.014, 'Frost Line': 0.04, 'Limit': 3.4})
db.insert({'type': 'L8', 'lum': 0.00005, 'mass': 0.0646, 'diameter': 0.00048, 'roche limit': 0.00076, 'H-': 0.005, 'H': 0.007, 'H+': 0.012, 'Frost Line': 0.035, 'Limit': 3.3})
db.insert({'type': 'L9', 'lum': 0.000035, 'mass': 0.0623, 'diameter': 0.00047, 'roche limit': 0.00074, 'H-': 0.004, 'H': 0.006, 'H+': 0.01, 'Frost Line': 0.029, 'Limit': 3.2})

User = Query()
result = db.search(User.type == 'F7 V')

print(result[0]['mass'])