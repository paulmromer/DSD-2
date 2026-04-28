# Configuration file for jupyter-server.
# The current recommendation on naming is to use
# jupyter_server_config.py instead of jupyter_lab_config.py

import pathlib


def cleanup_shortcut_settings(settings):
    for shortcut in settings["shortcuts"]:
        if shortcut.get("args") == {}:
            del shortcut["args"]

        if shortcut.get("keys") == [""]:
            del shortcut["keys"]

        if shortcut.get("macKeys") == [""]:
            del shortcut["macKeys"]


def settings_hook(source_path, json_settings_path, settings):
    sub_path = json_settings_path.relative_to(source_path)
    match sub_path.parts:
        case ("@jupyterlab", "shortcuts-extension", "shortcuts.jupyterlab-settings"):
            cleanup_shortcut_settings(settings)
    return settings


user_home = pathlib.Path.home().absolute()
project_home = pathlib.Path(".").absolute()
Files = project_home / "Files"
Pubs = project_home / "Pubs"

## upper_limit is the top of the tree that File Browser can reach
## start_dir is where File Browser starts
upper_limit = project_home
start_dir = Pubs.relative_to(upper_limit)


c = get_config()  # noqa

c.SettingsSyncApp.settings_changed_hook = settings_hook
c.SettingsSyncApp.dest_path = pathlib.Path.cwd() / "toml-settings"


## Allow access to hidden files
c.ContentsManager.allow_hidden = True

## Globs -- always hidden
c.ContentsManager.hide_globs = [
    "__pycache__",
    "*.pyc",
    "*.pyo",
    ".DS_Store",
    "*.so",
    "*.dylib",
    "*~",
    ".ipython",
    ".gennaker",
    ".virtual_documents",
    ".env",
    ".gitignore",
    ".jupyter_ystore.db",
    ".python-version",
    ".venv",
    ".ipynb_checkpoints",
    ".git",
    "pyproject.toml",
    ".jupyter",
    ".ropeproject",
    ".local-libraries",
    "*~",
    ".ropeproject",
    ".gennaker",
    ".python-version",
    "uv.lock",
    "uv.toml",
    "toml-settings",
]

c.ContentsManager.root_dir = str(upper_limit)
c.ContentsManager.preferred_dir = str(start_dir)

## Shutdown
# Shut down the server after N seconds with no kernels
# running and no activity. This can be used together with
# culling idle kernels (MappingKernelManager.cull_idle_timeout)
# to shutdown the Jupyter server when it’s not in use.
# This is not precisely timed: it may shut down up to a minute later.
# 0 (the default) disables this automatic shutdown.
# Default = 0
c.ServerApp.shutdown_no_activity_timeout = 1

## Time to wait for a kernel to terminate before killing it,
# in seconds. When a shutdown request is initiated, the kernel
# will be immediately sent an interrupt (SIGINT),
# followedby a shutdown_request message, after 1/2 of shutdown_wait_time
# it will be sent a terminate (SIGTERM) request, and finally at the end
# of shutdown_wait_time will be killed (SIGKILL).
# terminate and kill may be equivalent on windows.
# Default: 5.0
c.KernelManager.shutdown_wait_time = 1.0
