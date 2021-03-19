import pandas as pd 
import img2pdf 
from PIL import Image 
import os 
import glob
from fpdf import FPDF
import os.path
from os import path

snag = pd.read_excel("SnaggingList_floor2_3.xlsx")
issue = snag.Issue.unique()

print("<html>")
print("<head><head>")
print("<body>")

for f in floor:
    print("<b>Floor: " + str(f) + "</b>")
    print("<ul>")
    m = 0
    fsnag = snag[snag.Floor==f]
    issue = fsnag.Issue.unique()
    converted_list = []
    for i in issue:
        converted_list.append(i.strip())
    issue = converted_list

    for i in issue:
        pdf = FPDF()
        c_snag = snag[(snag.Issue == i) & (snag.Floor == f)]
        groupimages = c_snag.FileName
        for image in groupimages:
            if(path.exists(image)):
                pdf.add_page()
                pdf.image(image,10,20,150,150)
                pdf.set_font('helvetica', size=12)
                pdf.cell(w=0, txt=image)
                m = m + 1
        if(m>0):
            i2 = i.replace(" ","")
            newfile = 'pdf/'+str(f)+"_"+i2+".pdf"
            htmlfile = str(f)+"_"+i2+".pdf"
            pdf.output(newfile, "F")
            print("<li><a href='" + htmlfile +"'>" + htmlfile +"</a></li>")
    print("</ul>")
print("</body>")
print("</html>")
print("Done .............")

