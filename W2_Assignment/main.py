import argparse
import logging
from utils.command_handler import CommandHandler
from utils.command_parser import CommandParser

# TODO 1-1: Use argparse to parse the command line arguments (verbose and log_file).
# TODO 1-2: Set up logging and initialize the logger object.

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="Enable verbose argument")
parser.add_argument("--log_path", type=str, default="file_explorer.log")
args = parser.parse_args()

logging.basicConfig(filename=args.log_path, level=logging.INFO)

command_parser = CommandParser(verbose=arg.verbose)
handler = CommandHandler(command_parser)

while True:
    command = input(">> ")
    handler.execute(command)
    
