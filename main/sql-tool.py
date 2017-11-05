import argparse

def command_tool_mode():
    while 1:
        input = raw_input("command >> ")

def main():
    # create parser
    descStr = """
    This program provides some helpful functions for ZW group in CM-GZ
    """
    parser = argparse.ArgumentParser(description=descStr)
    
    # add a mutually exclusive group of arguments
    group = parser.add_mutually_exclusive_group()
    
    # add expected arguments
    group.add_argument('-s', action="store_true",
                       help="shell mode",required=False)
    # group.add_argument('--s', action="command_tool_mode", required=False)
    
    # parse args
    args = parser.parse_args()
    
    if args.s:
        try:
            command_tool_mode()
        except KeyboardInterrupt:
            print("Goodbye~")
    else:
        parser.print_help()
    



if __name__ == '__main__':
    main()