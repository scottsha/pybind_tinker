#------------------------------#
#  Pythonic Layer
#------------------------------#
pybind11_add_module(
        pybindtinker
        pylayer.cpp
)

target_include_directories(pybindtinker PUBLIC ../src)

target_link_libraries(
        pybindtinker PUBLIC
        bindtinkertome
        pybind11::pybind11
)