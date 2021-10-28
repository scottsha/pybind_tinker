import sys
sys.path.insert(0, '/home/scott/Programs/pybind_tinker/cmake-build-debug/lib')
import pybindtinker
import numpy as np

RR = pybindtinker.resolvent(np.identity(2), 1.2)
print(RR)

expect_RR = np.array([[-5., -0.],[-0.,-5.]])
assert np.linalg.norm(RR - expect_RR) < 1e-10