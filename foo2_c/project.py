import os
import subprocess

from sipbuild import Project

class FooProject(Project):
    def _build_foo(self):
        cwd = os.path.abspath('foo')
        build_dir = os.path.join(cwd,"build")
        os.makedirs(build_dir,exist_ok=True)
        subprocess.run(['cmake','..'], cwd=build_dir, capture_output=True, check=True)              # configure
        subprocess.run(['cmake','--build',build_dir], cwd=cwd, capture_output=True, check=True)     # build

    def build(self):        # sip-build
        self._build_foo()
        super().build()

    def build_sdist(self, sdist_directory): # sip-sdist
        self._build_foo()
        return super().build_sdist(sdist_directory)

    def build_wheel(self, wheel_directory): # sip-wheel
        self._build_foo()
        return super().build_wheel(wheel_directory)

    def install(self): # sip-install
        self._build_foo()
        super().install()