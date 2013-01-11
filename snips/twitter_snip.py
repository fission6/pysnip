from snip import JSONSnip


class TwitterSnip(JSONSnip):

    """
    PT snip implementation
    """

    resource = 'http://search.twitter.com/search.json?q=python&rpp=10&include_entities=true&result_type=mixed'

    def render_snip(self, snip):

        # loop through threads and print them out
        results = snip.get('results')
        for item in results:
            print u"**{from_user} - {created_at} \n {text} \n".format(**item)
