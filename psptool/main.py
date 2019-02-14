#!/usr/bin/env python3

from blob import Blob


class PSPTool:
    def __init__(self, filename):
        with open(filename, 'rb') as f:
            rom_bytes = bytearray(f.read())

        self.blob = Blob(rom_bytes, len(rom_bytes))


if __name__ == '__main__':
    # CLI stuff to create a PSPTool object and interact with it
    psp = PSPTool('test/binaries/Supermicro_H11DSU7.804-selfread.bin')
    pass