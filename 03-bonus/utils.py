import lldb
import commands

def ls(debugger, command, result, internal_dict):
    print >>result, (commands.getoutput('/bin/ls %s' % command))

def pwd(debugger, command, result, internal_dict):
    print >>result, (commands.getoutput('/bin/pwd'))

def cd(debugger, command, result, internal_dict):
    lldb.debugger.HandleCommand('platform settings -w %s' % command)

def rebuild(debugger, command, result, internal_dict):
    target = debugger.GetSelectedTarget()
    print >>result, (commands.getoutput('/usr/bin/make %s' % command))
    lldb.debugger.HandleCommand('file %s' % target)

def __lldb_init_module(debugger, internal_dict):
    lldb.debugger.HandleCommand('command script add -f utils.ls ls')
    print 'The ls command is now ready to use'
    lldb.debugger.HandleCommand('command script add -f utils.cd cd')
    print 'The cd command is now ready to use'
    lldb.debugger.HandleCommand('command script add -f utils.pwd pwd')
    print 'The pwd command is now ready to use'
    lldb.debugger.HandleCommand('command script add -f utils.rebuild rebuild')
    print 'The rebuild command is now ready to use'
