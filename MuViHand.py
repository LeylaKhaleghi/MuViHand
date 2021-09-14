#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: leyla Khaleghi

----------------------------
MuVIHand Dataset
---------------------

"""
import os
import json
# import numpy as np



# Root folder
main_path  = '/home/MuViHand/'
# Subjects
subject_ = [ '03', '04', '05' ,'06' , '07' , '08' , '09'  ]
#
Enviroment = ['E1', 'E2' ]
# Light
light = ['Sun', 'Point light']
# This refer to the type of the hand that you want to use.
# Data_hand_type ='Left_Hand'
Data_hand_type ='Right_Hand'


img_path = []

pose3d_array= []
pose2d_array= []


e= 0

for subject in subject_:
    print(subject)
    e=0
    for e_ in Enviroment:
        print(e_)
        e=e+1
        if (e_=='E1'):
            activity = ['01', '02', '03', '04', '05' ,'06' , '07' , '08' ]
            length_activity = ['95', '95', '95','85', '115' , '75' , '75' , '80']
        else : 
          activity = ['01', '02', '03', '04', '05' ,'06' , '07' , '08' , '09', '10', '11'  ]
          length_activity = ['80', '75', '100','75', '100' , '100' , '75' , '75', '80' , '120' , '80']

        a=0
        for a_ in activity:
            a=a+1 
            l= 1
            path = main_path +'Subject.'+ subject +  '/' + e_  + '/' + a_+ '/' + light[l-1]
            
            os.chdir(path)
            
            # fixed cameras
            # camera = ['Camera.01' , 'Camera.02' , 'Camera.03' , 'Camera.04' , 'Camera.05' , 'Camera.06']
            # Right Hand  Tracking cameras
            cameras = ['Camera.11' , 'Camera.12' , 'Camera.13']
            # Left Hand  Tracking cameras
            # cameras = ['Camera.14' , 'Camera.15' , 'Camera.16']
            
            

                
            for i in cameras:
                                 
                path_cam = path +'/' + i + '/'
                
                
                for count in range(int(length_activity[a-1])):
                    
                
                    if (a<10):
                        filename_img = path_cam +'S'+ subject +'_E' + str(e) +'_A' + '0' + str (a) +'_L' + str(l) +'_C'+ i[7]+ i[8]+ '_F' + str(count+1) + '.jpg'
                    
                    if (a>9):
                        filename_img = path_cam +'S'+ subject +'_E' + str(e) +'_A' + str (a) +'_L' + str(l) +'_C'+ i[7]+ i[8]+ '_F' + str(count+1) + '.jpg'
                   
                        
                    img_path.append(filename_img)
                
                
                if (a<10):
                        filename_3d = path_cam +'S'+ subject +'_E' + str(e) +'_A' + '0' + str (a) +'_L' + str(l) +'_C'+ i[7]+ i[8]+ '_'+Data_hand_type+ '.json'
                        filename_2d = path_cam +'S'+ subject +'_E' + str(e) +'_A' + '0' + str (a) +'_L' + str(l) +'_C'+ i[7]+ i[8]+ '_' 'Pixel'+ '_' +Data_hand_type+ '.json'
                    
                if (a>9):
                        filename_3d = path_cam +'S'+ subject +'_E' + str(e) +'_A' + str (a) +'_L' + str(l) +'_C'+ i[7]+ i[8]+ '_'+Data_hand_type+ '.json'
                        filename_2d = path_cam +'S'+ subject +'_E' + str(e) +'_A' + str (a) +'_L' + str(l) +'_C'+ i[7]+ i[8]+ '_' 'Pixel'+ '_' +Data_hand_type+ '.json'
                        
                with open(filename_3d) as json_file_3d:
                    right_3d = json.load(json_file_3d)
                    
                pose3d_array.extend(right_3d)
                
                with open(filename_2d) as json_file_2d:
                    right_2d = json.load(json_file_2d)
                    
                pose2d_array.extend(right_2d)
                
                
                # print(filename_3d)
                # print(filename_2d)
                
                
            l= 2
            path = '/home/leyla/Subject.'+ subject +  '/' + e_  + '/' + a_ + '/' + light[l-1]
            
            os.chdir(path)
                
       
            
                
            for i in cameras:
            
                                                
                path_cam = path +'/' + i + '/'
                
                
                for count in range(int(length_activity[a-1])):
                    
                
                    if (a<10):
                        filename_img_p = path_cam +'S'+ subject +'_E' + str(e) +'_A' + '0' + str (a) +'_L' + str(l) +'_C'+ i[7]+ i[8]+ '_F' + str(count+1) + '.jpg'
                    
                    if (a>9):
                        filename_img_p = path_cam +'S'+ subject +'_E' + str(e) +'_A' + str (a) +'_L' + str(l) +'_C'+ i[7]+ i[8]+ '_F' + str(count+1) + '.jpg'
                   
                        
                    img_path.append(filename_img_p)
                
                
                if (a<10):
                        filename_3d_p = path_cam +'S'+ subject +'_E' + str(e) +'_A' + '0' + str (a) +'_L' + str(l) +'_C'+ i[7]+ i[8]+ '_'+Data_hand_type+ '.json'
                        filename_2d_p = path_cam +'S'+ subject +'_E' + str(e) +'_A' + '0' + str (a) +'_L' + str(l) +'_C'+ i[7]+ i[8]+ '_' 'Pixel'+ '_' +Data_hand_type+ '.json'
                    
                if (a>9):
                        filename_3d_p = path_cam +'S'+ subject +'_E' + str(e) +'_A' + str (a) +'_L' + str(l) +'_C'+ i[7]+ i[8]+ '_'+Data_hand_type+ '.json'
                        filename_2d_p = path_cam +'S'+ subject +'_E' + str(e) +'_A' + str (a) +'_L' + str(l) +'_C'+ i[7]+ i[8]+ '_' 'Pixel'+ '_' +Data_hand_type+ '.json'
                        
                with open(filename_3d_p) as json_file_3d_p:
                    right_3d_p = json.load(json_file_3d_p)
                    
                pose3d_array.extend(right_3d_p)
                
                with open(filename_2d_p) as json_file_2d_p:
                    right_2d_p = json.load(json_file_2d_p)
                    
                pose2d_array.extend(right_2d_p)
                


