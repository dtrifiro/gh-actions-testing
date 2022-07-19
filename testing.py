import os
import shlex
import shutil
import subprocess
import sys
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


def main_paths():
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


def main_shlex():

    python = shutil.which("python")
    command = f'{python} cli.py --foo bar --quz "with extra args"'
    print(f"{command=}")

    for posix in True, False:
        print(f"{posix=}")
        split = shlex.split(command, posix=posix)
        print(f"{sys.platform=}")
        split[0] = command.split(maxsplit=1)[0]
        print(f"{split=}")

        try:
            p = subprocess.run(split, capture_output=True)
            print(f"{p}")
            print(f"{p.stdout=}")
            print(f"{p.stderr=}")
        except subprocess.CalledProcessError as exc:
            print(f"Failed to run: {exc}")
            print(f"{exc.stdout=}")
            print(f"{exc.stderr=}")
        print("-" * 30)


def main_path():
    print("path=", os.environ["PATH"])
    git_credential_store = shutil.which("git-credential-store")
    print(f"{git_credential_store=}")

    exec_path = subprocess.check_output(
        "git --exec-path".split(), universal_newlines=True
    ).strip()

    p = subprocess.run(
        os.path.join(exec_path, "git-credential-store"),
        universal_newlines=True,
        capture_output=True,
    )
    print(f"{p}")
    print(f"{p.stdout=}")
    print(f"{p.stderr=}")


def main_docker():
    import docker

    client = docker.from_env()
    try:
        print(f"{client.ping()=}")
    except docker.errors.APIError:
        print("Failed to communicate with the docker client")
        sys.exit(0)

    image = "python:3.8-slim"
    print(f"{sys.platform=}")
    pulled = client.images.pull(image)
    print(f"{pulled=}")
    res = client.containers.run(
        image,
        command="python -c 'print(\"hello\")'",
        stdout=True,
        stderr=True,
        # detach=True,
        remove=True,
    )
    print(f"{res=}")


def main():
    from scmrepo.git import Git

    git = Git()
    tree = os.path.join("dir", "subdir")
    os.makedirs(tree, exist_ok=True)
    newfile = os.path.join(tree, "newfile")
    with open(newfile, "w") as fh:
        fh.write("anewfile")
    git.add([newfile])
    git.commit("commit")

    with open(newfile, "w") as fh:
        fh.write("anewfile modified")
    git.add([newfile])
    newfile1 = os.path.join(tree, "newfile1")
    with open(newfile1, "w") as fh:
        fh.write("anewfile1")
    git.add([newfile1])
    with open(newfile, "a") as fh:
        fh.write("newcontent")
    untracked = os.path.join(tree, "untracked")
    with open(untracked, "w") as fh:
        fh.write("untracked")

    staged, modified, untracked = git.dulwich.status()
    print(f"dulwich: {staged=}, {modified=}, {untracked=}")


if __name__ == "__main__":
    main()
