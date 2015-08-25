#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
import json
import os
import requests


target_dir = os.path.dirname(os.path.abspath(__file__))
info_url = 'https://pipes.yahoo.com/pipes/person.info'
pipe_url = 'https://pipes.yahoo.com/pipes/pipe.info'


def save_pipes(pipes):
    for pipe in pipes:
        pipe_params = {'_out': 'json', '_id': pipe['id']}
        pip_def = requests.get(pipe_url, params=pipe_params).json()
        fname = os.path.join(target_dir, 'pipes', pipe['id'] + '.json')
        with open(fname, 'w') as f:
            json.dump(pip_def, f)
            print('Saved pipe definition in: {}'.format(fname))


@click.command(help='Run with your Yahoo Pipes user id to save all your published pipe definitions to the pipes directory.')
@click.argument('guid')
def main(guid):
    page = 1
    while True:
        info_params = {'_out': 'json', 'guid': guid, 'page': page}
        pipes_info = requests.get(info_url, params=info_params).json()
        pipes = pipes_info['value']['items']
        if not pipes:
            break
        page += 1
        save_pipes(pipes)


if __name__ == '__main__':
    main()