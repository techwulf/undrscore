import subprocess
path = '/home/techwulf/Projects/Cabal-Syndicate/DeepMagic/source/deepmagic/dom/elements'

def getdirs(dir):
    direct_output = str(subprocess.check_output(['ls ' + dir], \
            shell=True))[2:-3].replace('\\npackage.d','').split('\\n')

    return direct_output

out = getdirs(path)

for i in out:
    curdir = path + '/' + i +'/'
    out = getdirs(curdir)
    module = 'deepmagic.dom.elements.' + i + '.'

    for j in out:
        file = j.replace('element.d', '_element.d')
        mfile = file.replace('.d','')
        jfile = j.replace('.d','')

        print (curdir+j)

        if j != file:
            subprocess.call(['mv', curdir+j, curdir+file])

        fcontent = open(curdir+file)
        newcontent = fcontent.read()
        newcontent = newcontent.replace(module+jfile, module+mfile)
        fcontent = open(curdir+file,'w')

        fcontent.write(newcontent)
        fcontent.close()

        package = open(curdir+"package.d")
        pcontent = package.read() 
        pcontent = pcontent.replace(module+jfile, module+mfile)
        package = open(curdir+'package.d','w')

        package.write(pcontent)
        package.close()

        

    #print (out, '\n')


    
#print (out)
