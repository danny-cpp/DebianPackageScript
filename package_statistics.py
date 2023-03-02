#!/usr/bin/env python3

# Debian Package Download and Statistics
#
# Danh Nguyen
# https://github.com/danny-cpp
# March, 2023


import argparse
import urllib.request
import gzip

if __name__ == '__main__':

    # Script take in 1 argument, which is the name of the architecture
    parser = argparse.ArgumentParser(description='Download and parse Debian Contents file for a given architecture')
    parser.add_argument('architecture', type=str, help='the architecture type')
    args = parser.parse_args()

    url = f'http://ftp.uk.debian.org/debian/dists/stable/main/Contents-{args.architecture}.gz'

    # Download the file and read it into memory
    with urllib.request.urlopen(url) as response:
        with gzip.GzipFile(fileobj=response) as gzfile:
            contents = gzfile.read().decode()

    # Parse the file and count the number of files for each package
    packages = {}
    for line in contents.split('\n'):
        if line.strip():
            package, _, _ = line.partition(' ')
            packages[package] = packages.get(package, 0) + 1

    # Output the top 10 packages with the most files
    i = 1
    for package, count in sorted(packages.items(), key=lambda x: x[1], reverse=True)[:10]:
        row = [i, str(package).replace("usr/share/", ""), count]
        print("{: >2}.{: >40} {: >10}".format(*row))
        i = i + 1
