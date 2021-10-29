# Requires conan.

pip uninstall pybindtinker -y; pip install .; pip show -f pybindtinker; python -c "import sys; sys.path.insert(0, '/home/scott/Programs/pybind_tinker/cmake-build-release/lib'); import pybindtinker; print(pybindtinker.hi())"