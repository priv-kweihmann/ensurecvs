# ensurecvs

![Build status](https://github.com/priv-kweihmann/ensurecvs/workflows/Build/badge.svg)
[![PyPI version](https://badge.fury.io/py/ensurecvs.svg)](https://badge.fury.io/py/ensurecvs)
[![Python version](https://img.shields.io/pypi/pyversions/ensurecvs)](https://img.shields.io/pypi/pyversions/ensurecvs)
[![Downloads](https://img.shields.io/pypi/dm/ensurecvs)](https://img.shields.io/pypi/dm/ensurecvs)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/priv-kweihmann/ensurecvs.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/priv-kweihmann/ensurecvs/context:python)

## Purpose

This tool shall help identify commits in current source tree that are

* available remote on the same branch
* available in the parent branch

and are likely to contain bugfixes.

## History

When you're using a 3rd party components in your project it's hard to balance between keeping it safe and tested against keeping in touch with upstream/mainline, especially when you have to decide if the code is as safe as possible.

Most would rely here on CVE-notifications for the used component and the corresponding version.

I was watching the [2019's keynote of Greg Kroah-Hartman at Embedded Linux Conference Europe in Lyon](https://www.youtube.com/watch?v=fIwr_znLsec&list=PLbzoR-pLrL6pamOj4UifcMJf560Ph6mJp&index=6&t=0s) where he said, that most issues don't even get a CVE entry anymore, they will just be fixed with a commit in upstream (at least for the kernel).

This is somehow hard to maintain, as mostly you simply don't want to change the feature-set (as this has been tested and approved) but need the bug- and issue-fixes from that project.

That is where this tool comes into play - It performs automatic checks if there are upstream fixes available - and if so, if they only contain fixes and NOT features.

Ensurecvs, helps you to __ensure__ and you're using the best of the used __content versioning system__

### What it does

* It extracts the currently used commit from the local repository clone
  * this can be overridden by specifying ```--srcrev``` or ```--srctag``` in command line
* It extracts the currently used branch from the local repository clone
  * this can be overridden by specifying ```--srcbranch``` in command line
* It gets all remote available commits in current branch
* It gets all commits made to 'master' since current branch has been branched off (an alternative branch to 'master' can be specified by using ```--upstream``` in command line)
  * it filters all commits out, that might have been cherry-picked in current branch
* all the remaining commits are classified regarding their commit message
* commits that are classified to be likely bugfixes are presented at the console (STDOUT)

## Usage

```shell
usage: ensurecsv [-h] [--srcbranch SRCBRANCH]
                 [--srcrev SRCREV | --srctag SRCTAG] [--upstream UPSTREAM]
                 localdir

Ensure that you're using the most secure source code

positional arguments:
  localdir              Path to local repo

optional arguments:
  -h, --help            show this help message and exit
  --srcbranch SRCBRANCH
                        Use explicitly given branch
  --srcrev SRCREV       Use explicitly given source revision
  --srctag SRCTAG       Use explicitly given tag
  --upstream UPSTREAM   Use explicitly given branch as upstream
```

## Installation

### From pypi

simply run

```sh
pip3 install ensurecvs
```

### From source

* git clone this repository
* cd to \<clone folder\>/ensurecvs
* Install the needed requirements by running ```pip3 install -r requirements.txt```
* run ```python3 setup.py build install``` (possibly 'sudo' is needed)

## Output

The tool will return

```sh
[branch] commit <commit hash>:'<commit message>'  is likely to contain bugfixes
```

e.g.

```shell
[master] commit 173dfc1c07c9fa901a91adbc9bf8fd41961b9837:'Fix compile issue with python-astor' is likely to contain bugfixes
```

that means that commit __173dfc1c07c9fa901a91adbc9bf8fd41961b9837__ currently to be found in branch __master__ is likely to contain a bugfix that isn't yet used in the currently selected branch

## Implementation notes

Currently only git-repositories are supported

## Future

If you have interest in one or more of the following topics, feel free to get in contact with me

* better commit classification (maybe with something like [this here](https://github.com/nxs5899/Multi-Class-Text-Classification----Random-Forest))
* better documentation
* changeset code analysis for better commit classification
* check on out-of-tree patches in local code
* compare the changeset diff for cherry-pick analysis
* streamline code
* svn-repository support

## Contribution

Feel free to add issues or pull requests
