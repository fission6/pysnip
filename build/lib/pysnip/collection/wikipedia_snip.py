from pysnip.snip.snip.types import JSONSnip


class WikipediaSnip(JSONSnip):

    """
    Wikipedia snip implementation
    """

    endpoint = 'http://en.wikipedia.org/w/api.php'
    snip_slug = 'wiki'

    def get_snip_args(self, snip_args):

        args = {
            'title': snip_args.get('params').pop(),
        }

        return args

    def get_request_parameters(self):

        params = {
            'action': 'query',
            'titles': self.args.get('title'),
            'prop': 'extracts',
            'format': 'json',
            'exintro': '1',
            'explaintext': '1',
        }
        return params

    def render_snip(self, snip):

        # loop through threads and print them out
        results = snip.get('query').get('pages')
        for page, item in results.iteritems():
            print u"**{title}.** \n\n {extract} \n\n".format(**item)
