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

    print "Decompile {}".format(func.getName())

    return decomp_api.decompile(func)
    

try:
    sourceProgram = currentProgram
    sourceFunc = getFunctionContaining(currentAddress)

    sourcePseudocode = getPseudocode(sourceProgram, sourceFunc).split(u'\r\n')

    destProgram = askProgram("Program to diff")
    destFuncName = askString("Function to Diff", "", sourceFunc.getName())
    

    destFunc = None
    destFuncs = destProgram.getListing().getFunctions(True)

    for func in destFuncs:
        if func.getName() == destFuncName:
            destFunc = func
            break
    
    if destFunc == None:
        raise Exception("Function {} not found from {}".format(destFuncName, destProgram.getName()))

    destPseudocode = getPseudocode(destProgram, destFunc).split(u'\r\n')

    diff_html = askFile("Choose Path", "Save")

    if diff_html.exists() and askYesNo("Warning", "File {} already exists, want to overwrite?".format(diff_html.getName())):
        with open(diff_html.getAbsolutePath(), "w") as result:
            diff = difflib.HtmlDiff().make_file(sourcePseudocode, destPseudocode, context=False)
            result.write(diff)


except Exception as e:
    print str(e)
