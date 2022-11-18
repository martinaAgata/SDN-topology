from pox.core import core
from pox.lib.revent import EventMixin
import pox.forwarding.l2_learning as l2_learning
import pox.lib.packet as pkt

log = core.getLogger()


#
# SOME HIGHLIGHTS FROM:
# https://homepages.dcc.ufmg.br/~mmvieira/cc/OpenFlow%20Tutorial%20-%20OpenFlow%20Wiki.htm#ofp_match_class
#
# ofp_match describe packet header fields and an input port to match on.
#
# ofp_flow_mod instructs a switch to install a flow table entry (FTE).
# FTEs match some fields of incoming packets, and execute some list of
# actions on matching packets. The match is described by an ofp_match.
#


def discardDestinationPort80(event):
    # Creating matches for matching packets with custom specifications.

    # TCP filter match
    tcp_match = of.ofp_match()
    # Specify protocol of layers in order
    tcp_match.dl_type = pkt.ethernet.IP_TYPE
    tcp_match.nw_proto = pkt.ipv4.TCP_PROTOCOL
    # Then, specify port
    tcp_match.tp_dst = 80
    # To instruct the switch to match the custom specifications
    tcp_msg_port = of.ofp_flow_mod(match=tcp_match)

    # UDP filter match
    udp_match = of.ofp_match()
    udp_match.dl_type = pkt.ethernet.IP_TYPE
    udp_match.nw_proto = pkt.ipv4.UDP_PROTOCOL
    udp_match.tp_dst = 80
    udp_msg_port = of.ofp_flow_mod(match=udp_match)

    # Sending OpenFlow messages to the switch
    event.connection.send(tcp_msg_port)
    event.connection.send(udp_msg_port)


class Firewall(EventMixin):

    def __init__(self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp(self, event):
        discardDestinationPort80(event)

    def launch():
        # Starting the Firewall module
        l2_learning.launch()
        core.registerNew(Firewall)
