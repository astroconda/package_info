#!/usr/bin/env python
from pkg_resources import get_distribution
import sys
import json


def get_package_info(name):
    read_desc = False
    result = {}

    # PKG-INFO keys that are considered lists
    requires_list = [
        "classifier",
        "project_url",
        "requires_dist",
        "provides_extra",
    ]

    # Get package dist information
    try:
        pkg = get_distribution(name)
    except Exception as e:
        return result

    # Parse PKG-INFO file
    for i, record in enumerate(pkg._get_metadata(pkg.PKG_INFO)):
        # Are we reading key pairs or the long package descripton (at the end of the file)?
        if not read_desc:
            # Is a key pair present? If not, we're at the long desciption
            if ':' not in record or not record:
                result["description"] = record + "\n"
                read_desc = True
                continue

            # Parse the record into a key pair
            key, value = record.split(':', 1)

            # Remove dashes from key and convert to lower-case
            key = key.replace("-", "_").lower()

            # Remove leading and trailing whitespace from value
            value = value.lstrip().strip()

            # Is the key we've encounted supposed to be a list, or string?
            if key in requires_list:
                # Create a new key in the dictionary as a list
                if result.get(key) is None:
                    result[key] = []

                # Write value to result
                result[key].append(value)
            else:    
                # Write string value to result
                result[key] = value
        else:
            # Write description block to result
            result["description"] += record + '\n'

    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Not enough arguments: need package name", file=sys.stderr)
        exit(1)

    name = sys.argv[1]
    result = get_package_info(name)

    if len(sys.argv) < 3:
        # Dump all data as JSON
        print(json.dumps(result, indent=4))
    else:
        # Dump the value of a key as JSON
        pattern = sys.argv[2]
        try:
            print(json.dumps(result[pattern], indent=4))
        except KeyError:
            print("{}")
            exit(1)
