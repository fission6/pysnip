from snip import JSONSnip


class TwitterSnip(JSONSnip):

    """
    PT snip implementation
    """

    endpoint = 'http://search.twitter.com/search.json'
    snip_slug = 'twitter'

    def get_snip_args(self, snip_args):

        args = {
            'q': snip_args.get('params').pop(),
        }

        return args

    def get_request_parameters(self):

        params = {
            'q': self.args.get('q'),
            'rpp': '10',
            'include_entities': 'true',
            'result_type': 'mixed',
        }
        return params

    def render_snip(self, snip):

        # loop through threads and print them out
        results = snip.get('results')
        for item in results:
            print u"**{from_user} - {created_at} \n {text} \n".format(**item)
