from pysnip import commands, registered_snips
import argparse


def main():
    parser = argparse.ArgumentParser(description="""
        A pluggable tool to get a `snip` of small summary of a
        resource such as a webpage, webservice, or file.
        """
    )
    parser.add_argument('snip_slug',
        help="Enter the snip you'd like (ie. `twitter`)"
    )
    parser.add_argument('params', nargs='*')
    args = parser.parse_args()

    # get slug to map to snip class
    snip_slug = args.snip_slug

    if snip_slug in registered_snips:

        snip_class = registered_snips.get(snip_slug)
        snip = snip_class(args)
        snip.display()

    elif snip_slug in commands:
        command = commands.get(snip_slug)
        # if function then call
        command()


if __name__ == "__main__":
    main()
