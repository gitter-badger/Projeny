
import os
from mtm.ioc.Inject import Inject
from mtm.ioc.Inject import InjectMany
import mtm.ioc.IocAssertions as Assertions
from prj.reg.LocalFolderReleaseSource import LocalFolderReleaseSource
from mtm.util.Assert import *

class AssetStoreCacheReleaseSource:
    def __init__(self):
        unityUserRootFolder = os.path.join(os.getenv('APPDATA'), 'Unity')
        assetStoreCache1 = os.path.join(unityUserRootFolder, 'Asset Store')
        assetStoreCache2 = os.path.join(unityUserRootFolder, 'Asset Store-5.x')

        self._folderSources = [
            LocalFolderReleaseSource(assetStoreCache1), LocalFolderReleaseSource(assetStoreCache2)]

    @property
    def releases(self):
        result = []
        for subReg in self._folderSources:
            result += subReg.releases
        return result

    def init(self):
        for subReg in self._folderSources:
            subReg.init()

    def getName(self):
        return "Asset Store Cache"

    def installRelease(self, packageRoot, releaseInfo, forcedName):
        for subReg in self._folderSources:
            if releaseInfo in subReg.releases:
                return subReg.installRelease(packageRoot, releaseInfo, forcedName)

        assertThat(False)
