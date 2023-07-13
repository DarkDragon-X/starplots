# File: ReadFile.py

# Description: This program reads the data from the bsc5.txt file and formats it into a csv file

# Name:Nipun Nagendra

# UT EID:nn8684

# Date: 6/27/2023

import sys
def main():
    key = [
        (1, 4),    
        (5, 14),   
        (15, 25),  
        (26, 31),  
        (32, 37),  
        (38, 41),  
        (42, 42),  
        (43, 43),  
        (44, 44),  
        (45, 49),  
        (50, 51),  
        (52, 60),  
        (61, 62),  
        (63, 64),  
        (65, 68),  
        (69, 69),  
        (70, 71),  
        (72, 73),  
        (74, 75),  
        (76, 77),  
        (78, 79),  
        (80, 83),  
        (84, 84),  
        (85, 86),  
        (87, 88),  
        (89, 90),  
        (91, 96),  
        (97, 102), 
        (103, 107),
        (108, 108),
        (109, 109),
        (110, 114),
        (115, 115),
        (116, 120),
        (121, 121),
        (122, 126),
        (127, 127),
        (128, 147),
        (148, 148),
        (149, 154),
        (155, 160),
        (161, 161),
        (162, 166),
        (167, 170),
        (171, 174),
        (175, 176),
        (177, 179),
        (180, 180),
        (181, 184),
        (185, 190),
        (191, 194),
        (195, 196),
        (197, 197) 
    ]
    titles = ['HR', 'Name', 'DM', 'HD', 'SAO', 'FK5', 'IRflag', 'r_IRflag', 'Multiple',
            'ADS', 'ADScomp', 'VarID', 'RAh1900', 'RAm1900', 'RAs1900', 'DE-1900',
            'DEd1900', 'DEm1900', 'DEs1900', 'RAh', 'RAm', 'RAs', 'DE-', 'DEd', 'DEm',
            'DEs', 'GLON', 'GLAT', 'Vmag', 'n_Vmag', 'u_Vmag', 'B-V', 'u_B-V', 'U-B',
            'u_U-B', 'R-I', 'n_R-I', 'SpType', 'n_SpType', 'pmRA', 'pmDE', 'n_Parallax',
            'Parallax', 'RadVel', 'n_RadVel', 'l_RotVel', 'RotVel', 'u_RotVel', 'Dmag',
            'Sep', 'MultID', 'MultCnt', 'NoteFlag']

    with open('bsc5.txt', 'r') as file:
        rows = file.readlines()

    formatted_rows = []
    for row in rows:
        formatted_row = ''
        for label_range in key:
            label = row[label_range[0] - 1 : label_range[1]].strip()
            formatted_row += label + ','
        formatted_rows.append(formatted_row[:-1]) 


    formatted_rows.insert(0, ','.join(titles))


    with open('bsc5.csv', 'w') as file:
        file.write('\n'.join(formatted_rows))

if __name__ == "__main__":
    main()
