from pathlib import Path
from omniORB import CORBA
import Temperature_idl

orb = CORBA.ORB_init([], CORBA.ORB_ID)
obj = orb.string_to_object(Path(__file__).with_name('server.ior').read_text())
remote = obj._narrow(Temperature_idl._0_Temperature.Temperature)
if remote is None: raise RuntimeError('CORBA service unavailable')
while True:
    print('\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Exit')
    choice = input('Choose option: ').strip()
    if choice == '3': break
    if choice not in ('1', '2'):
        print('Invalid option'); continue
    try: value = float(input('Enter temperature: '))
    except ValueError:
        print('Invalid temperature'); continue
    result = remote.cToF(value) if choice == '1' else remote.fToC(value)
    print(f'Result: {result:.2f} {"F" if choice == "1" else "C"}')
orb.destroy()
