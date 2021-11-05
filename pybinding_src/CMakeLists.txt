#------------------------------#
#  Pythonic Layer
#------------------------------#
pybind11_add_module(
        pybindtinkerlib
        pylayer.cpp
)

target_include_directories(pybindtinkerlib PUBLIC ../src)

target_link_libraries(
        pybindtinkerlib PUBLIC
        bindtinkertome
        pybind11::pybind11
)

#set_target_properties (
#        pybindtinkerlib PROPERTIES
#        RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/pybindtinker"
#)

add_custom_command(TARGET pybindtinkerlib POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:pybindtinkerlib> ${CMAKE_SOURCE_DIR}/pybindtinker
        )