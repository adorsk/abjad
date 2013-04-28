from experimental.tools.scoremanagertools.proxies.DirectoryProxy import DirectoryProxy
import os


class ExgDirectoryProxy(DirectoryProxy):

    def __init__(self, score_package_name=None, session=None):
        path = os.path.join(self.configuration.scores_directory_path, score_package_name, 'exg')
        DirectoryProxy.__init__(self, path=path, session=session)
