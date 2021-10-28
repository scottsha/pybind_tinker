add_library(
        bindtinkertome
        eigen_mat_math.cpp
        eigen_mat_math.h
)

target_link_libraries(
        bindtinkertome PUBLIC
        Boost::Boost
        Eigen3::Eigen3
)
