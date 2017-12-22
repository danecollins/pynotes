import argparse

# create the parser object
parser = argparse.ArgumentParser(description='This description is displayed immediately after the usage line in the help')

# create a boolean option that will be true is used, false if missing
parser.add_argument('-e', '--exclude', help='exclude internal users', action='store_true')

# create an argument that can have one of 2 values if specified, legal values can be None, 'opta', 'optb'
parser.add_argument('-f', '--filter', help='field to filter on: opta or optb', choices=['opta', 'optb'])

# create an argument that can have a value of None or any string
parser.add_argument('-s', '--string', help='string to match to')

# create an argument with one required string value
parser.add_argument('-x', '--exact', required=True, help='match exactly')

# argument that is not a switch.  Can be left out which will cause default to be used
# if specified can only be 1 name
# parser.add_argument('filename', nargs='?', help='file name to store to',
#                     default='data.df')

# argument that is not a switch.  Can be left out which will cause default to be used
# due to '*' can specify multiple names and .filename will be a list
parser.add_argument('filename', nargs='*', help='file name to store to',
                    default=['data.df'])

parsedargs = parser.parse_args()
print(parsedargs)

print('Exclude =', parsedargs.exclude)
print('Exact =', parsedargs.exact)
print('String =', parsedargs.string)
print('Filter =', parsedargs.filter)
print('Filename =', parsedargs.filename)

# parser.print_help() - generate usage message
