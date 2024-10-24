from urllib.request import urlopen
import json

from typing import TYPE_CHECKING

import sys


if TYPE_CHECKING:
    from http.client import HTTPResponse


def main():
    repository = "modh/vllm"
    response: "HTTPResponse" = urlopen(
        f"https://quay.io/api/v1/repository/{repository}/tag/"
    )

    assert response.status == 200

    content = response.read().decode()
    data = json.loads(content)

    input_digest = sys.argv[1]

    found = False
    for tag in data["tags"]:
        digest = tag["manifest_digest"]

        name = tag["name"]

        print(f"{name=} {digest=}")

        if digest == input_digest:
            found = True
            break

    if not found:
        print(f"Couldn't find {input_digest=}", file=sys.stderr)
        sys.exit(2)

    print(f"Tag has {name=}")

    if "cuda" not in name:
        print(f"{input_digest=} corresponds to {name=}. We only want cuda tags.")
        sys.exit(1)


if __name__ == "__main__":
    main()
