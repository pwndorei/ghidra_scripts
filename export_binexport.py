#@category FunctionID
#@menupath Tools.BinExport.Export

from com.google.security import binexport
import java.io.File as File

addr_set = currentProgram.getMemory()
f = File(currentProgram.getName() + '.BinExport')
exporter = binexport.BinExportExporter() # Binary BinExport (v2) for BinDiff
exporter.export(f, currentProgram, addr_set, monitor)

