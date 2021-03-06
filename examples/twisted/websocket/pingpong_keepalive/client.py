###############################################################################
##
##  Copyright (C) 2011-2013 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

import sys

from twisted.internet import reactor
from twisted.python import log

from autobahn.twisted.websocket import WebSocketClientFactory, \
                                       WebSocketClientProtocol, \
                                       connectWS


if __name__ == '__main__':

   log.startLogging(sys.stdout)

   if len(sys.argv) < 2:
      print("Need the WebSocket server address, i.e. ws://localhost:9000")
      sys.exit(1)

   factory = WebSocketClientFactory(sys.argv[1], debug = True)
   factory.protocol = WebSocketClientProtocol
   connectWS(factory)

   reactor.run()
