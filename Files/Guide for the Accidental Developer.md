# Guide for the Accidental Developer

These days, many of us are "accidental developers." To do our jobs, we have to learn to manage code as if we are professional software developers.

Here is a master list of things that an accidental developer should eventually master.

## The four main tools

    1. Text editor
    2. File Browser
    3. Terminal that runs a shell program
    4. A Python interpreter

## The big concept

    - a file system tree

## The big challenge

    - knowing where to find shared code in the file tree
        - the developer needs to know where to look
        - apps also need to know where to look
            - see the last entry for more on why finding things is complicated

## Two strategies for learning

    - Triangularization
        - creates a sequence of learning objectives
        - relies on something only after the user understands it

    - Installers that curate a predictable learning environment
        - makes sure that the four main tools work
        - relies on constraints that hide complications that users do not yet understand
        - lets users relax the constraints them when they are ready

## Triangularization

    - find an order A, B, C, D, E, ... where
        - A has no dependencies
        - B depends only on A
        - C depends only on A and B
        - D depends only on A, B, and C ...
        - ...
    - Perhaps
        A = file browser
        B = app installers
        C = text editor
        D = terminal
        E = an official Python distribution from python.org
            - many people get into trouble because they get Python from another source
            - the have trouble because the instructions for official Python don't work for their version
        F = use a text editor to create a terminal profile that modifies PATH
        G = use a Python virtual environment to manage PATH and PYTHONPATH for a Python project
        H = install external Python libraries

    - Problem with this approach
        - there is a huge amount to learn before a user can use such libraries as Numpy or Matplotlib

## Alternative: An installer with escape hatches

    - Annaconda was an installer
        - It trapped people into using a proprietary product

    - Gennaker is an installer that is designed to make sure that learners can stop using it
        - When they are ready, it shows users the escape hatches

    -Gennaker provides
        - a text editor
        - a terminal
        - versions of Python that only Gennaker uses
        - notebooks that run Python and display markdown
        - a limited file browser that shows only one directory at a time
            - does display "bread crumbs" that convey text with information about locations in the file tree
    - Gennaker's projects are independent
        - each has its own customized version of PATH and PYTHONPATH
        - each can then have its own
            - version of Python
            - versions of Python libraries
            - its own binaries that the OS will run
    - Gennaker lets someone learn the basics of the four main tools
        - without asking them to
            - install libraries and dependencies
                - which requires an understanding of where to find things
                - including how to manage versions, PATH, or PYTHONPATH

## The issues that got in our way this semester were

    - getting Gennaker installers to work on both macOS and Windows
    - setting up a seemless yet secure way for an author to distribute content
        - e.g. to fix bugs in code in a notebook

## Concepts developers should eventually understand

    - text file and text interfaces
    - markup
    - file system tree
    - PATH, PYTHONPATH
    - virtual environments
    - hardware separation
    - permissions
    - authentication

## The text interface

    - Unix philosopy: "text file as universal interface"
    - the combinatorics of text
    - Example: command palette in applications
    - Example: System preferences on macOS

## Navigating the file tree

    - the asymmetry between up and down
    - how to go up and down in the file browser, editor, shell, python
        - in the shell, understand the . and .. nicknames for directories and `~`

## Path objects for Python

    - dot notation
    - overloaded operators, e.g. '/'
    - strings for macOS, Linux, Windows as derived attributes or outputs

## Update strategy for shared libraries and modules

    - PATH provides flexibility over timing
    - A cooldown protects you from newly introduced malware
        - for Node modules
            - npm now offers a cooldown option for node modules
            - pnpm does as well
        - for Python libraries
            - pip does not yet offer a cooldown option
            - uv does

## How to be a developer despite Windows

    - avoid the many confusing shell programs that are specific to Windows
        - in particular, avoid the use of command prompt and various PowerShells
    - use git bash
    - or use Windows Subsystem for Linux, where the shell is bash
    - Escape from Windows: when vs if?

## How to setup macOS

    - create a terminal profile for zsh
        - turn on secure keyboard entry
    - Finder (file browser)
        - customize the sidebar
            - keep only the features you use
            - make sure you have an entry for your Home directory
        - follow the tree
            - don't use Recents
        - Learn about the `Home/Library` folder that apps use
    - install Python
        - know how to run `python3 script.py`
    - setup keyboard shortcuts so you can switch between the four main tools
        - e.g. to open a terminal in a directory selected in Finder
        - use a command to open your editor in the directory for a project
            - may require some setup to make sure you can start your editor from terminal
    - use tabs for Terminal and Finder to limit the proliferation of windows
    - pick a default way to run python
        - REPL
        - interpreter and a script.py file
        - run code in a Jupyter notebook

## How to setup Windows - Git Bash

    - quiet the Windows noise
    - put an icon for Git Bash on bottom bar
    - File Manager
        - use the sidebar
            - add an entry for your home directory
            - remove misleading entries if you can learn how
                - e.g. for One Drive
        - follow the tree
        - learn about the directories that Git Bash uses
        - learn about the directories that Windows uses
    - install Python
        - learn how to run `python script.py`
    - set keyboard shortcuts so you can switch between the four main tools
        - may require some setup to start editor from terminal
    - if possible, use tabs for Terminal and Finder
    - pick a default way to run python
        - REPL
        - interpreter and script.py file
        - JupyterLab notebook

## How to setup Windows WSL

    - quiet the Windows noise
    - install Linux
        - Debian is a natural distribution to use
    - put an icon that starts your distribution on bottom bar
    - Debian does not have a file browser
        - customize a File Manager window for use with WSL
            - think about what your home directory means
        - rely more heavily on the bash shell to move around the file system tree
    - install Python via apt package manager in Debian
        - learn how to run `python script.py` from Bash
    - set keyboard shortcuts so you can switch between your editor and the shell
        - may require some setup to start editor from your terminal
        - discover ways to get from File Manager to Bash and back
    - use tabs for Terminal and Finder
    - pick a default way to run python
        - REPL
        - interpreter and script.py file
        - JupyterLab notebook

## Security

    - why you should do os updates asap
    - have a system for saving and retrieving passwords
        - use different types of passwords for different purposes
            - "horse-staple-battery..." vs "jeOEO23u02$23r421"
    - understand the advantages of hardware separation over software boundaries
    - understand the value of actions that require user intervention
    - understand the difference between admin vs standard roles
    - understand the principles behind file permissions (macOS and Linux) and access control lists (Windows)
    - on macOS and Linux, learn how to use `sudo`
    - understand that Windows does not have anything equivalent to `sudo`
    - understand the difference between
        - keeping malware from running on your computer
        - limiting the damage that malware can do if it runs with your permissions
    - understand the difference between the two main systems for remote authentication
        - send a secret over the wire
        - use a challenge-response protocol
    - understand the difference between
        - https
            - sets up an encrypted tunnel
            - uses PKI to authenticate the server
            - under http, user authentication is handled separately
                - stateless; every message from users needs to authenticate the user
                    - initial authentication
                    - persistence mechanism
                        - typically relies on bearer credentials that can be stolen
        - SSH
            - sets up an encrypted tunnel
            - maintains state
            - uses public keys to identify server and client
                - public keys are then used to support a challenge-response authentication protocol
            - the setup challenge
                - find an independent channel that provides public keys to server and client
                - this is difficult but only has to be done once

## Appendix: Why finding things is complicated

    - apps use
      - APIs provided by the OS
      - dependencies that are developed independently
      - Python is one of these dependencies; it has its own dependencies
      - apps refer to dependencies by name only
        - code tells Windoes to run "python"
        - on macOS, there was an exception
          - during a long transition, code could say
            - "python2" to run version 2 of Python
            - "python3" to run version 3 of Python
      - in Python
        - code says `import Numpy` without specifying which version
        - as a result, no changes are needed in your code when a new version of Numpy makes only internal changes
        - it would be onerous for an app developer to keep track of all the versions of all dependencies
    - The OS provider and app developers coordinate updates for
        1. the OS
        2. apps
    - With many open-source dependencies, it is impossible to coordinate updates to
        2. apps
        3. dependencies

    - Python developers coordinate updates to the interpreter and the standard Library
    - They do not coordinate updates with external libraries such as pip

    - "DLL Hell" is the popular name for the conflicts that can arise
      - suppose two apps rely on the same dependency; and
      - they look in the same folder to find it; and
      - an update to a dependency contains "breaking changes."

      - For example:
        - each app looks for something called "dep" in a specific folder
        - in that folder, there can be only one file named "dep"
        - app_1 has been upgraded to work only with ver_N of dep
          - if app_1 finds and runs ver_M it will break
        - app_2 has not yet been upgraded to handle the changes in dep
          - if it finds and uses the newer ver_N of dep, app_2 breaks
      - In this case, it is impossible
        - to update app_1 and app_2 on different dates and
        - and keep both apps running durring the transition
      - The solution is to have app_1 and app_2 look in different folders.

    - How PATH helps
      - PATH tells each app where to look to find its version of the dependency "dep"
      - Different apps can have given copies of PATH
      - Ver_N of dep can be saved in one directory
      - Ver M of dep exists in another directory
    - The OS uses PATH to guide apps when they look for binaries that the OS can run

    - The Python interpreter has its own version, PYTHONPATH
      - different Python apps can have different versions of PYTHONPATH
      - they tell the interpreter where to find the Python libaries for each app
    - Technically, Python creates another level between the OS and the apps:
      - Apps use a version of Python and versions of specific dependencies

## EOF
