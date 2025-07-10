import pathlib


class _Setting:
    ROOTDIR = pathlib.Path(__file__).parent


setting = _Setting()
