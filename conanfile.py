#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostSmart_PtrConan(base.BoostBaseConan):
    name = "boost_smart_ptr"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-boost_smart_ptr"
    lib_short_names = ["smart_ptr"]
    header_only_libs = ["smart_ptr"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_move",
        "boost_predef",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_type_traits"
    ]


