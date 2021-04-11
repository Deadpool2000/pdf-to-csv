import tabula
import os
import sys


print("""

>>>>>>>>    PDF to CSV converter    <<<<<<<<

              By Deadpool2000



Note - make sure your pdf files are stored in 'PDF' folder.

-----------------------------------------------------------

""")
try:
    mainpath=os.path.dirname(os.path.abspath(sys.argv[0]))
    path=mainpath+"/PDF/"
    savepath=mainpath+"/output/"
    os.mkdir(path)
    os.mkdir(savepath)
    a=[]
    val=0
    ent=os.listdir(path)
    for en in ent:
        a.append(en)
    for i in range(len(a)):
        print("Converting",a[val],".......")
        fname= path+a[val]
        out= savepath+a[val]+".csv"
        tabula.convert_into(fname, out, output_format="csv", stream=True, pages='all')
        print("\nFile '"+a[val]+".csv' saved.")
        val+=1
except:
    print("Something went wrong! Please try again!")

