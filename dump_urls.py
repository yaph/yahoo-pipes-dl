#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
import json


@click.command(help='Dump source URLs from a pipe definition.')
@click.argument('input', type=click.File('r'))
def main(input):
    pipe = json.load(input)
    definition = json.loads(pipe['PIPE']['live'])

    for mod in definition['modules']:
        for url in mod['conf'].get('URL', []):
            if isinstance(url, dict):
                print(url['value'])


if __name__ == '__main__':
    main()