from snip.types import HTMLSnip


class SlashdotSnip(HTMLSnip):

    """
    PT snip implementation
    """

    endpoint = 'http://slashdot.org/'
    snip_slug = 'slashdot'

    def render_snip(self, snip):

        # loop through threads and print them out
        for item in snip:
            print u"**{title}** \n\n {summary} \n\n".format(**item)

    def parse_response(self, response):

        # recent_posts = response('h2.story span[id^="title"] a')
        recent_posts = response('article.article')
        snip = []
        # loop through recent posts and built up output
        for post in recent_posts[:10]:
            pq_post = recent_posts(post)
            thread = {
                'title': pq_post.find('span[id^="title"] a').text(),
                'summary': pq_post.find('div.body i').text(),
            }

            snip.append(thread)

        return snip
