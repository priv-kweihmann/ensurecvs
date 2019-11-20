# ensurecvs

![Build status](https://github.com/priv-kweihmann/ensurecvs/workflows/Build/badge.svg)
[![PyPI version](https://badge.fury.io/py/ensurecvs.svg)](https://badge.fury.io/py/ensurecvs)
[![Python version](https://img.shields.io/pypi/pyversions/ensurecvs)](https://img.shields.io/pypi/pyversions/ensurecvs)
[![Downloads](https://img.shields.io/pypi/dm/ensurecvs)](https://img.shields.io/pypi/dm/ensurecvs)

## Purpose

This tool shall help identify commits in current source tree that are

* available remote on the same branch
* available in the parent branch

and are likely to contain bugfixes.

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

Ensure that you're using the most security source code

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
* compare the changeset diff for cherry-pick analysis
* streamline code
* svn-repository support

## Contribution

Feel free to add issues or pull requests
