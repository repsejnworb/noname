import importlib
import select
import socket

import errno
import pygame

from noname import sprites
from noname import constants
from noname import units


if not pygame.font:
    print "Warning, fonts disabled"
if not pygame.mixer:
    print "Warning, sound disabled"

class GameClient(object):
    """ The GameClient, drawing on the screen """

    def __init__(self, server_address, width=constants.DEFAULT_WIDTH,
                 height=constants.DEFAULT_HEIGHT, fps=constants.DEFAULT_FPS,):
        pygame.init()
        self.server_address = server_address
        self.socket = self.connect()
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.level = None
        self.players = []
        self.player = None
        self.clock = pygame.time.Clock()

    def connect(self):
        # No connection required as we are running UDP
        print "Connecting to %s:%s" % (self.server_address[0],
                                       self.server_address[1])
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setblocking(0)
        return s

    def send(self, data):
        """ Sends data to server """
        size = len(data)
        total_sent = 0

        while len(data):
            try:
                sent = self.socket.sendto(data, self.server_address)
                total_sent += sent
                data = data[sent:]
            except socket.error as e:
                if e.errno != errno.EAGAIN:
                    raise e
                yield ('w', self.socket)
        print "Sent %d number of bytes" % size

    def read(self, buf=4096):
        try:
            data, server = self.socket.recvfrom(buf)
        except socket.error as e:
            if e.args[0] == errno.EWOULDBLOCK:
                print 'EWOULDBLOCK'
            yield data

    def update(self):
        self.clock.tick(self.fps)
        self.screen.fill(0)
        self.level.draw(self.screen)
        self.draw_players()
        pygame.display.flip()

    def run(self):
        try:
            # FIXME
            # DEV SHIT REMOVE
            import time
            start = time.time()
            # DEV SHIT REMOVE

            running = True
            self.load_level(constants.DEFAULT_LEVEL)
            while running:
                print self.send("c hello")
                print self.read()
                self.update()
                for event in pygame.event.get():
                    #pygame.time.wait(500)  # dev quit
                    #return  # dev quit
                    if event.type == pygame.QUIT:
                        return

                    # IMAGE FLIP ONLY?
                    # elif event.type == pygame.KEYDOWN:
                    #    if self.is_controls_moving(event):
                    #         self.player.move(event.key)
                keys = pygame.key.get_pressed()
                print "PRESSED KEYS: ", keys
                if pygame.K_DOWN in keys:
                    print "YEP YEP"
                    print "YEP YEP"
                    print "YEP YEP"
                    print "YEP YEP"
                    print "YEP YEP"
                    print "YEP YEP"
                    print "YEP YEP"
                    print "YEP YEP"
                if self.is_controls_moving(keys):
                    self.player.move(keys)
                if (time.time() - start) >= 1:
                    running = False

        finally:
            print "closing socket"
            self.socket.close()

    def is_controls_moving(self, keys):
        if (keys[pygame.K_UP] or keys[pygame.K_DOWN] or
           keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            print "key pressed"
            return True
        else:
            return False

        #if ((event.key == pygame.K_RIGHT) or (event.key == pygame.K_LEFT) or
        #   (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN)):
        #    return True
        #else:
        #    return False

    def load_level(self, name):
        module_name = "noname.levels.%s" % name
        print "Loading level: %s" % module_name
        level_module = importlib.import_module(module_name)
        self.level = level_module.Level()
        self.level.load_sprites()

    def draw_players(self):
        for player in self.players:
            print "Sprite: %r" % player.sprite
            player.sprite.draw(self.screen)

    def add_player(self, x=0, y=0):
        single_player_metadata = {
            "name": "gary",
            "file": "Gary.png",
            "width": 32,
            "height": 32,
            "position": {
                "x": x,
                "y": y,
            },
        }
        player = units.Player(single_player_metadata["name"],
                              single_player_metadata)
        # FIXME
        if self.player is None:
            self.player = player
        self.players.append(player)


class PlayerInput(object):
    def is_moving(self):
        pass
