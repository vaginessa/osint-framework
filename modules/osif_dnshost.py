from sploitkit import Module, Config, Option
import requests
from terminaltables import SingleTable

class dnsHost(Module):
    """ This module find DNS Host information
    Author:  laet4x
    Version: 1.0
    """
    config = Config({
        Option(
            'DOMAIN',
            "Provide your target Domain",
            True,
        ): str("google.com"),
    })    

    #path = "auxiliary/dns"

    def run(self):
        domain = self.config.option('DOMAIN').value
        print("\n"" Analyzing '%s'..." % (domain))
        request = requests.get("https://api.hackertarget.com/hostsearch/?q=" + domain)
        res = request.text
        print("\n", res)
        

