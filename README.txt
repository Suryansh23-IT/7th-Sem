Q4 - Simple CORBA Temperature Converter (C + Python)

4 handwritten source files:
  temperature.idl  CORBA remote interface
  convert.c        Temperature math implemented in C
  server.py        Genuine omniORB CORBA server, using the C library
  client.py        Genuine omniORB CORBA client

Important: the CORBA server is PYTHON, not C; it calls compiled C functions.
This shows C and Python integration using CORBA but is NOT a native C CORBA server.
No pure C CORBA server is provided.

Requirements: omniORBpy + omniidl, Python (matching the omniORBpy build), GCC.
These are external requirements. Unlike plain sockets, CORBA CANNOT run without middleware.

Once omniORBpy/omniidl is correctly installed and both commands are on PATH:
  omniidl -bpython temperature.idl
  gcc -shared -o convert.dll convert.c   (Windows MinGW)
  python server.py                       (first PowerShell terminal)
  python client.py                       (second PowerShell terminal)

Ubuntu alternative (if you choose to use it):
  sudo apt install python3-omniorb omniidl gcc
  omniidl -bpython temperature.idl
  gcc -shared -fPIC -o convert.so convert.c
  python3 server.py
  python3 client.py

Actual CORBA client/server run has NOT been verified in this environment.
C library and Python syntax are checked; you must install compatible omniORBpy to run.
