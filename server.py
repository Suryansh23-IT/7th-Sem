import ctypes
from pathlib import Path
from omniORB import CORBA, PortableServer
import Temperature_idl

lib = ctypes.CDLL(str(Path(__file__).with_name('convert.dll' if __import__('os').name == 'nt' else 'convert.so')))
lib.c_to_f.argtypes = [ctypes.c_double]
lib.c_to_f.restype = ctypes.c_double
lib.f_to_c.argtypes = [ctypes.c_double]
lib.f_to_c.restype = ctypes.c_double

class Service(Temperature_idl._0_Temperature__POA.Temperature):
    def cToF(self, c): return lib.c_to_f(c)
    def fToC(self, f): return lib.f_to_c(f)

orb = CORBA.ORB_init([], CORBA.ORB_ID)
poa = orb.resolve_initial_references('RootPOA')
ref = Service()._this()
Path(__file__).with_name('server.ior').write_text(orb.object_to_string(ref))
poa._get_the_POAManager().activate()
print('CORBA server running...', flush=True)
orb.run()
