width_copper = {
    'A': 9,  # Metal 1
    'B': 9,  # Data 2
    'C': 12,  # Buyer 3
    'D': 9,  # Metal 4
    'E': 9,  # Data 5
    'F': 12,  # Buyer 6
    'G': 9,  # Metal 7
    'H': 12,  # Data 8
    'I': 9   # Buyer 9
}

width_copper = {
    'A': 20,  # Metal 1
    'B': 9,  # Data 2
    'C': 12,  # Buyer 3
    'D': 20,  # Metal 4
    'E': 9,  # Data 5
    'F': 12,  # Buyer 6
    'G': 20,  # Metal 7
    'H': 9,  # Data 8
    'I': 12   # Buyer 9
}

for col, width in width.items():
        worksheet.set_column(col + ':' + col, width)
        
#parâmetros para passar(width)