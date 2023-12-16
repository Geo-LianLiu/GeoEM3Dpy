## GeoEM3Dpy: A python package for 3D geophysical electromagnetic (GeoEM) simulation and data inversion


- MT3DFD

  A python module for 3D Magnetotelluric (MT) forward simulation and data inversion based on the finite difference (FD) method

- DC3DFD

  A python module for 3D Direct Current resistivity (DC) forward simulation and data inversion based on the finite difference (FD) method

- CSEM3DFD

  A python module for 3D Controlled Source ElectroMagnetic forward simulation and data inversion based on the finite difference (FD) method

- Magnetic3D

  A python module for 3D Magnetic forward simulation and data inversion based on the rectilinear grid

- Gravity3D
  
  A python module for 3D Gravity forward simulation and data inversion based on the rectilinear grid




## Install
- Install Anaconda and create a new environment

  wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh

  `bash Anaconda3-2023.09-0-Linux-x86_64.sh`

  `conda create -n GeoEM3Dpy python=3.10`

- Install TensorFlow

  `conda install -c main tensorflow==2.11 or conda install tensorflow==2.11`

  `conda install mpi4py matplotlib`

  `pip install psutil pyevtk`

- Install GeoEM3Dpy
  
  `python setup.py build`
  `python setup.py install`

  or 

  `python setup.py build install`


### To do
- TEM3DFD

- Joint inversion
