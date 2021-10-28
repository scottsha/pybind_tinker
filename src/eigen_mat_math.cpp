#include "eigen_mat_math.h"

Eigen::MatrixXd resolvent(const Eigen::MatrixXd& x, const double& lambda) {
    Eigen::MatrixXd id = Eigen::MatrixXd::Identity(x.rows(), x.cols());
    Eigen::MatrixXd res = (x - lambda * id).inverse();
    return res;
}
