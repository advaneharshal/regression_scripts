## Author : advaneharshal
## This script is used for filtering out the 
## srand failures as per the Error signatures
## and convert the same into output.csv file 
## which can be open in  Excel sheet for tracking 
## CMD : To be run in srand path dir
## CMD : python filter_failure.py 


import os
import subprocess
import re
import csv
def listToString(s):
   
    # initialize an empty string
    str1 = " "
   
    # return string 
    return (str1.join(s))


first_err =[]
final_dict = {'Testcase_name':'Error signature'}
file_dict = {'tc_name': 'err_sign'} 
stream = os.popen('ls failures/')
#print("%s"%stream)
out = stream.read()
out = out.split("\n")
print(" %s"%out)
for n in range(len(out)):
   print (n)
   cmd = ["grep", "-R", "%E", "failures/%s/logfile"%out[n]]
  
   #list1 = ['H','my','name','is']
   #cmd = "grep -R %E failures/%s/logfile" %(out)
   cmd_exe = " "
   cmd_exe=listToString(cmd)
   print (" cmd to be exe  %s" %(cmd_exe))
   stream = os.popen(cmd_exe)
   err_sign = stream.read()
   #print(" error signature %s" %err_sign)
   split_string = "%E-"
   err_sign = err_sign.split('%E')
   print(" error signaturelist %d %s" %(len(err_sign),err_sign))
   if len(err_sign)<2:
      print (" Not error reported ")
      #final_dict.update([(out[n],first_err[n])])
      first_err.append(listToString(err_act))
   else:
      err_act = err_sign[1].split()
      err_act = err_act[1:]
      first_err.append(listToString(err_act))
      print(" error actual %s %d" %(first_err,len(first_err)))
      print (" tc_name: %s error: %s"%(out[n],first_err[n]))
      final_dict.update([(out[n],first_err[n])])

print (final_dict)
flip = {}
for key,value in final_dict.items():
   #print (final_final_dict[key])
   if value not in flip:
      flip[value] = [key]
   else:
      flip[value].append(key)

for key,value  in flip.items():
   print (" %s  %s"%(key,value))

with open('output.csv', 'w') as output:
    writer = csv.writer(output)
    for key, value in flip.items():
        writer.writerow([key, value])


#os.popen('gvim mylog')
