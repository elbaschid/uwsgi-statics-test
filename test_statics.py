# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import os
import sys
import time
import json
import click
import humanize
import requests

from datetime import datetime
from collections import defaultdict


scenarios = {
    's3': {
        'path': '/s3-static',
        'host': 'uwsgi-statics-test.s3.amazonaws.com',
        'port': 80,
    },
    'uwsgi': {
        'path': '/uwsgi-static',
        'port': 8000,
    },
    'django': {
        'path': '/static',
        'port': 8000,
    },
    'nginx': {
        'path': '/nginx-static',
        'port': 5000,
    }
}


@click.command()
@click.option('--runs', default=100)
@click.option('--host', default='b2d')
@click.option('--verbose', default=False, is_flag=True)
@click.option('--logfile', default='uwsgi-statics')
@click.option('--ignore')
def request_static_files(runs, host, verbose, logfile, ignore):
    results = {}
    files = set(os.listdir('assets'))
    files -= set([ignore])

    log_filename = '{}_{}.log'.format(datetime.now().strftime('%Y-%m-%d'),
                                      logfile)
    logfile = open(log_filename, 'w')

    for __ in range(runs):
        for filename in files:

            for name, config in scenarios.items():
                url = 'http://{host}:{port}{path}/{filename}'.format(
                    host=config.get('host') or host,
                    port=config['port'],
                    path=config['path'],
                    filename=filename)

                if verbose:
                    print('running: {}'.format(name))
                    print(url)

                start = time.time()
                response = requests.get(url)
                duration = time.time() - start

                if verbose:
                    print("Duration: {}".format(duration))

                if not response.ok:
                    raise click.ClickException(
                        '\nerror processing request: {}\n{}'.format(
                            url, response.reason))

                if not verbose:
                    print('.', end='')
                    sys.stdout.flush()

                if filename not in results:
                    results[filename] = defaultdict(int)

                results[filename][name] += int(duration * 1000)

                logfile.write('{}\n'.format(
                    json.dumps({'name': name,
                                'url': url,
                                'duration': duration,
                                'filename': filename})))

    logfile.close()

    print('\n')

    print('{:<10}{:<30}{:<10}{:<10}'.format(
        'served by', 'filename', 'size', 'time (ms)'))
    print('-' * 60)

    for filename, tests in results.items():
        for name, time_sum in tests.items():
            file_size = os.path.getsize('assets/{}'.format(filename))

            print('{:<10}{:<30}{:<10}{:<10}'.format(
                name.upper(),
                filename,
                humanize.naturalsize(file_size),
                (time_sum / runs)))

        print('-' * 60)


if __name__ == '__main__':
    request_static_files()
