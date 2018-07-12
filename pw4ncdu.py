from optparse import OptionParser
import subprocess
import sys
import os
import json

version = "0.0.1"

def build_statement_and_exec(options):
    # This function is to build the NCDU statements from running params
    # Example: ncdu -xo- /home/Nova/Downloads/dosbox
    path = options.path # Path to be scanned
    command_assets = []
    command_assets.append("ncdu -xo- ")
    command_assets.append(path)
    #print(command_assets)
    command_string = ' '.join(command_assets)
    results = subprocess.getoutput(command_string)
    return results

file_array = [] # The array for storing file data
def rescan(json):
    if type(json) == dict: # File information
        file_array.append(json)
    elif type(json) == list:
        for items in json:
            rescan(items)
    return file_array

def parse_ncdu_results(results):
    j = json.loads(results)
    print("The PATH you are scanning for is %s" % j[3][0]['name'])
    sort_dict = {} # For sort the files
    for item in rescan(j):
        if "name" in item:
            sort_dict["name"] = item['name']
            #print(item['name'],item['asize'])

def main():
    parser = OptionParser()
    usage = "%prog"
    # set up the parser object
    parser = OptionParser(usage, version='%prog ' + version)
    parser.add_option("-p", "--path", dest="path",
                      help="Scan the specified PATH")
    parser.add_option("-e", "--exclude", dest="exclude",
                      help="Exclude specific file extensions")

    (options, args) = parser.parse_args()
    json_results = build_statement_and_exec(options)
    parse_ncdu_results(json_results)

if __name__ == "__main__":
    main()
