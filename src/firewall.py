from pox.core import core
from pox.lib.revent import EventMixin
import pox.forwarding.l2_learning as l2_learning


log = core.getLogger()


class Firewall(EventMixin):

    def __init__(self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    # def _handle_ConnectionUp(self, event):
        # Add your logic here ...

    def launch():
        # Starting the Firewall module
        l2_learning.launch()
        core.registerNew(Firewall)
