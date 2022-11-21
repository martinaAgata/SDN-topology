from __future__ import print_function
import json

class Rule(object):
    def __init__(self, protocol = None, src_host = None, src_port = None, dst_host = None, dst_port= None):
        self.protocol = protocol
        self.src_host = src_host
        self.src_port = src_port
        self.dst_host = dst_host
        self.dst_port = dst_port

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "Rule {{ protocol={}, src_host={}, src_port={}, dst_port={}, dst_port={} }}".format(
            self.protocol,
            self.src_host,
            self.src_port,
            self.dst_host,
            self.dst_port,
        )

class Policies(object):
    def __init__(self, switch=None, rules=[]):
        self.switch = switch
        self.rules = self._create_rules(rules)

    def _create_rules(self, rules):
        mapped_rules = []
        for rule in rules:
            mapped_rules.append(Rule(**rule))
        
        return mapped_rules

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "Policies {{ rules={} }}".format(
            ["{}".format(str(x)) for x in self.rules],
        )

def get_policies():
    policies = None
    with open('./policies.json', 'r') as outfile:
        j = json.load(outfile)
        policies = Policies(**j)
        print(policies)
    
    return policies

