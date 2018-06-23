import lldb

def reverse(debugger, command, result, internal_dict):
    target = debugger.GetSelectedTarget()
    if target:
        ret = "FT_" + str(target)[::-1]
        print(ret)
    else:
        print("No target currently selected")

def __lldb_init_module(debugger, internal_dict):
    lldb.debugger.HandleCommand('command script add -f reverse.reverse reverse')
    print 'The reverse command is now ready to use'
