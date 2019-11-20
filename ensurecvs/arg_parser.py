import argparse


def parse_args():
    global RUNARGS
    global DEFAULT_VERSION
    parser = argparse.ArgumentParser(
        prog="ensurecsv", description="Ensure that you're using the most security source code")
    parser.add_argument("localdir", help="Path to local repo")
    parser.add_argument("--srcbranch", default=None,
                        help="Use explicitly given branch")

    revgroup = parser.add_mutually_exclusive_group()
    revgroup.add_argument("--srcrev", default=None,
                          help="Use explicitly given source revision")
    revgroup.add_argument("--srctag", default=None,
                          help="Use explicitly given tag")

    parser.add_argument("--upstream", default="master",
                        help="Use explicitly given branch as upstream")
    parser.add_argument("--filterLists", default=[],
                        nargs='+', help=argparse.SUPPRESS)
    parser.add_argument("--usedefaultfiler", default=True,
                        action="store_false", help=argparse.SUPPRESS)
    RUNARGS = parser.parse_args()
    return RUNARGS
