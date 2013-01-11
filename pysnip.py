from snips import *
import argparse


def load_snip_routes():

    return {
        'twitter': TwitterSnip,
        'pt': PTSnip,
    }

snip_routes = load_snip_routes()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("snip", help="Enter the snip you'd like (ie. `twitter`)")
    args = parser.parse_args()
    snip_slug = args.snip

    if snip_slug in snip_routes:
        snip_class = snip_routes.get(snip_slug)
        snip = snip_class()
        snip.display()

    # main()
