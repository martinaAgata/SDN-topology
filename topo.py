from mininet.topo import Topo


class ChainTopo(Topo):
    """
    ChainTopo is a parameterizable topology; it has a variable number of
    switches forming a chain with two hosts at its ends.
    """

    def __init__(self, n):
        """
        Initializes a ChainTopo receiving a number of switches.
        """

        # Add hosts
        H1 = self.addHost('H1')
        H2 = self.addHost('H2')
        H3 = self.addHost('H3')
        H4 = self.addHost('H4')

        # Declare variables for first and last switches
        firstSwitch = None
        lastSwitch = None

        # Add switches
        for i in range(n):
            newSwitch = self.addSwitch(f"S{str(i)}")
            if lastSwitch:
                # Link switches generating a chain
                self.addLink(newSwitch, lastSwitch)
            else:
                # Saving first switch for later linking
                firstSwitch = newSwitch
            lastSwitch = newSwitch

        # Add links between switches and hosts H1 and H2
        self.addLink(H1, firstSwitch)
        self.addLink(H2, firstSwitch)

        # Add links between switches and hosts H3 and H4
        self.addLink(H3, lastSwitch)
        self.addLink(H4, lastSwitch)


topos = {'chainTopo': (lambda n: ChainTopo(n))}
