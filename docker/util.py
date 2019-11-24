from shutil import which
def get_container_exe(executables = ['docker', 'podman']):
    for exe in executables:
        path = which(exe)
        if path:
            return path
    else:
        raise FileNotFoundError(
        f'Following container tools not installed: {",".join(executables)}')
