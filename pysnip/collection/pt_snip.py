from snip.types import HTMLSnip


class PTSnip(HTMLSnip):

    """
    PT snip implementation
    """

    endpoint = 'http://phantasytour.com/bands/1/topics'
    snip_slug = 'pt'

    def render_snip(self, snip):

        # loop through threads and print them out
        for item in snip:
            print "{title} | {poster} | {post_count} | {last_post}".format(**item)

    def parse_response(self, response):

        recent_posts = response('table.topics_listing tr')
        snip = []
        # loop through recent posts and built up output
        for post in recent_posts[1:8]:
            pq_post = recent_posts(post)
            thread = {
                'title': pq_post.find('td.topic_subject').text(),
                'poster': pq_post.find('td.topic_author_display_name').text(),
                'post_count': pq_post.find('td.topic_posts').text(),
                'last_post': pq_post.find('td.topic_last_post').text(),
            }

            snip.append(thread)

        return snip
