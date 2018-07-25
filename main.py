#!/usr/bin/env python
import configparser
import argparse
import json
import redis
from pprint import pprint

config = configparser.ConfigParser()
config.read('./conf/config.ini')

# argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--id', type=str, help="Input redis key")
args = parser.parse_args()

# connect to redis
r = redis.StrictRedis(host=config['Redis']['host'], port=config['Redis']['port'])

def main():
    key = args.id
    if key:
        print(key)
        row = json.loads(r.execute_command('JSON.GET', key))
        pprint(row)


if __name__ == "__main__":
    main()
