import sys
import os

from help import help
from generate import generate
from create import create
from start import start

args = sys.argv
args_count = len(args)

if args_count == 1:
    print('Incorrect command')
    help()
else:
    command = args[1]
    if(command == 'help'):
        help()
    elif(command == 'generate'):
        generate()
    elif(command == 'create'):
        create()
    elif(command == 'start'):
        start()
    else:
        print('Incorrect command')
        help()

# print(sys.argv)
# print(os.getcwd())