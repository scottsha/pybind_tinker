from conans import ConanFile, tools

class Cocoon(ConanFile):
    requires = \
        "boost/1.76.0", \
        "eigen/3.3.9", \
        "pybind11/2.7.1"
    #
    generators = "cmake_find_package"
    # default_options = {"poco:shared": True, "openssl:shared": True}

    def build(self):
        cmake = CMake(self) # it will find the packages by using our auto-generated FindXXX.cmake files
        cmake.configure()
        cmake.build()

    # def imports(self):
    #     self.copy("*.dll", dst="bin", src="bin") # From bin to bin
    #     self.copy("*.dylib*", dst="bin", src="library") # From library to bin