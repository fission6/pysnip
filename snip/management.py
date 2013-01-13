from snip import registered_snips


def list_snips():
    """
    List all available / installed snips for the user.
    """

    print "Listing Available Snips"

    for snip in registered_snips:
        print "*", snip


commands = {
    'list': list_snips,
}
