def two_fer(*args):
    if(len(args) == 0):
        return "One for you, one for me.ex"
    else:
        return "One for " + args[0] + ", one for me." 
