import os
import subprocess
import tempfile


def main():
    path = os.path.join(tempfile.gettempdir(), "dulwich-git-credential-store-test")

    for shell in [True, False]:
        print(f"Running {shell=}")
        cmd = f"git credential-store --file {path} store"
        if not shell:
            cmd = cmd.split(" ")

        url = "https://github.com"
        username = "username"
        password = "password"
        subprocess_in = f"url={url}\nusername={username}\npassword={password}\n".encode(
            "UTF-8"
        )

        try:
            p = subprocess.run(
                cmd, shell=shell, capture_output=True, check=True, input=subprocess_in
            )
            print(f"{p}")
            print(f"{p.stdout=}")
            print(f"{p.stderr=}")

        except subprocess.CalledProcessError as exc:
            print(f"Failed to run: {exc}")
            print(f"{exc.stdout=}")
            print(f"{exc.stderr=}")

        subprocess_in = f"url={url}\n".encode("UTF-8")
        cmd = f"git credential-store --file {path} get"
        if not shell:
            cmd = cmd.split(" ")
        try:
            p = subprocess.run(
                cmd, shell=shell, capture_output=True, check=True, input=subprocess_in
            )
            print(f"{p}")
            print(f"{p.stdout=}")
            print(f"{p.stderr=}")

        except subprocess.CalledProcessError as exc:
            print(f"Failed to run: {exc}")
            print(f"{exc.stdout=}")
            print(f"{exc.stderr=}")


if __name__ == "__main__":
    main()
