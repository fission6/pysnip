Overview
--------

This project (pysnip) is meant to be a light weight command line tool to get "snippets" of a resource.
Internet resources such as webpages or web services are prime examples. Snip (for short) creates a small interface
to allow for pluggable modules, known as "snips" to be seamlessly included and installed. The project includes
example snips for phantasytour.com, twitter.com, ... The end goal is not necessarily a command line browser but rather a robust "snip" manager where people can easily install, remove, update, modify snips for resources.

Install
-------

- working on a pip package though not stable enough at the moment.
- fork / clone through github and install directly:
    1. git clone git@github.com:fission6/pysnip.git
    2. python setup.py install (may need to sudo)

- install via pip
    1. pip install git+https://github.com/fission6/pysnip.git


Usage
-----

- snip pt
- snip twitter 'python'
- snip twitter '#github'
- snip --help
- snip list
    Listing Available Snips
    - wiki
    - twitter
    - slashdot
    - pt

Creating a Snip
---------------
to be filled out shortly.


Initial Roadmap
---------------

1. Snip sprint: gather many more snips for useful / popular resources to make the tool engaging.
2. Design a simple snip loader and router, right now snips are python classes, so essentially a router to classes.
3. Refine / build an interface to command options for each snip.
4. Continue to refine interface for creating a snip in terms of robustness but simplecity for creation.
5. Modify how a snip is designed, maybe there is a way to not use python but describe in YAML or something.
6. Provide easy push / pull for snip repository of sorts.
7. Added support for simple pagination of sorts for snips.


Contribute
----------

Right now the most essential contribution is to offer a snip by a git-pull. The more snips the better overview we will when considering how to refine the snip interface and whats needed.  You can model your snips after snips in the snips/ path / module.

To conclude, a simple pull request for the snip you've implemented would be great.
