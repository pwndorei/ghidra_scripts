#Simple Pseudo-code Diffing script
#@author pwndorei
#@category Diff
#@keybinding 
#@menupath
#@toolbar


#TODO Add User Code Here

import difflib
from ghidra.app.decompiler.flatapi import FlatDecompilerAPI
from ghidra.program.flatapi import FlatProgramAPI


def getPseudocode(prog, func):
    prog_api = FlatProgramAPI(prog)
    decomp_api = FlatDecompilerAPI(prog_api)
    
    if isinstance(func, unicode):
        funcName = func
        func = prog_api.getFunction(funcName)
        if func == None:
            raise Exception("Function {} not found".format(funcName))

    print "Decompile {}".format(func.getName())

    return decomp_api.decompile(func)
    

try:
    sourceProgram = currentProgram
    sourceFunc = getFunctionContaining(currentAddress)

    sourcePseudocode = getPseudocode(sourceProgram, sourceFunc).split(u'\r\n')

    destProgram = askProgram("Program to diff")
    destFuncName = askString("Function to Diff", "", sourceFunc.getName())
    
    destPseudocode = getPseudocode(destProgram, destFuncName).split(u'\r\n')

    diff_html = askFile("Choose Path", "Save")

    if diff_html.exists() and (not askYesNo("Warning", "File {} already exists, want to overwrite?".format(diff_html.getName()))):
        raise Exception("Save cancelled")
        
    with open(diff_html.getAbsolutePath(), "w") as result:
        diff = difflib.HtmlDiff().make_file(sourcePseudocode, destPseudocode, context=False)
        result.write(diff)


except Exception as e:
    print str(e)
