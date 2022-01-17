# 17/01/2022
# SP - Script to genereate psp without NLCC in psp8 and upf format

import numpy as np
import os

elements = ['Ag','Al','Ar','As','At','Au','Ba','Be','B','Bi','Br',
'Ca','Cd','Ce','C','Cl','Co','Cr','Cs','Cu','Dy','Er','Eu','Fe',
'F','Ga','Gd','Ge','He','Hf','H','Hg',
'Ho','I','In','Ir','K','Kr','La','Li',
'Lu','Mg','Mn','Mo','Na','Nb','Nd','Ne',
'N','Ni','O','Os','Pb','Pd','P','Pm','Po','Pr','Pt',
'Rb','Re','Rh','Rn','Ru','Sb','Sc','Se',
'S','Si','Sm','Sn','Sr','Ta','Tb','Tc',
'Te','Ti','Tl','Tm','V','W','Xe','Yb',
'Y','Zn','Zr']

nb = len(elements)

# Update input files
#for ii in np.arange(100):
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/psp8/both/g\' '+str(elements[ii])+'.in && sed -i \'/icmod/{n;s/.*/0 0 0/}\' '+str(elements[ii])+'.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/psp8/both/g\' '+str(elements[ii])+'-sp.in && sed -i \'/icmod/{n;s/.*/0 0 0/}\' '+str(elements[ii])+'-sp.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/psp8/both/g\' '+str(elements[ii])+'-spd.in && sed -i \'/icmod/{n;s/.*/0 0 0/}\' '+str(elements[ii])+'-spd.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/psp8/both/g\' '+str(elements[ii])+'-fsp.in && sed -i \'/icmod/{n;s/.*/0 0 0/}\' '+str(elements[ii])+'-fsp.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/psp8/both/g\' '+str(elements[ii])+'-d.in && sed -i \'/icmod/{n;s/.*/0 0 0/}\' '+str(elements[ii])+'-d.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/psp8/both/g\' '+str(elements[ii])+'-low.in && sed -i \'/icmod/{n;s/.*/0 0 0/}\' '+str(elements[ii])+'-low.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/psp8/both/g\' '+str(elements[ii])+'-high.in && sed -i \'/icmod/{n;s/.*/0 0 0/}\' '+str(elements[ii])+'-high.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/psp8/both/g\' '+str(elements[ii])+'-sp-high.in && sed -i \'/icmod/{n;s/.*/0 0 0/}\' '+str(elements[ii])+'-sp-high.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/psp8/both/g\' '+str(elements[ii])+'-spd-high.in && sed -i \'/icmod/{n;s/.*/0 0 0/}\' '+str(elements[ii])+'-spd-high.in && cd ../')

# Run and copy
for ii in np.arange(nb):
    input = str(elements[ii])+'.in'
    output = str(elements[ii])+'.out'
    psp8 = str(elements[ii])+'.psp8'
    upf = str(elements[ii])+'.upf' 
    if (os.path.isfile(str(elements[ii])+'/'+input)):  
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/Dropbox/program/oncvpsp-3.3.0/src/oncvpsp.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )

for ii in np.arange(nb):
    input = str(elements[ii])+'-sp.in'
    output = str(elements[ii])+'-sp.out'
    psp8 = str(elements[ii])+'-sp.psp8'
    upf = str(elements[ii])+'-sp.upf'    
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/Dropbox/program/oncvpsp-3.3.0/src/oncvpsp.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )

for ii in np.arange(nb):
    input = str(elements[ii])+'-spd.in'
    output = str(elements[ii])+'-spd.out'
    psp8 = str(elements[ii])+'-spd.psp8'
    upf = str(elements[ii])+'-spd.upf'    
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/Dropbox/program/oncvpsp-3.3.0/src/oncvpsp.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )

for ii in np.arange(nb):
    input = str(elements[ii])+'-fsp.in'
    output = str(elements[ii])+'-fsp.out'
    psp8 = str(elements[ii])+'-fsp.psp8'
    upf = str(elements[ii])+'-fsp.upf'    
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/Dropbox/program/oncvpsp-3.3.0/src/oncvpsp.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )

for ii in np.arange(nb):
    input = str(elements[ii])+'-d.in'
    output = str(elements[ii])+'-d.out'
    psp8 = str(elements[ii])+'-d.psp8'
    upf = str(elements[ii])+'-d.upf'
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/Dropbox/program/oncvpsp-3.3.0/src/oncvpsp.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )
    
for ii in np.arange(nb):
    input = str(elements[ii])+'-low.in'
    output = str(elements[ii])+'-low.out'
    psp8 = str(elements[ii])+'-low.psp8'
    upf = str(elements[ii])+'-low.upf'    
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/Dropbox/program/oncvpsp-3.3.0/src/oncvpsp.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )

for ii in np.arange(nb):
    input = str(elements[ii])+'-high.in'
    output = str(elements[ii])+'-high.out'
    psp8 = str(elements[ii])+'-high.psp8'
    upf = str(elements[ii])+'-high.upf'    
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/Dropbox/program/oncvpsp-3.3.0/src/oncvpsp.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )


for ii in np.arange(nb):
    input = str(elements[ii])+'-sp-high.in'
    output = str(elements[ii])+'-sp-high.out'
    psp8 = str(elements[ii])+'-sp-high.psp8'
    upf = str(elements[ii])+'-sp-high.upf'    
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/Dropbox/program/oncvpsp-3.3.0/src/oncvpsp.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )


for ii in np.arange(nb):
    input = str(elements[ii])+'-spd-high.in'
    output = str(elements[ii])+'-spd-high.out'
    psp8 = str(elements[ii])+'-spd-high.psp8'
    upf = str(elements[ii])+'-spd-high.upf'    
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/Dropbox/program/oncvpsp-3.3.0/src/oncvpsp.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )





