from pox.core import core
from pox.lib.addresses import IPAddr
from pox.lib.revent import EventMixin
from pox.lib.util import dpid_to_str
import pox.forwarding.l2_learning as l2_learning
import pox.lib.packet as pkt
import pox.openflow.libopenflow_01 as of
from policies import get_policies


#
# SOME HIGHLIGHTS FROM:
# https://homepages.dcc.ufmg.br/~mmvieira/cc/OpenFlow%20Tutorial%20-%20OpenFlow%20Wiki.htm#ofp_match_class
#
# ofp_match describes packet header fields and an input port to match on.
#
# ofp_flow_mod instructs a switch to install a flow table entry (FTE).
# FTEs match some fields of incoming packets, and execute some list of
# actions on matching packets. The match is described by an ofp_match.
#

log = core.getLogger()


class Firewall(EventMixin):

    def __init__(self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp(self, event):
        # When a connection to a switch starts, a ConnectionUp event is fired.
        log.debug("Switch %s has come up.", dpid_to_str(event.dpid))
        policies = get_policies()
        for rule in policies.rules:
            self.set_policy(event, rule)

    def set_policy(self, event, rule):
        # Creating matches for matching packets with custom specifications.
        protocols = [pkt.ipv4.TCP_PROTOCOL, pkt.ipv4.UDP_PROTOCOL]

        if rule.protocol == 'TCP':
            protocols = protocols[:1]
        
        if rule.protocol == 'UDP':
            protocols = protocols[1:]

        for protocol in protocols:
            # Instance object for matching.
            matcher = of.ofp_match()
            # Specify protocol of layers in order.
            matcher.dl_type = pkt.ethernet.IP_TYPE
            matcher.nw_proto = protocol
            
            if rule.src_host:
                matcher.nw_src = IPAddr(rule.src_host)

            if rule.src_port:
                matcher.tp_src = rule.src_port

            if rule.dst_host:
                matcher.nw_dst = IPAddr(rule.dst_host)

            if rule.dst_port:
                matcher.tp_dst = rule.dst_port

            # To instruct the switch to match the custom specifications.
            msg = of.ofp_flow_mod(match=matcher)

            log.debug("Sending message: %s", msg.show())
            # Sending OpenFlow messages to the switch.
            event.connection.send(msg)


def launch():
    # Starting the Firewall module
    l2_learning.launch()
    core.registerNew(Firewall)
