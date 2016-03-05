from routes.help import help
from routes.generate import generate
from routes.create import create
from routes.start import start
from routes.uninstall import uninstall

def router(args):
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
            create(args)
        elif(command == 'start'):
            start(args)
        elif(command == 'version'):
            print('Sanelotto 2.2')
        elif(command == 'uninstall'):
            uninstall()
        else:
            print('Incorrect command')
            help()