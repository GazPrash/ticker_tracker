import os


def get_version():
    with open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "_version.txt")
    ) as f:
        return f.read().strip()


__version__ = get_version()

if __name__ == "__main__":
    print(__version__)
