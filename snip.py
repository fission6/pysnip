from pyquery import PyQuery as pq
import urllib2
import json
import pprint


class Snip(object):
    """
    Base snip class
    """

    def __init__(self, **kwargs):
        """
        Constructor. Called in the URLconf; can contain helpful extra
        keyword arguments, and other things.
        """

        self._get_snip()

    def _get_snip(self):
        self.get_resource()
        self.snip = self.parse_response(self.response)

    def display(self):
        self.render_snip(self.snip)

    def render_snip(self, snip):
        pprint.pprint(self.snip, width=20)

    def parse_response(self, response):
        snip = response
        return snip

    def get_resource(self):
        url = self.resource
        self.response = pq(url=url)

        return self.response


class JSONSnip(Snip):

    def get_resource(self):
        resource = urllib2.urlopen(self.resource)
        self.response = json.load(resource)

        return self.response
