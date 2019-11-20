import json
import os
import re

from ensurecvs.configs.keywords_base import KEYWORDS_BASE
from ensurecvs.configs.extension_base import EXTENSION_BASE


class IssueFinder(object):
    def __init__(self, useDefaultFilter=True, filterLists=[]):
        super().__init__()
        self.__filterLists = []
        if useDefaultFilter:
            self.__filterLists += KEYWORDS_BASE
        for fil in filterLists:
            try:
                with open(os.path.join(fil)) as i:
                    self.__filterLists += json.load(i)
            except Exception as e:
                print(str(e))

    def __containsValidFile(self, cvs, commit):
        _cfiles = cvs.GetPatchPathsFromCommit(commit)
        ignorable = True
        for f in _cfiles:
            ignorable &= any([f.endswith(x) for x in EXTENSION_BASE])
        return not ignorable

    def __classifyCommitMessage(self, message):
        __hits = {k: 0 for k in KEYWORDS_BASE.keys()}
        for k, v in KEYWORDS_BASE.items():
            for word in v:
                if re.search(word, message, re.IGNORECASE):
                    __hits[k] += 1
        return [k for k, v in __hits.items() if v == __hits[max(__hits, key=__hits.get)]]

    def GetIssues(self, csv, commit_list):
        res = []
        for commit in commit_list:
            if not self.__containsValidFile(csv, commit):
                continue
            if self.__classifyCommitMessage(commit.message) in [["corrective"], ["corrective", "streamline"], ["corrective", "management"]]:
                res.append(commit)
        return res
