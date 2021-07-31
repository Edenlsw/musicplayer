from ui.interface import Interface, ConsoleIO
import subprocess

interface = Interface(ConsoleIO(), subprocess)
interface.run()
