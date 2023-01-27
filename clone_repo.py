import os

from scmrepo.git import Git


def clone():

    git = Git.clone("ssh://git@github.com/dtrifiro/gh-actions-testing", "tmp")
    print(f"{git=}")
    assert os.path.isdir("tmp")


if __name__ == "__main__":
    clone()
