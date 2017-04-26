import select
import socket


class GameServer(object):

    def __init__(self, port=4200, max_num_players=5):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(("127.0.0.1", port))

        self.read_list = [self.socket]
        self.write_list = []  # populated once clients connect

        self.players = {}

    def run(self):
        print "Running..."
        try:
            while True:
                readable, writeable, exceptional = (
                    select.select(self.read_list, self.write_list, [])
                )
                for f in readable:
                    if f is self.socket:
                        msg, addr = f.recvfrom(32)
                        print "Recieved message: %r" % msg
                        if len(msg) >= 1:
                            cmd = msg[0]
                            if cmd == "c":
                                # new connection
                                self.players[addr] = (0, 0)
                            elif cmd == "u":
                                # player movement
                                print msg
                            elif cmd == "d":
                                # disconnect
                                if addr in self.players:
                                    del self.players[addr]
                            else:
                                print "Unexpected msg %r from addr %r" % (msg,
                                                                          addr)
                for player in self.players:
                    self.socket.sendto("gameUpdate()", player)

        except KeyboardInterrupt as e:
            print "Keyboard interrupt"
            raise e

server = GameServer()
server.run()