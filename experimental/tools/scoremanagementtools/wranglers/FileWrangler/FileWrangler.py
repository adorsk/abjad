from abjad.tools import iotools
from experimental.tools.scoremanagementtools.proxies.FileProxy import FileProxy
from experimental.tools.scoremanagementtools.wranglers.AssetWrangler import AssetWrangler
import os


class FileWrangler(AssetWrangler):

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def asset_class(self):
        return FileProxy