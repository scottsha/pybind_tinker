#include "pybind11.h"
#include "eigen.h"

#include "eigen_mat_math.h"

namespace py = pybind11;

PYBIND11_MODULE(pybindtinker, bindtinker_module) {
    bindtinker_module.doc() = "pybind11 example plugin";
    bindtinker_module.def("resolvent", &resolvent, "Add identity then invert the matrix");
}