cmake_minimum_required(VERSION 3.20)
project(bindtinker)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR} ${CMAKE_MODULE_PATH})

#------------------------------#
#    SETUP CONAN
#------------------------------#
if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
    message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
    file(DOWNLOAD "https://raw.githubusercontent.com/conan-io/cmake-conan/master/conan.cmake"
            "${CMAKE_BINARY_DIR}/conan.cmake")
endif()
include(${CMAKE_BINARY_DIR}/conan.cmake)

conan_cmake_run(CONANFILE conanfile.py
        BASIC_SETUP TARGETS
        BUILD missing)

#------------------------------#
#    FIND PACKAGES
#------------------------------#
find_package(Boost REQUIRED)
if (TARGET Boost::Boost)
    message(STATUS "Found boost target")
else()
    message(STATUS "Could not find boost target")
endif()

find_package(Eigen3 REQUIRED)
if (TARGET Eigen3::Eigen3)
    message(STATUS "Found Eigen3 target")
else()
    message(STATUS "Could not find Eigen3 target")
endif()

find_package(pybind11 REQUIRED)
if (TARGET pybind11::pybind11)
    message(STATUS "Found pybind11 target")
else()
    message(STATUS "Could not find pybind11 target")
endif()

#------------------------------#
#    Build Core Libraries
#------------------------------#
add_subdirectory(src)

#------------------------------#
#    PYTHON BINDING
#------------------------------#
add_subdirectory(pybinding_src)