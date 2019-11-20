class CVS(object):

    def __init__(self):
        super().__init__()

    def GetLocalDir(self):
        raise NotImplementedError()

    def GetCurrentRevision(self, branch=None):
        raise NotImplementedError()

    def GetRevisionFromTag(self, tag):
        raise NotImplementedError()

    def GetCurrentBranch(self):
        raise NotImplementedError()

    def GetFirstBranchCommit(self, branch=None):
        raise NotImplementedError()

    def GetCommitSinceBranch(self, branch=None, master="master"):
        raise NotImplementedError()

    def GetPatchPathsFromCommit(self, commit):
        raise NotImplementedError()

    def GetCherryPickedCommit(self, commit, start, branch=None):
        raise NotImplementedError()

    def GetAllBranchCommits(self, branch=None):
        raise NotImplementedError()

    def GetUpstreamChangeSet(self, start=None, end=None, branch=None):
        raise NotImplementedError()
