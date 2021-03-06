from pyquery import PyQuery as pq
import urllib2
import json
import urllib
import pprint

registered_snips = {}


def register(cls):
    # This needs to be a bit more robust
    if hasattr(cls, 'snip_slug') and issubclass(cls, Snip):
        registered_snips[cls.snip_slug] = cls
    return cls


class SnipPluginMount(type):

    def __new__(cls, clsname, bases, attrs):
        newclass = super(cls, SnipPluginMount).__new__(cls, clsname, bases, attrs)
        register(newclass)  # here is your register function
        return newclass


class Snip(object):

    __metaclass__ = SnipPluginMount

    def __init__(self, snip_args, **kwargs):
        """
        Constructor.
        """
        self.snip_args = vars(snip_args)
        self._get_snip()

    def _get_snip(self):
        print "You are at the base snip"

    def display(self):
        self.render_snip(self.snip)


class HTTPSnip(Snip):
    """
    HTTP resources base.
    """

    def _get_snip(self):
        """
        Kick of main flow of a snip lifecycle.
        """
        self.args = self.get_snip_args(self.snip_args)
        self.build_resource()
        self.get_resource()
        self.snip = self.parse_response(self.response)

    def get_snip_args(self, snip_args):
        """
        Method which takes in the raw snip args (command line arguments).
        Processes anyway it so desires then returns a dict which is assigned
        to self.args for other methods to utilize. A good utilization
        for example, is to use self.args inside a subclass of get_request_parameters.
        """

        return {}

    def build_resource(self):
        """
        Build on the endpoint any parameters the user has defined.
        Should build in verbs as well (GET, POST, etc...)
        """

        self.params = self.get_request_parameters()
        if self.params:
            self.endpoint = self.endpoint + '?' + urllib.urlencode(self.params)

    def get_request_parameters(self):
        """
        Return a dictionary of parameters to send along with the request.
        Think, query string.
        """

        return {}

    def render_snip(self, snip):
        """
        Method which displays the snip on the console for the user.
        """

        pprint.pprint(self.snip, width=20)

    def parse_response(self, response):
        """
        Method to be subclassed. Here is where most logic related to the parsing of
        a snip resource should be performed. It should return a snip object which can be
        processed by your render_snip method.
        """

        snip = response
        return snip

    def get_resource(self):
        """
        Get resource. Could be a web service with json but default is a URL for now.
        Could also be a file or anything readable.
        """

        return urllib2.urlopen(self.endpoint)


class HTMLSnip(HTTPSnip):
    """
    HTML resource based snip. Note that the self.resource is a pyquery object.
    """

    def get_resource(self):
        """
        Get resource. Could be a web service with json but default is a URL for now.
        Could also be a file or anything readable.
        """

        url = self.endpoint
        self.response = pq(url=url)

        return self.response


class JSONSnip(HTTPSnip):
    """
    JSON resource snip. Note that the self.resource is a python dict object.
    """

    def get_resource(self):
        resource = super(JSONSnip, self).get_resource()
        self.response = json.load(resource)

        return self.response
