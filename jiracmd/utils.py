from tabulate import tabulate

def output_table(obj, sort_by=None, reverse=False):
    if sort_by:
        obj = sorted(obj, key = lambda x: x[sort_by], reverse=reverse)
    table = tabulate(obj, headers="keys")
    print(table)
    return table

def yaml_multiline_string_pipe(dumper, data):
    if len(data.splitlines()) > 1:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style="|")
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

