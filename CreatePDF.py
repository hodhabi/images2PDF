#This Python script creates PDF files from a large number of images.
#The images are taken after a construction project to show areas
#that require desnagging.  Issues include painting, flooring, 
#power sockt installation and many other issues
#A PDF file is create for each floor and issue
#An HTML code is generated to link the produced PDF files

import pandas as pd 
import img2pdf 
from PIL import Image 
import os 
import glob
from fpdf import FPDF
import os.path
from os import path


#Reading an excel file that includes records for each image
#The columns are filename, Floor, Issue, and fe more columns
snag = pd.read_excel("SnaggingList_floor1_G.xlsx")
issue = snag.Issue.unique()

floor = snag["Floor"].unique()

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

