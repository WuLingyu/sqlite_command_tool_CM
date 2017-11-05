import argparse

def provide_help():
    print "provide help"

def command_tool_mode():
    print "command tool mode"

def main():
    # create parser
    descStr = """
    This program provides some helpful functions for ZW group in CM-GZ
    """
    parser = argparse.ArgumentParser(description=descStr)
    
    # add a mutually exclusive group of arguments
    group = parser.add_mutually_exclusive_group()
    
    # add expected arguments
    group.add_argument('--help',action="provide_help", required=False)
    group.add_argument('--s', action="command_tool_mode", required=False)
    
    # parse args
    args = parser.parse_args()
    



if __name__ == '__main__':
    main()