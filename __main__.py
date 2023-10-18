#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv

from bot import disco_ball

def TOKEN(): return os.environ['TOKEN']

def main(args):
	load_dotenv()
	db = disco_ball()
	db.run(TOKEN())
	return 0;

if __name__ == '__main__':
	sys.exit(main(sys.argv))

