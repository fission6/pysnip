Snip is meant to be a light weight command line tool to get snippets of a resource.
Internet resources such as webpages or web services are prime examples. Snip creates a small interface
to allow for pluggable modules, known as "snips" to be seamlessly included and installed. The project includes
example snips for phantasytour.com, twitter.com, ... The end goal is not nessarily a command line browser but rather a robust "snip" manager where people can easily install, remove, update, modify snips for resources.

Install

Usage

Initial Roadmap
1. Snip sprint: gather many more snips for useful / popular resources to make the tool engaging.
2. Design a simple snip loader and router, right now snips are python classes, so essentially a router to classes.
3. Continue to refine interface for creating a snip in terms of robustness but simplecity for creation.
4. Modify how a snip is desiged, maybe there is a way to not use python but describe in YAML or something.
5. Provide easy push / pull for snip repository of sorts.
6. Added support for simple pagination of sorts for snips.


Contribute
Right now the most essential contribution is to offer a snip by a gitpull. The more snips the better overview we will when considering how to refine the snip interface and whats needed.

To conclude, a simple pull request for the snip you've implemented would be great.

