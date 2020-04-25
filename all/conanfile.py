from conans import ConanFile, CMake, tools
import os


class CgallastoolsConan(ConanFile):
    name = "cgal-lastools"
    version = "git"
    license = "LGPL"
    author = "Martin Isenburg"
    url = "https://github.com/JLight/CGAL-LAStools"
    description = "Fork is design to be lightweight and self-contained LASLib"
    # topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    exports_sources = "CMakeLists.txt"
    generators = "cmake"
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"
    _cmake = None

    def _configure_cmake(self):
        if not self._cmake:
            self._cmake = CMake(self)
            self._cmake.configure(build_folder=self._build_subfolder)
        return self._cmake

    def source(self):
        tools.get('https://github.com/J-Light/LAStools/archive/master.zip')
        os.rename('LAStools-master', self._source_subfolder)

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        tools.rmdir(os.path.join(self.package_folder, "lib", "cmake"))
        tools.rmdir(os.path.join(self.package_folder, "lib", "pkgconfig"))

    def package_info(self):
        self.cpp_info.includedirs = ['include/LASzip', 'include/LASlib']
        self.cpp_info.libs = ['las']
