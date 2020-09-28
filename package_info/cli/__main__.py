import sys
import json
from argparse import ArgumentParser
from ..package_info import get_package_info


def main():
    parser = ArgumentParser()
    parser.add_argument("package", nargs="*")
    args = parser.parse_args()

    name = args.package[0]
    result = get_package_info(name)

    if len(args.package) < 2:
        # Dump all data as JSON
        print(json.dumps(result, indent=4))
    else:
        # Dump the value of a key as JSON
        pattern = args.package[1]
        try:
            print(json.dumps(result[pattern], indent=4))
        except KeyError:
            print("{}")
            return 1
 
if __name__ == "__main__":
    sys.exit(main())
