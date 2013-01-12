import snips
import argparse


snip_routes = snips.registered_snips

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('snip_slug', help="Enter the snip you'd like (ie. `twitter`)")
    parser.add_argument('params', nargs='*')
    args = parser.parse_args()
    print "Args", args
    snip_slug = args.snip_slug

    if snip_slug in snip_routes:
        params = args.params
        print "Calling", snip_slug, 'with', params
        snip_class = snip_routes.get(snip_slug)
        snip = snip_class(args)
        snip.display()
