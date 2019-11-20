from ensurecvs.classes.CVS_git import CVSgit


class CVSHelper(object):
    @staticmethod
    def GetCVS(localdir):
        return CVSgit(localdir)
