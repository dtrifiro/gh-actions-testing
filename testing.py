import os
import shlex
import shutil
import subprocess
import tempfile


def main_credential_store():
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


def main_subprocess_run():
    shell = True

    cmd = "f() { echo test; }; f"
    try:
        p = subprocess.run(cmd, shell=shell, capture_output=True, check=True)
        print(f"{p}")
        print(f"{p.stdout=}")
        print(f"{p.stderr=}")
    except subprocess.CalledProcessError as exc:
        print(f"Failed to run: {exc}")
        print(f"{exc.stdout=}")
        print(f"{exc.stderr=}")


def main_encoding():
    import locale
    import sys

    print(f"{sys.getdefaultencoding()=}")
    print(f"{sys.getfilesystemencoding()=}")
    print(f"{locale.getpreferredencoding(False)=}")
    print(f"{os.linesep=}")
    try:
        p = subprocess.run(
            ["python", "--version"],
            capture_output=True,
            check=True,
        )
        print(f"{p}")
        print(f"{p.stdout=}")
        print(f"{p.stderr=}")

    except subprocess.CalledProcessError as exc:
        print(f"Failed to run: {exc}")
        print(f"{exc.stdout=}")
        print(f"{exc.stderr=}")

    print(p.stdout.split(b"\n"))


def main():
    path = os.path.join(os.sep, "path", "to", "executable")
    print(f"{path=}")
    print(f"{os.path.isabs(path)=}")
    git_path = shutil.which("git")
    print(f"{git_path=}")
    found_path = shutil.which(git_path)
    print(f"{found_path=}")
    nonexisting_path = os.path.join(os.sep, "path", "to", "exe")
    print(f"{os.path.isabs(nonexisting_path)=}")
    found_nonexisting = shutil.which(nonexisting_path)
    print(f"{nonexisting_path=}")
    print(f"{found_nonexisting=}")

    command = f'{nonexisting_path} --foo bar --quz "with extra args"'
    print(f"{command=}")
    split = shlex.split(command)
    print(f"{split=}")
    split_nonposix = shlex.split(command, posix=False)
    print(f"{split_nonposix=}")


if __name__ == "__main__":
    main()
