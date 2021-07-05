import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
from PIL import ImageFont, ImageDraw, Image
import arabic_reshaper
from bidi.algorithm import get_display
import integrate #front&back


def remove_newline(txt):
    txt_arr=txt.splitlines()
    res=""
    for i in txt_arr:
        if(i!=""):
            res=res+" "+i+" "
            
    return res


def form(front_path,back_path):
    integrate.front_read(front_path)
    integrate.back_read(back_path)
    name=remove_newline(integrate.name)
    id=integrate.IDNumber
    address=remove_newline(integrate.add)
    birthdata=integrate.BDate
    place_of_birth=integrate.govern
    gender=integrate.gender
    religion=integrate.religion
    social_status=integrate.a3zb
    husband_name="لا يوجد"#integrate.husband
    if(len(integrate.husband)>1):
        husband_name=integrate.husband
    job=integrate.job+" "+integrate.job2
    file1 = open("/home/mo/National-ID-card-reader/Data_saving.txt","a") 
    file1.write("\n\n")
    file1.write("الاسم :")
    file1.write(name)
    file1.write("  الرقم القومي : ")
    file1.write(id)
    file1.write("  العنوان : ")
    file1.write(address)
    file1.write("  تاريخ الميلاد :")
    file1.write(birthdata)
    file1.write("  محل الميلاد : ")
    file1.write(place_of_birth)
    file1.write("  المهنه :")
    file1.write(job)
    file1.write("  الجنس :")
    file1.write(gender)
    file1.write("  الديانه :")
    file1.write(religion)
    file1.write("  الحالة الاجتماعية :")
    file1.write(social_status)
    if not 'متزوجة' in social_status:
              file1.write("")   
    else:file1.write("  اسم الزوج  : "+husband_name)
    
    file1.close()  
  

