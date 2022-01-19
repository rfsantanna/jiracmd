from tabulate import tabulate

def output_table(obj):
    table = tabulate(obj, headers="keys")
    print(table)
    return table

    
