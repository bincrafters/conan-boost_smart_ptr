from conans import ConanFile, tools, os

class BoostSmart_PtrConan(ConanFile):
    name = "Boost.Smart_Ptr"
    version = "1.64.0"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-smart_ptr"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["smart_ptr"]
    requires =  "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Move/1.64.0@bincrafters/testing", \
                      "Boost.Predef/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing", \
                      "Boost.Throw_Exception/1.64.0@bincrafters/testing"
 
    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()