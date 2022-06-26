__global__ void cu3phsr(double *****fc3rd, double *mass, double **mesh, int iq1, double **eigVal, cuDoubleComplex ***eigVec)
{
    // fc3rd  (natom_in_uc, n_neigh_atom, 3, 3, 3)
    // eigVal (nq, nmode)
    // eigVec (nq, nmode, nmode)


    size_t iq2 = blockIdx.x;

    size_t imod1 = threadIdx.x;
    size_t imod2 = threadIdx.y;
    size_t imod3 = threadIdx.z;

}

