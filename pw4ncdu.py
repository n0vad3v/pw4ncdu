from optparse import OptionParser
from subprocess import call
import sys

version = "0.0.1"

def build_statement_and_exec(options):
    # This function is to build the NCDU statements from running params
    # Example: ncdu -xo- /home/Nova/Downloads/dosbox
    path = options.path # Path to be scanned
    command_assets = []
    command_assets.append("ncdu -xo- ")
    command_assets.append(path)
    command_string = ' '.join(command_assets)
    #results = call(command_string)
    return results

def main():
    parser = OptionParser()
    usage = "%prog"
    # set up the parser object
    parser = OptionParser(usage, version='%prog ' + version)
    parser.add_option("-p", "--path", dest="path",
                      help="Scan the specified PATH")

    (options, args) = parser.parse_args()
    #print(build_statement(options))
    print(build_statement_and_exec(options))

if __name__ == "__main__":
    main()
