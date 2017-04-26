#!/usr/bin/python
# Copyright (C) 2017 Repsejnworb.
# All rights reserved.
"""noname main."""

import argparse
import logging
import os
import socket
import sys

from noname import constants
from noname import gameclient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

x = 0
y = 1000
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)


def is_valid_ipv4_address(address):
    try:
        socket.inet_aton(address)
        return True
    except socket.error:
        return False


def is_valid_port(port):
    if port in range(0, 65535):
        return True
    else:
        return False


def exit(code, message=None):
    if message:
        print message
    sys.exit(code)


def main():
    """Main entrypoint for service."""

    p = argparse.ArgumentParser()
    p.add_argument("-l", "--loglevel", default="info")
    p.add_argument("--width", default=constants.DEFAULT_WIDTH)
    p.add_argument("--height", default=constants.DEFAULT_HEIGHT)
    p.add_argument("--fps", default=constants.DEFAULT_FPS)
    p.add_argument("--server", default=constants.DEFAULT_SERVER)

    options = p.parse_args()

    if not options.server:
        server_ip = raw_input("Server IP: ")
        if not is_valid_ipv4_address(server_ip):
            exit(1, "'%s' is not a valid IP address" % server_ip)

        server_port = raw_input("Server port: ")
        if not is_valid_port(server_port):
            exit(1, "'%s' is not a valid TCP port" % server_port)
    else:
        server_ip, server_port = options.server.split(":")
        server_port = int(server_port)
        if not is_valid_ipv4_address(server_ip):
            exit(1, "'%s' is not a valid IP address" % server_ip)
        if not is_valid_port(server_port):
            exit(1, "'%s' is not a valid TCP port" % server_port)

    game_instance = gameclient.GameClient((server_ip, server_port),
                                          options.width, options.height,
                                          options.fps)
    game_instance.add_player()
    game_instance.run()  # NOTE: HANGING CALL
    exit(0, "Quit successful")

if __name__ == "__main__":
    main()
