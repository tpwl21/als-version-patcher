import argparse
import configparser
import gzip
import os
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Tuple

CONFIG_FILE = "../config/live_headers.ini"

def get_config_for_version(config_ini: str, version: str) -> List[Tuple]:

    filein = os.path.join(os.path.dirname(__file__), config_ini)
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(Path(filein).absolute())
    if config.sections() == []:
        print(filein)
    for section in config.sections():
        if section.replace('Ableton', '') == version:
            return config.items(section)


def patch_als_root(als_input_path: str, als_output_path: Path, version: str) -> None:

    als_input_path = Path(als_input_path)
    patched_conf = dict(get_config_for_version(CONFIG_FILE, version))

    print(f'[*] Patching als file IN: {als_input_path.name}')

    with tempfile.NamedTemporaryFile(dir='/tmp', suffix='.gz', delete=True) as temp_file:

        with gzip.open(als_input_path, 'rb') as f:
            temp_file.write(f.read())

        tree = ET.parse(temp_file.name)
        root = tree.getroot()

        print(f'[-] OLD: {dict(root.items())}')
        print(f'[+] NEW: {patched_conf}')

        for key, value in root.items():
            try:
                if key not in patched_conf.keys():
                    del root.attrib[key]
                else:
                    root.attrib[key] = patched_conf[key]
            except KeyError:
                print(f'[!] Parameter {key} not found')

        xml_out = ET.tostring(root, encoding="UTF-8", xml_declaration=True)

        with gzip.open(als_output_path, 'wb') as fout:
            fout.write(xml_out)

        print(f'[*] Patched succesfully OUT: {als_output_path}')

def main():

    parser = argparse.ArgumentParser(description='als version modifier')
    parser.add_argument('-i', help='Path to the input als file')
    parser.add_argument('-o', default=None, help='Path to the output als file')
    parser.add_argument('-v', default='11', help='Ableton target version')
    args = parser.parse_args()
    if args.o is None:
        args.o = args.i.replace('.als', f'_patched{args.v}.als')

    patch_als_root(args.i, args.o, args.v)

if __name__ == '__main__':
    main()



