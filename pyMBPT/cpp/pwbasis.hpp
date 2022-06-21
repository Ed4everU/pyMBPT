#ifndef PYMBPT_PWBASIS
#define PYMBPT_PWBASIS

#include <boost/python.hpp>


class PWbasis
{
    PWbasis()
    {
        
    }
}




boost::python::BOOST_PYTHON_MODULE(PWbasis)
{
    class_<PWbasis>("PWbasis")
    .def()
}

#endif // PYMBPT_PWBASIS