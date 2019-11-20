import git

from ensurecvs.classes.CSV_base import CVS


class CVSgit(CVS):

    def __init__(self, localdir):
        super().__init__()
        self.__git = git.Repo(path=localdir)
        self.__git.git.fetch()

    def GetLocalDir(self):
        return self.__git.working_dir

    def GetCurrentRevision(self, branch=None):
        _branch = branch or self.GetCurrentBranch()
        x = [x for x in self.__git.heads if x.name == _branch]
        if x:
            return x[0].commit.hexsha
        return None

    def GetRevisionFromTag(self, tag):
        for x in self.__git.tags:
            for y in x.list_items(self.__git):
                if str(y) == tag:
                    return y.commit.hexsha
        return None

    def GetCurrentBranch(self):
        return self.__git.active_branch

    def GetFirstBranchCommit(self, branch=None):
        _branch = branch or self.GetCurrentBranch()
        if _branch == "master":
            return []
        return list(self.__git.iter_commits("master..{}".format(_branch)))[-1]

    def GetCommitSinceBranch(self, branch=None, master="master"):
        _branch = branch or self.GetCurrentBranch()
        if _branch == master:
            return []
        _commit = self.GetFirstBranchCommit(branch=_branch)
        _master_commits = self.GetAllBranchCommits(branch=master)
        _start = None
        for i in _commit.parents:
            if any([True for x in _master_commits if x.binsha == i.binsha]):
                _start = i.hexsha
                break
        if _start is not None:
            return self.GetUpstreamChangeSet(branch=master, start=_start)
        return []

    def GetPatchPathsFromCommit(self, commit):
        res = set()
        for x in self.__git.git.diff_tree("--no-commit-id", "--name-only", "-r", "{}".format(commit.hexsha)).split("\n"):
            res.add(x)
        return list(res)

    def GetCherryPickedCommit(self, commit, start, branch=None):
        _branch = branch or self.GetCurrentBranch()
        _end = self.GetCurrentRevision(_branch)
        for i in self.__git.iter_commits("{}..{}".format(start, _end)):
            if i.message == commit.message:
                return i
            if i.summary == commit.summary and \
                    self.GetPatchPathsFromCommit(i) == self.GetPatchPathsFromCommit(commit):
                return i
        return None

    def GetAllBranchCommits(self, branch=None):
        _branch = branch or self.GetCurrentBranch()
        return self.__git.iter_commits("{}".format(_branch))

    def GetUpstreamChangeSet(self, start=None, end=None, branch=None):
        _end = end or self.GetCurrentRevision(branch=branch)
        _start = start or _end
        return list(self.__git.iter_commits("{}..{}".format(_start, _end)))
