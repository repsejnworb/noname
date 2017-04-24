#!/usr/bin/python
# Copyright (C) 2017 Repsejnworb.
# All rights reserved.
"""noname main."""

import argparse
import sys

from noname import constants
from noname import game


def main():
    """Main entrypoint for service."""

    p = argparse.ArgumentParser()
    p.add_argument("-l", "--loglevel", default="info")
    p.add_argument("--width", default=constants.DEFAULT_WIDTH)
    p.add_argument("--height", default=constants.DEFAULT_HEIGHT)

    options = p.parse_args()

    game_instance = game.Game(options.width, options.height)
    game_instance.start()
    sys.exit(0)

if __name__ == "__main__":
    main()
