from tinydb import TinyDB, Query


db = TinyDB('db.json')

print('Clearing database')

db.truncate()

# Bright Supergiants (Luminosity Class I / Ia)
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

db.insert({'type': 'B0 Ia', 'lum': 560000, 'mass': 45, 'diameter': 0.242, 'roche limit': 0.529, 'H-': 562, 'H': 752, 'H+': 1321, 'Frost Line': -1, 'Limit': 2475})
db.insert({'type': 'B1 Ia', 'lum': 488800, 'mass': 42, 'diameter': 0.264, 'roche limit': 0.494, 'H-': 525, 'H': 703, 'H+': 1234, 'Frost Line': -1, 'Limit': 2310})
db.insert({'type': 'B2 Ia', 'lum': 417600, 'mass': 39, 'diameter': 0.285, 'roche limit': 0.459, 'H-': 485, 'H': 649, 'H+': 1141, 'Frost Line': -1, 'Limit': 2145})
db.insert({'type': 'B3 Ia', 'lum': 346400, 'mass': 36, 'diameter': 0.306, 'roche limit': 0.428, 'H-': 442, 'H': 592, 'H+': 1039, 'Frost Line': -1, 'Limit': 1980})
db.insert({'type': 'B4 Ia', 'lum': 275000, 'mass': 33, 'diameter': 0.328, 'roche limit': 0.388, 'H-': 394, 'H': 527, 'H+': 926, 'Frost Line': -1, 'Limit': 1815})
db.insert({'type': 'B5 Ia', 'lum': 204000, 'mass': 30, 'diameter': 0.349, 'roche limit': 0.353, 'H-': 339, 'H': 454, 'H+': 798, 'Frost Line': -1, 'Limit': 1650})
db.insert({'type': 'B6 Ia', 'lum': 184600, 'mass': 27.6, 'diameter': 0.405, 'roche limit': 0.405, 'H-': 322, 'H': 431, 'H+': 758, 'Frost Line': -1, 'Limit': 1518})
db.insert({'type': 'B7 Ia', 'lum': 165200, 'mass': 25.2, 'diameter': 0.464, 'roche limit': 0.464, 'H-': 305, 'H': 409, 'H+': 718, 'Frost Line': -1, 'Limit': 1386})
db.insert({'type': 'B8 Ia', 'lum': 145800, 'mass': 22.8, 'diameter': 0.517, 'roche limit': 0.517, 'H-': 286, 'H': 383, 'H+': 673, 'Frost Line': -1, 'Limit': 1254})
db.insert({'type': 'B9 Ia', 'lum': 126000, 'mass': 20.4, 'diameter': 0.572, 'roche limit': 0.572, 'H-': 266, 'H': 357, 'H+': 627, 'Frost Line': -1, 'Limit': 1122})

db.insert({'type': 'A0 Ia', 'lum': 107000, 'mass': 18, 'diameter': 0.628, 'roche limit': 0.628, 'H-': 246, 'H': 329, 'H+': 578, 'Frost Line': -1, 'Limit': 990})
db.insert({'type': 'A1 Ia', 'lum': 101800, 'mass': 17.4, 'diameter': 0.641, 'roche limit': 0.641, 'H-': 240, 'H': 321, 'H+': 564, 'Frost Line': -1, 'Limit': 957})
db.insert({'type': 'A2 Ia', 'lum': 96600, 'mass': 16.8, 'diameter': 0.654, 'roche limit': 0.654, 'H-': 234, 'H': 313, 'H+': 549, 'Frost Line': -1, 'Limit': 924})
db.insert({'type': 'A3 Ia', 'lum': 91400, 'mass': 16.2, 'diameter': 0.667, 'roche limit': 0.667, 'H-': 227, 'H': 304, 'H+': 534, 'Frost Line': -1, 'Limit': 891})
db.insert({'type': 'A4 Ia', 'lum': 86200, 'mass': 15.6, 'diameter': 0.680, 'roche limit': 0.680, 'H-': 221, 'H': 296, 'H+': 519, 'Frost Line': -1, 'Limit': 858})
db.insert({'type': 'A5 Ia', 'lum': 81000, 'mass': 15, 'diameter': 0.693, 'roche limit': 0.693, 'H-': 214, 'H': 287, 'H+': 503, 'Frost Line': -1, 'Limit': 825})
db.insert({'type': 'A6 Ia', 'lum': 77000, 'mass': 14.6, 'diameter': 0.717, 'roche limit': 0.771, 'H-': 209, 'H': 281, 'H+': 490, 'Frost Line': -1, 'Limit': 803})
db.insert({'type': 'A7 Ia', 'lum': 73000, 'mass': 14.2, 'diameter': 0.740, 'roche limit': 0.740, 'H-': 203, 'H': 272, 'H+': 477, 'Frost Line': -1, 'Limit': 781})
db.insert({'type': 'A8 Ia', 'lum': 69000, 'mass': 13.8, 'diameter': 0.763, 'roche limit': 0.763, 'H-': 198, 'H': 265, 'H+': 464, 'Frost Line': -1, 'Limit': 759})
db.insert({'type': 'A9 Ia', 'lum': 65000, 'mass': 13.4, 'diameter': 0.846, 'roche limit': 0.846, 'H-': 192, 'H': 257, 'H+': 450, 'Frost Line': -1, 'Limit': 737})

# White

db.insert({'type': 'F0 Ia', 'lum': 61000, 'mass': 13, 'diameter': 0.810, 'roche limit': 0.810, 'H-': 186, 'H': 249, 'H+': 436, 'Frost Line': -1, 'Limit': 637})
db.insert({'type': 'F1 Ia', 'lum': 59000, 'mass': 12.8, 'diameter': 0.837, 'roche limit': 0.837, 'H-': 183, 'H': 245, 'H+': 429, 'Frost Line': -1, 'Limit': 628})
db.insert({'type': 'F2 Ia', 'lum': 57000, 'mass': 12.6, 'diameter': 0.865, 'roche limit': 0.865, 'H-': 180, 'H': 241, 'H+': 422, 'Frost Line': -1, 'Limit': 618})
db.insert({'type': 'F3 Ia', 'lum': 55000, 'mass': 12.4, 'diameter': 0.893, 'roche limit': 0.893, 'H-': 176, 'H': 236, 'H+': 414, 'Frost Line': -1, 'Limit': 608})
db.insert({'type': 'F4 Ia', 'lum': 53000, 'mass': 12.2, 'diameter': 0.921, 'roche limit': 0.921, 'H-': 173, 'H': 232, 'H+': 407, 'Frost Line': -1, 'Limit': 598})
db.insert({'type': 'F5 Ia', 'lum': 51000, 'mass': 12, 'diameter': 0.949, 'roche limit': 0.949, 'H-': 170, 'H': 228, 'H+': 399, 'Frost Line': -1, 'Limit': 588})
db.insert({'type': 'F6 Ia', 'lum': 54200, 'mass': 12, 'diameter': 1.037, 'roche limit': 1.037, 'H-': 175, 'H': 234, 'H+': 411, 'Frost Line': -1, 'Limit': 588})
db.insert({'type': 'F7 Ia', 'lum': 57400, 'mass': 12, 'diameter': 1.124, 'roche limit': 1.124, 'H-': 180, 'H': 241, 'H+': 423, 'Frost Line': -1, 'Limit': 588})
db.insert({'type': 'F8 Ia', 'lum': 60600, 'mass': 12, 'diameter': 1.211, 'roche limit': 1.211, 'H-': 185, 'H': 248, 'H+': 435, 'Frost Line': -1, 'Limit': 588})
db.insert({'type': 'F9 Ia', 'lum': 63800, 'mass': 12, 'diameter': 1.299, 'roche limit': 1.299, 'H-': 190, 'H': 254, 'H+': 446, 'Frost Line': -1, 'Limit': 588})

# Yellow-tinted White

db.insert({'type': 'G0 Ia', 'lum': 67000, 'mass': 12, 'diameter': 1.386, 'roche limit': 1.386, 'H-': 195, 'H': 261, 'H+': 457, 'Frost Line': -1, 'Limit': 588})
db.insert({'type': 'G1 Ia', 'lum': 71400, 'mass': 12.1, 'diameter': 3.062, 'roche limit': 3.062, 'H-': 201, 'H': 269, 'H+': 472, 'Frost Line': -1, 'Limit': 593})
db.insert({'type': 'G2 Ia', 'lum': 75800, 'mass': 12.2, 'diameter': 3.353, 'roche limit': 3.353, 'H-': 207, 'H': 277, 'H+': 486, 'Frost Line': -1, 'Limit': 598})
db.insert({'type': 'G3 Ia', 'lum': 80200, 'mass': 12.3, 'diameter': 3.643, 'roche limit': 3.642, 'H-': 213, 'H': 285, 'H+': 500, 'Frost Line': -1, 'Limit': 603})
db.insert({'type': 'G4 Ia', 'lum': 84600, 'mass': 12.4, 'diameter': 3.933, 'roche limit': 3.933, 'H-': 219, 'H': 293, 'H+': 514, 'Frost Line': -1, 'Limit': 608})
db.insert({'type': 'G5 Ia', 'lum': 89000, 'mass': 12.5, 'diameter': 4.223, 'roche limit': 4.223, 'H-': 224, 'H': 300, 'H+': 527, 'Frost Line': -1, 'Limit': 613})
db.insert({'type': 'G6 Ia', 'lum': 90600, 'mass': 12.7, 'diameter': 4.671, 'roche limit': 4.671, 'H-': 226, 'H': 303, 'H+': 532, 'Frost Line': -1, 'Limit': 623})
db.insert({'type': 'G7 Ia', 'lum': 92200, 'mass': 12.9, 'diameter': 5.023, 'roche limit': 5.023, 'H-': 228, 'H': 305, 'H+': 536, 'Frost Line': -1, 'Limit': 633})
db.insert({'type': 'G8 Ia', 'lum': 93800, 'mass': 13.1, 'diameter': 5.376, 'roche limit': 5.376, 'H-': 230, 'H': 307, 'H+': 541, 'Frost Line': -1, 'Limit': 642})
db.insert({'type': 'G9 Ia', 'lum': 95400, 'mass': 13.4, 'diameter': 5.730, 'roche limit': 5.730, 'H-': 232, 'H': 311, 'H+': 546, 'Frost Line': -1, 'Limit': 657})

# Orange-tinted White

db.insert({'type': 'K0 Ia', 'lum': 97000, 'mass': 13.8, 'diameter': 3.042, 'roche limit': 3.042, 'H-': 234, 'H': 313, 'H+': 550, 'Frost Line': -1, 'Limit': 677})
db.insert({'type': 'K1 Ia', 'lum': 99000, 'mass': 14.2, 'diameter': 3.376, 'roche limit': 3.376, 'H-': 237, 'H': 310, 'H+': 528, 'Frost Line': -1, 'Limit': 696})
db.insert({'type': 'K2 Ia', 'lum': 101000, 'mass': 14.6, 'diameter': 3.707, 'roche limit': 3.707, 'H-': 239, 'H': 320, 'H+': 561, 'Frost Line': -1, 'Limit': 716})
db.insert({'type': 'K3 Ia', 'lum': 103000, 'mass': 15.0, 'diameter': 4.038, 'roche limit': 4.038, 'H-': 241, 'H': 323, 'H+': 567, 'Frost Line': -1, 'Limit': 735})
db.insert({'type': 'K4 Ia', 'lum': 105000, 'mass': 15.5, 'diameter': 4.369, 'roche limit': 4.369, 'H-': 244, 'H': 326, 'H+': 572, 'Frost Line': -1, 'Limit': 760})
db.insert({'type': 'K5 Ia', 'lum': 107000, 'mass': 16.5, 'diameter': 4.700, 'roche limit': 4.700, 'H-': 246, 'H': 329, 'H+': 578, 'Frost Line': -1, 'Limit': 784})
db.insert({'type': 'K6 Ia', 'lum': 109000, 'mass': 16.5, 'diameter': 5.124, 'roche limit': 5.124, 'H-': 248, 'H': 332, 'H+': 583, 'Frost Line': -1, 'Limit': 809})
db.insert({'type': 'K7 Ia', 'lum': 111000, 'mass': 16.5, 'diameter': 5.549, 'roche limit': 5.549, 'H-': 250, 'H': 337, 'H+': 588, 'Frost Line': -1, 'Limit': 809})
db.insert({'type': 'K8 Ia', 'lum': 113000, 'mass': 16.5, 'diameter': 5.973, 'roche limit': 5.973, 'H-': 253, 'H': 339, 'H+': 594, 'Frost Line': -1, 'Limit': 809})
db.insert({'type': 'K9 Ia', 'lum': 115000, 'mass': 16.5, 'diameter': 6.397, 'roche limit': 6.397, 'H-': 255, 'H': 341, 'H+': 599, 'Frost Line': -1, 'Limit': 809})

# Red-Tinted White

db.insert({'type': 'M0 Ia', 'lum': 117000, 'mass': 17, 'diameter': 6.511, 'roche limit': 6.511, 'H-': 257, 'H': 344, 'H+': 604, 'Frost Line': -1, 'Limit': 833})
db.insert({'type': 'M1 Ia', 'lum': 155300, 'mass': 18, 'diameter': 6.625, 'roche limit': 6.625, 'H-': 296, 'H': 396, 'H+': 696, 'Frost Line': -1, 'Limit': 882})
db.insert({'type': 'M2 Ia', 'lum': 193500, 'mass': 19, 'diameter': 6.738, 'roche limit': 6.738, 'H-': 331, 'H': 443, 'H+': 777, 'Frost Line': -1, 'Limit': 931})
db.insert({'type': 'M3 Ia', 'lum': 231700, 'mass': 20, 'diameter': 6.829, 'roche limit': 6.829, 'H-': 362, 'H': 484, 'H+': 850, 'Frost Line': -1, 'Limit': 980})
db.insert({'type': 'M4 Ia', 'lum': 270000, 'mass': 21, 'diameter': 6.852, 'roche limit': 6.852, 'H-': 390, 'H': 522, 'H+': 918, 'Frost Line': -1, 'Limit': 1029})
db.insert({'type': 'M5 Ia', 'lum': 308300, 'mass': 22, 'diameter': 7.353, 'roche limit': 7.353, 'H-': 417, 'H': 558, 'H+': 980, 'Frost Line': -1, 'Limit': 1078})
db.insert({'type': 'M6 Ia', 'lum': 346500, 'mass': 23.5, 'diameter': 7.855, 'roche limit': 7.855, 'H-': 442, 'H': 592, 'H+': 1039, 'Frost Line': -1, 'Limit': 1152})
db.insert({'type': 'M7 Ia', 'lum': 384800, 'mass': 25, 'diameter': 8.356, 'roche limit': 8.356, 'H-': 466, 'H': 624, 'H+': 1095, 'Frost Line': -1, 'Limit': 1225})
db.insert({'type': 'M8 Ia', 'lum': 423000, 'mass': 27.5, 'diameter': 9.192, 'roche limit': 9.192, 'H-': 488, 'H': 653, 'H+': 1148, 'Frost Line': -1, 'Limit': 1348})
db.insert({'type': 'M9 Ia', 'lum': 461300, 'mass': 30, 'diameter': 10.027, 'roche limit': 10.027, 'H-': 510, 'H': 683, 'H+': 1199, 'Frost Line': -1, 'Limit': 1470})

# Supergiant Stars (Luminosity Class Ib)

# Red-Tinted White

db.insert({'type': 'M0 Ib', 'lum': 46000, 'mass': 16, 'diameter': 3.988, 'roche limit': 0, 'H-': 161, 'H': 216, 'H+': 379, 'Frost Line': -1, 'Limit': 784})
db.insert({'type': 'M1 Ib', 'lum': 54600, 'mass': 16.8, 'diameter': 5.117, 'roche limit': 0, 'H-': 176, 'H': 236, 'H+': 413, 'Frost Line': -1, 'Limit': 824})
db.insert({'type': 'M2 Ib', 'lum': 63200, 'mass': 17.6, 'diameter': 6.25, 'roche limit': 0, 'H-': 189, 'H': 253, 'H+': 444, 'Frost Line': -1, 'Limit': 863})
db.insert({'type': 'M3 Ib', 'lum': 71800, 'mass': 18.4, 'diameter': 7.38, 'roche limit': 0, 'H-': 201, 'H': 269, 'H+': 473, 'Frost Line': -1, 'Limit': 902})
db.insert({'type': 'M4 Ib', 'lum': 80400, 'mass': 19.2, 'diameter': 8.51, 'roche limit': 0, 'H-': 213, 'H': 285, 'H+': 501, 'Frost Line': -1, 'Limit': 941})
db.insert({'type': 'M5 Ib', 'lum': 89000, 'mass': 20, 'diameter': 9.643, 'roche limit': 0, 'H-': 224, 'H': 300, 'H+': 527, 'Frost Line': -1, 'Limit': 980})
db.insert({'type': 'M6 Ib', 'lum': 96000, 'mass': 21.3, 'diameter': 10.575, 'roche limit': 0, 'H-': 233, 'H': 312, 'H+': 547, 'Frost Line': -1, 'Limit': 1044})
db.insert({'type': 'M7 Ib', 'lum': 103000, 'mass': 22.5, 'diameter': 11.508, 'roche limit': 0, 'H-': 241, 'H': 323, 'H+': 567, 'Frost Line': -1, 'Limit': 1103})
db.insert({'type': 'M8 Ib', 'lum': 110000, 'mass': 23.7, 'diameter': 12.444, 'roche limit': 0, 'H-': 249, 'H': 334, 'H+': 586, 'Frost Line': -1, 'Limit': 1162})
db.insert({'type': 'M9 Ib', 'lum': 17000, 'mass': 25, 'diameter': 13.376, 'roche limit': 0, 'H-': 257, 'H': 344, 'H+': 604, 'Frost Line': -1, 'Limit': 1225})

# Bright Giants (Luminosity Class II)

# White

db.insert({'type': 'F0 II', 'lum': 600, 'mass': 10, 'diameter': 0.075, 'roche limit': 0.118, 'H-': 18.4, 'H': 24.7, 'H+': 43.3, 'Frost Line': 119, 'Limit': 500})
db.insert({'type': 'F1 II', 'lum': 582, 'mass': 9.7, 'diameter': 0.077, 'roche limit': 0.114, 'H-': 18.1, 'H': 24.3, 'H+': 42.6, 'Frost Line': 117, 'Limit': 485})
db.insert({'type': 'F2 II', 'lum': 564, 'mass': 9.3, 'diameter': 0.079, 'roche limit': 0.11, 'H-': 17.9, 'H': 23.5, 'H+': 42, 'Frost Line': 116, 'Limit': 465})
db.insert({'type': 'F3 II', 'lum': 546, 'mass': 8.9, 'diameter': 0.080, 'roche limit': 0.105, 'H-': 17.6, 'H': 23.6, 'H+': 41.3, 'Frost Line': 114, 'Limit': 445})
db.insert({'type': 'F4 II', 'lum': 528, 'mass': 8.5, 'diameter': 0.082, 'roche limit': 0.1, 'H-': 17.3, 'H': 23.2, 'H+': 40.6, 'Frost Line': 112, 'Limit': 425})
db.insert({'type': 'F5 II', 'lum': 510, 'mass': 8.1, 'diameter': 0.084, 'roche limit': 0.095, 'H-': 17.0, 'H': 22.8, 'H+': 39.9, 'Frost Line': 110, 'Limit': 405})
db.insert({'type': 'F6 II', 'lum': 520, 'mass': 8.1, 'diameter': 0.091, 'roche limit': 0.095, 'H-': 17.2, 'H': 23.0, 'H+': 40.3, 'Frost Line': 111, 'Limit': 405})
db.insert({'type': 'F7 II', 'lum': 530, 'mass': 8.1, 'diameter': 0.097, 'roche limit': 0, 'H-': 17.4, 'H': 23.2, 'H+': 40.7, 'Frost Line': 112, 'Limit': 405})
db.insert({'type': 'F8 II', 'lum': 540, 'mass': 8.1, 'diameter': 0.104, 'roche limit': 0, 'H-': 17.5, 'H': 23.4, 'H+': 41.1, 'Frost Line': 113, 'Limit': 405})
db.insert({'type': 'F9 II', 'lum': 550, 'mass': 8.1, 'diameter': 0.11, 'roche limit': 0, 'H-': 17.6, 'H': 23.6, 'H+': 41.4, 'Frost Line': 114, 'Limit': 405})

# Yellow-Tinted White

db.insert({'type': 'G0 II', 'lum': 560, 'mass': 8.1, 'diameter': 0.117, 'roche limit': 0, 'H-': 17.8, 'H': 23.8, 'H+': 41.8, 'Frost Line': 115, 'Limit': 405})
db.insert({'type': 'G1 II', 'lum': 596, 'mass': 8.5, 'diameter': 0.128, 'roche limit': 0, 'H-': 18.4, 'H': 24.6, 'H+': 43.1, 'Frost Line': 119, 'Limit': 425})
db.insert({'type': 'G2 II', 'lum': 632, 'mass': 8.9, 'diameter': 0.139, 'roche limit': 0, 'H-': 18.9, 'H': 25.3, 'H+': 44.4, 'Frost Line': 122, 'Limit': 445})
db.insert({'type': 'G3 II', 'lum': 668, 'mass': 9.3, 'diameter': 0.15, 'roche limit': 0, 'H-': 19.4, 'H': 26, 'H+': 45.7, 'Frost Line': 126, 'Limit': 465})
db.insert({'type': 'G4 II', 'lum': 704, 'mass': 9.6, 'diameter': 0.161, 'roche limit': 0, 'H-': 20, 'H': 26.8, 'H+': 46.9, 'Frost Line': 129, 'Limit': 480})
db.insert({'type': 'G5 II', 'lum': 740, 'mass': 10, 'diameter': 0.172, 'roche limit': 0, 'H-': 20.5, 'H': 27.4, 'H+': 48.1, 'Frost Line': 132, 'Limit': 500})
db.insert({'type': 'G6 II', 'lum': 770, 'mass': 10.2, 'diameter': 0.188, 'roche limit': 0, 'H-': 20.9, 'H': 28, 'H+': 49, 'Frost Line': 135, 'Limit': 510})
db.insert({'type': 'G7 II', 'lum': 800, 'mass': 10.4, 'diameter': 0.204, 'roche limit': 0, 'H-': 21.3, 'H': 28.5, 'H+': 50, 'Frost Line': 138, 'Limit': 520})
db.insert({'type': 'G8 II', 'lum': 830, 'mass': 10.6, 'diameter': 0.22, 'roche limit': 0, 'H-': 21.7, 'H': 29, 'H+': 50.9, 'Frost Line': 140, 'Limit': 530})
db.insert({'type': 'G9 II', 'lum': 860, 'mass': 10.8, 'diameter': 0.236, 'roche limit': 0, 'H-': 22, 'H': 29.5, 'H+': 51.8, 'Frost Line': 143, 'Limit': 540})

# Red

db.insert({'type': 'M0 II', 'lum': 4600, 'mass': 14, 'diameter': 1.103, 'roche limit': 0, 'H-': 50.9, 'H': 68.2, 'H+': 120, 'Frost Line': 329, 'Limit': 700})
db.insert({'type': 'M1 II', 'lum': 6660, 'mass': 14.4, 'diameter': 1.544, 'roche limit': 0, 'H-': 61, 'H': 81.8, 'H+': 144, 'Frost Line': 396, 'Limit': 720})
db.insert({'type': 'M2 II', 'lum': 8720, 'mass': 14.8, 'diameter': 1.986, 'roche limit': 0, 'H-': 70.1, 'H': 83.9, 'H+': 165, 'Frost Line': 453, 'Limit': 740})
db.insert({'type': 'M3 II', 'lum': 10780, 'mass': 15.2, 'diameter': 2.428, 'roche limit': 0, 'H-': 78, 'H': 93.9, 'H+': 184, 'Frost Line': 504, 'Limit': 760})
db.insert({'type': 'M4 II', 'lum': 12840, 'mass': 15.6, 'diameter': 2.87, 'roche limit': 0, 'H-': 85.1, 'H': 105, 'H+': 200, 'Frost Line': 550, 'Limit': 780})
db.insert({'type': 'M5 II', 'lum': 14900, 'mass': 16, 'diameter': 3.311, 'roche limit': 0, 'H-': 91.6, 'H': 114, 'H+': 216, 'Frost Line': 592, 'Limit': 800})
db.insert({'type': 'M6 II', 'lum': 15225, 'mass': 16.5, 'diameter': 3.57, 'roche limit': 0, 'H-': 92.6, 'H': 124, 'H+': 218, 'Frost Line': 599, 'Limit': 825})
db.insert({'type': 'M7 II', 'lum': 15550, 'mass': 17, 'diameter': 3.824, 'roche limit': 0, 'H-': 93.6, 'H': 126, 'H+': 220, 'Frost Line': 605, 'Limit': 850})
db.insert({'type': 'M8 II', 'lum': 15875, 'mass': 17.5, 'diameter': 4.081, 'roche limit': 0, 'H-': 94.6, 'H': 127, 'H+': 223, 'Frost Line': 622, 'Limit': 875})
db.insert({'type': 'M9 II', 'lum': 16200, 'mass': 18, 'diameter': 4.332, 'roche limit': 0, 'H-': 95.6, 'H': 128, 'H+': 225, 'Frost Line': 618, 'Limit': 900})


# Giant Stars (Luminosity Class III)

# Blue-White

db.insert({'type': 'A0 III', 'lum': 280, 'mass': 12, 'diameter': 0.058, 'roche limit': 0, 'H-': 12.6, 'H': 16.9, 'H+': 29.6, 'Frost Line': 83.5, 'Limit': 600})
db.insert({'type': 'A1 III', 'lum': 242, 'mass': 11.4, 'diameter': 0.055, 'roche limit': 0, 'H-': 11.7, 'H': 15.7, 'H+': 27.5, 'Frost Line': 77.6, 'Limit': 570})
db.insert({'type': 'A2 III', 'lum': 204, 'mass': 10.8, 'diameter': 0.052, 'roche limit': 0, 'H-': 10.8, 'H': 14.5, 'H+': 25.3, 'Frost Line': 71.4, 'Limit': 540})
db.insert({'type': 'A3 III', 'lum': 166, 'mass': 10.2, 'diameter': 0.049, 'roche limit': 0, 'H-': 9.69, 'H': 13, 'H+': 22.8, 'Frost Line': 64.3, 'Limit': 510})
db.insert({'type': 'A4 III', 'lum': 128, 'mass': 9.6, 'diameter': 0.046, 'roche limit': 0, 'H-': 8.49, 'H': 11.4, 'H+': 20, 'Frost Line': 56.4, 'Limit': 480})
db.insert({'type': 'A5 III', 'lum': 90, 'mass': 9, 'diameter': 0.043, 'roche limit': 0, 'H-': 7.12, 'H': 9.54, 'H+': 16.8, 'Frost Line': 47.4, 'Limit': 450})
db.insert({'type': 'A6 III', 'lum': 82, 'mass': 8.8, 'diameter': 0.043, 'roche limit': 0, 'H-': 6.8, 'H': 9.1, 'H+': 16, 'Frost Line': 45.2, 'Limit': 440})
db.insert({'type': 'A7 III', 'lum': 75, 'mass': 8.6, 'diameter': 0.044, 'roche limit': 0, 'H-': 6.5, 'H': 8.7, 'H+': 15.3, 'Frost Line': 43.2, 'Limit': 430})
db.insert({'type': 'A8 III', 'lum': 67, 'mass': 8.4, 'diameter': 0.044, 'roche limit': 0, 'H-': 6.13, 'H': 8.23, 'H+': 14.5, 'Frost Line': 40.1, 'Limit': 420})
db.insert({'type': 'A9 III', 'lum': 60, 'mass': 8.2, 'diameter': 0.044, 'roche limit': 0, 'H-': 5.82, 'H': 7.79, 'H+': 13.7, 'Frost Line': 38.7, 'Limit': 410})

# White

db.insert({'type': 'F0 III', 'lum': 53, 'mass': 8, 'diameter': 0.022, 'roche limit': 0, 'H-': 5.47, 'H': 7.11, 'H+': 12.9, 'Frost Line': 35.3, 'Limit': 400})
db.insert({'type': 'F1 III', 'lum': 51, 'mass': 7.4, 'diameter': 0.023, 'roche limit': 0.087, 'H-': 5.36, 'H': 7.2, 'H+': 12.7, 'Frost Line': 34.7, 'Limit': 370})
db.insert({'type': 'F2 III', 'lum': 49, 'mass': 6.8, 'diameter': 0.023, 'roche limit': 0.08, 'H-': 5.26, 'H': 7.05, 'H+': 12.4, 'Frost Line': 34.0, 'Limit': 340})
db.insert({'type': 'F3 III', 'lum': 47, 'mass': 6.2, 'diameter': 0.024, 'roche limit': 0.073, 'H-': 5.15, 'H': 6.89, 'H+': 12.1, 'Frost Line': 33.3, 'Limit': 310})
db.insert({'type': 'F4 III', 'lum': 45, 'mass': 5.6, 'diameter': 0.024, 'roche limit': 0.066, 'H-': 5.04, 'H': 6.76, 'H+': 11.9, 'Frost Line': 32.6, 'Limit': 280})
db.insert({'type': 'F5 III', 'lum': 43, 'mass': 5, 'diameter': 0.025, 'roche limit': 0.056, 'H-': 4.93, 'H': 6.6, 'H+': 11.6, 'Frost Line': 31.8, 'Limit': 250})
db.insert({'type': 'F6 III', 'lum': 44, 'mass': 4.5, 'diameter': 0.026, 'roche limit': 0.053, 'H-': 4.98, 'H': 6.69, 'H+': 11.8, 'Frost Line': 32.2, 'Limit': 225})
db.insert({'type': 'F7 III', 'lum': 46, 'mass': 4, 'diameter': 0.028, 'roche limit': 0.047, 'H-': 5.09, 'H': 6.82, 'H+': 12.0, 'Frost Line': 32.9, 'Limit': 200})
db.insert({'type': 'F8 III', 'lum': 47, 'mass': 3.5, 'diameter': 0.03, 'roche limit': 0.042, 'H-': 5.15, 'H': 6.89, 'H+': 12.1, 'Frost Line': 33.3, 'Limit': 175})
db.insert({'type': 'F9 III', 'lum': 49, 'mass': 3, 'diameter': 0.032, 'roche limit': 0.035, 'H-': 5.26, 'H': 7.05, 'H+': 12.4, 'Frost Line': 34, 'Limit': 150})

# Yellow

db.insert({'type': 'G0 III', 'lum': 50, 'mass': 2.5, 'diameter': 0.034, 'roche limit': 0, 'H-': 5.31, 'H': 7.19, 'H+': 12.5, 'Frost Line': 34.3, 'Limit': 125})
db.insert({'type': 'G1 III', 'lum': 55, 'mass': 2.64, 'diameter': 0.037, 'roche limit': 0, 'H-': 5.57, 'H': 7.46, 'H+': 13.1, 'Frost Line': 36, 'Limit': 132})
db.insert({'type': 'G2 III', 'lum': 60, 'mass': 2.78, 'diameter': 0.041, 'roche limit': 0, 'H-': 5.82, 'H': 7.79, 'H+': 13.7, 'Frost Line': 37.6, 'Limit': 139})
db.insert({'type': 'G3 III', 'lum': 65, 'mass': 2.92, 'diameter': 0.044, 'roche limit': 0, 'H-': 6.05, 'H': 8.12, 'H+': 14.3, 'Frost Line': 39.1, 'Limit': 146})
db.insert({'type': 'G4 III', 'lum': 70, 'mass': 3.06, 'diameter': 0.048, 'roche limit': 0, 'H-': 6.28, 'H': 8.41, 'H+': 14.8, 'Frost Line': 40.6, 'Limit': 153})
db.insert({'type': 'G5 III', 'lum': 75, 'mass': 3.2, 'diameter': 0.052, 'roche limit': 0, 'H-': 6.5, 'H': 8.7, 'H+': 15.3, 'Frost Line': 42, 'Limit': 160})
db.insert({'type': 'G6 III', 'lum': 79, 'mass': 3.36, 'diameter': 0.056, 'roche limit': 0, 'H-': 6.67, 'H': 8.93, 'H+': 15.7, 'Frost Line': 43.1, 'Limit': 166})
db.insert({'type': 'G7 III', 'lum': 83, 'mass': 3.52, 'diameter': 0.061, 'roche limit': 0, 'H-': 6.84, 'H': 9.16, 'H+': 16.1, 'Frost Line': 44.2, 'Limit': 176})
db.insert({'type': 'G8 III', 'lum': 87, 'mass': 3.68, 'diameter': 0.066, 'roche limit': 0, 'H-': 7, 'H': 9.38, 'H+': 16.5, 'Frost Line': 45.3, 'Limit': 184})
db.insert({'type': 'G9 III', 'lum': 91, 'mass': 3.84, 'diameter': 0.07, 'roche limit': 0, 'H-': 7.16, 'H': 9.6, 'H+': 16.9, 'Frost Line': 46.3, 'Limit': 192})

# Orange

db.insert({'type': 'K0 III', 'lum': 95, 'mass': 4, 'diameter': 0.075, 'roche limit': 0, 'H-': 7.32, 'H': 9.82, 'H+': 17.3, 'Frost Line': 47.3, 'Limit': 200})
db.insert({'type': 'K1 III', 'lum': 140, 'mass': 4.2, 'diameter': 0.099, 'roche limit': 0, 'H-': 8.88, 'H': 11.9, 'H+': 20.9, 'Frost Line': 57.4, 'Limit': 210})
db.insert({'type': 'K2 III', 'lum': 185, 'mass': 4.4, 'diameter': 0.123, 'roche limit': 0, 'H-': 10.3, 'H': 13.8, 'H+': 24, 'Frost Line': 66, 'Limit': 220})
db.insert({'type': 'K3 III', 'lum': 230, 'mass': 4.6, 'diameter': 0.147, 'roche limit': 0, 'H-': 11.4, 'H': 15.3, 'H+': 26.8, 'Frost Line': 73.6, 'Limit': 230})
db.insert({'type': 'K4 III', 'lum': 275, 'mass': 4.8, 'diameter': 0.172, 'roche limit': 0, 'H-': 12.5, 'H': 16.7, 'H+': 29.3, 'Frost Line': 80.5, 'Limit': 240})
db.insert({'type': 'K5 III', 'lum': 320, 'mass': 5, 'diameter': 0.196, 'roche limit': 0, 'H-': 13.5, 'H': 18.1, 'H+': 31.6, 'Frost Line': 86.8, 'Limit': 250})
db.insert({'type': 'K6 III', 'lum': 350, 'mass': 5.26, 'diameter': 0.215, 'roche limit': 0, 'H-': 14.1, 'H': 18.9, 'H+': 33.1, 'Frost Line': 90.1, 'Limit': 263})
db.insert({'type': 'K7 III', 'lum': 380, 'mass': 5.52, 'diameter': 0.225, 'roche limit': 0, 'H-': 14.7, 'H': 19.7, 'H+': 34.5, 'Frost Line': 94.6, 'Limit': 276})
db.insert({'type': 'K8 III', 'lum': 410, 'mass': 5.78, 'diameter': 0.254, 'roche limit': 0, 'H-': 15.2, 'H': 20.4, 'H+': 35.8, 'Frost Line': 98.2, 'Limit': 289})
db.insert({'type': 'K9 III', 'lum': 440, 'mass': 6.04, 'diameter': 0.274, 'roche limit': 0, 'H-': 15.8, 'H': 21.2, 'H+': 37.1, 'Frost Line': 102, 'Limit': 302})

# Red

db.insert({'type': 'M0 III', 'lum': 470, 'mass': 6.3, 'diameter': 0.293, 'roche limit': 0, 'H-': 16.3, 'H': 21.8, 'H+': 38.3, 'Frost Line': 106, 'Limit': 315})
db.insert({'type': 'M1 III', 'lum': 832, 'mass': 6.52, 'diameter': 0.447, 'roche limit': 0, 'H-': 21.7, 'H': 29.0, 'H+': 50.9, 'Frost Line': 140, 'Limit': 326})
db.insert({'type': 'M2 III', 'lum': 1194, 'mass': 6.74, 'diameter': 0.6, 'roche limit': 0, 'H-': 25.9, 'H': 34.7, 'H+': 61, 'Frost Line': 168, 'Limit': 337})
db.insert({'type': 'M3 III', 'lum': 1556, 'mass': 6.96, 'diameter': 0.754, 'roche limit': 0, 'H-': 29.6, 'H': 39.7, 'H+': 69.7, 'Frost Line': 192, 'Limit': 348})
db.insert({'type': 'M4 III', 'lum': 1918, 'mass': 7.18, 'diameter': 0.907, 'roche limit': 0, 'H-': 32.9, 'H': 44, 'H+': 77.3, 'Frost Line': 213, 'Limit': 359})
db.insert({'type': 'M5 III', 'lum': 2280, 'mass': 7.40, 'diameter': 1.06, 'roche limit': 0, 'H-': 35.9, 'H': 48, 'H+': 84.3, 'Frost Line': 232, 'Limit': 370})
db.insert({'type': 'M6 III', 'lum': 2382, 'mass': 7.85, 'diameter': 1.214, 'roche limit': 0, 'H-': 36.7, 'H': 49.1, 'H+': 86.2, 'Frost Line': 237, 'Limit': 392})
db.insert({'type': 'M7 III', 'lum': 2485, 'mass': 8.3, 'diameter': 1.368, 'roche limit': 0, 'H-': 37.4, 'H': 50.1, 'H+': 88, 'Frost Line': 242, 'Limit': 415})
db.insert({'type': 'M8 III', 'lum': 2587, 'mass': 8.75, 'diameter': 1.521, 'roche limit': 0, 'H-': 38.2, 'H': 51.1, 'H+': 89.8, 'Frost Line': 247, 'Limit': 437})
db.insert({'type': 'M9 III', 'lum': 2690, 'mass': 9.2, 'diameter': 1.675, 'roche limit': 0, 'H-': 39.0, 'H': 52.2, 'H+': 91.6, 'Frost Line': 252, 'Limit': 460})

# Subgiant Stars (Luminosity Class iV)

# Blue-White

db.insert({'type': 'O0 IV', 'lum': 1360000, 'mass': 100, 'diameter': 0.159, 'roche limit': 1.175, 'H-': 835, 'H': 1171, 'H+': 2059, 'Frost Line': -1, 'Limit': 5500})
db.insert({'type': 'O1 IV', 'lum': 1090000, 'mass': 97, 'diameter': 0.145, 'roche limit': 1.140, 'H-': 784, 'H': 1049, 'H+': 1843, 'Frost Line': -1, 'Limit': 4850})
db.insert({'type': 'O2 IV', 'lum': 872000, 'mass': 95, 'diameter': 0.132, 'roche limit': 1.117, 'H-': 701, 'H': 938, 'H+': 1649, 'Frost Line': -1, 'Limit': 4750})
db.insert({'type': 'O3 IV', 'lum': 696000, 'mass': 93, 'diameter': 0.118, 'roche limit': 1.093, 'H-': 626, 'H': 838, 'H+': 1473, 'Frost Line': -1, 'Limit': 4650})
db.insert({'type': 'O4 IV', 'lum': 552000, 'mass': 89, 'diameter': 0.105, 'roche limit': 1.046, 'H-': 558, 'H': 747, 'H+': 1312, 'Frost Line': -1, 'Limit': 4450})
db.insert({'type': 'O5 IV', 'lum': 437000, 'mass': 77, 'diameter': 0.091, 'roche limit': 0.905, 'H-': 496, 'H': 664, 'H+': 1167, 'Frost Line': -1, 'Limit': 3850})
db.insert({'type': 'O6 IV', 'lum': 313000, 'mass': 55, 'diameter': 0.085, 'roche limit': 0.647, 'H-': 420, 'H': 562, 'H+': 988, 'Frost Line': -1, 'Limit': 2750})
db.insert({'type': 'O7 IV', 'lum': 223000, 'mass': 44, 'diameter': 0.079, 'roche limit': 0.517, 'H-': 355, 'H': 475, 'H+': 834, 'Frost Line': -1, 'Limit': 2250})
db.insert({'type': 'O8 IV', 'lum': 157000, 'mass': 34, 'diameter': 0.071, 'roche limit': 0.400, 'H-': 298, 'H': 399, 'H+': 700, 'Frost Line': -1, 'Limit': 1700})
db.insert({'type': 'O9 IV', 'lum': 110000, 'mass': 27, 'diameter': 0.067, 'roche limit': 0.318, 'H-': 249, 'H': 333, 'H+': 585, 'Frost Line': -1, 'Limit': 1350})

# Blue-White

db.insert({'type': 'B0 IV', 'lum': 81000, 'mass': 20, 'diameter': 0.061, 'roche limit': 0.215, 'H-': 214, 'H': 287, 'H+': 503, 'Frost Line': -1, 'Limit': 1000})
db.insert({'type': 'B1 IV', 'lum': 65200, 'mass': 18, 'diameter': 0.054, 'roche limit': 0.212, 'H-': 192, 'H': 257, 'H+': 451, 'Frost Line': -1, 'Limit': 900})
db.insert({'type': 'B2 IV', 'lum': 49400, 'mass': 16, 'diameter': 0.047, 'roche limit': 0.188, 'H-': 167, 'H': 224, 'H+': 392, 'Frost Line': -1, 'Limit': 800})
db.insert({'type': 'B3 IV', 'lum': 33600, 'mass': 14, 'diameter': 0.039, 'roche limit': 0.165, 'H-': 138, 'H': 185, 'H+': 324, 'Frost Line': -1, 'Limit': 700})
db.insert({'type': 'B4 IV', 'lum': 17800, 'mass': 12, 'diameter': 0.032, 'roche limit': 0.141, 'H-': 101, 'H': 135, 'H+': 236, 'Frost Line': -1, 'Limit': 600})
db.insert({'type': 'B5 IV', 'lum': 2000, 'mass': 10, 'diameter': 0.025, 'roche limit': 0.118, 'H-': 33.6, 'H': 45, 'H+': 79, 'Frost Line': 217, 'Limit': 500})
db.insert({'type': 'B6 IV', 'lum': 1632, 'mass': 9.2, 'diameter': 0.024, 'roche limit': 0.109, 'H-': 30.4, 'H': 40.7, 'H+': 71.3, 'Frost Line': 196, 'Limit': 460})
db.insert({'type': 'B7 IV', 'lum': 1263, 'mass': 8.4, 'diameter': 0.024, 'roche limit': 0.099, 'H-': 26.7, 'H': 35.8, 'H+': 62.8, 'Frost Line': 173, 'Limit': 420})
db.insert({'type': 'B8 IV', 'lum': 894, 'mass': 7.6, 'diameter': 0.0023, 'roche limit': 0.09, 'H-': 22.5, 'H': 30.1, 'H+': 52.8, 'Frost Line': 145, 'Limit': 380})
db.insert({'type': 'B9 IV', 'lum': 525, 'mass': 6.8, 'diameter': 0.0022, 'roche limit': 0.08, 'H-': 17.2, 'H': 23.1, 'H+': 40.5, 'Frost Line': 112, 'Limit': 340})

# Blue-White

db.insert({'type': 'A0 IV', 'lum': 156, 'mass': 6, 'diameter': 0.021, 'roche limit': 0.071, 'H-': 9.38, 'H': 12.6, 'H+': 22.1, 'Frost Line': 60.6, 'Limit': 300})
db.insert({'type': 'A1 IV', 'lum': 133, 'mass': 5.6, 'diameter': 0.020, 'roche limit': 0.066, 'H-': 8.66, 'H': 11.6, 'H+': 20.1, 'Frost Line': 56, 'Limit': 280})
db.insert({'type': 'A2 IV', 'lum': 109, 'mass': 5.2, 'diameter': 0.018, 'roche limit': 0.062, 'H-': 7.84, 'H': 10.5, 'H+': 18.4, 'Frost Line': 50.7, 'Limit': 260})
db.insert({'type': 'A3 IV', 'lum': 84.6, 'mass': 4.8, 'diameter': 0.016, 'roche limit': 0.057, 'H-': 6.91, 'H': 9.26, 'H+': 16.3, 'Frost Line': 44.6, 'Limit': 240})
db.insert({'type': 'A4 IV', 'lum': 60.8, 'mass': 4.4, 'diameter': 0.015, 'roche limit': 0.052, 'H-': 5.86, 'H': 7.85, 'H+': 13.8, 'Frost Line': 37.9, 'Limit': 220})
db.insert({'type': 'A5 IV', 'lum': 37, 'mass': 4.0, 'diameter': 0.013, 'roche limit': 0.047, 'H-': 4.57, 'H': 6.13, 'H+': 10.8, 'Frost Line': 29.5, 'Limit': 200})
db.insert({'type': 'A6 IV', 'lum': 33.4, 'mass': 3.7, 'diameter': 0.013, 'roche limit': 0.044, 'H-': 4.34, 'H': 5.81, 'H+': 10.2, 'Frost Line': 28, 'Limit': 185})
db.insert({'type': 'A7 IV', 'lum': 29.8, 'mass': 3.4, 'diameter': 0.013, 'roche limit': 0.04, 'H-': 4.10, 'H': 5.49, 'H+': 9.64, 'Frost Line': 26.5, 'Limit': 170})
db.insert({'type': 'A8 IV', 'lum': 26.2, 'mass': 3.1, 'diameter': 0.0013, 'roche limit': 0.037, 'H-': 3.85, 'H': 5.15, 'H+': 9.04, 'Frost Line': 24.9, 'Limit': 155})
db.insert({'type': 'A9 IV', 'lum': 22.6, 'mass': 2.8, 'diameter': 0.0013, 'roche limit': 0.033, 'H-': 3.57, 'H': 4.78, 'H+': 8.4, 'Frost Line': 23.1, 'Limit': 140})

# White

db.insert({'type': 'F0 IV', 'lum': 19.0, 'mass': 2.5, 'diameter': 0.0013, 'roche limit': 0.03, 'H-': 3.28, 'H': 4.39, 'H+': 7.7, 'Frost Line': 21.2, 'Limit': 125})
db.insert({'type': 'F1 IV', 'lum': 17.6, 'mass': 2.4, 'diameter': 0.0013, 'roche limit': 0.029, 'H-': 3.15, 'H': 4.22, 'H+': 7.41, 'Frost Line': 20.4, 'Limit': 120})
db.insert({'type': 'F2 IV', 'lum': 16.2, 'mass': 2.3, 'diameter': 0.013, 'roche limit': 0.028, 'H-': 3.02, 'H': 4.05, 'H+': 7.11, 'Frost Line': 19.6, 'Limit': 115})
db.insert({'type': 'F3 IV', 'lum': 14.8, 'mass': 2.2, 'diameter': 0.013, 'roche limit': 0.026, 'H-': 2.89, 'H': 3.87, 'H+': 6.79, 'Frost Line': 18.7, 'Limit': 110})
db.insert({'type': 'F4 IV', 'lum': 13.4, 'mass': 2.1, 'diameter': 0.013, 'roche limit': 0.025, 'H-': 2.75, 'H': 3.68, 'H+': 6.47, 'Frost Line': 17.8, 'Limit': 105})
db.insert({'type': 'F5 IV', 'lum': 12, 'mass': 2.0, 'diameter': 0.012, 'roche limit': 0.024, 'H-': 2.6, 'H': 3.48, 'H+': 6.12, 'Frost Line': 16.8, 'Limit': 100})
db.insert({'type': 'F6 IV', 'lum': 10.9, 'mass': 1.95, 'diameter': 0.012, 'roche limit': 0.023, 'H-': 2.48, 'H': 3.32, 'H+': 5.83, 'Frost Line': 16, 'Limit': 98})
db.insert({'type': 'F7 IV', 'lum': 9.8, 'mass': 1.9, 'diameter': 0.012, 'roche limit': 0.023, 'H-': 2.35, 'H': 3.15, 'H+': 5.53, 'Frost Line': 15.2, 'Limit': 95})
db.insert({'type': 'F8 IV', 'lum': 8.7, 'mass': 1.85, 'diameter': 0.0012, 'roche limit': 0.022, 'H-': 2.22, 'H': 2.97, 'H+': 5.21, 'Frost Line': 14.3, 'Limit': 93})
db.insert({'type': 'F9 IV', 'lum': 7.6, 'mass': 1.8, 'diameter': 0.0012, 'roche limit': 0.022, 'H-': 2.07, 'H': 2.77, 'H+': 4.87, 'Frost Line': 13.4, 'Limit': 90})

# Yellow

db.insert({'type': 'G0 IV', 'lum': 6.5, 'mass': 1.75, 'diameter': 0.0012, 'roche limit': 0.021, 'H-': 1.92, 'H': 2.57, 'H+': 4.5, 'Frost Line': 12.5, 'Limit': 88})
db.insert({'type': 'G1 IV', 'lum': 6.18, 'mass': 1.8, 'diameter': 0.0012, 'roche limit': 0.022, 'H-': 1.87, 'H': 2.5, 'H+': 4.39, 'Frost Line': 12.1, 'Limit': 90})
db.insert({'type': 'G2 IV', 'lum': 5.86, 'mass': 1.85, 'diameter': 0.013, 'roche limit': 0.022, 'H-': 1.82, 'H': 2.44, 'H+': 4.28, 'Frost Line': 11.8, 'Limit': 93})
db.insert({'type': 'G3 IV', 'lum': 5.54, 'mass': 1.9, 'diameter': 0.013, 'roche limit': 0.023, 'H-': 1.77, 'H': 2.37, 'H+': 4.16, 'Frost Line': 11.5, 'Limit': 95})
db.insert({'type': 'G4 IV', 'lum': 5.22, 'mass': 1.95, 'diameter': 0.013, 'roche limit': 0.023, 'H-': 1.72, 'H': 2.3, 'H+': 4.04, 'Frost Line': 11.1, 'Limit': 98})
db.insert({'type': 'G5 IV', 'lum': 4.9, 'mass': 2.0, 'diameter': 0.013, 'roche limit': 0.024, 'H-': 1.67, 'H': 2.23, 'H+': 3.91, 'Frost Line': 10.8, 'Limit': 100})
db.insert({'type': 'G6 IV', 'lum': 4.86, 'mass': 2.06, 'diameter': 0.014, 'roche limit': 0.025, 'H-': 1.66, 'H': 2.22, 'H+': 3.89, 'Frost Line': 10.7, 'Limit':103})
db.insert({'type': 'G7 IV', 'lum': 4.81, 'mass': 2.12, 'diameter': 0.014, 'roche limit': 0.025, 'H-': 1.65, 'H': 2.21, 'H+': 3.87, 'Frost Line': 10.7, 'Limit': 106})
db.insert({'type': 'G8 IV', 'lum': 4.77, 'mass': 2.18, 'diameter': 0.0015, 'roche limit': 0.026, 'H-': 1.64, 'H': 2.2, 'H+': 3.86, 'Frost Line': 10.6, 'Limit': 109})
db.insert({'type': 'G9 IV', 'lum': 4.72, 'mass': 2.24, 'diameter': 0.0015, 'roche limit': 0.027, 'H-': 1.63, 'H': 2.19, 'H+': 2.84, 'Frost Line': 10.6, 'Limit': 112})

# Orange

db.insert({'type': 'K0 IV', 'lum': 4.67, 'mass': 2.3, 'diameter': 0.0016, 'roche limit': 0.028, 'H-': 1.63, 'H': 2.18, 'H+': 3.82, 'Frost Line': 10.5, 'Limit': 115})
db.insert({'type': 'K1 IV', 'lum': 4.63, 'mass': 2.36, 'diameter': 0.0016, 'roche limit': 0.029, 'H-': 1.62, 'H': 2.17, 'H+': 3.8, 'Frost Line': 10.5, 'Limit': 118})

# Main Sequence Stars (Luminosity Class V)

# Blue-White

db.insert({'type': 'O0 V', 'lum': 1240000, 'mass': 100, 'diameter': 0.093, 'roche limit': 1.175, 'H-': 835, 'H': 1118, 'H+': 1965, 'Frost Line': -1, 'Limit': 5000})
db.insert({'type': 'O1 V', 'lum': 994000, 'mass': 97.5, 'diameter': 0.089, 'roche limit': 1.146, 'H-': 748, 'H': 1001, 'H+': 1759, 'Frost Line': -1, 'Limit': 4875})
db.insert({'type': 'O2 V', 'lum': 795000, 'mass': 95, 'diameter': 0.083, 'roche limit': 1.117, 'H-': 669, 'H': 875, 'H+': 1492, 'Frost Line': -1, 'Limit': 4750})
db.insert({'type': 'O3 V', 'lum': 634000, 'mass': 92.5, 'diameter': 0.079, 'roche limit': 1.087, 'H-': 597, 'H': 799, 'H+': 1405, 'Frost Line': -1, 'Limit': 4625})
db.insert({'type': 'O4 V', 'lum': 504000, 'mass': 90, 'diameter': 0.075, 'roche limit': 1.058, 'H-': 532, 'H': 713, 'H+': 1253, 'Frost Line': -1, 'Limit': 4500})
db.insert({'type': 'O5 V', 'lum': 398000, 'mass': 60, 'diameter': 0.07, 'roche limit': 0.705, 'H-': 473, 'H': 633, 'H+': 1113, 'Frost Line': -1, 'Limit': 3000})
db.insert({'type': 'O6 V', 'lum': 260000, 'mass': 37, 'diameter': 0.066, 'roche limit': 0.435, 'H-': 382, 'H': 512, 'H+': 900, 'Frost Line': -1, 'Limit': 1850})
db.insert({'type': 'O7 V', 'lum': 154000, 'mass': 30, 'diameter': 0.061, 'roche limit': 0.353, 'H-': 294, 'H': 394, 'H+': 692, 'Frost Line': -1, 'Limit': 1500})
db.insert({'type': 'O8 V', 'lum': 99100, 'mass': 23, 'diameter': 0.056, 'roche limit': 0.271, 'H-': 238, 'H': 316, 'H+': 556, 'Frost Line': -1, 'Limit': 1150})
db.insert({'type': 'O9 V', 'lum': 57600, 'mass': 20, 'diameter': 0.052, 'roche limit': 0.235, 'H-': 180, 'H': 245, 'H+': 424, 'Frost Line': -1, 'Limit': 1000})

# Blue-White

db.insert({'type': 'B0 V', 'lum': 36200, 'mass': 17.5, 'diameter': 0.0047, 'roche limit': 0.206, 'H-': 143, 'H': 192, 'H+': 336, 'Frost Line': -1, 'Limit': 875})
db.insert({'type': 'B1 V', 'lum': 19400, 'mass': 14.2, 'diameter': 0.0042, 'roche limit': 0.167, 'H-': 104, 'H': 140, 'H+': 246, 'Frost Line': 676, 'Limit': 710})
db.insert({'type': 'B2 V', 'lum': 9360, 'mass': 10.9, 'diameter': 0.0035, 'roche limit': 0.129, 'H-': 72, 'H': 97, 'H+': 171, 'Frost Line': 470, 'Limit': 545})
db.insert({'type': 'B3 V', 'lum': 4890, 'mass': 7.6, 'diameter': 0.031, 'roche limit': 0.09, 'H-': 53, 'H': 71, 'H+': 124, 'Frost Line': 340, 'Limit': 380})
db.insert({'type': 'B4 V', 'lum': 2290, 'mass': 6.7, 'diameter': 0.026, 'roche limit': 0.079, 'H-': 36, 'H': 49, 'H+': 85, 'Frost Line': 233, 'Limit': 335})
db.insert({'type': 'B5 V', 'lum': 1160, 'mass': 5.9, 'diameter': 0.021, 'roche limit': 0.07, 'H-': 26, 'H': 35, 'H+': 61, 'Frost Line': 166, 'Limit': 295})
db.insert({'type': 'B6 V', 'lum': 692, 'mass': 5.2, 'diameter': 0.02, 'roche limit': 0.062, 'H-': 20, 'H': 27, 'H+': 47, 'Frost Line': 128, 'Limit': 260})
db.insert({'type': 'B7 V', 'lum': 404, 'mass': 4.5, 'diameter': 0.019, 'roche limit': 0.053, 'H-': 16, 'H': 21, 'H+': 36, 'Frost Line': 97.5, 'Limit': 225})
db.insert({'type': 'B8 V', 'lum': 211, 'mass': 4.1, 'diameter': 0.018, 'roche limit': 0.049, 'H-': 11, 'H': 15, 'H+': 26, 'Frost Line': 70.5, 'Limit': 205})
db.insert({'type': 'B9 V', 'lum': 119, 'mass': 3.8, 'diameter': 0.016, 'roche limit': 0.045, 'H-': 8.2, 'H': 11, 'H+': 20, 'Frost Line': 52.9, 'Limit': 190})

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

# Subdwarf Stars (Luminosity Class VI)

# White

db.insert({'type': 'F5 VI', 'lum': 0.977, 'mass': 0.8, 'diameter': 0.0053, 'roche limit': 0.0094, 'H-': 0.75, 'H': 1, 'H+': 1.75, 'Frost Line': 4.8, 'Limit': 40})
db.insert({'type': 'F6 VI', 'lum': 0.846, 'mass': 0.76, 'diameter': 0.0052, 'roche limit': 0.009, 'H-': 0.69, 'H': 0.03, 'H+': 1.63, 'Frost Line': 4.46, 'Limit': 38})
db.insert({'type': 'F7 VI', 'lum': 0.715, 'mass': 0.72, 'diameter': 0.0051, 'roche limit': 0.0085, 'H-': 0.64, 'H': 0.86, 'H+': 1.5, 'Frost Line': 4.11, 'Limit': 36})
db.insert({'type': 'F8 VI', 'lum': 0.584, 'mass': 0.68, 'diameter': 0.005, 'roche limit': 0.008, 'H-': 0.58, 'H': 0.78, 'H+': 1.35, 'Frost Line': 3.71, 'Limit': 34})
db.insert({'type': 'F9 VI', 'lum': 0.453, 'mass': 0.64, 'diameter': 0.0049, 'roche limit': 0.0076, 'H-': 0.51, 'H': 0.68, 'H+': 1.19, 'Frost Line': 3.27, 'Limit': 32})

# Yellow

db.insert({'type': 'G0 VI', 'lum': 0.322, 'mass': 0.6, 'diameter': 0.0048, 'roche limit': 0.0071, 'H-': 0.43, 'H': 0.57, 'H+': 1, 'Frost Line': 2.76, 'Limit': 30})
db.insert({'type': 'G1 VI', 'lum': 0.295, 'mass': 0.586, 'diameter': 0.0043, 'roche limit': 0.0069, 'H-': 0.41, 'H': 0.55, 'H+': 0.96, 'Frost Line': 2.64, 'Limit': 29})
db.insert({'type': 'G2 VI', 'lum': 0.268, 'mass': 0.571, 'diameter': 0.0039, 'roche limit': 0.0068, 'H-': 0.39, 'H': 0.52, 'H+': 0.91, 'Frost Line': 2.52, 'Limit': 29})
db.insert({'type': 'G3 VI', 'lum': 0.24, 'mass': 0.557, 'diameter': 0.0035, 'roche limit': 0.0066, 'H-': 0.37, 'H': 0.5, 'H+': 0.87, 'Frost Line': 2.38, 'Limit': 28})
db.insert({'type': 'G4 VI', 'lum': 0.213, 'mass': 0.542, 'diameter': 0.003, 'roche limit': 0.0064, 'H-': 0.35, 'H': 0.47, 'H+': 0.82, 'Frost Line': 2.24, 'Limit': 27})
db.insert({'type': 'G5 VI', 'lum': 0.186, 'mass': 0.528, 'diameter': 0.0026, 'roche limit': 0.0062, 'H-': 0.33, 'H': 0.44, 'H+': 0.76, 'Frost Line': 2.1, 'Limit': 26})
db.insert({'type': 'G6 VI', 'lum': 0.172, 'mass': 0.508, 'diameter': 0.0025, 'roche limit': 0.006, 'H-': 0.31, 'H': 0.42, 'H+': 0.73, 'Frost Line': 2.02, 'Limit': 25})
db.insert({'type': 'G7 VI', 'lum': 0.158, 'mass': 0.489, 'diameter': 0.0023, 'roche limit': 0.0058, 'H-': 0.3, 'H': 0.4, 'H+': 0.7, 'Frost Line': 1.93, 'Limit': 24})
db.insert({'type': 'G8 VI', 'lum': 0.145, 'mass': 0.469, 'diameter': 0.0022, 'roche limit': 0.0056, 'H-': 0.29, 'H': 0.39, 'H+': 0.67, 'Frost Line': 1.85, 'Limit': 23})
db.insert({'type': 'G9 VI', 'lum': 0.131, 'mass': 0.45, 'diameter': 0.0021, 'roche limit': 0.0053, 'H-': 0.27, 'H': 0.37, 'H+': 0.64, 'Frost Line': 1.76, 'Limit': 22})

# Orange

db.insert({'type': 'K0 VI', 'lum': 0.117, 'mass': 0.43, 'diameter': 0.0019, 'roche limit': 0.0051, 'H-': 0.26, 'H': 0.35, 'H+': 0.61, 'Frost Line': 1.66, 'Limit': 21})
db.insert({'type': 'K1 VI', 'lum': 0.099, 'mass': 0.41, 'diameter': 0.0018, 'roche limit': 0.0049, 'H-': 0.24, 'H': 0.32, 'H+': 0.56, 'Frost Line': 1.53, 'Limit': 20})
db.insert({'type': 'K2 VI', 'lum': 0.081, 'mass': 0.39, 'diameter': 0.0017, 'roche limit': 0.0046, 'H-': 0.22, 'H': 0.29, 'H+': 0.5, 'Frost Line': 1.38, 'Limit': 19})
db.insert({'type': 'K3 VI', 'lum': 0.062, 'mass': 0.37, 'diameter': 0.0016, 'roche limit': 0.0044, 'H-': 0.19, 'H': 0.26, 'H+': 0.44, 'Frost Line': 1.21, 'Limit': 18})
db.insert({'type': 'K4 VI', 'lum': 0.043, 'mass': 0.35, 'diameter': 0.0016, 'roche limit': 0.0042, 'H-': 0.16, 'H': 0.22, 'H+': 0.37, 'Frost Line': 1.01, 'Limit': 17})
db.insert({'type': 'K5 VI', 'lum': 0.025, 'mass': 0.33, 'diameter': 0.0015, 'roche limit': 0.0039, 'H-': 0.13, 'H': 0.17, 'H+': 0.28, 'Frost Line': 0.77, 'Limit': 16})
db.insert({'type': 'K6 VI', 'lum': 0.0222, 'mass': 0.295, 'diameter': 0.0013, 'roche limit': 0.0035, 'H-': 0.12, 'H': 0.16, 'H+': 0.26, 'Frost Line': 0.73, 'Limit': 15})
db.insert({'type': 'K7 VI', 'lum': 0.0194, 'mass': 0.26, 'diameter': 0.0012, 'roche limit': 0.0031, 'H-': 0.11, 'H': 0.15, 'H+': 0.25, 'Frost Line': 0.68, 'Limit': 13})
db.insert({'type': 'K8 VI', 'lum': 0.0166, 'mass': 0.224, 'diameter': 0.0011, 'roche limit': 0.0027, 'H-': 0.10, 'H': 0.14, 'H+': 0.23, 'Frost Line': 0.63, 'Limit': 11})
db.insert({'type': 'K9 VI', 'lum': 0.0138, 'mass': 0.189, 'diameter': 0.001, 'roche limit': 0.0021, 'H-': 0.09, 'H': 0.12, 'H+': 0.21, 'Frost Line': 0.57, 'Limit': 9.5})

# Red

db.insert({'type': 'M0 VI', 'lum': 0.11, 'mass': 0.154, 'diameter': 0.0009, 'roche limit': 0.0018, 'H-': 0.08, 'H': 0.1, 'H+': 0.19, 'Frost Line': 0.51, 'Limit': 7.7})
db.insert({'type': 'M1 VI', 'lum': 0.0092, 'mass': 0.144, 'diameter': 0.0008, 'roche limit': 0.0017, 'H-': 0.07, 'H': 0.09, 'H+': 0.17, 'Frost Line': 0.47, 'Limit': 7.2})
db.insert({'type': 'M2 VI', 'lum': 0.0074, 'mass': 0.134, 'diameter': 0.0008, 'roche limit': 0.0016, 'H-': 0.06, 'H': 0.08, 'H+': 0.15, 'Frost Line': 0.42, 'Limit': 6.7})
db.insert({'type': 'M3 VI', 'lum': 0.0056, 'mass': 0.124, 'diameter': 0.0007, 'roche limit': 0.0015, 'H-': 0.05, 'H': 0.07, 'H+': 0.13, 'Frost Line': 0.37, 'Limit': 6.2})
db.insert({'type': 'M4 VI', 'lum': 0.0038, 'mass': 0.114, 'diameter': 0.0006, 'roche limit': 0.0014, 'H-': 0.05, 'H': 0.06, 'H+': 0.11, 'Frost Line': 0.3, 'Limit': 5.7})
db.insert({'type': 'M5 VI', 'lum': 0.002, 'mass': 0.104, 'diameter': 0.0006, 'roche limit': 0.0013, 'H-': 0.04, 'H': 0.05, 'H+': 0.08, 'Frost Line': 0.22, 'Limit': 5.2})
db.insert({'type': 'M6 VI', 'lum': 0.0015, 'mass': 0.093, 'diameter': 0.0006, 'roche limit': 0.0011, 'H-': 0.03, 'H': 0.04, 'H+': 0.07, 'Frost Line': 0.19, 'Limit': 4.7})
db.insert({'type': 'M7 VI', 'lum': 0.001, 'mass': 0.092, 'diameter': 0.0006, 'roche limit': 0.0011, 'H-': 0.03, 'H': 0.04, 'H+': 0.06, 'Frost Line': 0.16, 'Limit': 4.6})
db.insert({'type': 'M8 VI', 'lum': 0.0009, 'mass': 0.091, 'diameter': 0.0006, 'roche limit': 0.0011, 'H-': 0.02, 'H': 0.03, 'H+': 0.05, 'Frost Line': 0.15, 'Limit': 4.6})
db.insert({'type': 'M9 VI', 'lum': 0.0007, 'mass': 0.09, 'diameter': 0.0006, 'roche limit': 0.0011, 'H-': 0.02, 'H': 0.03, 'H+': 0.04, 'Frost Line': 0.13, 'Limit': 4.5})

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

# T-Class Methane Dwarfs

db.insert({'type': 'T0', 'lum': 0.000020, 'mass': 0.06, 'diameter': 0.00071, 'roche limit': 0.00071, 'H-': 0.003, 'H': 0.005, 'H+': 0.008, 'Frost Line': 0.021, 'Limit': 3.0})
db.insert({'type': 'T1', 'lum': 0.000015, 'mass': 0.0057, 'diameter': 0.00067, 'roche limit': 0.00067, 'H-': 0.003, 'H': 0.004, 'H+': 0.007, 'Frost Line': 0.018, 'Limit': 2.9})
db.insert({'type': 'T2', 'lum': 0.000009, 'mass': 0.054, 'diameter': 0.00064, 'roche limit': 0.00064, 'H-': 0.002, 'H': 0.003, 'H+': 0.005, 'Frost Line': 0.015, 'Limit':2.7})
db.insert({'type': 'T3', 'lum': 0.000006, 'mass': 0.0524, 'diameter': 0.00062, 'roche limit': 0.00062, 'H-': 0.002, 'H': 0.003, 'H+': 0.004, 'Frost Line': 0.012, 'Limit': 2.6})
db.insert({'type': 'T4', 'lum': 0.000004, 'mass': 0.0498, 'diameter': 0.00059, 'roche limit': 0.00059, 'H-': 0.001, 'H': 0.002, 'H+': 0.004, 'Frost Line': 0.010, 'Limit': 2.5})
db.insert({'type': 'T5', 'lum': 0.000003, 'mass': 0.0472, 'diameter': 0.00056, 'roche limit': 0.00056, 'H-': 0.001, 'H': 0.002, 'H+': 0.003, 'Frost Line': 0.009, 'Limit': 2.4})
db.insert({'type': 'T6', 'lum': 0.000002, 'mass': 0.0446, 'diameter': 0.00053, 'roche limit': 0.00053, 'H-': 0.001, 'H': 0.001, 'H+': 0.003, 'Frost Line': 0.007, 'Limit': 2.3})
db.insert({'type': 'T7', 'lum': 0.000001, 'mass': 0.042, 'diameter': 0.00050, 'roche limit': 0.0004, 'H-': 0.001, 'H': 0.001, 'H+': 0.002, 'Frost Line': 0.005, 'Limit': 2.1})
db.insert({'type': 'T8', 'lum': 0, 'mass': 0.0395, 'diameter': 0.00047, 'roche limit': 0.00047, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.002, 'Limit': 2.0})
db.insert({'type': 'T9', 'lum': 0, 'mass': 0.0372, 'diameter': 0.00044, 'roche limit': 0.00044, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.001, 'Limit': 1.9})

# T-Class Ultra-Cool Dwarfs

db.insert({'type': 'Y0', 'lum': 0, 'mass': 0.035, 'diameter': 0.00039, 'roche limit': 0.00043, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.00079, 'Limit': 1.7})
db.insert({'type': 'Y1', 'lum': 0, 'mass': 0.033, 'diameter': 0.00038, 'roche limit': 0.00042, 'H-': 0., 'H': 0, 'H+': 0, 'Frost Line': 0.00078, 'Limit': 1.6})
db.insert({'type': 'Y2', 'lum': 0, 'mass': 0.031, 'diameter': 0.00037, 'roche limit': 0.00041, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.00076, 'Limit': 1.5})
db.insert({'type': 'Y3', 'lum': 0, 'mass': 0.029, 'diameter': 0.000637, 'roche limit': 0.00040, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.00074, 'Limit': 1.4})
db.insert({'type': 'Y4', 'lum': 0, 'mass': 0.027, 'diameter': 0.00036, 'roche limit': 0.00040, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.00072, 'Limit': 1.3})
db.insert({'type': 'Y5', 'lum': 0, 'mass': 0.025, 'diameter': 0.00035, 'roche limit': 0.00039, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.00071, 'Limit': 1.2})
db.insert({'type': 'Y6', 'lum': 0, 'mass': 0.02, 'diameter': 0.00034, 'roche limit': 0.00038,'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.0007, 'Limit': 1.0})
db.insert({'type': 'Y7', 'lum': 0, 'mass': 0.0175, 'diameter': 0.00034, 'roche limit': 0.00038, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.00068, 'Limit': 0.9})
db.insert({'type': 'Y8', 'lum': 0, 'mass': 0.0150, 'diameter': 0.00033, 'roche limit': 0.00037, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.00067, 'Limit': 0.8})
db.insert({'type': 'Y9', 'lum': 0, 'mass': 0.0125, 'diameter': 0.00032, 'roche limit': 0.00036, 'H-': 0, 'H': 0, 'H+': 0, 'Frost Line': 0.00065, 'Limit': 0.7})

print('Loaded ' + str(len(db)) + ' items.')