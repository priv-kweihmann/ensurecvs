from ensurecvs.arg_parser import parse_args
from ensurecvs.classes.CVS import CVSHelper
from ensurecvs.classes.IssueFinder import IssueFinder

if __name__ == '__main__':
    runargs = parse_args()
    __cvs = CVSHelper.GetCVS(runargs.localdir)

    _startrev = runargs.srcrev or __cvs.GetRevisionFromTag(
        runargs.srctag) or None

    _masterSinceBranch = __cvs.GetCommitSinceBranch(
        branch=runargs.srcbranch, master=runargs.upstream)
    _masterSinceBranch = [x for x in _masterSinceBranch if not __cvs.GetCherryPickedCommit(
        x, _masterSinceBranch[0].hexsha, branch=runargs.srcbranch)]
    _upstreamChanges = __cvs.GetUpstreamChangeSet(
        branch=runargs.srcbranch, start=_startrev)
    _upstreamChanges = [x for x in _upstreamChanges if not __cvs.GetCherryPickedCommit(
        x, _upstreamChanges[0].hexsha, branch=runargs.upstream)]

    _findingsUpstream = IssueFinder(useDefaultFilter=runargs.usedefaultfiler,
                                    filterLists=runargs.filterLists).GetIssues(__cvs, _upstreamChanges)
    _findingsMaster = IssueFinder(useDefaultFilter=runargs.usedefaultfiler,
                                  filterLists=runargs.filterLists).GetIssues(__cvs, _masterSinceBranch)
    for f in _findingsUpstream:
        print("[{}] commit {}:'{}' is likely to contain bugfixes".format(
            runargs.srcbranch or __cvs.GetCurrentBranch(), f.hexsha, f.summary))

    for f in _findingsMaster:
        print("[{}] commit {}:'{}' is likely to contain bugfixes".format(
            runargs.upstream, f.hexsha, f.summary))
