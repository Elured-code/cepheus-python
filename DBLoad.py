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

db.insert({'type': 'K0 V', 'lum': 1.21, 'mass': 1.040, 'diameter': 0.0048, 'roche limit': 0.0123, 'H-': 0.83, 'H': 1.10, 'H+': 1.95, 'Frost Line': 5.34, 'Limit': 52})
db.insert({'type': 'K1 V', 'lum': 1.102, 'mass': 1.020, 'diameter': 0.0048, 'roche limit': 0.0120, 'H-': 0.79, 'H': 1.05, 'H+': 1.86, 'Frost Line': 5.10, 'Limit': 51})
db.insert({'type': 'K2 V', 'lum': 0.994, 'mass': 1, 'diameter': 0.0047, 'roche limit': 0.0118, 'H-': 0.75, 'H': 1, 'H+': 1.76, 'Frost Line': 4.84, 'Limit': 50})
db.insert({'type': 'K3 V', 'lum': 0.886, 'mass': 0.98, 'diameter': 0.0045, 'roche limit': 0.0116, 'H-': 0.71, 'H': 0.95, 'H+': 1.67, 'Frost Line': 4.57, 'Limit': 49})
db.insert({'type': 'K4 V', 'lum': 4.42, 'mass': 1.38, 'diameter': 0.0068, 'roche limit': 0.0163, 'H-': 1.6, 'H': 2.2, 'H+': 3.8, 'Frost Line': 10.2, 'Limit': 56})
db.insert({'type': 'K5 V', 'lum': 3.5, 'mass': 1.3, 'diameter': 0.0066, 'roche limit': 0.0153, 'H-': 1.5, 'H': 2.0, 'H+': 3.3, 'Frost Line': 9.08, 'Limit': 59})
db.insert({'type': 'K6 V', 'lum': 3.042, 'mass': 1.248, 'diameter': 0.0062, 'roche limit': 0.0147, 'H-': 1.4, 'H': 1.9, 'H+': 3.1, 'Frost Line': 8.46, 'Limit': 50})
db.insert({'type': 'K7 V', 'lum': 2.584, 'mass': 1.196, 'diameter': 0.0059, 'roche limit': 0.0141, 'H-': 1.3, 'H': 1.7, 'H+': 3.1, 'Frost Line': 7.80, 'Limit': 48})
db.insert({'type': 'K8 V', 'lum': 2.126, 'mass': 1.144, 'diameter': 0.0055, 'roche limit': 0.0135, 'H-': 1.1, 'H': 1.5, 'H+': 2.6, 'Frost Line': 7.08, 'Limit': 46})
db.insert({'type': 'K9 V', 'lum': 1.668, 'mass': 1.092, 'diameter': 0.0052, 'roche limit': 0.0129, 'H-': 1.0, 'H': 1.4, 'H+': 2.3, 'Frost Line': 6.27, 'Limit': 44})

# Red

db.insert({'type': 'M0 V', 'lum': 1.21, 'mass': 1.040, 'diameter': 0.0048, 'roche limit': 0.0123, 'H-': 0.83, 'H': 1.10, 'H+': 1.95, 'Frost Line': 5.34, 'Limit': 52})
db.insert({'type': 'M1 V', 'lum': 1.102, 'mass': 1.020, 'diameter': 0.0048, 'roche limit': 0.0120, 'H-': 0.79, 'H': 1.05, 'H+': 1.86, 'Frost Line': 5.10, 'Limit': 51})
db.insert({'type': 'M2 V', 'lum': 0.994, 'mass': 1, 'diameter': 0.0047, 'roche limit': 0.0118, 'H-': 0.75, 'H': 1, 'H+': 1.76, 'Frost Line': 4.84, 'Limit': 50})
db.insert({'type': 'M3 V', 'lum': 0.886, 'mass': 0.98, 'diameter': 0.0045, 'roche limit': 0.0116, 'H-': 0.71, 'H': 0.95, 'H+': 1.67, 'Frost Line': 4.57, 'Limit': 49})
db.insert({'type': 'M4 V', 'lum': 4.42, 'mass': 1.38, 'diameter': 0.0068, 'roche limit': 0.0163, 'H-': 1.6, 'H': 2.2, 'H+': 3.8, 'Frost Line': 10.2, 'Limit': 56})
db.insert({'type': 'M5 V', 'lum': 3.5, 'mass': 1.3, 'diameter': 0.0066, 'roche limit': 0.0153, 'H-': 1.5, 'H': 2.0, 'H+': 3.3, 'Frost Line': 9.08, 'Limit': 59})
db.insert({'type': 'M6 V', 'lum': 3.042, 'mass': 1.248, 'diameter': 0.0062, 'roche limit': 0.0147, 'H-': 1.4, 'H': 1.9, 'H+': 3.1, 'Frost Line': 8.46, 'Limit': 50})
db.insert({'type': 'M7 V', 'lum': 2.584, 'mass': 1.196, 'diameter': 0.0059, 'roche limit': 0.0141, 'H-': 1.3, 'H': 1.7, 'H+': 3.1, 'Frost Line': 7.80, 'Limit': 48})
db.insert({'type': 'M8 V', 'lum': 2.126, 'mass': 1.144, 'diameter': 0.0055, 'roche limit': 0.0135, 'H-': 1.1, 'H': 1.5, 'H+': 2.6, 'Frost Line': 7.08, 'Limit': 46})
db.insert({'type': 'M9 V', 'lum': 1.668, 'mass': 1.092, 'diameter': 0.0052, 'roche limit': 0.0129, 'H-': 1.0, 'H': 1.4, 'H+': 2.3, 'Frost Line': 6.27, 'Limit': 44})

User = Query()
result = db.search(User.type == 'F7 V')

print(result[0]['mass'])